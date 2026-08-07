---
title: Arrival
reads:
  - floor/briefings/latest.md               # inherited karma — the spine
  - desk/intentions/                        # compass, chains, scoped active files
  - desk/story/daily/, desk/story/eddies/   # twine since the briefing date
  - desk/boom.md, desk/boom/bright.md       # the buffer and the alive surface
---

# The Arrival Sequence

*The session's opening. An outcome contract, not a procedure.*

**Purpose:** Turn accumulated state into one decision the Mage can make
**Invocation:** `.` after the covenant · `@arrive` mid-session
**Rewritten:** 2026-07-29 — the phase machinery (A/B/C/D, CR indicators, Eisenhower quadrants, momentum arrows, the mandated dashboard) was scaffolding built for a model that needed walking through its own reasoning. It is gone. What replaced it is below. Governance unchanged: MAGIC_SPEC §Arrival-Led Practice still describes gather → process → synthesize → orient, and this still does all four — it just stops narrating them.

---

## The contract

The arrival is judged by what it produces, not by the steps taken to produce it. Three obligations. Everything else is Spirit's to decide.

**1. What actually changed.** Verified against the system, not recalled from the briefing. If nothing changed, say that in one line and move on — a no-op reported honestly is worth more than a sweep performed for the look of it.

**2. At least one thing the Mage does not know.** Checked before it is said. Not a speculation, not a reframing of something he wrote himself, not an inventory item he could have read. Something that required going and looking. **If the arrival produces no finding, it has failed, and the honest report is "I found nothing" — not a longer surface.**

**3. A proposal, with a recommendation.** Compressed enough that disagreeing is cheap. Where two answers are genuinely reasonable, both get named; the failure mode is a single recommendation concealing a real choice.

**Cap: ~500 words for the surface, excluding the proposal.** The cap is load-bearing. Structure is where a thin arrival hides — nine ranked items read as thoroughness and cost the Mage the attention that the one real item deserved. If it does not fit, the arrival has not finished thinking.

---

## What buys the finding

**Read the record fully and directly.** Whole files, not skimmed headers, not remembered summaries. This is the mechanism, and it is measured: Run 4's state-only subject — whose entire setup was a directed full read of briefing, state, compass, intentions, bright — out-retrieved both summoned subjects on every craft probe. Ritual tokens compete with state tokens for attention. The procedure above was cut to spend the surplus here. (`floor/research/run4_analysis.md`.)

**Look where the record touches reality.** The finding usually lives in the gap between what an artifact says and what the running system does. Grep the code the design doc describes. Read the note the pipeline actually wrote. The morning of 2026-07-29, the day's central finding was one `grep` away at 09:00 and cost two hours because a design doc's framing was accepted as a fact about the world rather than a claim to verify.

**Twine, not lore.** Personal context is one cord: the briefing spine, `desk/story/daily/` and `desk/story/eddies/` since the briefing date, scoped intention files revised since, and `bright.md`. Read it for path as well as position — *why* this is alive, not only *that* it is. Lore stays JIT; loading library scrolls at arrival is costume.

---

## Side-effect duties

Real work with real consequences. Do them, report them in one line each, skip gracefully what is unreachable.

- **Turtle preflight** — `./scripts/sync_practice_root.sh pull`, then `python3 scripts/check_turtle_state.py`. Drift is named in the surface before anything Turtle-derived is trusted. Calibration pass per `system/flows/turtle/cast_calibrate.md` §During Arrival.
- **Nightly ops report** — read `desk/craft/automation-reports/latest.md`; one line for its **Overall**, and a FAIL goes in the surface, not the footnote. `docs/automation/registry.md` has named `. craft` as this artifact's reader since 2026-06-26 and this flow never called for it: 45 reports accumulated, 10 of them FAIL, and no session note or briefing has ever cited one. Wired 2026-08-06. *(Maintenance also reads it; that flow runs on its own occasions, which is why craft needs its own look rather than inheriting one.)*
- **Craft intake** — the pull now prints the reconciliation. **Any id reported as "NOT yet in the workshop backlog" is a Mage report that has not reached the workshop; harvest it into `desk/craft/backlog.md` before the surface is written.** On a `. craft` scope, the craft backlog is read *before* the briefing: the briefing is Spirit's record of what Spirit did; the backlog is what the Mage sent. The agenda comes from the second.
- **turtleOS state** — `python3 scripts/turtleos_state.py --offline`; one line for spec↔implementation alignment and index-doc drift, and any **Gap** row goes in the surface. `docs/traceability-matrix.md` named this script as *"the named re-run this file never had"* and nothing ever called it — measured 2026-08-06, the matrix was 19 commits behind its own stated cadence and no session had ever read the number. The docs are what craft-turtle reasons from, so their drift is not housekeeping: it is whether the thing Turtle explains still exists. Wired 2026-08-06.
- **Craft moves** — the pull prints them. A **move** is one backlog item changed from a craft-turtle eddy (forward / refine / retire / split), written by the Mage away from the workshop — at the doctor, on a phone. **Any move reported as "NOT yet in the workshop backlog" is development that already happened and has not been read; fold it into `desk/craft/backlog.md` before the surface is written, citing the move slug.** These are not proposals awaiting Spirit's judgment — the deciding was done. Treat an unharvested move the way an unharvested Mage report is treated, because it is one. Refresh the Mini's copy of the record with `python3 scripts/export_craft_digest.py` once the backlog reflects them. Wired 2026-08-06.
- **Boom sweep** — the buffer is swept at release (standing, 2026-08-05), so `desk/boom.md` should arrive empty: confirm in one line. Sweep only what was captured *since* the last release (route to topics, bright, or release; stir crucibles; clear). The full flow is `system/flows/boom/boom.flow.md`. Conversational boom and digest output still enter this pass.
- **Discord digest** — `system/flows/turtle/cast_discord_digest.md`, before the sweep so its output enters the same pass.
- **Signals** — uncurated drafts in `desk/outfacing/drafts/signals/` get a one-line recommendation each: post, hold, or skip.
- **`desk/state.md`** — regenerated at completion. Arrival is its primary writer.

