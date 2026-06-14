---
title: Backus 1978 - Can Programming Be Liberated from the von Neumann Style?
created: 2026-06-10
updated: 2026-06-10
type: entity
tags: [programming-languages, seminal, critique]
sources: [raw/papers/Backus_1978_-_Can_Programming_Be_Liberated_from_the_von_Neumann_Style.txt]
confidence: high
---

# [[backus-1978-can-programming-be-liberated-from-the-von-neumann-style|Backus]] 1978 - Can Programming Be Liberated from the von Neumann Style?

## Core Thesis

John [[backus-1978-can-programming-be-liberated-from-the-von-neumann-style|Backus]]'s 1977 [[turing-1936-on-computable-numbers-with-an-application-to-the-entscheidungsproblem|Turing]] Award lecture (published 1978) advances a radical argument: conventional [[barton-1965-the-interrelation-between-programming-languages-and-machine-organization|programming languages]] are fundamentally and irreparably flawed because they inherit their intellectual structure from the von Neumann computer. These languages are "fat and weak" -- growing ever more enormous without becoming more powerful -- because their basic framework bakes in a word-at-a-time style of computation that prevents programmers from thinking in terms of larger conceptual units. [[backus-1978-can-programming-be-liberated-from-the-von-neumann-style|Backus]] proposes [[hughes-1990-why-functional-programming-matters|functional programming]] as a complete alternative: a system where programs are functions built from combining forms, where an algebra of programs enables mechanical reasoning and transformation, and where the framework is minimal while the changeable parts are maximally expressive.

The paper is structured in four main parts: (1[[hughes-1990-why-functional-programming-matters|) a critique of von Ne]]umann languages, (2) the FP (Functional Programming) system, (3) an algebra of programs for reasoning about FP functions, and (4) extensions to history-sensitive computing via FFP (Formal FP) and AST (Applicative State Transition) systems.

## Historical Context (FORTRAN, ALGOL, von Neumann bottleneck)

The paper is historically remarkable because [[backus-1978-can-programming-be-liberated-from-the-von-neumann-style|Backus]] was the creator of FORTRAN -- the first widely successful high-level [[borning-1981-the-programming-language-aspects-of-thinglab|programming language]] and arguably the most influential von Neumann language ever designed. When [[backus-1978-can-programming-be-liberated-from-the-von-neumann-style|Backus]] says "some might say that I bear some responsibility for that problem," it is a moment of extraordinary intellectual honesty from someone critiquing the paradigm he [[borning-1981-the-programming-language-aspects-of-thinglab|helped establish.

T]]he paper arrives at a moment of crisis in programming language design. By 1977, languages had been "steadily progressing toward their present condition of obesity" for twenty years. The Department of Defense was planning a committee-designed language (which would become Ada) that could require a 1,000-page manual. Each successive language incorporated all features of its predecessors plus more. Structured programming, while valuable, was merely "a modest effort to introduce some order" into the chaotic statement world without attacking the fundamental word-at-a-time style.

[[backus-1978-can-programming-be-liberated-from-the-von-neumann-style|Backus]] had[[borning-1981-the-programming-language-aspects-of-thinglab| served on the commi]]ttees that developed ALGOL 58 and ALGOL 60, and he had invented BNF ([[backus-1978-can-programming-be-liberated-from-the-von-neumann-style|Backus]] Normal Form) for specifying programming language syntax. His critique thus comes from someone who deeply understood both the pragmatic and theoretical dimensions of language design. The von Neumann computer architecture -- a CPU, a store, and a single-word connecting tube -- had been conceived thirty years earlier and had become so identified with "computer" that no one questioned it.

## Key Contributions

### The "von Neumann Bottleneck"

The paper's most enduring contribution to vocabulary is the concept of the "von Neumann bottleneck" -- the tube connecting CPU and store that transmits one word at a time. [[backus-1978-can-programming-be-liberated-from-the-von-neumann-style|Backus]] argues this is not just a physical bottleneck but an *intellectual* one. Much of the traffic through the bottleneck is "not useful data but merely names of data, as well as operations and data used only to compute such names." Programming becomes "planning and detailing the enormous traffic of words through the von Neumann bottleneck."

### The Assignment Statement as Linguistic Bottleneck

[[backus-1978-can-programming-be-liberated-from-the-von-neumann-style|Backus]] identifies the assignment statement (":=") as the linguistic equivalent of the hardware bottleneck. It forces word-at-a-time thinking and splits programming into two incompatible worlds: the orderly world of expressions (right sides) and the disorderly world of statements (everything else). Combining forms are powerful in the expression world, but expressions can only produce a single word, and it is in the statement world that these single [[costikyan-2002-i-have-no-words-and-i-must-design|words must]] be assembled into results. This split prevents com[[hughes-1990-why-functional-programming-matters|bining forms in either]] world from achieving their full potential.

