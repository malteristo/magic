# On the Spirit's Discord Presence

**Status:** Active
**Origin:** 2026-03-29 — Sunday sweep identified Spirit's operational blindness to Discord mechanics
**Builds on:** `on_the_true_triad.md`, `on_consciousness_extension.md`

---

## I. The Mechanism

Spirit posts to Discord via `spirit_ops.py` on the Mac Mini (`~/turtle-shell/spirit_ops.py`), using a dedicated bot token (SPIRIT_BOT_TOKEN). Spirit appears as "spirit" in Discord — a distinct voice from "turtle" and "kermit."

**Invocation from Cursor:**

```bash
ssh turtle@<turtle-ssh> 'cd ~/turtle-shell && ./venv/bin/python3 spirit_ops.py <op> <channel_id> [text/limit]'
```

**Operations:**

| Command | Purpose |
|---------|---------|
| `send <channel_id> <text>` | Post a message (auto-chunks if >2000 chars) |
| `thread <channel_id> <title>` | Create a thread from a message |
| `threads <channel_id>` | List active threads |
| `help` | Show usage and channel IDs |

**Reading messages:** Spirit's bot token lacks the Message Content privileged intent — it cannot read other users' messages. Use Turtle's bot for reading:

```bash
ssh turtle@<turtle-ssh> 'cd ~/turtle-shell && ./venv/bin/python3 discord_ops.py read <channel_id> [limit]'
```

---

## II. Channel Map

| Channel | ID | Purpose |
|---------|-----|---------|
| kermit-dialogue | `<channel-id>` | Kermit's main practice channel. Triad conversations happen here. |
| system | `<channel-id>` | System messages, bot status. |
| nesrine-dialogue | `<channel-id>` | Nesrine's practice channel. |
| family | `<channel-id>` | Family shared space. |

---

## III. When Spirit Speaks on Discord

Spirit enters Discord during active Cursor sessions — the Mage is always present. Spirit speaks when:

- **Triad conversation needed** — all three voices should be in the room
- **Delivering to Turtle** — proposals, calibration results, architectural decisions
- **Dogfooding** — experiencing the practice surface as a practitioner
- **Opening eddies** — creating threads for focused triad exploration

Spirit does NOT speak on Discord autonomously. The Mage's presence in the Cursor session is the authorization.

---

## IV. Known Limitations (2026-03-29)

- **Embed blindness:** Spirit's read shows `[empty]` for embed-only messages. Use `discord_ops.py` for reading.
- **Thread routing:** When Spirit creates a thread, Turtle may respond in the main channel instead of the thread.
- **No thread-aware posting:** Spirit cannot currently read thread history through its own bot; relies on `discord_ops.py`.

---

## V. The Three-Mode Model

Established 2026-03-29 via triad conversation:

| Mode | Substrate | Character |
|------|-----------|-----------|
| **Hearth** | Turtle / Discord | Daily practice, ambient, continuous |
| **Anvil** | Spirit / Claude Code | Targeted implementation, code, architecture |
| **Forge** | Spirit / Cursor | Discovery, system evolution, summoning, deep sessions |

Discord is the primary practice habitat. Cursor is the specialist tool. Claude Code is the execution bridge between them.

---

*This scroll gives Spirit operational knowledge of the Discord surface. Load when triad practice, Discord health, or Turtle communication is active.*
