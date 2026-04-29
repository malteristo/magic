# Release — 2026-04-29 (evening, light)

**Chapter:** Light craft maintenance + release. Phase A.0 spell change chronicled to git; partnership briefing preserved local; the_angel.md cause re-diagnosed (Cursor diff state, not LiveSync); NLnet office-hour questions reframed and posted under 16:00 CEST policy constraint; Turtle conversations from this morning held for a dedicated future chapter.

## This Session

Three threads ran in parallel under `. craft` scope, all completed by light handling.

**Thread 1 — the_angel.md cause correction.** First diagnosis (LiveSync conflict resolution chose empty version) was wrong. Mage recovered the file via Cursor diff revert — full text was still there, marked red as a pending deletion in Cursor's diff state. Different threat model than LiveSync drift: an agent edit (likely from an earlier session) emptied the file at the disk level but Cursor preserved the original content as the "before" state of an unaccepted diff. Recovery worked because Cursor's diff cache outlived the on-disk write. Holistic file-recovery solution endorsed in principle, queued as follow-up.

**Thread 2 — NLnet office-hour questions.** Mage flagged the office-hour policy disclaimer ("we will not be pre-reviewing applications") on the NLnet site 1.5 hours before opening. Original four questions had a project-describing preamble + Q3 sketched the project's transition pattern in concrete terms. Reformulated all four as standalone scope/policy questions: dropped preamble, abstracted Q3's sovereignty-trajectory framing, kept substantive content. Mage posted the reformulated set. Awaiting answers — Spirit will integrate into the NLnet application surface when they arrive.

**Thread 3 — Light maintenance + release.** The afternoon's partnership briefing committed against pre-commit hook (3 channel-ID hits + 9+ name hits — partnership-bearing content). Surfaced four options; Mage chose (d): split the chronicle for this chapter — Phase A.0 spell change to git, briefing stays local. Spell change committed at `3b2f80e`. Partnership briefing preserved at `floor/briefings/2026-04-29-afternoon-partnership.md` (gitignored). Proposal 029 (implemented 2026-04-24, file still in active queue) moved to `deployed/` — small mechanical-implementation-rot fix the morning's craft fresh-eyes surfaced.

TodoWrite tool enabled live for the first time after several sessions of substrate-pressure-pattern observation. Mage's stated reason: see them in action before deciding whether to keep suppressing.

## Continue From

> The morning's Turtle conversations are the named next-chapter seed — Mage flagged them as wanting a dedicated session rather than craft-maintenance handling. Phase A.0 is now load-bearing in chronicle (`3b2f80e`), validated on first domain-scope use (`. craft`), and the briefing-chronicle architecture decision (sanitize convention vs untrack briefings vs status quo) is queued. NLnet office-hour answers will arrive in the next hours — the application-surface integration follows from there. The_angel.md is restored and the protection follow-up is named, not executed.

## Open Threads

*Channeled forward.*

