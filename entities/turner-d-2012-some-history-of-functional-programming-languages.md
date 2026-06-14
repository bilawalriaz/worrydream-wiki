---
title: Turner D 2012 - Some History of Functional Programming Languages
created: 2026-06-10
updated: 2026-06-10
type: entity
tags: [computing-history, hci, programming-languages, mathematics]
sources: [raw/papers/Turner_D_2012_-_Some_History_of_Functional_Programming_Languages.txt]
confidence: high
---

# [[turner-f-2017-dont-be-evil|Turner]] D 2012 - Some History of Functional Programming Languages

## Core Thesis
D.A. [[turner-f-2017-dont-be-evil|Turner]] argues that the lineage leading to modern, purely functional languages like Haskell is not a series of isolated inventions but a coherent, goal-oriented evolution defined by a specific set of desirable properties: **laziness (lazy evaluation), higher-order functions, polymorphic types, and purity (the absence of side effects)**. The paper is a teleological history, tracing milestones not just chronologically but by their contribution to this specific synthesis. The nuance is that this path was often non-obvious and required solving fundamental problems in evaluation strategy and implementation. [[turner-f-2017-dont-be-evil|Turner]]'s core claim is that the convergence on these properties in Haskell was not accidental but represented the logical resolution of decades of theoretical and practical challenges in functional programming.

## Historical Context
[[turner-f-2017-dont-be-evil|Turner]] situates functional programming's origins in a quest for a more mathematical, declarative foundation for computation, as an alternative to the imperative, state-centric model of FORTRAN and its descendants. Before the developments he outlines, the dominant programming paradigm involved explicit sequences of commands modifying global state. The lambda calculus provided a pure, formal model of computation based on function application and abstraction, but it remained a theoretical tool. LISP introduced practical symbolic computation and the idea of a program as data, but its practical implementations (LISP 1.5) were impure, featuring assignment and dynamic scoping. The 1960s and 70s saw a tension between the theoretical purity of the lambda calculus and the practical, but messy, reality of languages designed for real machines. The field was grappling with how to retain the mathematical clarity of functions while creating usable, efficient languages. The "problem" was twofold: a) achieving referential transparency (purity) in a practical language, and b) finding an evaluation order (lazy vs. eager) that was both semantically clean and computationally tractable.

## Key Contributions
1.  **Curating a Specific Genealogy:** The primary contribution is the selection and framing of nine milestones (Lambda Calculus, LISP, Algol 60, ISWIM, PAL, SASL, Edinburgh ML/HOPE, Miranda, Haskell) to construct a narrative of progress toward a defined ideal.
2.  **Demythologizing LISP:** [[turner-f-2017-dont-be-evil|Turner]] forcefully argues against common misconceptions, stating that "Pure LISP" never existed, that LISP was not based on the lambda calculus, and that its M-language was first-order. This reframes LISP not as a pure precursor but as a pragmatic, impure system whose theoretical underpinnings were Kleene's recursive functions.
3.  **Highlighting the Critical Role of Evaluation Strategy:** The paper emphasizes that the choice between normal order (lazy) and applicative order (eager) reduction was a central, consequential decision. He credits Wadsworth with making lazy evaluation practical via graph reduction and traces its implementation lineage directly to modern Haskell compilers (G-machine, Spineless Tagless G-machine).
4.  **Positioning ISWIM as the Conceptual Blueprint:** [[landin-1966-the-next-700-programming-languages|Landin]]'s 1966 ISWIM is presented as the visionary, theoretical design that pointed the way for later practical languages (Miranda, Haskell), featuring lazy evaluation, higher-order functions, and a block structure based on `where` clauses.
5.  **Tracing Implementation Mechanics:** The paper provides a clear, technical thread connecting the theory of graph reduction to the concrete engineering of compilers, showing how abstract concepts like the Y-combinator are made efficient on real hardware.

## Methodology
The methodology is **historical synthesis and argumentation**. [[turner-f-2017-dont-be-evil|Turner]] uses the approach of a "series of snapshots" to build a case. It is not empirical research but a curated analysis of primary sources (key papers and language definitions). The argument is structured as a progressive story, where each milestone either introduces a key concept (lambda calculus, LISP's data structures), makes a crucial design choice (Algol 60's block structure), or solves a previous shortcoming (graph reduction for efficiency). The tone is authoritative and corrective, especially in debunking myths about LISP. It is the work of a participant-historian ([[turner-f-2017-dont-be-evil|Turner]] himself developed SASL and Miranda) synthesizing the field's development to justify the design choices embodied in Haskell.

