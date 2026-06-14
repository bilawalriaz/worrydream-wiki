---
title: Borning 1981 - The Programming Language Aspects of ThingLab
created: 2026-06-10
updated: 2026-06-10
type: entity
tags: [computing-history, hci, programming-languages, mathematics]
sources: [raw/papers/Borning_1981_-_The_Programming_Language_Aspects_of ThingLab.txt]
confidence: high
---

# Borning 1981 - The Programming Language Aspects of ThingLab

## Core Thesis
Alan Borning's paper argues that integrating **declarative constraints** into an **object-oriented programming environment** fundamentally transforms the creation of interactive, graphic simulations. The core thesis is not merely technical; it is a proposition about a new paradigm for human-computer interaction and knowledge representation. Borning contends that constraints, as bidirectional relations maintained automatically by the system, liberate users from the "mechanical bookkeeping" of conventional programming. When combined with the modularity of objects and the taxonomic power of inheritance hierarchies, constraints enable a system where the user specifies *what* relations must hold, and the system deduces *how* to maintain them. The nuance lies in the successful resolution of a key tension: object-oriented systems promote local, message-passing interaction, while constraint satisfaction requires global analysis of interconnected dependencies. ThingLab demonstrates that these metaphors can be integrated, with objects providing the natural modularity needed to scope constraints and compute incremental updates.

## Historical Context
ThingLab emerges from two powerful lineages at Xerox [[parc-1971-parc-papers-for-pendery-and-planning-purposes|PARC]] in the late 1970s:
1.  **The Direct Manipulation Tradition:** Ivan Sutherland's **Sketchpad (1963)** established the vision of interactive graphics where users manipulate visual objects directly. It introduced constraints (e.g., "these two lines are parallel") and recursive merging (creating instances from masters). However, Sketchpad's constraints were limited in scope and lacked a sophisticated underlying programming model.
2.  **The Object-Oriented Revolution:** **Smalltalk (1972-1980)**, created by Alan Kay and his colleagues, provided a clean, powerful object-oriented language centered on message passing, classes, instances, and inheritance. It was the ideal substrate for building flexible, modular systems.

The problem Borning addresses is the next logical step: how to create a *dynamic* simulation environment where relationships are not static, but are continuously enforced in real-time as the user interacts with objects. Existing systems like Sketchpad were either domain-specific drawing tools or lacked the expressiveness and modularity of a full object-oriented language. The state of the field lacked a general-purpose mechanism for binding together the graphic, symbolic, and behavioral aspects of an interactive model. ThingLab aims to be a "kit-building kit"—a meta-environment for constructing domain-specific simulation toolkits (for physics, geometry, etc.).

## Key Contributions
ThingLab introduced or pioneered several interconnected ideas that significantly advanced programming language design and interactive systems:

1.  **Bidirectional, Procedural Constraints:** Constraints in ThingLab are not just boolean tests; they are objects with associated *methods* that can "fire" to restore satisfaction. This makes them inherently bidirectional. For a constraint like `x = y + 1`, a change to `x` can trigger a method that adjusts `y`, and vice versa. This is a fundamental step beyond unidirectional dataflow.
2.  **Incremental Constraint Satisfaction via Compilation:** To achieve interactive speed, Borning devised a two-phase approach: a **planning phase** that analyzes the constraint graph and determines an order of operations, and a **compilation phase** that generates efficient Smalltalk code to execute that plan. This incremental compilation is a key innovation for real-time interactivity.
3.  **Integration of Constraints with Multiple Hierarchies:** ThingLab formally integrates three types of relationships:
    *   **Constraint Hierarchy:** Defines mathematical/logical relations.
    *   **Part-Whole Hierarchy:** Defines structural composition (e.g., a triangle is made of three points).
    *   **Inheritance Hierarchy:** Defines taxonomic similarity (a `BouncyBall` is a subclass of `Ball`).
    Borning provides explicit mechanisms (like "path" expressions and "prototype" objects) to navigate and reference across these hierarchies, solving a major problem in combining modularity with constraint-based systems.
4.  **Class Definition by Example:** Users could create new classes of objects not by writing code, but by constructing a prototypical instance on screen, manipulating it, and then abstracting it into a class definition. This made the system's extensibility accessible to a wider, more visually-oriented audience.

## Methodology
The methodology is **design-based research**, characteristic of systems-building work in computer science. The argument is structured as follows:
1.  **Problem Formulation:** Define the requirements for a general-purpose interactive simulation environment.
2.  **Conceptual Integration:** Propose a theoretical framework that synthesizes constraints, objects, and inheritance.
3.  **System Implementation:** Build a concrete, runnable prototype (ThingLab in Smalltalk-76) that embodies this framework.
4.  **Demonstration and Argument:** Use the implemented system as both a proof of concept and a vehicle for exploration. The paper's evidence consists of:
    *   **Examples of Simulations:** Concrete demonstrations of geometric figures, electrical circuits, and a graphic calculator.
    *   **Architectural Explanation:** Detailed description of how constraints are represented, how satisfaction is achieved, and how hierarchies are linked.
    *   **Analysis of Trade-offs:** Honest discussion of limitations, such as the difficulty of handling circular constraints or the computational cost of planning.
The paper is **polemical** in the sense that it advocates for a new programming paradigm, using the working system as the primary argument.

