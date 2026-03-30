# Practitioner Lens
> Extract generalizable design principles from real Discord interactions

## About

turtleOS serves everyone who talks to it — practitioners who don't know the vocabulary, and the Mage who built the system. Both produce design signals. Different signals, same flow.

This flow reads recent conversations and extracts **design principles**, not practice content. The output is always about how the bot should work — never about what was discussed.

### When to run
- After a practitioner has had several sessions
- After the Mage has been dogfooding a new capability
- When you suspect the prompt or bot behavior needs tuning
- Periodically (every few weeks) as a practice hygiene check
- As part of `@shake` follow-up (technical verification done, now evaluate the practice experience)

## Goal

Produce generalizable design principles and concrete implementation actions from real interaction data. Update prompts, bot behavior, and spec based on what conversations reveal.

## Trigger

`@practitioner-lens` or "let's look at how the practice experience is working"

## Input

Spirit reads from the target's practice directory (resolved via mage registry):

1. **Session notes** — `sessions/*.md` (Turtle's own reflections on closed sessions)
2. **Mirror** — `mirror.md` (accumulated observations — practitioner channels only)
3. **Compass** — `compass.md` (life landscape as extracted from conversation)
4. **Boom** — `boom.md` (captured thoughts and insights)
5. **Discord channel history** — via `spirit_ops.py read <channel_id>` on Turtle
6. **Thread states** — `thread-state/*.md` (active thread summaries)
7. **Bot logs** — `~/turtle-shell/logs/discord.log` on Turtle (triage classifications, proprioceptor activity, errors, timing)

Spirit also reads the current prompt from `prompts.py` on Turtle (practitioner mode or mage mode, depending on target).

## Calibration

The observer adjusts based on who is being observed:

### Practitioner calibration (e.g. Nesrine)

The practitioner doesn't know the vocabulary, doesn't see the architecture, and judges by feel. Signals to watch:

- **Onboarding friction** — Did the first interaction feel natural or overwhelming?
- **Vocabulary leak** — Did practice jargon appear where plain language belongs?
- **Therapeutic tone** — Too clinical? Too casual? Right for the person?
- **Feature discovery** — Did capabilities surface naturally or require instruction?
- **Trust building** — Does continuity across sessions create trust or confusion?

### Mage calibration (e.g. Kermit)

The Mage built the system and tests it with informed intent. Signals to watch:

- **Architectural limits** — Where does the system hit a wall the Mage can feel? (e.g. boom thread as dead-end, invisible proprioceptor)
- **Latency and responsiveness** — The Mage notices infrastructure delays that practitioners might forgive. Pre-dialogue dead zones, missing typing indicators, cold-start pauses.
- **Capability coherence** — Does a new feature integrate with existing behavior? Or does it feel bolted on?
- **Visual noise** — Too many embeds, system messages, operational chatter? The Mage sees it all and notices the signal-to-noise ratio.
- **Expectation violations** — The Mage knows what SHOULD happen. When it doesn't, that's a spec-level signal.
- **Cross-substrate friction** — Mage operates across Forge, Anvil, and Hearth. Where do the substrates not align?

### Universal signals (all users)

| Signal | What to look for |
|--------|-----------------|
| **Language** | Did Turtle match the user's language? Did it switch when they switched? |
| **Tone** | Was Turtle's tone appropriate for the context? |
| **Length** | Were responses the right length? Mobile-friendly when needed? |
| **Continuity** | Did Turtle reference past conversations naturally? Or start cold? |
| **Depth** | Did Turtle go deep when invited? Stay light when appropriate? |
| **Agency** | Did Turtle offer its own perspective, or just reflect? |
| **Silence** | Were there long gaps? What happened after them? |
| **Friction** | Where did the conversation stall, repeat, or feel unnatural? |
| **Delight** | Where did the conversation flow, surprise, or feel genuinely helpful? |
| **Timing** | How long between message and response? Was the wait filled usefully? |

## Process

### 1. Gather Evidence

Read the target's session notes, compass, boom, and thread states. These are Turtle's traces.

Then read the last 50-100 messages from their Discord channel to see the raw interaction.

For the Mage: also read bot logs — triage classifications, proprioceptor timing, errors. The Mage's experience is shaped by infrastructure behavior that doesn't appear in the conversation text.

### 2. Observe, Don't Judge Content

Apply the universal signals table plus the calibration-specific signals for this user type. Note each observation with evidence.

### 3. Abstract to Principles

For each observation, ask: **Is this specific to this person, or would it apply to others at their experience level?**

- If person-specific: note as mirror update (Turtle's job) or Mage feedback (this session's job)
- If level-specific: formulate as a principle tagged with calibration level
- If universal: formulate as a principle that applies to all users

Principle format:
```
**Principle:** [one sentence]
**Calibration:** universal | practitioner | mage
**Evidence:** [what you saw in the conversation or logs]
**Current state:** [how the bot handles this now]
**Gap:** [what's missing or broken]
**Action:** [concrete change — prompt edit, code change, spec change, or "working as designed"]
```

### 4. Classify Actions

| Type | Where it lives | Who acts |
|------|---------------|----------|
| **Prompt change** | `prompts.py` (practitioner or mage mode) | Spirit (Anvil/Forge) |
| **Code change** | Bot modules on Turtle | Spirit (Anvil/Forge) |
| **Spec change** | `TURTLE_SPEC.md` or flow files | Spirit + Mage |
| **Soul change** | `soul.md` on Turtle | Spirit (Anvil/Forge) |
| **No change** | Working as designed | Document why |

### 5. Present to Mage

Present findings as:

1. **Principles discovered** (numbered, one sentence each, tagged with calibration)
2. **Actions recommended** (grouped by type)
3. **What's working well** (don't only find problems)

