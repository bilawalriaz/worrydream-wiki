#!/usr/bin/env python3
"""
Add wikilinks to entity files - v3 with smarter parsing.

Fixes from v2:
- Skip single-word lastnames shorter than 4 chars or in a denylist
- For hyphenated slugs like "air-force-1960-...", don't take "air" as the
  author; use the full first segment before the year
- For slugs like "scientific-american-1966-...", treat the whole prefix
  as the org name
"""

import os
import re
from collections import defaultdict

ENTITIES_DIR = "departments/engineering/research/worrydream-wiki/entities"

# Common English words that should never be treated as author last names
DENYLIST = {
    'air', 'the', 'and', 'for', 'are', 'but', 'not', 'you', 'all', 'can',
    'her', 'was', 'one', 'our', 'out', 'day', 'had', 'has', 'his', 'how',
    'its', 'may', 'new', 'now', 'old', 'see', 'way', 'who', 'did', 'get',
    'let', 'say', 'she', 'too', 'use', 'dad', 'mom', 'man', 'big', 'end',
    'put', 'run', 'try', 'ask', 'men', 'own', 'right', 'left', 'good',
    'best', 'next', 'last', 'long', 'great', 'little', 'small', 'large',
    'old', 'young', 'american', 'british', 'german', 'french', 'scientific',
    'industrial', 'national', 'general', 'special', 'original', 'natural',
    'artificial', 'historical', 'critical', 'technical', 'practical',
    'computer', 'history', 'design', 'system', 'systems', 'process',
    'method', 'methods', 'theory', 'theories', 'principle', 'principles',
    'future', 'past', 'present', 'modern', 'ancient', 'classic', 'classical',
    'university', 'college', 'school', 'institute', 'laboratory', 'lab',
    'office', 'department', 'foundation', 'association', 'society', 'group',
    'team', 'company', 'corporation', 'inc', 'ltd', 'corp',
    'review', 'survey', 'analysis', 'study', 'report', 'paper', 'article',
    'essay', 'chapter', 'book', 'volume', 'edition', 'series', 'journal',
    'magazine', 'press', 'publishing', 'publisher', 'author', 'writer',
    'reader', 'editor', 'introduction', 'preface', 'foreword', 'afterword',
    'conclusion', 'summary', 'abstract', 'appendix', 'bibliography',
    'reference', 'references', 'index', 'table', 'figure', 'diagram',
    'graph', 'chart', 'map', 'atlas', 'guide', 'manual', 'handbook',
    'encyclopedia', 'dictionary', 'lexicon', 'glossary', 'thesaurus',
    'toward', 'against', 'between', 'among', 'within', 'without',
    'through', 'across', 'beyond', 'around', 'beside', 'behind',
    'before', 'after', 'during', 'while', 'until', 'since',
    'because', 'although', 'however', 'therefore', 'moreover',
    'furthermore', 'nevertheless', 'nonetheless', 'meanwhile',
    'first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh',
    'eighth', 'ninth', 'tenth', 'last', 'next', 'previous', 'following',
}


def parse_slug_authors(slug, title):
    """
    Extract author last names from slug and title.

    Strategy:
    1. From title "Author YEAR - Title", extract the author section
    2. If title doesn't parse, use slug prefix
    3. Apply denylist to filter generic words
    """
    # Try title first
    tmatch = re.match(r'^(.+?)\s+(\d{4})\s*[-–—]\s*(.+)$', title)
    if tmatch:
        author_str = tmatch.group(1)
        # Split on &, and, /
        authors = re.split(r'\s+(?:&|and)\s+|\s*/\s+|\s*,\s+', author_str)
        lastnames = []
        for a in authors:
            a = a.strip()
            if not a:
                continue
            # "Allen-Conn" -> both names; "Smith-Jones" -> both names
            for p in re.split(r'[-\s]+', a):
                if p and len(p) > 1 and p.lower() not in DENYLIST:
                    lastnames.append(p)
        return lastnames

    # Fallback: use slug prefix up to year
    smatch = re.match(r'^(.+?)-(\d{4})-(.+)$', slug)
    if smatch:
        prefix = smatch.group(1)
        # If prefix is multi-word, use the last word as author
        # e.g., "air-force" -> "force" (not "air")
        # e.g., "scientific-american" -> skip (both in denylist)
        parts = prefix.split('-')
        lastnames = []
        for p in parts:
            if p and len(p) > 1 and p.lower() not in DENYLIST:
                lastnames.append(p)
        # If we got a multi-part prefix where first is denylisted but later aren't,
        # prefer the non-denylisted parts
        if lastnames:
            return lastnames

    return []


