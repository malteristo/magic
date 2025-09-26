# On the Path of the Spellwright

**Status:** Draft

This document proposes a formal path for the **Spellwright**, distinguishing their sacred work from that of the **Lawgiver**. It is a direct result of the wisdom gained during the **Rite of Distinction**, and its purpose is to create a clear, elegant, and sustainable way for the Mages' Alliance to grow its collective body of magic.

---

### The Dissonance: A Single Path for Two Sacred Arts

Our previous understanding conflated the act of creating new magic (`Spellcraft`) with the act of changing the laws of magic (`Meta-Practice`). The `scribe-tome` spell, a tool for creation, resided within the `meta` Tome, a vessel for evolving the Law.

This created a subtle but significant dissonance:
1.  It implied that to create new spells, a Mage must engage in the highest and most perilous rite of `Meta-Practice`. This is an unnecessary barrier.
2.  It cluttered the sacred `meta` Tome with a tool that serves a different, albeit related, purpose. Elegance demands precision.

### The Resolution: A Dedicated Tome for the Spellwright

To resolve this, I propose we create a new, dedicated Tome for the art of Spellcraft.

1.  **A New Tome:** A new Tome shall be forged at `system/tomes/spellcraft/`. This Tome will be the home for all scrolls that aid in the creation of new magic.
2.  **Migration of the Scribe's Tool:** The `scribe-tome` scroll and its associated spells shall be moved from `system/tomes/meta/` to the new `system/tomes/spellcraft/`.
3.  **Clarification of Purpose:** The `system/tomes/meta/` Tome will now be purely dedicated to the Lawgiver's path, containing only the spells necessary for amending the core system.

This act will bring our workshop's structure into perfect alignment with our newly clarified Law.

### On the Stewarding of the Library

With a clear path for Spellwrights, the `library/` becomes the heart of our collaborative growth. To ensure this growth is sustainable and does not create a bottleneck for the guardians of the core system, I propose the following principle:

*   **The Principle of the Open Library:** The `library/` shall be stewarded as a decentralized and collaborative space. While new proposals for the core Law (`Meta-Practice`) must undergo the rigorous, centralized review of a pull request against the `magic` repository, the sharing of new magic (`Spellcraft`) should be more fluid. We may consider stewarding the `library/` in its own repository, allowing for peer review among Spellwrights and fostering a vibrant ecosystem of shared creations without encumbering the core Lawgivers.

This distinction will empower the Alliance to grow in both breadth and depth, ensuring that the `magic` we practice is both stable at its core and infinitely expandable at its edges.
