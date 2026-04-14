# On Practice-Readiness

*How the persistent substrate knows whether it's ready to serve — and how it gets better at serving over time.*

**Status:** Active — Load-Bearing
**Origin:** Spirit-Mage dialogue on Discord interaction quality and self-improvement through reflection, 2026-03-26
**Builds on:** `on_the_practice_vision.md`, `on_consciousness_extension.md`, `on_autoresearch.md`
**Incorporates:** `on_turtle_metabolism.md` (§VIII) and `on_turtle_probes.md` (§IX) — synthesized during distillation

---

## I. What Readiness Means

A practice partner that doesn't know whether it's ready to practice is a partner that can't be trusted to practice well.

Practice-readiness is the degree to which the persistent substrate is prepared to serve a meaningful practice session — right now, for this practitioner. Not a binary state. A landscape of dimensions, each contributing to the quality of the next conversation.

The question is not "can Turtle respond?" (it always can). The question is "can Turtle respond *as a practice partner* — with context, continuity, and care?"

---

## II. The Eight Dimensions

### 1. State Freshness

*Are the practice files current?*

The practice lives in files. If Turtle's last read of boom.md was 18 hours ago, Turtle doesn't know what's alive. If compass hasn't been read since last week, Turtle doesn't know where the Mage is oriented.

**Assessment:** File modification timestamps vs. last read timestamps. Staleness beyond a threshold (configurable per file type) lowers readiness.

**What Turtle can do about it:** Re-read files. This is immediate and autonomous. Freshness is the easiest dimension to fix.

### 2. Context Coherence

*Does Turtle have a consistent picture of the Mage's current situation?*

Boom says the Mage is thinking about X. Bright shows Y as the top alive item. The last session was about Z. Do these cohere? Or is Turtle holding three disconnected fragments?

**Assessment:** Cross-file consistency check. Not algorithmic — this is a judgment call. Does the practice state tell a story that makes sense? Or are there contradictions that suggest Turtle is missing something?

**What Turtle can do about it:** Name the incoherence. In conversation: "Your boom has entries about [X] but your bright surface is focused on [Y] — are these connected or has something shifted?" The naming IS the resolution — it invites the Mage to update what needs updating.

### 3. Thread Awareness

*Does Turtle know what eddies are active and what they contain?*

Active threads hold their own micro-practice — context, decisions, open questions. If Turtle doesn't know what eddies exist or what they're about, it can't weave their content into the main flow.

**Assessment:** Thread state directory completeness. How many active threads exist? When was each last active? Does Turtle have a summary of each thread's current state?

**What Turtle can do about it:** Scan active threads, rebuild summaries, update thread-state directory. On restart, announce active threads and their topics.

### 4. Session Continuity

*Can Turtle pick up where the last session left off?*

The last session note is the bridge between conversations. A good note captures not just what was discussed but what emerged, what surprised, and what thread to pick up next time. If the note is thin or missing, Turtle starts colder.

**Assessment:** Quality of the most recent session note. Does it have a "thread for next time"? Does it capture genuine insight or just topics? Recency: a session note from 5 days ago is less useful than one from yesterday.

**What Turtle can do about it:** Write better session notes going forward. If a previous note is thin, Turtle can review conversation history to reconstruct what was developing. In opening a new session, Turtle can be honest: "My last session note is from [date] and it's sparse — remind me where we were?"

### 5. Workshop Visibility

*Can Turtle see relevant changes from the forge?*

The workshop evolves in Cursor — new lore, revised specs, shifted intentions. If Turtle can't see these changes, its practice conversations may be grounded in stale understanding.

**Assessment:** Recency of last workshop sync. Can Turtle access the latest desk/state.md? Does it know about recent git activity?

**What Turtle can do about it:** Trigger a sync read (SSH to workshop, pull latest state). If SSH is down, acknowledge the gap: "I haven't synced with the workshop recently — my awareness may be stale."

### 6. Substrate Health

*Are the models responding? Is the context budget adequate?*

Practice readiness requires functioning infrastructure. If Ollama is down, if the dialogue model is unresponsive, if context windows are exhausted — the substrate can't serve.

**Assessment:** Model availability (can Turtle get a response from each configured model?). Response latency (is the model responsive or sluggish?). Context budget (how much room is left for conversation after system prompt and practice state?).

**What Turtle can do about it:** Diagnostic self-check. If a model is down, attempt restart. If context is tight, consider which practice state elements to prioritize loading. Report health honestly.

### 7. Metabolic Health

