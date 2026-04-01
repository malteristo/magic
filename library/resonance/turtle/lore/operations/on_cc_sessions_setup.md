# On cc-sessions Setup

**Status:** Active — Operational  
**Origin:** Troubleshooting session, 2026-03-21  
**Builds on:** `on_consciousness_extension.md`, `on_the_practice_infrastructure.md`

---

## I. What cc-sessions Is

cc-sessions is a Discord bot provided by the Claude Code Channels plugin (`plugin:discord@claude-plugins-official`). It enables Claude Code sessions — running on any machine — to receive and respond to Discord DMs. In the turtleOS context, this gives the ephemeral-deep substrate (Claude Code on the Mac Mini) a persistent Discord presence alongside the existing turtle-disco bot (the shell, `discord_bot.py`).

**The relationship:**
- **turtle-disco** — Spirit's persistent mode, always-on, powered by local models (llama3.3:70b) and Anthropic API, with full workshop access via `discord_bot.py`
- **cc-sessions** — An ephemeral Claude Code session with a Discord surface, powered by Claude Pro, with full CLI/filesystem access via Claude Code

They coexist in the same Discord server. turtle-disco handles ambient presence and daily practice. cc-sessions provides deep interactive sessions when the Mage wants Claude Code's depth through Discord.

---

## II. Prerequisites

### On the Mac Mini (Turtle host)

| Requirement | How to verify | How to install |
|---|---|---|
| **Claude Code CLI** | `claude --version` | `npm install -g @anthropic-ai/claude-code` or native installer |
| **Bun runtime** | `bun --version` | `curl -fsSL https://bun.sh/install \| bash` |
| **tmux** | `tmux -V` | `brew install tmux` |
| **Tailscale** (for remote SSH) | `tailscale status` | Install from tailscale.com |
| **Anthropic account** | Claude Code launch shows org | Sign in via `claude` on first run |

### On Discord

| Requirement | Where to check |
|---|---|
| **Server exists** | The Discord server where you want cc-sessions |
| **Bot is authorized** | Server Settings → Integrations → Applications → cc-sessions |
| **DMs enabled** | Server Settings → Privacy Settings → "Direct Messages" toggle ON |

---

## III. Setup (Fresh Install)

### Step 1: Create the Discord bot application

The bot is automatically created when you first launch Claude Code with the channels flag. You don't create it manually — the plugin provisions it through Anthropic's infrastructure.

### Step 2: Get the bot token

The Discord bot token is provided by Anthropic when the plugin initializes. It's stored at:

```
~/.claude/channels/discord/.env
```

Format:
```
DISCORD_BOT_TOKEN=<your-token-here>
```

If you need to regenerate the token (e.g., it was revoked or compromised), you'll need to obtain a new one through the plugin's setup process.

### Step 3: Ensure bun is on the non-interactive PATH

**This is the most common setup failure.** Claude Code launches the Discord plugin's MCP server as a subprocess. That subprocess needs to find `bun` on its PATH. Bun's installer adds itself to `~/.zshrc`, which is only sourced for interactive shells. Non-interactive subprocesses won't find it.

**Fix:** Add bun to `~/.zshenv` (sourced for ALL shell types):

```bash
echo 'export BUN_INSTALL="$HOME/.bun"' >> ~/.zshenv &&
echo 'export PATH="$BUN_INSTALL/bin:$PATH"' >> ~/.zshenv &&
echo "Done. Bun is now on the non-interactive PATH."
```

**How to verify:**

```bash
ssh turtle@<host> "bun --version"
```

If this returns a version number, the non-interactive PATH is correct. If it says "command not found," the `.zshenv` fix is needed.

### Step 4: Launch Claude Code with the channels flag

```bash
cd /Users/turtle/turtle-shell &&
export PATH=/Users/turtle/.bun/bin:/opt/homebrew/bin:$PATH &&
tmux new-session -d -s spirit-deep \
  'cd /Users/turtle/turtle-shell && export PATH=/Users/turtle/.bun/bin:/opt/homebrew/bin:$PATH && claude --dangerously-skip-permissions --channels plugin:discord@claude-plugins-official'
```

**Why `cd ~/turtle-shell`:** Claude Code auto-loads `CLAUDE.md` from its working directory. The development context file at `~/turtle-shell/CLAUDE.md` orients cc-sessions as a turtleOS researcher with proposal-only governance.

