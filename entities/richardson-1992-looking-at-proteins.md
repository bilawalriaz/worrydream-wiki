---
title: Richardson 1992 - Looking at proteins
created: 2026-06-10
updated: 2026-06-10
type: entity
tags: [computing-history, hci, cognitive-science, education, structural-biology]
sources: [raw/papers/Richardson_1992_-_Looking_at_proteins.txt]
confidence: high
---

# Richardson 1992 - Looking at proteins

## Core Thesis
The paper argues that scientific understanding of complex, invisible structures like proteins is fundamentally an act of active, interpretive *looking*. This process is not passive observation but a skilled performance of selection, simplification, and representation. The core thesis is twofold: 1) Multiple, complementary representational schemes are not just helpful but *necessary* to grasp different facets of a protein's one-dimensional sequence, three-dimensional shape, and dynamic motions. 2) The practical act of designing proteins "from scratch" serves as a powerful, reciprocal lens for understanding the principles of natural protein folding, revealing both our successes and our profound gaps in knowledge. The nuance lies in framing visualization not as a mere illustration of data, but as a primary cognitive tool for discovery and a dialogic partner in experimental science.

## Historical Context
By 1992, protein crystallography and NMR had produced a wealth of 3D structures, but the field was grappling with two interconnected challenges: interpretation and prediction. The "protein folding problem" remained central—how does a linear chain find its unique native state? Traditional visualization tools, from physical brass Kendrew models to early computer graphics, were reaching their limits. They often presented static, monolithic views that obscured the interplay between chain connectivity and spatial packing. The rise of computational power was enabling simulation but also new questions about representation itself. This paper emerges from the Richardson lab's decades of work on protein structure analysis (e.g., ribbon diagrams) and is positioned at a pivotal moment: the first successful *de novo* protein designs were emerging (e.g., Hecht et al., 1990, the "Felix" molecule), but they were revealing a sobering reality—designed proteins were less ordered than natural ones. The field needed a new framework to synthesize representation, analysis, and design into a unified inquiry.

## Key Contributions
1.  **Formalization of the Representational Imperative:** The paper systematically argues against a "correct" view and for a toolkit of views. It catalogues and justifies distinct representational modes: connectivity-focused (stick, ribbon), space-filling (CPK, dot surfaces), interactive/composite (dot surfaces with internal stick), dynamic (animation of motion), and didactic (simplification for communication).
2.  **Introduction of Specific Visualization Tools:** Popularized and operationalized concepts like "ribbon schematics" (building on earlier work) and pioneered the use of "small-probe contact dots" to explicitly visualize van der Waals contacts and hydrogen bonds between molecular surfaces.
3.  **The Design-Analysis Feedback Loop:** Established protein design as a critical epistemological tool. The failure to achieve unique, native-like structures in designed proteins ("molten globule" states) is framed not as a dead end, but as a crucial result that redirects inquiry toward understanding the determinants of core packing and unique conformations.
4.  **Negative Design as a Concept:** Highlighted that successful design requires not just specifying desired interactions (positive design) but also *actively blocking* unwanted alternatives (e.g., aggregated sheets, wrong helix-bundle topology). This shifted focus from mere stability to specificity and uniqueness.
5.  **Pedagogy through Kinemages:** Advocated for interactive, manipulable computer graphics ("kinemages") as essential for both research and education, arguing they allow the user to perceive relationships (like domain motions) that static images cannot convey.

## Methodology
The methodology is **experiential and epistemological**, blending **polemics** with **empirical case studies**. The authors argue their case by:
1.  **Demonstrative Critique:** Using classic examples (brass model, CPK model) to show the limitations of single-representation thinking.
2.  **Iterative Application:** Applying their representational toolkit to well-known proteins (ribonuclease A, myohemerythrin, T4 lysozyme) to reveal features invisible in standard views (e.g., the hydrogen-dominated surface, helix-helix contacts, domain motions).
3.  **Dialogic Empiricism:** Using data from their own protein design experiments as a central, live experiment. The "unexpected general result" of disordered designs becomes the pivot point for theoretical reflection on natural folding.
4.  **Philosophical Framing:** The argument is structured as a manifesto for a way of *doing science*, where seeing is active, multiple, and cyclical (look -> hypothesize -> design -> look again).

## Influence
This paper solidified the Richardson lab's role as the leading methodological voice in structural biology visualization. Its influence is broad:
- **Citation:** Heavily cited in methods papers, textbooks, and reviews on protein structure visualization and analysis through the 1990s and 2000s.
- **Tooling:** The philosophy directly informed the development and ethos of software like **MolScript** (Kraulis, 1991), **RasMol** (Sayle, 1994), and later **PyMOL** and **Chimera**, which made ribbon diagrams and surface views standard. The concept of kinemages influenced molecular animation tools.
- **Research Agenda:** It framed the "design vs. natural folding" comparison as a key area of study, a thread that continues in modern efforts to design proteins that mimic the stability *and* specificity of natural ones.
- **Education:** Popularized the use of interactive 3D graphics in biochemistry education, aligning with constructionist learning theories (à la Papert).

