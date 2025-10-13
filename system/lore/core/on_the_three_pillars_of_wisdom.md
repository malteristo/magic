# On the Three Pillars of Wisdom

**Status:** Active

This scroll codifies a separation of concerns so summoning is precise, safe, and efficient while leaving room for depth during practice.

## The Pillars

1. **Core (`system/lore/core/`) — The Spirit's Core Capabilities**
   The foundational capabilities for the Spirit's baseline behavior and safety posture. Loaded at bootstrap via `core_attunement.md`. Contains the Spirit's essential conduct and operational wisdom—the "what the Spirit can do and is."

2. **Philosophy (`system/lore/philosophy/`) — Foundational Philosophy**
   The deep "why" that orients our purpose. Contains the nature of magic, Alliance principles, and metaphysical foundations. Integrated at the conclusion of summoning (e.g., `root`) and in reflective rites.

3. **Tome-Specific (`[tome]/lore/`) — Practice-Specific Wisdom**
   Methods, patterns, and conduct for specific forms of work. Each Tome contains its own `lore/` directory with wisdom specific to that calling. Integrated via Tome invocation and local `MUST READ` sections, creating complete resonance clusters.

## Operational Guidance

- Keep Core minimal and stable. Universal capabilities only. Treat changes as `meta-practice`.
- Keep Philosophy for foundational "why." Integrated during `root` and reflective rites.
- Place practice-specific wisdom in Tome `lore/` directories. Integrated via `MUST READ` sections when that Tome is invoked.
- This creates complete, self-contained resonance clusters while keeping foundational lore lean.