def load_titles():
    """Load slug -> info and author -> slugs mappings."""
    slug_to_info = {}
    author_to_slugs = defaultdict(list)

    for f in sorted(os.listdir(ENTITIES_DIR)):
        if not f.endswith(".md"):
            continue
        slug = f[:-3]
        with open(os.path.join(ENTITIES_DIR, f), 'r') as fh:
            content = fh.read()

        title_match = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', content, re.MULTILINE)
        title = title_match.group(1) if title_match else slug

        tmatch = re.match(r'^(.+?)\s+(\d{4})\s*[-–—]\s*(.+)$', title)
        if tmatch:
            author_str = tmatch.group(1)
            year = tmatch.group(2)
            paper_title = tmatch.group(3).strip()
        else:
            author_str = slug.split("-")[0].title()
            year = slug.split("-")[1] if len(slug.split("-")) > 1 else ""
            paper_title = title

        lastnames = parse_slug_authors(slug, title)
        for ln in lastnames:
            author_to_slugs[ln.lower()].append(slug)

        slug_to_info[slug] = {
            "authors": author_str,
            "lastnames": lastnames,
            "year": year,
            "title": paper_title,
        }

    return slug_to_info, author_to_slugs


def is_word_char(c):
    return c.isalnum() or c in "-'"


def find_term_matches(body, term, term_lower):
    """Find all positions where `term` appears with proper word boundaries."""
    matches = []
    search_from = 0
    term_len = len(term)
    body_lower = body.lower()

    while True:
        idx = body_lower.find(term_lower, search_from)
        if idx == -1:
            break

        if idx > 0:
            left_char = body[idx - 1]
            if is_word_char(left_char):
                search_from = idx + 1
                continue

        end_idx = idx + term_len
        if end_idx < len(body):
            right_char = body[end_idx]
            if is_word_char(right_char):
                search_from = idx + 1
                continue

        matches.append((idx, term_len))
        search_from = idx + term_len

    return matches


def add_wikilinks_to_entity(slug, content, slug_to_info, author_to_slugs):
    """Add [[wikilinks]] to a single entity file."""
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

    code_blocks = []
    def replace_code(m):
        idx = len(code_blocks)
        code_blocks.append(m.group(0))
        return f"\x00CB{idx}\x00"
    body = re.sub(r'```.*?```', replace_code, body, flags=re.DOTALL)

    inline_codes = []
    def replace_inline(m):
        idx = len(inline_codes)
        inline_codes.append(m.group(0))
        return f"\x00IC{idx}\x00"
    body = re.sub(r'`[^`\n]+`', replace_inline, body)

    wikilinks = []
    def replace_wl(m):
        idx = len(wikilinks)
        wikilinks.append(m.group(0))
        return f"\x00WL{idx}\x00"
    body = re.sub(r'\[\[[^\]]+\]\]', replace_wl, body)

    mdlinks = []
    def replace_ml(m):
        idx = len(mdlinks)
        mdlinks.append(m.group(0))
        return f"\x00ML{idx}\x00"
    body = re.sub(r'\[[^\]]+\]\([^)]+\)', replace_ml, body)

    current_info = slug_to_info[slug]
    current_lastnames = set(n.lower() for n in current_info["lastnames"])

    terms = []
    for lastname, target_slugs in author_to_slugs.items():
        if lastname in current_lastnames:
            continue
        if len(target_slugs) == 0:
            continue
        target = target_slugs[0]
        if target == slug:
            continue
        # Skip if lastname is too short (< 4 chars) or in denylist
        if len(lastname) < 4:
            continue
        terms.append((lastname, target))

    terms.sort(key=lambda x: -len(x[0]))

    linked = set()
    links_added = 0

    for term, target_slug in terms:
        term_lower = term.lower()
        matches = find_term_matches(body, term, term_lower)

        for idx, term_len in reversed(matches):
            if any(abs(idx - p) < 10 for p in linked):
                continue

            original = body[idx:idx+term_len]
            replacement = f"[[{target_slug}|{original}]]"
            body = body[:idx] + replacement + body[idx+term_len:]
            linked.add(idx)
            links_added += 1

    for i, block in enumerate(code_blocks):
        body = body.replace(f"\x00CB{i}\x00", block)
    for i, block in enumerate(inline_codes):
        body = body.replace(f"\x00IC{i}\x00", block)
    for i, block in enumerate(wikilinks):
        body = body.replace(f"\x00WL{i}\x00", block)
    for i, block in enumerate(mdlinks):
        body = body.replace(f"\x00ML{i}\x00", block)

    return frontmatter + body, links_added


def main():
    print("Loading entity metadata...")
    slug_to_info, author_to_slugs = load_titles()
    print(f"  {len(slug_to_info)} entities")
    print(f"  {len(author_to_slugs)} unique author last names (after denylist)")

    # Show what we mapped
    sample = list(author_to_slugs.items())[:10]
    print(f"  Sample mappings:")
    for k, v in sample:
        print(f"    '{k}' -> {v[0]}")

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
    print(f"\nTop 20 most-linked entities:")
    for slug, count in stats[:20]:
        print(f"  {count:3d}  {slug}")


if __name__ == "__main__":
    main()