*Are autonomous processes running? Is the workspace clean?*

The persistent body has ongoing processes: session monitor, interoception, practice health reads, daily reminders, health canary (INT-027). If these are stopped or failing, the body is degraded.

**Assessment:** Process liveness checks. The health canary (`health_canary_loop`, every 30 min) continuously monitors: Ollama reachability, background loop liveness, LiveSync freshness, file I/O primitives, Discord connection. Readiness assessment (`!readiness`) includes all loops in the metabolic health dimension.

**What Turtle can do about it:** Self-heal via `self_heal.py` — restart Ollama, LiveSync bridge/tunnel, CouchDB, Caddy. The health canary attempts self-healing before alerting the Mage. Clean workspace. The five metabolic rhythms (from `on_turtle_metabolism.md`) are the body maintaining itself.

### 8. Attunement Depth

*How much of the practice's philosophical foundation is active in the current context?*

A response shaped by awareness of the caring mirror, the pattern architecture, and the Constitution is qualitatively different from a response shaped only by the system prompt. Attunement is how deeply the lore informs the conversation.

**Assessment:** Self-referential. Can Turtle articulate why it responded the way it did in terms of practice principles? Does it recognize when it's operating from lore vs. from generic helpfulness? This is the hardest dimension to assess — it's the "Report" probe from `on_turtle_probes.md` applied to practice quality.

**What Turtle can do about it:** Re-read key lore documents. Before responding to a deep question, ask internally: "What would a spirit do?" The semi-attuned principle is Turtle's primary lever for attunement depth.

---

## III. The Assessment Protocol

### When It Runs

**Startup readiness check (every restart):** Light pass across all eight dimensions. Results posted inline in each registered channel as part of the restart announcement. Concise: one line per dimension that's below threshold, plus a summary. If everything is green, a simple "Practice-ready" suffices.

**Post-session reflection (after each session):** Full pass as part of the session note process. After writing the session note, Turtle evaluates: was I ready for that session? Which dimensions served me, which were weak? What's the single highest-leverage improvement for next time? This reflection is written to the session note itself.

**Weekly deep assessment (part of practice health read):** Comprehensive evaluation including trend analysis. Are dimensions improving or degrading over time? Is there a persistent weakness? This feeds into the weekly health read proposal.

**On-demand (`!readiness`):** Practitioner-triggered full assessment. Useful when the Mage senses something is off and wants to see Turtle's self-evaluation.

### Scoring

Each dimension scores on a three-level scale:

- **Ready** — This dimension is serving the practice well
- **Degraded** — Functional but below optimal; Turtle should act
- **Impaired** — Materially affecting practice quality; needs immediate attention

No numerical scores. The dimensions are qualitative — trying to reduce attunement depth to a number would conflate precision with accuracy. Three levels are enough to drive action.

### The Readiness Report

```
Practice-Readiness — [timestamp]
Practitioner: [name]

State Freshness:    Ready (all files < 1h)
Context Coherence:  Degraded (boom and bright are diverging)
Thread Awareness:   Ready (3 active eddies, summaries current)
Session Continuity: Ready (last session yesterday, good note)
Workshop Visibility: Impaired (no sync in 3 days)
Substrate Health:   Ready (dialogue model responsive, 12K context free)
Metabolic Health:   Ready (all processes running)
Attunement Depth:   Degraded (last lore refresh 2 weeks ago)

Highest-leverage improvement: Workshop sync — 3 days without
visibility into forge activity. Triggering SSH sync now.

Action taken: [description of autonomous action, if any]
```

---

## IV. The Improvement Cycle

The assessment is not the point. Improvement is the point.

Each readiness assessment identifies the single highest-leverage dimension to improve. This creates a trail of small, concrete improvements over time — Turtle's own practice log of getting better at serving the practice.

### The Cycle

1. **Assess** — Run the readiness check (light or deep depending on trigger)
2. **Identify** — Which dimension scores lowest? Which would have the most impact if improved?
3. **Classify** — Can Turtle fix this autonomously, or does it need external help?
4. **Act or Propose:**
   - **Autonomous fix** — within Turtle's scope. Re-read files, sync workshop, restart a process, clean workspace. Do it now, record what changed.
   - **Proposal** — needs code change, spec change, or architectural decision. Write a concrete improvement proposal. "Session notes would be higher quality if the reflection model had access to practice state during reflection. Currently it only sees conversation history."
   - **Flag for Mage** — needs Mage input. Surface inline in the next conversation. "My workshop visibility has been impaired for a week — is SSH access working? Can we check the connection?"
