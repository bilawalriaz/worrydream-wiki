---
title: Iverson 1991 - A Personal View of APL
created: 2026-06-10
updated: 2026-06-10
type: entity
tags: [computing-history, hci, programming-languages, mathematics]
sources: [raw/papers/Iverson_1991_-_A_Personal_View_of_APL.txt]
confidence: high
---

# Iverson 1991 - A Personal View of APL

## Core Thesis
Kenneth Iverson’s essay is not a neutral history; it is a polemic for the soul of programming notation. The core thesis is that APL’s original and most profound purpose was not as a commercial programming tool, but as a **precise, executable notation for teaching and thinking** across a wide range of subjects. Iverson argues that this pedagogical mission was hijacked by commercial interests and limited by technological constraints (like the custom alphabet). The creation of J, a decade after his retirement, represents his concerted effort to reclaim this original purpose by designing a dialect that is accessible (shareware, printable, cross-platform) while advancing the language’s conceptual frontiers, particularly in array handling and tacit (functional) programming. The paper is an intellectual autobiography, tracing the evolution of his own thinking on notation through the lens of dialectal choices.

## Historical Context
The paper sits at a pivotal moment, 35 years after APL’s inception at Harvard. The field of programming languages had fragmented. Mainstream languages (C, Pascal, etc.) prioritized verbosity and explicit control flow. APL itself had bifurcated into commercial dialects (like IBM’s APL2) that preserved the iconic symbol set and remained tied to mainframes, and experimental variants. Iverson frames this as a problem of lost vision: “I continue to believe that its most important use remains to be exploited: as a simple, precise, executable notation for the teaching of a wide range of subjects.” The context includes the rise of personal computers and the need for shareware, as well as the growing interest in functional programming sparked by John [[backus-1978-can-programming-be-liberated-from-the-von-neumann-style|Backus]]’s 1978 [[turing-1936-on-computable-numbers-with-an-application-to-the-entscheidungsproblem|Turing]] Award lecture. Iverson is directly responding to these constraints and opportunities, seeking to make a form of APL relevant for a new era and a new audience (students and teachers, not just professional programmers).

## Key Contributions
1.  **The Conceptual Re-founding of APL via J:** The paper documents the birth of J as a deliberate return to first principles. J’s key innovations—the ASCII-based spelling, the emphasis on “cells” and “items” via the rank operator, the use of “hooks” and “forks,” and the systematic use of the copula (`=:`) for function assignment—are presented as the mature realization of APL’s potential.
2.  **Terminology as Design Philosophy:** A central, often overlooked, contribution is the argument for terminology from natural language over mathematical jargon. Replacing “function/operator/noun” with “verb/adverb/conjunction/noun” is not cosmetic; it clarifies roles and relationships (e.g., an adverb “applies to a verb to produce a related verb”). This is a design decision aimed at lowering cognitive barriers for non-specialists.
3.  **Codification of the Dialect Families:** Iverson provides a clear taxonomy, identifying the two most influential families of APL: the **APL2 family** (maintaining the symbolic heritage) and the **J family** (advancing a textual, printable, and more functionally-oriented approach). This framework helps structure the subsequent history of the language.
4.  **A Blueprint for Tacit Programming in an Array Language:** While [[backus-1978-can-programming-be-liberated-from-the-von-neumann-style|Backus]] championed functional programming, Iverson shows how the specific features of J (hook, fork, derived functions) enable a powerful form of tacit programming—an argument is never named, allowing for highly composed, efficient, and mathematically clear code. This bridges the gap between array-oriented and functional paradigms.

## Methodology
The methodology is **retrospective synthesis and polemical design**. Iverson is not conducting an experiment or proving a theorem. He is:
*   **Curating a Personal History:** He filters 35 years of collaborative development through his own evolving perspective, explicitly stating this is his “personal essay” and that citations don’t imply agreement.
*   **Making a Design Case:** The essay is structured as a series of comparisons between early choices (mathematical terms, custom glyphs) and later, refined ones (natural language terms, ASCII spelling). This constitutes an argument by design, where the “evidence” is the elegance and pedagogical utility of the later choices.
*   **Laying Out a Manifesto:** The initial list of requirements for a teaching dialect (shareware, printable, general) serves as the problem statement, and the description of J is the proposed solution. The methodology is fundamentally that of a designer-philosopher justifying a lineage of decisions.

## Influence
This paper solidified the intellectual foundations for the J language and community, distinguishing it sharply from commercial APL. Its influence radiates in several directions:
*   **Direct Lineage:** It inspired and informed the development of other modern array languages, notably **K** (by Arthur Whitney, who helped start J) and **Q** (built on K), which dominate in high-frequency finance. The focus on compactness, performance, and tacit composition stems from this Iversonian vision.
*   **Academic and Pedagogical:** It reinvigorated the argument for executable notation in education, directly leading to projects like **J for Education** and materials like *Tangible Math*.
*   **Influence on Programming Language Theory:** The clear separation of word formation (lexing) from parsing in J’s implementation is a notable contribution to language design, often cited as an example of clean, table-driven architecture.
*   **Citation and Discourse:** The paper is a primary source for understanding the evolution of APL, widely cited in histories of programming languages and in discussions about notation, tacit programming, and the pedagogy of computing. It frames the “APL vs. J” dialectic as a philosophical divide about accessibility versus symbolic purity.