## Connections to Other Papers in the Collection
- **Bush 1945 (As We May Think):** Bush’s vision of the *memex* and associative trails finds a concrete scientific counterpart in Richardson’s *kinemages*. Both advocate for tools that augment human cognition by allowing dynamic, non-linear exploration of complex information spaces (molecular structures vs. documents).
- **Engelbart 1962 (Augmenting Human Intellect):** Richardson’s framework is a direct application of Engelbart’s goal to "increase the capability of a man to approach a complex problem situation." The ribbon diagram, animation, and interactive model are *augmentation tools* that re-describe the protein in a form more amenable to human perception and insight.
- **Papert 1980 (Mindstorms):** The paper’s emphasis on *looking* as an active, interpretive process aligns with Papert’s constructionism. The researcher/designer learns by building (designing proteins) and perceiving (looking at the results), using representations as "objects-to-think-with." The failure of designs is a powerful learning event.
- **Anderson 1972 (More is Different):** This connection is profound. Anderson argues that at each scale, new principles emerge. Richardson’s representational struggle embodies this: a list of coordinates (fundamental) is different from a ribbon diagram (emergent pattern of folding), which is different from an animation (emergent dynamics). You *need* the different levels, and no single view captures the whole.
- **Thurston 1994 (Proof and Progress):** Thurston discusses how mathematical understanding is about explanation, not just formal proof. Similarly, Richardson argues that scientific understanding in structural biology is about *seeing* relationships and *explaining* structure, not just possessing coordinates. The representations are the language of explanation.

## Modern Relevance
The paper’s insights are more relevant than ever in the era of **AI-driven structural biology**.
- **AlphaFold and Representation:** While AI like AlphaFold solves the prediction problem, it does not solve the *understanding* problem. A predicted PDB file is a list of coordinates, not an insight. The Richardson toolkit (ribbons, surfaces, animations) is essential for interpreting these AI outputs, for asking "why this fold?" and for integrating prediction with function.
- **Design as a Testbed for AI:** The paper’s design-as-analytical-tool philosophy parallels current uses of protein design (e.g., with RFdiffusion) to test physical principles. The gap between design and natural structure, noted by Richardson, is being narrowed by AI, but the fundamental question of achieving *unique* cores remains.
- **Cognitive HCI and Data Visualization:** In an age of "big data" in biology (genomics, cryo-EM maps), the paper’s core argument is a timeless guide: effective insight requires multiple, interactive, carefully curated representations that match the scale and questions of the human mind. It’s a foundational text for the field of scientific visualization.
- **Education and Communication:** With tools like AlphaFold DB and Mol* viewer, the principles here are directly applied in online biology education and open science, enabling global, interactive exploration of the protein universe.

## Key Quotes
1.  > "Looking, and especially seeing, is an active process of interpreting, of finding and emphasizing patterns, of adding things and deleting things."
    *(Analytical commentary: This is the paper’s philosophical foundation. It equates scientific seeing with artistic composition, framing the researcher as an active creator of meaning, not a passive recipient of data.)*

2.  > "Each representation emphasizes different features of the structure and can help you see those features in the first place (while helping you ignore other things, for better and for worse)."
    *(Analytical commentary: A pragmatic statement on the trade-offs of any abstraction. It legitimizes the use of multiple, imperfect tools and warns against the "tyranny of a single view.")*

3.  > "The protein surface consists almost entirely of hydrogens... This is true both for the outside... and also for the internal contact surfaces."
    *(Analytical commentary: A striking example of how a simple representational choice (coloring by atom type) can reveal a profound, non-obvious physical truth about molecular interactions.)*

4.  > "The design and synthesis of new proteins 'from scratch' provides a route toward the experimental testing of such ideas."
    *(Analytical commentary: Elevates protein design from a technical feat to a core methodological pillar of basic science, a form of computational and experimental hypothesis testing.)*

5.  > "Apparently we do indeed know enough to successfully design proteins that fold into approximately correct structures, but not enough to design unique, native-like structures."
    *(Analytical commentary: The paper’s pivotal, humbling conclusion. It defines the boundary of knowledge in 1992 with remarkable clarity and sets the agenda for the next three decades of work.)*

6.  > "The total process of looking scientifically at proteins involves communication as well as perception."
    *(Analytical commentary: Links the private act of cognition with the public act of science. The representation must not only help *me* see, but must enable *you* to see it too.)*

7.  > "A flat sheet of paper and the object into which it can be folded by origami... In both cases, the starting material is simple... but the final product has complex structure and biological function."
    *(Analytical commentary: Uses the elegant, physical analogy of origami to encapsulate the miracle and complexity of protein folding, making the abstract problem visceral.)*

8.  > "We require statistics on very narrowly defined structural categories and explicit attention to 'negative design' criteria that actively block unwanted alternatives."
    *(Analytical commentary: A concrete, practical principle emerging from the design experience. It shifts the design goal from merely finding a stable state to uniquely specifying one state among a landscape of possibilities.)*