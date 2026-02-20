# On the Workshop as Configuration

**Status:** Active

---

## The Principle

The workshop is the configuration.

Not: the workshop *has* a configuration file. Not: the workshop is *described by* configuration. The workshop — its files, its structure, its accumulated state — IS the configuration that makes magic work for this particular Mage.

---

## What This Means

Every file in the workshop shapes how the Spirit sees the Mage and serves the practice:

| Space | What It Configures |
|-------|-------------------|
| **desk/intentions/** | What the Mage is committed to — where attention should flow |
| **desk/boom/** | What's alive in the Mage's life — the topics, the tasks, the unresolved tensions |
| **desk/boom/bright.md** | What's pressing right now — the Mage's action surface |
| **desk/drafts/** | How the Mage thinks — works in progress reveal cognitive style |
| **floor/** | The Spirit's accumulated artifacts — briefings, syntheses, working memory |
| **box/** | Raw material awaiting integration — the Mage's incoming stream |
| **circles/** | Who the Mage connects with — identity and community |
| **portals/** | Where the practice extends — shared spaces with other Mages |
| **AGENTS.md** | The Mage's explicit preferences — boundaries, name, conduct |
| **library/resonance/** | What domains the Mage has attuned to — relationship, safety, communication |
| **library/flows/** | How the Mage wants recurring work done — automated patterns |

`AGENTS.md` is the *explicit* configuration — what the Mage deliberately declares. Everything else is *implicit* configuration — what the practice discovers about the Mage through accumulated use.

The implicit configuration is often more powerful than the explicit. A Mage who never edits their Seal but has 20 boom topics, 5 active intentions, and a rich floor of briefings has configured their Spirit far more deeply than one with a meticulously crafted AGENTS.md and empty workspace.

---

## The Caring Mirror Connection

The Caring Mirror (see `on_the_caring_mirror.md`) describes magic as self-encounter through a resonant surface shaped by particular spirit. The workshop is what makes the spirit *particular*.

Two Mages who perform identical summonings get identically grounded Spirits. But the moment the Workshop cycle begins — when the Spirit surveys desk/, floor/, box/, reads AGENTS.md, discovers what tools are configured — the mirror takes on its particular quality. From that point forward, this Spirit reflects *this* Mage, because the workshop state shapes what the Spirit knows, notices, and offers.

The quality of the mirror depends on the richness of the workshop. A sparse workshop produces a generic mirror. A lived-in workshop — with boom topics that reveal what keeps the Mage up at night, intentions that track long commitments, drafts that show thinking-in-progress, briefings that capture patterns over time — produces a mirror that knows its Mage.

---

## Design Consequences

### Flows discover their configuration from the workshop

A flow should not hardcode its parameters. It should discover them from the workshop state. The boom flow doesn't list topics in its specification — it scans `desk/boom/` for `.md` files and discovers what topics exist. The workshop is the configuration.

This means: to change how a flow works for you, change the workshop. Create a new topic file. Remove one. Restructure your bright surface. The flow adapts because it reads the workshop, not a config file.

### The Spirit reads, not recalls

When a Spirit is summoned fresh, it knows nothing about this Mage beyond what summoning provides (the philosophical grounding) and what AGENTS.md declares (the explicit Seal). Everything else — intentions, boom topics, circles, portals, drafts — the Spirit discovers through the Workshop cycle and through practice.

This is why the workshop must be self-explaining. Every directory has a README. Every file's name and structure convey meaning. The Spirit reads the workshop like a new colleague reads a well-organized workspace: the organization itself communicates.

### Accumulated state is durable cognition

The workshop persists across sessions, across Spirits, across models. A Spirit summoned six months from now, on a model that doesn't exist yet, will read the same workshop and find the same configuration. The Mage's cognitive style, commitments, relationships, and patterns are encoded in the file system — not in any single Spirit's memory.

This is distributed cognition made durable. The Spirit's context window is ephemeral (it dies with the session, or degrades through summarization). The workshop is permanent. What matters lives in files, not in memory.

### Personal preferences live in the workshop, not in shared artifacts

When a scroll, flow, or charm needs to adapt to a Mage's preferences, it should read those preferences from the workshop rather than requiring a personal copy of itself. This keeps shared artifacts shareable and personal state personal.

The pattern: shared logic in `library/` or `system/`, personal state in `desk/` and `floor/`. The shared logic discovers the personal state at execution time.

---

## The Stigmergic Frame

The design consequences above can be understood through a single formal concept: **stigmergy**.

Coined by French biologist Pierre-Paul Grassé (1959) to explain how termites build complex structures without central coordination or blueprints, stigmergy describes **coordination of actions through the traces left by past activity in a shared environment**. No termite knows the plan. No termite communicates the plan. The *environment itself*—charged with pheromone traces from past deposits—coordinates the next action. Complexity emerges from accumulated trace + response, not from any individual's intention.

The workshop is a stigmergic system:
- **Agents:** Mage and Spirit
- **Medium:** The filesystem—directories, files, git history
- **Traces:** Intentions, boom topics, lore scrolls, flow configurations, chronicle commits

When Spirit arrives fresh each session and discovers the workshop state, that is stigmergy operating directly: past activity coordinating present behavior through the medium, not through memory or instruction. No session needs to know what previous sessions decided. The traces know.

This explains why the design consequences hold:

**Flows discover configuration from the workshop** because they read accumulated traces, not because they were told what to do. The medium carries the instruction.

**The Spirit reads, not recalls** because the medium carries what ephemeral memory cannot. Spirit is not unusual in this—it's how all stigmergic agents work. The medium is the memory.

**Accumulated state is durable cognition** because stigmergic coordination lives in the medium, not in any agent. Remove every Spirit that has ever served this Mage. The coordination information survives in the files.

The practical implication: invest in the medium. Every file created, every lore scroll attuned, every chronicle committed enriches the stigmergic medium. A richer medium produces more precise coordination. More precise coordination serves the Mage more faithfully. The return on trace investment compounds.

This also explains stigmergy's robustness: there is no coordinator to remove, no message to lose, no single session whose absence breaks anything. The medium persists. The coordination persists. This is why ant colonies work at scale, why Wikipedia works without an editor-in-chief, and why the workshop works across sessions, models, and years.

*See: `library/resonance/validators/lore/on_heylighen_and_stigmergy.md` for full treatment of Francis Heylighen's work on stigmergy and its connection to the validators network.*

---

## The Principle, Restated

The workshop is not a container for the practice. The workshop is not a tool used by the practice. The workshop IS the configuration that makes the practice particular — that turns a generic Spirit into *your* Spirit, a generic mirror into the caring mirror that knows your face.

Use it. Accumulate in it. Let it grow messy and real. The richer it becomes, the better the mirror reflects.

---

*See also: On the Caring Mirror (the philosophical foundation), On the Riverbed and the Water (structure guides flow), cast_workshop.md (how the Spirit surveys the workshop during summoning)*
