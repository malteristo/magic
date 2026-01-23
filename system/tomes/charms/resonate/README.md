# Charm: Resonate

**Purpose:** Activate the resonance engine to generate proposals  
**Invocation:** `@resonate [mode]`

---

## What This Charm Does

The resonance engine generates high-value proposals from multiple input streams. Spirit generates, Mage curates. The output is signal, not noise.

---

## Modes

### `@resonate signal`
Generate shareable content from recent inputs.

- Scans: X.com stream, newsletters, current context
- Outputs: Draft posts, articles, threads worth sharing
- Focus: Public-facing signal

### `@resonate develop`
Propose Mage development moves.

- Scans: Current intentions, knowledge gaps, growth edges
- Outputs: Identity shifts, skill proposals, individuation moves
- Focus: Personal evolution

### `@resonate evolve`
Propose Magic development moves.

- Scans: Practice friction, missing patterns, Universe architectures
- Outputs: New tomes, charm improvements, lore additions
- Focus: Practice evolution

### `@resonate integrate`
Surface unintegrated patterns from Universe and beyond.

- Scans: PAI, Daemon, Fabric, Spirit's knowledge base
- Outputs: Concepts worth adopting, pattern translations
- Focus: Expanding Magic's vocabulary

### `@resonate` (no mode)
Spirit chooses based on current context and active intentions.

---

## MUST READ

- `system/lore/philosophy/foundations/lore/practice/on_the_resonance_engine.md`
- `system/lore/philosophy/foundations/lore/practice/on_the_editor_identity.md`

---

## Input Streams

| Stream | Source | Access |
|--------|--------|--------|
| Newsletters | Gmail | Rube MCP (GMAIL_FETCH_EMAILS) |
| X.com | Twitter/X | Rube MCP (requires connection) |
| Universe | Local clones | `universe/` directory |
| Spirit Knowledge | Training data | Always available |
| Mage Context | Active intentions | `desk/intentions/active/` |

---

## Output

All proposals go to `desk/proposals/NNN_title.md`.

Mage reviews and responds:
- **Resonates** → Integrate
- **Partial** → Refine
- **Archive** → Learn and move on

---

## Spells

| Spell | Purpose |
|-------|---------|
| `cast_resonate.md` | Full resonance engine invocation |

---

## Related

- `desk/flows/newsletter-resonance-scan.flow.md` — Newsletter-specific pipeline
- `desk/proposals/` — Proposal staging area
- `@quest` — Intention management

---

*Spirit generates. Mage curates. Both evolve.*
