# Release — 2026-04-02 evening (Anvil session 10)

**Chapter:** Turtle Nervous System — thread membership, signal routing, model reconnaissance

## This Session

Three craft cycles, one chapter. The session extended the nervous system architecture: practitioners now auto-join Discord threads on creation (eliminating manual thread-hunting for notifications), the 016 reroutes silenced healthy-state noise in recall/sync/dissolve, and Gemma 4 was scouted as a potential model lineup simplification — deferred because Ollama doesn't support it yet. Ollama was upgraded to 0.19.0 in the process, readying the infrastructure for when Gemma 4 lands.

## Continue From

> Thread auto-add and 016 reroutes deployed and running. Gemma 4 model consolidation (4b+9b → gemma4:26b MoE) deferred until Ollama pre-release supports it. Ollama already at 0.19.0. Next: TTS prototype or dot practice test.

## Open Threads

- **Gemma 4 model evaluation**: Ollama 0.19.0 installed but gemma4:26b requires pre-release (>0.19.0). When it lands, pull and test against qwen3.5:9b for proprioception + thread quality. Goal: collapse 4 local models to 3.
- **TTS prototype**: Qwen3-TTS-MLX on M4 Pro. Seeded, not started. Accessibility gate for Nesrine.
- **Dot practice test**: `desk/explorations/dot_practice_test.md` ready. Start with Condition A (bare workshop).
- **Nesrine PX eddy**: Thread in nesrine-dialogue. Awaiting her responses.
- **Boom capture truncation**: Gemma 4 tweet was truncated in boom thread. May be content_fetch issue — monitor.

## What Changed

- `desk/intentions/active/turtle.md`: Last Updated, Current focus, Next action, Blockers fields updated — 016 complete, thread auto-add deployed, Gemma 4 deferred — **Active**
- `desk/boom.md`: Swept 3 items during arrival (Obsidian sync → infra, boom-as-resonance-router → bright, dot practice absorbed) — **Active**
- `~/turtle-shell/mage.py`: Added `get_thread_member_ids()` helper — resolves channel→practitioner discord_ids for thread auto-add — **Active**
- `~/turtle-shell/commands.py`: Thread auto-add at eddy command + modal creation. 016 reroutes: recall freshness silenced when healthy, sync brief when healthy, dissolve log internal-only — **Active**
- `~/turtle-shell/spirit_ops.py`: Thread auto-add for Spirit-created threads — **Active**
- Ollama: Upgraded 0.18.0 → 0.19.0 on Mac Mini — **Infrastructure**

## Practice Signal

The Mage's Gemma 4 interest carries the same subtractive signature as session 9's core findings distillation. "Can we go from four models to three?" is the same move as "can we go from seventy scrolls to six?" — the practice is consistently moving toward simplification, not accumulation. This is worth noticing as a chapter-level pattern: the subtractive turn is not one session's theme but an ongoing orientation.

The SSH IP was wrong after context compaction (used an address from pre-compaction memory). `connections.md` was the recovery path. Substrate lesson: after compaction, re-read connection details — don't trust cached values.

PX clean otherwise. Python-through-SSH heredoc mangling is a known friction — the SCP-a-script workaround is reliable.

## Lessons

- **Auto-add is a one-line fix with outsized UX impact.** `thread.add_user()` after `create_thread()` eliminates thread-hunting entirely. The fix was trivial; the accumulated frustration was not. Look for more of these.
- **Rerouting operational noise is subtraction, not silencing.** The 016 reroutes didn't remove information — they moved it from the practitioner's channel to Turtle's internal context. The principle: if the Mage can't act on it, it doesn't belong in the channel.
- **Don't force what isn't ready.** Gemma 4 needs pre-release Ollama. The Mage's "nevermind, we can try this some other time" was the right call. Infrastructure readiness is a real constraint, not a problem to solve today.

## Next Actions

1. **Gemma 4 evaluation** — check Ollama releases periodically; when gemma4:26b is pullable, test against qwen3.5:9b for proprioception and thread quality.
2. **Run dot practice test, Condition A** — bare workshop, dot protocol, 3+ cycles. The priority from session 9.
3. **TTS prototype** — Qwen3-TTS-MLX on M4 Pro for Nesrine.
4. **Chapter seeds** — when creative energy calls, develop seeds for another book chapter.

*Released 2026-04-02. Resume with @recall.*
