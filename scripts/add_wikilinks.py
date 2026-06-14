#!/usr/bin/env python3
"""
Add wikilinks to entity files - optimized version.

Strategy:
1. Build a regex of all author last names (the most common linkable term)
2. For each entity, run a single regex pass to find all author mentions
3. Resolve ambiguity when multiple entities share a last name (pick the
   most common one or the one matching the year in context)
"""

import os
import re
import json
from collections import defaultdict, Counter

ENTITIES_DIR = "departments/engineering/research/worrydream-wiki/entities"


def load_titles():
    """Load slug -> (authors_str, year, title) from frontmatter."""
    slug_to_info = {}
    author_to_slugs = defaultdict(list)  # lastname (lowercase) -> [slugs]

    for f in sorted(os.listdir(ENTITIES_DIR)):
        if not f.endswith(".md"):
            continue
        slug = f[:-3]
        with open(os.path.join(ENTITIES_DIR, f), 'r') as fh:
            content = fh.read()

        title_match = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', content, re.MULTILINE)
        title = title_match.group(1) if title_match else slug

        # Parse "Author YEAR - Title" or "Author1 & Author2 YEAR - Title"
        tmatch = re.match(r'^(.+?)\s+(\d{4})\s*[-–—]\s*(.+)$', title)
        if tmatch:
            author_str = tmatch.group(1)
            year = tmatch.group(2)
            paper_title = tmatch.group(3).strip()
        else:
            author_str = slug.split("-")[0].title()
            year = slug.split("-")[1] if len(slug.split("-")) > 1 else ""
            paper_title = title

        # Extract all author last names
        # Handle "Smith & Jones", "Smith-Jones", "Smith, Jones", "Smith/Jones"
        authors = re.split(r'\s+(?:&|and)\s+|\s*,\s+|\s*/\s+|\s*-\s*(?=[A-Z][a-z])', author_str)
        lastnames = []
        for a in authors:
            a = a.strip()
            if not a:
                continue
            # "Allen-Conn" -> ["Allen", "Conn"]
            # "Mead" -> ["Mead"]
            # "Nelson P" -> ["Nelson"] (skip initials)
            for p in re.split(r'[-\s]', a):
                # Skip single-letter initials
                if p and len(p) > 1:
                    lastnames.append(p)
                    author_to_slugs[p.lower()].append(slug)

        slug_to_info[slug] = {
            "authors": author_str,
            "lastnames": lastnames,
            "year": year,
            "title": paper_title,
        }

    return slug_to_info, author_to_slugs


def split_content(content):
    """Split into frontmatter and body. Extract code blocks as placeholders."""
    # Frontmatter
    if content.startswith("---"):
        end = content.find("---", 3)
        if end != -1:
            frontmatter = content[:end + 3]
            body = content[end + 3:]
        else:
            frontmatter = ""
            body = content
    else:
        frontmatter = ""
        body = content

    # Extract fenced code blocks
    code_blocks = []
    def replace_code(m):
        idx = len(code_blocks)
        code_blocks.append(m.group(0))
        return f"\x00CB{idx}\x00"
    body = re.sub(r'```.*?```', replace_code, body, flags=re.DOTALL)

    # Extract inline code
    inline_codes = []
    def replace_inline(m):
        idx = len(inline_codes)
        inline_codes.append(m.group(0))
        return f"\x00IC{idx}\x00"
    body = re.sub(r'`[^`\n]+`', replace_inline, body)

    # Extract existing wikilinks (don't touch)
    wikilinks = []
    def replace_wl(m):
        idx = len(wikilinks)
        wikilinks.append(m.group(0))
        return f"\x00WL{idx}\x00"
    body = re.sub(r'\[\[[^\]]+\]\]', replace_wl, body)

    # Extract markdown links [text](url)
    mdlinks = []
    def replace_ml(m):
        idx = len(mdlinks)
        mdlinks.append(m.group(0))
        return f"\x00ML{idx}\x00"
    body = re.sub(r'\[[^\]]+\]\([^)]+\)', replace_ml, body)

    return frontmatter, body, code_blocks, inline_codes, wikilinks, mdlinks


