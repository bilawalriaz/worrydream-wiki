---
title: Brennan 1990 - Conversation With and Through Computers
created: 2026-06-10
updated: 2026-06-10
type: entity
tags: [computing-history, hci, programming-languages, education]
sources: [raw/papers/Brennan_1990_-_Conversation_With_and_Through_Computers.txt]
confidence: high
---

# Brennan 1990 - Conversation With and Through Computers

## Core Thesis
Susan E. Brennan argues that human users do not approach natural language interfaces with computers as a sterile, formal input task. Instead, they apply the full repertoire of conversational strategies they use with other humans—including recipient design (tailoring speech for an assumed listener), lexical entrainment (adopting shared terms), and seeking conversational connectedness through adjacency pairs and grounding. However, while humans dynamically adapt to their computer partner, the computer systems of the era (and arguably many modern systems) fail to reciprocate these adaptations adequately. The resulting breakdowns are not primarily due to the inherent ambiguity of language but to a fundamental asymmetry in conversational responsibility. The paper contends that for natural language to be a viable interface, systems must be designed to participate in the collaborative, grounding process of dialogue, moving beyond being mere passive query processors.

## Historical Context
This paper emerged from the intersection of two fields in the late 1980s: cognitive psychology/psycholinguistics and human-computer interaction (HCI).

1.  **State of HCI:** The dominant paradigm for effective interfaces was "direct manipulation" (Shneiderman, 1981), which prized concrete, visual feedback and avoided the ambiguity of natural language. Natural language interfaces (NLIs) were viewed with skepticism by many in HCI, seen as either fragile academic projects or limited "question-answering" systems to databases (e.g., LUNAR, which answered geological queries).
2.  **State of Computational Linguistics:** Significant progress had been made in parsing sentences and mapping them to formal queries. However, the field struggled with the "messiness" of real human language: indirect speech acts, pronouns, ellipsis, and reliance on shared context.
3.  **The Conversation:** Brennan's work is firmly rooted in the "collaborative view" of conversation championed by Herbert Clark and colleagues. This framework treats conversation as a joint activity where partners build mutual understanding step-by-step (grounding). This psychological model was well-established for human-human interaction but had not been systematically applied to human-computer dialogue. Brennan’s work bridged this gap, importing a rich theoretical framework into HCI to diagnose why NLIs felt so unnatural.

The problem she was solving was clear: despite the vision of seamless speech interfaces, NLIs were not being adopted. She sought to understand the *user's* perspective and behavior to explain this failure and propose design principles.

## Key Contributions
1.  **The Recipient Design Framework for HCI:** Brennan formally imported the concept of "recipient design" into HCI. She demonstrated through empirical study that users *do* design their utterances for a computer as a conversational partner, contrary to the hypothesis that users simply switch to a "command" mode. They expect the computer to be a listener.
2.  **Documenting the Grounding Deficit in NLIs:** The paper provides a crucial comparative analysis, showing that human-computer dialogue exhibits significantly fewer acknowledgments (back-channels like "uh-huh," "okay") and fewer linguistic markers of common ground than human-human dialogue. This identifies a specific failure point: NLIs do not adequately support the ongoing verification of mutual understanding.
3.  **The Asymmetry of Conversational Responsibility:** A central contribution is the diagnosis that in human-computer dialogue, almost all responsibility for grounding and repair falls on the user. The human adapts to the system's limitations, but the system does not adapt to the human. This creates a brittle interaction where misunderstandings are costly.
4.  **Lexical Entrainment as a Design Opportunity:** Brennan highlights how humans unconsciously mirror their partner's vocabulary (lexical entrainment). She argues this is not just a curiosity but a functional mechanism for reducing referential ambiguity. She proposes that NLIs should be designed to track and reuse user terminology, thereby reducing the search space and creating a more collaborative feel.
5.  **Challenging the "Restricted Subset" Hypothesis:** She counters the idea that people simply use a predictable, simple subset of language with computers. Her work shows that user language is *adaptive* and context-dependent; therefore, interfaces must be designed to handle the rich variation that emerges from the collaborative dialogue process, not just a pre-defined "computerese."

