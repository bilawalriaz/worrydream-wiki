---
title: Kay 2007 - Children Learning by Doing
created: 2026-06-10
updated: 2026-06-10
type: entity
tags: [computing-history, hci, programming-languages, mathematics]
sources: [raw/papers/Kay_2007_-_Children_Learning_by_Doing.txt]
confidence: high
---

# [[kay-2007-steps-2007-progress-report|Kay]] 2007 - Children Learning by Doing

## Core Thesis
This paper is a technical and philosophical manifesto for Squeak Etoys, a multimedia authoring environment, as deployed on the One Laptop Per Child (OLPC) XO computer. The core thesis is that **children learn [[allen-conn-2003-powerful-ideas-in-the-classroom|powerful ideas]] best by actively constructing and simulating [[cook-2000-how-complex-systems-fail|complex systems]] in a dynamic, object-oriented, multimedia environment.** [[kay-1968-flex-a-flexible-extendable-language|Kay]] argues that true "computer literacy" is not about using productivity software, but about the ability to *read and write dynamic simulations of ideas*, particularly systems of interacting entities. Etoys is presented not as a mere tool, but as a "virtual [[scientific-american-1966-information-june-1966|scientific]] laboratory" and "meta-medium" that unifies the exploratory, constructionist approaches of LOGO, HyperCard, StarLogo, and Smalltalk into a single, accessible environment. The nuances are critical: learning is "by doing" in a specific sense—the "doing" is the *authoring* of active media, where scripts are also mathematics, and where the boundary between playing, modeling, and creating dissolves.

## Historical Context
The paper emerges at the intersection of several decades of research. The immediate context is the OLPC project (circa 2007), Nicholas [[negroponte-1976-an-idiosyncratic-systems-approach-to-interactive-graphics|Negroponte]]'s initiative to provide rugged, low-cost laptops to children in developing nations. The challenge was software: what should a child *do* with this machine? [[kay-1968-flex-a-flexible-extendable-language|Kay]]'s answer rejects the prevailing desktop metaphor of applications and documents. Instead, he draws from a rich lineage:
1.  **LOGO ([[papert-2000-whats-the-big-idea-toward-a-pedagogy-of-idea-power|Papert]], 1960s-70s):** The foundational constructionist environment where children program a "turtle" to explore geometry. Etoys' scripting is a direct descendant, but generalized to any object with a "costume."
2.  **Smalltalk ([[kay-1968-flex-a-flexible-extendable-language|Kay]] et al., 1970s at Xerox [[parc-1971-parc-papers-for-pendery-and-planning-purposes|PARC]]):** The dynamic, object-oriented [[ingalls-1988-fabrik-a-visual-programming-environment|programming environment]] where everything is a live object. Etoys is built *on* Squeak (an open-source Smalltalk), making the entire system reflective and malleable.
3.  **HyperCard (Atkinson, 1987):** The "multimedia stack" that made authoring and linking graphical objects accessible to non-programmers. Etoys adopts its WYSIWYG, card/page-based authoring but adds scripting and simulation capabilities.
4.  **StarLogo (MIT, 1980s-90s):** An extension of LOGO for modeling massively parallel systems (like ant colonies). Etoys integrates this capacity, allowing scripts for one object to be replicated across thousands of instances.

The problem being solved was twofold: providing a software platform appropriate for the OLPC's educational mission, and[[papert-2000-whats-the-big-idea-toward-a-pedagogy-of-idea-power| more ]]fundamentally, advancing the decades-old dream (held by [[kay-1968-flex-a-flexible-extendable-language|Kay]], [[papert-1980-mindstorms|Papert]], and others) of using computers to fundamentally reshape how children think about complex ideas.

## Key Contributions
1.  **A Unified "Meta-Medium":** The paper's central technical contribution is presenting Etoys as a coherent synthesis of its predecessors. It is "Like LOGO" with costumes, "Like Starlogo" at all scales, "Like HyperCard" for media authoring, and "Like Smalltalk" underneath. This unification is not merely feature-listing but a [[clark-d-1988-the-design-philosophy-of-the-darpa-internet-protocols|design philosophy]] where each paradigm's strengths are leveraged in a single, fluid interface.
2.  **The "No Keyboard Input" Scripting Paradigm:** A crucial pedagogical innovation. Scripts are built visually by dragging-and-dropping tiles representing commands, properties, and tiles from object viewers. This removes the syntactic barrier of typing, allowing children to focus on *combinatorial logic* and *systemic behavior* rather than grammar.
3.  **Scalability of Ideas from One to Thousands:** The seamless transition from scripting a single object to running a simulation with 10,000 instances is a key technical and conceptual fea[[cook-2000-how-complex-systems-fail|t. It makes the]] emergent properties of complex systems (epidemics, gas laws, ecosystems) directly accessible to experiential learning.
4.  **The "Computer Literacy" Argument:** [[kay-1968-flex-a-flexible-extendable-language|Kay]] redefines computer literacy from *using* tools to *authoring* dynamic models. He posits that this skill—modeling systems of interacting entities—will be as transformative to human thought as the printing press and classical science. This elevates the software's purpose from education to epistemological change.