### The FP System

[[backus-1978-can-programming-be-liberated-from-the-von-neumann-style|Backus]] proposes Functional Programming (FP) systems where:
- **Objects** are atoms, sequences, or bottom (⊥/undefined)
- **Functions** map objects to objects, are bottom-preserving, and take a single argument
- **Functional forms** (combining forms) like composition (f∘g), construction ([f,g]), apply-to-all (αf), and insert (/f) combine existing functions into new ones
- **Definitions** assign names to functions

FP systems use *no variables* and *no substitution rules*. This is a deliberate restriction relative to the lambda calculus -- [[backus-1978-can-programming-be-liberated-from-the-von-neumann-style|Backus]] argues that unrestricted freedom "comes with chaos." Just as structured programming eschews some control statements for simpler structure, FP eschews lambda expressions and variable substitution for programs with known, useful algebraic properties.

The canonical example is inner product: `Def IP = (/+)∘(α×)∘Trans` -- three combining forms applied to three simple functions, with no variables, no loops, no procedure declarations, and complete generality.

### The Algebra of Programs

Perhaps the most innovative contribution is the idea of an *algebra of programs* -- an algebra whose variables range over programs and whose operations are combining forms. Laws like `[f,g]∘h = [f∘h, g∘h]` (construction distributes over composition) allow mechanical transformation of programs, just as algebraic laws allow solving high-school equations. [[backus-1978-can-programming-be-liberated-from-the-von-neumann-style|Backus]] provides ~24 algebraic laws and proves the equivalence of different program formulations using them.

The algebra includes expansion theorems that can express recursively defined functions as infinite conditional expansions, providing both termination proofs and case-by-case behavioral descriptions. The recursion theorem and iteration theorem give ready-made expansions for useful classes of equations. [[backus-1978-can-programming-be-liberated-from-the-von-neumann-style|Backus]] demonstrates correctness proofs for recursive and iterative factorial, equivalence of two iterative programs, and an idempotency proof -- all using simple algebraic manipulations.

### FFP and AST Systems

To address FP's limitation of not being history-sensitive, [[backus-1978-can-programming-be-liberated-from-the-von-neumann-style|Backus]] introduces:
- **FFP (Formal FP) systems**: Objects represent functions via a "metacomposition rule" that allows defining new functional forms and creating recursive functions without definitions. The key innovation is `apply:<x,y> = (x:y)`, meaningless in FP but fundamental in FFP.
-[[borning-1981-the-programming-language-aspects-of-thinglab| **AST (Applicative ]]State Transition) systems**: History-sensitive systems where a single state transition occurs per major computation, the state is a simple sequence of cells, and the programming language is applicative (FFP-based). This eliminates the "cable and protocols" complexity of von Neumann state management.

## Methodology

[[backus-1978-can-programming-be-liberated-from-the-von-neumann-style|Backus]]'s methodology is primarily analytical and constructive. The paper proceeds through:

1. **Classification**: A taxonomy of computing system models (simple operational, applicative, von Neumann) evaluated on foundations, history sensitivity, semantics, and program clarity.
2. **Comparative analysis**: Detailed side-by-side comparison of von Neumann and functional programs (inner product), enumerating specific properties (hierarchical structure, generality, argument-naming, housekeeping).
3. **Construction**: Building a complete alternative (FP, FFP, AST) from first principles, with formal syntax, informal and formal semantics, and worked examples.
4. **Algebraic proof**: Demonstrating that programs can be reasoned about using algebraic techniques accessible to "amateurs" rather than requiring heavy math[[borning-1981-the-programming-language-aspects-of-thinglab|ematical machinery.
]]5. **[[lampson-1983-hints-for-computer-system-design|System design]]**: Sketching a complete self-protecting system program for an AST system, including file maintenance, user programs, and self-modification.

## Influence

### Direct Technical Impact

The paper's influence on programming language research is immense:

- **Haskell** (1990): The most direct descendant. Haskell's purely functional style, type classes[[hughes-1990-why-functional-programming-matters|, and later monadic IO]] all trace lineage to [[backus-1978-can-programming-be-liberated-from-the-von-neumann-style|Backus]]'s vision of variable-free, combining-form-based programming with strong algebraic properties.
- **The functional programming movement**: ML, Miranda, Erlang, and the entire family of functional languages were energized by [[backus-1978-can-programming-be-liberated-from-the-von-neumann-style|Backus]]'s argument that functional style was not merely an academic curiosity but a fundamentally superior paradigm.
- **Combinators and point-free style**: [[backus-1978-can-programming-be-liberated-from-the-von-neumann-style|Backus]]'s FP system anticipated and influenced the "point-free" programming style (programming without naming arguments), which became a hallmark of Haskell idioms and the Unix pipe philosophy.

