---
title: Kay 2001 - Software - Art, Engineering, Mathematics, or Science
created: 2026-06-10
updated: 2026-06-10
type: entity
tags: [computing-history, programming-languages, mathematics, physics]
sources: [raw/papers/Kay_2001_-_Software-_Art,_Engineering,_Mathematics,_or_Science.txt]
confidence: high
---

# [[kay-1968-flex-a-flexible-extendable-language|Kay]] 2001 - Software: Art, Engineering, Mathematics, or Science?

## Core Thesis
Alan [[kay-1968-flex-a-flexible-extendable-language|Kay]] argues that the discipline of [[meyer-1989-the-new-culture-of-software-development|software development]] is not a mature field. It is not engineering, science, or mathematics in any developed sense, but rather a primitive, ad-hoc craft akin to pre-architectural construction. The core problem is that we cannot reliably build large, complex software systems from scratch in a predictable, learnable way. The solution is not to [[air-force-1960-air-force-office-of-scientific-research|force]] the label of "engineering" onto our current practices, but to build a true discipline by studying the large, important software systems we *do* create, treating them as phenomena to be understood. This requires creating systems that are fundamentally *late-bound* and changeable, like the Squeak environment, so they can serve as both the object of study and the tool for building better systems. This creates a feedback loop of construction, analysis, and redesign, which is the only path to a genuine science and engineering of software.

## Historical Context
[[kay-1968-flex-a-flexible-extendable-language|Kay]] writes in 2001, a period of profound frustration in the software industry. The "software crisis" identified in the late 1960s had not been solved; it had merely been managed with varying degrees of success. Large projects like the FBI's Virtual Case File system were failing spectacularly. The field was dominated by a "cookbook" approach, where practitioners used recipes (design patterns, methodologies) that had "somewhat worked in the past," without a foundational understanding. The term "Software Engineering" was coined in 1968, but by 2001, [[kay-1968-flex-a-flexible-extendable-language|Kay]] still considers it an "oxymoron."

The intellectual backdrop includes decades of debate on the nature of computing. Is it applied mathematics (as embodied by formal verification efforts)? Is it a branch of engineering (focused on process and reliability)? Or is it a new kind of science? [[kay-1968-flex-a-flexible-extendable-language|Kay]] engages with this lineage, dismissing the simple application of [[scientific-american-1966-information-june-1966|scientific]] or mathematical models as insufficient. He contrasts the synthetic nature of computing ("we start with rules and compute a kind of 'reality'") with the analytic nature of traditional science. His call is to study the *artifacts* we build as a natural sc[[scientific-american-1966-information-june-1966|ience, an ]]approach reminiscent of the "new kind of [[scientific-american-1966-information-june-1966|scientific]] engineering" developed for physical structures like bridges and buildings, which cannot be analyzed purely from first principles.

## Key Contributions
1.  **The Disciplinary Critique:** A clear, memorable articulation of why "software engineering" and "[[hamming-1968-one-mans-view-of-computer-science|computer science]]" are premature or misleading labels. He provides the foundational analogy of the pyramid versus the[[air-force-1960-air-force-office-of-scientific-research| Empi]]re State Building to illustrate the gap between brute-[[air-force-1960-air-force-office-of-scientific-research|force]] accumulation and designed construction.
2.  **The Science of Artifacts:** Proposes a specific methodology for progress: build important, large software systems *and* design them to be objects of study. This reframes the goal from merely producing software to producing *understanding* through the analysis of software systems.
3.  **Extreme Late Binding as a Core Principle:** Positions the principle of late binding (deferring decisions and bindings as long as possible) as the "secret weapon" for achieving malleability. He traces its history from hardware (relocation registers) to software (objects, metaprogramming), arguing it is the key to creating systems that are analyzable and changeable.
4.  **Squeak as a Proto-Discipline:** Introduces Squeak not as a mere tool or language, but as a *manifesto in code*. It is a system designed to be completely visible, mutable, and educational, embodying the principle that the "system is the curriculum." It is presented as a prototype for the kind of artifact that could enable a real science of software.
5.  **The Call to "Extreme Play":** A polemical instruction to the reader to treat the system as a metalanguage, to modify its foundations, and to invent new deep features. This is an explicit rejection of passive tool usage in favor of transformative engagement, positioning the programmer as a research scientist in their own right.

