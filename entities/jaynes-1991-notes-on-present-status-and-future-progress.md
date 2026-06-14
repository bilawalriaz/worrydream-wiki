---
title: Jaynes 1991 - Notes on Present Status and Future Progress
created: 2026-06-10
updated: 2026-06-10
type: entity
tags: [probability-theory, statistical-mechanics, philosophy-of-science, ai-history, scientific-method]
sources: [raw/papers/Jaynes_1991_-_Notes_on_Present_Status_and_Future_Progress.txt]
confidence: high
---

# [[jaynes-1984-the-evolution-of-carnots-principle|Jaynes]] 1991 - Notes on Present Status and Future Progress

## Core Thesis
The paper argues that the Maximum Entropy (MaxEnt) method, properly understood as a principle of inference from incomplete information, represents a fundamental and universal logic of science. [[jaynes-1984-the-evolution-of-carnots-principle|Jaynes]] contends it resolves long-standing philosophical debates (like the role of ergodicity in statistical mechanics) by shifting the goal of science from *deduction* from microscopic laws to *inference* under uncertainty. The MaxEnt distribution is not a description of a physical system's objective state, but rather the uniquely honest representation of the state of knowledge of an observer. This epistemological shift, he argues, is both simpler and more powerful than the traditional justifications, and its successful application across diverse fields proves the universality of the reasoning.

