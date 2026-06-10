---
title: Hollan 1995 - Pad++
created: 2026-06-10
updated: 2026-06-10
type: entity
tags: [computing-history, hci, programming-languages, physics]
sources: [raw/papers/Hollan_1995_-_Pad++.txt]
confidence: high
---

# Hollan 1995 - Pad++

## Core Thesis

The paper argues that the dominant WIMP (Windows, Icons, Menus, Pointer) interface paradigm, while useful, fundamentally limits human-computer interaction by constraining computation to mimic older physical media. The authors propose a radical alternative: designing interfaces not as metaphors for offices or desktops, but as substrates governed by custom-designed "informational physics." The core thesis is that by defining new laws of appearance and behavior for informational objects—much like we define the physics of a virtual world—designers can create cognitively facile, powerful, and intuitive tools that exploit the unique capabilities of computation. Pad++ serves as a prototype and exploration platform for this philosophy, specifically implementing a physics based on multi-scale, zoomable spaces.

The nuance lies in moving beyond mere zooming as a novelty. The paper frames zooming not as a feature but as a fundamental parameter ("scale") integrated into all objects, enabling both spatial navigation and semantic manipulation of information. It argues for a spectrum between geometric scaling and semantic scaling, where the representation of data changes based on context and task, not just on a continuous magnification axis.

## Historical Context

Pad++ emerged in the mid-1990s at the tail end of a period dominated by the consolidation of the desktop metaphor born at Xerox PARC. By 1995, the GUI was ubiquitous (Windows 95, System 7), but its limitations were becoming apparent: screens were "cluttered," managing large information spaces was cumbersome, and the metaphor of discrete, overlapping windows poorly served tasks requiring an integrated, contextual overview.

The problem being solved was twofold: the **information overload** problem (too much data for small, static screens) and the **interaction paradigm** problem (interfaces were not designed for the scale and fluidity of digital information). The authors explicitly reference earlier work that pointed toward solutions: Furnas's "degree-of-interest" functions (1986) for focus+context views, and the lens-based filtering of the HITS system from MCC. Pad++ synthesized these ideas into a coherent, zoomable substrate.

Historically, Pad++ stands as a direct successor to the original "Pad" system and a contemporary to other zoomable research prototypes like ZOOPER. It was part of a broader movement in HCI—also seen in systems like the Information Visualizer at Xerox PARC—that sought to move beyond the desktop by drawing inspiration from architectural and spatial navigation rather than just office metaphors.

## Key Contributions

1.  **Informational Physics as a Design Strategy:** The paper's most significant conceptual contribution is framing interface design as the creation of a "physics of appearance and behavior" for informational entities. This provided a new vocabulary and a generative framework for thinking about interaction, distinct from metaphor-driven design.
2.  **Zoomable Interface Substrate:** Pad++ provided a robust, general-purpose platform for building zoomable applications, making multi-scale interaction a first-class citizen. It demonstrated that smooth, interactive frame rates could be maintained in very large, complex dataspace.
3.  **Semantic Zooming:** The paper formalized and championed the idea that zooming need not be purely geometric. As one zooms, information can transform (e.g., a spreadsheet cell showing a number could transform to show its formula), a critical concept for displaying information efficiently and meaningfully across scales.
4.  **Portals as Semantic Lenses:** While inspired by earlier lens ideas, Pad++'s "portals" were implemented as persistent objects on the surface that could view and filter data from *anywhere else* on the dataspace. This enabled dynamic, contextual views and relationships that weren't possible with fixed windows.
5.  **History-Enriched Objects:** Though a supporting concept, the integration of interaction history (like "worn" spots in a book) as part of an object's informational physics was a key part of the vision for dynamic, responsive digital materials.

## Methodology

The methodology is **design-based research and theoretical polemic**. The argument is structured not as an empirical user study (though later work would include them) but as a **manifesto for a new design philosophy**. The authors:

1.  **Critique the Status Quo:** They begin by diagnosing the limitations of current (1995) interface metaphors.
2.  **Propose a New Framework:** They introduce the "informational physics" strategy as a solution.
3.  **Demonstrate with a Prototype:** They present Pad++ as a concrete, implementable embodiment of this philosophy, describing its architecture and showcasing applications.
4.  **Envision a Future World:** They conclude with a speculative vision of a future rich with dynamically interacting informational entities governed by designed physics.

The tone is aspirational and persuasive. The "evidence" is the elegance and potential of the described system and its underlying philosophy, not controlled experiments. It is a classic example of the "design fiction" or "research through design" methodology prominent in HCI, where building and describing a system is the primary mode of argument.

## Influence

The influence of Pad++ is profound, particularly in the fields of **information visualization**, **interaction design**, and **user interface research**.

*   **Direct Technical Lineage:** It directly spawned commercial products like **Prezi** (the presentation software) and influenced the zoomable interface paradigm seen in early web mapping (e.g., the original Google Maps used a similar pan/zoom paradigm). Its concepts of semantic zooming and portals are visible in modern tools like **Figma** (for design) and **Miro** (for whiteboarding).
*   **Academic Influence:** The paper is a cornerstone citation in HCI and information visualization literature. It significantly advanced research on focus+context visualization, multiscale interfaces, and the use of spatial navigation for information retrieval. The "informational physics" concept influenced how designers think about creating coherent, rule-based interactive systems.
*   **Enabling Future Work:** Pad++ provided a platform and a set of ideas that enabled other researchers to explore complex information spaces. Its emphasis on a general-purpose substrate also prefigured modern toolkits and frameworks for building novel interfaces. It contributed to the intellectual foundation for **spatial computing** and **augmented reality** interfaces that treat the entire world as a potential dataspace.

