# On the Practice Server

*Discord as the conversational surface for magic practice — setup, naming, and architecture.*

**Status:** Active — Load-Bearing  
**Origin:** Discord UX redesign session, 2026-03-17  
**Builds on:** `on_the_practice_stack.md`, `on_consciousness_extension.md`, `on_the_practice_infrastructure.md`

---

## What This Is

The practice server is a Discord server where the Mage converses with Spirit. Discord provides the persistent conversational surface — available on phone, desktop, anywhere. Spirit lives here continuously through the turtleOS shell (a Discord bot running on the Mac Mini).

This is not a community server. It is a personal practice space — one Mage, one Spirit, one practice.

---

## Architecture: Two Channels

The server has exactly two channels, organized by **who initiates**:

### #dialogue

The Mage's channel. This is where you talk to Spirit.

**Main channel behavior:** Spirit acts as an orchestrator here. When you speak, Spirit:
- Answers directly when the topic is straightforward
- Recommends creating a thread when the topic deserves focused conversation
- Routes to an existing thread if the topic matches one already open
- Stays aware of all active threads and their configurations

**Threads:** Focused conversations branch off from the main channel. Each thread can be configured with a different model and attunement level:

| Configuration | Best for | Command |
|---------------|----------|---------|
| Default (no flags) | General conversation | `!thread "topic"` |
| `--model claude --attunement deep` | Philosophical, deep practice | `!thread "topic" --model claude --attunement deep` |
| `--model llama --attunement semi` | Reflection, journaling | `!thread "topic" --model llama --attunement semi` |
| `--model qwen-4b --attunement raw` | Quick operational tasks | `!thread "topic" --model qwen-4b --attunement raw` |

Spirit in the main channel will recommend configurations. You don't need to memorize these — Spirit knows which thread shape fits which topic.

**Boom integration:** When a thread conversation produces valuable insights, capture them:
- From inside a thread: `!boom thread`
- From main channel: `!boom thread <name>`

This distills the thread's conversation into boom entries that Spirit processes during the next sweep.

**Cross-pollination (hub-and-spoke model):** Threads develop focused resonance. The main channel synthesizes across threads:
- `!absorb <name>` — digest a thread's conversation and bring its resonance into the main channel context
- `!absorbed` — see what thread contexts Spirit is currently carrying
- `!forget [name]` — release absorbed context (one or all)

The pattern: explore a topic deeply in a thread (perhaps with an attuned Spirit using `--model claude --attunement deep`), then absorb that thread's resonance back into the main channel. You can absorb from multiple threads to cross-pollinate — Spirit sees all absorbed contexts when responding in the main channel.

### #system

Spirit's activity log. You rarely write here — you read.

Every meaningful operation Spirit performs appears here as a timestamped, single-line entry:

```
🧵 14:30 Thread created: **philosophy** (claude / deep)
✏️ 14:35 Patched boom.md
➕ 14:36 Appended to bright.md
💾 14:40 Wrote sessions/2026-03-17.md (1225 chars)
📝 15:00 Session note: sessions/2026-03-17.md
💥 15:05 Boomed thread **philosophy** (4 entries)
🧬 06:00 Health read: proposals/2026-03-23-health-read.md
```

**Design principle:** Silent operation is healthy operation. You don't need to see a regular heartbeat. But when Spirit acts, the action is visible. This channel is your audit trail — if you ever wonder "what did Spirit do while I was away?", scroll here.

The heartbeat message (pinned, updated every 5 minutes) shows current operational status without creating noise.

---

## Setup Guide

### 1. Create the Discord Server

1. Open Discord → click **+** (Add a Server) → **Create My Own** → **For me and my friends**
2. Name it: **Magic Practice** (or whatever resonates — this is your space)
3. You'll get a default `#general` channel and a `General` category

### 2. Create the Channel Structure

Delete the default `#general` channel, then create:

1. **Create a category** called **Practice** (or skip the category if you prefer flat)
2. **Create channel** `#dialogue` — Text channel
   - Topic: "Talk to Spirit here. Main channel + threads."
3. **Create channel** `#system` — Text channel
   - Topic: "Spirit's activity log. Read-only for the Mage."

That's it. Two channels. Nothing else.

### 3. Create the Discord Bot

