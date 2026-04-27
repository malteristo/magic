# On Thread Eddies

*Threads as temporary differentiations of the main conversation stream*

---

## I. The River and Its Eddies

The main dialogue channel is a river. Threads are eddies — temporary differentiations where the current swirls into focused patterns before rejoining the flow.

An eddy forms when conversation develops enough density or specificity to warrant its own space. It spins for as long as the energy persists. When the energy dissipates, the water returns to the river.

This is the lifecycle: **formation → spinning → harvest/calcification → optional dissolution → reabsorption**.

The practice doesn't accumulate dead threads. It breathes.

---

## II. Eddy Types

Three types, distinguished by how they dissolve.

**Standard** (💬 default) — Most conversations. A question, a brainstorm, an exploration. Standard eddies are checked by metabolic cycles — if quiet for 7+ days, they're flagged for calcification, release, continued spinning, or standing-wave upgrade.

**Standing Wave** (🌊 permanent) — A deliberate feature of the river. Reference threads, ongoing projects, persistent eddies like the learnings journal. Standing waves never dissolve automatically — they're infrastructure, not conversation.

**Manual Release** (🍃 session-end) — Ephemeral by design. When the conversation goes idle (session timeout), the thread dissolves automatically: Turtle captures the essence to boom, archives the conversation, and notifies the parent channel. No dissolution prompt — the ephemerality is the point.

The default is standard because most conversations benefit from recurring metabolic review. The type can be changed at any time via the config buttons or `!thread-type`.

---

## III. Harvest, Calcification, and Dissolution

Dissolution is not deletion. It is also not the only way an eddy metabolizes. Three operations are distinct:

1. **Harvest** — Turtle notices what the eddy produced: decisions, open loops, resonance, proposals, learnings, issues, or "nothing durable."
2. **Calcification** — Turtle writes or updates a durable artifact that lets future Turtle remember why the eddy existed and what came from it.
3. **Dissolution** — The Discord thread goes quiet or archives. This is optional; standing waves can calcify periodically while staying open.

The landing place depends on the eddy's purpose. A proposal-bearing eddy updates the proposal. A learning eddy creates a learning record. A debugging eddy updates issues. An exploratory eddy may become `notes/eddies/<slug>.md`. Some eddies release with no artifact because no durable resonance emerged.

When an eddy calcifies, Turtle posts a short outcome note at the end of the Discord thread with the artifact link, outcome, open loops, and status. The thread remains Discord coral. The artifact is the calcification that persists in the practice files.

The Mage always has the final word. Dissolution is flagged, never forced. Three options appear as buttons:
- **Archive & Capture** — Extract essence, archive, close
- **Keep Spinning** — Reset the timer, the thread isn't done
- **Make Standing Wave** — Upgrade to permanent

Future buttons should distinguish these operations more precisely: **Calcify**, **Calcify & Archive**, **Release**, **Keep Spinning**, **Make Standing Wave**.

---

## IV. Integration Points

**Metabolic cycles**: Quiet eddy review can happen during weekly maintenance, post-session reflection, interoception, or on demand. Sunday practice remains one container, but the metabolism should not depend on one remembered day.

**Release ritual**: During `@release`, Spirit reviews any flagged threads. Resonance that should persist in the practice (not just in the archive) gets attention. The Spirit evaluates: does this thread's essence belong in bright, a proposal, a learning record, an issue, an eddy note, or nowhere durable?

**Session monitor**: The existing 15-minute idle detection runs independently. Dissolution is a longer timescale — days, not minutes. Session notes capture individual conversations; dissolution captures the thread's whole arc.

**Pulse and interoception**: Pulse should report eddy lifecycle state — which eddies need calcification, which are standing, which are already calcified — not just quiet-thread counts.

---

## V. Buttons and Commands

Every action is available as both a `!` command and a Discord button. Commands are for power users and automation. Buttons are for mobile, for accessibility, for making the invisible visible.

When a thread is created, type-selection buttons appear. The Mage can tap to change — no need to remember syntax. When a thread is flagged for metabolism, Turtle should offer the relevant actions as buttons: calcify, calcify and archive, release, keep spinning, merge, or make standing wave.

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