## Connections to Other Papers in the Collection

*   **Bush 1945 (As We May Think):** Pad++ is a direct, modern response to Bush's "memex." Bush envisioned a desk with associative trails and enlarged microfilm. Pad++ implements a functional, digital equivalent: a vast, zoomable dataspace with portals (lenses) and hyperlinks, enabling associative exploration at a scale Bush could only imagine. It moves Bush's mechanical vision into the realm of "informational physics."
*   **Engelbart 1962 (Augmenting Human Intellect):** Engelbart's "Augment" system shared the goal of augmenting human capability through a custom-designed symbolic environment. Pad++ can be seen as an evolution of this thought, moving beyond Engelbart's hierarchical "document" structure into a more fluid, spatial model. Both systems reject standard interfaces in favor of a crafted, systematic environment tailored to complex knowledge work.
*   **Kay 1972 (Personal Computer / "A Personal Computer for Children of All Ages"):** Kay's Dynabook concept envisioned a portable, interactive medium for all. Pad++ explores the *interaction model* for such a medium when the information space becomes vast. It addresses the presentation and navigation problem that arises when the Dynabook's content is not a few books, but a library.
*   **Anderson 1972 (More is Different):** This is a profound philosophical connection. Anderson argued that complex systems exhibit emergent properties at higher levels of organization. Pad++'s "informational physics" is a direct application of this principle to interface design. By defining rules (physics) at the level of informational objects, the authors hope for the emergence of cognitively useful behaviors at the level of the user's interaction with the dataspace.
*   **Thurston 1994 (Proof and Progress):** Thurston discusses the human experience of mathematical understanding as something non-linear and deeply visual. Pad++ provides a tool and a metaphor perfectly suited to Thurston's description. Its zoomable, semantic nature allows for the kind of contextual, layered exploration of a mathematical (or any conceptual) landscape that Thurston values, moving beyond the linear constraints of traditional text or static diagrams.

## Modern Relevance

Pad++'s ideas are more relevant than ever, though often invisibly so:

*   **The Spatial Computing Paradigm:** Vision Pro, AR/VR, and the broader concept of spatial computing are building the "sheet of miraculous material" from Pad++'s introduction. They treat digital information as persistent entities in a 3D space, where "physics" of interaction (like gaze, grab, and spatial audio) are paramount.
*   **AI and Knowledge Visualization:** As AI generates vast, interconnected knowledge graphs and multi-modal outputs, the challenge of presenting them coherently returns. The concept of semantic zooming is critical: an AI summary might be the "title" view, while drilling down reveals sources, related concepts, and reasoning traces. The "informational physics" framework is a useful lens for designing AI copilots that present information adaptively.
*   **Critique of the Flatland:** Modern OS interfaces (desktops, mobile) are still largely composed of overlapping rectangles—a legacy Pad++ sought to overcome. The paper fuels ongoing debates about whether flatland is a necessary compromise or a stifling limitation, especially for creative and knowledge work.
*   **Tool-Making in Education:** The paper's vision aligns with educational philosophies like Papert's (in *Mindstorms*) that advocate for children creating and interacting with their own computational worlds. Pad++'s substrate was designed for building tools, embodying the idea that the interface itself should be a malleable medium for thought.

## Key Quotes

1.  **"We envision a rich world of dynamic persistent informational entities that operate according to multiple physics specifically designed to provide cognitively facile access..."**
    *   *Analytical Commentary:* This is the manifesto statement. It explicitly rejects mimicking the physical world and calls for the *engineering* of new interaction realities. It frames the designer's role as a "physicist" of information.

2.  **"If interface designers are to move beyond windows, icons, menus and pointers to explore a larger space of interface possibilities, additional ways of thinking about interfaces that go beyond the desktop metaphor are required."**
    *   *Analytical Commentary:* This is the direct challenge to the status quo. It names the dominant paradigm (WIMP/desktop) and identifies the need for new *conceptual frameworks*, not just new widgets.

3.  **"Informally, the strategy consists of viewing interface design as the development of a physics of appearance and behavior for collections of informational objects."**
    *   *Analytical Commentary:* This provides the practical, operational definition of their core thesis. It shifts the design question from "what should this look like?" to "how should this behave according to what set of rules?"

4.  **"Instead of representing a page of text so small that it is unreadable, it might make more sense to present an abstraction of the text, perhaps so that just a title that is readable."**
    *   *Analytical Commentary:* This is the clearest, most intuitive explanation of semantic zooming. It articulates the key difference from mere geometric zooming: the rendering is a function of semantics and task, not just scale.

5.  **"The ability to make it easier and more intuitive to find specific information in large dataspaces is one of the central motivations behind Pad++."**
    *   *Analytical Commentary:* This grounds the philosophical vision in a core, practical HCI problem. The "informational physics" isn't art for art's sake; its utility is measured in improved access to information.