## Historical Context
The paper emerges from decades of [[jaynes-1984-the-evolution-of-carnots-principle|Jaynes]]'s work promoting Bayesian probability and MaxEnt as the foundation for [[scientific-american-1966-information-june-1966|scientific]] inference. The context is a field in transition:
*   **Pre-[[jaynes-1984-the-evolution-of-carnots-principle|Jaynes]] Viewpoint:** Statistical mechanics relied on concepts like ergodicity (the system exploring its entire phase space) to justify using microcanonical or canonical ensembles. This was a *deductive* attempt to derive thermodynamics from mechanics. The debate was often circular and inconclusive.
*   **The Jaynesian Revolution:** Beginning with his seminal 1957 paper, [[jaynes-1984-the-evolution-of-carnots-principle|Jaynes]] re-framed statistical mechanics as a problem of inference. Given macroscopic constraints (energy, volume), which probability distribution over microstates represents our state of knowledge? The answer is the one with maximum entropy, as it is the least biased by anything not known.
*   **State of the Field in 1991:** The "MaxEnt movement" was maturing. Initial resistance was giving way to widespread, if often unacknowledged, adoption. Applications had expanded far beyond physics into geophysics, economics, medicine, and machine learning (via [[jaynes-1984-the-evolution-of-carnots-principle|Jaynes]]'s student, the geophysicist [[gull-1993-imaginary-numbers-are-not-real|Gull]]). [[jaynes-1984-the-evolution-of-carnots-principle|Jaynes]] is reflecting on its establishment and diagnosing the sociological patterns of its acceptance.

## Key Contributions
1.  **The Epistemological Reframing:** The paper's core contribution is the crystallization of MaxEnt as a *logic of reasoning*, not a physical principle. It explicitly reverses the direction of justification: entropy maximization justifies the use of an ensemble, not vice-versa.
2.  **Resolution of the Ergodicity Debate:** [[jaynes-1984-the-evolution-of-carnots-principle|Jaynes]] demonstrates that the question of ergodicity becomes irrelevant to the practice of statistical mechanics once it is seen as an inference problem. The MaxEnt distribution is the "best prediction" regardless. This liberated the fi[[scientific-american-1966-information-june-1966|eld from a]] theoretical quagmire.
3.  **A Theory of [[scientific-american-1966-information-june-1966|Scientific]] Progress:** He outlines a model for how new ideas gain acceptance (citing Helmholtz, Planck, Freud), placing MaxEnt in "Phase III" of acceptance—where it is u[[scientific-american-1966-information-june-1966|sed widely]] but its name and philosophical basis are often stripped away. This is a meta-commentary on [[scientific-american-1966-information-june-1966|scientific]] sociology.
4.  **Diagnosis of the Mind-Projection Fallacy:** Through the example of machine translation, [[jaynes-1984-the-evolution-of-carnots-principle|Jaynes]] diagnoses a core error: confusing a state of knowledge about an object with a property of the object itself. He argues this fallacy crippled early attempts at translation.
5.  **A Universal Heuristic:** The paper explicitly states the MaxEnt principle as a universal tool for problem-solving in any field where inferences must be drawn from incomplete data.

## Methodology
The argument is primarily **polemical and theoretical**, structured as a reflective status report. [[jaynes-1984-the-evolution-of-carnots-principle|Jaynes]] uses:
*   **Historical Narration:** To contrast the old and new viewpoints.
*   **Philosophical Argument:** To defend the epistemological stance against claims of "subjectivity."
*   **Sociological Analysis:** To explain resistance and eventual adoption.
*   **Case Studies:** To illustrate the practical and conceptual points (machine translation, parameter estimation).
*   **Rhetorical Appeals to Authority:** Quoting great scientists (Von Neumann, Gibbs, Jeffreys) to show his ideas have deep precedent, and Helmholtz/Planck/Freud to frame the pattern of resistance.
The structure moves from big-picture philosophy to specific applications and back, defending the method's robustness.

## Influence
[[jaynes-1984-the-evolution-of-carnots-principle|Jaynes]]'s work, especially as distilled in this paper, had a profound and delayed influence:
*   **Legitimized Bayesian Inference in Science:** He provided the rigorous, intuitive justification that allowed Bayesian methods to gain a foothold in mainstream science, from astrophysics to genetics.
*   **Founded Modern MaxEnt Applications:** The applications he alludes to (image reconstruction, spectral analysis, geophysical inversion, financial modeling) exploded in the 1990s and 2000s, forming a key toolkit in data science.
*   **Prefigured Modern AI & Machine Learning:** The core idea—that learning is inference from data under uncertainty, and that models should encode prior knowledge through constraints—is foundational to Bayesian neural networks and probabilistic graphical models. The "Universal Intermediate Language" for translation is a prescient, if simplistic, version of intermediate representations in modern multilingual NLP.
*   **Influenced Philosophy of Science:** His clear distinction between deduction and inference became a touchstone in debates about the role of probability in science.
*   **Cited as a Classic:** This paper and [[jaynes-1984-the-evolution-of-carnots-principle|Jaynes]]'s 1957 work are routinely cited in introductions to Bayesian methods, information theory, and the history of statistical mechanics.

## Connections to Other Papers in the Collection
*   **[[feynman-1974-cargo-cult-science|Feynman 1974]] (Cargo [[feynman-1974-cargo-cult-science|Cult Science]]):** [[jaynes-1984-the-evolution-of-carnots-principle|Jaynes]]'s discussion of the "lunatic [[scientific-american-1966-information-june-1966|fringe" an]]d "Establishment" opposing new ideas is a direct counterpart to [[feynman-1974-cargo-cult-science|Feynman]]'s warning against pseudo-science. Both are concerned with integrity in [[scientific-american-1966-information-june-1966|scientific]] practice. [[jaynes-1984-the-evolution-of-carnots-principle|Jaynes]] provides the *[[scientific-american-1966-information-june-1966|positive* ]]methodology (MaxEnt) that [[feynman-1974-cargo-cult-science|Feynman]] calls for.
*   **[[thurston-1994-on-proof-and-progress-in-mathematics|Thurston 1994]] (Proof and Progress):** Both papers explore the sociology of mathematical/[[scientific-american-1966-information-june-1966|scientific]] progress. [[thurston-1994-on-proof-and-progress-in-mathematics|Thurston]] focuses on communication and understanding in mathematics; [[jaynes-1984-the-evolution-of-carnots-principle|Jaynes]] on acceptance of a new inferential framework. Both describe how new methods become "de facto" tools.
*   **[[anderson-1972-more-is-different|Anderson 1972]] (More is Different):** [[jaynes-1984-the-evolution-of-carnots-principle|Jaynes]]'s work is a direct application of [[anderson-1972-more-is-different|Anderson]]'s principle to statistical mechanics. "More is Different" justifies using coarse-grained, statistical descriptions (like MaxEnt) because the emergent macroscopic level has its own valid laws, independent of the microscopic details. [[jaynes-1984-the-evolution-of-carnots-principle|Jaynes]] provides the *inference framework* for doing this correctly.
*   **[[lockhart-2002-mathematicians-lament|Lockhart 2002]] (Mathematician's Lament):** [[lockhart-2002-mathematicians-lament|Lockhart]] decries the ritualistic, de-contextualized teaching of math. [[jaynes-1984-the-evolution-of-carnots-principle|Jaynes]]'s paper is a passionate argument for re-contextualizing probability theory not as a set of tools, but as a coherent *logic of reasoning*. Both advocate for deeper, meaningful understanding over mere procedure.
*   **[[bush-1945-as-we-may-think-with-engelbart-notes|Bush 1945]] (As We May Think):** [[jaynes-1984-the-evolution-of-carnots-principle|Jaynes]]'s concept of a "Universal Intermediate Language" for translation echoes [[vannevar-bush-symposium-1995-closing-panel|Bush]]'s vision of associative, non-linear information retrieval and manipulation. Both seek to overcome the limitations of sequential, [[nelson-g-2006-natural-language-semantic-analysis-and-interactive-fiction|natural language]] by creating better symbolic representations.

## Modern Relevance
*   **AI and Large Language Models (LLMs):** [[jaynes-1984-the-evolution-of-carnots-principle|Jaynes]]'s Mind-Projection Fallacy is directly relevant to modern debates about AI "understanding" and bias. An LLM's parameters represent a MaxEnt-like distribution over probable text continuations, given its training constraints. It is a model of human knowledge/inference, not a conscious agent. Confusing the two is the Fallacy.
*   **Data Science and Bayesian Inference:** MaxEnt is now a core technique in machine learning (e.g., for estimating feature distributions in CRF models, or in the principle of maximum entropy for policy optimization in RL). The philosophy underpins the entire Bayesian machine learning movement.
*  [[scientific-american-1966-information-june-1966| **Informa]]tion Theory and Compression:** MaxEnt distributions are the least biased (highest entropy) and thus represent the worst-case optimal data compression scheme. This links directly to [[shannon-1956-the-bandwagon|Shannon]]'s work and modern efficient coding.
*   **The Nature of [[scientific-american-1966-information-june-1966|Scientific]] Knowledge:** In an era of "big data," [[jaynes-1984-the-evolution-of-carnots-principle|Jaynes]]'s core message is more critical than ever. More data does not eliminate uncertainty; it merely provides more constraints for our inferential models. The *interpretation* of data remains an epistemological act of inference, not a discovery of objective truth. His paper is a manual for clear thinking in the age of AI.

## Key Quotes
1.  **"It agrees with everything that is known, but carefully avoids assuming anything that is not known."**  
    *The definitive statement of the MaxEnt principle as a tool for honest reasoning.*
2.  **"When the goal of Statistical Mechanics was seen as predicting the laws of thermodynamics by deductive reasoning... Now we see the goal as inference from incomplete information rather than deduction."**  
    *Captures the fundamental epistemological shift [[jaynes-1984-the-evolution-of-carnots-principle|Jaynes]] ch[[scientific-american-1966-information-june-1966|ampioned.*]]
3.  **"Failure of the predictions would give us cogent evidence for non-ergodicity and a clue as to which subspace of the full phase space Nature is using... we look eagerly for such failures, because they would tell us new things about the underlying dynamics."**  
    *A radical reframing of [[scientific-american-1966-information-june-1966|scientific]] "failure" as a source of new knowledge.*
4.  **"One can argue with a philosophy or even a theorem; it is not so easy to argue with a computer printout, which displays the facts of actual performance, independently of all philosophy and all theorems."**  
    *A pragmatic defense of computational results as the ultimate arbiter in science.*
5.  **"They are parasites feeding on the new idea; while giving the appearance of opposing it, in fact they are deriving their sole sustenance from it, since they have no other agenda."**  
    *A sharp, memorable diagnosis of a specific type of opposition to new ideas.*
6.  **"The MaxEnt distribution is always the correct answer to a definite, well-posed question: 'What probability distribution has maximum entropy subject to the basic measure chosen and the constraints imposed?'... Nothing in MaxEnt... can do more than answer the question that the user asked."**  
    *Defends MaxEnt against naive critiques, emphasizing the importance of problem formulation.*
7.  **"Von Neumann could not overcome that mental block [of the Mind-Projection Fallacy]. Of course, entropy was a relevant tool for dealing with their problem; but it was not the entropy of an imaginary 'statistical distribution' of French thought... It was the average entropy of the MaxEnt distribution of possible English equivalents."**  
    *The perfect example of the central fallacy, using a story about AI/NLP predecessors.*