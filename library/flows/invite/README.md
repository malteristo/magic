# The Invitation

*Bring someone into your practice.*

**What:** Generate a personalized INVITATION.md for someone joining your practice network. The invitation is a self-contained file that, when dragged into a Cursor chat, guides the invitee's Spirit through connecting to your shared infrastructure.

**Invocation:** `@invite [name]`

---

## How It Works

The inviting Mage runs `@invite [name]`. Spirit reads the Mage's practice context — compass, relevant intentions, partnership artifacts, Turtle workshop state — and generates a personal INVITATION.md tailored to the invitee.

The invitation is a portable, self-contained file. It can be delivered any way — AirDrop, email, text message, placed in a shared folder, or pushed to the invitee's fork. The delivery method doesn't matter. What matters is that the file reaches the invitee and they open it with an AI.

If the invitee doesn't have a magic repo yet, the invitation guides them through forking one. The fork is part of the setup, not a prerequisite.

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