## Methodology
[[kay-1968-flex-a-flexible-extendable-language|Kay]]’s methodology is **polemical analogy and design-based argumentation**. He does not present empirical data or formal proofs. I[[meyer-1989-the-new-culture-of-software-development|nstead, he uses:
*  ]] **Historical Analogy:** Comparing software development to pre-architectural building and physical engineering.
*   **Philosophical Distinction:** Carefully separating the temperaments and concerns of mathematics (truth), science (reality), and engineering (construction).
*   **Exemplary Artifact:** Using the [[clark-d-1988-the-design-philosophy-of-the-darpa-internet-protocols|design philosophy]] of Squeak as the concrete proof-of-concept for his abstract argument. The system itself is the evidence for what a "late-bound" approach enables.
*   **Provocative Reframing:** Re-labeling core activities (calling Squeak a "metalanguage," urging "extreme play") to shift the reader's mindset from user to creator/researcher.

The argument is structured as a diagnosis, a proposed treatment protocol, and a demonstration of a therapeutic agent. It is inherently rhetorical, aimed at inspiring a change in practice and self-perception among developers.

## Influence
This foreword crystallized and amplified ideas [[kay-1968-flex-a-flexible-extendable-language|Kay]] had been developing since the 1970s (e.g., in his "The Early History of Smalltalk"). It became a seminal text for the **constructivist** and **human-centered** approaches to computing.
*   It directly influenced the **Squeak community and educational technology movement**, framing Squeak and its successors (like Scratch) as environments for "learning by making" and systemic understanding.
*   The argument for late binding and malleable systems is a direct philosophical ancestor of **live coding, end-user programming, and the "software as[[meyer-1989-the-new-culture-of-software-development| material" movement*]]* (e.g., Bret Victor's work).
*   It provided a powerful critique absorbed by the **agile software development** community, which shares its distrust of rigid, upfront "engineering" processes, though [[kay-1968-flex-a-flexible-extendable-language|Kay]]'s solution is more radical (changing the system itself, not just the process).
*   The idea of studying software systems as artifacts connects to modern **software archaeology and mining software repositories**, though [[kay-1968-flex-a-flexible-extendable-language|Kay]]'s focus is on *designed* malleability for study, not just analyzing legacy code.

## Connections to Other Papers in the Collection
*   **[[engelbart-1962-augmenting-human-intellect-typeset|Engelbart 1962]] ([[engelbart-1962-augmenting-human-intellect|Augmenting Human]] Intellect):** Shares the goal of using computers to improve human capability, but [[kay-1968-flex-a-flexible-extendable-language|Kay]] focuses more on the malleability of the tool itself as the key to intellectual augmentation.
*   **[[kay-1972-personal-computer-for-children|Kay 1972]] ([[kay-1972-a-personal-computer-for-children-of-all-ages|Personal Computer]]):** This 2001 foreword is the mature philosophical underpinning of the vision sketched in the 1972 Dynabook proposal. The "meta-language" concept realizes the earlier dream of a [[kay-1976-personal-dynamic-media-lrg|personal dynamic]] medium.
*   **[[papert-1980-mindstorms-1st-ed|Papert 1980]] (Mindstorms):** The "system as curriculum" and learning-by-modifying directly extends [[papert-2000-whats-the-big-idea-toward-a-pedagogy-of-idea-power|Papert]]'s constructionist learning theory, moving it from Logo to the entire system level.
*   **[[feynman-1974-cargo-cult-science|Feynman 1974]] (Cargo [[feynman-1974-cargo-cult-science|Cult Science]]):** [[kay-1968-flex-a-flexible-extendable-language|Kay]] is urging a move away from "[[feynman-1974-cargo-cult-science|cargo cult]] engineering" (imitating the forms of engineering without the substance) towards a practice grounded in genuine, iterative learning from reality—which, in computing, is the reality of the systems we build.
*   **[[thurston-1994-on-proof-and-progress-in-mathematics|Thurston 1994]] (Proof and Progress):** Both authors argue that progress in a field comes from the creation of new *concepts and perspectives*, not just solving predefined problems. [[kay-1968-flex-a-flexible-extendable-language|Kay]]'s "extreme play" is a call to create new programming concepts.
*   **[[hofstadter-2001-analogy-as-the-core-of-cognition|Hofstadter 2001]] (Analogy):** [[kay-1968-flex-a-flexible-extendable-language|Kay]]'s entire argument is built on a series of layered analogies (pyramids, bridges, sciences) to make his case about the nature of software.
*   **[[lockhart-2002-mathematicians-lament|Lockhart 2002]] (Mathematician's Lament):** Both texts are fierce critiques of their fields for confusing the *mechanics* of the discipline (syntax, proofs, building code) with the *creative, exploratory soul* of it (problem-solving, beauty, understanding). [[kay-1968-flex-a-flexible-extendable-language|Kay]]'s call to treat Squeak as a playground for invention parallels [[lockhart-2002-mathematicians-lament|Lockhart]]'s call to treat mathematics as art.

## Modern Relevance
[[kay-1968-flex-a-flexible-extendable-language|Kay]]'s critique remains strikingly relevant. The industry's scale has increased exponentially, making the "pyramid" problem even more acute. His proposed solution resonates in several contemporary trends:
*   **AI and Large Language Models:** The current AI paradigm is the ultimate "synthetic" reality. [[kay-1968-flex-a-flexible-extendable-language|Kay]]'s call for a science of the artifacts we build is urgent: we need to treat neural networks and AI systems not as black-box tools, but as malleable artifacts to be studied, understood, and redesigned from first principles to avoid creating inscrutable, fragile systems.
*   **Metaprogramming and AI-Assisted Coding:** The idea of systems that can reason about and rewrite their own code (meta-programming) is now being supercharged by AI. [[kay-1968-flex-a-flexible-extendable-language|Kay]]'s vision of a "metalanguage" is being realized in tools like GitHub Copilot, but his emphasis on human understanding and control is a crucial caution against abdication.
*   **Education and Knowledge Work:** The "system as curriculum" idea is the foundation of modern constructionist educational tools (from Scratch to Jupyter notebooks). It argues that the best way to understand [[cook-2000-how-complex-systems-fail|complex systems]] (like knowledge itself) is to build and manipulate representations of them.
*   **Open Source as [[scientific-american-1966-information-june-1966|Scientific]] Method:** The open-source movement's practice of exposing all code for scrutiny and forking is an accidental implementation of [[kay-1968-flex-a-flexible-extendable-language|Kay]]'s "build it in a form that allows analysis." However, few projects are designed from the ground up for malleability and study in the Squeak sense.

[[kay-1968-flex-a-flexible-extendable-language|Kay]]’s foreword is a demand that we stop being passive users of computing metaphors and become active scientists of the digital world we are constructing.

## Key Quotes
1.  **"I interpret this to mean that 'Software Engineering' is still an oxymoron."**
    *   *Analysis:* The paper's provocative thesis statement. It dismisses the field's chosen name as a premature and misleading aspiration, forcing a re-examination of its foundations.
2.  **"We need to do more building of important software structures, and we need to do it in a form that allows analysis, learning, and reformulating the design and fabrication from what has just been learned."**
    *   *Analysis:* The core methodological prescription. It defines a circular, empirical process: build, study, redesign. This is the engine of the proposed "science."
3.  **"I believe that the secret weapon that can be used to make progress here is extreme late bi[[scientific-american-1966-information-june-1966|nding."**
]]    *   *Analysis:* Identifies the single, crucial design principle that enables the entire [[scientific-american-1966-information-june-1966|scientific]] cycle. Late binding provides the flexibility needed to study and change a system without starting from scratch.
4.  **"Consider Squeak as a metalanguage that can build languages."**
    *   *Analysis:* Reframes the purpose of the software system. It is not a tool for writing programs, but a meta-tool for creating new ways of expression and thought, elevating the programmer's role.
5.  **"The system is the curriculum."**
    *   *Analysis:* The pedagogical mantra. It states that understanding comes not from external documentation, but from direct engagement with a transparent, changeable system. The artifact teaches about itself.
6.  **"We not only give permission for you to do this, we urge you to try! Why? Because our field is still a long way from a reasonable state, and we cannot allow bad defacto standards (mostly controlled by vendors) to hold back progress."**
    *   *Analysis:* A call to arms against complacency and proprietary control. It positions the act of modifying a foundational system as a necessary, ethical act for the advancement of the field.
7.  **"At some point a much better system than Squeak will be created, and nothing could make us happier -- especially if you can do it while we're still around to [[scientific-american-1966-information-june-1966|enjoy the ]]new ideas!"**
    *   *Analysis:* The ultimate goal is not the preservation of a system (Squeak), but the progress of ideas. This embodies the [[scientific-american-1966-information-june-1966|scientific]] ethos: building a platform for others to surpass.