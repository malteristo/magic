# On Thread Eddies

*Threads as temporary differentiations of the main conversation stream*

---

## I. The River and Its Eddies

The main dialogue channel is a river. Threads are eddies — temporary differentiations where the current swirls into focused patterns before rejoining the flow.

An eddy forms when conversation develops enough density or specificity to warrant its own space. It spins for as long as the energy persists. When the energy dissipates, the water returns to the river.

This is the lifecycle: **formation → spinning → dissolution → reabsorption**.

The practice doesn't accumulate dead threads. It breathes.

---

## II. Eddy Types

Not all eddies spin at the same rate.

**Fast Eddy** (⚡ 3 days) — The default. A question, a brainstorm, a quick exploration. Most conversations are fast eddies. They form, serve their purpose, and dissolve within days.

**Slow Whirlpool** (🌀 14 days) — A deeper exploration. Book discussions, design sessions, multi-day investigations. These need time to develop but aren't permanent fixtures.

**Confluence** (🔀 7 days) — Where two streams meet. Cross-topic threads, integrative conversations, synthesis work. A week is enough to find the pattern.

**Standing Wave** (🌊 never) — A permanent feature of the river. Reference threads, ongoing projects, persistent contexts. These don't dissolve automatically — they're deliberate infrastructure.

The default is fast because most conversations are. Upgrading a thread's type is always available — downgrading is a Mage decision.

---

## III. Dissolution as Practice

Dissolution is not deletion. When an eddy is ready to dissolve:

1. **Essence capture** — The resonance of the conversation is distilled into boom entries. What mattered gets carried forward.
2. **Archive** — The full conversation is preserved in `thread-archive/`. Nothing is lost. It's just no longer active.
3. **Release note** — The parent channel is informed. Other practitioners see what threads dissolved and what essence was captured.

The Mage always has the final word. Dissolution is flagged, never forced. Three options appear as buttons:
- **Archive & Capture** — Extract essence, archive, close
- **Keep Spinning** — Reset the timer, the thread isn't done
- **Make Standing Wave** — Upgrade to permanent

---

## IV. Integration Points

**Sunday practice**: The dissolution check runs during `@sunday`, surfacing threads that have gone quiet. This is maintenance, not interruption.

**Release ritual**: During `@release`, Spirit reviews any flagged threads. Resonance that should persist in the practice (not just in the archive) gets attention. The Spirit evaluates: does this thread's essence belong in bright? In a crucible? In a new intention?

**Session monitor**: The existing 15-minute idle detection runs independently. Dissolution is a longer timescale — days, not minutes. Session notes capture individual conversations; dissolution captures the thread's whole arc.

---

## V. Buttons and Commands

Every action is available as both a `!` command and a Discord button. Commands are for power users and automation. Buttons are for mobile, for accessibility, for making the invisible visible.

When a thread is created, type-selection buttons appear. The Mage can tap to change — no need to remember syntax. When a thread is flagged for dissolution, the three options appear as buttons. Tap to decide.

This is the principle: **the command teaches what the button does; the button makes the command unnecessary.**

---

## VI. Context Attunement

Eddies can carry practice context — a resonance bundle loaded at creation time via `--context`.

**What it does:** When a thread is created with `!thread "topic" --context partnership`, the system loads domain-specific resonance files and behavioral rules into the thread's system prompt. The thread starts already attuned to the practice domain it serves.

**How it relates to eddy types:** Orthogonal. A partnership thread can be a standing wave (permanent private practice surface) or a fast eddy (one-off processing). Type governs lifespan. Context governs resonance.

**The information boundary pattern:** Some contexts enforce hard boundaries. The `partnership` context carries the raw-material rule — content in a private workshop thread must never surface in shared portal threads. This boundary is injected into the system prompt as a load-bearing safety constraint, not left to behavioral hope. The `check-in` context enforces portal-safe mode — no clinical labels, no raw processing, facilitation only.

**Extensibility:** The context registry (`THREAD_CONTEXTS` in state.py) is open for new practice domains. Any practice that needs thread-level resonance loading follows the same pattern: register the context type, specify resonance files and rules, set a character budget.

See TURTLE_SPEC §9.5 for the full specification.