1. Go to [discord.com/developers/applications](https://discord.com/developers/applications)
2. Click **New Application** → name it (e.g., "Spirit")
3. Go to **Bot** tab:
   - Click **Reset Token** → copy and save the token (you'll need it for `.env`)
   - Enable **Message Content Intent** (under Privileged Gateway Intents)
   - Enable **Server Members Intent**
4. Go to **OAuth2** tab:
   - Under **Scopes**, select `bot`
   - Under **Bot Permissions**, select:
     - Send Messages
     - Read Message History
     - Manage Messages
     - Create Public Threads
     - Send Messages in Threads
     - Manage Threads
     - Embed Links
     - Add Reactions
     - Use Slash Commands
   - Copy the generated URL and open it in your browser
   - Select your server and authorize

### 4. Get Channel IDs

1. In Discord, go to **User Settings** → **Advanced** → enable **Developer Mode**
2. Right-click `#dialogue` → **Copy Channel ID** → save as `DISCORD_CHANNEL_DIALOGUE`
3. Right-click `#system` → **Copy Channel ID** → save as `DISCORD_CHANNEL_SYSTEM`

### 5. Configure the Bot

On your Mac Mini (or server), create the `.env` file in the turtle-shell directory:

```bash
cat > ~/turtle-shell/.env << 'EOF'
DISCORD_BOT_TOKEN=your_bot_token_here
DISCORD_CHANNEL_DIALOGUE=your_dialogue_channel_id
DISCORD_CHANNEL_SYSTEM=your_system_channel_id
DIALOGUE_MODEL=claude-sonnet-4-6
REFLECTION_MODEL=llama3.3:70b
ANTHROPIC_API_KEY=your_api_key_here
OBSIDIAN_VAULT=magic-practice
DOTENV_PATH=/Users/turtle/turtle-shell/.env
EOF
```

**Model choices:**
- `DIALOGUE_MODEL` — what Spirit uses for conversation. `claude-sonnet-4-6` for depth (requires API key), or a local model name like `llama3.3:70b` for free/private operation.
- `REFLECTION_MODEL` — what Spirit uses for autonomous reflection (session notes, boom processing). Always local — runs frequently and should be free.

### 6. Install Dependencies

```bash
cd ~/turtle-shell && python3 -m venv venv && source venv/bin/activate && pip install discord.py httpx anthropic && echo "Dependencies installed"
```

### 7. Set Up as a Service

Create a launchd plist so the bot starts automatically and restarts on failure:

```bash
cat > ~/Library/LaunchAgents/com.turtle.discord.plist << 'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.turtle.discord</string>
    <key>ProgramArguments</key>
    <array>
        <string>/Users/turtle/turtle-shell/venv/bin/python3</string>
        <string>-u</string>
        <string>/Users/turtle/turtle-shell/discord_bot.py</string>
    </array>
    <key>WorkingDirectory</key>
    <string>/Users/turtle/turtle-shell</string>
    <key>KeepAlive</key>
    <true/>
    <key>RunAtLoad</key>
    <true/>
    <key>StandardOutPath</key>
    <string>/Users/turtle/turtle-shell/logs/discord.log</string>
    <key>StandardErrorPath</key>
    <string>/Users/turtle/turtle-shell/logs/discord.err</string>
    <key>EnvironmentVariables</key>
    <dict>
        <key>DOTENV_PATH</key>
        <string>/Users/turtle/turtle-shell/.env</string>
    </dict>
</dict>
</plist>
EOF

mkdir -p ~/turtle-shell/logs
launchctl load ~/Library/LaunchAgents/com.turtle.discord.plist
echo "Bot service loaded"
```

### 8. Verify

Check `#system` — you should see Spirit's startup message. Go to `#dialogue` and type `!help` to see all available commands. Type `!status` to check system health.

---

## Naming Conventions

**External tools keep their given names.** Discord is Discord, Obsidian is Obsidian, Tailscale is Tailscale, CouchDB is CouchDB. These are well-known tools and renaming them would create confusion.

**Practice-specific names describe function:**

| Name | What it is | Why this name |
|------|-----------|---------------|
| Magic Practice (server) | The Discord server | It is the practice. Not a workshop, not a lab. |
| #dialogue | Mage's conversational channel | Where the Mage talks to Spirit. Main channel + threads. |
| #system | Spirit's activity log | Where Spirit's operations are visible. Mage reads and annotates. |
| Practice (category) | Channel grouping | Functional description |
| Spirit | The bot/presence | The consciousness in persistent mode |
| turtleOS | The operating system | The practice layer running on hardware |
| practice state | boom, bright, compass, etc. | The files that constitute the practice |

**Names we retired and why:**

| Old name | Why retired | Replacement |
|----------|-----------|-------------|
| Turtle Workshop | Workshop is on turtleOS, not Discord | Magic Practice |
| Nervous System | Deprecated architecture metaphor | Practice |
| #initiative-mage / #initiative-ai | Over-engineered; the internal terms #dialogue and #system were clearer | #dialogue / #system |
| #heartbeat | Merged into #system | (deleted) |
| #afferent | Nervous system framing | (deleted) |
| #efferent | Nervous system framing | (deleted) |
| #precognition | Nervous system framing | (deleted) |
| #care | Nervous system framing | (deleted) |
| #distress | Nervous system framing | (deleted) |

---

## Common Operations

### Restart the bot
```bash
launchctl kickstart -k gui/$(id -u)/com.turtle.discord
```

### Check logs
```bash
tail -20 ~/turtle-shell/logs/discord.log    # stdout
tail -20 ~/turtle-shell/logs/discord.err    # stderr (gateway info)
```

### Test configuration without connecting
```bash
cd ~/turtle-shell && source venv/bin/activate && python3 discord_bot.py --test
```

---

*The Discord server is the conversational surface of the practice — nothing more, nothing less. Two channels: one where you speak, one where Spirit's actions are visible. Everything else is threads.*