## Influence
ThingLab's influence was profound and direct, seeding several important research and product lines:

*   **Direct Descendants:** It led to **Kaleido**, a constraint language for interactive graphics developed by Borning and his students at the University of Washington, and later to **Belding** and **ThingLab II**, which further explored constraint solving.
*   **The Wave of Constraint UIs:** Ideas from ThingLab directly informed the design of constraint-based UIs in products like **Microsoft Excel** (constraint-based spreadsheets) and research systems like **Fabrik** (a visual, constraint-based programming environment). The concept of "dataflow" in visual programming owes much to this work.
*   **Reactive and Live Programming:** ThingLab is a foundational precursor to modern "reactive" programming paradigms and "live" coding environments where data flows automatically through declared dependencies. Systems like **React.js** in web development embody a similar philosophy of declaring UI as a function of state, with the framework handling updates.
*   **Educational Technology:** Its emphasis on interactive, visual manipulation of mathematical and physical models influenced educational software and the development of tools like **GeoGebra**.

## Connections to Other Papers in the Collection
*   **Kay 1972 (Personal Computer):** ThingLab is a direct realization of Kay's vision of the computer as a "medium for creative thought." It transforms the PC from a document generator into a personal, interactive laboratory for exploring dynamic models.
*   **[[engelbart-1960-games-that-teach-the-fundamentals-of-computer-operation|Engelbart]] 1962 (Augmenting Human Intellect):** Borning's work is a powerful example of "augmenting" a specific intellectual activity—scientific and geometric reasoning—by providing tools that directly manipulate the symbolic representations (constraints, objects) of that domain.
*   **[[bush-1931-the-differential-analyzer|Bush]] 1945 (As We May Think):** While not about a memex, ThingLab's "kit-building kit" concept parallels Bush's idea of associative trails. Users build trails of constraints and object relationships that dynamically link pieces of knowledge in a manipulable space.
*   **[[papert-1980-mindstorms-1st-ed|Papert]] 1980 (Mindstorms):** Both Borning and [[papert-1980-mindstorms-1st-ed|Papert]] champion constructionist learning through interactive manipulation of formal systems. ThingLab could be seen as a "mathland" for exploring physics and geometry, where the user manipulates the laws themselves (constraints) rather than just the objects.

## Modern Relevance
ThingLab's core ideas are more relevant today than ever, especially in the context of AI and knowledge work:

1.  **Declarative UI and State Management:** Modern frameworks (React, Vue, SwiftUI) are built on the principle that UI is a declarative function of state. This is a direct intellectual descendant of Borning's insight that relations should be declared, not imperatively managed. The "constraint" is the mapping from state to view.
2.  **AI Planning and Reasoning:** Borning's two-phase approach (plan then execute) mirrors how modern AI systems work. A large language model (LLM) performing a complex task might first "reason" or "plan" (the planning phase) and then generate a sequence of actions (the compiled code). The challenge of handling circular constraints is analogous to complex planning with feedback loops.
3.  **Digital Twins and Simulation:** The creation of interactive, real-time simulations of physical systems (digital twins) is a vast, modern industry. ThingLab is an early prototype of the principles needed: objects with state, connected by physical laws (constraints), all updated in real-time in a visual interface.
4.  **Knowledge Graphs and Ontologies:** The integration of part-whole and inheritance hierarchies with constraints foreshadows modern knowledge representation. In a knowledge graph, nodes are objects, edges are relations (constraints), and classes/taxonomies provide structure. ThingLab's methods are akin to "rules" or "reasoners" that infer new facts or maintain consistency in such graphs.

## Key Quotes

1.  > "In a constraint-oriented system such as ThingLab, the user can specify the relation between the text and the integer and leave it to the system to maintain that relation."
    *   **Commentary:** This is the core user-centric promise of the system. It shifts cognitive burden from the user to the machine, enabling direct manipulation of relationships rather than their procedural enforcement.

2.  > "Constraints in ThingLab are represented as a rule and a set of methods that can be invoked to satisfy the constraint. The rule is used by the system to construct a procedural test... the methods describe alternate ways of satisfying the constraint."
    *   **Commentary:** This technical definition reveals the clever dual nature of constraints as both declarative specifications (the rule) and imperative solutions (the methods). This duality is key to their power and flexibility.

3.  > "There is consequently a tension between the object and constraint metaphors; the integration of these approaches in ThingLab is one of its points of interest."
    *   **Commentary:** Borning explicitly names the central intellectual problem of his work: reconciling the locality of objects with the globality of constraints. This tension remains a design challenge in distributed systems and complex software architectures.

4.  > "ThingLab is not a general-purpose language, many of the concepts and techniques described here would be useful in such a context. A promising direction for future research is to explore the design of a full constraint-oriented programming language."
    *   **Commentary:** A prescient statement. Borning correctly identifies his work as a proof of concept for a broader paradigm. This call has been answered in subsequent decades by languages like Oz, Swift (with its value binding), and declarative UI frameworks.

5.  > "To move a vertex of the triangle, the user should be able to point to it on the screen and drag it along with a pointing device, seeing it in continuous motion, rather than pointing to the destination and having the triangle jump suddenly."
    *   **Commentary:** This describes the gold standard for interactive design that we now take for granted. Borning articulates the goal of **real-time, fluid interaction** where the system's internal model is seamlessly synchronized with the user's actions.