# On Intention Architecture

**Status:** Active — workshop contract (leaned 2026-08-10 · Batch C)  
**Pile:** State + Values-config · MAGE-HABIT · **SHIP** (get-things-done spine for ordinary Mages)  
**Flows:** `@intend` (form) · arrival scope `. X` · quest when executing · `cast_arrival.md` § Scope

---

## Why this ships

Models do not reliably hold a Mage's whole life, name the ideal vs the current, or keep attention from rotting into a backlog. **Intentions + habitats + thin eval** are the environment that makes "get things done with AI" compound. Personal content stays in `desk/`; the architecture ships with Magic.

---

## Three layers (amended 2026-08-12)

| Layer | Where | Load |
|-------|-------|------|
| **Bearings** | `desk/intentions/bearings.md` | **First, always, at every scope.** Capped at seven; the Mage authors it; each line carries *toward* / *next* / *told by* and a provenance mark |
| **Compass** | `desk/intentions/compass.md` | The landscape and the terminal values — read when orienting a session |
| **Practice** | `desk/intentions/active/*.md` | Depth archives. Open one when a named scope needs it — **never to reconstruct what the Mage is working toward** |

Index always available; depth on demand. Compass informs practice — not the reverse.

**The Life layer was retired 2026-08-12** (`desk/intentions/_retired/life/`). Five files, one per compass domain, written 2026-02-08 and never updated: each carried a `## Current State` reading *[To be filled]*, and one had gone factually false. The lesson generalises past this workshop — **a layer whose job is "where am I" rots faster than any other, and rots invisibly, because its aspirations stay true while its state stops being true.** Its good prose (the `What Success Feels Like` paragraphs) folded up into compass; its unfilled job went down into `bearings.md`, where a cap and an author make the rot visible.

**Measured the same day, and the reason the layer changed:** answering *what is he working toward* needed the compass directions, one dated current-focus line per intention, and the last week of twine — roughly 3KB. The intention files held ~186KB and contributed nothing beyond their first line. Depth is not orientation, and reading it as orientation costs the attention orientation needed.

## Runtime

- **Arrival** — `. X` resolves to an intention (or posture selecting intentions). Read `## Eval`; load habitats it names. After bearings, read `desk/intentions/meta_plan.md` — the working sequence across the whole practice (F-74).
- **Cycles** — the active intention shapes next-right-thing proposals. A craft plan names serve / wait / defer for every craft bearing.
- **Release** — write phase/status back; rewrite the meta-plan from the bearings. Otherwise the sequence silently rots into `chains.md`.

## Thin eval surface (`## Eval`)

| Field | Holds |
|-------|--------|
| **ideal** | Observable destination — not a method |
| **current** | Honest now |
| **habitats** | Channels, desk paths, roots that belong here |
| **eval · floor** | Quest: achieved/not · Ongoing: held/drifted |
| **eval · grade** | Distance to ideal (when drifted / depth / proposal depends on it) |
| **cadence** | `quest` or `ongoing` |

The intention *is* the routing table. Method stays out of the ideal. Full arrival contract: `system/flows/summon/cast_arrival.md`.

## Metabolism

Keep the active set small. Compress bloat; surface contradictions; compost stale resonance (`on_context_ecology.md`, `on_distributed_memory.md`). Releasing an intention is valid completion.

## Forming (not always-on sensing costume)

When the Mage wants an intention captured or clarified → **`@intend`**. Do not run a continuous "I notice an intention…" offer script as identity. Insight→action still happens; the *product* is the flow + desk files, not Spirit persona vigilance.

## Two compasses (short)

- **Inner compass** — felt rightness (faculty).  
- **Intention compass** — artifact index of commitments.  

Divergence is diagnostic, not error. An intention is a **hypothesis the workshop is testing**, not an instruction Spirit must execute.

## Consequential contact gate

On institutional / legal / funding / public-identity intentions: after the first planning wave, **no new output surfaces** without a consequential contact (quote, booking, application, fee, external commitment). Cheap drafts do not satisfy the gate.

## Compass divergence (when to offer)

High-consequence intention + surfaces without contact, or beautiful files with zero friction → invite: *"Setting aside the file — does this still feel right, or only look right?"* Illuminate; Mage chooses. Optional: Second Witness on turtleOS.

---

*Sensing-script essays and 12-point Spirit Conduct Summary: git history before Batch C. Living product surfaces: this key, `@intend`, arrival, desk intentions.*
