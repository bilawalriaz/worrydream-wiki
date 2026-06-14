# Wiki Log

> Chronological record of all wiki actions. Append-only.
> Format: `## [YYYY-MM-DD] action | subject`
> Actions: ingest, update, query, lint, create, archive, delete
> When this file exceeds 500 entries, rotate.

## [2026-06-10] create | Wiki initialized
- Domain: Bret Victor's WorryDream reference collection (worrydream.com/refs/)
- 394 papers identified (371 PDF, 22 HTML, 1 index)
- Structure created with SCHEMA.md, index.md, log.md
- Purpose: Hyperflash research asset, RAG demo, website content
- Pipeline: download, extract, analyse via subagents, cross-synthesize

## [2026-06-10] create | Kay 1972 Dynabook paper analysis
- Created entity page `entities/kay-1972-personal-computer-for-children.md`
- Deep analysis: core thesis, historical context, Dynabook concept, object-oriented thinking precursor, personal computing theory, pedagogical framework (Moore, Papert, Piaget), methodology (design fiction + engineering), influence (PARC, Smalltalk-80, iPad, constructionism), connections to Bush/Engelbart/Papert/Backus/Anderson, modern relevance, 7 key quotes
- ~2400 words. Source: `raw/papers/Kay_1972_-_A_Personal_Computer_for_Children_of_All_Ages.txt`

## [2026-06-10] create | Pipeline batch: 327 entity analyses (mimo-v2.5)
- Pipeline script: `pipeline.py` (OpenCode Go API, mimo-v2.5 model)
- Processed: 327 entity analyses via API
- Model: mimo-v2.5 via OpenCode Go
- Average runtime: ~50s per paper
- Total: 337 entity files in `entities/` (10 from initial mimo-v2.5-pro batch, 327 from mimo-v2.5 batch)

## [2026-06-10] create | Cross-synthesis concept pages (5)
- `concepts/tools-for-thought.md` - From memex to AI (Bush, Engelbart, Kay, Papert, Sutherland, Licklider, Nelson)
- `concepts/mathematics-as-understanding.md` - Anti-formalism (Hamming, Thurston, Lockhart, Arnold, Wigner, Hadamard, Feynman)
- `concepts/anti-reductionism-and-emergence.md` - More is different (Anderson, Hestenes, Cardelli, Barut, Smaldino, Wilson)
- `concepts/scientific-integrity-and-rigor.md` - Form vs substance (Feynman, Postman, Cook, Barber, Oppenheimer)
- `concepts/programming-paradigms-and-vision.md` - Von Neumann to functional to OOP (Backus, Kay, Ingalls, Ungar, Landin, Gabriel, Hudak, Hughes)

## [2026-06-10] update | Index and log
- `index.md` regenerated with all 337 entities + 5 concepts = 342 entries
- `log.md` updated to reflect full pipeline output

## [2026-06-10] create | GitHub repo and deployment
- Repo: `bilawalriaz/worrydream-wiki` (public, GitHub Pages enabled)
- Deploy workflow: `.github/workflows/deploy.yml` (Quartz 5 build → GitHub Pages)
- Live at: https://bilawalriaz.github.io/worrydream-wiki/

## [2026-06-10] update | Quartz theme: default Obsidian theme
- Config: `quartz.config.yaml`
- Theme: default Obsidian template with stock colors
- Fonts: Schibsted Grotesk, Source Sans Pro, IBM Plex Mono
- Build succeeded, deployed to GitHub Pages

## [2026-06-10] update | Redesign: Hyperflash dark aesthetic
- Custom SCSS: `quartz/styles/custom.scss` (12KB)
- Dark near-black background (#09090b) matching hyperflash.uk
- Electric blue accents (#3b82f6) for links, tags, highlights
- Inter font (headers + body), JetBrains Mono (code)
- Hidden dark mode toggle (always dark)
- Custom scrollbars, search styling, graph view, backlinks, callouts
- Footer links: Hyperflash, GitHub, Bret Victor
- Syntax highlighting: github-dark for both modes
- Commit: c2a7f6e

## [2026-06-10] update | Drift fix: wikilinks + frontmatter + log
- Script: `scripts/add_wikilinks.py` (v3, 5.9s runtime)
- Added 3,452 clean wikilinks across 337 entity files (avg 10.2 per file)
- v1 had substring match bug (e.g., 'instantl' in 'instantly'); v3 uses proper word boundaries
- v1 had generic word false positives (e.g., 'air', 'scientific'); v3 uses 130+ word denylist
- All 337 entities now have >= 2 wikilinks (SCHEMA.md compliance)
- All 337 entities have complete frontmatter (title, tags, sources, confidence)
- 9 entities fixed for missing fields (altmann, armstrong, cardelli, fenton, heeffer, hestenes-1987, jaynes-1990, jefferson, nrc-1999)
- heeffer-2011 had nested code block unwrapped
- Top linked: clark-w-1986 (37), hunt-2015 (27), kay-1977 (26), kay-1990 (25)
