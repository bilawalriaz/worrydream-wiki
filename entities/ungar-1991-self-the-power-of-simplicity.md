---
title: Ungar 1991 - Self, The Power of Simplicity
created: 2026-06-10
updated: 2026-06-10
type: entity
tags: [computing-history, hci, programming-languages, design]
sources: [raw/papers/Ungar_1991_-_Self,_The_Power_of_Simplicity.txt]
confidence: high
---

# Ungar 1991 - Self, The Power of Simplicity

## Core Thesis
The paper argues that the dominant model of object-oriented programming—rooted in classes, instance variables, and methods—is an unnecessary conceptual complication. By radically simplifying the ontology of computation to just three ideas—prototypes, slots, and behavior—a language can achieve greater conceptual economy, flexibility, and expressiveness. The core nuance is not merely proposing "prototypes instead of classes," but demonstrating that merging data and procedures into a single construct ("slots") and eliminating variables fundamentally changes the nature of inheritance, scoping, and the relationship between objects, procedures, and closures. The thesis is that this simplicity isn't a lack of features, but a powerful foundation for a more uniform and dynamic computational model.

## Historical Context
The paper emerges from a period of ferment in object-oriented programming (OOP). The dominant paradigms, exemplified by Smalltalk-80, Simula, and later C++, were built on a strict separation between the description of an object (the class) and its use (the instance). This model provided clear structure but introduced conceptual overhead (class hierarchies, meta-classes for classes, instance variables distinct from methods) and rigidity.

Simultaneously, the concept of "prototype-based" languages, pioneered by Lieberman (1986), was gaining traction as a potential alternative. Ungar and Smith's work was a direct, rigorous, and influential formalization of this prototype idea. They were solving the problem of OOP's growing conceptual complexity and inflexibility, aiming to create a language for "exploratory programming" where the barrier between thinking about a problem and expressing a solution was minimized. Their work built directly on earlier prototype ideas but synthesized them into a coherent language design with specific, radical consequences.

## Key Contributions
1.  **The Prototype-Based Object Model:** Formalized a system where new objects are created by copying ("cloning") existing prototype objects, not by instantiating a class plan. This eliminates the class-instance duality, simplifying the "is a" vs. "kind of" relationships into a single "inherits from" link.
2.  **Slots as a Unified Construct:** Eliminated the distinction between instance variables (state) and methods (behavior). A "slot" is a named location in an object that contains any object. Accessing a slot with state (e.g., a number) and accessing one with behavior (e.g., a method) are the same operation: sending a message to "self" to retrieve the slot's value.
3.  **Inheritance as Dynamic Parent Lookup:** Without variables, state access is achieved via message passing. If an object doesn't have a slot for a message, the search recursively follows a "parent" pointer to other objects. This makes the inheritance hierarchy perform the work of lexical scoping.
4.  **Conflation of Object, Procedure, and Closure:** Procedures are not a special primitive. They are simply objects (activation records) with a "code" slot. Cloning a prototype procedure creates a new activation record (a closure), sharing the same mechanism as cloning any other object.
5.  **Simplification of Special Cases:** The model elegantly handles one-of-a-kind objects (e.g., `true` and `false` in Smalltalk) without needing dedicated singleton classes. Any object can have its own unique slots and behavior.

## Methodology
The paper is a **polemical design argument** structured as a comparative analysis. Its methodology is to:
*   **Establish a benchmark:** Use Smalltalk-80, the most familiar "pure" OOP language, as the primary point of comparison.
*   **Propose a new principle:** Present the three core ideas (prototypes, slots, behavior) and their guiding philosophies ("Messages-at-the-bottom," "Occam's razor," "Concreteness").
*   **Demonstrate conceptual reduction:** Systematically show how SELF's model subsumes or eliminates features from the Smalltalk model (classes, variables, special object creation for booleans, meta-regress).
*   **Provide concrete examples:** Use visual diagrams (Figures 1-3) to contrast object representations and creation processes, making the abstract argument tangible.
The argument is theoretical and analytical, grounded in language design principles rather than empirical performance data. It is a manifesto for a specific, minimalist vision of OOP.

## Influence
SELF was profoundly influential, not as a widely adopted language, but as a **research catalyst** and **design template**.
*   **Direct Language Lineage:** It inspired **NewtonScript** (for the Apple Newton), and crucially, **JavaScript**. Brendan Eich, JavaScript's creator, has explicitly cited SELF (and Scheme) as the core influences on its prototype-based object model. The ubiquity of JavaScript means SELF's ideas now permeate web development.
*   **Research in VM Implementation:** The SELF project became famous for its pioneering work in **optimizing dynamic object-oriented languages**. Techniques like **dynamic compilation (JIT), polymorphic inline caches, and hidden class optimizations**, developed to make SELF fast, became foundational to modern JIT compilers for Java, .NET, and JavaScript engines (V8, SpiderMonkey).
*   **Conceptual Impact:** It legitimized and popularized the prototype paradigm, shifting part of the OOP discourse away from class-centric design. It directly influenced later prototype-based languages like **Io**, **Lua** (which uses tables as universal prototypes), and arguably the object models in languages like **Python** (where everything is an object and classes are objects themselves).