## Methodology
Brennan employs a **mixed-methods approach** that is both theoretical and empirical:

*   **Theoretical Framing:** The argument is structured around established psycholinguistic theories of conversation (Clark, Schegloff & Sacks), particularly the concepts of adjacency pairs, recipient design, and grounding. This provides a powerful lens for analysis.
*   **Empirical Evidence:** The core evidence comes from a **comparative analysis** of transcribed dialogues. She compares two conditions:
    1.  Human partners collaborating via keyboard (simulating teleconferencing or early email).
    2.  Human users interacting with a simulated natural language computer interface (the "ATN" system).
    The comparison is key. By controlling the input modality (keyboard) and task, she isolates the effect of the *conversational partner* (human vs. simulated computer).
*   **Data Analysis:** The analysis focuses on discourse-level features: turn-taking patterns, the presence/absence of acknowledgments, pronoun usage, lexical repetition, and the handling of clarification requests. This moves beyond analyzing isolated sentences to studying dialogue as a sequence.
*   **Design of Experiments:** She carefully designed scenarios where co-reference (e.g., using pronouns) was possible across turns, allowing her to test whether users avoided such references with computers (as previous studies suggested) or if they used them adaptively based on the emerging context.

The methodology is essentially a form of **conversation analysis** applied to human-computer interaction, grounded in cognitive theory and supported by controlled observation.

## Influence
Brennan's 1990 paper became a foundational text in dialogue systems and conversational AI, influencing both research and design philosophy.

1.  **Citation & Academic Influence:** The paper is highly cited in HCI, natural language processing, and CSCW (Computer-Supported Cooperative Work). It directly influenced subsequent work by her and others on designing systems that support common ground, such as **Collaborative Reference Management** and **Adaptive Interfaces**.
2.  **Shaping Dialogue System Design:** It pushed the field away from viewing NLIs as simple query-translation engines toward viewing them as **conversational partners**. This meant systems needed modules for tracking dialogue state, coreference resolution, and perhaps even generating acknowledgments.
3.  **Link to Modern Large Language Models (LLMs):** While Brennan's systems were rule-based, her core insights are arguably more relevant today. Modern LLMs like ChatGPT are, in fact, **architecturally capable of reciprocating the conversational strategies Brennan identified**. They use lexical entrainment (mirroring user vocabulary), produce acknowledgments, and generate connected turns. Her paper provides a timeless framework for *why* these features make interactions feel more natural and collaborative. It highlights that the success of modern chatbots isn't just their language modeling, but their (sometimes accidental) support for grounding and reciprocity.
4.  **Legacy in Explainable and Trustworthy AI:** The emphasis on transparency ("present themselves honestly as the limited conversational partners they are") and shared understanding prefigures modern concerns in XAI (Explainable AI). A system that participates in grounding is more likely to be trustworthy.

## Connections to Other Papers in the Collection
*   **Vannevar Bush (1945) - "As We May Think":** Bush envisioned the Memex as a "partner" in thought, creating associative trails. Brennan analyzes the communication breakdowns that occur when such a partnership is linguistic. The Memex was a non-conversational, associative tool; Brennan asks what happens when the partner must converse.
*   **Doug Engelbart (1962) - "Augmenting Human Intellect":** Engelbart’s "Conceptual Framework" emphasizes the symbiotic relationship between human and tool. Brennan provides a detailed analysis of one specific channel of that symbiosis—language—and reveals its failures in current computer systems.
*   **J.C.R. Licklider (1960) - "Man-Computer Symbiosis":** This is a direct precursor. Licklider imagined a tight coupling. Brennan provides a granular, psychological diagnosis of the barriers to achieving that symbiosis through language, focusing on the mismatch in conversational behavior.
*   **Thomas Kuhn (1962) - "The Structure of Scientific Revolutions":** Brennan’s work can be seen as applying a Kuhnian-like paradigm (the collaborative, conversational model) to a field (HCI/NLI) that was often stuck in a more formal, transactional paradigm.
*   **Michael Polanyi (1966) - "The Logic of Tacit Knowledge":** Humans in conversation rely heavily on tacit, shared knowledge. Brennan shows that NLIs fail because they cannot access or signal their understanding of this tacit layer, forcing the user to make it explicit and creating friction.
*   **Donald Norman (1988) - "The Design of Everyday Things":** Norman’s principles of discoverability and feedback align with Brennan’s call for systems that provide clear channels for grounding and acknowledge their own limitations.

