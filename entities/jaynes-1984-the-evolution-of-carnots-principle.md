---
title: Jaynes 1984 - The Evolution of Carnot's Principle
created: 2026-06-10
updated: 2026-06-10
type: entity
tags: [thermodynamics, philosophy-of-science, information-theory, maximum-entropy, inference]
sources: [raw/papers/Jaynes_1984_-_The_Evolution_of_Carnot's_Principle.txt]
confidence: high
---

# [[jaynes-1988-clearing-up-mysteries|Jaynes]] 1984 - The Evolution of Carnot's Principle

## Core Thesis
[[jaynes-1988-clearing-up-mysteries|Jaynes]] argues that Carnot's principle—the theoretical limit on the efficiency of heat engines—underwent a series of logical transformations over a century, ultimately shedding its identity as a "law of physics" and becoming a general "principle of reasoning" for making inferences from incomplete data. The core nuance is that this transformation was not a change in content but a clarification of its true nature. [[jaynes-1988-clearing-up-mysteries|Jaynes]] posits that the mathematical procedure embodied in Gibbs's 19th-century thermodynamics for predicting chemical equilibrium states is **identical** in rationale and method to the 20th-century "maximum entropy" inference used in disparate fields. The paper's argument is that what we now call the maximum entropy method is not a new invention but the late recognition of the generality inherent in a procedure that was always there, rooted in Carnot's insight about resolving ambiguity in a way that avoids assuming "something for nothing."

## Historical Context
The paper sits at a fascinating intersection. It was written in 1984, at a time when "maximum entropy" methods were generating both excitement and skepticism in fields like X-ray crystallography and statistical mechanics (as indicated by the conference it opened). [[jaynes-1988-clearing-up-mysteries|Jaynes]] addresses the common disbelief that a tool from thermodynamics could be so universally applicable.

The historical context he traces is the evolution of thermodynamics itself:
1. **Carnot (1824):** Working in a pre-energy-conservation era, he used a *reductio ad absurdum* argument (the impossibility of a perpetual motion machine of the second kind) to derive a powerful, qualitative principle: no engine can be more efficient than a reversible one. This resolved a mass of engineering ambiguities but did not yield quantitative predictions.
2. **Kelvin & Joule (1850s):** Integration of Joule's quantitative mechanical equivalent of heat allowed Kelvin to derive the functional form of reversible efficiency, leading to the definition of an absolute (Kelvin) temperature scale. This was the first "metamorphosis": from a qualitative principle to a quantitative, calibration-defining tool.
3. **Clausius (1850s-60s):** Formulated the Second Law as a differential inequality (`dS ≥ dQ/T`) and introduced the concept of entropy as a state function. This was a second metamorphosis: from an operational principle about engines to a statement about the direction of natural processes, though still seen as a law of physics.
4. **Gibbs (1870s):** The crucial third metamorphosis. Gibbs derived the conditions for chemical equilibrium by maximizing the entropy function subject to constraints (conservation of mass, energy). [[jaynes-1988-clearing-up-mysteries|Jaynes]] stresses that Gibbs recognized the logic was probabilistic, not deterministic ("the impossibility of an uncompensated decrease seems reduced to improbability"). The Second Law became a criterion for quantitative prediction in the face of incomplete data.
5. **Boltzmann (1870s-1900s):** Provided the statistical-mechanical foundation (`S = k log W`), explaining entropy in terms of microstates. [[jaynes-1988-clearing-up-mysteries|Jaynes]] sees this as a fourth, microscopic metamorphosis, but not the source of the general inference method.

The problem being solved evolved from "How do we build a better steam engine?" to "Given macroscopic constraints on a complex system, what is the most likely macroscopic state?"

## Key Contributions
1. **Historical Reframing:** [[jaynes-1988-clearing-up-mysteries|Jaynes]] reinterprets the history of thermodynamics not as the discovery of physical laws, but as the gradual, often unwitting, development of a general method for inference under uncertainty.
2. **Identification of Gibbs as the Proto-Bayesian:** He explicitly identifies Gibbs's equilibrium calculations as the direct antecedent of maximum entropy inference, stating, "the logic and the procedure of our present maximum entropy applications are easily recognized in the methods for predicting equilibrium conditions introduced by Gibbs."
3. **Unification Through "Metamorphosis":** He structures the history around four conceptual shifts ("metamorphoses"), showing how each thinker built upon the last while changing the principle's philosophical interpretation, not its core mathematical utility.
4. **Clarification of "Extracting Information":** He directly addresses the skepticism that maxent "gets something for nothing," explaining that it combines the information in the data with the additional, objective information encoded in the entropy function (representing our state of ignorance).

## Methodology
[[jaynes-1988-clearing-up-mysteries|Jaynes]] employs a **historical-conceptual analysis** with a **polemical** edge. The argument is structured as a retrospective, "hindsight" lecture. He methodically walks through the derivations of each stage (Kelvin's functional equation, Clausius's inequality, Gibbs's maximization) to demonstrate their logical kinship. The key methodological move is to show that even when Carnot's principle was considered a fundamental "law," it was *used* in practice only to resolve ambiguities and define consistent measures (like temperature). The paper is **theoretical** throughout, relying on textual analysis of key works and reconstruction of their logical implications. It is also **pedagogical**, aiming to demystify maxent for a skeptical audience.

## Influence
This paper is a cornerstone in the philosophical justification of Bayesian and maximum entropy methods. Its influence is seen in:
- **Information Theory & Statistics:** It provided a powerful historical narrative linking Gibbs's statistical mechanics to [[jaynes-1988-clearing-up-mysteries|Jaynes]]'s own "Probability Theory: The Logic of Science" (1996), where the maximum entropy principle is presented as an extension of logical inference.
- **[[cook-2000-how-complex-systems-fail|Complex Systems]] & Machine Learning:** It bolstered the theoretical foundation for using entropy-based principles (like in variational autoencoders or regularization techniques) as tools for principled inference from incomplete data, not just as [[seeman-1988-physical-models-for-exploring-dna-topology|physical models]].
- **Philosophy of Science:** It contributed to the debate about the interpretation of probability (as logical vs. frequentist) and the nature of [[scientific-american-1966-information-june-1966|scientific]] laws. The idea that a "law" can evolve into [[scientific-american-1966-information-june-1966|a "princip]][[le-goc-2016-zooids-building-blocks-for-swarm-user-interfaces|le]] of inference" is a sophisticated meta-[[scientific-american-1966-information-june-1966|scientific]] insight.
Who cited it: It is widely referenced in works by E.T. himself, and by authors in statistical physics (e.g., [[jaynes-1988-clearing-up-mysteries|Jaynes]], Haken), information theory (e.g., Shore & [[johnson-1989-the-xerox-star-a-retrospective|Johnson]]), and the philosophy of science (e.g., Seidenfeld, Howson & Urbach).

## Connections to Other Papers in the Collection
- **[[feynman-1974-cargo-cult-science|Feynman 1974]] (Cargo [[feynman-1974-cargo-cult-science|Cult Science]]):** [[jaynes-1988-clearing-up-mysteries|Jaynes]]'s pa[[feynman-1974-cargo-cult-science|per is a pro]]found antidote to [[feynman-1974-cargo-cult-science|cargo cult]] science. He is arguing for a deep, logical understanding of a methodology, not just its superficial rituals. He wants maxent users to understand *why* it works, tracing its lineage to first principles.
- **[[hofstadter-2001-analogy-as-the-core-of-cognition|Hofstadter 2001]] (Analogy, Melody, Isomorphism):** [[jaynes-1988-clearing-up-mysteries|Jaynes]]'s entire argument is an exercise in recognizing a deep analogy—and indeed an *isomorphism*—between the mathematical structure of Gibbs's thermodynamics and general inference. He is identifying a "deep analogy" between two seemingly disconnected fields.
- **[[lockhart-2002-mathematicians-lament|Lockhart 2002]] (A Mathematician's Lament):** [[lockhart-2002-a-mathematicians-lament|Lockhart]] laments the divorce of mathematical formalism from its meaning and soul. [[jaynes-1988-clearing-up-mysteries|Jaynes]] is performing the exact opposite: he is resurrecting the "soul" and original motivating questions (e.g., "what *will* most likely happen?") behind the cold formalism of entropy maximization.
- **[[anderson-1972-more-is-different|Anderson 1972]] (More is Different):** While [[anderson-1972-more-is-different|Anderson]] emphasizes emergent complexity, [[jaynes-1988-clearing-up-mysteries|Jaynes]] emphasizes a unifying logical principle that cuts across different levels of description (from engine efficiency to chemical equilibrium to general inference). Both, however, are concerned with the relationship between microscopic rules and macroscopic understanding.
- **[[backus-1978-can-programming-be-liberated-from-the-von-neumann-style|Backus 1978]] (FP):** [[backus-1978-can-programming-be-liberated-from-the-von-neumann-style|Backus]] argues for a shift from imperative to [[hughes-1990-why-functional-programming-matters|functional programming]] to manage complexity. [[jaynes-1988-clearing-up-mysteries|Jaynes]] narrates a similar conceptual shift in science: from a "law-based" (imperative-like) view of the Second Law to an "inference-based" (functional-like) principle for calculating outcomes from constraints.

## Modern Relevance
[[jaynes-1988-clearing-up-mysteries|Jaynes]]'s analysis is startlingly relevant to contemporary AI, data science, and epistemology:
1. **AI and Machine Learning:** The maximum entropy principle is the theoretical foundation for logistic regression and many probabilistic graphical models. Understanding its lineage as a method for *inference from incomplete data*—not just a physical law—is crucial for data scientists. [[jaynes-1988-clearing-up-mysteries|Jaynes]] provides the philosophical warrant for why maxent is a principled, not arbitrary, choice for creating the least-biased model given constraints.
2. **Information Retrieval & Search:** Search engines use Bayesian inference and language models that are, at their core, about making predictions under uncertainty. [[jaynes-1988-clearing-up-mysteries|Jaynes]]'s framework helps explain why these methods "work" so well for extracting meaning from sparse, incomplete signals (queries).
3. **Knowledge Management & Sensemaking:** The paper addresses the fundamental human cognitive challenge: how to reason rigorously with incomplete information. [[jaynes-1988-clearing-up-mysteries|Jaynes]] shows this isn't a new problem; our most successful physical theories are, at heart, tools for this exact task.
4. **Education:** It presents a model for teaching science not as a sequence of arbitrary laws, but as a developing toolkit for solving problems and resolving ambiguities. It connects the *what* (entropy) to the *why* (predicting outcomes from limited data).

## Key Quotes
1.  **"The impossibility of an uncompensated decrease seems reduced to improbability." ([[jaynes-1988-clearing-up-mysteries|Jaynes]] quoting Gibbs)**
    *Analysis: This single quote captures the pivotal metamorphosis. It shows Gibbs reframing a physical prohibition as a statement about likelihood, making the logical gap explicit and opening the door to quantitative inference.*

2.  **"Since Gibbs' Heterogeneous Equilibrium the second law has been used in practice, not as a 'law of physics', but as a principle of human inference; a criterion for resolving the ambiguities of incomplete data."**
    *Analysis: This is the paper's core thesis distilled. It marks the precise moment [[jaynes-1988-clearing-up-mysteries|Jaynes]] claims the shift occurred—from a statement about the world to a rule for our reasoning about the world.*

3.  **"Carnot's principle... is outstandingly beautiful, because it deduces so much from so little... In this respect, I think that Carnot's principle ranks with Einstein's principle of relativity."**
    *Analysis: [[jaynes-1988-clearing-up-mysteries|Jaynes]] is not just a his[[scientific-american-1966-information-june-1966|torian but]] an advocate. This high praise elevates Carnot's logical methodology to the highest tier of [[scientific-american-1966-information-june-1966|scientific]] thought, framing it as an archetype of powerful, abstract reasoning.*

4.  **"Gibbs deprived the second law of that logical certainty, [but] extended its practical application to serve the stronger purpose of quantitative prediction."**
    *Analysis: This highlights the trade-off at the he[[scientific-american-1966-information-june-1966|art of the]] metamorphosis. We lose absolute deterministic certainty but gain a vastly more powerful and general predictive tool. This is a mature view of [[scientific-american-1966-information-june-1966|scientific]] progress.*

5.  **"The method expresses, and has evolved from, an explicit statement of the opposite [of 'something for nothing']; that you cannot get something for nothing."**
    *Analysis: This is [[jaynes-1988-clearing-up-mysteries|Jaynes]]'s direct rebuttal to critics. He grounds maxent not in magic, but in a fundamental accounting principle—the conservation of information/energy. The constraints represent what we *know*; the entropy maximization represents the state of knowledge that assumes nothing more.*

6.  **"We are beginning to understand them [Laplace and Carnot]. And we hope that the disappointment of some at the simplicity of the maximum entropy principle, will be partially relieved on finding that it actually does work."**
    *Analysis: This closing remark connects the high-minded historical narrative to the immediate pedagogical goal. The "ultrfine machinery" is missing, but like [[maxwell-2006-tracing-the-dynabook|Maxwell]]'s telephone, its elegant simplicity is validated by its efficacy.*

7.  **"Carnot solved the problem only implicitly... [he] did not find the explicit formula for the reversible efficiency."**
    *Analysis: This shows [[jaynes-1988-clearing-up-mysteries|Jaynes]]'s respect for the logical power of a principle over its immediate computational utility. The value of Carnot's thought was in defining the structure of the problem, a role analogous to establishing a correct programming paradigm before writing the code.*