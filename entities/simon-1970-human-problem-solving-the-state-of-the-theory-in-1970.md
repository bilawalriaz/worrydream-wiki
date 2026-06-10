---
title: Simon 1970 - Human Problem Solving, The State of the Theory in 1970
created: 2026-06-10
updated: 2026-06-10
type: entity
tags: [computing-history, hci, programming-languages, mathematics]
sources: [raw/papers/Simon_1970_-_Human_Problem_Solving,_The_State_of_the_Theory_in_1970.txt]
confidence: high
---

# Simon 1970 - Human Problem Solving, The State of the Theory in 1970

## Core Thesis
Simon and Newell’s 1970 paper is not a presentation of new findings but a programmatic review and manifesto. Its core thesis is that the "magic" of human thought—specifically problem solving—can and should be explained as a physical symbol system operating via heuristic search within a bounded, serial, information-processing architecture. The nuance lies in the argument’s dual purpose: to legitimize the computational theory of mind against both mystification and behaviorist skepticism, and to lay out a concrete, testable research strategy for cognitive science. They are arguing that the search for explanation must be grounded in mechanisms (processes) that can be precisely specified and instantiated in a computer, moving beyond mere behavioral prediction. The paper is a victory lap and a strategic re-commitment, asserting that the core methodology they pioneered—computer simulation of cognitive processes—has successfully passed its "sufficiency proof" stage and now demands rigorous refinement and expansion.

## Historical Context
This paper emerges at a pivotal moment in the history of psychology and artificial intelligence. In 1970, cognitive psychology was ascendant, having largely displaced behaviorism as the dominant paradigm, thanks in no small part to the work of Simon and Newell themselves. The state of the field in 1958, when they published "Elements of a Theory of Human Problem Solving," was vastly different. Problem solving was indeed treated as a "mysterious" capacity, or explained through opaque S-R (stimulus-response) chains. Their work was a direct challenge to this, introducing the digital computer not as a mere calculator but as a universal device for exploring any symbol manipulation process.

The immediate preceding work was their own: the development of the Logic Theorist (1956) and the General Problem Solver (1958), and the formalization of "physical symbol systems." The problem being solved was two-fold: (1) creating a rigorous language to describe mental processes that escaped the vagueness of traditional "mentalism," and (2) demonstrating that this language could generate behavior indistinguishable from human problem solving. By 1970, they were reporting on over a decade of successful simulations across domains like chess, logic, and language acquisition, using a shared architecture (the list-processing languages IPL, the problem-solving language FTP). The paper is thus a mid-course assessment, situating their research program within a maturing cognitive science and preparing for its next phase.

## Key Contributions
1.  **The "Explanation Requirements" Framework:** The paper restates and amplifies their foundational 1958 criteria for a theory of problem solving. This framework—demanding prediction of performance, explanation of process, prediction of incidental phenomena, and accounts of learning—provided a powerful methodological blueprint for cognitive science, moving it beyond mere correlation to mechanism.
2.  **The 11-Step Research Strategy:** The most explicit contribution is the retrospective description of their own research strategy as an 11-step program. This is a profound piece of meta-methodology. It articulates how a research program in cognitive simulation should be structured: from discovering primitive processes, to building simulation languages, to testing and modifying programs against human data, to eventually seeking neurophysiological correlates. It demystifies scientific discovery as a planned, iterative engineering effort.
3.  **Formal Defense of "Mentalism":** Simon and Newell provide a powerful philosophical defense of referencing internal states. They argue that by defining "memory," "symbol structure," and "process" in terms of programmable operations, they have transformed mentalism from vague speculation into a rigorous, falsifiable science. An internal "mental image" is not a metaphor but a data structure.
4.  **Consolidation of the Physical Symbol System Hypothesis:** By 1970, the hypothesis was no longer a speculation but a working framework. This paper consolidates it, showing how it unifies their diverse simulations (LT, GPS, chess programs) and provides a coherent explanation for human competence.
5.  **Articulation of "Selectivity of Search":** The paper crystallizes a key insight: human (and machine) problem-solving prowess comes not from brute-force calculation but from the intelligent, heuristic-guided search that cuts down an astronomical problem space to a manageable one. This became a foundational principle of early AI.

## Methodology
The argument is fundamentally **theoretical and polemical**, grounded in the analysis of a completed empirical and engineering program. Its methodology is one of **retrospective rational reconstruction**. Simon and Newell are not presenting new experimental data. Instead, they are:
*   **Meta-Analytical:** They survey their own body of work and the broader field, abstracting a coherent research strategy from what was, as they admit, a messier iterative process.
*   **Programmatic:** The paper is structured as a forward-looking plan, using past successes as justification for a continued and expanded agenda.
*   **Philosophical:** A significant portion is dedicated to epistemology and philosophy of science—defining what constitutes an explanation, defending the study of internal processes, and arguing against the "mystification" of the mind.
*   **Architectural:** The argument rests on the demonstrated validity of a specific architecture (the serial, information-processing, symbol-manipulating system). Their claim is that this architecture is sufficient and necessary for explaining human problem solving.

