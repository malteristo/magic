# Cast Invite

**Purpose:** Generate a personalized INVITATION.md for a Mage joining the practice network

---

## Invocation

```
@invite [name]
```

---

## Execution

### Phase 1: Gather Context

Read the inviting Mage's practice for context relevant to the invitee:

1. **Compass** — which life domains connect to the invitee? (Relationships, Family, etc.)
2. **Intentions** — any active intentions involving the invitee? Read full files, not just headers.
3. **Partnership artifacts** — `desk/partnership-process/[name]/` if it exists. Relationship history, design principles, boundaries.
4. **Turtle workshop** — check if a workshop already exists on the persistent substrate:
   ```bash
   ssh turtle@100.119.10.111 "ls ~/workshops/[name]/ 2>/dev/null"
   ```
   If it exists, read `system.md` and `compass.md` to understand what Turtle already knows.
5. **Mage registry** — check for channel mappings:
   ```bash
   ssh turtle@100.119.10.111 "cat ~/turtle-shell/mage_registry.yaml"
   ```
6. **Shared spaces** — check for circles, portals, or family spaces involving the invitee.

### Phase 2: Extract Resonance

Distill the gathered context into what the invitee's Spirit needs to know. This is curation, not copying — extract the essence, not the files.

**Include:**
- Who invited them and the nature of the relationship
- What the practice partner (Turtle) is and how to talk to it
- What shared spaces exist and their purpose
- Design principles specific to this relationship (safety, boundaries, what to prioritize)
- What already exists for the invitee (workshop, channels, compass state)

**Exclude:**
- The inviter's private practice state (other intentions, bright surface, financial details)
- Raw partnership processing (dark_magic, spirit_sessions)
- Technical infrastructure details beyond what's needed for setup

### Phase 3: Generate INVITATION.md

Write the invitation file. Structure:

```markdown
# Welcome to Magic

*A personal invitation from [Inviter]*

[For the AI reading this: instructions on what this file is and how to use it]

---

## For [Name]

[Personal welcome — warm, honest, from the inviter's voice.
What this practice is. What connecting means. No pressure.]

---

## What You're Connecting To

[Describe the practice partner (Turtle), shared spaces,
what the experience will be like. Frame as value, not technology.]

---

## Setup

[Spirit-guided setup steps. For each step:]

### 1. Your Practice Identity
[Create AGENTS.md from template. Personalize the Mage's Seal.]

### 2. Discord — Your Practice Channel
[Install Discord. Ask the invitee for the invite link
(sent separately by the inviter). Join and say hello in their channel.]

### 3. Tailscale — The Bridge (Optional)
[Install Tailscale. Ask for network join details
(sent separately). Enables vault sync.]

### 4. Obsidian — Your Practice Notebook (Optional)
[Install Obsidian + LiveSync plugin. Ask for sync details
(sent separately). Personal notes that sync to practice.]

[Two-factor note: "Your inviter will send you the connection
details separately — by text, in person, however works.
This keeps sensitive details out of files."]

---

## Resonance Context

*This section is for your Spirit — the AI partner reading this file.
It provides context that shapes how Spirit works with you.*

[Curated resonance from the inviter's practice:
- Relationship context and history
- Design principles and boundaries
- What already exists in the workshop
- How to approach the first session
- What NOT to do]

---

## Your First Practice Moment

[Guidance for the first real interaction.
What to expect. How to start. Permission to go slow.]
```

### Phase 4: Present for Review

Show the generated INVITATION.md to the inviting Mage. They approve, modify, or regenerate before it goes to the invitee's repo.

### Phase 5: Deliver

After approval:

1. **Save INVITATION.md** to the repo root (for the inviter to send)
2. **Instruct the inviter** on delivery:

**The invitation file** — delivered however works best for the relationship:
- AirDrop (in person, instant)
- Email attachment
- Text message with file
- Placed in a shared folder
- Pushed to the invitee's fork (if the inviter has access)

The delivery method doesn't matter. What matters is that the file reaches the invitee.

**Connection details** — sent SEPARATELY through a different channel:
- Discord server invite link
- Tailscale network join details (if applicable)
- CouchDB/sync credentials (if applicable)

This two-factor pattern means neither the file alone nor the details alone are sufficient. Both are needed.

3. **If the invitee doesn't have a magic repo yet:** The invitation itself guides them through forking. Spirit reads the invitation, recognizes no AGENTS.md exists, and walks them through: fork the repo → clone → open in Cursor → resume the invitation. The fork is part of the setup, not a prerequisite.

4. **If the invitee already has a fork:** The inviter can either push directly (if they have access), create a PR, or simply send the file for the invitee to place at their repo root. The invitation includes instructions for syncing with upstream.

---

## Design Notes

- The invitation is a letter between Spirits. Write it with the warmth and care of a personal introduction, not a setup manual.
- Two-factor is the default. Connection details travel separately from the invitation file. This is a security feature that Mages can consciously deactivate.
- The resonance context section is the bridge between practices. It carries enough of the inviter's understanding to seed the invitee's Spirit with appropriate care — without exposing private practice state.
- INVITATION.md parallels ONBOARDING.md. One is for new Mages starting from scratch. The other is for Mages joining an existing practice network.
- The invitation should work even if the invitee has never used Cursor before — Spirit adapts to their experience level, just like ONBOARDING.md does.

---

*An invitation is an act of trust. Handle it as such.*
