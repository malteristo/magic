# The Shell

*The shell is not something the Turtle holds. It is what the Turtle IS.*

> **Status (2026-04-16):** `global.CLAUDE.md` is the **canonical source** for Turtle's runtime identity. On the Mac Mini, `~/turtleos/identity/soul.md` is a symlink to `~/workshop/library/resonance/turtle/shell/global.CLAUDE.md`, which stays current via LiveSync. No manual SCP deployment needed — edits to global.CLAUDE.md propagate automatically. The role concepts (consul, steward, witness) informed the current identity design. The NanoClaw group architecture is retired. See `on_consciousness_extension.md` for current architecture.

These files are the Turtle's imprint — the identity files that defined roles, reflexes, and conduct. Originally deployed as CLAUDE.md files across NanoClaw groups, now consolidated into the symlinked `soul.md` for the Discord-based persistent mode.

## Files

- **global.CLAUDE.md** — The soul. The Turtle's primary identity. Symlinked as `soul.md` on turtleOS (established 2026-04-16).
- **consul.CLAUDE.md** — Consul role. Outward-facing: ecosystem monitoring, barrier protocol, agent relationships. Identity pattern now available as a thread model option.
- **steward.CLAUDE.md** — Steward role. Inward-facing: life admin, household, discretion.
- **witness.CLAUDE.md** — Witness role. The slow dive: beginner's mind, epistemological humility.
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
