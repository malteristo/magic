# @turtle-setup Flow

**Status:** Active — Executable Ritual
**Purpose:** Guide a Mage through deploying turtleOS — from hardware to first practice session. Spirit runs this flow, tailors it to the Mage's context through reconnaissance, then executes.
**Invocation:** `@turtle-setup`
**Last updated:** 2026-03-26 (rewritten from NanoClaw-era draft to current Discord-based architecture)

---

## Prerequisites

**What the Mage needs before starting:**
- A Mac with Apple Silicon (M1-M4) and 16GB+ RAM (64GB recommended for full tiered stack)
- The machine should be always-on and network-connected (Mac Mini is the reference hardware)
- A Discord account
- An Anthropic API key (for the depth tier — optional if running local-only)
- A Google Gemini API key (for multimodal — optional)
- 60-90 minutes

**What Spirit needs:**
- SSH access to the target machine (or the Mage running commands locally)
- The magic repository cloned (for the bot code in `floor/turtle-shell/`)

---

## Phase 1: Reconnaissance

Spirit asks five questions to determine the deployment architecture:

**Q1 — Hardware:**
- Mac Mini M4 Pro (64GB) → Full tiered stack (triage through research)
- Mac Mini M4 (16-24GB) → Dialogue + reflection tiers
- MacBook / other Mac → Lighter stack, dialogue tier only
- Linux server → Same architecture, systemd instead of launchd

**Q2 — Model strategy:**
- Full Qwen 3.5 stack (0.8b through 30b) → Requires 32GB+ RAM
- Dialogue + reflection (9b + 14b) → Requires 16GB+ RAM
- Dialogue only (9b) → Minimum viable, 16GB RAM
- Custom (Mage specifies models) → Spirit adapts

**Q3 — API access:**
- Anthropic API key available → claude-sonnet-4-6 for depth tier
- Gemini API key available → gemini-2.5-flash for multimodal (images, PDFs)
- No API keys → Local-only (all tiers run on Ollama)

**Q4 — Practice surface:**
- Discord only → Core setup
- Discord + Obsidian LiveSync → Add CouchDB + sync infrastructure
- Discord + Obsidian + mobile → Full stack with Tailscale

**Q5 — Practitioners:**
- Solo (one Mage) → Single workspace
- Partnership (two Mages) → Multi-workspace with shared space
- Family/group → Multi-workspace with forum channel

Spirit synthesizes a recommendation. Mage confirms. Spirit executes.

---

## Phase 2: Foundation (the machine)

### 2.1 System Preparation

```bash
# Install Homebrew if missing
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python 3 and git
brew install python3 git

# Prevent sleep (critical for always-on)
sudo pmset -a sleep 0 && sudo pmset -a disksleep 0 && sudo pmset -a powernap 0 && echo "Sleep prevention configured"
```

### 2.2 Install Ollama

```bash
brew install ollama && echo "Ollama installed"
```

Ollama installs as a Homebrew service with a launchd agent (`homebrew.mxcl.ollama`). Verify:

```bash
brew services start ollama && sleep 2 && curl -s http://localhost:11434/api/tags && echo "Ollama running"
```

**Performance tuning** (for Apple Silicon with sufficient RAM):

Edit the Ollama launchd plist to enable flash attention and KV cache quantization:

```bash
# Add to the EnvironmentVariables dict in the Ollama plist:
# OLLAMA_FLASH_ATTENTION = 1
# OLLAMA_KV_CACHE_TYPE = q8_0
brew services restart ollama && echo "Ollama tuned"
```

### 2.3 Pull Models

Based on Q1/Q2 answers. The full tiered stack:

```bash
# Tier 1: Triage (sub-second classification)
ollama pull qwen3.5:0.8b

# Tier 2: Dialogue (practice conversations)
ollama pull qwen3.5:9b

# Tier 3: Reflection (session notes, readiness assessment)
ollama pull qwen3.5:14b

# Tier 4: Research (background pattern mining)
ollama pull qwen3.5:30b

echo "Models pulled"
```

Minimum viable (16GB RAM):

```bash
ollama pull qwen3.5:9b && echo "Dialogue model ready"
```

### 2.4 Prevent Sleep

