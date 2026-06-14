---
title: Ungar 2007 - Self (HOPL)
created: 2026-06-10
updated: 2026-06-10
type: entity
tags: [computing-history, hci, programming-languages, physics]
sources: [raw/papers/Ungar_2007_-_Self_(HOPL).txt]
confidence: high
---

# Ungar 2007 - Self (HOPL)

## Core Thesis
The core thesis of this retrospective is twofold, reflecting the dual nature of the Self project itself. Primarily, it argues that the Self language and its integrated environment (1986-1995) represented a cohesive, ambitious vision to make programmers "more productive and creative" by harmonizing a simple, powerful prototype-based language with a high-performance implementation and a direct-manipulation user interface that externalized cognitive load. The nuances are critical: the goal was not merely a new language, but a **unified whole** where the purity of the object model necessitated and inspired revolutionary implementation techniques, which in turn enabled a novel, responsive interface. Secondarily, and more pointedly, the paper argues that while this holistic vision remains unfulfilled in the mainstream, its individual components have been profoundly influential, often in ironic or diffuse ways. The language's prototype model was sidelined, but its dynamic optimization techniques became foundational to mainstream virtual machines for more conservative languages like Java. The paper serves as both a celebration of these technical contributions and a lament for the lost potential of the integrated dream.

## Historical Context
The paper meticulously grounds Self in the specific intellectual ecosystem of Xerox [[parc-1971-parc-papers-for-pendery-and-planning-purposes|PARC]] in the early 1980s, dominated by the legacy of Smalltalk. The problem being solved was a perceived limitation of Smalltalk: despite its power and directness, it was not "pure" (it had primitive types and classes were objects of a special metaclass) and its performance was a bottleneck that limited expressiveness. Ungar and [[smith-da-2003-croquet-a-collaboration-system-architecture|Smith]] sought to "improve upon Smalltalk by increasing both expressive power and simplicity, while obtaining a more concrete feel."

This aspiration emerged from two direct inspirations: **Randall Smith's Alternate Reality Kit (ARK)**, which demonstrated a world of live, interacting objects animated with physics and direct manipulation, and **David Ungar's frustration** with Smalltalk's performance on contemporary hardware. The historical context is thus one of post-Smalltalk refinement, a desire to push the Smalltalk paradigm further toward its own philosophical ideals of universality and direct engagement, while solving the engineering hurdle that prevented such dynamism from being practical. The design phase occurred at Xerox [[parc-1971-parc-papers-for-pendery-and-planning-purposes|PARC]] (1986), and the implementation phase moved to Stanford and then Sun Microsystems (1991), situating the project in premier industrial and academic research labs during a period of rapid computer science advancement.

## Key Contributions
The Self project's contributions were manifold, spanning language design, virtual machine implementation, user interface research, and programming environments.

1.  **Prototype-Based Object Model:** Self pioneered and thoroughly explored a pure prototype-based system for mainstream programming. Unlike class-based systems (Smalltalk, C++), objects clone other objects directly. This eliminated the class/object dichotomy, achieving greater uniformity and dynamic flexibility. All state and behavior are held in objects, and message passing is the sole mechanism for computation.
2.  **Dynamic Compilation and Optimization Techniques:** This is arguably Self's most enduring technical legacy. To make its dynamic language efficient, the Self VM team invented:
    *   **Customization and Splitting:** Techniques for specializing methods for particular receiver types.
    *   **Type Prediction:** Inferring the likely type of an object to generate better machine code.
    *   **Polymorphic Inline Caches (PICs):** Efficiently handling message sends to objects of multiple types.
    *   **Adaptive Optimization:** Dynamically recompiling hot code paths with improved, type-specialized versions.
    *   **Dynamic Deoptimization:** Reverting from optimized code to the interpreter when assumptions (like a predicted type) are invalidated, a critical component for a stable, speculatively optimized VM.
