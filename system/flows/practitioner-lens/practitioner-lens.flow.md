# Practitioner Lens
> Extract generalizable practitioner design principles from real Discord interactions

## About

The bot serves practitioners — people who aren't mages, who don't know the vocabulary, who just talk to Turtle as a thinking partner. The best design insights come from watching real conversations: where the bot meets them well, where it falls short, what patterns emerge that no spec anticipated.

This flow reads recent practitioner conversations and extracts **design principles**, not practice content. The Mage never needs to see what was discussed — only what the experience reveals about how the bot should work.

### When to run
- After a practitioner has had several sessions
- When you suspect the prompt or bot behavior needs tuning
- Periodically (every few weeks) as a practice hygiene check

## Goal

Produce a set of generalizable practitioner design principles and concrete implementation actions from real interaction data. Update the practitioner prompt and bot behavior based on what the conversations reveal.

## Trigger

`@practitioner-lens` or "let's look at how the practitioner experience is working"

## Input

Spirit reads from the practitioner's practice directory (resolved via mage registry):

1. **Session notes** — `sessions/*.md` (Turtle's own reflections on closed sessions)
2. **Mirror** — `mirror.md` (accumulated observations about the practitioner)
3. **Compass** — `compass.md` (life landscape as extracted from conversation)
4. **Boom** — `boom.md` (captured thoughts and insights)
5. **Discord channel history** — via `spirit_ops.py read <channel_id>` on Turtle

Spirit also reads the current practitioner prompt from `prompts.py` on Turtle.

## Process

### 1. Gather Evidence

Read the practitioner's session notes, mirror, compass, and boom. These are Turtle's traces — what it extracted from conversation.

Then read the last 50-100 messages from the practitioner's Discord channel to see the raw interaction.

### 2. Observe, Don't Judge Content

For each conversation segment, note:

| Signal | What to look for |
|--------|-----------------|
| **Language** | Did Turtle match the practitioner's language? Did it switch when they switched? |
| **Tone** | Was Turtle's tone appropriate? Too formal? Too casual? Too therapeutic? |
| **Length** | Were responses the right length for the context? Mobile-friendly? |
| **Continuity** | Did Turtle reference past conversations naturally? Or start cold every time? |
| **Vocabulary** | Did any practice jargon leak through? |
| **Depth** | Did Turtle go deep when invited? Stay light when appropriate? |
| **Agency** | Did Turtle offer its own perspective, or just reflect? |
| **Silence** | Were there long gaps? What happened after them? |
| **Friction** | Where did the conversation stall, repeat, or feel unnatural? |
| **Delight** | Where did the conversation flow, surprise, or feel genuinely helpful? |

### 3. Abstract to Principles

For each observation, ask: **Is this specific to this person, or would it apply to any practitioner?**

- If specific: note it as a mirror/compass update (Turtle's job, not the flow's)
- If general: formulate as a design principle

Principle format:
```
**Principle:** [one sentence]
**Evidence:** [what you saw in the conversation]
**Current state:** [how the bot handles this now]
**Gap:** [what's missing or broken]
**Action:** [concrete change — prompt edit, code change, or "working as designed"]
```

### 4. Classify Actions

| Type | Where it lives | Who acts |
|------|---------------|----------|
| **Prompt change** | `prompts.py` practitioner mode block | Spirit (Anvil/Forge) |
| **Code change** | Bot modules on Turtle | Spirit (Anvil/Forge) |
| **Spec change** | `TURTLE_SPEC.md` or flow files | Spirit + Mage |
| **No change** | Working as designed | Document why |

### 5. Present to Mage

Present findings as:

1. **Principles discovered** (numbered, one sentence each)
2. **Actions recommended** (grouped by type)
3. **What's working well** (don't only find problems)

Do NOT present:
- What the practitioner talked about
- Personal details or life content
- Direct quotes (unless they illustrate a UX point and are anonymizable)

### 6. Implement (with Mage approval)

For approved actions:
- Prompt changes: edit `prompts.py`, deploy to Turtle
- Code changes: edit relevant module, deploy to Turtle
- Spec changes: update the relevant document

After implementation, note what changed in the flow's output file.

## Output

### Principles File

Append new principles to `library/resonance/foundations/lore/practitioner_principles.md`:

```markdown
# Practitioner Design Principles

Extracted from real interactions. Each principle is general — not tied to any individual.

## Language & Tone
- [principles about communication style]

## Continuity & Memory
- [principles about cross-session awareness]

## Depth & Agency
- [principles about when to go deep, when to stay light]

## Session Lifecycle
- [principles about openings, closings, timeouts]

## Friction & Delight
- [principles about what breaks flow and what enables it]
```

### Run Log

Each run appends to `floor/practitioner-lens-log.md`:

```markdown
## Run — [date]
- Practitioner channels reviewed: [count]
- Messages analyzed: [count]
- Principles extracted: [count new, count confirmed]
- Actions taken: [list]
- Actions deferred: [list with reason]
```

## Guidance

- **Privacy is non-negotiable.** The Mage sees principles, not content. If a principle can't be stated without revealing practice content, generalize further.
- **Small sample, big signal.** Even 10 messages can reveal a prompt gap. Don't wait for statistical significance.
- **Confirm before changing.** Principles inform; the Mage decides what to change.
- **Accumulate, don't replace.** Each run adds to the principles file. Principles that keep getting confirmed are strong. Principles that get contradicted should be revised, not deleted.
- **The bot is the intervention.** This flow doesn't change the practitioner's experience directly — it changes the bot, which changes every practitioner's experience.