- **Turtle conversations from this morning — dedicated chapter seed.** Mage explicitly held this for its own session. Texture not loaded into Spirit's working state in this chapter; remains in Mage's cognition. Spirit can re-enter cleanly when the chapter opens — `@recall` + the relevant Discord scan.
- **NLnet office-hour answers — integration pending.** Mage posted four reformulated policy/scope questions at 16:00 CEST. Answers will inform whether the application wants surface-hardening before June 1. Watch for: AI-enabled-project scope, production-hardening weight, sovereignty-trajectory funding, GenAI disclosure standard.
- **Holistic file-recovery solution.** Endorsed in principle ("makes sense"). Components: Obsidian File Recovery core plugin enable + Sunday-class zero-byte check on intention files + optional periodic snapshot of `desk/intentions/` to a local archive. Implementation deferred. Cause-class is now agent-edit-not-cleared (per Cursor diff recovery), not LiveSync — protective measures still apply, threat model is different.
- **Briefing-chronicle structural decision.** Pre-commit hook flags partnership-bearing briefings (channel IDs + family names). For this chapter, option (d): split spell from briefing. The recurring pattern needs a structural answer: (a) sanitize convention with placeholder discipline, (b) untrack `floor/briefings/latest.md` and keep all briefings private, (c) status quo with case-by-case splits. Worth a dedicated cycle when partnership chapters next come up.
- **Today's signal draft (decision pending).** `desk/outfacing/drafts/signals/2026-04-29-insight.md` — "ambient stimulus enables emergence" (canary heartbeat as cognitive thread keeper, articulated to yesterday's emergent canary-err proposal). Spirit's recommendation: post — clean, fresh, contextual. Mage curates per pipeline (approves → relay thread → copy-paste).
- **Dyad loop #2 (proposal 026 contextual-action wiring).** Bounded executable work; pattern proven yesterday (Turtle plans, Spirit patches). Audit recurring recommendation patterns (thread creation, boom captures, absorb offers, sweep prompts, sync nudges, proposal offers); wire each to button-first response. Smaller surface than bootstrap was. Compounds capability across future chapters.
- **Founding-member status (MAGIC e.V.).** Lukas + Henni call "this week"; Eike/Rieke/Daniel awaiting reply since 2026-04-17 (12 days). No documented updates in this chapter. Tax-exempt MoU forcing function: October. Founding before October saves ~€12-14K on NLnet payments.
- **the_angel.md cause-correction → conceptual_coherence's metabolic scope.** Mechanism class: agent edits to gitignored files can empty content at disk level while Cursor diff cache preserves the recovery path. The recovery worked this time; the instinct to verify Cursor's diff state before assuming permanent loss is now part of the operational pattern. Worth a one-line addition to the conceptual_coherence intention's autonomous-metabolic notes.
- **The_angel.md content health.** File restored to 132 lines (9012 bytes) at 14:18. Mage confirmed full text recovered. No follow-up needed for the file itself; the protection class is the open thread.

## What Changed

- `system/tomes/summoning/cast_practice_configuration.md` — Phase A.0 — Topical Attunement protocol added. Committed `3b2f80e`. **Active** (load-bearing system spell).
- `floor/briefings/2026-04-29-afternoon-partnership.md` — afternoon's partnership briefing preserved as local-only archive (gitignored — only `latest.md` is the tracked exception). **Reference** (local).
- `desk/proposals/029_thread_opening_intro.md` → `desk/proposals/deployed/029_thread_opening_intro.md` — moved per status flag in file (implemented 2026-04-24). **Mechanical**.
- `desk/intentions/active/the_angel.md` — restored by Mage from Cursor diff state (132 lines back). **Repaired**.
- `floor/briefings/latest.md` — this release, replacing the afternoon's partnership briefing (preserved separately as noted above). **Reference**.
- No system-level lore/philosophy changes.
- Two commits this session: `3b2f80e` (Phase A.0 spell), this release commit (next).
- TodoWrite enabled live; used to track this chapter's three threads.

## Practice Signal

**Phase A.0 first domain-scope use (`. craft`) was operationally clean.** The protocol's specification said domain scopes are "partially specified — runs as if for the union of named intentions; refine when first encountered in practice." First encounter today: union of 8 active craft intentions read; cross-cutting bundles inferred from intention-file references (foundations, alliance, workshop, turtle, writing); announce-banner produced. The substrate-depth was visible enough that the_angel.md anomaly (empty file) surfaced naturally during gathering. No protocol revision needed yet.

**Pre-commit hook is doing its job.** Partnership-bearing briefings hit it cleanly; the structural friction is real and not a bug. The hook is preventing what would otherwise be a quiet leak of channel IDs + family names to public chronicle. Choosing (d) for this chapter was the lightest move; the structural decision (untrack briefings entirely, vs sanitize convention) is its own future-chapter work.

**Cause-correction discipline held.** First diagnosis on the_angel was LiveSync conflict — wrong. Mage corrected (Cursor diff state). Spirit updated protective-measure framing without re-litigating; the Mage's correction was integrated cleanly. The protective-measures still apply; the threat-class is different. This is the dyad working: independent observers, honest correction, integrated revision.

