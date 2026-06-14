---
title: Kay 2007 - STEPS 2007 Progress Report
created: 2026-06-10
updated: 2026-06-10
type: entity
tags: [computing-history, hci, programming-languages, mathematics]
sources: [raw/papers/Kay_2007_-_STEPS_2007_Progress_Report.txt]
confidence: high
---

# Kay 2007 - STEPS 2007 Progress Report

## Core Thesis
The paper argues that the staggering growth in the complexity and code volume of modern software systems (operating systems, applications) is not an intrinsic necessity of functionality, but rather a pathological artifact of inadequate tools, concepts, and methodologies. The STEPS project's core thesis is that a "Moore's Law" leap in software expressiveness is achievable: a 3-4 order of magnitude reduction in code size for systems of comparable scope and power. This is not presented as a mere optimization, but as a fundamental reinvention of programming itself, enabled by identifying and applying a set of "powerful principles" from computing's history, most of which have never been combined as the guiding architecture for a comprehensive system. The goal is to create a runnable, comprehensible model that illuminates the essential complexity of personal computing, demonstrating it is far closer to the simplicity of a constitution than to the "3 cubic miles of case law" of current practice.

## Historical Context
This work is a direct response to the "software crisis" that began in the 1960s and has only intensified. By 2007, bloated software had become a culturally recognized problem (encapsulated by Negroponte's quote: "Andy giveth, but Bill taketh away!"). The state of the field was characterized by immense, fragile stacks and a prevailing view that complexity was unavoidable. Kay positions STEPS as a radical alternative to two concurrent trends: 1) incremental improvements to existing languages and platforms, and 2) the proliferation of narrowly-scoped Domain-Specific Languages (DSLs). He argues these fail to address the fundamental, general-purpose architecture of computing systems. STEPS looks back to the foundational, exploratory period of ARPA-IPTO and Xerox [[parc-1971-parc-papers-for-pendery-and-planning-purposes|PARC]] in the 60s/70s (when Kay, [[minsky-1961-steps-toward-artificial-intelligence|Minsky]], and colleagues were inventing personal computing, GUIs, and OOP) but aims to synthesize their insights into a new, coherent whole. It is an attempt to answer the question: if we were to start over today with the deepest principles we've learned, what would a truly minimal yet powerful system look like?

## Key Contributions
1.  **The "Moore's Law Software" Goal:** Articulating the audacious, quantitative target of a 100x-10,000x code reduction for a full system, framing it as a scientific question about the intrinsic complexity of computing experiences.
2.  **OMeta (and its meta-meta use):** A pattern-matching/transformation language that is itself expressed using its own syntax. This is a key tool for achieving compactness, allowing the entire system—from parsers to compilers to domain-specific "languages" (like a tiny TCP/IP stack)—to be built with a single, powerful, recursive transformation engine.
3.  **The Gezira Rendering Pipeline:** A practical demonstration of the "particles and fields" principle. It implements a sophisticated, hardware-accelerated-capable graphics pipeline in an astonishingly small amount of code by separating the declarative *meaning* of graphical operations from their optimization and execution.
4.  **Bootstrapping as Methodology:** The project's primary strategy was to build a series of simple, interlocking systems (Logo, Prolog, HyperCard model, BASIC, visual dataflow) within a single, growing substrate. Each increment both proved a principle and became the foundation for the next, aiming for the "miracle" of an integrated core.
5.  **Architectural Focus on "Meaning":** A insistence on separating the semantic *meaning* of operations from their syntactic forms and implementation optimizations. The line-of-code metric counts only this essential meaning, arguing that most existing code is syntactic and optimization cruft.

## Methodology
The methodology is neither purely theoretical nor empirical in the traditional scientific sense; it is **bootstrapping design and radical prototyping**. Kay describes it as "doing big things in very simple ways." The approach is experimental: work from the "outsides" of a system (low-level hardware interfacing and high-level end-user facilities) inward, toward a central "miracle" core of powerful, general principles. The paper is a **polemical progress report**, blending technical description of prototypes (OMeta translations, Gezira formulas) with a philosophical argument for a different direction in computer science. It uses a **design fiction** element—the hypothetical "20,000-line OS"—as a guiding star. The validation is in the incremental achievement of seemingly complex tasks (TCP/IP, graphics, multiple language interpreters) within tiny code footprints, demonstrating the viability of the approach. Success is measured by comprehensibility and the emergent power of the small, principled components.

## Influence
This 2007 report documents the genesis of research streams that have had significant downstream influence. OMeta directly inspired and evolved into **Morphic/OMeta2** and influenced parser generator tools in the JavaScript ecosystem. The work on Gezira and "particles and fields" prefigured modern declarative, constraint-based UI frameworks. Most importantly, STEPS was the direct progenitor of **The Lively Kernel** (mentioned as a component), which became a major research platform for live programming, direct manipulation, and educational computing. The project's philosophy—that software's complexity is a choice, not a destiny—has become a rallying cry for movements like **Software Carpentry** and various **minimalist computing** initiatives. It heavily informed Alan Kay's subsequent keynote speeches and writings (e.g., "Powerful Ideas Need to be Found Everywhere") that continue to challenge CS education and industry practice.

## Connections to Other Papers in the Collection
*   **[[engelbart-1960-games-that-teach-the-fundamentals-of-computer-operation|Engelbart]] 1962 (Augmenting Human Intellect):** STEPS is the direct heir to Engelbart's "bootstrap" methodology and his quest for tools that amplify human capability. The Lively Kernel aspect is pure Augment philosophy.
*   **Kay 1972 (Personal Computer):** This 2007 report is the next chapter in Kay's lifelong pursuit of the "Dynamic Media" vision from 1972. It asks: with modern hardware, how little code is needed to realize that original dream?
*   **[[bush-1931-the-differential-analyzer|Bush]] 1945 (As We May Think):** The HyperCard model and "linking ideas" components of STEPS are modern, programmatic instantiations of Bush's "memex" concept, seeking a more intimate, associative human-information relationship.
*   **[[backus-1978-can-programming-be-liberated-from-the-von-neumann-style|Backus]] 1978 (FP):** Kay's emphasis on "separating meaning from optimizations" and using powerful combinators (like OMeta's transformations) echoes Backus's call for a new functional style of programming based on higher-level programs combining functions.
*   **[[papert-1980-mindstorms-1st-ed|Papert]] 1980 (Mindstorms):** The STEPS work with Logo, the Lively Kernel, and the HyperCard model is a deep technical implementation of Papert's constructionist philosophy, where the system is designed to be "transparent" to children's thinking.
*   **[[feynman-1974-cargo-cult-science|Feynman]] 1974 (Cargo Cult Science):** STEPS is an explicit indictment of "cargo cult programming"—imitating the surface forms (syntax, APIs, large codebases) of successful systems without understanding their deep, unifying principles.
*   **[[thurston-1990-mathematical-education|Thurston]] 1994 (Proof and Progress):** Kay's work is a form of "proof by construction." The progress in understanding comes not from abstract proofs, but from *building* these small, powerful systems and demonstrating their explanatory and functional power.

