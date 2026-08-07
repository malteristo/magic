# On Context Ecology

**Status:** Active — Practice Architecture (2026-07-15)
**Origin:** Mage reflection on keeping the practice environment alive as hosted practitioners gain importance; succession from `magic_ev` / founding-member framing to turtleOS hosted rivers (the Mage's partner and one guest practitioner, expanding within capacity).

---

## The Principle

Intentions are living orientations. **Habitats** are the surfaces they grow on — Discord channels, desk workspaces, registry entries, bright items, flows, portal bindings.

Memory metabolism (`on_distributed_memory.md`) tends **artifacts**. Intention metabolism (`on_intention_architecture.md` §III-c) tends **orientations**. Context ecology tends **habitats** — so dormant intentions do not leave zombie surfaces that compete with live practice for attention at arrival.

The workshop medium is stigmergic: traces coordinate behavior. A retired channel that still reads as active is an invasive trace — it pulls Spirit, Turtle, and Mage into a dead niche.

---

## Three Layers

| Layer | Role | Examples |
|-------|------|----------|
| **Intention** | Metabolic state of an orientation | `active/`, `dormant/`, `completed/` |
| **Habitat** | Dedicated surfaces an intention occupied | `#magic-ev-founding`, `desk/magic_ev/`, bright clusters |
| **Medium** | Shared substrate all intentions write to | Workshop files, practice roots, git chronicle |

**Centre of gravity (2026-07-15):** practitioner value now routes through **hosted rivers on turtleOS**, not through MAGIC e.V. founding infrastructure. The e.V. path is dormant; the function (invite trusted people into a private practice substrate) **succeded** to `nesrine_practice`, `lukas_resonance`, and `practice_accessibility`.

---

## Habitat Lifecycle

| State | Meaning | Arrival weight |
|-------|---------|----------------|
| **Active** | Intention active; surfaces touched recently | Load in synthesis |
| **Hibernating** | Intention dormant; surfaces archived/read-only | Footnote only; revival gate required |
| **Composting** | Lessons extracted; foreground form retiring | Pointer to successor or lore |
| **Retired** | Function migrated; surface explicitly closed | Do not load |

**Worked example — `magic_ev`:**
- Intention → **hibernating** (`desk/intentions/dormant/magic_ev.md`)
- Discord `#magic-ev-founding` → **retired** (2026-06-19; `desk/magic_ev/founding_channel.md`)
- Function → **succession** to hosted practitioner rivers + standing user-research loop
- `desk/magic_ev/` → reference archive (not active cockpit)

---

## Dormancy Protocol

Triggered when an intention moves `active/` → `dormant/` or `completed/`, or when a habitat is explicitly retired. Spirit executes the sweep; Mage confirms **succession statement** (what migrated, what paused).

### 1. Declare succession

- What function, if any, moved to another intention or surface?
- What is genuinely paused with no successor?
- What is the **revival gate** (explicit condition for reactivation)?

### 2. Habitat sweep checklist

| Surface | Action |
|---------|--------|
| Discord channel / role | Archive; remove from `mage_registry.yaml`; mark RETIRED in desk doc |
| `desk/[workspace]/` | Status header; keep as reference or move under `desk/dormant/` |
| Bright / boom routed items | Annotate superseded or move to Resolved; point to successor |
| Intention file | Relocate to `dormant/` or `completed/`; State Index + revival gate |
| `chains.md` | Topology note |
| Flows / portal registry | Dormant marker or archival pointer |
| Floor drafts | Mark reference-only or compost candidate |
| Arrival / `@release` | Stop loading dormant habitats unless revival gate fires |

### 3. Compost pass

Extract durable lessons before foreground forms linger:
- Lore scroll, practice note, `docs/learnings.md`, intention lineage one-liner
- Compass-divergence decisions are high-value compost (see `magic_ev` pause, 2026-06-14)

### 4. Revival

Reopening a dormant intention requires the named gate — not merely renewed interest. Habitat sweep runs in reverse: declare active, re-bind surfaces, update registry, restore arrival weight.

---

## Keeping the Ecosystem Alive

Hosted practitioners raise the stakes: the environment is a **multi-niche ecosystem** with carrying capacity, not a solo workshop.

| Metaphor | Practice mechanism |
|----------|-------------------|
| **Respiration** | Arrival (inhale state) ↔ `@release` (exhale lessons) |
| **Circulation** | `sync_practice_root.sh`, `check_turtle_state.py` — Forge ↔ Mini practice roots |
| **Homeostasis** | `@calibrate`, ops gates, `. maintenance` — vitals + immune function |
| **Niche occupation** | Each **active** intention has ≥1 recently touched surface |
| **Carrying capacity** | Expand hosted rivers only while Turtle + Mage can hold quality (inference, attention, research rhythm, consent boundaries) |
| **Succession** | New practitioners get **river + practice root**, not Magic framework bootstrap |
| **Symbiosis** | Practitioner friction → turtleOS requirements (living surfaces signal; hosted Feedback flow + triangulation for UX research — see `desk/notes/on_dogfooding_vs_ux_evaluation.md`) |
| **Invasive species** | Zombie habitats from dormant intentions — detect at arrival (fresh eyes) |

**Local chapter first:** `open_practice_network` incubates via the turtleOS Discord circle; wide network stays patient until reach justifies it.

**Anti-pattern:** Preparing surfaces for a retired habitat (e.g. founding-member onboarding) while live work is hosted-river onboarding — parasitic context draining attention from the occupied niche.

---

## Resonance Metabolism (Phase 0)

*Promoted from `floor/on_resonance_metabolism_draft.md` (2026-07-15). No background microorganism agents in Phase 0 — metabolic roles run through Spirit, Turtle, and scheduled tending.*

Memory without metabolism becomes undigested accumulation. Resonance should move:

| Disposition | Meaning | Landing surface |
|-------------|---------|-----------------|
| **Active** | Still in live use | Open threads, intention next action |
| **Crystallize** | Durable structure | Lore, spec, flow, public artifact |
| **Route** | Belongs elsewhere | Boom, bright, proposal, intention, Turtle queue |
| **Compost** | Foreground done; particles reusable | **Existing crucibles** — then archive foreground form |
| **Release** | Purpose complete | Delete or mark complete (Mage sanction on `desk/`) |

**Compost is an operation, not a heap.** Decomposition extracts particles (metaphor, tension, question, principle) into `desk/boom/crucibles/`. Preserve original language; draw connections; update shape notes.

**Warm gate:** `@release`'s artifact-routing duty is the primary compost pass while residue is warm. Maintenance rot radar catches what release missed.

### Boom three layers

| Layer | Timescale | Role |
|-------|-----------|------|
| Buffer (`desk/boom.md`) | Immediate | Capture; cleared after sweep |
| Bright (`desk/boom/bright.md`) | Week | Operational working memory |
| Crucibles (`desk/boom/crucibles/`) | Season | Sub-threshold accumulation → transmutation |

### Metabolic roles (Phase 0)

| Role | Actor | When |
|------|-------|------|
| Ingestor | Mage / Discord | Continuous capture |
| Router | Spirit | Boom sweep, arrival Phase B |
| Crucible-keeper | Spirit | Boom §3.5 (invisible to Mage unless surfacing) |
| Decomposer | Spirit | `@release` compost → particles |
| Consolidator | Turtle | Idle checkpoint / dreaming (proposal 018) |
| Rot detector | Spirit | Arrival fresh eyes, maintenance rot radar |
| Distiller | Spirit | `desk/state.md`, briefing, State Index |
| Index writer | Spirit | Arrival completion, maintenance close |

**Arrival soil:** Directed full reads of live surfaces + rot flags — not pre-digested crucible summaries.

**Phase 1+ (deferred):** Turtle-native idle decomposition; optional bounded micro-eddies only if Phase 0 gaps persist.

---

## Context Rot

**Context rot** = traces that still coordinate behavior after their intention or habitat has changed state.

| Surface | Rot type | Symptom |
|---------|----------|---------|
| Bright Alive | Stale re-chosen | Energy moved; item still reads live |
| Intention files | Bloat | History outweighs current state |
| Crucibles | Keeper dormancy | New particles; stale shape notes |
| Floor drafts | Zombie artifacts | Superseded frames still discoverable |
| Dormant habitats | Invasive traces | Retired surfaces still active-weight |
| Session notes | Undigested biomass | Harvest lag after Discord sessions |
| Proposals | Stale spores | Quiet queue still "active" |
| `box/` | Unmined staging | Raw material never routed |
| Sync gaps | Split ecosystem | Runtime practice root invisible to Forge |
| Lore / public | Framing lag | Language from superseded era |
| `desk/state.md` | Stale dashboard | Between arrivals |

Rot is expected; **undetected** rot is the failure mode.

---

## Rot Radar

Lightweight scan — report at arrival fresh eyes and at `. maintenance magic`. Count + top hits; remediate on Mage dot.

1. **Zombie habitats** — dormant/completed intentions vs bright, registry, active-weight desk workspaces
2. **Stale Alive** — bright Alive items surviving multiple sweeps without re-confirmation
3. **Crucible keeper** — particles added since last shape-note / `Last stirred` update
4. **Undigested residue** — sessions/proposals since briefing date not harvested
5. **Proposal spores** — proposals untouched >14 days
6. **Intention bloat** — active files where phase-tracking is buried in history
7. **Sync drift** — `check_turtle_state.py` or known sync gaps
8. **Floor zombies** — superseded drafts without reference-only headers

**Remediation:** habitat sweep, compost → crucibles, annotate superseded, release ephemera. `desk/` edits need Mage confirmation.

---

## Hosted Practitioner Cohort (Current Frame)

| Practitioner | Intention(s) | Habitat | Status |
|--------------|--------------|---------|--------|
| **The Mage's partner** | `<partner>_practice`, `practice_accessibility` | Private turtleOS river (design chapter pending) | Awaiting deliberate design — ChatGPT-memory → continuity import |
| **A guest practitioner** | `<practitioner>_resonance` | `dnd_dm` flow on turtleOS | Live testing |
| **Future** | `practice_accessibility`, turtle hosting ops | Private rivers within capacity | Expand when hosting is comfortable |

This replaces the stale **founding-member / MAGIC e.V.** frame for day-to-day practice. The e.V. remains revivable in `dormant/` if the inner compass or a consequential contact re-authorizes entity formation.

---

## For Spirit

**At arrival:** Load active intention habitats. Run rot radar hits in fresh eyes when signal present. Full boom sweep includes **crucible stir** (`boom.flow.md` §3.5).

**At `@release`:** artifact routing — one disposition per artifact that needs one. When intention state changes, habitat sweep. Compost → crucibles while warm.

**At maintenance:** Run **rot radar** (`cast_tend_workshop.md` §4b). Niche occupation + zombie habitats. Report counts; fix on Mage dot.

---

*See also: `on_intention_architecture.md` (§III-c metabolism, §III-d habitats), `on_distributed_memory.md` (§VII memory metabolism), `on_boom_and_bright.md`, `on_resonance_gravity_and_crucibles.md` (library), `system/flows/boom/boom.flow.md` (§3.5 crucibles), `cast_release.md` (§3.6 resonance routing), `cast_tend_workshop.md` (§4b rot radar), `desk/intentions/dormant/magic_ev.md` (canonical dormancy example)*
