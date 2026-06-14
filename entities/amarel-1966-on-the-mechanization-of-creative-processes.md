---
title: Amarel 1966 - On the Mechanization of Creative Processes
created: 2026-06-10
updated: 2026-06-10
type: entity
tags: [computing-history, hci, programming-languages, mathematics]
sources: [raw/papers/Amarel_1966_-_On_the_Mechanization_of_Creative_Processes.txt]
confidence: high
---

# Amarel 1966 - On the Mechanization of Creative Processes

## Core Thesis
Saul Amarel argues that a specific, crucial component of creative problem-solving—the process of formulating an appropriate problem representation—can be understood in operational, information-processing terms and is a viable, though distant, target for mechanization. He contends that the "creative" act is not necessarily a mysterious, ineffable spark, but often manifests as the act of "casting the problem in the appropriate space." This is distinct from the search for a solution *within* a given space, which had dominated early AI. Amarel’s central nuance is a hierarchy of problem-solving: the highest-order creative act is meta-cognitive, involving the construction or selection of the representational framework (the "problem space" or "model") itself, within which all subsequent search and evaluation occur. He posits that the mechanisms for this are akin to those found in theory formation, suggesting a path toward mechanization.

## Historical Context
The paper emerged from the formative decade of Artificial Intelligence (1956-1966). The field's initial successes focused on the *control* problem—designing heuristic search algorithms for theorem proving (Newell & Simon's Logic Theorist), game playing (Samuel's checkers), and problem solving within predefined, fixed state spaces. Amarel acknowledges this progress but identifies its limitation: the human designer still bore the full burden of choosing the representation, evaluation metrics, and overall strategy. The machine's "intelligent behavior" was circumscribed by these static, human-imposed choices.

The problem Amarel addresses is the "bottleneck" this creates. To solve more complex, real-world problems—like forming scientific theories or engineering designs—AI needed to automate the higher-level creative work of figuring out *how* to think about the problem, not just how to search. This placed his work at the frontier of AI research, moving from solving puzzles to tackling open-ended, ill-defined problems. He references Polya's work on mathematical discovery and the emerging focus on "heuristic search," situating his proposal as a necessary evolution beyond these foundations.

## Key Contributions
1.  **Problem of Representation as the Core Creative Act:** Amarel reframes creativity in technical problem-solving as primarily being about "finding the most appropriate space." This isolates a tractable, operational component of creativity for study and potential mechanization, moving beyond vague notions of "synthesis" or "analogy."
2.  **Tripartite Framework for Problem Solving:** He clearly delineates three interconnected problems: (a) Representation (defining the state space), (b) Evaluation (defining progress measures), and (c) Control (search strategies). He argues that prior AI work over-emphasized (c) while (a) was the domain of human creativity.
3.  **Link to Theory Formation:** Amarel makes a profound connection: the process of building an appropriate problem model is structurally similar to the scientist's process of constructing an explanatory theory. Both involve synthesizing elements into a coherent structure that elegantly summarizes relationships. This suggests that research in "theory formation procedures" could be transferred to mechanize representation-building.
4.  **Critique of Static Human-Machine Roles:** He challenges the passive view of human creativity in "man-machine partnership." If the human is merely presented with a fixed, convenient model, the main creative work has already been done. True augmentation requires systems that support the dynamic evolution and modification of models during problem-solving.
5.  **Operational Definition as Research Program:** He proposes a methodological program: define creative processes operationally (via information-processing models), test these definitions against observations, and iteratively refine them. This frames the study of creativity as a science.

## Methodology
The paper is theoretical and polemical, structured as a visionary research proposal. Its methodology is not empirical but argumentative, drawing on:
*   **Analysis of Existing Problem-Solving Procedures:** Amarel uses his own work on propositional calculus theorem-proving as a case study, demonstrating how a "spectacular improvement" occurred upon shifting the problem representation (from logical formulas to directed graph closures).
*   **Taxonomy and Synthesis:** He taxonomizes the components of problem solving (representation, evaluation, control) and synthesizes ideas from cognitive psychology, mathematical heuristics (Polya), and early AI to construct his thesis.
*   **Extrapolation by Analogy:** His core method is analogical reasoning: the process of model-formation in problem solving is *like* theory formation in science. Therefore, insights from the latter can inform the former.

The tone is deliberately exploratory ("tentative ideas"), presenting a framework for future investigation rather than reporting completed results.

## Influence
Amarel's paper was prescient and influential in shaping the trajectory of AI and cognitive science.
*   **Direct Influence on Automated Reasoning:** The emphasis on representation and theory formation directly influenced later work in automated theorem proving and non-monotonic reasoning, where finding the right logical formulation is key.
*   **Foundation for Meta-Level Reasoning and Planning:** The idea of operating on representations (rather than just searching through them) is a cornerstone of modern AI planning systems and meta-reasoning architectures.
*   **Interactive Problem-Solving and Design:** His vision for flexible, model-building languages in man-machine partnership foreshadowed research in intelligent CAD systems and interactive theorem provers.
*   **Cognitive Science:** The paper contributed to the "computational theory of mind" perspective, modeling high-level cognitive functions like creativity as manipulable information processes. It influenced how psychologists and AI researchers thought about expertise and insight.

The paper is cited in histories of AI (e.g., Crevier's *AI: The Tumultuous Search for Artificial Intelligence*) as an early, clear articulation of the representation problem and its centrality to higher-level cognition.

## Connections to Other Papers in the Collection
*   **[[bush-1931-the-differential-analyzer|Bush]] 1945 (As We May Think):** Bush's Memex is a tool for associative indexing—a fixed, powerful *representation* for personal knowledge. Amarel's paper asks the deeper question: how does one *create* such a representation dynamically for a novel problem? The Memex supports the use of models; Amarel seeks to mechanize their creation.
*   **[[engelbart-1960-games-that-teach-the-fundamentals-of-computer-operation|Engelbart]] 1962 (Augmenting Human Intellect):** Both papers are deeply concerned with augmenting human problem-solving. Engelbart's framework focuses on the hierarchy of capabilities and tools. Amarel provides a specific, critical capability that must be augmented: the mechanization of representation-building. His argument implies that Engelbart's "system" must include powerful, dynamic model-building tools.
*   **Kay 1972 (Personal Computer):** Kay's vision of the computer as a "metamedium" for modeling ideas aligns with Amarel's need for flexible model-building languages. Kay's Dynabook is the potential platform for the kind of dynamic, interactive model evolution Amarel describes as the essence of creative partnership.
*   **[[backus-1978-can-programming-be-liberated-from-the-von-neumann-style|Backus]] 1978 (FP):** [[backus-1978-can-programming-be-liberated-from-the-von-neumann-style|Backus]] criticizes the von Neumann bottleneck and advocates for a higher-level, functional style of programming. This is, in a sense, a proposal for a more "appropriate" representation for certain kinds of computation, echoing Amarel's core insight that changing representation transforms problem difficulty.
*   **[[thurston-1990-mathematical-education|Thurston]] 1994 (Proof and Progress):** [[thurston-1990-mathematical-education|Thurston]] describes the creative, communicative, and often non-linear process of mathematical understanding. Amarel seeks the operational principles underlying such processes, specifically the part where a mathematician "finds the right framework" for a proof, which is the creative act Thurston describes from the inside.
*   **[[hofstadter-2001-analogy-as-core-of-cognition|Hofstadter]] 2001 (Analogy):** [[hofstadter-2001-analogy-as-core-of-cognition|Hofstadter]] argues that analogy is the core of creativity and perception. Amarel's "formation of an appropriate problem space" can be seen as a large-scale analogy-finding process: mapping the new problem onto an existing, well-understood structural model (like mapping a theorem to a graph).

## Modern Relevance
Amarel's ideas are startlingly relevant to contemporary challenges in AI and knowledge work.
1.  **The "Prompt Engineering" Parallel:** The current focus on crafting effective prompts for Large Language Models (LLMs) is a modern, crude form of "representation engineering." The user must creatively formulate the problem in a way the AI's fixed representation can process effectively. Amarel's vision is of a system that automates this formulation step.
2.  **Foundation Models and Representation Learning:** Modern deep learning, particularly foundation models, can be seen as systems that *learn* powerful, implicit representations of data. This is a form of the "theory formation" Amarel described, albeit statistical rather than symbolic. The quest for better architectures (Transformers, etc.) is a quest for better, more general "spaces" for reasoning.
3.  **AI for Science and Design:** AlphaFold (protein structure prediction) and AI for materials discovery exemplify Amarel's original examples. Their success comes from learning powerful representations of biological or physical systems that make the problem tractable. They mechanize the "creative" step of finding the right abstract features to model.
4.  **Human-AI Collaboration Tools:** The design of tools like Copilot or advanced CAD software embodies the debate Amarel frames. Is the AI a search engine within a fixed representation (autocomplete), or a partner in evolving the model (suggesting entirely new architectural forms)? Amarel argues the latter is the true creative augmentation.
5.  **The Meta-Learning Problem:** Amarel's tripartite framework reappears in modern meta-learning ("learning to learn"), where the goal is to create systems that can automatically adjust their own representation and optimization strategies for new tasks.

## Key Quotes
1.  **"I would like to suggest that the formation of an appropriate concept of problem space... is a creative process."**
    *   *This is the core thesis crystallized. It operationalizes creativity as a specific, identifiable cognitive/computational act: the act of defining the problem's world.*
2.  **"The relatively intelligent behavior of the machine... is therefore circumscribed by the choices of representation, evaluation and control that are made by the designer."**
    *   *A critical indictment of early AI's limitations. It points out that the human designer, not the machine, is performing the highest-level creative work.*
3.  **"The most spectacular improvement was obtained when the problem representation was changed in an 'appropriate' way... the shift in representation has transformed the problem to one of finding appropriate closures to certain directed graphs."**
    *   *A concrete case study proving the thesis. The act of re-representation was the creative leap that unlocked a solution path.*
4.  **"If we exclude the belief in such unexplainable processes, then it is reasonable to attempt explications of (at least some) creative processes in terms of information-processing models."**
    *   *A methodological declaration. It positions the paper within the computational theory of mind and sets the agenda for a scientific study of creativity.*
5.  **"In the present state of the artificial intelligence art, the designer of a problem-solving procedure is required to solve without aid from the machine the problems of choosing a state space, a basis for evaluation, and a strategy for heuristic search."**
    *   *Clearly states the problem his research aims to solve: to push the boundary of what machines can do, automating the meta-level decisions previously reserved for humans.*
6.  **"The objective is to construct efficiently an information structure... that would summarize 'elegantly' and 'explain' a set (usually large) of empirically obtained relationships... In the model-formation problem of the problem solver the objective is to construct a theory... that expresses... the properties of the problem state space."**
    *   *The crucial analogical link. By equating model-building with theory-building, he opens up a research pathway (theory formation) to tackle his target problem (creative representation).*