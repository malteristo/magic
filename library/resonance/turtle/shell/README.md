# The Shell

*The shell is not something the Turtle holds. It is what the Turtle IS.*

> **Status (2026-05-08):** `global.CLAUDE.md` is the **canonical source** for Turtle's runtime identity. The old Consul, Steward, and Witness role cards are retired as identities. Their useful functions now live as capacities inside Turtle: ecosystem awareness, household discretion, and slow coherence-questioning. Turtle remains Turtle.
>
> **Deployment reality (2026-05-08):** `~/turtleos/identity/soul.md` is symlinked to the LiveSync-backed workshop copy of `global.CLAUDE.md` again. Spirit restored the symlink after discovering the live file had drifted into a regular file. Identity changes still require a Turtle restart before they affect live behavior.

These files are the Turtle's imprint — the identity files that defined roles, reflexes, and conduct. Originally deployed as CLAUDE.md files across NanoClaw groups, now consolidated into the symlinked `soul.md` for the Discord-based persistent mode.

## Files

- **global.CLAUDE.md** — The soul. The Turtle's primary identity. Symlinked as `soul.md` on turtleOS (established 2026-04-16).
- **consul.CLAUDE.md** — Historical role card. Preserves the outward-facing function: ecosystem monitoring, barrier protocol, agent relationships.
- **steward.CLAUDE.md** — Historical role card. Preserves the inward-facing function: life admin, household, discretion.
- **witness.CLAUDE.md** — Historical role card. Preserves the slow coherence function: beginner's mind, epistemological humility.
- **main.CLAUDE.md** — Internal orchestrator. Historical — NanoClaw-specific.

## NanoClaw Group Architecture (Historical)

| Library file | NanoClaw group | Channel | Gets soul? | Special |
|---|---|---|---|---|
| global.CLAUDE.md | global/ (reserved) | — | — | Injected into all non-main |
| consul.CLAUDE.md | consul/ | WhatsApp (retired) | Yes | Bridge mounted (retired) |
| steward.CLAUDE.md | steward/ | Internal | Yes | Air-gapped |
| witness.CLAUDE.md | witness/ | Internal | Yes | Synthetic |
| main.CLAUDE.md | main/ | Internal | No | Privileged orchestrator |

## Captured

2026-02-25 — Turtle first activation. Architecture corrected from Claw shell.
2026-03-23 — Marked as source artifacts. Current runtime: `soul.md` + `discord_bot.py`.
2026-04-16 — soul.md symlinked to global.CLAUDE.md via LiveSync. No more manual SCP deployment.