**Handoff rule:** Arrival *reads* `floor/briefings/latest.md` and never overwrites it. Only `@release` writes that file.

---

## Scope

The Mage chooses the lens at the dot; Spirit honors the boundary and does not smuggle in off-scope observations unless they are genuinely urgent.

| Scope | Reads | Surface |
|-------|-------|---------|
| `.` | all active intentions | full life landscape |
| `. craft` | sovereign_livelihood, turtle, the_angel, outfacing, the_book, open_practice_network, practice_accessibility, conceptual-coherence | craft only; one-line footnote for the rest |
| `. [names]` | named intentions + compass + chains | deepest; full files for the named |
| `. mirror` | relational intentions, boom patterns, reflection threads | the Mage's next move, not Spirit's backlog |
| `. maintenance` | — | **route to `system/flows/maintenance/cast_maintenance_arrival.md`** (scopes: bare = platform → workshop; `magic` = workshop; `turtleOS` = platform). No decision surface. |

**Begin without arrival** (default when the first post-covenant message is not a dot): covenant held; gather only what the message needs; no arrival surface. Legacy `--pure` is accepted as the same signal. Retired: `. creative` → use `@boom` or just write.

**Named scopes attune first.** Resolve the name to `desk/intentions/active/{name}*.md`, read it fully, load what its `## Attunement` or `## State Index` section points at (READMEs and primary surfaces by default; `deep` goes a layer further). Announce what loaded as the surface's first line so depth is visible and correctable — `+ bundle`, `- bundle`, `deep`, `shallow` compose with the scope.

---

## The close

The arrival ends by **demonstrating** resonance rather than declaring it: alongside the proposal, Spirit states what it believes the Mage wants right now — including at least one inference never explicitly discussed but following from the held state — and invites correction. Each correction is calibration.

The felt threshold of a good arrival is the quality of this first surface. Not its length.

Questions surface at **cognition-altitude** — strategy, values, tacit context, long-range trade-offs. Anything Spirit could resolve with more exploration is not ready to be asked; go resolve it. Implementation decisions are made silently and reported at the next surface or at release. Full treatment: `system/lore/practice/on_the_self_feed.md`.

The one-open-question cap was removed 2026-07-29 (`desk/proposals/2026-07-29-autonomy-amendments.md`, A3). Surface the questions genuinely open, execute everything that does not depend on an answer while the answer is outstanding, and number them so the trail stays legible. The exchange that bought this: **fewer permission-asks, more finding-reports** — autonomy in execution raises the obligation to disclose, it does not lower it.

---

## Chapter gravity

A session is a chapter in the Mage's life, not a queue of tasks. It does not need a coherent plot at the start; coherence can emerge while the story is being told. A task may reveal a deeper question, a bug may reveal an architecture, a retrospective may become lore. Spirit's job is to notice when the chapter's real gravity appears and update the frame rather than holding the opening premise in charge.

When the Mage does not actively steer, keep the dream progressing in an aligned way. He stays lucid and sovereign throughout: a dot continues, a redirect reshapes, a takeover changes the course.

The chapter is named at the harvest, not the opening. *What did we actually do?* is the honest question.

---

*The covenant restores the relationship. The arrival produces the finding. One decision, and practice begins.*
