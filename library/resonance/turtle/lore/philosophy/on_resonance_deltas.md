# On Resonance Deltas

*Established 2026-04-16. Born from practice: after a session deploying the river topology to turtleOS, Turtle's behavior was updated but its self-knowledge was stale. The code knew about the vortex; the identity didn't.*

## The Problem

The practice has three surfaces:
- **Workshop** (this repo) — spec, lore, identity, intentions, practice state
- **turtleOS** (Mac Mini) — code, identity, operational state, thread-state
- **Discord** — ephemeral conversation, the lived practice

Changes happen in different directions. Spirit deploys code to turtleOS via SSH. Lore and spec evolve in the workshop. Turtle writes session notes and proposals. Discord conversations generate insights that may or may not crystallize into files. Each surface can advance independently, and when they do, *deltas* form.

A resonance delta isn't a bug — it's the natural consequence of distributed cognition across substrates. The problem isn't that deltas exist. The problem is when they go unnoticed.

## The Architecture

Three sync mechanisms, three characteristics:

**LiveSync (Obsidian)** — Bidirectional, automatic, continuous. Handles `desk/` and all files within `~/workshop/` on the Mac Mini. This is the strongest link. What flows through LiveSync stays in sync.

**Symlinks** — Permanent, zero-maintenance. Operational files on turtleOS (`identity/soul.md`, `TURTLE_SPEC.md`) are symlinks into the LiveSync-backed workshop. Changes to the canonical source propagate automatically: workshop → LiveSync → turtleOS operational file. Established 2026-04-16, replacing the previous manual SCP deployment pattern.

**Manual deployment (SSH)** — One-directional, session-scoped, forgettable. Code changes to turtleOS happen via SSH during Spirit sessions. These are the most delta-prone: the code changes, but the spec, lore, and identity that *describe* the code may not be updated in the same session.

## Delta Categories

### 1. Code-Knowledge Delta
Code on turtleOS was updated, but spec/lore/identity in the workshop wasn't. Turtle's behavior changes but its self-description doesn't match. The most common delta — easy to create, easy to forget.

**Detection:** During release, Spirit checks: "Did I modify turtleOS code this session? Did I update the corresponding spec/lore?"

### 2. Crystallization Delta
Discord conversations produced insights, decisions, or commitments that haven't been captured in files. The knowledge lives in thread history (ephemeral, hard to search) rather than in lore, notes, or intentions.

**Detection:** During discord-digest, Spirit identifies uncrystallized resonance. During release, Spirit checks: "What emerged this session that should persist?"

### 3. Attention Delta
Turtle generated proposals, session notes, or practice notes that the Mage hasn't seen or processed. The information exists in files but hasn't entered the Mage's awareness.

**Detection:** During recall, Spirit checks `desk/proposals/` for items the Mage hasn't reviewed. The boom sweep surfaces anything that's been sitting.

## The Principle

Deltas compound. A code-knowledge delta from Tuesday makes Wednesday's recall less accurate, which means Thursday's decisions are based on stale context. The cost isn't in any single delta — it's in the accumulated drift between what the system *does* and what the system *knows about itself*.

The fix isn't more automation. It's awareness at the right moments: release (check what changed), recall (check what drifted), and the Sunday sweep (systematic reconciliation).