3.  **Integrated User Interface & Environment:** Self pioneered:
    *   **Cartoon Animation for Legibility:** Using animation not as decoration, but as a tool to make changes in dynamic graphs (like object space) comprehensible to the human mind.
    *   **Morphic:** A direct-manipulation, object-centered UI toolkit built within Self, demonstrating a uniform "use-mention" distinction (objects in the system are the widgets you manipulate).
    *   **An Exploratory, Multi-User Environment:** A programming environment designed for live, interactive exploration of objects, which could also support distributed users.

## Methodology
The paper's methodology is **historical narrative and analytical retrospection**. It is structured as a four-part autobiography of a project: (1) Personal and professional histories leading to the design, (2) The design and evolution of the technology, (3) An assessment of its impact, and (4) A personal retrospective. The argument is built through a synthesis of:
*   **Technical Exposition:** Clear descriptions of the language, VM techniques, and UI innovations.
*   **Causal Analysis:** Tracing how one innovation (the pure language) forced another (the advanced VM), and how a personal frustration (Ungar's slow Smalltalk) redirected a career (from VLSI to VMs).
*   **Comparative Critique:** Continuously positioning Self against its predecessors (Smalltalk) and successors (C++, Java), evaluating trade-offs in simplicity, performance, and adoption.
*   **Personal Voice:** The inclusion of personal motivations (Smith's physics background, Ungar's father's advice) adds a layer of human-centered reasoning to the technical choices, framing them as expressions of a worldview.

## Influence
The influence of Self is profound but often invisible, as it was absorbed into the mainstream rather than adopted wholesale.
*   **Virtual Machines:** The adaptive compilation, inline caching, and type prediction techniques from Self directly informed the design of the **HotSpot Java Virtual Machine**, which became the dominant JVM. As the authors note, "ironically, the implementation techniques developed for Self thrive today in almost every desktop virtual machine for Java." This lineage is direct, via researchers like Urs Hölzle who moved from Self to Sun's Java group.
*   **Programming Languages:** The prototype-based object model, while not displacing class-based OOP in the mainstream, saw a resurgence in **JavaScript** (ECMAScript), which uses prototypes and dynamic dispatch. The paper explicitly notes JavaScript as a successor. The idea of extreme dynamism and a simple, uniform object model also influenced languages like **Lua** and **Ruby**.
*   **User Interface Research:** Concepts like using animation for legibility in dynamic interfaces and the object-centered, direct-manipulation environment influenced later work in information visualization and exploratory programming environments. The Morphic toolkit inspired similar systems.
*   **Academic Impact:** The project served as a crucial case study and testbed for ideas in programming language implementation, language design, and human-computer interaction for a generation of computer scientists.

## Connections to Other Papers in the Collection
*   **Kay 1972 (Personal Computer as Media):** Self is the direct philosophical descendant of the Smalltalk vision Kay outlines. It takes the Smalltalk ideal of a uniform, interactive "media" and pushes it toward greater purity and power. The focus on an exploratory, object-centered environment is a continuation of Kay's dream of computers as "metamedia."
*   **[[engelbart-1960-games-that-teach-the-fundamentals-of-computer-operation|Engelbart]] 1962 (Augmenting Human Intellect):** Self's integrated environment, with its direct manipulation and tools to offload cognitive burden, is a concrete implementation of Engelbart's goal to "augment human intellect." The focus on making complex system states (dynamic object graphs) legible through animation is a specific augmentation strategy.
*   **[[backus-1978-can-programming-be-liberated-from-the-von-neumann-style|Backus]] 1978 (FP):** Both [[backus-1978-can-programming-be-liberated-from-the-von-neumann-style|Backus]] and the Self team are driven by a quest for **simplicity and mathematical purity** as a source of power. [[backus-1978-can-programming-be-liberated-from-the-von-neumann-style|Backus]] sought it in functional, variable-free programming; Self sought it in a pure, uniform object model where everything is a message send. Both critiques stem from a dissatisfaction with the complexity and ad-hoc nature of contemporary languages.
*   **[[hoare-1981-the-emperors-old-clothes|Hoare]] 1973 (The Emperor's Old Clothes):** Ungar explicitly cites Hoare's call for simplicity as an aesthetic influence. The Self language's small size and uniformity are attempts to follow this ideal, contrasting with the growing complexity of languages like C++.
*   **[[lockhart-2002-a-mathematicians-lament|Lockhart]] 2002 (A Mathematician's Lament):** While about mathematics, Lockhart's core argument—that the soul of a discipline (creativity, exploration) is killed by an overemphasis on rigid procedure and assessment—resonates with Self's goal. Self was designed to allow programming to be more like an exploratory, creative "physics" and less like a formal, prescriptive chore.

## Modern Relevance
The relevance of Self is both direct and cautionary.
1.  **The Technical Legacy is Everywhere:** Modern **managed runtimes and JIT compilers** (for JavaScript, Java, C#, etc.) are built on a foundation of techniques (adaptive optimization, PICs) pioneered or perfected for Self. Understanding Self is understanding the engine under the hood of most high-level software.
2.  **The Vision of a Malleable, Live Environment Remains Aspirational:** Self's ideal of a programming environment that feels like manipulating a live physical world—where everything is inspectable, modifiable, and understandable in real-time—has not been mainstreamed. However, it lives on in modern **live coding environments**, **interactive notebooks** (Jupyter), **repls**, and research systems like **Smalltalk derivatives** (Pharo) and **Lively Kernel**. These systems chip away at the same problem: making the development process more exploratory and less mediated.
3.  **AI and Knowledge Work:** Self's environment can be seen as a sophisticated **knowledge management system** for program concepts. Its use of animation to represent dynamic relationships is a form of **externalized cognition**. As AI seeks to create tools that augment human reasoning and creativity (e.g., in code generation or scientific discovery), the principles of direct manipulation, live feedback, and reducing cognitive load through interface design, as explored in Self, become critically relevant. The gap between a powerful but opaque model (like a neural network) and human understanding is precisely the kind of gap Self's animated, interactive visualization aimed to bridge.

## Key Quotes
1.  > *"Self was designed to help programmers become more productive and creative by giving them a simple, pure, and powerful language, an implementation that combined ease of use with high performance, a user interface that off-loaded cognitive burden, and a programming environment that captured the malleability of a physical world of live objects."*
    **Analysis:** This is the project's manifesto. It outlines the four pillars (language, implementation, interface, environment) and explicitly states the human-centered goal: enhancing creativity and reducing cognitive burden.

2.  > *"Ironically, the implementation techniques developed for Self thrive today in almost every desktop virtual machine for Java™, a language much more conservative in design."*
    **Analysis:** This quote captures the central irony of Self's legacy. Its most successful innovations were extracted from their original, radical context and applied to sustain a different, more conventional paradigm. It highlights a common fate for visionary projects.

3.  > *"The computer is a blank canvas upon which programmers write their own laws of physics."* ([[smith-da-2003-croquet-a-collaboration-system-architecture|Smith]], quoted by Ungar)
    **Analysis:** This encapsulates the metaphysical underpinning of the Self project, inherited from the Smalltalk tradition. It frames programming not as engineering a static system, but as defining a dynamic universe, which directly motivated the need for a pure, uniform, and interactive object model.

4.  > *"The vision we tried to capture in the unified whole has yet to be achieved."*
    **Analysis:** This is the paper's melancholic but honest conclusion. Despite scattered technical successes, the integrated dream of language, tool, and interface working as one to revolutionize human-computer thought partnership remains a project for the future.

5.  > *"Simplicity and uniformity, particularly in its use of message passing for all computation, meant that a new approach to virtual machine design would be required for reasonable performance."*
    **Analysis:** This quote articulates the key driver of Self's technical innovations. The philosophical commitment to language purity directly created the engineering challenge that led to the creation of adaptive optimization, demonstrating how constraints breed creativity.