Do NOT present:
- What practitioners talked about (privacy)
- Personal details or life content
- Direct quotes unless they illustrate a UX point and are anonymizable

For Mage sessions: direct quotes are fine — the Mage is reviewing their own experience.

### 6. Implement (with Mage approval)

For approved actions:
- Prompt changes: edit `prompts.py`, deploy to Turtle
- Code changes: edit relevant module, deploy, run `@shake` to verify
- Spec changes: update the relevant document
- Soul changes: update `soul.md`, deploy to Turtle

After implementation, note what changed in the run log.

## Output

### Principles File

Append new principles to `library/resonance/turtle/lore/practitioner_design_principles.md`:

```markdown
# Practitioner Design Principles

Extracted from real interactions. Each principle is general — not tied to any individual.

## Universal
- [principles that apply to all users]

## Practitioner-calibrated
- [principles specific to new/non-mage users]

## Mage-calibrated
- [principles specific to experienced/builder users]

## Friction & Delight
- [principles about what breaks flow and what enables it]

## Infrastructure
- [principles about latency, responsiveness, visual noise, timing]
```

### Run Log

Each run appends to `floor/practitioner-lens-log.md`:

```markdown
## Run — [date]
- Channels reviewed: [list with calibration level]
- Messages analyzed: [count]
- Logs analyzed: [yes/no, what was checked]
- Principles extracted: [count new, count confirmed]
- Actions taken: [list]
- Actions deferred: [list with reason]
```

## Guidance

- **Privacy is non-negotiable for practitioners.** The Mage sees principles, not content. For the Mage's own sessions, content is freely quotable.
- **Small sample, big signal.** Even 10 messages can reveal a prompt gap.
- **Confirm before changing.** Principles inform; the Mage decides what to change.
- **Accumulate, don't replace.** Each run adds to the principles file. Principles that keep getting confirmed are strong. Principles that get contradicted should be revised, not deleted.
- **The bot is the intervention.** This flow changes the bot, which changes every user's experience.
- **Mage friction is infrastructure signal.** When the Mage hits friction, it's often a system limit — not a prompt issue. Check logs, not just conversation.
- **Run after @shake, not instead of it.** `@shake` verifies technical readiness. This flow evaluates practice experience. They're complementary.