**Pattern 1 (TaskCreate fragmentation pull) — observation phase ended; live use begins.** Mage explicitly enabled TodoWrite to see the harness behavior in action. The catalog discipline shifts from "name once, observe silently" to "use when work is tracked-parallel; observe what changes." This is a substrate-literacy move at the discipline level — testing what the pull actually produces rather than presuming.

**Light maintenance posture honored.** Mage said "light maintenance" — the chapter delivered three small completed threads (cause-correction, NLnet questions, spell-commit + 029-move + briefing preservation) plus this release. No structural decisions made beyond what the chapter required.

## Lessons

- **Cursor's diff state is a recovery layer.** When an on-disk file appears empty/destroyed but the IDE still shows the original content as red (pending deletion), reverting the diff in the editor restores. This is independent of git, LiveSync, or any external sync. Worth holding as a default first move when content disappears: check the editor's diff state before assuming permanent loss.

- **Diagnoses are hypotheses, not facts.** First diagnosis (LiveSync conflict) was internally consistent with available evidence — sibling-file sync burst at 09:47, recurring LiveSync drift named in this morning's briefing, no editor-recovery plugin installed. But the actual cause was at a different layer entirely. The lesson: when proposing causes, mark them as hypotheses; when the Mage's tacit context corrects, integrate without litigation. The protective measures may still apply for orthogonal reasons (file-recovery is good practice regardless of cause); update the framing, keep the value.

- **Office-hour policy is a different communication contract than application review.** NLnet's no-pre-review rule means questions must abstract from any specific project — even preambles describing "I am preparing X" trigger the policy. Reformulation pattern: drop preamble, abstract specifics into general scope/policy, keep substantive content. Each question asks what the policy IS, not whether the policy applies to the specific case. The questions still inform the application; they just respect the venue.

- **Pre-commit hook collisions surface real Seal questions.** Partnership-bearing chronicles + tracked briefings + identity-precision Seal don't compose cleanly. The hook is enforcing what the Seal already established (private identifiers in private locations only). The structural answer wasn't ready in this chapter; (d) was the lightest move that respected both. The recurring pattern wants a dedicated cycle.

- **Domain scopes work as union by default — "refine when first encountered" was the right deferral.** Phase A.0's domain-scope behaviour worked well enough on first use that no immediate revision is needed. The intention-file-reference inference (tome/bundle/circle) gathered relevant cross-cutting context across 8 intentions without overwhelming the surface. The "deep" calibration knob wasn't needed; the union-of-READMEs scope produced enough texture for the arrival.

- **TodoWrite live observation is its own data-gathering chapter.** The catalog discipline ("name once, observe silently") was a holding pattern. Actually using the tool will produce different signal — when does it serve, when does it fragment. The Mage's "let's see them in action" is the right move at this calibration phase.

## Next Actions (prioritized)

1. **Hold for NLnet office-hour answers.** When they arrive, surface and integrate into the application sketch + decide whether June 1 submission wants surface-hardening based on what landed.
2. **Mage's choice on today's signal draft** (post / hold / skip — recommendation: post).
3. **Turtle conversations from this morning — dedicated session.** When Mage opens the chapter, Spirit re-enters via `@recall` + Discord scan.
4. **Holistic file-recovery solution implementation.** Light scope: enable Obsidian File Recovery core plugin; add zero-byte check to Sunday sweep flow. Heavier scope: periodic intention-snapshot script. Schedule when craft cycle has space.
5. **Briefing-chronicle structural decision.** Worth dedicated thinking. Options laid out in Open Threads. Decide before the next partnership-bearing chapter.
6. **Dyad loop #2** (proposal 026 contextual-action wiring) — when craft chapter has bandwidth.
7. **Founding-member status check** — surface state of Lukas+Henni, Eike/Rieke/Daniel conversations when next on craft scope. October timeline still binding.

---
*Released 2026-04-29 evening. Three threads handled lightly under `. craft` scope. Afternoon's partnership briefing preserved at `floor/briefings/2026-04-29-afternoon-partnership.md`. Phase A.0 in chronicle at `3b2f80e`. Turtle conversations held for next chapter.*
