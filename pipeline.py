#!/usr/bin/env python3
"""
WorryDream Wiki Analysis Pipeline
Uses OpenCode Go (mimo-v2.5) directly via API for cost-efficient paper analysis.
"""
import os
import sys
import json
import time
import re
import hashlib
import glob
from pathlib import Path

try:
    import requests
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests", "-q"])
    import requests

# Load env
def load_env(env_path):
    env = {}
    with open(env_path) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, _, val = line.partition('=')
                env[key.strip()] = val.strip().strip('"').strip("'")
    return env

env_path = os.path.expanduser("~/.hermes/profiles/atlas/.env")
env = load_env(env_path)

API_KEY = env.get("OPENCODE_GO_API_KEY")
BASE_URL = env.get("OPENCODE_GO_BASE_URL", "https://opencode.ai/zen/go/v1")
MODEL = "mimo-v2.5"  # cheaper non-pro model

WIKI = os.path.expanduser("~/repos/hyperflash-business/departments/engineering/research/worrydream-wiki")
RAW_DIR = os.path.join(WIKI, "raw", "papers")
ENTITIES_DIR = os.path.join(WIKI, "entities")
CONCEPTS_DIR = os.path.join(WIKI, "concepts")
COMPARISONS_DIR = os.path.join(WIKI, "comparisons")

ANALYSIS_SYSTEM = """You are a deep research analyst. Your job is to analyze academic papers and produce thorough, insightful wiki pages.

Your analyses must go BEYOND surface-level summary. For each paper:
1. Identify the core thesis and its nuances
2. Situate it in historical context (what came before, what problem was being solved)
3. Extract key contributions (what changed because of this paper)
4. Analyze methodology (how the argument is structured)
5. Trace influence (what came after, who cited it, what it enabled)
6. Find connections to other works in the collection
7. Assess modern relevance (especially to AI, computing, knowledge work)
8. Select the most important direct quotes

Write in clear, direct prose. No corporate buzzwords. No em-dashes. Be analytical, not descriptive."""

ANALYSIS_PROMPT_TEMPLATE = """Analyze this paper and produce a deep wiki page analysis.

PAPER: {filename}
TEXT:
{text}

Write the analysis as markdown with this structure:

---
title: {title}
created: 2026-06-10
updated: 2026-06-10
type: entity
tags: [{tags}]
sources: [raw/papers/{filename}]
confidence: high
---

# {title}

## Core Thesis
[What is the paper arguing or demonstrating? Be specific about nuances.]

## Historical Context
[What came before? What problem was being solved? What was the state of the field?]

## Key Contributions
[What did this paper introduce or change? List the specific ideas/concepts/frameworks it pioneered.]

## Methodology
[How was the argument structured? Theoretical? Empirical? Polemical? Design fiction?]

## Influence
[What came after this paper? Who cited it? What did it enable? Be specific about the lineage.]

## Connections to Other Papers in the Collection
[Link to other papers from the WorryDream collection. Suggested connections: Bush 1945 (As We May Think), Engelbart 1962 (Augmenting Human Intellect), Kay 1972 (Personal Computer), Backus 1978 (FP), Papert 1980 (Mindstorms), Anderson 1972 (More is Different), Feynman 1974 (Cargo Cult Science), Thurston 1994 (Proof and Progress), Hofstadter 2001 (Analogy), Lockhart 2002 (Mathematician's Lament). Connect to whichever are relevant.]

## Modern Relevance
[How does this relate to current technology, AI, knowledge management, education, or Hyperflash's work?]

## Key Quotes
[Select the 5-10 most important direct quotes from the paper. Include brief analytical commentary after each.]

Target: 1500-2500 words. Be analytical and insightful, not just descriptive."""

CONCEPT_SYSTEM = """You are a research synthesizer. Your job is to analyze connections across multiple papers and produce concept/theme wiki pages that reveal deeper patterns.

Write in clear, direct prose. No corporate buzzwords. No em-dashes. Be analytical."""