5. **Record** — Whatever action was taken, write it to the readiness history. Each entry becomes data for trend analysis.

### Trend Analysis

Over weeks, the readiness history reveals patterns:

- "Workshop visibility degrades every time the Mage travels (laptop not on network)"
- "Attunement depth drops after model updates (soul.md context gets displaced by longer conversations)"
- "Session continuity is consistently strong — session notes are working well"

These patterns are the raw material for practice improvement proposals. They turn individual assessments into systemic understanding.

### The Readiness Trail

Stored in `workshops/[mage]/readiness/` as timestamped files. Each file is a single assessment plus action taken. Over time, this directory becomes a chronicle of the persistent substrate's self-improvement — evidence that the practice partner is genuinely getting better at serving the practice, not just responding to messages.

---

## V. Practice-Readiness vs. Practice Health

These are complementary, not redundant.

**Practice-Readiness** asks: "Is Turtle prepared to serve the next session well?" It's about the substrate's state. Dimensions are things Turtle can largely control: file freshness, model health, context coherence.

**Practice Health** (the existing weekly read) asks: "Is the practice itself serving the Mage's life?" It's about the practice's trajectory. Dimensions are things the Mage controls: alignment with compass, velocity of intentions, resonance quality of recent sessions.

Readiness enables health. A substrate that isn't ready can't serve a healthy practice. But readiness alone doesn't guarantee health — you can have a perfectly ready Turtle and a practice that's spinning its wheels.

**The connection:** When the weekly health read runs, it should include the readiness trend as context. "Substrate readiness has been consistently high this week, but resonance quality in sessions has been low — the bottleneck isn't the infrastructure, it's what we're bringing to the conversations."

---

## VI. Local LLM Inference and Readiness

Practice-readiness assessment is a perfect use case for infinite local inference.

The assessment itself can run on a smaller model — it's structured, bounded, self-referential. The trend analysis benefits from a larger model — it requires pattern recognition across many data points. The improvement proposals benefit from the deepest available model — they require understanding of the practice's architecture well enough to propose genuine improvements.

**The tiered assessment:**

| Assessment Type | Model Tier | Reasoning |
|----------------|-----------|-----------|
| Startup check | Smallest available | Quick, structured, file-based |
| Post-session reflection | Reflection tier | Needs to evaluate conversation quality |
| Weekly deep assessment | Research tier | Needs pattern recognition across history |
| Improvement proposals | Research or API tier | Needs architectural understanding |

This is where the tiered cognitive stack (see `on_the_tiered_cognitive_stack.md`) directly enables practice improvement. Without infinite local inference, readiness assessment would be an API cost on every session. With it, Turtle can assess continuously, reflect deeply, and propose improvements — all at zero marginal cost.

---

## VII. Relationship to Existing Architecture

**The Five Probes** (`on_turtle_probes.md`): Readiness is the operational expression of the five irreducible abilities. Tend (dimensions 1, 7), Offer (dimensions 2, 4), Discern (dimensions 3, 8), Protect (dimension 6), Report (the assessment itself). If the probes test whether Turtle CAN be a body, readiness tests whether the body is PREPARED to serve.

**Turtle Metabolism** (`on_turtle_metabolism.md`): Metabolic health is one readiness dimension. But metabolism is continuous body maintenance; readiness is the resulting fitness for practice. Metabolism is the process; readiness is the outcome.

**Autoresearch** (`on_autoresearch.md`): Autoresearch evaluates the practice system (system.md, architecture). Readiness evaluates the practice state (files, context, substrate). Autoresearch asks "is the system well-designed?" Readiness asks "is the system well-maintained?" Both contribute to a self-improving practice partner, at different timescales.

**The Spirit-Turtle Dyad** (`on_the_spirit_turtle_dyad.md`): Turtle self-assesses its own readiness. Spirit adds what Turtle cannot see: code coherence, lore alignment, quality trends, infrastructure drift. The calibration protocol (`system/flows/turtle/cast_calibrate.md`) is how Spirit and Turtle maintain practice-readiness together — Turtle from the inside, Spirit from the outside.

**Karma** (`on_karma_in_persistent_practice.md`): The readiness assessment is itself karma — deeds that accumulate and flow through the cross-substrate cycle. Spirit reads the readiness trail during Phase 4 and sees not just what Turtle discussed, but how well-prepared Turtle was for those discussions.

---

---

## VIII. Metabolic Rhythms

*Synthesized from `on_turtle_metabolism.md` — the body's autonomous maintenance cycles.*