## Connections to Other Papers in the Collection
*   **[[bush-1931-the-differential-analyzer|Bush]] 1945 (As We May Think):** Both [[bush-1931-the-differential-analyzer|Bush]] and Iverson envision tools that augment human thought. [[bush-1931-the-differential-analyzer|Bush]]’s Memex is a hypertext machine; Iverson’s APL/J is an executable mathematical notation. Both are fundamentally about **externalizing and manipulating thought** with new technological media.
*   **[[engelbart-1960-games-that-teach-the-fundamentals-of-computer-operation|Engelbart]] 1962 (Augmenting Human Intellect):** [[engelbart-1960-games-that-teach-the-fundamentals-of-computer-operation|Engelbart]]’s “conceptual framework” for augmentation—language, artifacts, methodology—finds a concrete counterpart in APL. APL is both a new language and a new artifact for intellectual work, and Iverson’s focus on teaching aligns with [[engelbart-1960-games-that-teach-the-fundamentals-of-computer-operation|Engelbart]]’s goal of boosting “capability” to tackle complex problems.
*   **[[backus-1978-can-programming-be-liberated-from-the-von-neumann-style|Backus]] 1978 (FP):** This is the most direct philosophical dialogue. Iverson’s work in J can be seen as an *applied answer* to [[backus-1978-can-programming-be-liberated-from-the-von-neumann-style|Backus]]’s challenge to move beyond the “von Neumann bottleneck” and embrace functional, higher-order programming. Iverson’s tacit programming is his array-oriented implementation of this functional ideal, demonstrating it can be practical and efficient.
*   **[[papert-1980-mindstorms-1st-ed|Papert]] 1980 (Mindstorms):** Papert’s “mathematics of programming” and his advocacy for children to “command the computer” as a personal tool resonate deeply with Iverson’s pedagogical mission for J. Both see computing not as a vocational skill but as a medium for intellectual exploration and empowerment.
*   **[[thurston-1990-mathematical-education|Thurston]] 1994 (Proof and Progress):** [[thurston-1990-mathematical-education|Thurston]] argues that mathematical understanding is a social, conceptual artifact, not just a chain of formal proofs. Iverson’s APL philosophy aligns: the notation is a tool for building and sharing *understanding*, not just for writing correct code. The goal is to make mathematical ideas tangible and manipulable.
*   **[[lockhart-2002-a-mathematicians-lament|Lockhart]] 2002 (Mathematician’s Lament):** [[lockhart-2002-a-mathematicians-lament|Lockhart]] decries the rote, de-contextualized teaching of “mathematics” (as procedures). Iverson’s entire project with J and *Tangible Math* is a direct response to this lament. He provides the tool to teach mathematics as a creative, exploratory, and *executable* art.

## Modern Relevance
Iverson’s arguments are strikingly prescient for today’s landscape of AI, data science, and low-code/no-code tools.
*   **Array-Oriented Thinking for AI:** The core of modern AI—tensor operations in PyTorch or TensorFlow—is array programming. Iverson’s relentless focus on array dimensions, ranks, and operations over them (reduction, scan) is the conceptual bedrock for this. J’s explicit handling of “cells” and “items” is a clearer, more general model for tensor broadcasting than ad-hoc rules.
*   **The Quest for Executable Notation:** The dream of a “simple, precise, executable notation” lives on in tools like Jupyter notebooks, which blend prose, code, and output. Iverson’s critique—that our tools should serve learning and thinking, not just compilation—challenges this ecosystem to be more mathematically pure and concise. Projects in **live-coding** and **reactive programming** echo this desire for immediacy.
*   **Tacit Programming and Modern Languages:** The trend toward anonymous functions, composition operators (`.`), and functional pipelines in languages like Python, JavaScript, and Swift validates Iverson’s push for tacit programming. J’s “hooks” and “forks” are an elegant, unified model for these increasingly common patterns.
*   **The Democratization of Tools:** Iverson’s requirement for “shareware” and cross-platform access pre-figures the open-source movement and the app economy. His fight against the “onerous” custom alphabet is a historical parallel to today’s battles over proprietary file formats, walled-garden app stores, and the need for interoperable, open tools for knowledge work.

## Key Quotes

1. > “I continue to believe that its most important use remains to be exploited: as a simple, precise, executable notation for the teaching of a wide range of subjects.”
    *   **Analysis:** This is the mission statement. It reframes APL/J not as a programming language in the commercial sense, but as a **notation for thought**, elevating its purpose from utility to epistemology.

2. > “The present discussion is organized by topic, tracing the evolution of the treatments of arrays, functions, and operators; as well as that of other matters such as function definition, grammar, terminology, and spelling (that is, the representation of primitives).”
    *   **Analysis:** This reveals Iverson’s design-as-linguistics approach. He treats programming language creation as a holistic problem of semantics, grammar, and even orthography, akin to constructing a constructed language (conlang) for formal thought.

3. > “Not only are they familiar to a broader audience, but they clarify the purposes of the parts of speech... A verb specifies an ‘action’ upon a noun... An adverb applies to a verb to produce a related verb...”
    *   **Analysis:** This encapsulates the shift from mathematical to natural-language terminology as a core usability principle. The language’s syntax should mirror its conceptual structure, making it more intuitive.

4. > “These facilities permit the extensive use of tacit programming in which the arguments of a function are not explicitly referred to in its definition, a form of programming that requires no reparsing of the function on execution, and therefore provides some of the efficiency of compilation.”
    *   **Analysis:** This is a crucial technical and philosophical point. It argues that a higher-level, more abstract style (tacit) can simultaneously be *more efficient* than a lower-level, explicit one, by eliminating runtime overhead. It’s a rejection of the “higher-level means slower” trope.

5. > “The set of graphics in ASCII is much richer than the meager set available when the APL alphabet was designed... A much simpler scheme using words of one or two letters was adopted in J, in a manner that largely retains, and sometimes enhances, the international mnemonic character of APL words.”
    *   **Analysis:** This justifies a fundamental break from APL tradition. It acknowledges that technological constraints (the custom alphabet) had become a barrier to adoption, and that a careful redesign could preserve philosophical purity while achieving practical accessibility.