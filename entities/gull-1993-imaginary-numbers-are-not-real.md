---
title: Gull 1993 - Imaginary Numbers are not Real
created: 2026-06-10
updated: 2026-06-10
type: entity
tags: [hci, programming-languages, mathematics, physics]
sources: [raw/papers/Gull_1993_-_Imaginary_Numbers_are_not_Real.txt]
confidence: high
---

# Gull 1993 - Imaginary Numbers are not Real

## Core Thesis
The paper argues that the complex imaginary unit \(i\) (and the broader use of complex numbers in physics) is not a mysterious, fundamental abstraction, but a direct geometric consequence of the algebraic product defined on real vectors. Specifically, in a two-dimensional geometric algebra, the directed area element (bivector) squares to -1, providing a "real" geometric meaning for the imaginary unit. This reframing reveals that much of physics, including electromagnetism and even some results attributed solely to quantum theory, can be expressed more naturally and powerfully in a real-numbered geometric algebra of spacetime. The central claim is not just pedagogical; it is ontological and methodological. The authors contend that conventional vector calculus and matrix notations are ad-hoc, fragmented, and hide geometric structure, whereas Hestenes' Spacetime Algebra (STA) is the unified, geometrically grounded language that physics requires. The "surprising" results they derive classically (e.g., a geometric form of the Dirac equation) are presented as evidence of this superior descriptive power.

