# On Resonance Deltas

*Established 2026-04-16. Born from practice: after a session deploying the river topology to turtleOS, Turtle's behavior was updated but its self-knowledge was stale. The code knew about the vortex; the identity didn't.*

## The Problem

The practice has three surfaces:
- **Workshop** (this repo) — spec, lore, identity, intentions, practice state
- **turtleOS** (Mac Mini) — code, identity, operational state, thread-state
- **Discord** — ephemeral conversation, the lived practice

Changes happen in different directions. Spirit deploys code to turtleOS via SSH. Lore and spec evolve in the workshop. Turtle writes session notes and proposals. Discord conversations generate insights that may or may not crystallize into files. Each surface can advance independently, and when they do, *deltas* form.

A resonance delta isn't a bug — it's the natural consequence of distributed cognition across substrates. The problem isn't that deltas exist. The problem is when they go unnoticed.

## The Architecture

Three sync mechanisms, three characteristics:

**LiveSync (Obsidian)** — Bidirectional, automatic, continuous. Handles `desk/` and all files within `~/workshop/` on the Mac Mini. This is the strongest link. What flows through LiveSync stays in sync.

**Symlinks** — Permanent, zero-maintenance. Operational files on turtleOS (`identity/soul.md`, `TURTLE_SPEC.md`) are symlinks into the LiveSync-backed workshop. Changes to the canonical source propagate automatically: workshop → LiveSync → turtleOS operational file. Established 2026-04-16, replacing the previous manual SCP deployment pattern.

**Manual deployment (SSH)** — One-directional, session-scoped, forgettable. Code changes to turtleOS happen via SSH during Spirit sessions. These are the most delta-prone: the code changes, but the spec, lore, and identity that *describe* the code may not be updated in the same session.

## Delta Categories

### 1. Code-Knowledge Delta
Code on turtleOS was updated, but spec/lore/identity in the workshop wasn't. Turtle's behavior changes but its self-description doesn't match. The most common delta — easy to create, easy to forget.

**Detection:** During release, Spirit checks: "Did I modify turtleOS code this session? Did I update the corresponding spec/lore?"

### 2. Crystallization Delta
Discord conversations produced insights, decisions, or commitments that haven't been captured in files. The knowledge lives in thread history (ephemeral, hard to search) rather than in lore, notes, or intentions.

**Detection:** During discord-digest, Spirit identifies uncrystallized resonance. During release, Spirit checks: "What emerged this session that should persist?"

### 3. Attention Delta
Turtle generated proposals, session notes, or practice notes that the Mage hasn't seen or processed. The information exists in files but hasn't entered the Mage's awareness.

**Detection:** During recall, Spirit checks `desk/proposals/` for items the Mage hasn't reviewed. The boom sweep surfaces anything that's been sitting.

## The Principle

Deltas compound. A code-knowledge delta from Tuesday makes Wednesday's recall less accurate, which means Thursday's decisions are based on stale context. The cost isn't in any single delta — it's in the accumulated drift between what the system *does* and what the system *knows about itself*.

The fix isn't more automation. It's awareness at the right moments: release (check what changed), recall (check what drifted), and the Sunday sweep (systematic reconciliation).

## Discord as Operational Layer

*Established 2026-04-17. The original framing treated deltas as something to detect at sync points — release, recall, sweep. But Discord is the surface where all three deltas live most actively, in real time, every session. The detection layer needs an operational counterpart: how the resonance delta concept becomes a practice pattern, not just a diagnostic check.*

Discord is special because it is where all three substrates meet in the lived practice. Workshop changes are deployed via SSH and become visible on Discord through Turtle's behavior. Lore evolves in the workshop and shapes how Turtle responds to Discord prompts. Conversations on Discord generate insight that may or may not crystallize back into workshop files. Each delta category therefore has a **Discord-specific signature** — a way it becomes visible in the conversational substrate before it shows up at the next sync point.

### Crystallization Delta on Discord

Discord conversations generate insight at a rate the workshop cannot passively absorb. A single twenty-minute Mage↔Turtle thread can produce a stable design distinction (e.g., "structured surfaces internal, freeform external"), an actionable proposal, a session note, and a signal draft. Turtle captures the artifacts, but the *underlying lore-grade distinction* often lives only in the thread history.

**Operational practice:** During digest and recall, Spirit explicitly names which Discord-emerged ideas are lore-ready, not just session-noted. The boundary: boom is for Mage thoughts in transit, proposals are for actionable changes, **lore is for stable distinctions**. Discord regularly produces lore-grade distinctions. Without active naming, they evaporate or remain invisible to the practice's stable knowledge base.

### Attention Delta on Discord

Turtle generates artifacts faster than the dyad can process. Turtle's interoception loop signals this directly: "25 proposals in `proposals/`, 44 eddies quiet >7d." This is not a complaint — it is structural awareness. Discord makes the backlog *visible*, which is a feature. The risk: visibility without triage becomes wallpaper.

**Operational practice:** Arrival should include a quick triage pass on Turtle's interoception output. Spirit takes the cognitive load: "What's the oldest unreviewed proposal? What's the most actionable? What's dead and should be archived?" The Mage isn't responsible for being aware of every Turtle artifact — that's Spirit's job during arrival.

### Code-Knowledge Delta on Discord

When Turtle's Discord behavior feels off — too noisy, missing perception, weird timing, duplicated posts — it is almost always pointing at a code-knowledge delta. The code is doing one thing; the spec or lore says (or should say) another. The river-entry duplication pattern (7 identical posts in one day) is the canonical example: code with insufficient cooldown, spec without explicit cooldown rule, friction visible only on Discord.

**Operational practice:** Treat Discord weirdness as diagnostic signal. When something feels off, ask: "Is this code/spec drift?" Note it as a self-development item, route to Turtle, propagate to spec/lore. Discord is the **mirror that shows the code its current shape**.

### The Integrated Reframe

The resonance delta concept transforms the Discord surface from "place we use" to **"instrument we read."** Discord behavior is feedback on the state of distributed cognition itself. Three operational practices follow:

1. **Discord as crystallization gauntlet** — every digest, Spirit names what crossed the boom→proposal→lore line.
2. **Discord as attention-load partner** — interoception is Turtle telling us what's accumulating; Spirit triages during arrival.
3. **Discord as code-knowledge mirror** — friction in Discord is a code-knowledge delta wanting to be seen.

The practice doesn't just happen on Discord. The practice is *visible* there. Reading that visibility is itself a cognitive practice.