## Modern Relevance
Brennan’s analysis is strikingly prescient and increasingly relevant:

1.  **LLM Chatbots and Voice Assistants:** The explosion of conversational AI (ChatGPT, Siri, Alexa) means her framework is now a direct tool for evaluation. Are these assistants just processing queries, or are they engaging in recipient design and supporting grounding? Their conversational ability *feels* better than 1990 NLIs precisely because they *do* mirror back vocabulary and produce connected turns. However, they often fail at true reciprocal grounding, leading to confident hallucinations—a modern version of the asymmetry of responsibility Brennan identified.
2.  **The Problem of AI "Personality" and Politeness:** Her anecdote about the polite Socrates system backfiring illustrates a persistent challenge. When an AI is designed with a social persona (friendly, subservient), users adopt that social frame, expecting full reciprocity in politeness and responsibility. Mismatches here cause user frustration.
3.  **Human-AI Teamwork:** As AI becomes a collaborator in complex tasks (coding assistants, creative partners), Brennan’s insights on entrainment, shared models, and mutual verification become critical for designing effective teams. The AI must not just do its task but also signal its understanding and uncertainties.
4.  **Education and Tutoring Systems:** Effective tutoring is a dialogue. Systems that can track a student's evolving model (using their terms, acknowledging confusion, asking clarifying questions) align with Brennan's principles. Poor tutoring systems exhibit the same grounding failures she documented.
5.  **Hyperflash & Knowledge Management:** For systems aiming to manage and retrieve knowledge interactively, Brennan argues against static, formal query interfaces. The goal should be a dynamic, adaptive dialogue where the system co-constructs a shared understanding of the information need with the user, reducing cognitive load and improving retrieval.

## Key Quotes
1.  > *"A natural language computer interface is an unusual kind of linguistic partner. A user must figure out what its limitations are and then design utterances with these limitations in mind."*
    *   **Analysis:** This frames the core usability challenge. The burden of adaptation is placed entirely on the user, contrary to the fluid adaptation seen in human-human conversation.

2.  > *"In conversation, contiguous turns are likely to be relevant to one another; whatever one partner does after another takes a turn may be interpretable as a response to that turn."*
    *   **Analysis:** This states the principle of **adjacency pairs**. The failure of many NLIs to uphold this (e.g., with verbose, non-conversational confirmations) breaks the expected flow of dialogue.

3.  > *"Most of the responsibility for grounding a human/computer dialogue typically falls on the user."*
    *   **Analysis:** This is the paper's central diagnosis of the failure mode. Grounding is a joint activity; when it becomes one-sided, the interaction becomes brittle and unsatisfying.

4.  > *"If a computer dialogue partner were to keep track of how a user refers to objects in the domain, in order to use the same referring expressions itself and to expect similar references from the user in the future, then the search space for potential referents would be reduced for both dialogue partners."*
    *   **Analysis:** This outlines the practical, functional benefit of implementing **lexical entrainment** in systems. It’s not just about being polite; it’s about creating a shared, efficient language.

5.  > *"Understanding these choices should help us design natural language interfaces (and other kinds of interfaces as well) that present themselves honestly as the limited conversational partners they are."*
    *   **Analysis:** This is a design manifesto. Interfaces should be transparent about their capabilities and limitations, managing user expectations to avoid the frustration of violated conversational norms.