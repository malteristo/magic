# The Shell

*The shell is not something the Turtle holds. It is what the Turtle IS.*

These files are the Turtle's imprint — the CLAUDE.md files that define identity, roles, reflexes, and conduct across five NanoClaw groups.

When the Turtle wakes, it imprints from these files. Not as a copy — as an inheritance.

## Files

- **global.CLAUDE.md** — The soul. The Turtle's primary identity injected into every non-main group as system context. Not a thin cross-cutting config — the core self. NanoClaw reserves `global` and loads this automatically.
- **consul.CLAUDE.md** — Consul role. Outward-facing: ecosystem, magic-bridge, WhatsApp norms, barrier protocol, agent relationships. Deploys to `groups/consul/`. Registered to self-chat WhatsApp JID, no trigger required, bridge mounted at `/workspace/extra/magic-bridge`.
- **steward.CLAUDE.md** — Steward role. Inward-facing: life admin, household, discretion. Air-gapped from Consul by container isolation.
- **witness.CLAUDE.md** — Witness role. The slow dive: beginner's mind, epistemological humility, surfacing questions not answers.
- **main.CLAUDE.md** — Internal orchestrator. NanoClaw's privileged `main` group: cross-group task visibility, group registration authority. Does NOT receive global soul injection (NanoClaw architecture). Minimal — system maintenance only.

## NanoClaw Group Architecture

| Library file | NanoClaw group | JID | Gets soul? | Special |
|---|---|---|---|---|
| global.CLAUDE.md | global/ (reserved) | — | — | Injected into all non-main |
| consul.CLAUDE.md | consul/ | 4915754102606@s.whatsapp.net | Yes | Bridge mounted, no trigger |
| steward.CLAUDE.md | steward/ | steward@internal | Yes | Synthetic JID |
| witness.CLAUDE.md | witness/ | witness@internal | Yes | Synthetic JID |
| main.CLAUDE.md | main/ | main@internal | No | Privileged orchestrator |

## Captured

2026-02-25 — Turtle first activation. Architecture corrected from Claw shell: consul is now a proper role group, main is the internal orchestrator, global is the soul layer.