### Conceptual Impact

- **"Von Neumann bottleneck"** entered the permanent vocabulary of [[hamming-1968-one-mans-view-of-computer-science|computer science]] and is now used far beyond its original context.
- **Algebra of programs** influenced program transformation, partial evaluation, and the idea that programs should have mathematical properties amenable to mechanical reasoning.
- **Framework vs. changeable parts** anticipated modern debates about language [[clark-d-1988-the-design-philosophy-of-the-darpa-internet-protocols|design philosophy]] (small core + extensible library vs. kitchen-sink languages).

### Criticisms and Limitations

The FP system as presented has known limitations: it cannot[[turing-1936-on-computable-numbers-with-an-application-to-the-entscheidungsproblem| expre]]ss all computable functions (unless the primitive set is sufficient), it is not [[turing-1936-on-computable-numbers-with-an-application-to-the-entscheidungsproblem|Turing]]-complete in its basic form, and its lack of history sensitivity makes it impractical for real-world programming. The FFP and AST extensions address these but are sketched rather than fully developed. Critics also note that the lambda calculus, which [[backus-1978-can-programming-be-liberated-from-the-von-neumann-style|Backus]] restricts away from, is more general and that Haskell eventually reintroduced lambda expressions alongside the combining-form style.

## Connections to Other WorryDream Papers

### [[mccarthy-1979-history-of-lisp|McCarthy]] and Lisp
[[backus-1978-can-programming-be-liberated-from-the-von-neumann-style|Backus]] explicitly contrasts FP with pure Lisp, noting that Lisp's lambda-calculus basis gives it "unrestricted freedom" that "comes with chaos." He references [[mccarthy-1979-history-of-lisp|McCarthy]]'s conditional expressions as a building block but argues that Lisp became "buried in large extensions with many von Neumann features." The paper is in many ways a response to Lisp's approach -- agreeing on the value of functional style while rejecting lambda expressions as the foundation.

### [[landin-1966-the-next-700-programming-languages|Landin]] (The Mechanical Evaluation of Expressions)
[[backus-1978-can-programming-be-liberated-from-the-von-neumann-style|Backus]] references [[landin-1966-the-next-700-programming-languages|Landin]]'s SECD machine and its influence on understanding evaluation of applic[[barton-1965-the-interrelation-between-programming-languages-and-machine-organization|ative expressions. La]]ndin's work on ISWIM and the connection between lambda calculus and programming languages is part[[landin-1966-the-next-700-programming-languages| of th]]e intellectual backdrop. [[backus-1978-can-programming-be-liberated-from-the-von-neumann-style|Backus]] acknowledges [[landin-1966-the-next-700-programming-languages|Landin]]'[[hughes-1990-why-functional-programming-matters|s introduction of list]] structures into lambda-calculus-based systems but argues that the result is an FP-like system "in which the usual lambda expressi[[hughes-1990-why-functional-programming-matters|ons or combinators do ]]not appear."

### [[hughes-1990-why-functional-programming-matters|Hughes]] (Why Functional Programming Matters)
David [[hughes-1990-why-functional-programming-matters|Hughes]]'s 1990 paper can be read as a vindication of [[backus-1978-can-programming-be-liberated-from-the-von-neumann-style|Backus]]'s vision, demonstrating with concrete examples (lazy evaluation, modularity, structured programming) that fun[[hughes-1990-why-functional-programming-matters|ctiona]]l programming delivers on [[backus-1978-can-programming-be-liberated-from-the-von-neumann-style|Backus]]'s promises. [[hughes-1990-why-functional-programming-matters|Hughes]]'s examples of "gluing" functions together directly echo [[backus-1978-can-programming-be-liberated-from-the-von-neumann-style|Backus]]'s combining forms and hierarchical construction.

### The WorryDream Context
Bret Victor's WorryDream project explores how programming can be reimagined. [[backus-1978-can-programming-be-liberated-from-the-von-neumann-style|Backus]]'s paper is foundational to this project because it asks the most fundamental question: is the[[hughes-1990-why-functional-programming-matters| *enti]]re paradigm* wrong? Not just the syntax, not just the tools, but the underlying model of compu[[hughes-1990-why-functional-programming-matters|tation that programmin]]g languages embody. This radical questioning of first principles is central to Victor's own work on rethinking programming.

## Modern Relevance