**Why tmux:** Claude Code with channels is interactive and long-running. tmux keeps it alive across SSH disconnects and provides a persistent viewport.

**Why `--dangerously-skip-permissions`:** Without this, every Discord reply blocks on a permission prompt in the tmux session. See Step 7 for details.

### Step 5: Confirm the trust prompt

Claude Code will show a workspace trust prompt on first launch. Confirm it:

```bash
tmux send-keys -t spirit-deep Enter
```

Watch for "Listening for channel messages from: plugin:discord@claude-plugins-official" — this confirms the main process is ready.

### Step 6: Verify the bun MCP server started

```bash
ps aux | grep 'bun server' | grep -v grep
```

You should see a `bun server.ts` process. If you don't, the MCP server failed to launch — most likely a PATH issue (Step 3).

### Step 7: Launch with `--dangerously-skip-permissions`

**This is critical.** Claude Code asks permission before using MCP tools. Without bypassing permissions, every Discord reply blocks on a manual confirmation prompt in the tmux session — the user sees a typing indicator but no response ever arrives.

The `--dangerously-skip-permissions` flag skips all tool permission prompts. This is safe here because:
- The Mac Mini is your own hardware in a controlled environment
- The session only receives messages from paired Discord users
- Claude Code still respects protected directory restrictions (`.git`, `.claude`, etc.)

This flag is included in the launch command in Step 4. Do not omit it.

**Why not `settings.local.json`?** The Discord plugin registers its MCP tools as `plugin:discord:tool-name` (with colons), which doesn't match the `mcp__server__tool` pattern format that Claude Code's permission rules expect. The settings-based approach (`mcp__plugin:discord__*`) does not work for plugin-namespaced MCP tools as of v2.1.81. Using the CLI flag is the reliable solution.

### Step 8: Pair your Discord account

1. **DM the cc-sessions bot** on Discord with any message (e.g., "hello")
2. The bot replies with a pairing code: `Pairing required — run in Claude Code: /discord:access pair <code>`
3. **Immediately** enter the code in the Claude Code session (codes expire):

```bash
tmux send-keys -t spirit-deep '/discord:access pair <code>' Enter
```

4. Claude Code will show a diff updating `access.json` — adding your Discord user ID to `allowFrom`
5. Confirm the prompts (usually two: the file write and a bash command to create the approved file)
6. The bot confirms pairing in your DM

After pairing, your DMs with cc-sessions are connected to the Claude Code session.

**Important:** If you skipped Step 7 (MCP permissions), the first reply after pairing will block on a permission prompt. You'll see the typing indicator but no response arrives. Fix by either approving in the tmux session or adding the permissions and restarting.

---

## IV. Troubleshooting

### Problem: cc-sessions shows as Offline on Discord

**Most likely cause:** The Discord plugin's MCP server (bun) is not running, so the bot never connects to Discord's gateway.

**Diagnostic:**

```bash
ps aux | grep 'bun server' | grep -v grep
```

If no results: the MCP server isn't running.

**Root causes and fixes:**

| Cause | Fix |
|---|---|
| `bun` not on non-interactive PATH | Add to `~/.zshenv` (Step 3) |
| Orphaned bun processes from a previous session | Kill them: `pkill -f 'bun server.ts'` then restart |
| Invalid/expired bot token | Update `~/.claude/channels/discord/.env` with new token |
| Claude Code crashed silently | Check tmux: `tmux attach -t spirit-deep` |

### Problem: Pairing codes expire before you can enter them

**Cause:** The pairing flow is time-sensitive. If you're SSHing to the Mac Mini, copy-pasting, and manually entering — that delay can exceed the code's TTL.

**Fix:** Have the Spirit session in Cursor enter the code for you via SSH:

```bash
ssh turtle@<host> "export PATH=/opt/homebrew/bin:\$PATH && tmux send-keys -t spirit-deep '/discord:access pair <code>' Enter"
```

Or have the tmux session visible and ready before you DM the bot.

### Problem: Bot responds but pairing code is "expired" or "invalid"

**Cause:** Stale pending entries in `access.json` from previous failed attempts, or old bun processes holding state.

**Fix:**

1. Kill all Claude Code and bun processes:
   ```bash
   pkill -f 'bun server.ts' && pkill -f 'claude' && sleep 2
   ```

