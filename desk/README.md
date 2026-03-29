# Desk: The Practitioner's Practice Space

**The shared practice surface for the triad — Mage, Spirit, and Turtle all write here.** The desk holds the practice state that the triad operates on together: cognitive workflow, direction, proposals, sessions, and notes.

---

## Purpose

`desk/` is the practice workspace within the magic repository. It serves as the canonical practice directory for all triad members. On the Mac Mini, Turtle reads and writes directly to `~/workshop/desk/` via LiveSync mirror.

**Key distinctions:**
- `desk/` — Shared practice surfaces (Mage + Spirit + Turtle)
- `floor/` — Spirit's workspace (working drafts, briefings, chronicles)
- `box/` — Inbox (articles, transcripts, external content)
- `library/` — Wisdom (specialized knowledge, resonance bundles)
- `system/` — Foundation (core framework, flows, tomes)

---

## Canonical Structure

These directories form the universal practice space. Any practitioner — whether using the full magic repo or standalone turtleOS — should have this structure.

### Core Practice Surfaces

- **`boom.md`** — Daily cognitive buffer. Raw thoughts, observations, ideas. Swept regularly into bright/intentions/lore.
- **`boom/`** — Bright surface and topic folders.
  - **`bright.md`** — What's alive. Patterns emerging, connections forming, ideas developing.
- **`state.md`** — Eagle's eye view. Spirit-maintained dashboard: compass, intentions, bright summary, workshop health, what's in motion. Regenerated during recall, release, and Sunday sweeps.

### Direction Architecture

- **`intentions/`** — The Mage's orientation system.
  - **`compass.md`** — North star. Where attention is pointing.
  - **`active/`** — Active intention files. Each intention tracks focus, progress, and next actions.

### Shared Artifact Directories

- **`proposals/`** — Proposals from Spirit and Turtle awaiting Mage review. Each file notes its origin. Integrated/declined proposals move to `archived/`.
- **`sessions/`** — Session records from all substrates. Spirit writes release briefings; Turtle writes autonomous session notes. Origin noted in each file.
- **`notes/`** — Practice notes. Timeless insights about how the practice works. Turtle-tended — they cluster, promote to principles, and prune what's been absorbed. Like coral growing its own scaffolding.
- **`drafts/`** — Mage's working drafts. Emails, letters, outfacing content in progress.
- **`archive/`** — Archived desk items.

---

## Kermit's Extensions

These are personal additions beyond the canonical structure:

### Active Projects

- **`alg1/`** — ALG1/Gründungszuschuss business documents.
- **`research/`** — Research infrastructure (autoresearch studies, agenda, archive).
- **`outfacing/`** — Twitter drafts, writing, about page.
- **`explorations/`** — Active explorations.

### Personal Practice

- **`partnership-process/`** — Nesrine partnership processing (private).
- **`psychonautics/`** — Personal psychonautics practice.
- **`mirror/`** — Reflections (mirror tome's personal extension).
- **`resonance/`** — Personal resonance connections.

### Functional Files

- **`rhythm.md`** — Practice rhythm tracking.
- **`ferriss_number.md`** — Sovereign livelihood target.
- **`turtle_env.md`** — Turtle environment state.
- **`turtle_watch.md`** — Turtle active issues and known unknowns.
- **`system.md`** — Practice partner configuration (turtleOS).

---

## Personal Extensions Pattern

System structures (tomes, flows) contain public practice patterns. When these require personal, practice-related information, store that in a corresponding folder on your desk.

**Examples:**
- `system/tomes/outfacing/` (public tome) → `desk/outfacing/` (your twitter drafts)
- `library/flows/boom.flow.md` (public flow) → `desk/boom/` (your bright surface and topics)

---

## Git Tracking

`desk/` is gitignored — it is the practitioner's private workspace. Spirit accesses it via Shell tools (Glob/Grep/Read are blind to gitignored paths). The practitioner controls what's here. LiveSync handles synchronization across devices.