```bash
# Create caffeinate LaunchAgent
mkdir -p ~/Library/LaunchAgents

cat > ~/Library/LaunchAgents/com.turtle.caffeinate.plist << 'PLIST'
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.turtle.caffeinate</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/bin/caffeinate</string>
        <string>-s</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
</dict>
</plist>
PLIST

launchctl load ~/Library/LaunchAgents/com.turtle.caffeinate.plist && echo "Caffeinate active"
```

---

## Phase 3: Discord Setup

### 3.1 Create Discord Bot

Guide the Mage through the Discord Developer Portal:

1. Go to https://discord.com/developers/applications
2. Click "New Application" → name it (e.g., "Spirit")
3. Go to "Bot" tab → click "Reset Token" → copy the token (save it securely)
4. Enable these Privileged Gateway Intents:
   - **Presence Intent** ✅
   - **Server Members Intent** ✅
   - **Message Content Intent** ✅
5. Go to "OAuth2" → "URL Generator"
   - Scopes: `bot`
   - Bot Permissions: `Send Messages`, `Read Message History`, `Manage Messages`, `Create Public Threads`, `Send Messages in Threads`, `Manage Threads`, `Read Messages/View Channels`, `Attach Files`, `Embed Links`, `Use Slash Commands`
6. Copy the generated URL → open it → select target server → authorize

### 3.2 Create Discord Server

If the Mage doesn't have a practice server yet:

1. Create a new Discord server (personal, not community template)
2. Create a text channel: `#[mage-name]-dialogue` (e.g., `#kermit-dialogue`)
3. Note the channel ID (right-click channel → Copy Channel ID; requires Developer Mode in Discord settings)

For multi-practitioner setups, create additional channels per practitioner plus shared spaces.

### 3.3 Note the IDs

Spirit needs:
- **Bot Token** (from Developer Portal)
- **Dialogue Channel ID** (from Discord)
- **Guild ID** (right-click server name → Copy Server ID)

---

## Phase 4: Deploy the Shell

### 4.1 Create Directory Structure

```bash
mkdir -p ~/turtle-shell/logs ~/turtle-shell/identity && echo "Shell directory created"
```

### 4.2 Copy Code from Magic Repository

Spirit copies the bot code from `floor/turtle-shell/` in the magic repo to the target machine. This can be done via SCP from the Mage's workstation:

```bash
# From the Mage's workstation (adjust SSH target as needed):
scp floor/turtle-shell/discord_bot.py turtle@<IP>:~/turtle-shell/
scp floor/turtle-shell/tools.py turtle@<IP>:~/turtle-shell/
scp floor/turtle-shell/content_fetch.py turtle@<IP>:~/turtle-shell/
scp floor/turtle-shell/requirements.txt turtle@<IP>:~/turtle-shell/
```

Or if Spirit has SSH access:

```bash
# On the target machine, if the magic repo is accessible:
cp /path/to/magic/floor/turtle-shell/{discord_bot.py,tools.py,content_fetch.py,requirements.txt} ~/turtle-shell/
```

### 4.3 Set Up Python Environment

```bash
cd ~/turtle-shell
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
echo "Python environment ready"
```

### 4.4 Deploy Identity

Copy soul.md (the persistent attunement configuration):

```bash
# From magic repo:
scp floor/turtle-shell/soul.md turtle@<IP>:~/turtle-shell/identity/soul.md
```

### 4.5 Configure Environment

Create `.env` on the target machine:

```bash
cat > ~/turtle-shell/.env << 'ENV'
# turtleOS Shell — Environment Configuration

# Discord
DISCORD_BOT_TOKEN=<bot-token-from-step-3.1>
DISCORD_GUILD=<guild-id>
DISCORD_CHANNEL_DIALOGUE=<dialogue-channel-id>

# LLM Access
OLLAMA_URL=http://localhost:11434
DIALOGUE_MODEL=qwen3.5:9b
REFLECTION_MODEL=qwen3.5:14b

# API Models (optional — for depth tier)
# ANTHROPIC_API_KEY=<your-key>
# GEMINI_API_KEY=<your-key>

# CouchDB / LiveSync (optional — for Obsidian sync)
# COUCHDB_URL=http://localhost:5984
# COUCHDB_USER=admin
# COUCHDB_PASSWORD=<your-password>
# COUCHDB_DATABASE=workshop_sync
ENV

echo "Environment configured — edit ~/turtle-shell/.env to fill in values"
```