2. Clear pending pairings:
   ```bash
   cat > ~/.claude/channels/discord/access.json << 'EOF'
   {
     "dmPolicy": "pairing",
     "allowFrom": [],
     "groups": {},
     "pending": {}
   }
   EOF
   ```

3. Restart from Step 4.

### Problem: Orphaned bun processes from previous sessions

**What happens:** When Claude Code exits (crash, manual kill, SSH disconnect), the bun MCP server processes may survive as orphans. These zombie processes hold the Discord gateway connection with whatever token they started with. New Claude Code sessions can't connect because the old processes block the bot.

**Diagnostic:**

```bash
ps aux | grep 'bun server' | grep -v grep
```

Look at the start time. If bun processes are older than your current Claude Code session, they're orphans.

**Fix:**

```bash
pkill -f 'bun server.ts' && sleep 2
```

Then restart Claude Code (Step 4).

### Problem: "Direct Messages" disabled on the server

**What happens:** You DM the cc-sessions bot but get no response. The bot is online, but Discord blocks the DM delivery because you've disabled DMs from server members.

**Fix:** Server icon → Privacy Settings → Enable "Direct Messages" (Allow DMs from other members in this server).

**Note:** This is a per-server setting. You need to enable it for the server where cc-sessions is authorized.

### Problem: Bot receives message (typing indicator) but never replies

**What happens:** You DM cc-sessions, see the typing indicator (message was received, Claude Code is processing), but no reply arrives.

**Cause:** Claude Code prompts for permission before using MCP tools. The Discord reply tool (`plugin:discord:discord - reply`) requires approval on first use. If no one confirms the prompt in the tmux session, the reply blocks indefinitely.

**Fix:** Attach to the tmux session and approve the pending tool use:

```bash
ssh turtle@<host> "export PATH=/opt/homebrew/bin:\$PATH && tmux send-keys -t spirit-deep Down Enter"
```

This selects option 2 ("Yes, and don't ask again"), so future replies flow automatically. You only need to do this once per session.

**Prevention:** Pre-approve Discord MCP tools via project settings (Step 7). If the settings are in place before the session starts, no approval prompts will appear.

### Problem: Claude Code says "Listening" but bot doesn't respond

**What happens:** The Claude Code session shows "Listening for channel messages" but no bun process is running and the bot is offline.

