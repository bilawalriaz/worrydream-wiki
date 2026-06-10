---
title: Luzin 1998 - The Evolution of Function, Part II
created: 2026-06-10
updated: 2026-06-10
type: entity
tags: [mathematics, history-of-science, philosophy-of-mathematics, definability]
sources: [raw/papers/Luzin_1998_-_The_Evolution_of_Function,_Part_II.txt]
confidence: high
---

# Luzin 1998 - The Evolution of Function, Part II

## Core Thesis
Nikolai Luzin's paper argues that the modern concept of a mathematical function is not a static discovery but a contested, evolving idea whose development was propelled by a fundamental schism following Fourier's discovery. The core thesis is that Fourier's work on trigonometric series forced a permanent and productive separation between the *concept* of a function (a rule of correspondence) and its *analytic representation* (a formula or expression). This separation birthed two divergent trajectories in mathematics: one (Weierstrass) seeking to preserve organic interdependence within functions of a complex variable, and the other (Dirichlet) embracing complete independence of values for functions of a real variable. Luzin contends that the clarity provided by the resulting definitions (especially Dirichlet's) was temporary and that subsequent mathematical developments, particularly the critiques of Borel, Baire, and the Moscow School, revealed profound, unresolved philosophical tensions about definability, communication, and the very meaning of a mathematical object.

