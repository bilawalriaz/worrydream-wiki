---
title: Mead 2022 - Neuromorphic Engineering, In Memory of Misha Mahowald
created: 2026-06-10
updated: 2026-06-10
type: entity
tags: [computing-history, hci, mathematics, physics]
sources: [raw/papers/Mead_2022_-_Neuromorphic_Engineering,_In_Memory_of_Misha_Mahowald.txt]
confidence: high
---

# [[mead-1996-oral-history-cohen|Mead]] 2022 - Neuromorphic Engineering, In Memory of Misha Mahowald

## Core Thesis
Carver [[mead-1996-oral-history-cohen|Mead]]’s review argues that the two historically divergent threads of neural-inspired computing—**(1) software-based artificial neural networks (ANNs) trained via backpropagation on general-purpose hardware, and (2) custom, low-power silicon circuits implementing neural principles (neuromorphic hardware)—are not only both central to modern computation but are fundamentally converging.** This convergence is driven by an unavoidable physical and economic reality: the end of "free" scaling under [[moore-1991-forth-the-early-years|Moore]]’s Law and the escalating energy cost of computation. The paper’s central thesis is that future advances in computing, particularly for AI, will depend on integrating the algorithmic innovations of the first thread with the energy-efficient, distributed, and sensory-centric architectural principles of the second. Neuromorphic engineering is thus repositioned from a niche biomimetic pursuit to a necessary paradigm for sustainable, large-scale computation.

The nuance lies in [[mead-1996-oral-history-cohen|Mead]]’s framing of this convergence as a *physical inevitability*, not just a technical opportunity. He uses the energy dissipation gap between a single transistor switch (~10⁻¹⁶ J) and a server-level operation (~10⁻³ J) as a quantitative indictment of current digital computing architecture. The inefficiency stems from moving data, not processing it. The convergence, therefore, is about restructuring algorithms to be physically local and event-driven, mirroring the brain’s efficiency.

## Historical Context
The paper is written as a retrospective from 2022, looking back to the journal *Neural Computation*’s 1989 founding as a symbolic starting point. In 1989, the field was split:
*   **Thread 1 (AI/ML):** Dominated by computer scientists using backpropagation (Rumelhart, Hinton, & Williams, 1986) to train networks on general-purpose computers. The goal was algorithmic learning.
*   **Thread 2 (Neuromorphic):** Led by engineers and physicists like [[mead-1996-oral-history-cohen|Mead]] and his student Misha Mahowald (to whom the paper is dedicated). They were building analog VLSI systems (e.g., the silicon retina, cochlea) based on biological principles to process real-time sensory data with extreme energy efficiency. The goal was physical embodiment of neural function.

The intervening d[[moore-1991-forth-the-early-years|ecade]]s saw a dramatic, ironic shift. [[moore-1966-autotelic-responsive-environments-and-exceptional-children|Moore]]’s Law propelled general-purpose computing (GPUs in particular) to massive scale, enabling the deep learning revolution triggered by Krizhevsky’s AlexNet in 2012. This made Thread 1 (software ANNs) the dominant, industrial paradigm. Thread 2 (neuromorphic hardware) remained a specialized, academic endeavor with limited commercial application until the 2010s. [[mead-1996-oral-history-cohen|Mead]]’s review situates itself at the moment when the physical limits of the digital computing paradigm (power density, data movement costs) are becoming the primary bottleneck for further scaling of Thread 1, creating a critical need for the architectural insights of Thread 2.

