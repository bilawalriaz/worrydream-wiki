# WorryDream References Wiki

## Domain

A curated knowledge base built from Bret Victor's personal reference library at worrydream.com/refs/. Covers foundational works in computing, human-computer interaction, programming languages, mathematics, physics, cognitive science, education, design, and the philosophy of technology. Spans 1945 to 2016.

This wiki exists as a Hyperflash research asset: a deeply analysed, cross-referenced library for use in product development (Hyperflash Assist RAG), website content, and demonstrating AI-powered knowledge synthesis.

## Conventions

- File names: lowercase, hyphens, no spaces (e.g., `bush-1945-as-we-may-think.md`)
- Every wiki page starts with YAML frontmatter (see below)
- Use `[[wikilinks]]` to link between pages (minimum 2 outbound links per page)
- When updating a page, always bump the `updated` date
- Every new page must be added to `index.md` under the correct section
- Every action must be appended to `log.md`
- **Provenance markers:** On pages that synthesize 3+ sources, append `^[raw/papers/source-file.md]` at the end of paragraphs whose claims come from a specific source
- Analyses must go beyond surface summary: identify key arguments, historical context, influence on later work, and connections to other papers in the collection

## Frontmatter

```yaml
---
title: Page Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query | summary
tags: [from taxonomy below]
sources: [raw/papers/source-file.md]
confidence: high | medium | low
contested: true | false
contradictions: [other-page-slug]
---
```

### Raw Source Frontmatter

```yaml
---
source_url: https://worrydream.com/refs/filename.pdf
ingested: YYYY-MM-DD
author: Author Name
year: YYYY
title: Paper Title
type: paper | article | interview | book-chapter
---
```

## Tag Taxonomy

### Domains
- `computing-history` - History of computing, labs, institutions
- `hci` - Human-computer interaction, interface design
- `programming-languages` - Language design, paradigms, theory
- `mathematics` - Pure math, proof, mathematical philosophy
- `physics` - Physics, quantum mechanics, relativity
- `cognitive-science` - Cognition, learning, perception
- `education` - Teaching, pedagogy, learning theory
- `design` - Design thinking, visual communication, architecture
- `philosophy` - Philosophy of science, technology, knowledge
- `systems` - Distributed systems, networks, infrastructure

### Types
- `seminal` - Foundational work that shaped a field
- `visionary` - Forward-looking, prescient ideas
- `critique` - Challenges existing paradigms
- `survey` - Reviews or synthesizes a field
- `interview` - Oral history or Q&A
- `tutorial` - Explanatory or pedagogical

### Cross-cutting
- `visual-thinking` - Emphasis on visual/spatial representation
- `direct-manipulation` - Interactive, tangible interfaces
- `constructionism` - Learning by building
- `systems-thinking` - Holistic, interconnected analysis
- `anti-reductionism` - Arguments against pure reductionism

## Page Thresholds

- **Create a page** when an entity/concept appears in 2+ sources OR is central to one source
- **Add to existing page** when a source mentions something already covered
- **DON'T create a page** for passing mentions or minor details
- **Split a page** when it exceeds ~200 lines
- **Archive a page** when its content is fully superseded

## Analysis Depth

Each paper analysis (stored in `raw/` as processed markdown) should include:

1. **Core thesis** - What is the paper arguing or demonstrating?
2. **Historical context** - What came before? What problem was being solved?
3. **Key contributions** - What did this paper introduce or change?
4. **Methodology** - How was the argument structured? (theoretical, empirical, experimental, polemical)
5. **Influence** - What came after this paper? Who cites it? What did it enable?
6. **Connections** - Links to other papers in the WorryDream collection
7. **Modern relevance** - How does this relate to current technology/AI/Hyperflash's work?
8. **Key quotes** - The most important passages (direct quotes)