## Influence
The influence of this paper, and the research program it summarizes, is monumental and pervasive.
*   **Cognitive Science:** It helped define the core of cognitive science as the study of mental processes through computational modeling. It provided the canonical methodology for a generation of researchers.
*   **Artificial Intelligence:** It established the "good old-fashioned AI" (GOFAI) paradigm—based on symbolic representation, logic, and search—as the dominant approach for decades. The emphasis on heuristics and problem spaces directly shaped AI research.
*   **Human-Computer Interaction (HCI):** By modeling humans as information processors, it laid the conceptual groundwork for understanding users interacting with computers. The idea of "mental models" in HCI is a direct descendant.
*   **Education and Cognitive Psychology:** The paper influenced theories of expertise (as a collection of production rules and heuristics), learning, and instructional design, focusing on how knowledge is structured and retrieved.
*   **Citation and Lineage:** It is a cornerstone citation for anyone writing on the history of AI, cognitive psychology, or computational theories of mind. It directly enabled the entire field of cognitive architecture research (e.g., ACT-R, SOAR).

## Connections to Other Papers in the Collection
*   **Vannevar Bush (1945) - *As We May Think***: Bush envisions associative, memex-like aids for the mind. Simon and Newell provide a formal model of what the "thinking" they are augmenting might be. The memex is a tool for an information-processing brain.
*   **Doug Engelbart (1962) - *Augmenting Human Intellect***: Engelbart’s vision of augmenting human capabilities is the applied, engineering counterpart to Simon and Newell’s theoretical framework. "Augment" is the tool; Simon & Newell’s theory explains the "human intellect" being augmented.
*   **John Backus (1978) - *Programming Languages and Their Relation to Thought***: Backus argues that the structure of programming languages shapes how we conceptualize problems. Simon & Newell’s list-processing languages (IPL) were created precisely to model thought processes. They are the practical embodiment of Backus’s thesis.
*   **Seymour Papert (1980) - *Mindstorms***: Papert builds on Piagetian constructionism but uses the computational metaphor. Simon and Newell provide the underlying model of the "mind as computer" that Papert makes accessible to children via LOGO. Their theory is the "how" behind Papert’s educational "what."
*   **Steven Thurston (1994) - *On Proof and Progress in Mathematics***: Thurston describes mathematical thinking as a deeply visual, intuitive, and social process. Simon and Newell’s framework captures a formal, symbolic version of this. Thurston’s paper implicitly challenges the completeness of the Simon/Newell model for explaining mathematical insight, which often feels less like heuristic search and more like conceptual transformation.
*   **Richard Feynman (1974) - *Cargo Cult Science***: Feynman warns against the form of science without its rigor. Simon and Newell’s paper is a detailed blueprint for avoiding cargo cult science in psychology: don't just mimic the *form* of human behavior; discover and test the underlying *mechanism*. Their insistence on process-level explanation is the antidote to Feynman’s critique.

## Modern Relevance
The paper’s relevance remains profound, though its specific conclusions are debated.
*   **AI and the Symbolic vs. Sub-Symbolic Debate:** The paper is the high-water mark of the symbolic AI paradigm. Modern deep learning (sub-symbolic, statistical, pattern-matching) challenges its core tenets. However, the search for "explainable AI" (XAI) and neuro-symbolic AI is, in a sense, a return to Simon and Newell’s demand for process-level explanation and structured knowledge representation. Their work asks: what are the *symbols* being manipulated in a neural network?
*   **Knowledge Work and Productivity:** The framing of problem solving as search within a problem space using heuristics is directly applicable to analyzing and optimizing knowledge work. It suggests that expertise is not speed but better search strategies and better pruning of irrelevant possibilities.
*   **Cognitive Architectures and AI Assistants:** The blueprint for a cognitive architecture (sensory buffers, memory, central processor, heuristics) informs modern efforts to build more coherent, human-like AI agents and assistants, moving beyond monolithic large language models.
*   **The Limits of the Model:** The paper’s relevance is also defined by its limitations, which modern research explores. It underplays embodied cognition, emotion, social context, and the unconscious. Its focus on *problem solving* is narrower than the full scope of mind. Modern AI and cognitive science are filling in these gaps, often by departing from the strict symbolic framework.

## Key Quotes

1.  **"What questions should a theory of problem solving answer? First, it should predict the performance of a problem solver handling specified tasks. It should explain how human problem solving takes place: what processes are used, and what mechanisms perform these processes."**
    *   *Analysis:* This is the foundational methodological statement. It demands a science of *process*, not just behavior, establishing the gold standard for cognitive explanation.

2.  **"LT was, first and foremost, a demonstration of sufficiency. The program's ability to discover proofs for theorems in logic showed that, with no more capabilities than it possessed... a system could perform tasks that, in humans, require thinking."**
    *   *Analysis:* This clarifies the rhetorical role of early programs like Logic Theorist. They weren't claiming to be *models* of humans yet, but *proofs of concept* that the components of thought (symbol manipulation) could be mechanized.

3.  **"Selective search, not speed, was taken as the key organizing principle, and essentially no use was made of the computer's ultrarapid arithmetic capabilities in the simulation program."**
    *   *Analysis:* This is the core insight of their computational model of intelligence. It reframes smartness not as raw power but as clever heuristics—a principle still central to efficient algorithm design and AI.

4.  **"American behaviorism has been properly skeptical of 'mentalism'... Magic is explained only if the terms of explanation are less mysterious than the feats of magic themselves. It is no explanation of the rabbit's appearing from the hat to say that it 'materialized'."**
    *   *Analysis:* A brilliant rhetorical move. They co-opt behaviorism’s valid critique of vague mentalism and turn it into an argument for their own precise, mechanistic mentalism.

5.  **"An internal representation, or 'mental image,' of a chess board, for example, is not a metaphorical picture of the external object, but a symbol structure with definite properties on which well-defined processes can operate to retrieve specified kinds of information."**
    *   *Analysis:* This demystifies the "internal" and makes it tractable for science. It replaces vague notions of mental pictures with concrete data structures, bridging the gap between psychology and computer science.