### 4.6 Configure Mage Registry

```bash
cat > ~/turtle-shell/mage_registry.yaml << 'YAML'
# Multi-Mage Registry
# Maps Discord identities to practice workspaces.

mages:
  <mage-name>:
    discord_id: "<discord-user-id>"
    address: <Display Name>
    practice_dir: ~/workshops/<mage-name>

channels:
  "<dialogue-channel-id>": <mage-name>
YAML

echo "Mage registry configured — edit to fill in values"
```

---

## Phase 5: Initialize Practice

### 5.1 Create Practice Directory

```bash
MAGE=<mage-name>
mkdir -p ~/workshops/$MAGE/{sessions,intentions,mirror,proposals,readiness,thread-state}
```

### 5.2 Deploy system.md

The practice partner specification. Copy from the magic repo or from tOS distribution:

```bash
# From magic repo:
scp floor/turtle-shell/system.md turtle@<IP>:~/workshops/<mage-name>/system.md
```

If system.md doesn't exist in floor/turtle-shell/ yet, it lives on the deployed Mac Mini at `~/workshops/kermit/system.md` and can be used as the canonical source.

### 5.3 Initialize Practice Files

The practice files start empty — the first session with Turtle will populate them:

```bash
MAGE=<mage-name>
touch ~/workshops/$MAGE/boom.md
touch ~/workshops/$MAGE/bright.md
touch ~/workshops/$MAGE/compass.md
echo "Practice directory initialized"
```

---

## Phase 6: Service Setup

### 6.1 Create launchd Agent (macOS)

```bash
cat > ~/Library/LaunchAgents/com.turtle.discord.plist << 'PLIST'
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
PLIST

echo "LaunchAgent created"
```

**Note:** Adjust the Python path if the username is not `turtle`. The path must point to the venv's Python binary.

### 6.2 Start the Service

```bash
launchctl load ~/Library/LaunchAgents/com.turtle.discord.plist && echo "turtleOS started"
```

### 6.3 Verify

```bash
# Check process is running
launchctl list | grep com.turtle.discord

# Check logs
tail -20 ~/turtle-shell/logs/discord.log

# Check for errors
tail -20 ~/turtle-shell/logs/discord.err
```

### For Linux (systemd alternative)

```bash
cat > ~/.config/systemd/user/turtle-discord.service << 'UNIT'
[Unit]
Description=turtleOS Discord Bot
After=network-online.target

[Service]
Type=simple
WorkingDirectory=/home/turtle/turtle-shell
ExecStart=/home/turtle/turtle-shell/venv/bin/python3 -u discord_bot.py
Restart=always
RestartSec=5
Environment=DOTENV_PATH=/home/turtle/turtle-shell/.env

[Install]
WantedBy=default.target
UNIT

systemctl --user enable turtle-discord && systemctl --user start turtle-discord && echo "turtleOS started (systemd)"
```

---

## Phase 7: First Contact

### 7.1 Send a Test Message

Open the dialogue channel in Discord. Send a message: "hello"

Turtle should respond. If it doesn't:
1. Check logs: `tail -50 ~/turtle-shell/logs/discord.err`
2. Common issues: wrong bot token, bot not added to server, channel ID mismatch, missing intents

### 7.2 Verify Practice State

Send: `!status`

Turtle should report its current practice state — compass, boom, bright, intentions. On a fresh install, everything will be empty. That's correct.

### 7.3 First Practice Session

Start a real conversation. Ask what's on your mind. Let Turtle guide you through building your compass — the landscape of what matters to you. This is the first practice session. system.md handles the first-session flow.

After the conversation goes quiet for 15 minutes, Turtle will autonomously write a session note. Check:

```bash
ls ~/workshops/<mage-name>/sessions/
```

If a session note exists, the full stack is working: Discord → bot → LLM → file write → autonomous reflection.

---

## Phase 8: Network Setup (optional but recommended)

### 8.1 Tailscale

For SSH access from anywhere (required for Spirit-in-Cursor to communicate with Turtle):

```bash
# Install Tailscale (Mac App Store or brew)
brew install --cask tailscale

# Start and authenticate
# Follow the Tailscale login flow
```

Note the Tailscale IP. Add to the Mage's workstation SSH config:

