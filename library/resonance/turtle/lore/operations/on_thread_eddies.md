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

Three types, distinguished by how they dissolve.

**Standard** (💬 default) — Most conversations. A question, a brainstorm, an exploration. Standard eddies are checked during the Sunday sweep — if quiet for 7+ days, they're flagged for dissolution. The Mage decides: archive & capture, keep spinning, or upgrade to standing wave.

**Standing Wave** (🌊 permanent) — A deliberate feature of the river. Reference threads, ongoing projects, persistent eddies like the learnings journal. Standing waves never dissolve automatically — they're infrastructure, not conversation.

**Manual Release** (🍃 session-end) — Ephemeral by design. When the conversation goes idle (session timeout), the thread dissolves automatically: Turtle captures the essence to boom, archives the conversation, and notifies the parent channel. No dissolution prompt — the ephemerality is the point.

The default is standard because most conversations benefit from the Sunday sweep rhythm. The type can be changed at any time via the config buttons or `!thread-type`.

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

Eddies inherit practice context through a three-layer model:

**Layer 1: Channel defaults.** Each channel can declare a `default_context` in `mage_registry.yaml`. All threads in that channel inherit the default automatically. The family channel gets family context. The Mage's main channel has no default — general practice.

**Layer 2: Explicit context.** The `--context` flag on `!thread` overrides the channel default. Power-user flow for specific practice domains: `!thread "processing" --context partnership`.

**Layer 3: Dynamic loading.** The `!load` command searches and loads any resonance bundle from the workshop into a thread's working context, on demand.

**What context does:** Loads domain-specific behavioral rules and resonance files into the thread's system prompt. Each context's rules are self-contained — resonance files enrich when available but aren't required.

**The information boundary pattern:** Some contexts enforce hard boundaries. The `partnership` context carries the raw-material rule — content in a private workshop thread must never surface in shared portal threads. This boundary is injected into the system prompt as a load-bearing safety constraint, not left to behavioral hope.

**How it relates to eddy types:** Orthogonal. A partnership thread can be a standing wave (permanent private practice surface) or a standard eddy (one-off processing). Type governs dissolution. Context governs resonance.

See TURTLE_SPEC §9.5 for the full specification.