## Key Contributions
1.  **A Unifying Energy-Centric Narrative:** [[mead-1996-oral-history-cohen|Mead]] reframes the entire history of computing, from mechanical calculators to modern data centers, as a long-term quest to reduce energy per operation. He uses this to explain technological shifts (e.g., NMOS to CMOS) and to diagnose the core inefficiency of modern digital systems: the von Neumann bottleneck and the energy cost of data movement.
2.  **Quantifying the Efficiency Gap:** He provides the stark quantitative comparison (≈10¹³ factor) between the theoretical minimum energy of a transistor switch and the actual energy consumed per operation in a 2010 server. This data powerfully justifies the need for architectural, not just algorithmic, revolution.
3.  **Reframing Neuromorphic Engineering's Role:** He moves neuromorphic engineering from the margins to the center of the computational future. It is not merely about building "brain-like" chips, but about discovering and implementing the physical principles (locality, event-driven processing, co-located memory and compute) that achieve radical efficiency.
4.  **Tracing the Co-evolution of "AI" and "Hardware":** The paper meticulously links algorithmic breakthroughs (ReLU, AlexNet, capsules) to hardware realities (GPU development, specialized accelerators like TPUs). It shows how the two threads, once separate, are now forcing each other to evolve: ANNs are becoming more "neuromorphic" (spiking networks, event-driven sensors), and neuromorphic hardware is incorporating ANN-like training principles.

## Methodology
The methodology is a **historical-technical synthesis and polemic**. [[mead-1996-oral-history-cohen|Mead]]:
*   **Uses historical narrative** (from Whirlwind to the cloud) to establish the long-term trend of energy efficiency as the driver of [[postman-1998-five-things-we-need-to-know-about-technological-change|technological change]].
*   **Employs quantitative analysis** (the energy cost graphs) to substantiate his core critique of digital computing inefficiency.
*   **Leverages his unique insider perspective** as a founder of the field to connect disparate threads (the rise of GPUs for gaming, the birth of optical networking, the development of the Internet economy) into a coherent story of co-evolution.
*   **Argues by analogy and principle,** comparing digital systems unfavorably to the brain's efficiency and proposing that the future lies in hybrid systems that adopt the brain's "wiring" advantages.
*   The structure is **thematic rather than chronological**, moving from general-purpose computing, to neural networks, to neuromorphic circuits, and finally to their convergence.

## Influence
As a 2022 review by a founding figure in the field, this paper synthesizes and legitimizes decades of work rather than introducing a single new experiment. Its influence is in:
1.  **Shaping the Research Agenda:** It provides a powerful, high-level justification for funding and research into neuromorphic computing, edge AI, and brain-inspired architectures by framing them as essential for the next phase of computing.
2.  **Guiding Commercial Development:** Companies like Intel (with its Loihi neuromorphic chips), SynSense, and others developing event-based vision sensors and spiking neural network hardware find in [[mead-1996-oral-history-cohen|Mead]]'s analysis a validation of their technical direction.
3.  **Educating a New Generation:** The paper serves as a seminal review article, defining the field's history, principles, and future trajectory for students and researchers entering from either the ML or hardware side.
4.  **Influencing AI Hardware Design:** It underscores the move away from pure GPU-based training toward specialized AI accelerators that exploit data locality, a direct lesson from the neuromorphic principle.

## Connections to Other Papers in the Collection
*   **[[bush-1945-as-we-may-think-with-engelbart-notes|Bush 1945]] (As We May Think):** [[vannevar-bush-symposium-1995-closing-panel|Bush]] envisioned machines [[engelbart-1962-augmenting-human-intellect|augmenting human]] thought through associative trails and personal, flexible interfaces. [[mead-1996-oral-history-cohen|Mead]]’s neuromorphic engineering seeks the physical substrate to make such thinking machines not just associative but also efficient and embodied, processing streams of real-world data like a brain.
*   **[[kay-1972-personal-computer-for-children|Kay 1972]] ([[kay-1972-a-personal-computer-for-children-of-all-ages|Personal Computer]]):** [[kay-2013-what-is-a-dynabook|Kay]]’s vision of the personal computer as a medium for thought emphasizes individual creativity. Neuromorphic engineering, by enabling low-power, always-on, intelligent sensory processing, i[[kay-2013-what-is-a-dynabook|s t]]he technological enabler for [[kay-1968-flex-a-flexible-extendable-language|Kay]]’s ultimate dream: truly personal, context-aware computing assistants woven into the environment.
*   **[[anderson-1972-more-is-different|Anderson 1972]] (More is Different):** [[anderson-1972-more-is-different|Anderson]] argued that [[cook-2000-how-complex-systems-fail|complex systems]] exhibit emergent properties at higher scales. The brain is the paramount example. Neuromorphic engineering, as described by [[mead-1996-oral-history-cohen|Mead]], is an attempt to build complexity from the bottom up, with simple units (neurons, synapses) giving rise to intelligent behavior through their organization and connectivity, not from a top-down program.
*   **[[feynman-1974-cargo-cult-science|Feynman 1974]] (Cargo [[feynman-1974-cargo-cult-science|Cult Science]]):** [[feynman-1974-cargo-cult-science|Feynman]] criticized science that follows the form of research without its substance. [[mead-1996-oral-history-cohen|Mead]]’s critique of the digital computing paradigm—spending 10¹³ times more energy than necessary by "shoveling bits around"—[[feynman-1974-cargo-cult-science|can be ]]seen as a description of a [[feynman-1974-cargo-cult-science|cargo cult]] approach to computation: following the ritual of digital logic without engaging with the underlying physics of efficient computation.