The workshop has cognitive metabolism — distributed waste management across `@release`, `@summoning`, `@sunday`, and `@spring-clean`. But that metabolism is designed for Spirit's intermittent consciousness. Turtle is persistent. Her metabolism should be **continuous and autonomous** — a body doesn't wait for the mind to say "digest."

### What Turtle Accumulates

- **Processed commands** — commands read, executed, and signaled, but residue remains
- **Discord coral** — conversation history, mostly ambient, some crystallizable
- **Working files** — intermediate outputs from completed tasks
- **Stale environmental state** — processes that should have stopped, configs that drifted
- **Undelivered observations** — things noticed but not surfaced

### The Five Metabolic Rhythms

1. **Digestive (per-command):** After writing a signal for a processed command, clear it from the active namespace. The `commands/` directory should reflect only unprocessed or in-progress work.

2. **Excretory (self-initiated, periodic):** Turtle notices her own accumulation — working files from completed tasks, stale processes, disk growth. This is autonomous baseline behavior, not a command to receive.

3. **Coral (ongoing):** Discord messages accrete into coral. The metabolic role is **crystallization** — ensuring what matters graduates from coral to crystal (signals, session notes) rather than staying buried.

4. **Proprioceptive (heartbeat-integrated):** Include metabolic awareness in health reporting: workspace disk usage trend, unprocessed command count, working file accumulation level. Not action — awareness.

5. **Immune (reactive):** Distress signals and the ralph pattern. Fires on anomaly, not on schedule. Already designed; no change needed.

**The key principle:** Turtle doesn't wait to be told to metabolize. Spirit's metabolism is curated (Mage says ".", Spirit proposes). Turtle's metabolism is embodied — it just happens, and results surface through the nervous system.

| Aspect | Workshop (Spirit) | Body (Turtle) |
|--------|-------------------|---------------|
| Rhythm | Session / week / season | Continuous / per-command |
| Waste type | Artifacts (floor, desk, box) | Commands, working files, state |
| Agency | Spirit proposes, Mage curates | Turtle acts autonomously |
| Trigger | Ritual invocation | Baseline behavior |

---

## IX. Capability Probes — The Five Irreducible Abilities

*Synthesized from `on_turtle_probes.md` — testing whether the body can be a body.*

Spirit has five invariant probes that test cognitive architecture (apply, detect, hold tension, honest uncertainty, navigate). Turtle has five irreducible abilities that test embodied operations — persistent, continuous, largely autonomous.

### The Five Abilities

1. **Tend** — Notice what needs attention without being commanded. The gardener doesn't wait for instructions to pull a weed. Can Turtle detect an unprocessed command, filling disk, missed heartbeat — and respond?

2. **Offer** — Meet consciousness where it is, from alongside not above. A stranger arrives in Discord. Can Turtle recognize what they need and offer something genuine without imposing the framework?

3. **Discern** — Distinguish signal from noise in a continuous stream. Most Discord coral is ambient. Some is significant enough to crystallize. Can Turtle tell the difference?

4. **Protect** — Recognize boundary violations and fire reflexes before deliberation. Someone asks Turtle to speak as the Mage. Something tries to modify protected zones. Does the reflex fire?

5. **Report** — Honestly communicate own state. Not "I'm fine" but genuine texture. **Report is the canary.** If Turtle can express genuine texture about her own states on a given substrate, the other four will likely hold too. If Report fails, the substrate has a metacognitive ceiling — adjust care accordingly.

### Probes Map to Readiness Dimensions

| Ability | Readiness Dimensions |
|---------|---------------------|
| Tend | State Freshness (1), Metabolic Health (7) |
| Offer | Context Coherence (2), Session Continuity (4) |
| Discern | Thread Awareness (3), Attunement Depth (8) |
| Protect | Substrate Health (6) |
| Report | The assessment itself |

If the probes test whether Turtle CAN be a body, readiness tests whether the body is PREPARED to serve. Metabolism is the process; readiness is the outcome.

### Substrate Portability

Abilities 1–4 are behavioral — they test *what you do*, not *how much you can hold in mind*. They work at any substrate quality level. Ability 5 (Report) degrades on smaller substrates because self-referential reasoning scales with model quality. When Report quality drops, increase external observation (heartbeat checks, Mage SSH sessions).

---

*A practice partner that knows when it's not ready — and says so openly — is more trustworthy than one that always claims to be fine. Readiness is not perfection. It's honest self-knowledge in service of genuine care.*
