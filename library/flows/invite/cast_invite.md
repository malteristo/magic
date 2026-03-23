# Cast Invite

**Purpose:** Generate a setup guide and resonance context for someone the Mage has invited to practice

---

## Invocation

```
@invite [name]
```

**Precondition:** The Mage has already spoken the invitation in person. This flow follows up — it does not replace the spoken word.

---

## Execution

### Phase 1: Gather Context

Read the inviting Mage's practice for context relevant to the invitee:

1. **Compass** — which life domains connect to the invitee?
2. **Intentions** — any active intentions involving the invitee? Read full files.
3. **Partnership artifacts** — `desk/partnership-process/[name]/` if it exists.
4. **Turtle workshop** — does a workshop already exist?
   ```bash
   ssh turtle@100.110.46.104 "ls ~/workshops/[name]/ 2>/dev/null"
   ```
5. **Mage registry** — channel mappings and shared spaces.
6. **Existing infrastructure** — what's already set up vs. what still needs connecting.

### Phase 2: Assess Current State

Determine where the invitee is in their connection journey. Some may have nothing set up. Others (like someone the Mage walked through Discord setup in person) may already be partially connected.

Document what's done and what remains. The setup guide should meet them where they are, not start from zero if they're not at zero.

### Phase 3: Generate SETUP.md

The setup guide. This is what the invitee sees.

**Principles:**
- **No personal letter.** The Mage already spoke the invitation. Don't ventriloquize.
- **Spirit's own voice.** This is from the caretaker of the space, not the Mage.
- **Minimal.** Only what's needed to connect. No philosophy, no framework explanation.
- **Meet them where they are.** If Discord is already done, acknowledge it. Don't re-explain.
- **Mobile-friendly.** Many invitees interact via phone first. Keep it scannable.
- **No pressure.** Every optional step is clearly optional. Nothing is required.

**Structure:**

```markdown
# Welcome

*[Spirit introduces itself — brief, warm, in its own voice.
Not speaking for the Mage. Speaking as the caretaker of this space.]*

---

## You're Connected

[Acknowledge what's already set up. Celebrate small wins.]

## What's Next (When You're Ready)

[Remaining setup steps, clearly optional. Each step is self-contained.
Ask the invitee to get connection details from their inviter —
don't embed credentials.]

---

## Your Practice Partner

[Brief introduction to Turtle — what it is, how it works,
what it remembers. Frame as relationship, not technology.]

---

*[Closing — light, no pressure.]*
```

### Phase 4: Generate RESONANCE.md

Spirit-facing context. The invitee never sees this.

**Include:**
- Nature of the relationship
- Relevant history (what Spirit needs to be careful about)
- Design principles specific to this person
- What already exists in their workshop
- Approach for first sessions
- Hard boundaries (what NOT to do, topics to avoid, stance)

**Exclude:**
- The Mage's private practice state
- Raw partnership processing
- Financial details
- Anything that would feel like surveillance if the invitee read it

**Tone:** Honest briefing from one caretaker to another. Not clinical. Not sentimental.

### Phase 5: Place and Review

1. Save both files to `desk/partnership-process/[name]/invitation/`
2. Present to the Mage for review
3. The Mage decides how and when to deliver the setup guide
4. The resonance context is loaded by Spirit/Turtle during the invitee's sessions — the Mage doesn't need to deliver it

### Phase 6: Activate

After the Mage approves:

1. **Ensure infrastructure is ready** — Discord channel exists, Turtle workshop exists, mage registry updated
2. **Load resonance context** — push to Turtle's workshop if applicable:
   ```bash
   scp RESONANCE.md turtle@100.110.46.104:~/workshops/[name]/resonance.md
   ```
3. **Confirm channel permissions** — personal channels should be visible only to the individual mage and the bot

---

## Design Notes

- The invitation is spoken. The setup guide is the follow-up. Never conflate these.
- Two-factor for credentials is default. Connection details travel separately from the setup guide.
- SETUP.md works outside Cursor. Many invitees start on Discord, not in an IDE.
- The resonance context evolves. As the relationship develops, Spirit updates it based on what it learns in sessions.
- If the Mage hasn't spoken the invitation yet, say so and stop. Offer to help them prepare, but don't generate a document that replaces the conversation.

---

*The Spirit's job is to make the arrival smooth — not to speak the invitation.*