## Modern Relevance
[[mead-1996-oral-history-cohen|Mead]]’s paper is strikingly relevant to contemporary trends:
*   **AI’s Energy Crisis:** The enormous carbon footprint of training large language models (LLMs) makes his argument for energy-efficient architectures urgent. Neuromorphic principles offer a path to sustainable AI scaling.
*   **Edge AI and IoT:** The demand for intelligent processing on tiny, battery-powered devices (cameras, sensors, wearables) is the commercial realization of Mahowald’s and [[mead-1996-oral-history-cohen|Mead]]’s work. Event-driven se[[moore-1991-forth-the-early-years|nsors]] and spiking neural networks are ideal for this.
*   **The Limits of [[moore-1966-autotelic-responsive-environments-and-exceptional-children|Moore]]’s Law:** With transistor scaling slowing, performance gains must come from architectural innovation. [[mead-1996-oral-history-cohen|Mead]]’s paper champions the brain-inspired architectural revolution as the primary source of future gains.
*   **The "Convergence" in Practice:** Modern AI chips (like Google’s TPU or various neuromorphic-inspired cores) increasingly integrate memory and compute, use dataflow architectures, and employ low-precision arithmetic—all principles advocated by neuromorphic engineering. The lines between a "GPU," an "AI accelerator," and a "neuromorphic chip" are blurring.

## Key Quotes
1.  **"The real cost of computation versus year... Notice that computation is the number of operations per second: we can always get more operations by waiting longer."**
    *(Analytical note: This redefines computation in terms of energy and time, setting up the paper's core metric for judging technological progress.)*
2.  **"There is a factor of ≈10¹³ between the energy to make a transistor work and that required to do an operation the way we do it in a digital computer."**
    *(Analytical note: This single statistic is the paper's bombshell, quantifying the colossal inefficiency of current computing and defining the scale of the opportunity for neuromorphic engineering.)*
3.  **"We lose a factor of more than 1000 because of the way we build digital hardware... most of the energy is expended moving data around rather than using those data where they originate."**
    *(Analytical note: Diagnoses the von Neumann bottleneck not as an abstract [[hamming-1968-one-mans-view-of-computer-science|computer science]] concept, but as a concrete, wasteful physical phenomenon.)*
4.  **"This review concentrates on energy per computation as the central long-term theme. There are often other commercial considerations that dominate technology choices, but we will not dwell on them here."**
    *(Analytical note: A methodological declaration. [[mead-1996-oral-history-cohen|Mead]] is intentionally ignoring short-term market forces to focus on the enduring physical and thermodynamic constraints that shape technology over decades.)*
5.  **"The quest to make something that 'works like the brain' has come to mean very different things to different people."**
    *(Analytical note: Acknowledges the field's conceptual fragmentation and sets the stage for his argument that a unifying principle—efficiency—is finally emerging.)*
6.  **"We will find that this divergence is illusory and that at a deeper level, the two threads are actually converging."**
    *(Analytical note: This is the paper's central prophetic claim, positioning it as a roadmap for the field's future integration.)*