# On Discord Navigation from Cursor

*How Spirit accesses Discord content when working alongside Turtle.*

## The Instrument

Turtle's workshop includes `discord_ops.py` — a CLI for reading and writing Discord from SSH.

```bash
ssh turtle@<turtle-ssh> "cd ~/turtleos && ./venv/bin/python3 discord_ops.py <op> <channel_id> [args]"
```

**Operations:**
- `read <channel_id> [limit]` — read recent messages (default 20)
- `send <channel_id> <text>` — send a message
- `threads <channel_id>` — list active threads in a channel (returns thread IDs and message counts)
- `help` — show usage

## Channel IDs

The source of truth is `~/turtleos/mage_registry.yaml`. Key channels:

| Channel | ID | Workspace |
|---|---|---|
| #river (kermit) | <channel-id> | ~/workshop/desk |
| #nesrine-dialogue | <channel-id> | ~/workshops/nesrine |
| #family (forum) | <channel-id> | ~/workshops/family |

*Single-river model: operations post inline in the river channel. No separate system/heartbeat/afferent channels — those were part of the earlier multi-channel architecture and have been dissolved.*

## Forum Threads

Forum channels (like #family) contain threads, not direct messages. To read a thread:

1. Get thread IDs: `discord_ops.py threads <parent_channel_id>`
2. Read thread: `discord_ops.py read <thread_id> [limit]`

The thread ID is what you pass to `read`, not the parent forum channel ID.

## Anti-Patterns (Learned the Hard Way)

**Don't** improvise ad-hoc Python scripts over SSH to hit the Discord API.
- The `requests` library is not installed in Turtle's venv; `httpx` is, but this is fragile.
- The bot token env var is `DISCORD_BOT_TOKEN` (not `DISCORD_TOKEN`).
- SSH-piped Python has quoting nightmares. `discord_ops.py` handles all of this.

**Don't** guess channel IDs. Read `mage_registry.yaml` or run `discord_ops.py help`.

**Don't** start the bot with `nohup ... &`. The bot is managed by launchd (`com.turtle.discord`) with
`KeepAlive: true`. Starting a manual instance creates a duplicate — every message gets two responses.

## Bot Management

The bot runs as a launchd service. To restart after code changes:

```bash
ssh turtle@<turtle-ssh> "launchctl stop com.turtle.discord && sleep 2 && launchctl start com.turtle.discord"
```

To verify single process: `ps aux | grep discord_bot | grep -v grep` — should show exactly one PID.

**Logs:** `~/turtleos/logs/discord.log` (stdout) and `~/turtleos/logs/discord.err` (stderr).
**Plist:** `~/Library/LaunchAgents/com.turtle.discord.plist`.

## Environment Notes

- **Python venv:** `~/turtleos/venv/` (use `./venv/bin/python3`)
- **Bot token:** `DISCORD_BOT_TOKEN` in `~/turtleos/.env`
- **Bot code:** `~/turtleos/discord_bot.py` (~3600 lines)
- **Registry:** `~/turtleos/mage_registry.yaml`
