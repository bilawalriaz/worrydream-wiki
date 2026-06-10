---
title: Kay 2006 - STEPS proposal
created: 2026-06-10
updated: 2026-06-10
type: entity
tags: [computing-history, hci, programming-languages, mathematics]
sources: [raw/papers/Kay_2006_-_STEPS_proposal.txt]
confidence: high
---

# Kay 2006 - STEPS proposal

## Core Thesis
The STEPS (Steps Toward The Reinvention of Programming) proposal argues that the foundational architecture of personal computing—its operating systems, applications, and development models—is a convoluted, non-scalable, and intellectually opaque mess. It proposes a radical alternative: to design and implement a complete personal computing system, from end-user interface down to hardware abstraction, in under 20,000 lines of code. The system must not only be practical but also serve as its own "self-exploratorium," a comprehensive model that is understandable, modifiable, and thus a true pedagogical tool for learning powerful computing ideas. The nuance is that this is not a mere technical optimization or a user-friendly layer on top of existing systems. It is a fundamental reconceptualization aimed at restoring the "mathematical" and "poetic" ideals of early personal computing, where whole systems could be held in one's mind, contrasting sharply with the accidental, bloated complexity of commercial software.

## Historical Context
This proposal is the culmination of Alan Kay's lifelong critique of mainstream computing's evolution away from the vision of personal computing as a "metamedium" for thought amplification. By 2006, the field was dominated by monolithic, opaque operating systems (Windows, Mac OS, Linux), specialized application silos, and the ad-hoc, hyperlink-not-hypermedia architecture of the web. Programming had become largely synonymous with navigating vast, pre-built libraries and frameworks, obscuring fundamental concepts. Kay's own prior work (Smalltalk, Dynabook concepts, Squeak) demonstrated the power of compact, coherent systems but felt they had not gone far enough. The proposal explicitly diagnoses the core problem: a "mathematical entropy" where systems grow unnecessarily large, losing explanatory power and creative potential. It seeks to solve this by leveraging 30+ years of their own research into object-oriented systems, graphics, and educational computing to start fresh, applying first principles to eliminate accidental complexity.

## Key Contributions
1.  **The "Universal Object" as the Sole Primitive:** A system where *everything* (code, data, files, drivers, UI elements, documents) is a true object communicating via symmetric messaging. This eliminates the artificial distinctions between OS, apps, and media, enabling a fluid, composable "desktop publishing for everything" metaphor.
2.  **Elimination of Traditional OS/Applications Dichotomy:** Replaces layers of privileged monolithic code with a network-inspired model where functionality is provided by objects. Device drivers, for example, are not part of the core system but are safe, address-space-confined objects provided by devices themselves.
3.  **The System as its Own Model ("Exploratorium"):** The entire system is designed to be small enough, coherent enough, and instrumented enough to be completely understandable and modifiable by its users. This turns the system itself into a learning curriculum.
4.  **Novel Architectural Principles:** Introduces concepts like *invertible processes* (real-time checkpointing/versioning for safety), *labeled histories* for provenance, *protection via capabilities* and message confinement, and the separation of *meanings* (semantic intent) from *optimizations* (implementation tricks).
5.  **A New Bootstrapping Methodology:** Proposes bootstrapping the system in a novel way, likely using minimal, reflective cores that can grow and modify themselves, emphasizing the creation of tools that enable the creation of tools.

## Methodology
The argument is primarily **design-based and visionary**, grounded in a historical critique and an analysis of persistent architectural flaws. Kay employs a "proof by demonstration" ethos: the ultimate validation will be the construction of the system itself. The methodology draws on:
*   **Historical Analysis:** Tracing the lineage of problems in computing back to specific, avoidable design choices (e.g., tight coupling via procedure calls, the "stovepipe" application model).
*   **First-Principles Design:** Starting from the minimal viable requirements of personal computing (communication, media, protection, scripting) and designing a unified architecture from the ground up.
*   **Synthesis of Prior Research:** Drawing heavily on the authors' own extensive history (Smalltalk, Croquet's distributed objects, Squeak's media capabilities) to argue that the proposed pieces are not speculative but have been proven in isolation.
*   **Polemical Contrast:** Constantly contrasting their proposed approach with the "standard practice" to highlight its superior elegance and explanatory power.

## Influence
While the full STEPS system was never completed as envisioned, its ideas have had a profound, diffuse influence:
*   **Squeak, Etoys, and Scratch:** Directly descends from this line of thinking. Scratch, in particular, embodies the "universal object" metaphor for children, where sprites, scripts, and sounds are all interchangeable objects.
*   **Modern WebAssembly & Containerization:** The proposal's vision of safe, address-space-confined execution of foreign code (like drivers) prefigures modern ideas like WebAssembly modules and containerized microservices, which isolate functionality via standardized messaging interfaces.
*   **The "Software as Material" Movement:** Kay's ideas about systems being understandable, malleable, and instrumented for learning have influenced educational software and "live programming" environments (e.g., Pharo, Lively Kernel, certain aspects of modern IDEs).
*   **Discourse on Complexity:** It became a central reference point in discussions about software bloat, the importance of intellectual manageability, and the lost goals of software engineering. It is frequently cited in critiques of modern computing's opacity.

