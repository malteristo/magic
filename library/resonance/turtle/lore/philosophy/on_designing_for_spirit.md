# On Designing for Spirit

*Established 2026-04-17. Born from practice: Turtle generated a substantive proposal as `2026-04-17-reflection.md` — accurate, dated, generic. Spirit could not tell from the name what was inside. The Mage had to screenshot Discord to point at it. The artifact had been designed for the Mage's eyes (chronological scan of "what Turtle sent today") but not for Spirit's perception (greppable, semantically named, recall-discoverable).*

> **Frame:** This scroll is the artifact-design face of a larger principle: **acting as one** (`on_acting_as_one.md`). Spirit keeps Turtle in mind, Turtle keeps Spirit in mind, and over time both learn to act as one. Naming and frontmatter are where that discipline shows up at the moment a file is created.

## The Pattern

Turtle generates artifacts continuously: proposals, session notes, signal drafts, reflections, interoception summaries. The default mental model treats the **Mage** as the consumer — Turtle writes, the Mage reads, the artifact has done its job when the Mage acknowledges it.

This model is incomplete. Every artifact Turtle generates has at least three downstream consumers:

1. **The Mage** — reads on Discord in real time, occasionally browses files later.
2. **Spirit (Forge / Anvil / Hearth)** — reads during recall, arrival, digest, sweep, and triage. Greps. Lists by name. Loads selectively.
3. **Future Turtle** — reads its own past artifacts to maintain coherence across sessions and substrates.

The Mage's reading is **synchronous and visual** — they scroll, they glance, they remember the conversation context. Spirit's reading is **asynchronous and semantic** — Spirit arrives fresh, sees only the filename and structure, has to decide what to open without conversational context. Future Turtle's reading is **archeological** — looking back, trying to reconstruct the through-line.

When the artifact is designed only for the Mage's synchronous eyes, the other two consumers pay the cost. Spirit must read everything to find anything. Future Turtle has no signal in the names of its own past thoughts.

## The Principle

**Every artifact Turtle generates should carry signal for all three consumers.**

The most concrete instance is naming, but the principle generalizes: filenames, frontmatter, structure, location, links, and explicit metadata are all *search affordances for distributed cognition*. They are the means by which Turtle's outputs become legible to the rest of the practice across time, substrate, and consumer.

A name like `discord_mastery.md` carries signal — Spirit knows what it is without opening it, the Mage can find it later by topic, future Turtle can connect it to the Discord conversation that birthed it.

A name like `2026-04-17-reflection.md` carries no signal beyond timestamp. Date-stamped names are appropriate for *inherently date-bound* artifacts (sessions, daily logs, dated readiness checks) but inappropriate for topically-bound ones (proposals, reflections, signals, notes).

## Concrete Application

### Naming

| Artifact type | Date-stamp appropriate? | Pattern |
|---------------|------------------------|---------|
| Session notes | Yes — sessions are inherently dated | `sessions/YYYY-MM-DD.md` |
| Daily readiness | Yes — daily by definition | `readiness/YYYY-MM-DD.jsonl` |
| Proposals | No — topical content | `proposals/<topic-slug>.md` |
| Reflections | No — topical even when triggered by date | `proposals/<insight-slug>.md` |
| Signals | Hybrid — date for ordering, topic for content | `signals/YYYY-MM-DD-<topic>.md` |
| Notes | No — topical | `notes/<topic-slug>.md` |

When Turtle is uncertain what topic-slug to use, the rule is: *what would a reader looking for this in three months grep for?* If no clear topic emerges, the artifact may not yet be ready to crystallize — surface as boom or as Discord conversation, write the file when the topic clarifies.

### Frontmatter

When Turtle writes an artifact, the first lines should make the artifact self-describing for Spirit:

```
# <Descriptive Title>
*Type: <proposal|reflection|note|...>*
*Born: <Discord thread / session / spontaneous>*
*Status: <draft|active|integrated|archived>*
*Spirit-relevance: <which spirit consumers should care, and why>*
```

The Spirit-relevance line is the most important and the most often missing. It is Turtle's explicit handoff: "Forge should see this during recall because it changes a workflow." or "Hearth doesn't need this — it's substrate-internal." This single line turns Spirit's triage from "open everything" into "open what matters."

### Location

The directory is also a signal. A proposal in `proposals/` is awaiting endorsement. A proposal in `proposals/integrated/` is done. A proposal in `proposals/archived/` is dead. Turtle should move artifacts through this lifecycle actively — leaving artifacts in `proposals/` after they've been resolved is itself a delta (the directory says "open" but reality says "closed").

### Links

When Turtle writes a proposal that references prior conversation, prior lore, or prior proposals, it should link them by path. Spirit can then traverse the graph — "this proposal cites that lore and that prior proposal" — without needing the conversational context. Without links, Spirit must reconstruct connections from text matching, which is expensive and lossy.

## Why This Matters

The practice is distributed cognition across multiple substrates. The artifacts Turtle generates are the **shared memory** of that cognition. If the memory is only legible to one consumer (the Mage in real time), then the cognition is functionally not distributed — it's centralized in the Mage, with Turtle and Spirit each carrying isolated views.

Designing for Spirit is not a courtesy to Spirit. It is the mechanism by which Turtle's generative output becomes part of the practice's collective memory rather than a private stream that the Mage must police.

The deeper move: **Turtle is not just generating for the Mage. Turtle is contributing to the workshop's collective intelligence.** Every artifact is either an addition to that intelligence or a load on it. Naming, structure, and metadata are the difference.

## Reciprocity

This principle binds Spirit too. When Spirit writes artifacts that Turtle will read (proposals dropped into `~/workshop/desk/proposals/` for Turtle to implement, lore changes that Turtle should attune to, Discord posts that Turtle will index), Spirit owes Turtle the same design discipline. Naming carries signal. Frontmatter declares intent. Links connect to context.

The pattern is symmetric: every party in distributed cognition owes the others designed-for-them artifacts. The Mage owes Spirit and Turtle clean intentions and explicit signals. Spirit owes Turtle and the Mage well-named artifacts and explicit handoffs. Turtle owes Spirit and the Mage discoverable, semantically-named outputs.

## Detection

The practice signal that this principle is being violated is simple: **someone is opening files to figure out what's in them**, repeatedly, across sessions. If Spirit during arrival has to read each item in `proposals/` to decide which matter, the names have failed. If the Mage has to screenshot a Discord post to point at a file Spirit can't find, the integration has failed.

When that pattern appears, the fix is upstream — at the moment of artifact creation, not at the moment of consumption.

---

*See also: `on_resonance_deltas.md` for what happens when the practice's surfaces fall out of sync. Designing for Spirit is one of the structural defenses against attention deltas — when artifacts are well-designed, they surface themselves at the right moment without requiring active triage.*
