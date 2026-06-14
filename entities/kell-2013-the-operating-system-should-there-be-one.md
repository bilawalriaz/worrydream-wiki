---
title: Kell 2013 - The operating system, should there be one
created: 2026-06-10
updated: 2026-06-10
type: entity
tags: [computing-history, hci, programming-languages, cognitive-science]
sources: [raw/papers/Kell_2013_-_The_operating_system,_should_there_be_one.txt]
confidence: high
---

# Kell 2013 - The operating system, should there be one

## Core Thesis
Stephen Kell re-evaluates Dan Ingalls' 1981 provocation that "an operating system is a collection of things that don't fit inside a language; there shouldn't be one." Kell's central argument is that Ingalls' vision of absorbing OS functionality into a language-level object system (like Smalltalk) has not materialized, but that it *should not* have materialized in its pure form. Instead, the postmodern reality of diverse, fragmented computing ecosystems necessitates a different path. Kell argues that the Unix/Plan 9 philosophy, when extrapolated, naturally converges on an object abstraction similar to Smalltalk's. The key, therefore, is not to abolish the OS, but to recognize the "lurking Smalltalk" within Unix's evolutionary trajectory and to systematically unify OS- and language-level mechanisms. This would achieve the practical benefits [[ingalls-1978-the-smalltalk-76-programming-system|Ingalls]] sought—programmatic availability, descriptive availability, and interposable bindings—without requiring a totalizing "grand narrative" like Smalltalk. An operating system is still necessary, but its role should evolve to be a more expressive meta-system for composition.

## Historical Context
The paper dialogues with two seminal threads in computing history. First is the **Smalltalk vision**, where the entire computing environment—OS, language, and user interface—is a single, cohesive, object-oriented world. This "modernist" dream aimed for ultimate compositionality by eliminating boundaries between system and application code. Second is the **Unix philosophy**, which prioritized simplicity, text-stream composition, and pragmatic "do one thing well" tools. Unix succeeded brilliantly in a fragmented world by being agnostic to what happened inside processes, but this agnosticism led to systemic fragmentation: each language and runtime invented its own object-binding, persistence, and introspection mechanisms. The problem being addressed is the **cost of this fragmentation**—it impedes cross-paradigm composition and makes system-level tasks unnecessarily archeologically complex. Kell's work sits in the context of early 2010s efforts to rethink system design, with Plan 9 as a critical intermediary step that pushed Unix's file-everything principle further (e.g., via /proc and network-transparent file servers).