def restore_placeholders(body, code_blocks, inline_codes, wikilinks, mdlinks):
    """Restore all placeholders back to their original content."""
    for i, block in enumerate(code_blocks):
        body = body.replace(f"\x00CB{i}\x00", block)
    for i, block in enumerate(inline_codes):
        body = body.replace(f"\x00IC{i}\x00", block)
    for i, block in enumerate(wikilinks):
        body = body.replace(f"\x00WL{i}\x00", block)
    for i, block in enumerate(mdlinks):
        body = body.replace(f"\x00ML{i}\x00", block)
    return body


def add_wikilinks_to_entity(slug, content, slug_to_info, author_to_slugs):
    """Add [[wikilinks]] to a single entity file."""
    frontmatter, body, code_blocks, inline_codes, wikilinks, mdlinks = split_content(content)

    current_info = slug_to_info[slug]
    current_lastnames = set(n.lower() for n in current_info["lastnames"])

    # Build a master regex of all author last names (longest first to prefer
    # longer matches, e.g., "Allen-Conn" before "Allen")
    all_lastnames = list(author_to_slugs.keys())
    all_lastnames.sort(key=len, reverse=True)

    # Escape each name and join with |
    pattern_str = r'\b(' + '|'.join(re.escape(name) for name in all_lastnames) + r')\b'
    # Use case-insensitive matching but preserve original case
    pattern = re.compile(pattern_str, re.IGNORECASE)

    links_added = 0

    def replace_match(m):
        nonlocal links_added
        matched = m.group(1)
        pos = m.start()
        matched_lower = matched.lower()

        candidates = author_to_slugs[matched_lower]

        # Skip self-references
        candidates = [s for s in candidates if s != slug]
        if not candidates:
            return matched

        # Disambiguate: if multiple candidates, try to find a year near the match
        if len(candidates) > 1:
            # Look for 4-digit year within 200 chars
            context = body[max(0, pos - 100):min(len(body), pos + 200)]
            year_match = re.search(r'\b(19\d{2}|20\d{2})\b', context)
            if year_match:
                year = year_match.group(1)
                for c in candidates:
                    if slug_to_info[c]["year"] == year:
                        candidates = [c]
                        break
            # If still ambiguous, pick the one with most cross-references
            if len(candidates) > 1:
                # Default to first (alphabetically)
                candidates = [sorted(candidates)[0]]

        target_slug = candidates[0]

        # Preserve original casing
        original_case = matched
        # Capitalize first letter to match style
        replacement = f"[[{target_slug}|{original_case}]]"
        links_added += 1
        return replacement

    # Apply replacement
    new_body = pattern.sub(replace_match, body)

    # Restore all placeholders
    new_body = restore_placeholders(new_body, code_blocks, inline_codes, wikilinks, mdlinks)

    new_content = frontmatter + new_body
    return new_content, links_added


def main():
    print("Loading entity metadata...")
    slug_to_info, author_to_slugs = load_titles()
    print(f"  {len(slug_to_info)} entities")
    print(f"  {len(author_to_slugs)} unique author last names")

    total_links = 0
    files_modified = 0
    stats = []

    for i, slug in enumerate(sorted(slug_to_info.keys())):
        if i % 50 == 0:
            print(f"  Processing {i+1}/{len(slug_to_info)}...")

        filepath = os.path.join(ENTITIES_DIR, slug + ".md")
        with open(filepath, 'r') as f:
            content = f.read()

        new_content, links_added = add_wikilinks_to_entity(slug, content, slug_to_info, author_to_slugs)

        if links_added > 0:
            with open(filepath, 'w') as f:
                f.write(new_content)
            files_modified += 1
            total_links += links_added
            stats.append((slug, links_added))

    stats.sort(key=lambda x: -x[1])

    print(f"\n=== Results ===")
    print(f"Files modified: {files_modified}")
    print(f"Total links added: {total_links}")
    print(f"\nTop 20 most-connected entities (by incoming+outgoing):")
    for slug, count in stats[:20]:
        print(f"  {count:3d} links  {slug}")
    print(f"\nLowest connectivity:")
    for slug, count in stats[-10:]:
        print(f"  {count:3d} links  {slug}")


if __name__ == "__main__":
    main()