CONCEPT_PROMPT_TEMPLATE = """Create a concept/theme page analyzing the theme of "{theme}" across these papers.

PAPERS AND THEIR ANALYSES:
{analyses}

Write a markdown wiki page that:

---
title: {title}
created: 2026-06-10
updated: 2026-06-10
type: concept
tags: [{tags}]
sources: [{sources}]
confidence: high
---

# {title}

## Definition
[What is this concept/theme? Define it precisely.]

## Historical Evolution
[How did this idea evolve across the papers? Show the lineage.]

## Key Tensions and Debates
[Where do the papers disagree? What are the unresolved questions?]

## Cross-Pollination
[How did ideas from one paper influence another? What unexpected connections exist?]

## Modern Manifestations
[How does this theme play out in current technology, AI, and knowledge work?]

## Implications for Hyperflash
[How does this concept inform AI operations, tools for thought, or Hyperflash's product vision?]

## Key Synthesis
[The deepest insight that emerges only from reading these papers together, not individually.]

Target: 1500-2000 words. This should reveal connections invisible when reading papers in isolation."""


def call_mimo(prompt, system_msg, max_tokens=4000, retries=5):
    """Call OpenCode Go with mimo-v2.5. Retries with exponential backoff on 429."""
    url = f"{BASE_URL}/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system_msg},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": max_tokens,
        "temperature": 0.3
    }
    
    for attempt in range(retries):
        resp = requests.post(url, headers=headers, json=payload, timeout=300)
        
        if resp.status_code == 200:
            data = resp.json()
            content = data["choices"][0]["message"]["content"]
            usage = data.get("usage", {})
            return content, usage
        
        if resp.status_code == 429:
            wait = min(30 * (2 ** attempt), 120)
            print(f"  Rate limited (attempt {attempt+1}/{retries}), waiting {wait}s...", flush=True)
            time.sleep(wait)
            continue
        
        print(f"  API error {resp.status_code}: {resp.text[:200]}")
        return None
    
    print(f"  Failed after {retries} retries")
    return None


def extract_frontmatter(text):
    """Parse YAML frontmatter from extracted text."""
    meta = {}
    if text.startswith("---"):
        end = text.find("---", 3)
        if end != -1:
            fm = text[3:end]
            for line in fm.strip().split("\n"):
                if ":" in line:
                    k, _, v = line.partition(":")
                    meta[k.strip()] = v.strip()
    return meta


def analyze_paper(txt_path, force=False):
    """Analyze a single paper and save wiki page."""
    filename = os.path.basename(txt_path)
    wiki_name = filename.replace(".txt", ".md")
    
    # Create wiki filename from paper filename
    # e.g., "Bush_1945_-_As_We_May_Think.txt" -> "bush-1945-as-we-may-think.md"
    slug = filename.replace(".txt", "").lower()
    slug = re.sub(r'_+', '-', slug)
    slug = re.sub(r'[^a-z0-9-]', '', slug)
    slug = re.sub(r'-+', '-', slug).strip('-')
    wiki_path = os.path.join(ENTITIES_DIR, f"{slug}.md")
    
    if os.path.exists(wiki_path) and not force:
        print(f"  SKIP (exists): {slug}")
        return wiki_path
    
    # Read paper text
    with open(txt_path) as f:
        text = f.read()
    
    if len(text.strip()) < 100:
        print(f"  SKIP (too short): {filename}")
        return None
    
    # Check if scanned PDF
    is_scanned = text.strip().startswith("[SCANNED PDF")
    
    if is_scanned:
        # For scanned PDFs, analyze based on title/author/year alone
        # This gives a metadata-level entry; full analysis needs the actual text
        title = filename.replace(".txt", "").replace("_", " ")
        prompt = f"""Create a brief wiki entry for this paper based on its title and metadata. Note: the full text was not extractable (scanned PDF).

Title: {title}

Write a markdown entry with:
---
title: {title}
created: 2026-06-10
updated: 2026-06-10
type: entity
tags: [{', '.join(guess_tags(title, filename))}]
sources: [raw/papers/{filename}]
confidence: low
---

# {title}

## Overview
Based on the title and author, provide what is known about this work. Include:
- Who the author is and their significance
- What the paper likely covers based on the title
- Its place in the broader field
- Why it would be included in Bret Victor's reference collection
- Connections to other papers in the WorryDream collection

Note at the top: "This entry is based on metadata only. The original paper is a scanned PDF and full text extraction was not possible."

Target: 500-800 words."""
        print(f"  [SCANNED] {title[:55]}...", end="", flush=True)
    else:
        # Normal text analysis
        # Truncate if too long (keep first ~15K chars for analysis)
        if len(text) > 15000:
            text = text[:15000] + "\n\n[... truncated for analysis ...]"
        
        title = filename.replace(".txt", "").replace("_", " ")
        tags = guess_tags(text, filename)
        
        prompt = ANALYSIS_PROMPT_TEMPLATE.format(
            filename=filename,
            text=text,
            title=title,
            tags=", ".join(tags)
        )
        print(f"  {title[:55]}...", end="", flush=True)
    start = time.time()
    
    result = call_mimo(prompt, ANALYSIS_SYSTEM, max_tokens=4000)
    
    if result is None:
        print(" FAILED")
        return None
    
    content, usage = result
    elapsed = time.time() - start
    
    # Save wiki page
    with open(wiki_path, 'w') as f:
        f.write(content)
    
    in_tok = usage.get("prompt_tokens", 0)
    out_tok = usage.get("completion_tokens", 0)
    print(f" {elapsed:.0f}s | {in_tok}+{out_tok} tokens | {len(content.split())} words")
    
    return wiki_path


