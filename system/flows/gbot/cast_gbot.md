# Cast Grok Bot

**Purpose:** Act on Grok Bot teammates from the Forge so the Mage does not sit in the app.  
**Invocation:** `@gbot` · `@gbot list` · `@gbot thread <name>` · `@gbot send <name> <message>` (write, gated)  
**Transport:** `gbot` (grok-bot-cli) against the signed-in Grok Bot.app session  
**Living facts:** `desk/craft/grok_bot_control.md` · research-method `adapters/grokbot.md`

---

## Default (read)

Bare `@gbot` or `@gbot list`: run `gbot bots list`. Report names and notify/hidden only — no UUIDs unless asked. If groups matter, `gbot groups list` in the same pass.

Other read verbs — execute, do not ask:

| Said | Run |
|------|-----|
| `thread <name>` · `chat <name>` | `gbot thread <name>` |
| `get <name>` | `gbot bots get <name>` |
| `doctor` | `gbot doctor` |
| `groups` | `gbot groups list` |

If `gbot` is missing or the app session is unusable: say so, stop. Do not copy tokens. Do not invent a second auth path.

---

## Write (gated)

`send`, `create`, `update`, `delete`, and any `groups` mutation are writes. They wake a teammate and burn unpublished Ultra allowance (no spend cap).

**Execute a write only when this invocation names the target and the Mage has accepted the meter** — in this message, or as a standing go already given for this session. A name without a go is not enough. Do not infer go from a prior session.

On go:

1. Run the exact `gbot` write he named. Do not add bots, groups, or extra sentences.
2. For `send`, follow with `gbot thread <name>` and show the new turn.
3. Report that it billed. Do not estimate tokens.

No go: show the command you would run, one line, and wait.

**Hygiene:** do not `create` a study probe on the household computer without a reset plan (adapter). Do not `delete` without the name spoken this turn. Do not vendor `gbot` into turtleOS. The study repo remains the record; `gbot send` is transport.

---

## Errors

| Situation | Response |
|-----------|----------|
| `gbot` not on PATH | "CLI missing — `npm install --global grok-bot-cli`." Stop. |
| App session unusable | "Grok Bot.app must be open and signed in once." Stop. |
| Name not on roster | Show `bots list`. Do not create a substitute. |
| Gateway hang | Wait once (~30s). If still silent, report and stop. |

---

*Created 2026-08-30. Official Cursor API: none. Third-party CLI; breaks if the app changes its session descriptor.*