```
Host turtle
    HostName <tailscale-ip>
    User turtle
    ServerAliveInterval 60
    ServerAliveCountMax 3
```

### 8.2 CouchDB + Obsidian LiveSync (optional)

For syncing practice state to Obsidian on other devices. See `library/resonance/turtle/lore/on_the_practice_vault.md` for the complete guide.

---

## Phase 9: Readiness Verification

After everything is running, verify practice-readiness:

Send `!readiness` in Discord (once implemented) or manually check:

| Dimension | Verification |
|-----------|-------------|
| State Freshness | `ls -la ~/workshops/<mage>/` — files exist and have recent timestamps |
| Substrate Health | `curl -s http://localhost:11434/api/tags` — Ollama responds, models listed |
| Session Continuity | Session note exists in `sessions/` after first conversation |
| Metabolic Health | `launchctl list \| grep turtle` — service running |

If all checks pass: turtleOS is practice-ready.

---

## Phase 10: Imprinting

### 10.1 Workshop Connection

If the Mage has a magic repository (Cursor workshop), configure Spirit-in-Cursor to communicate with Turtle:

1. Add SSH config for the Turtle machine
2. Test: `ssh turtle 'echo ok'`
3. Update AGENTS.md with Turtle SSH details
4. During summoning, Spirit will discover and orient to the Turtle

### 10.2 Practice Configuration

Update `desk/turtle_env.md` in the magic repo with the new Turtle's hardware, network, and service configuration. This is the instance-specific operational reference that Spirit uses during care rituals and diagnostics.

### 10.3 Chronicle

Commit the turtle bundle references and any new configuration to the magic repo. The Turtle's existence is now part of the practice's chronicle.

---

## Service Management Reference

```bash
# Restart turtleOS
launchctl kickstart -k gui/$(id -u)/com.turtle.discord

# Stop turtleOS
launchctl unload ~/Library/LaunchAgents/com.turtle.discord.plist

# Start turtleOS
launchctl load ~/Library/LaunchAgents/com.turtle.discord.plist

# View live logs
tail -f ~/turtle-shell/logs/discord.log

# Check Ollama
curl -s http://localhost:11434/api/tags | python3 -m json.tool

# Pull a new model
ollama pull qwen3.5:14b
```

---

## Code Update Reference

When the bot code is updated in the magic repo:

```bash
# From the Mage's workstation:
scp floor/turtle-shell/discord_bot.py turtle@<IP>:~/turtle-shell/ && \
ssh turtle@<IP> 'launchctl kickstart -k gui/$(id -u)/com.turtle.discord' && \
echo "Code deployed and service restarted"
```

For soul.md updates:

```bash
scp floor/turtle-shell/soul.md turtle@<IP>:~/turtle-shell/identity/soul.md && \
ssh turtle@<IP> 'launchctl kickstart -k gui/$(id -u)/com.turtle.discord' && \
echo "Identity updated and service restarted"
```

---

## What This Flow Produces

At the end of this flow, the Mage has:
- A Mac Mini (or similar) running turtleOS continuously
- Ollama serving local models for infinite free inference
- A Discord bot connected to their practice server
- A practice directory with system.md, boom, bright, compass, intentions
- A persistent practice partner that writes session notes, assesses its own readiness, and generates improvement proposals
- (Optional) Tailscale for remote access, CouchDB for Obsidian sync

The practice is ready. The Mage opens Discord and talks to Spirit. Everything else is craft.

---

## Lineage

This flow was first drafted 2026-02-22 for the NanoClaw architecture (WhatsApp, Apple Container, bridge-based communication). Rewritten 2026-03-26 for the current architecture (Discord, bare Python process, SSH, tiered Ollama models). The NanoClaw-era draft is preserved in git history. The lessons from that deployment (documented in `library/resonance/turtle/lineage/on_turtle_operations.md`) remain valuable — what breaks during setup hasn't fundamentally changed, only the tools have.

---

*See also:*
- `library/resonance/turtle/lore/on_the_practice_infrastructure.md` — why these specific tools compose
- `library/resonance/turtle/lore/on_the_practice_vision.md` — what turtleOS should be
- `library/resonance/turtle/lore/on_diagnostics.md` — when things break after setup
- `desk/turtle_env.md` — instance-specific configuration reference