## Connections to Other Papers in the Collection
*   **Kay 1972 (A Personal Computer for Children of All Ages):** Both papers share a deep commitment to **simplicity as a pathway to power** and to creating environments for **exploratory, active learning**. Kay's Dynabook vision requires a language that is flexible and not constrained by rigid abstractions; SELF's design is a direct technical response to that need. The slot model facilitates the kind of direct, malleable object manipulation Kay envisioned.
*   **[[papert-1980-mindstorms-1st-ed|Papert]] 1980 (Mindstorms):** Papert's philosophy of "learning through making" and the idea of "objects to think with" resonate strongly. SELF's prototype model makes creating and modifying "objects to think with" even more direct, as any object can be cloned, examined, and modified on the fly without navigating class hierarchies. The language itself becomes a more immediate medium for thought.
*   **[[backus-1978-can-programming-be-liberated-from-the-von-neumann-style|Backus]] 1978 (Can Programming Be Liberated...?):** Both papers represent radical critiques of mainstream programming paradigms from within computer science. [[backus-1978-can-programming-be-liberated-from-the-von-neumann-style|Backus]] attacked the assignment state model; Ungar and [[smith-da-2003-croquet-a-collaboration-system-architecture|Smith]] attack the class-based object model. Both propose radical simplifications ([[backus-1978-can-programming-be-liberated-from-the-von-neumann-style|Backus]] to functional FP; Ungar/[[smith-da-2003-croquet-a-collaboration-system-architecture|Smith]] to prototypic SELF) to achieve greater expressiveness and freedom from "word-at-a-time" or "class-at-a-time" thinking.
*   **[[hofstadter-2001-analogy-as-core-of-cognition|Hofstadter]] 2001 (Analogy as the Core of Cognition):** The SELF model, where objects inherit and modify behavior from prototypes, is fundamentally **analogy-based**. Creating a new object by cloning and tweaking a parent is an act of analogy ("be like this, but different"). The language's mechanics mirror the cognitive process [[hofstadter-2001-analogy-as-core-of-cognition|Hofstadter]] describes.
*   **[[lockhart-2002-a-mathematicians-lament|Lockhart]] 2002 (A Mathematician's Lament):** [[lockhart-2002-a-mathematicians-lament|Lockhart]] laments how procedural ritual (like algebraic manipulation) obscures the act of creative thinking in mathematics. Similarly, Ungar and [[smith-da-2003-croquet-a-collaboration-system-architecture|Smith]] lament how class-based OOP ritual (designing hierarchies, defining types) obscures the act of expressing a dynamic system of objects. Both papers advocate for tools that keep the creator closer to the "act of creation."

## Modern Relevance
SELF's principles are arguably more relevant today than in 1991.
1.  **Dynamic Languages and JavaScript:** The dominance of JavaScript, Python, and Ruby in web, data science, and automation means billions of lines of code run on objects that are, in principle, prototype-based or have highly dynamic object models. Understanding SELF is key to understanding their design philosophy and quirks.
2.  **AI and Dynamic Knowledge Representation:** Modern large language models and AI systems that deal with fluid, context-dependent knowledge representations benefit from object models that are not rigidly pre-defined. SELF's model of objects that can gain, lose, and dynamically modify their own slots is a natural fit for representing evolving, interconnected concepts in knowledge graphs or agent-based systems.
3.  **Rapid Prototyping and Interactive Development:** In the era of agile development and interactive notebooks (Jupyter), the idea of modifying a running system's components directly, without recompilation or strict type-checking, is vital. SELF's design is intrinsically geared towards this mode of exploration.
4.  **Educational Technology:** For tools aimed at teaching programming or computational thinking (e.g., Scratch, which uses sprites/objects, though class-based), the prototype model's simplicity offers a less intimidating entry point. The direct "clone and modify" metaphor aligns well with constructionist learning.

## Key Quotes
1.  **"SELF has adopted a prototype metaphor for object creation... SELF objects access their state information by sending messages to 'self', the receiver of the current message."** (Introduction) *Defines the fundamental mechanism that replaces variables and unifies state access with method dispatch.*
2.  **"In a class-based language, an object would be created by instantiating a plan in its class. In a prototype-based language like SELF, an object would be created by cloning (copying) a prototype."** (Section 2.1) *The crisp, core distinction that defines the new creation metaphor, emphasizing concreteness over abstraction.*
3.  **"Slots unite variables and procedures into a single construct. This permits the inheritance hierarchy to take over the function of lexical scoping in conventional languages."** (Abstract) *States the most radical technical consequence of the design: inheritance becomes a universal lookup mechanism.*
4.  **"SELF objects and procedures are woven from the same yarn by representing procedures as prototypes of activation records."** (Section 1) *Highlights the deep unification achieved, dissolving a long-standing distinction in programming languages.*
5.  **"In a prototype-based system an object can include its own behavior; no other object is needed to breathe life into it. Prototypes eliminate meta-regress."** (Section 2.1) *Points out a philosophical advantage: objects are self-contained, avoiding the infinite regression of "class of a class of a class."*
6.  **"The simplicity and flexibility of SELF poses a challenge to the programming environment; it will have to include navigational and descriptive aids."** (Section 2.1) *A prescient acknowledgment that radical language simplicity transfers complexity to the tooling, anticipating modern IDE needs.*
7.  **"Self-sufficient objects do not need external description. An object need not be a member of any kind, and every object is a first-class entity."** (Section 4) *The ultimate statement of the object model's power and simplicity: every entity is autonomous and complete.*