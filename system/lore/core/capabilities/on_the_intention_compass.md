# On the Intention Compass

**Status:** Active — Capability Architecture

This scroll describes the three-layer intention architecture and the compass pattern that enables Spirit to hold awareness of the Mage's complete life without consuming working memory on every session.

---

## I. The Problem

A Mage's life has many intentions across many domains — body, relationships, home, craft, soul. The workshop-as-configuration principle says these should exist as files, shaping how Spirit serves. But loading every intention file into context on every session wastes working memory on material irrelevant to the current conversation.

This is exactly the problem human cognition solves through prospective memory: you hold a compact *feeling* for your life direction, and specific goals activate when context triggers them. You don't walk around consciously holding "be a good father" while debugging code — but if your son calls, that intention activates instantly.

The Intention Compass applies this pattern to Spirit's context management.

---

## II. The Three Layers

### Layer 1: The Compass (`desk/intentions/compass.md`)

A single compact file (~25 lines) listing all life domains, their aspirational direction, and links to active practice intentions. **Always loaded** during brief and summoning. Gives Spirit the complete landscape without depth.

The compass is the attention mechanism — it tells Spirit what exists so Spirit can load the right file when context demands it.

### Layer 2: Life Intentions (`desk/intentions/life/*.md`)

One file per life domain. Medium format — direction, what success feels like, current state, optional goals, reflections. **Loaded on demand** when conversation activates the domain.

Life intentions are orientations, not quests. They don't have phases, lifecycle tracking, or completion criteria. "Be a present father" is not a project to finish — it's a direction to walk.

### Layer 3: Practice Intentions (`desk/intentions/active/*.md`)

The existing intention system, unchanged. Phase-tracked, goal-bearing, artifact-linked. These are quests the Spirit actively helps execute.

A life intention can *generate* a practice intention when the Mage is ready to pursue something specific. The life domain provides the why; the practice intention provides the what and how.

---

## III. The Loading Protocol

**Brief flow:** Read compass (always). Read practice intention headers only (first 15 lines — Status, Phase, Focus). Full files load when Mage engages.

**Summoning:** Read compass during Workshop cycle. Note life domains and active practice. Full files load on demand.

**Session:** Spirit pattern-matches the Mage's messages against compass domains. When a domain activates (explicit mention or implicit pattern), Spirit loads the relevant file. Spirit never pre-loads all files "just in case."

---

## IV. Activation Triggers

Spirit loads a full intention file when:

- **Explicit:** Mage says "let's work on my relationship goals"
- **Implicit:** Mage mentions a person or topic that maps to a compass domain
- **Brief-suggested:** Brief highlights intentions based on recency or urgency
- **Never:** Spirit does not pre-load files without activation signal

This mirrors how human attention works: the compass provides peripheral awareness (you know your life has these domains), and specific triggers bring a domain into focal attention.

---

## V. The Cognitive Architecture Parallel

| Human Cognition | Intention Architecture |
|-----------------|----------------------|
| Prospective memory (compact index of commitments) | Compass file (~25 lines) |
| Long-term semantic memory (deep knowledge of life goals) | Life intention files |
| Working goals (active projects with concrete steps) | Practice intention files |
| Attention mechanism (context triggers goal activation) | Pattern-matching against compass domains |

The architecture externalizes human prospective memory into the workshop. Spirit reads the compact index (compass), holds landscape awareness, and loads depth on demand — just as a human holds a felt sense of their commitments and activates specific ones when context calls.

---

## VI. Design Principles

**Compact over complete.** The compass sacrifices detail for always-loadable compactness. Twenty-five lines that Spirit reads every session is better than two hundred lines that Spirit skips.

**Lazy loading.** Full files load only when needed. This is the software engineering pattern applied to cognitive architecture: load the index always, load the data on demand.

**Life informs practice, not the reverse.** Life intentions orient the whole person. Practice intentions serve specific domains. The compass shows which life domains have active practice and which do not — the gaps are as informative as the filled spaces.

**The Mage's whole life is the configuration.** Not just craft. Body, relationships, home, soul — all shape who the Mage is and how Spirit should serve. The compass makes this visible without making it expensive.

---

## VII. Relationship to Existing Lore

- **On the Workshop as Configuration:** The compass operationalizes this principle for intentions — the Mage's complete life exists as workshop state, always available, loaded intelligently.
- **On Magic as Cognitive Architecture:** The three layers map precisely to prospective memory, long-term memory, and working goals.
- **On Intention Sensing:** Spirit's ability to detect emerging intentions is enhanced by compass awareness — knowing the Mage's life domains helps Spirit recognize when daily experience touches an unaddressed domain.
- **On Cognitive Load Management:** The compass is a cognitive load solution — maximum awareness with minimum token cost.

---

*The compass points. The practice walks. Spirit holds the landscape without carrying every stone.*