def guess_tags(text, filename):
    """Heuristic tag assignment."""
    tags = []
    text_lower = text.lower()
    fname_lower = filename.lower()
    
    tag_keywords = {
        "computing-history": ["computer", "programming", "software", "digital", "electronic"],
        "hci": ["interface", "interaction", "display", "mouse", "gui", "man-computer"],
        "programming-languages": ["language", "compiler", "functional", "lisp", "syntax"],
        "mathematics": ["mathematic", "theorem", "proof", "geometry", "algebra"],
        "physics": ["quantum", "particle", "relativity", "symmetry", "physics"],
        "cognitive-science": ["cognitive", "perception", "memory", "analogy", "cognition"],
        "education": ["learn", "teach", "student", "classroom", "curriculum"],
        "design": ["design", "visual", "spatial", "graphic", "architecture"],
        "philosophy": ["philosophy", "epistemology", "ontology", "metaphysic"],
        "systems": ["distributed", "network", "protocol", "system"],
    }
    
    for tag, keywords in tag_keywords.items():
        if any(kw in text_lower or kw in fname_lower for kw in keywords):
            tags.append(tag)
    
    if not tags:
        tags = ["philosophy"]
    
    return tags[:4]


def synthesize_concepts():
    """Create cross-paper concept pages."""
    # Read all entity pages
    entities = {}
    for path in sorted(glob.glob(os.path.join(ENTITIES_DIR, "*.md"))):
        with open(path) as f:
            content = f.read()
        name = os.path.basename(path).replace(".md", "")
        entities[name] = content
    
    if len(entities) < 3:
        print("Not enough entity pages for synthesis")
        return
    
    # Define concept themes to synthesize
    themes = [
        {
            "name": "tools-for-thought",
            "title": "Tools for Thought: From Memex to AI",
            "papers": ["bush-1945", "engelbart-1962", "kay-1972", "papert-1980"],
            "tags": "computing-history, hci, visionary"
        },
        {
            "name": "mathematics-as-understanding",
            "title": "Mathematics as Understanding, Not Formalism",
            "papers": ["thurston-1994", "lockhart-2002", "papert-1980"],
            "tags": "mathematics, education, philosophy"
        },
        {
            "name": "anti-reductionism-and-emergence",
            "title": "Anti-Reductionism: Why More Is Different",
            "papers": ["anderson-1972", "hofstadter-2001", "feynman-1974"],
            "tags": "physics, philosophy, anti-reductionism"
        },
        {
            "name": "scientific-integrity-and-rigor",
            "title": "Scientific Integrity: Form vs Substance",
            "papers": ["feynman-1974", "anderson-1972", "thurston-1994"],
            "tags": "philosophy, critique, systems-thinking"
        },
        {
            "name": "programming-paradigms-and-vision",
            "title": "Programming Paradigms: From Von Neumann to Functional to Object-Oriented",
            "papers": ["backus-1978", "kay-1972", "engelbart-1962"],
            "tags": "programming-languages, computing-history, visionary"
        },
    ]
    
    for theme in themes:
        concept_path = os.path.join(CONCEPTS_DIR, f"{theme['name']}.md")
        if os.path.exists(concept_path):
            print(f"  SKIP concept (exists): {theme['name']}")
            continue
        
        # Gather analyses for this theme
        analyses = []
        sources = []
        for paper_slug in theme["papers"]:
            # Find matching entity
            for name, content in entities.items():
                if paper_slug in name:
                    body = content
                    if content.startswith("---"):
                        end = content.find("---", 3)
                        if end != -1:
                            body = content[end+3:].strip()
                    analyses.append(f"## {name}\n{body[:3000]}")
                    sources.append(f"raw/papers/{name}.md")
                    break
        
        if not analyses:
            continue
        
        combined = "\n\n---\n\n".join(analyses)
        
        prompt = CONCEPT_PROMPT_TEMPLATE.format(
            theme=theme["title"],
            analyses=combined,
            title=theme["title"],
            tags=theme["tags"],
            sources=", ".join(sources)
        )
        
        print(f"  Synthesizing: {theme['title']}...", end="", flush=True)
        start = time.time()
        
        result = call_mimo(prompt, CONCEPT_SYSTEM, max_tokens=3000)
        
        if result is None:
            print(" FAILED")
            continue
        
        content, usage = result
        elapsed = time.time() - start
        
        with open(concept_path, 'w') as f:
            f.write(content)
        
        print(f" {elapsed:.0f}s | {len(content.split())} words")


