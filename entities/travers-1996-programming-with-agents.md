---
title: Travers 1996 - Programming with Agents
created: 2026-06-10
updated: 2026-06-10
type: entity
tags: [computing-history, hci, programming-languages, mathematics]
sources: [raw/papers/Travers_1996_-_Programming_with_Agents.txt]
confidence: high
---

# Travers 1996 - Programming with Agents

## Core Thesis
Travers's dissertation argues that the dominant metaphors of traditional programming languages (imperative, functional, procedural, object-oriented, constraint-based) are poorly suited for creating and reasoning about systems composed of multiple, responsive, autonomous entities. He proposes a fundamental metaphorical shift: programming with "agents." An agent is not merely an object but a simple mechanism understood through anthropomorphic metaphors, endowed with properties like autonomy, purposefulness, and emotional state. The thesis contends that this shift enables new ways to think about computation—especially for educational and creative contexts—and allows complex behavior to emerge from the combination of simple agents. The work is as much a philosophical investigation into the nature of programming metaphors as it is the technical construction of an environment (LiveWorld) and a language paradigm to enact that philosophy.

## Historical Context
This work emerges from the confluence of three streams in the mid-1990s: 1) the "objects everywhere" paradigm in software engineering, 2) the growing interest in "agent-based modeling" in Artificial Life and social simulation, and 3) the constructionist educational philosophy of Seymour Papert and the Media Lab, which emphasized personal, expressive, and tangible computing. However, Travers identifies a gap: while object-oriented programming (OOP) was becoming dominant, its metaphor—objects as passive actors responding to messages—was still too inert for modeling lifelike worlds. Concurrently, AI research in "intelligent agents" was often overly complex and focused on single, sophisticated entities rather than societies of simple ones. Travers's problem was pedagogical and conceptual: how to make it easy for novices (and experts) to build worlds of interacting, animate things. He saw that existing tools demanded a command-and-control perspective ("do this, then that") rather than an ecological one ("behave like this, and interact with that").

## Key Contributions
1.  **The Agent Metaphor as a First-Class Programming Paradigm:** Formalizes the idea that programming can be centered on defining and combining autonomous, purposeful, emotionally-stateful agents, moving beyond objects-as-containers to agents-as-behaviors.
2.  **LiveWorld:** A visual, interactive programming environment designed to make the agent metaphor tangible. It uses a theatrical/spatial metaphor (objects on a stage), supports direct manipulation, and integrates a visual language for defining agent behaviors, enabling "improvisational programming."
3.  **Dynamic Agents (DA):** A concrete agent-based language and control architecture within LiveWorld. It introduces structures like Tasks, Goals, and Templates to model conflicting desires and goal-oriented behavior, explicitly handling issues like inter-agent conflict and concurrency in a user-understandable way.
4.  **Analytical Framework for Programming Metaphors:** Provides a detailed critique of the metaphors underpinning major programming models (imperative as "commander," functional as "algebra," procedural as "recipe," etc.) and situates the agent metaphor within a broader theory of animacy and perception.
5.  **Focus on Understandability and Conflict:** Addresses the new challenges raised by agent systems—specifically, how to make the activity of a complex society of agents understandable to the user, and how to present and resolve inter-agent conflicts, which becomes a central design problem rather than an implementation bug.

## Methodology
The methodology is fundamentally **design-based research** and **theoretical synthesis**. Travers builds an argument through:
1.  **Metaphorical Analysis:** Drawing on cognitive linguistics (Lakoff, Johnson) and philosophy of science, he deconstructs existing programming paradigms as rooted in specific, often unconscious, metaphors. This is a theoretical, polemical exercise to justify the need for a new one.
2.  **Construction and Implementation:** The core proof is the construction of LiveWorld and the Dynamic Agents system. This is an engineering and design endeavor, demonstrating that the proposed metaphors can be made computationally real and usable.
3.  **Example-Driven Demonstration:** The value of the approach is shown through a series of example programs (a video game, animal behavior, constraint problems) built in the system, arguing for its expressiveness and accessibility.
4.  **Argument by Analogy and Lineage:** He explicitly traces his ideas through the intellectual history of cybernetics, ethology, Minsky's *Society of Mind*, and constructionist education, situating his work as an evolution of these threads.

## Influence
Travers's work is a deep, niche contribution more influential in specific subfields than in mainstream software engineering. Its impact is seen in:
*   **Educational Programming Environments:** It directly influenced systems like Agentsheets (a contemporary project by Repenning) and ToonTalk (Ken Kahn), and prefigured later visual agent-based tools for teaching computational thinking and complex systems.
*   **Agent-Oriented Programming (AOP):** While not the sole origin, it contributed to the conceptual framework for AOP, particularly the emphasis on goals, conflict, and social interaction as first-class concerns.
*   **Artificial Life and Social Simulation:** It provided a usable, high-level environment for creating multi-agent simulations, aligning with the ALife community's interest in emergent behavior from simple rules.
*   **Citation Legacy:** Primarily cited in HCI, educational technology, and agent-based modeling literature. It remains a key reference for discussions on metaphor in programming and the design of animate environments. Its influence is indirect but palpable in any educational tool that encourages building worlds of interacting, autonomous characters.