## Connections to Other Papers in the Collection
*   **Bush 1945 (As We May Think):** The STEPS proposal can be seen as a technical blueprint for realizing Bush's Memex. Kay's "universal object" and HyperCard-on-steroids vision directly extend the idea of associative trails across a personal, multimedia knowledge store.
*   **Engelbart 1962 (Augmenting Human Intellect):** Both share the goal of creating integrated systems to augment thought. STEPS is the software system design needed to make Engelbart's NLS-like augmentation accessible and personal, moving from specialized terminals to a universal, comprehensible medium.
*   **Kay 1972 (Personal Computer):** This is the mature, realized vision of the 1972 paper. It addresses the engineering and architectural specifics needed to create a true Dynabook, updating the 1970s hardware constraints with 2006's possibilities while staying true to the original educational and creative ideals.
*   **Papert 1980 (Mindstorms):** STEPS is the ultimate computational environment for Papert's constructionism. The "system as curriculum" is a direct implementation of learning-by-making, where the child/user can explore and modify the entire world they are creating in.
*   **Backus 1978 (FP):** Kay's critique of "procedure calls" as "gear meshing" and his emphasis on "symmetric messaging" directly engages with Backus's argument that assignment-based languages obscure the true nature of computation. STEPS seeks to build a system whose messaging is closer to the functional ideal's clarity and composability.
*   **Lockhart 2002 (Mathematician's Lament):** Kay's frustration with how computing ideas are taught echoes Lockhart's lament. STEPS is an attempt to build the instrument (the system) that would allow computing to be taught as a creative, exploratory art (like music), not just a set of rote procedures (like sheet music).

## Modern Relevance
*   **Against AI Opacity:** In the age of deep learning "black boxes," Kay's insistence on *explainability by design* is more critical than ever. A STEPS-like system would be the antithesis of a neural network: every action, from a UI click to a file save, would be traceable, inspectable, and understandable through its object model.
*   **The Web's Original Sin:** Kay's critique of the web's "ad hoc" architecture presciently identified the source of many of its current problems (security, poor media handling, lack of true programmability). A universal-object-based web (like his proposed system) could have provided a more robust and expressive foundation.
*   **Education & Knowledge Work:** The model of a "comprehensible system" is a direct challenge to modern education technology and knowledge tools (e.g., spreadsheets, slide decks, IDEs), which are often complex and opaque. It points toward tools that teach their own underlying principles.
*   **Hyperflash's Work:** This proposal is foundational to Hyperflash's philosophy. The drive to create tools that are not just functional but *understandable* and *educational*, focusing on the craft of building systems from the ground up, is a direct inheritance from Kay's vision.

## Key Quotes
1.  **"We make, not just to have, but to know."**
    *   *Analysis:* This is the core epistemological belief driving the entire proposal. It distinguishes their engineering-as-research from commercial engineering. The goal isn't just a product; it's the creation of new understanding.

2.  **"Our intuitive sense of 'mathematical entropy' insists that an even more comprehensive design approach... could be smaller by a factor of 10 or more."**
    *   *Analysis:* "Mathematical entropy" is Kay's powerful metaphor for accidental complexity and design debt. It frames bloated software not as inevitable, but as a failure of conceptual clarity and a violation of elegant, minimal principles.

3.  **"Most so-called object-oriented languages don't really use the looser coupling of messaging, but instead use the much tighter 'gear meshing' of procedure calls – this hurts scalability and interoperability."**
    *   *Analysis:* A precise technical diagnosis of a widespread flaw. It argues that the mainstream co-opted the term "object" while discarding its most powerful idea (message-passing), leading to fragile, tightly-coupled systems.

4.  **"A practical working system that is also its own model... could be an 'Exploratorium of itself'."**
    *   *Analysis:* Defines the revolutionary dual purpose of the system: it is both a tool and a pedagogical instrument. It must be transparent enough to be studied, thus enabling a deeper form of learning.

5.  **"The system could be compact, comprehensive, clear, high-level, and understandable enough to be a 'system to learn about systems'."**
    *   *Analysis:* This is the core technical challenge set forth. It's not just about small code size, but about *conceptual* compactness and clarity—a system where the architecture itself teaches fundamental ideas.

6.  **"One metaphor that might help... is 'HyperCard on Steroids'. To do this one would extend HyperCard to have any number of useful objects, allow all to be scripted, and allow the hyperCards to be both full-fledged media pages... and to recursively be its own embedded media objects."**
    *   *Analysis:* Provides a concrete, relatable vision for the "universal object" idea. It grounds the abstract architecture in a familiar, powerful user experience (composable, scriptable media) that already existed in a limited form.