## Methodology
The paper's methodology is that of a **design manifesto and research program summary**. It is primarily **theoretical and argumentative**, grounded in a clear educational philosophy (constructionism) and a historical arc of [[nrc-1999-funding-a-revolution-government-support-for-computing-research|computing research]]. The argument is structured as:
1.  **Assertion:** Learning is best achieved by constructing active models.
2.  **Demonstration:** Etoys is presented as the optimal environment for this, with its capabilities demonstrated through a series of vignettes (the car, the epidemic, the aquarium).
3.  **Justification:** The design is justified by its lineage (LOGO, [[allen-conn-2003-powerful-ideas-in-the-classroom|etc.) and its ]]alignment with the goal of fostering "powerful ideas."
There is little empirical data presented (e.g., test scores, comparative studies); the evidence is logical, historical, and based on the authors' extensive prior experience. It is a polemic for a specific vision of child-computer interaction, arguing that the *form* of the software directly enables a deeper *mode* of learning.

## Influence
The influence of this work, and the broader Etoys/Squeak project, is significant but often indirect:
*   **Scratch ([[resnick-2013-the-somerville-steam-academy-innovation-plan|Resnick]] et al., 2007):** The most direct descendant. Developed at MIT Media Lab, Scratch adopted Etoys' tile-based, block-programming interface and constructionist ethos, but focused more on creative storytelling and games. Its massive global adoption made "block programming" the standard for youth coding education.
*   **Modern Block-Based Languages:** Tools like Blockly, Code.org's tools, and Google'sBlockly library all owe a debt to the interface paradigms pioneered in Smalltalk, refined in Etoys, and popularized by Scratch.
*   **Educational Technology Philosophy:** The paper reinforced the arguments for constructionism in education, influencing curriculum design in schools embracing "maker" cultures and project-based learning.
*   **Open Source & OLPC:** While the OLPC project itself had mixed success, Etoys' open-source nature and its presence on the XO inspired developers in many countries, contributing to a global community around educational software.
*   **[[kay-1968-flex-a-flexible-extendable-language|Kay]]'s Ongoing Work:** This paper is a checkpoint in [[kay-1968-flex-a-flexible-extendable-language|Kay]]'s lifelong quest (later continued in projects like Squeak and Croquet) to realize the computer as a "bicycle for the mind," evolving from a calculation device to a [[kay-1976-personal-dynamic-media-lrg|personal dynamic]] medium for modeling thought.