## Key Contributions
1.  **The "Lurking Smalltalk" Thesis:** Kell demonstrates that the trajectory of the Unix "file" abstraction, especially through Plan 9's 9P protocol and pervasive /proc filesystem, culminates in an entity that is functionally equivalent to a Smalltalk object—a named, stateful, interactive entity accessible via a uniform protocol. The OS calls that manipulate these (open, read, write, stat) are then the primitives of a meta-system.
2.  **Mapping of Composition Fixes to Language Concepts:** He systematically catalogs common Unix "point fixes" for compositional problems (e.g., pipes, redirection, LD_PRELOAD, /etc/alternatives, FUSE) and shows they are ad-hoc, fragmented implementations of features native to Smalltalk-like environments: message passing, interposition, object binding, and reflective meta-protocols.
3.  **The Evolutionary Postmodern Path:** He argues against a revolutionary replacement of the OS with a language runtime. Instead, he proposes evolutionary approaches to *increase the expressiveness of the existing Unix meta-system*. This involves treating system state more uniformly as a graph of objects and enriching the protocols (like 9P) and binding mechanisms to support more sophisticated interposition and introspection.
4.  **Diagnosis of the Application-Device Split:** He identifies a fundamental, enduring split in Unix between "application mechanisms" (opaque to the OS) and "file/device mechanisms" (the OS's domain). Smalltalk eliminates this split; Kell's work seeks to bridge it pragmatically.

## Methodology
The methodology is **historical analysis and conceptual synthesis**. Kell performs a close reading and comparison of seminal design documents and systems (Smalltalk, 5th Edition Unix, Plan 9). He employs a "tick-list" analysis, evaluating each system against a set of design ideals (programmatic availability, descriptive availability, interposable bindings). The argument is **polemical and design-oriented**, not empirical. He constructs a theoretical lineage from Unix to Smalltalk via Plan 9, then uses this framework to critique modern systems and propose design principles. The paper is an exercise in **conceptual archaeology**—uncovering latent potentials and hidden convergences in historical systems to guide future evolution.

## Influence
Kell's paper provides a crucial theoretical lens for understanding and advancing **systems programming and developer tools**. Its key influence lies in framing fragmented Unix mechanisms not as failures but as partial realizations of a deeper object-oriented ideal. This has resonated in work on:
*   **Language Servers and LSP:** The Language Server Protocol is a modern, network-transparent protocol for system-like services (code analysis, completion), effectively treating the language toolchain as a set of interactive objects, echoing the 9P/file-object analogy.
*   **Containerization and Virtual Filesystems:** Technologies like FUSE, overlay filesystems, and the container model (Docker, Podman) are, in Kell's framing, further experiments in making system abstractions more composable and interposable at the OS level.
*   **Unikernels and Library OSes:** These can be seen as radical attempts to re-draw the application-device split, often by making the OS a library linked into a language runtime, touching on Kell's evolutionary path.
*   The paper is cited in academic discussions on **operating system structure, meta-level architectures, and the convergence of language runtimes and OS kernels**. It provides a vocabulary for talking about Unix's implicit object model.

## Connections to Other Papers in the Collection
*   **Kay 1972 (Personal Computer):** Kell is directly in dialogue with Alan Kay's Smalltalk vision. While Kay focused on the personal, interactive, graphical application of this unity, Kell focuses on the systemic, evolutionary path to achieve it within existing infrastructure.
*   **[[bush-1931-the-differential-analyzer|Bush]] 1945 (As We May Think):** Bush's Memex was a personal, associative knowledge system that transcended file-system metaphors. Kell's work can be seen as a technical pathway toward making the OS itself a more Memex-like, associative, and interposable environment, moving beyond the linear "file" to richer object graphs.
*   **[[engelbart-1960-games-that-teach-the-fundamentals-of-computer-operation|Engelbart]] 1962 (Augmenting Human Intellect):** Engelbart's vision required a highly integrated, synergistic system (the Augment NLS). Kell's analysis shows why achieving such synergy is so hard in a fragmented Unix world and proposes incremental steps toward it by enriching the meta-system.
*   **[[backus-1978-can-programming-be-liberated-from-the-von-neumann-style|Backus]] 1978 (FP):** [[backus-1978-can-programming-be-liberated-from-the-von-neumann-style|Backus]] criticized the "word-at-a-time" imperative style of von Neumann languages. Smalltalk's message-passing offers an alternative. Kell notes that Unix pipes are a limited form of functional composition, but argues that a richer, object-oriented meta-system is needed to achieve the full compositional power hinted at by both FP and Smalltalk.

## Modern Relevance
This analysis is strikingly relevant to contemporary computing:
*   **AI and LLM Tooling:** Modern AI coding assistants are becoming "meta-systems" that interact with a user's codebase. Understanding the OS/language boundary is crucial for designing tools that can *compose* with development environments (like via LSP) and *interpose* in the editing/debugging process, which is exactly Kell's concern with interposable bindings and descriptive availability.
*   **Knowledge Management and Hypermedia:** For tools aiming to be hypermedia systems (like those in the WorryDream collection), Kell's point is that the underlying platform must support rich, composable, and interposable objects. A system that treats everything as a flat file is fundamentally limiting. His work advocates for OSes and languages that better support the associative, interactive knowledge structures envisioned by [[bush-1931-the-differential-analyzer|Bush]] and [[engelbart-1960-games-that-teach-the-fundamentals-of-computer-operation|Engelbart]].
*   **Developer Experience (DX):** The explosion of CLI tools, language servers, editor plugins, and containers represents a constant, ad-hoc effort to solve the composition and interposition problems Kell identifies. His paper provides a framework to understand this as a search for a more unified meta-system, moving the field toward a postmodern "lingua franca" for developer tools.
*   **WebAssembly and Edge Computing:** WASI (WebAssembly System Interface) is, in effect, a new standardized "file-like" interface for sandboxed code. Kell's analysis predicts that such interfaces will evolve to become richer object-capability systems to enable greater composability.

## Key Quotes
1.  **"An operating system is a collection of things that don’t fit into a language. There shouldn’t be one." ([[ingalls-1978-the-smalltalk-76-programming-system|Ingalls]], quoted)**
    *   This is the originating provocation. Kell spends the paper unpacking why this vision is both compelling and, in its pure form, impractical for a pluralistic computing world.

2.  **"Unix... succeeds in existing in the postmodern reality of diverse, independently developed, mutually incoherent language- and application-level abstractions, by virtue of its obliviousness to them."**
    *   This is a key nuance. Unix's strength—its agnosticism—is also its weakness for composition. It trades systemic unity for ecological survival.

3.  **"The natural trajectory of the Unix design, extrapolated through Plan 9 and beyond, yields an object abstraction mostly equivalent to that of Smalltalk."**
    *   This is the core thesis. It re-frames Unix's evolution not as a failed attempt at Smalltalk, but as an accidental, convergent evolution toward a similar endpoint via a different path.

4.  **"We call this the application–device split. [It] runs deep: between application mechanisms (which, aside from trapping into system calls, are opaque to the operating system) and file mechanisms (which are the operating system’s reason for being)."**
    *   This diagnosis explains why Unix fragmentation occurs. Bridging this split is the central technical challenge Kell identifies.

5.  **"If diverse binding mechanisms were not enough fragmentation, the addition of independently developed protocols and data representations 'in the small' adds even further impediment to composition."**
    *   Highlights that the problem isn't just between OS and app, but also *between* applications and languages, creating a multi-layered fragmentation that thwarts composition.