## Modern Relevance
This report is startlingly prescient. Its diagnosis of software bloat resonates in an era of Docker containers gigabytes in size and JavaScript bundle sizes spiraling out of control. The solutions it proposes are more relevant than ever:
1.  **AI & Code Generation:** The project's core goal is to create a system so compact and meaningful that it could be entirely understood, manipulated, and even generated by an AI. The STEPS approach is arguably a necessary precursor to beneficial AI programming assistants, providing a "minimal viable system" to reason about.
2.  **Web & JavaScript:** The use of OMeta to build translators targeting JavaScript, and the existence of the Lively Kernel (a live programming environment in the browser), directly prefigure the modern ecosystem of JS-based tools, parsers (e.g., Babel, Acorn), and even low-code/no-code platforms that abstract complexity.
3.  **Education & Knowledge Work:** The vision of a 20,000-line "constitution" for computing is the ultimate educational tool—a system a learner could plausibly master. This aligns with modern pushes for computational thinking and tools like Jupyter Notebooks, but aims for a far deeper, systemic understanding.
4.  **Sustainability & Maintenance:** The emphasis on comprehensibility as a primary virtue directly addresses the critical challenges of software maintenance, security, and technical debt in modern systems.

## Key Quotes
1.  **"The STEPS project is setting out to create 'Moore's Law Software': a high-risk high-reward exploratory research effort to create a large-scope-and-range software system in 3-4 orders of magnitude less code than current practice."**
    *   This states the project's audacious, quantitative thesis. It redefines Moore's Law as a law of *expressiveness*, not hardware, demanding a paradigm shift in how we measure progress.

2.  **"Is the personal computing experience (counting the equivalent of the OS, apps, and other supporting software) intrinsically 2 billion lines of code, 200 million, 20 million, 2 million, 200,000, 20,000, 2,000?"**
    *   This reframes the entire field's challenge as a fundamental scientific question about intrinsic versus accidental complexity. It dares to ask the question most practitioners consider irrelevant or naive.

3.  **"The battles here are fought, won or lost on how much power of meaning lies under the syntactic forms. Because one of our main principles is to 'separate meaning from optimizations' we only have to count the lines of meaning that are sufficient to make the system work."**
    *   This is the philosophical heart of the project. It argues that traditional metrics (LOC, function points) are misleading. True progress is in the compression of *meaning*, not the rewriting of code.

4.  **"Our plan of attack is to do many experiments and to work our way to the center from the outsides."**
    *   This describes the unique, pragmatic-yet-visionary methodology. It avoids the trap of designing the "perfect core" first, instead building out from proven edges to discover the necessary core organically.

5.  **"One of our favorite cartoons 'THEN A MIRACLE OCCURS …' is perched over the middle area, and this is apt since most of the unknowns of this project lie there."**
    *   A candid admission that the synthesis of powerful principles into a coherent whole is the project's deepest challenge. It acknowledges the gap between having tools (like OMeta) and achieving the "miracle" of a universal semantic kernel.