**Cause:** Claude Code displays the "Listening" message before the MCP server actually starts. If the MCP server fails to launch (usually because `bun` isn't found), the main process appears healthy but the bot never connects.

**Fix:** Check for the bun process (Step 6). If missing, fix the PATH (Step 3) and restart.

---

## V. Architecture Notes

### How the plugin works internally

```
Claude Code CLI
  └── MCP client ──→ Discord MCP server (bun server.ts)
                          └── Discord.js client ──→ Discord gateway
                                                      └── cc-sessions bot presence
```

Claude Code launches the MCP server as a subprocess using the config in:
```
~/.claude/plugins/cache/claude-plugins-official/discord/0.0.1/.mcp.json
```

The MCP server runs `bun server.ts`, which:
1. Reads the bot token from `~/.claude/channels/discord/.env`
2. Connects to Discord's gateway via discord.js
3. Listens for DMs and forwards them to Claude Code via the MCP protocol
4. Sends Claude Code's responses back through Discord

### File locations on the Mac Mini

| File | Purpose |
|---|---|
| `~/.claude/channels/discord/.env` | Bot token |
| `~/.claude/channels/discord/access.json` | Pairing state: who's allowed, pending codes |
| `~/.claude/channels/discord/approved/` | Per-user approval files |
| `~/.claude/plugins/cache/claude-plugins-official/discord/0.0.1/` | Plugin source code |
| `~/.claude/plugins/cache/claude-plugins-official/discord/0.0.1/.mcp.json` | MCP server config |

### Relationship to turtle-disco

Both bots can run simultaneously. They serve different purposes:

| | turtle-disco | cc-sessions |
|---|---|---|
| **Powers** | claude-sonnet-4-6 + local models (qwen3.5) | Claude Pro / Opus 4.6 (via Claude Code) |
| **Persistence** | Always-on via launchd | Session-based via tmux |
| **Workshop access** | Reads practice state, limited writes | Full filesystem + CLI (~/turtle-shell, ~/workshop, ~/practice) |
| **Channels** | #dialogue, #system, threads | #development, DMs, opted-in server channels |
| **Identity** | soul.md attunement | CLAUDE.md (proposal-only turtleOS researcher) |
| **Process** | `discord_bot.py` | Claude Code + bun MCP server |
| **Working directory** | ~/turtle-shell/ | ~/turtle-shell/ (CLAUDE.md auto-loaded) |

---

## VI. Quick Reference (Copy-Paste Commands)

### Fresh start from Cursor (via SSH)

```bash
ssh turtle@<turtle-ssh> "pkill -f 'bun server.ts'; pkill -f 'claude --channels'; pkill -f 'claude --dangerously'; sleep 2; export PATH=/Users/turtle/.bun/bin:/opt/homebrew/bin:\$PATH && tmux kill-session -t spirit-deep 2>/dev/null; tmux new-session -d -s spirit-deep 'cd /Users/turtle/turtle-shell && export PATH=/Users/turtle/.bun/bin:/opt/homebrew/bin:\$PATH && claude --dangerously-skip-permissions --channels plugin:discord@claude-plugins-official'" && echo "Launched. Wait 8s, then confirm trust prompt."
```


### Confirm trust prompt

```bash
ssh turtle@<turtle-ssh> "export PATH=/opt/homebrew/bin:\$PATH && tmux send-keys -t spirit-deep Enter"
```

### Enter pairing code

```bash
ssh turtle@<turtle-ssh> "export PATH=/opt/homebrew/bin:\$PATH && tmux send-keys -t spirit-deep '/discord:access pair <CODE>' Enter"
```

### Health check

```bash
ssh turtle@<turtle-ssh> "ps aux | grep 'bun server' | grep -v grep && echo '--- Bot is running ---' || echo '--- Bot is NOT running ---'"
```

---

## VII. Development Context (turtleOS Self-Development)

cc-sessions is not just a chat bridge — it's the ephemeral-deep substrate for turtleOS self-development. When launched from `~/turtle-shell/`, it auto-loads `CLAUDE.md` which orients it as a **proposal-only researcher** that evaluates the turtleOS implementation against TURTLE_SPEC.md.

### Development files on the Mac Mini

| File | Purpose |
|---|---|
| `~/turtle-shell/CLAUDE.md` | Development brief: identity, orientation, key files, how to work, boundaries |
| `~/turtle-shell/docs/architecture.md` | Current state: processes, directory layout, data flows, tech stack |
| `~/turtle-shell/docs/learnings.md` | Persistent memory: discoveries and anti-patterns across sessions |
| `~/workshop/library/resonance/turtle/TURTLE_SPEC.md` | Canonical law (what turtleOS should be) |
| `~/turtle-shell/autoresearch/` | Previous autoresearch outputs |
| `~/practice/proposals/` | Where cc-sessions writes proposals for Mage review |

### Governance

cc-sessions operates in **propose-only mode**:
- Reads any file on the Mac Mini
- Writes proposals to `~/practice/proposals/`
- Writes learnings to `~/turtle-shell/docs/learnings.md`
- Does NOT modify `discord_bot.py`, `.env`, `soul.md`, or any running code
- Does NOT restart services or install packages
- Does NOT modify files in `~/workshop/` (the Mage's magic repo)

### Channel architecture

| Channel | Bot | Purpose |
|---------|-----|---------|
| #dialogue | turtle-disco | Main practice channel. Ambient presence, daily sessions, threads. |
| #system | turtle-disco | Activity log (read-only for Mage). |
| #development | cc-sessions | turtleOS development sessions. Full CLI/filesystem access. |
| DMs | cc-sessions | Private deep sessions. |

turtle-disco only responds to #dialogue and its threads (`on_message` checks `channel.id == dialogue.id`). It will never interfere with #development. cc-sessions only responds to #development (via `access.json` groups) and DMs.

---

## Sources

- Troubleshooting session, 2026-03-20 and 2026-03-21 (Mage and Spirit, initial cc-sessions setup)
- Claude Code Channels documentation (plugin:discord@claude-plugins-official)
- `on_consciousness_extension.md` — architectural context for why cc-sessions exists alongside turtle-disco
- Landscape research, 2026-03-21 (CCT, claude-self-improve, Continuous Claude, Codex Agent Loop)