## Historical Context
The paper situates itself within the aftermath of the 18th and early 19th-century "vibrating string controversy." Before Fourier, the concept of a function was intrinsically tied to a single analytic expression. The debate over the sound of a vibrating string (d'Alembert, Euler, Bernoulli) revolved around whether any complex vibration could be represented by a simple formula like a trigonometric series. Fourier's revolutionary discovery—that piecewise continuous functions (even with jumps) could be represented by such series—shattered this equation. It demonstrated that a single analytic representation could describe a curve assembled from disparate, "inorganic" parts. The state of the field was thus one of crisis: the intuitive, formula-based understanding of functions was untenable, yet no new, universally accepted foundation existed. The immediate problem was to define a "function" in a way that was general enough to accommodate Fourier's results while being rigorous enough to serve as a foundation for analysis.

## Key Contributions
Luzin, writing as a historian and mathematician, does not introduce new mathematical results but provides a masterful synthesis and interpretation of a critical period. His key contributions are:
1.  **Framing the Schism:** He explicitly frames the post-Fourier evolution as a bifurcation into two opposing conceptual programs, personified by Weierstrass and Dirichlet, tracing their intellectual lineage back through the earlier debates.
2.  **Synthesis of the Critique of Dirichlet:** He masterfully synthesizes the philosophical critiques leveled against Dirichlet's overly permissive definition by Brodén, Borel, Baire, and Lebesgue. He clarifies their distinct objections: Brodén on communicability, Borel on "lawlessness," Baire on the necessity of a constructible description, and Lebesgue on the limitations of analytic representation.
3.  **Clarifying the Baire Classification and Its Limits:** He explains Baire's hierarchical classification of functions by their descriptive complexity and highlights Lebesgue's groundbreaking result that functions exist outside this entire classification, demonstrating that logical definition outstrips mathematical (analytic) construction.
4.  **Introducing the Moscow School's Challenge:** He presents the work of his Moscow colleagues (like Lusin and his students) as a further complication, showing that even Lebesgue's framework was incomplete, as some analytically definable functions (via triple limits) resisted classification into Baire's hierarchy.
5.  **Historical Narrative as Argument:** His primary contribution is the compelling historical argument that the "function concept" remains an active, unresolved problem in the foundations of mathematics, with contemporary debates echoing the old controversies.

## Methodology
Luzin's methodology is **historical and polemical**. He constructs a narrative of ideas, tracing lines of influence and conflict through key figures and their definitions. The argument is structured as a chronological drama of intellectual breakthrough and subsequent challenge. He uses:
*   **Conceptual Genealogy:** Mapping the "grouping of names" to show intellectual descent (e.g., Fourier -> Dirichlet -> Lebesgue -> Moscow School).
*   **Thought Experiments:** Relaying Borel's queue of people naming digits to illustrate the philosophical divide over determinacy and law.
*   **Technical Summary as Narrative:** Explaining the Baire classification and its negation not as a pure mathematical exercise but as a plot point in the story of definability.
*   **Rhetorical Juxtaposition:** Placing the initial "serenity" achieved by Dirichlet's definition against the "consternation" it later caused to emphasize the dynamism of mathematical thought.

## Influence
As a translation of a 1930s encyclopedia article, this specific text's direct citation influence is secondary to Luzin's original work. However, Luzin's synthesis has been influential in:
1.  **Pedagogy of Analysis:** It provides a profound historical context for the real analysis curriculum, explaining *why* definitions are what they are.
2.  **Philosophy of Mathematics:** It is a seminal text in discussions about definability, mathematical existence, and the role of constructive laws (connecting to debates about the Axiom of Choice).
3.  **Mathematical Logic:** The debates it chronicles (Borel, Baire) fed directly into the development of descriptive set theory and the study of definable sets of real numbers.
4.  **Historiography of Science:** It models a certain style of internalist, narrative history of mathematical concepts.

The paper traces a lineage from Fourier, through Dirichlet, to the foundational work of Borel, Baire, and Lebesgue, and finally to the Moscow School, which Luzin represented. It helped cement the view that the development of 19th-century analysis was driven by foundational crises.

## Connections to Other Papers in the Collection
*   **Thurston 1994 (Proof and Progress):** Both papers are deeply concerned with the *practice* and *communication* of mathematics. Thurston focuses on proof as a vehicle for conveying understanding; Luzin focuses on definitions as attempts to codify concepts for communication. Both explore the gap between formal objects and human comprehension.
*   **Hofstadter 2001 (Analogy):** Luzin's narrative is built on a core analogy: the evolution of "function" mirrors the earlier debate about the vibrating string. He also explores the analogy between "logical definition" and "mathematical definition," showing their non-equivalence.
*   **Papert 1980 (Mindstorms):** Connects to the theme of definitional frameworks enabling or constraining thought. Just as LOGO provides a computational framework for thinking, Dirichlet's definition provided a framework for analysis, but one whose limitations, as Luzin shows, eventually constrained mathematical imagination.
*   **Lockhart 2002 (Mathematician's Lament):** Both decry a ossified view of mathematics. Lockhart laments the deadening effect of procedural teaching; Luzin laments any view that the "function concept" is a settled, dead issue. Both champion mathematics as a living, evolving process of inquiry.

## Modern Relevance
Luzin's analysis is strikingly relevant to contemporary issues in computation and AI:
1.  **The "Black Box" Problem in AI:** Modern neural networks are quintessential Dirichlet functions—they are arbitrary mappings from input to output with no discernible analytic representation or "law." They are, in Borel's terms, "lawless." The debate over their interpretability is a direct echo of the arguments Luzin chronicles about communicability and the necessity of a descriptive law.
2.  **Functional Programming and Computability:** The paper's core tension maps onto the distinction in computer science between *specification* (the function as a mapping) and *implementation* (the algorithm or analytic expression). The search for "referential transparency" in functional programming relates to the desire for predictable, analyzable functions. Conversely, the existence of non-computable functions (a logical, not analytic, definition) mirrors Lebesgue's non-Baire function.
3.  **Data-Driven Science:** The shift from theory-driven models (analytic expressions) to machine-learned models (complex, opaque functions) recapitulates the post-Fourier turn. We accept models that work (fit data) without requiring an organic, analytic understanding, reigniting debates about what constitutes a satisfactory "explanation."
4.  **Mathematical Education:** The paper argues that understanding *why* we define things as we do is crucial. This supports a historical, conceptual approach to teaching mathematics, moving beyond rote manipulation of definitions to grasp their origins and philosophical stakes.

## Key Quotes
1.  > "His discovery showed clearly that most of the misunderstandings that arose in the debate about the vibrating string were the result of confusing two seemingly identical but actually vastly different concepts, namely that of function and that of its analytic representation."
    *   *Analysis: This is the paper's central thesis in miniature. It identifies the precise conceptual error that Fourier's work corrected, setting the stage for all subsequent developments.*

2.  > "It seemed that the only property of the values of an analytic expression was their determinacy, and that they were otherwise completely arbitrary, each independent of the others. This was the sense of the definition of the function concept given by Dirichlet."
    *   *Analysis: Captures the radical reductionism of Dirichlet's definition—its power and its philosophical peril. It defines a function by its output, discarding any notion of intrinsic connection between points.*

3.  > "For our minds all reduces to the finite."
    *   *Analysis: Baire's concise rebuttal of the notion of a "lawless" infinite object. It argues that mathematical understanding is fundamentally a communicable, step-by-step process, a view that challenges naive Platonism.*

4.  > "Lebesgue goes one step further and claims that a mathematician who does not have a law that realizes a function y(x) he is considering cannot be certain that he is talking about the same function at different moments of his investigation."
    *   *Analysis: Extends the communicability argument to internal consistency. It suggests that without a definable law, a mathematical object lacks a stable identity, making coherent thought about it impossible.*

5.  > "Thus while Lebesgue is willing to accept any law (logical or mathematical) as long as it yields an individual function, Borel insists on the restriction that the law be countable... Brouwer seems to go still further..."
    *   *Analysis: This snippet shows the spectrum of opinions within the "anti-Dirichlet" camp, highlighting that the objection to "lawlessness" was not monolithic but existed on a continuum of constructivism.*

6.  > "the controversy about the vibrating string has been renewed in another light and with a different content."
    *   *Analysis: The paper's ultimate conclusion. It asserts that foundational debates in mathematics are not settled but transform, with the core issue of definability and existence recurring in new forms.*