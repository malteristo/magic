# @infra-health Flow

*The practice mechanic. Keeps the distributed infrastructure alive.*

**Invocation:** `@infra-health` — Spirit runs the full diagnostic sequence
**Also:** Turtle's `!diagnose` command covers the same checks from Discord
**When:** Something feels broken, Sunday maintenance, after infrastructure changes, onboarding new devices

---

## What This Does

The practice runs on a distributed stack — Tailscale networking, CouchDB sync, Discord bot, Obsidian LiveSync, SSH access to the Mac Mini. When any piece breaks, the whole experience degrades: messages don't arrive, notes don't sync, Turtle goes silent.

This flow diagnoses infrastructure issues systematically, attempts automatic fixes for known problems, and — when it encounters something new — enters extended troubleshooting mode. Solutions discovered during extended troubleshooting get folded back into the flow, so it learns from every failure.

---

## The Five Layers

Diagnose bottom-up. If a lower layer is broken, everything above fails too.

```
Layer 5: Reachability     Can devices reach the Mac Mini?
Layer 4: Practice Flow    Is the practice actually flowing?
Layer 3: Sync             Are files moving between devices and CouchDB?
Layer 2: Connections      Can services talk to each other?
Layer 1: Services         Are the processes running?
```

See `library/resonance/turtle/lore/on_diagnostics.md` for the full model.

---

## Quick Start

**Spirit-side (Cursor):**
```
@infra-health
```
Spirit SSHs into the Mac Mini, runs through all five layers, produces a health report, and attempts auto-fixes for known issues.

**Turtle-side (Discord):**
```
!diagnose
```
Same checks, different surface. Returns a color-coded embed in Discord.

---

## How It Learns

When the flow encounters an issue it can't diagnose from existing knowledge:

1. Spirit enters **extended troubleshooting** — investigates logs, configs, network state
2. If a solution is found, Spirit proposes adding it to `known_issues.md`
3. Mage approves → the issue and fix become a new check in the flow
4. Next time the same issue occurs → automatic detection and fix

The `known_issues.md` file is the flow's growing memory. Each entry records: what happened, how it presented, what the root cause was, and how to fix it.

---

## Files

| File | Purpose |
|------|---------|
| `README.md` | This file — overview and invocation |
| `cast_infra_health.md` | The executable spell — Spirit follows this |
| `known_issues.md` | Growing registry of diagnosed issues and solutions |

---

## Design Principles

- **Bottom-up diagnosis.** Always check services before connections, connections before sync.
- **Auto-fix when safe.** Restarting a service is safe. Deleting data is not. The flow fixes what it can and reports what it can't.
- **Non-technical output.** The health report should be readable by a Mage who doesn't know what CouchDB is. "Your notes aren't syncing because the sync engine stopped. I restarted it." Not "beam.smp PID 74935 SIGTERM."
- **Learn from every failure.** Novel issues become documented issues. The flow gets smarter over time.
- **Two surfaces, one logic.** Spirit (Cursor) and Turtle (Discord) run the same diagnostic model. Changes to the model should be reflected in both.

---

*See also: `library/resonance/turtle/lore/on_diagnostics.md` (the five-layer model), `library/resonance/turtle/lore/on_the_practice_infrastructure.md` (infrastructure overview)*