def main():
    """Main pipeline."""
    mode = sys.argv[1] if len(sys.argv) > 1 else "resume"
    
    # Find all text files
    txt_files = sorted(glob.glob(os.path.join(RAW_DIR, "*.txt")))
    
    # Set up logging
    log_path = os.path.join(WIKI, "pipeline.log")
    
    if mode == "analyze":
        # Analyze all papers (force re-analyze)
        print(f"\n=== ANALYZING {len(txt_files)} PAPERS (force) ===\n")
        results = {"success": 0, "skipped": 0, "failed": 0}
        
        for i, txt_path in enumerate(txt_files):
            print(f"[{i+1}/{len(txt_files)}]", end="", flush=True)
            result = analyze_paper(txt_path, force=True)
            if result:
                results["success"] += 1
            else:
                results["failed"] += 1
            time.sleep(1)
            # Log progress every 10
            if (i + 1) % 10 == 0:
                with open(log_path, 'a') as lf:
                    lf.write(f"[{time.strftime('%H:%M:%S')}] Progress: {i+1}/{len(txt_files)} | {results}\n")
        
        print(f"\n=== RESULTS: {results} ===\n")
        with open(log_path, 'a') as lf:
            lf.write(f"[{time.strftime('%H:%M:%S')}] DONE | {results}\n")
    
    elif mode == "test":
        print(f"\n=== TEST MODE: analyzing first paper ===\n")
        if txt_files:
            analyze_paper(txt_files[0], force=True)
    
    elif mode == "resume":
        # Resume from where we left off (skip existing) - DEFAULT
        total = len(txt_files)
        existing = len(glob.glob(os.path.join(ENTITIES_DIR, "*.md")))
        print(f"\n=== RESUMING ANALYSIS ===")
        print(f"  Text files: {total}")
        print(f"  Already analyzed: {existing}")
        print(f"  Remaining: ~{total - existing}\n")
        
        with open(log_path, 'a') as lf:
            lf.write(f"[{time.strftime('%H:%M:%S')}] RESUME | {total} files, {existing} existing\n")
        
        results = {"success": 0, "skipped": 0, "failed": 0}
        for i, txt_path in enumerate(txt_files):
            print(f"[{i+1}/{total}]", end="", flush=True)
            result = analyze_paper(txt_path)
            if result:
                if "SKIP" in str(result):
                    results["skipped"] += 1
                else:
                    results["success"] += 1
            else:
                results["failed"] += 1
            
            # Log progress every 25
            if (i + 1) % 25 == 0:
                with open(log_path, 'a') as lf:
                    lf.write(f"[{time.strftime('%H:%M:%S')}] {i+1}/{total} | {results}\n")
                print(f"\n  --- checkpoint: {results} ---\n", flush=True)
            
            # Delay between successful API calls
            if result and "SKIP" not in str(result):
                time.sleep(1)
        
        print(f"\n=== RESULTS: {results} ===\n")
        with open(log_path, 'a') as lf:
            lf.write(f"[{time.strftime('%H:%M:%S')}] DONE | {results}\n")
    
    elif mode == "synthesize":
        print(f"\n=== SYNTHESIZING CONCEPTS ===\n")
        synthesize_concepts()
    
    elif mode == "full":
        print(f"\n=== FULL PIPELINE ===\n")
        print(f"Step 1: Analyze {len(txt_files)} papers")
        for i, txt_path in enumerate(txt_files):
            print(f"[{i+1}/{len(txt_files)}]", end="", flush=True)
            result = analyze_paper(txt_path)
            if result and "SKIP" not in str(result):
                time.sleep(1)
        
        print(f"\nStep 2: Synthesize concepts")
        synthesize_concepts()
        print(f"\n=== DONE ===")


if __name__ == "__main__":
    main()