## Connections to Other Papers in the Collection
*   **Papert (1980) *Mindstorms*:** The most direct intellectual ancestor. Travers extends Papert's constructionist, Logo-based "microworlds" by making the objects within the world not just geometric, but animate and social. It answers Papert's call to "teach AI to children."
*   **Minsky (1986) *The Society of Mind*:** The conceptual bedrock. Travers translates Minsky's psychological theory of mind as a society of simple agents into a programming paradigm. The thesis supervisor's influence is profound.
*   **Kay (1972) *A Personal Computer for Children of All Ages*:** Shares the vision of the computer as a "metamedium" for expressive modeling. LiveWorld's direct-manipulation, object-centric interface is a descendant of Kay's Dynabook ideal, specialized for animacy.
*   **Engelbart (1962) *Augmenting Human Intellect*:** Connects on the theme of using computers to externalize and manipulate mental models. Travers's agents are a specific kind of "conceptual object" to be augmented with behavior.
*   **Backus (1978) *Can Programming Be Liberated from the von Neumann Style?*:** An indirect but important contrast. While Backus sought liberation through functional purity, Travers seeks it through an organic, social metaphor. Both reject the dominant imperative model for its cognitive constraints.
*   **Hofstadter (2001) *Analogy as the Core of Cognition*:** Resonates deeply. Travers's entire project is built on the premise that the right *analogy* (the agent metaphor) is the key to powerful cognition and programming.

## Modern Relevance
This 1996 work is strikingly prescient.
*   **AI Agents & LLMs:** The current boom in autonomous AI agents (e.g., AutoGPT, LangChain agents) mirrors Travers's vision of combining simple, purposeful mechanisms. The challenges he identifies—conflict resolution, understandability, and social dynamics within agent societies—are now at the forefront of designing multi-agent AI systems.
*   **Game Design & Interactive Media:** His focus on creating responsive, autonomous objects is the foundation of modern game AI and interactive narrative. Tools like Unreal Engine's Behavior Trees or visual scripting for NPC behavior echo the principles of LiveWorld.
*   **Educational Technology:** The thesis directly informs modern platforms like Scratch (though Scratch is more event-driven than agent-driven) and StarLogo/NetLogo, which are used to teach complex systems. The debate about what metaphors best facilitate learning to code continues.
*   **Human-AI Interaction:** The problem of making agent activity "understandable to the user" is critical today for explainable AI (XAI). How do we design interfaces that let us comprehend the goals and conflicts of digital agents acting on our behalf?
*   **Knowledge Work:** The idea of using agents to model complex, dynamic systems (ecologies, economies, workflows) is a form of interactive knowledge management. Travers's work suggests that thinking in terms of purposeful, interacting entities may be a more natural way for humans to model complex domains than thinking in terms of data structures and functions.

## Key Quotes
1.  **"In this context, an agent is a simple mechanism intended to be understood through anthropomorphic metaphors and endowed with certain lifelike properties such as autonomy, purposefulness, and emotional state."**
    *   *Analytical:* Defines the agent not by its computational power, but by its perceived *character*. This is a cognitive and design principle first, a technical one second.
2.  **"Complex behavior is achieved by combining simple agents into more complex structures."**
    *   *Analytical:* The core synthesis principle, borrowed directly from *Society of Mind*. It rejects the monolithic program in favor of emergent, social computation.
3.  **"Traditional programming languages are not particularly suited to the task... partly because the models and metaphors underlying them are not particularly suited to the task."**
    *   *Analytical:* A direct challenge to the neutrality of programming languages. They are not mere tools; they are lenses that shape thought and constrain possibility.
4.  **"The agent metaphor also raises new problems such as inter-agent conflict and new tasks such as making the activity of a complex society of agents understandable to the user."**
    *   *Analytical:* Acknowledges that a new metaphor doesn't just solve old problems—it creates a new class of problems. This shows mature, systems-level thinking about design trade-offs.
5.  **"If we learn the world by constructing it, now we have at hand a medium that enables world-building as an everyday learning activity."**
    *   *Analytical:* States the constructionist premise that drives the entire project. The computer is not for executing pre-written programs but for building and exploring executable models.
6.  **"An animate object is one that acts, and from whose actions we can perceive intentions."**
    *   *Analytical:* From the theoretical core. It reduces the high-level concept of "agency" to the perceptual experience of intention, grounding the computational metaphor in human psychology.