## Influence
This paper itself is a retrospective synthesis, but the history it describes had immense influence. The lineage it traces directly enabled:
*   **The Haskell Language:** The 1990s and onward saw Haskell become the de facto standard for lazy, pure functional programming, serving as a research platform and influencing ideas in mainstream languages (e.g., list comprehensions in Python, lambda expressions in Java/C#).
*   **The Spread of Functional Concepts:** The ideas of immutability, higher-order functions, and algebraic data types (via ML) have permeated mainstream programming (Scala, Kotlin, Swift, Rust).
*   **Compiler Technology:** Techniques like lambda lifting, graph reduction, and spineless tagless G-machines are foundational in modern compiler design, not just for functional languages.
*   **Academic Pedagogy:** This historical narrative is a standard part of programming language curricula, shaping how generations of computer scientists understand language design.

## Connections to Other Papers in the Collection
While the specific WorryDream collection isn't fully enumerated, the themes in [[turner-f-2017-dont-be-evil|Turner]]'s paper connect to several likely works:
*   **[[bush-1945-as-we-may-think-with-engelbart-notes|Bush]] 1945 (As We May Think):** Both deal with tools that augment human thought. [[bush-1945-as-we-may-think-with-engelbart-notes|Bush]]'s Memex is a hypertext system; functional programming provides a mathematical tool for clear, composable thought about computation. The connection is the pursuit of powerful symbolic tools for the mind.
*   **[[backus-1978-can-programming-be-liberated-from-the-von-neumann-style|Backus]] 1978 (FP):** This is the most direct connection. [[turner-f-2017-dont-be-evil|Turner]]'s paper explains the historical context that led to, and was superseded by, the functional programming paradigm [[backus-1978-can-programming-be-liberated|Backus]] advocated for in his [[turing-1936-on-computable-numbers-with-an-application-to-the-entscheidungsproblem|Turing]] Award lecture. Haskell is the practical realization of the ideals [[backus-1978-can-programming-be-liberated|Backus]] championed.
*   **[[kay-1972-a-personal-computer-for-children-of-all-ages|Kay]] 1972 (Personal Computer):** [[kay-1972-a-personal-computer-for-children-of-all-ages|Kay]]'s vision was of a personal, dynamic medium. Functional programming, with its focus on expression and composition rather than imperative control, aligns with the idea of programming as a direct, creative act of modeling ideas.
*   **[[thurston-1994-on-proof-and-progress-in-mathematics|Thurston]] 1994 (Proof and Progress):** [[thurston-1994-on-proof-and-progress-in-mathematics|Thurston]] discusses the social and cognitive aspects of mathematical progress. [[turner-f-2017-dont-be-evil|Turner]]'s narrative can be seen as a parallel in computer science: a community converging on an aesthetic (the elegance of pure, lazy functional programming) and a set of agreed-upon problems to solve.
*   **[[hofstadter-2001-analogy-as-core-of-cognition|Hofstadter]] 2001 (Analogy):** The history of functional programming is a story of analogy and abstraction: from the formal lambda calculus, to the practical but impure LISP, to the designed ideal of ISWIM, to the implemented reality of Haskell. Each step involves abstracting the essence of "function" to new contexts.

## Modern Relevance
[[turner-f-2017-dont-be-evil|Turner]]'s history is profoundly relevant to contemporary computing:
1.  **AI and Machine Learning:** Modern AI frameworks (PyTorch, TensorFlow) are built on concepts of automatic differentiation and computation graphs, which are fundamentally about tracking functional transformations of data, not imperative state changes. The emphasis on immutability and defined dataflow in functional programming is mirrored in these systems.
2.  **Concurrent and Parallel Programming:** The core functional property of referential transparency (purity) eliminates entire classes of bugs related to shared mutable state, making concurrent programming safer. This is why ideas from Haskell are influential in languages designed for concurrency, like Erlang/Elixir and the actor model.
3.  **Knowledge Management and "Literate" Programming:** The functional paradigm encourages building systems by composing well-defined, mathematically analyzable parts. This aligns with the goal of creating software and knowledge systems that are more understandable, maintainable, and trustworthy—key concerns in managing complex information.
4.  **The State of Mainstream Languages:** The "functional features" now common in JavaScript, Python, Java, and C# (map/filter/reduce, lambdas, optional chaining) are direct descendants of the ideas [[turner-f-2017-dont-be-evil|Turner]] chronicles. His history explains the source and original purpose of these tools.

## Key Quotes
1.  **"Something called 'Pure LISP' never existed — [[mccarthy-1979-history-of-lisp|McCarthy]] (1978) records that LISP had assignment and goto before it had conditional expressions and recursion..."**
    *   *Analysis: A potent corrective to a pervasive myth. It underscores [[turner-f-2017-dont-be-evil|Turner]]'s thesis that practicality often preceded purity, and that the path to functional programming was not a straight line from theory to implementation.*

2.  **"Call-by-value is an unsafe reduction strategy for lambda calculus... but efficient because the actual parameter is reduced only once."**
    *   *Analysis: This distills the central trade-off that shaped decades of language design. The "safety" here refers to conformity with the mathematical semantics of the lambda calculus (finding normal forms), not memory safety. It frames the lazy/eager choice as a fundamental conflict between semantics and efficiency.*

3.  **"The thesis of Wadsworth (1971, Ch 4) showed that the efficiency disadvantage of normal order reduction can be overcome by normal graph reduction."**
    *   *Analysis: This highlights the pivotal, enabling insight that rescued lazy evaluation from being a theoretical curiosity. It shows how a theoretical property (efficiency of computation) was solved by a representational shift (graphs vs. trees), a key theme in computer science.*

4.  **"The pure untyped lambda calculus is already computationally complete... It is the power to define functions of higher type, together with clean technical properties... that make lambda calculus... a natural choice as a basis for functional programming."**
    *   *Analysis: This is the foundational justification for the entire enterprise. It asserts that the power and elegance of the mathematical model itself is the reason for using it as a programming foundation, rather than merely being inspired by it.*

5.  **"At the time he invented LISP, [[mccarthy-1979-history-of-lisp|McCarthy]] was aware of (Church 1941) but had not studied it. The theoretical model behind LISP was Kleene’s theory of first order recursive functions."**
    *   *Analysis: Another corrective that separates LISP's practical origins from the lambda calculus' theoretical purity. It emphasizes that historical influence is often indirect and based on available knowledge, not an inevitable convergence.*