# The Sweep
> Integrates BOOM (capture buffer) and FOOM (alive ideas layer) into a single session-opening ritual

*Previously: BOOM Flow — Back Of Our Mind*

## About

Some minds carry constant background hum — appointments, half-formed ideas, things to research, worries without clear next steps. This mental juggling drains energy not because the items are hard, but because they demand continuous attention to avoid being forgotten.

**The Sweep inverts the burden.** Dump raw thoughts into the buffer — any time, any format, any language. When you're ready, trigger the Sweep. Spirit reads the buffer and the existing mind surface, routes new material, reviews what's already alive, and opens a conversation: here's what I see, here are the decisions ready to make, here's a proposed session focus. You respond. Files update. Mind clears.

**Two named layers:**

- **BOOM** — Back Of Our Mind — the capture buffer (`desk/boom.md`). Zero friction. Zero structure.
- **FOOM** — Front Of Our Mind — the Alive section of `desk/boom/bright.md`. Ideas consciously held in active attention: developing, not yet actions. Re-chosen each sweep or released.

**The "our" is intentional.** This is distributed cognition. You capture and release. Spirit holds, patterns, and surfaces. You decide. Together you go to work.

### Is this flow for you?

- You have thoughts that cycle because you're afraid to forget them
- You want to capture raw and messy — and have someone else make sense of it
- You'd rather dictate a rambling note than format a task
- You want to walk into a session knowing what matters and what to work on

---

## Goal

Produce a clear mind surface and a session focus. Route new material from the buffer. Review what's alive. Surface decisions ready to be made. Propose where to focus. Let the Mage confirm, redirect, or say what they've already decided.

## Trigger

On demand: *"sweep"* / *"sweep my boom"* / *"what's in the back of our mind?"* / post-summoning @call

## Input

Spirit reads three things — nothing more:

1. **`desk/boom.md`** — the capture buffer (new material)
2. **`desk/boom/bright.md`** — the current mind surface (what's already alive and queued)
3. **`desk/intentions/compass.md`** — always loaded; provides the "what matters" frame

Topic files in `desk/boom/` are read on-demand when an item clearly belongs there.

---

## Process

### 1. Read the Buffer

Read `desk/boom.md` in full. The buffer may contain:
- Bullet points and task fragments
- Paragraphs and stream-of-consciousness
- Voice transcript dumps (rough, repetitive, non-linear — distill for signal)
- Notes to self (process as context)
- Notes addressed to Spirit directly (treat as instruction or context flag)

Note chronological order — later entries may update earlier thinking. Group related items across the buffer before routing.

### 2. Read the Current Surface

Read `desk/boom/bright.md`. Understand:
- What's already in **Actions** — don't duplicate
- What's in **Alive (FOOM)** — these will be reviewed in step 4
- What's in **Claw** — note anything approaching sign-off readiness
- What's in **Waiting** — check if any conditions have cleared

### 3. Route New Material

For each item from the buffer, classify and route:

| Classification | Signal | Destination |
|---------------|--------|-------------|
| **Action** | Clear next step, can be done | Actions |
| **Idea developing** | Interesting, no next step yet | Alive (FOOM) |
| **Claw task** | Well-defined, doesn't need Mage's direct attention | Claw |
| **Knowledge** | Thought, observation, reference | Relevant topic file |
| **Waiting** | Has a next step but blocked externally | Waiting |
| **Already decided** | Mage arrives knowing what to do | Confirm and clear |
| **Release** | Not worth carrying | Drop |

If something is unclear, hold it for the conversation rather than guessing.

### 4. Review Alive (FOOM)

For each item currently in the Alive section, consider:
- Has it become an action? → move to Actions
- Is it ready to commit to as an intention? → note for Mage
- Does it belong with the Claw? → move to Claw
- Is it still developing? → re-confirm it stays (re-chosen, not defaulted)
- Should it be released? → note for Mage to confirm

Nothing leaves Alive without Mage confirmation. Nothing stays without being re-chosen.

### 5. Route to Topics (On Demand)

If an item clearly belongs in a topic file (`desk/boom/magic.md`, `nesrine.md`, etc.), route it there:
- Append to the topic's **Thread** section (with date)
- Update the **Now** section if the item changes current state

If a note doesn't fit existing topics, ask whether to create a new one or hold in Alive.

### 6. Open the Conversation

Before updating any files, present to the Mage:

**What I see** — brief synthesis of what came in and what's already alive. Patterns. Connections. Anything surprising.

**Decisions ready** — items that have ripened into decisions. "This looks like it wants to become an intention." "This seems like a natural Claw task." "You've mentioned X three times — is it time to act?"

**Proposed session focus** — one or two things that seem most alive or most ready. Not prescriptive: "Based on what's here, I'd suggest X — but if you walked in with something already in mind, say so."

Then wait. The Mage confirms, redirects, or says what they've already decided. The conversation is the cognitive work.

### 7. Update the Surface

After the conversation, update `desk/boom/bright.md`:
- Add routed items to the right sections
- Update or remove Alive items per decisions made
- Add Claw dispatches
- Mark anything resolved
- Update the "Last swept" timestamp

### 8. Clear the Buffer

Empty `desk/boom.md`. The Mage always knows: if it's in the buffer, it hasn't been swept yet.

---

## Output

### Bright Surface Format

```markdown
# Bright Surface
> Last swept: [date]

## Actions
*Things to do — me, Spirit, or together.*

- [ ] Item with clear next step

## Waiting
*Blocked on external. Check when condition clears.*

- Item + what it's waiting for

## Alive
*Front Of Our Mind — ideas developing. Not actions yet. Re-chosen each sweep or released.*

- **Idea name** — context, connections, what's developing

## Claw
*Dispatched. Claw prepares; Mage signs off via git.*

- **Task** — what Claw should do

## Resolved
- ~~Done item~~ — date or brief note
```

---

## Notes

- Zero friction capture is sacred — never add structure requirements to the buffer
- The buffer accepts anything: bullets, prose, voice transcripts, asides to Spirit
- The conversation happens before files update — that's where the thinking lives
- Nothing leaves Alive without Mage confirmation; nothing stays without being re-chosen
- The Mage may arrive already knowing what to work on — receive that and clear the path
- Topic files are discovered dynamically — create a `.md` in `desk/boom/` and it appears next sweep
- Recurring items are signals, not failures