## Connections to Other Papers in the Collection
*   **[[papert-1980-mindstorms-1st-ed|Papert 1980]] (Mindstorms):** The foundational text for the constructionist philosophy that Etoys operationalizes. [[papert-1980-mindstorms|Papert]]'s "turtle geometry" becomes any object's trajectory; his vision of children as scientists is enabled by Etoys' simulation capacity.
*   **[[bush-1945-as-we-may-think-with-engelbart-notes|Bush 1945]] (As We May Think):** [[kay-1968-flex-a-flexible-extendable-language|Kay]]'s vision of a "meta-medium" where one can create, connect, and simulate ideas echoes [[vannevar-bush-symposium-1995-closing-panel|Bush]]'s memex, but with the crucial addition of *dynamic behavior*. Etoys is a memex where the trails are executable scripts.
*   **[[engelbart-1962-augmenting-human-intellect-typeset|Engelbart 1962]] ([[engelbart-1962-augmenting-human-intellect|Augmenting Human]] Intellect):** Both are focused on using computers to enhance human cognitive capabilities, but [[engelbart-2003-improving-our-ability-to-improve|Engelbart]]'s vision was largely for knowledge workers. [[kay-1968-flex-a-flexible-extendable-language|Kay]]'s paper radicalizes this by aiming for the cognitive development of children.
*   **[[backus-1978-can-programming-be-liberated-from-the-von-neumann-style|Backus 1978]] (FP):** [[kay-1968-flex-a-flexible-extendable-language|Kay]]'s dismissal of "textual syntax" in favor of visual, combinational tile-building is a direct response to the problems of conventional [[barton-1965-the-interrelation-between-programming-languages-and-machine-organization|programming languages]] that [[backus-1978-can-programming-be-liberated-from-the-von-neumann-style|Backus]] also critiqued, albeit from a purely functional perspective.
*   **[[hofstadter-2001-analogy-as-the-core-of-cognition|Hofstadter 2001]] (Analogy):** The Etoys environment is a powerful tool for creating analogical models. A child scripting an ant following a pheromone gradient is building a concrete, executable analogy for diffusion processes.
*   **[[lockhart-2002-mathematicians-lament|Lockhart 2002]] (Mathematician's Lament):** Both [[kay-1968-flex-a-flexible-extendable-language|Kay]] and [[lockhart-2002-mathematicians-lament|Lockhart]] lament the formalistic, symbolic-only teaching of mathematics. Etoys offers a path out, by allowing children to *experience* mathematical ideas (vectors, probability, systems dynamics) through construction and play.

## Modern Relevance
The paper's relevance has, in many ways, increased.
*   **AI and Simulation:** In the age of large language models and agent-based simulations, [[kay-1968-flex-a-flexible-extendable-language|Kay]]'s argument for "computer literacy" as *writ[[cook-2000-how-complex-systems-fail|ing dynamic sim]]ulations* is prescient. Understanding the emergent behavior of complex systems (from neural networks to climate models) is a critical modern skill, and Etoys-style modeling is a direct pedagogical approach to it.
*   **Education vs. EdTech:** The paper is a sharp critique of modern "EdTech," which often focuses on digitizing worksheets or delivering content. [[kay-1968-flex-a-flexible-extendable-language|Kay]]'s vision—software as a thinking environment—remains a high bar that most commercial educational software does not meet.
*   **Knowledge Management & Hypermedia:** Etoys' integration of authoring, scripting, and publishing prefigures modern interactive notebooks (like Jupyter) and low-code platforms, but with a stronger emphasis on *narrative* and *system modeling* than on data analysis.
*   **Open Source & Equity:** The commitment to free, open-source, multilingual software for global access is a model for equitable technology development, directly relevant to today's debates about digital divides and AI democratization.
*   **Design of Programming Environments:** The "no keyboard" tile-based interface is now ubiquitous in introductory coding, but [[kay-1968-flex-a-flexible-extendable-language|Kay]]'s deeper point—that the environment should make the *combinatorial* and *systemic* nature of programming obvious—is often lost in the imitation.

## Key Quotes

> "True 'computer literacy' (which involves being able to read and write dynamic simulations of ideas, especially in terms of systems of related entities, themselves also portrayed as systems) will eventually create an even larger change in how humans think about ideas than the printing press and classical mathematics and science."
*   **Analysis:** This is the paper's grand claim. [[kay-1968-flex-a-flexible-extendable-language|Kay]] elevates the skill of simulation modeling to a hist[[scientific-american-1966-information-june-1966|orical epi]]stemological shift, placing it above the [[scientific-american-1966-information-june-1966|scientific]] revolution itself. It frames the entire Etoys project not as teaching coding, but as teaching a new mode of thought.

> "People have to reach beyond their common sense into the 'uncommon sense' of models for disasters in order to help their imagination spur them to early action."
*   **Analysis:** This quote distills the practical, life-or-death relevance of the paper's work. It argues that intuitive, common-sense reasoning fails for slow-moving, complex crises (like AIDS), and that interactive simulation is the tool to cultivate the "uncommon sense" needed to visualize [[cook-2000-how-complex-systems-fail|and respond to ]]such systems.

> "The continuity of scripting between large and small allows children to explore very complex systems by just scripting the behavior of one item and making many copies."
*   **Analysis:** This describes the core technical-pedagogical breakthrough. The power comes from fractal consistency: the same logical blocks used for a single character can be scaled to model a gas or an ecosystem, making complexity approachable through pattern replication.

> "Should the comp[[papert-2000-whats-the-big-idea-toward-a-pedagogy-of-idea-power|uter p]]rogram the kid, or should the kid program the computer?"
*   **Analysis:** The paper opens with this foundational question from [[papert-1980-mindstorms|Papert]]. It sets up the entire work as an answer. Etoys is the definitive tool for "the kid programming the computer," positioning the child as the active author of their own [[egan-2003-some-cognitive-tools-of-literacy|cognitive tools]], not the passive recipient of pre-programmed experiences.

> "Etoys is... 'Like Squeak Smalltalk': In Fact, It Is."
*   **Analysis:** This seemingly simple statement is profound. It means every object in the child's world is a live, introspectable, and modifiable Smalltalk object. This provides a "ceiling" that grows with the user; a child's project is not a dead artifact but a foundation that a teenager can later open in the full Smalltalk environment, revealing the layers of abstraction beneath.