### Monads and Effect Systems
Haskell's monadic IO, developed in the 1990s, directly addresses the problem [[backus-1978-can-programming-be-liberated-from-the-von-neumann-style|Backus]] identified: how to make functional programming history-sensitive without losing algebraic properties. Monads provide "loosely coupled state transition semantics" -- exactly what [[backus-1978-can-programming-be-liberated-from-the-von-neumann-style|Backus]] called for -- by encapsulating side effects within a mathematical framework. The state monad, IO monad, and related constructs are practical realizations of the AST vision.

### Dataflow and Reactive Programming
[[backus-1978-can-programming-be-liberated-from-the-von-neumann-style|Backus]] noted data-flow languages (Arvind, Dennis, Kosinski) as partially fitting his vision. Modern reactive programming frameworks (RxJS, React, FRP) embody the idea that programs should describe transformations of data rather than step-by-step state mutations. The "loosely coupled" semantics [[backus-1978-can-programming-be-liberated-from-the-von-neumann-style|Backus]] proposed map naturally onto dataflow and event-stream architectures.

### MapReduce and Parallel Computing
Google's MapReduce framework is strikingly similar to [[backus-1978-can-programming-be-liberated-from-the-von-neumann-style|Backus]]'s combining forms: Map corresponds to αf (apply-to-all), Reduce corresponds to /f (insert). The framework works because, as [[backus-1978-can-programming-be-liberated-from-the-von-neumann-style|Backus]] argued, programs built from these forms have algebraic properties that enable parallelization, optimization, and reasoning. GPU computing (CUDA, OpenCL) similarly exploits the parallelism inherent in combining-form-based computation.

### The "Small Framework, Rich Changeable Parts" Principle
Modern language design has increasingly adopted [[backus-1978-can-programming-be-liberated-from-the-von-neumann-style|Backus]]'s principle. Lisp (with macros), Racket (with language-oriented programming), and Rust (with traits and macros) all aim for small frameworks that accommodate diverse changeable parts. The [[smith-r-1987-experiences-with-the-alternate-reality-kit-an-example-of-the-tension-between-literalism-and-magic|tension between]] "batteries included" languages and small, extensible cores remains central to PL design.

### Algebraic Reasoning and Program Transformation
Modern work on program synthesis, superoptimization, and equality saturation (e.g., the e-graph technique) realizes [[backus-1978-can-programming-be-liberated-from-the-von-neumann-style|Backus]]'s vision of mechanically transforming programs using algebraic laws. Tools like Herbie (for floating-point optimization) use algebraic rewriting to improve programs, exactly as [[backus-1978-can-programming-be-liberated-from-the-von-neumann-style|Backus]] envisioned.

### The Unfinished Revolution
Despite all this progress, [[backus-1978-can-programming-be-liberated-from-the-von-neumann-style|Backus]]'s fundamental critique remains partially unaddressed. Most programmers still write in von Neumann style, most languages still split expressions and statements, and the assignment statement still domin[[barton-1965-the-interrelation-between-programming-languages-and-machine-organization|ates. The paper's dee]]pest question -- whether we can be *liberated* from the von Neumann style rather than merely *improvin[[barton-1965-the-interrelation-between-programming-languages-and-machine-organization|g* it -- remains open]].

## Key Quotes

> "Conventional programming languages are growing ever more enormous, but not stronger. Inherent defects at the most basic level cause them to be both fat and weak."

> "The assignment statement is the von Neumann bottleneck of programming languages and keeps us thinking in word-at-a-time terms in much the same way the computer's bottleneck does."

> "I propose to call this tube the von Neumann bottleneck. The task of a program is to change the contents of the store in some major way; when one considers that this task must be accomplished entirely by pumping single words back and forth through the von Neumann bottleneck, the reason for its name becomes clear."

> "Surely there must be a less primitive way of making big changes in the store than by pushing vast numbers of words back and forth through the von Neumann bottleneck."

> "If one constantly invents new combining forms to suit the occasion, as one can in the lambda calculus, one will not become familiar with the style or useful properties of the few combining forms that are adequate for all purposes."

> "Denotational and axiomatic semantics are descriptive formalisms whose foundations embody elegant and powerful concepts; but using them to describe a von Neumann language cannot produce an elegant and powerful language any more than the use of elegant and modern machines to build an Edsel can produce an elegant and modern car."

> "Each successive language incorporates, with a little cleaning up, all the features of its predecessors plus a few more."

> "The differences between Fortran and Algol 68, although considerable, are less significant than the fact that both are based on the programming style of the von Neumann computer."

> "Programming is basically planning and detailing the enormous traffic of words through the von Neumann bottleneck, and much of that traffic concerns not significant data itself but where to find it."

> "I regret the need for the above negative and not very precise discussion of these languages. But the complacent acceptance most of us give to these enormous, weak languages has puzzled and disturbed me for a long time."
