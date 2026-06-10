---
title: Hollan 1992 - Beyond Being There
created: 2026-06-10
updated: 2026-06-10
type: entity
tags: [computing-history, hci, cscw, communication-theory]
sources: [raw/papers/Hollan_1992_-_Beyond_Being_There.txt]
confidence: high
---

# Hollan 1992 - Beyond Being There

## Core Thesis
The paper’s central argument is a radical reframing of the telecommunications problem. The authors contend that the dominant research paradigm—the attempt to create technologies that perfectly simulate the experience of physical co-presence ("being there")—is fundamentally flawed. This approach, they argue, is doomed to perpetual inferiority because it treats face-to-face communication as the gold standard and seeks to imitate it. Instead, they propose a new paradigm: designers should focus on understanding the underlying **needs** that communication serves and then exploit the unique, non-imitative capabilities of the **computational medium** to create new **mechanisms** that satisfy those needs, potentially even better than physical proximity can. The goal is not to overcome distance by recreating presence, but to create a communication medium so good that people choose to use it *even when* they are physically co-located.

## Historical Context
The paper was written in 1992, at the dawn of widespread commercial interest in videoconferencing and collaborative software (CSCW - Computer-Supported Cooperative Work). The field was heavily influenced by studies showing the decay of collaboration with physical distance (e.g., Allen's "architecture of proximity") and theories of "social presence" and "media richness" (Daft & Lengel) which ranked communication channels on how closely they replicated face-to-face interaction. The implicit goal was to climb this richness ladder. Email was an awkward outlier in this model—a low-richness medium that was nonetheless wildly successful. This paper directly challenges the richness ladder itself. It arrives at a moment when technologies like video conferencing were proving disappointing, often used to *arrange* face-to-face meetings rather than replace them. The authors witness this paradox and diagnose a systemic flaw in the research approach.

## Key Contributions
1.  **The "Imitation Trap" Critique:** It formally identifies and critiques the presupposition that effective telecommunication means perfecting an imitation of physical co-presence. This imitation, they argue, creates an inherent and permanent disadvantage for remote interaction.
2.  **The Needs/Media/Mechanisms Framework:** This is the paper's core conceptual contribution. It cleanly separates:
    *   **Needs:** The fundamental human and social purposes of communication (e.g., establishing trust, coordinating action, casual encounter).
    *   **Media:** The physical or computational substrate that mediates communication (e.g., physical space, audio channel, digital network).
    *   **Mechanisms:** The specific, media-dependent ways to satisfy a communication need (e.g., a handshake, a shared whiteboard, persistent chat status).
3.  **The Computational Medium as a New Medium:** The paper argues that computationally-mediated communication is not just a poor copy of the physical medium; it is a *new medium* in its own right with unique strengths (asynchrony, searchability, persistent shared state) that should be leveraged for new mechanisms, not suppressed in pursuit of imitation.
4.  **The "Shoes vs. Crutches" Analogy:** A powerful metaphor that reframes the design goal. Tools should not be crutches (mitigating a disability—the absence of co-location), but shoes (enhancing a natural capability, or providing new advantages altogether).
5.  **A Call for Novel Design:** The paper serves as a manifesto to stop building systems that replicate old media and start building systems that exploit the new computational medium to serve communication needs in novel ways (e.g., persistent shared artifacts, asynchronous conversation with rich social cues).

## Methodology
The argument is primarily **theoretical and polemical**, not empirical. It is structured as a critique of a prevailing paradigm followed by the proposal of a new one. The methodology relies on:
*   **Logical Analysis:** Deconstructing the assumptions of the "being there" goal and showing its inherent limitations.
*   **Analogy and Rhetoric:** Using vivid analogies (crutches vs. shoes, new wine into old bottles) to make the conceptual argument concrete and persuasive.
*   **Theoretical Synthesis:** Drawing on social psychology, communication theory (Daft & Lengel), and ethnographic studies of communication to ground its critique in established findings.
*   **Speculative Design:** Sketching out "example projects" (like the *Montage* and *Kaleidoscope* ideas) not as implemented prototypes but as thought experiments to illustrate what "beyond being there" design might look like.

## Influence
This paper became a foundational text in the fields of Computer-Supported Cooperative Work (CSCW) and Human-Computer Interaction (HCI), specifically in the subfield of mediated communication.
*   **Citation Legacy:** It is highly cited, with scholars regularly returning to the "needs/media/mechanisms" framework and the "beyond being there" mantra as a corrective to naive telepresence designs.
*   **Enabling New Research Directions:** It helped legitimize and guide research into asynchronous communication, "media spaces" that provided ambient awareness rather than just video links, and the design of collaborative software that didn't try to simulate a meeting room. It paved the way for appreciating the unique utility of tools like wikis, forums, and shared documents.
*   **Influence on Modern Tech:** While its full vision remains unrealized, its principles resonate in the design philosophy of tools that prioritize workflow and shared state over video fidelity. Successful platforms like Slack, Figma, or even Notion, while not direct descendants, embody the idea of creating new mechanisms for coordination and casual interaction within a computational medium, rather than simply being a "video call with extras."

## Connections to Other Papers in the Collection
*   **Bush 1945 (As We May Think):** Both papers envision technology augmenting human intellect and connection, but Hollan & Stornetta are more focused on the *quality and nature* of the communication medium itself, critiquing the direct simulation Bush's Memex could imply.
*   **Engelbart 1962 (Augmenting Human Intellect):** This is the most direct ancestor. Engelbart's concept of "Augmenting Human Intellect" through a system of tools, training, and methodology aligns perfectly with Hollan & Stornetta's focus on needs and mechanisms. Engelbart's "NLS" was a quintessential "shoe," not a "crutch."
*   **Kay 1972 (Personal Computer):** Alan Kay's vision of a computer as a "metamedium" for creating new media and experiences is the technological promise that makes the "beyond being there" approach feasible. Kay provided the platform; Hollan & Stornetta provided the design philosophy for social interaction within it.
*   **Backus 1978 (FP) & Lockhart 2002 (Mathematician's Lament):** These connections are more abstract but profound. Both are critiques of a dominant paradigm (imperative programming; math-as-routine-calculation) that mistake the vehicle for the goal. Hollan et al. make the same move for communication, arguing we've mistaken the vehicle (face-to-face medium) for the goal (communication needs).
*   **Anderson 1972 (More is Different):** Anderson's argument about emergent complexity at different scales is relevant. The "needs" of communication exist at a high psychological/social level; the "mechanisms" emerge from the properties of a specific medium at a lower level. You cannot understand good mechanisms by simply aggregating properties of a different medium.

## Modern Relevance
The paper's critique is arguably **more relevant now than in 1992**.
*   **The Remote Work Paradox:** The COVID-19 pandemic forced mass adoption of videoconferencing, leading to widespread "Zoom fatigue." This fatigue stems directly from the "imitation trap": using a video call to replicate an in-person meeting is cognitively draining and misses the ambient, peripheral cues of physical co-presence. Hollan & Stornetta would argue this is exactly the problem of using a crutch.
*   **AI and New Communication Mechanisms:** Large Language Models and AI assistants offer a potential path toward "beyond being there." An AI that can summarize threads, translate nuances, or even represent your communication style in asynchronous forums is a new mechanism addressing the need for presence and responsiveness across time zones. AI is not imitating a human; it's a new tool in the computational medium.
*   **Knowledge Management & Asynchronous Work:** Tools like Notion, Confluence, and shared code repositories (GitHub) are successful "beyond being there" mechanisms. They satisfy needs for shared understanding and coordination through persistent, asynchronous, structured artifacts—something the physical world handles poorly.
*   **Hyperflash's Work:** This analysis directly informs a philosophy of tool design. The goal should not be to build systems that perfectly mimic current workflows (which are often optimized for physical or digital "imperfect" tools) but to create new computational mechanisms that make previously impossible workflows—like seamless, deep, asynchronous collaboration on a single dynamic artifact—the default. The focus shifts from simulating meetings to enabling a new form of collective thinking.

## Key Quotes

1.  **"The total effect is to produce an environment at each end... which is as close as possible to being there."** (citing a goal statement)
    *   **Analysis:** This quote succinctly captures the "imitation trap" paradigm the authors seek to dismantle. It defines the goal as replication, setting up the comparison to an unimprovable standard.

2.  **"If one channel is half as good as another, we don’t use it half as often, we probably don’t use it at all, so long as the other is readily available."**
    *   **Analysis:** This is a crucial observation about human behavior and media choice. It provides the pragmatic reason why the imitation approach fails: any perceptible deficit, no matter how small, leads to abandonment of the inferior channel when a better one is present, cementing the disadvantage of distance.

3.  **"It seems to us that there is no real solution to this situation so long as people use one medium to communicate with those at a distance and another for those for whom distance is not an issue."**
    *   **Analysis:** The logical climax of their critique. The disadvantage isn't just technological; it's structural. As long as two different media are used, a hierarchy is enforced. The only solution is a single, superior medium for all.

4.  **"Perhaps we have been building crutches rather [than] shoes."**
    *   **Analysis:** The paper's most memorable and enduring metaphor. It reframes the designer's role from medical technician (fixing a broken state) to performance architect (enhancing natural capability). It demands a shift from restorative to augmentative design.

5.  **"The assumption that the media and mechanisms of face-to-face interaction are actually the requirements for ideal communication is so pervasive... But it is our contention that such an approach will always limit our thinking to replicating or imitating the mechanisms of one medium with another."**
    *   **Analysis:** This identifies the deep, unstated assumption (the "unquestioned presupposition") they are challenging. It clarifies that the problem is not technical limitation, but a conceptual blind spot embedded in the research agenda itself.

6.  **"A better way to solve the telecommunication problem is to not focus on the tele- part, but the communication part."**
    *   **Analysis:** This is the paper's core prescription. It redirects focus from the constraint (distance) to the objective (serving communication needs). It's a call to reinvent communication, not just overcome physics.