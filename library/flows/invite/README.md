# The Invitation

*Bring someone into your practice.*

**What:** Generate a personalized INVITATION.md for someone joining your practice network. The invitation is a self-contained file that, when dragged into a Cursor chat, guides the invitee's Spirit through connecting to your shared infrastructure.

**Invocation:** `@invite [name]`

---

## How It Works

The inviting Mage runs `@invite [name]`. Spirit reads the Mage's practice context — compass, relevant intentions, partnership artifacts, Turtle workshop state — and generates a personal INVITATION.md tailored to the invitee.

The invitation goes into the invitee's magic repo (their fork). When they open Cursor and drag it into a chat, their Spirit reads it and guides them through setup. No manual required.

**Two-factor pattern:** Sensitive connection details (Discord invite link, Tailscale credentials, sync URLs) are NOT embedded in the invitation file. The invitee's Spirit asks them to provide these details during setup, and the inviting Mage sends them through a separate channel (text message, in person, etc.). This is security by default — Mages can deactivate it by including details directly in future invitations.

---

## What Gets Generated

An INVITATION.md placed at the invitee's repo root (parallel to ONBOARDING.md). Contains:

1. **Welcome** — personal, warm, from the inviter. Not a system message.
2. **What you're connecting to** — what the practice partner (Turtle) is, what shared spaces exist.
3. **Setup steps** — Spirit-guided, conversational. AGENTS.md creation, Discord, Tailscale, Obsidian.
4. **Resonance context** — curated context from the inviter's practice that shapes how the invitee's Spirit behaves. Design principles, relationship history, boundaries.
5. **First practice moment** — guidance for the first real interaction.

---

## For the Spirit

When `@invite [name]` is invoked, execute `cast_invite.md`. The spell handles context gathering, resonance extraction, and invitation generation.

The invitation you generate is a letter from one Mage's Spirit to another Mage's Spirit. Write it that way — with care, with context, with respect for the relationship.