## Historical Context
By 1993, the mathematical language of theoretical physics was a hybrid ecosystem. Complex numbers, introduced by Euler and formalized by Cauchy, were ubiquitous in oscillations, waves, and quantum mechanics. Quaternions, invented by Hamilton, found use in rotations but were largely superseded by Gibbs' vector analysis. Quantum mechanics relied heavily on matrix mechanics (Heisenberg) and spinor formalisms (Pauli, Dirac), which were mathematically powerful but abstract. Geometric Algebra (GA), rooted in the 19th-century work of Grassmann and Clifford, had been largely marginalized. David Hestenes' foundational work, particularly his 1966 *Space-Time Algebra*, had developed STA but had not gained mainstream traction. The problem [[hestenes-1983-quantum-mechanics-from-self-interaction|Hestenes]], and later Gull, Lasenby, and Doran, sought to solve was twofold: the "Babel" of notations (Grassmann's, Gibbs', Clifford's, quaternions) and the lack of a single, intuitive algebraic structure that naturally encoded rotations, reflections, and spacetime geometry without introducing artificial complex numbers or splitting spacetime into 3+1 dimensions from the outset.

## Key Contributions
1.  **Pedagogical Demystification of Imaginary Numbers:** The paper provides a clear, tutorial-style derivation showing how the bivector \(\sigma_1\sigma_2\) in a 2D GA squares to -1, making \(i\) a geometric entity.
2.  **Promotion of Spacetime Algebra (STA) as the Primary Framework:** It strongly advocates for Hestenes' STA—based on a 4D Clifford algebra with signature (+---)—as the natural arena for classical and quantum physics.
3.  **Geometric Reformulation of Classical Physics:** It demonstrates the power of STA by:
    *   Combining Maxwell's equations into a single, elegant multivector equation: \(\nabla F = J\).
    *   Deriving the electromagnetic field of an accelerating charge using geometric products.
    *   Showing that the Lorentz [[air-force-1960-air-force-office-of-scientific-research|force]] and the geometry of spinors (rotations/reflections) are natural in GA.
4.  **Bridging Classical and "Quantum" Geometry:** The paper claims and demonstrates that many results thought to require quantum theory (e.g., spinors, the Dirac equation's structure) can be derived classically using geometric algebra, suggesting a hidden geometric unity.
5.  **Direct Comparison and Critique of Conventional Methods:** It explicitly contrasts GA with Gibbs vector calculus and matrix methods, highlighting GA's coordinate-free nature, dimension independence, and avoidance of cross-product ambiguities.

## Methodology
The methodology is primarily **expository and polemical**, structured as a tutorial building from simple to complex. It begins by "un-learning" the cross product and introducing the outer product, then defines the geometric product as the fundamental operation. The argument proceeds by example: analyzing 2D and 3D space to build intuition, then extending to spacetime and electromagnetism. The tone is didactic but urgent, framed by the authors' frustration with the field's resistance to Hestenes' ideas. They position themselves as translators, stating their goal is to "AMPLIFY and state [Hestenes'] message in a language that ordinary physicists understand." The paper is theoretical and algebraic, relying on logical derivation from axioms (the properties of the geometric product) and demonstrating consistency with known physics. It is deliberately classical to underscore that the power of GA is not contingent on quantum postulates.

## Influence
This 1993 *Foundations of Physics* paper was instrumental in catalyzing the modern resurgence of Geometric Algebra in academia and engineering. It acted as a clear, accessible gateway, especially for physicists. Following its publication:
*   The **Cambridge GA group** (Gull, Lasenby, Doran, and others) became prolific, applying GA to general relativity, computer graphics, and robotics.
*   It influenced developments in **computational geometry** and **physics engines** (e.g., libraries like *GABLE*, *GAViewer*).
*   It laid groundwork for later, more advanced texts like Doran & Lasenby's *Geometric Algebra for Physicists* (2003).
*   It fed into the broader "Geometric Calculus" movement, influencing how multivariate calculus is conceptualized and taught.
*   Its core argument about complex numbers has been echoed in fields like **electrical engineering** and **computer graphics**, where GA offers more direct representations of rotations and transforms.

## Connections to Other Papers in the Collection
*   **William Clifford (referenced in epigraph):** Clifford invented the algebra the paper advocates for. This paper is a modern vindication and practical application of Clifford's vision.
*   **Thomas Kuhn (implied):** The paper's struggle to change physicists' "normal science" language fits Kuhn's model of paradigm shift. It identifies the conventional notation as a rigid paradigm impeding clear geometric thinking.
*   **Seymour [[papert-1980-mindstorms-1st-ed|Papert]] (1980, *Mindstorms*):** Strong resonance. Both argue for a "low threshold" computational/geometric language (GA/Logo) that connects directly to intuitive, geometric thinking ("low floor"). Both are critiques of abstract, disembodied formalism (matrix QM / traditional math) that creates unnecessary barriers.
*   **J. R. Pierce (1972, *The Unreasonable Effectiveness* - not in list, but thematic):** The paper's claim that GA is the "most powerful and general language" is a direct engagement with Pierce's question about mathematical language and nature. GA is presented as more "effective" because it maps directly to geometric reality.
*   **Brian Cantwell [[smith-da-2003-croquet-a-collaboration-system-architecture|Smith]] (1996, *On the Origin of Objects* - not in list, but thematic):** The paper's insistence on deriving imaginary units from real geometry parallels Smith's project of grounding mathematical entities in primitive, spatial/geometric commitments.
*   **HyperCard / Kay's Dynabook (Kay, 1972):** GA's multivector concept—a coherent bundle of scalars, vectors, bivectors—is analogous to HyperCard's "card" as a heterogeneous collection of data types (text, fields, buttons). Both are attempts to create richer, more structured data objects than flat lists or scalar arrays.

## Modern Relevance
*   **AI and Spatial Reasoning:** GA provides a principled mathematical framework for AI systems that need to manipulate rotations, reflections, and geometric transformations—crucial for robotics, 3D vision, and simulated environments. Its coordinate-free nature aligns with the goal of AI understanding geometry in a general way, not tied to a specific reference frame.
*   **Programming Languages:** The paper's core insight—that conventional programming constructs (like separate `Vector` and `Complex` classes) often misrepresent the underlying geometry—parallels modern language design seeking more expressive, geometrically coherent primitives. GA offers a model for algebraic type systems.
*   **Education:** It represents a powerful critique of how mathematics is taught. By showing "imaginary" numbers as concrete areas, it embodies the "concreteness before abstraction" philosophy, relevant to CS and math pedagogy (see Papert, [[lockhart-2002-a-mathematicians-lament|Lockhart]]).
*   **Knowledge Management & Tool Building:** The paper is an argument for a better *notation* as a thinking tool. This is the central theme of the WorryDream collection. GA, like a well-designed HyperCard stack or Engelbart's augmented intellect, is a "thinking tool" that externalizes geometric intuition, potentially enabling more powerful reasoning about physical systems.

## Key Quotes

1.  **"physicists quickly become impatient with any discussion of elementary concepts"** - *Reveals the paper's core antagonist: disciplinary impatience with foundational critique. It frames the resistance to GA as a psychological and sociological problem, not just a technical one.*
2.  **"we will temporarily un-learn the cross product"** - *A key pedagogical moment. "Un-learning" is presented as essential to progressing beyond 3D-specific, incomplete representations. This is a direct parallel to the need to "un-learn" flawed programming abstractions.*
3.  **"The result of adding a scalar to a bivector is an object that has both scalar and bivector parts, in exactly the same way that the addition of real and imaginary numbers yields an object with both real and imaginary parts."** - *This is the paper's pivotal conceptual bridge. It reframes complex numbers not as a different number system, but as a multivector in a 2D geometric algebra, dissolving their mystery.*
4.  **"we believe that he wrote no less than the truth and that, as a result of learning how to multiply vectors together, we can all gain a great increase in our mathematical facility and understanding."** - *A passionate endorsement of Hestenes' project. The "great increase" promised is not minor efficiency, but a fundamental shift in understanding and capability.*
5.  **"Physics is greatly facilitated by the use of [[hestenes-1983-quantum-mechanics-from-self-interaction|Hestenes]]’ spacetime algebra, which automatically incorporates the geometric structure of spacetime."** - *The central technical claim. The advantage is automatic and structural, not a forced fit. It argues GA is isomorphic to physical reality in a way other formalisms are not.*
6.  **"In the course of this purely classical exposition many surprising results are obtained — results which are usually thought to belong to the preserve of quantum theory."** - *A provocative thesis. It suggests the geometric language of GA is so natural that it naturally contains "quantum" structures, blurring the classical/quantum divide and pointing to a deeper geometric unity.*
7.  **"We conclude that geometric algebra is the most powerful and general language available for the development of mathematical physics."** - *The paper's definitive, polemical closing statement. It makes an explicit claim of superiority and generality, positioning GA as the rightful successor to the fragmented languages it critiques.*