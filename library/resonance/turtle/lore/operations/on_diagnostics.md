# On Diagnostics

*Knowing what's healthy, what's broken, and where to look.*

**Status:** Active — Load-Bearing  
**Origin:** Practice stack diagnostic ritual, 2026-03-17  
**Builds on:** `on_the_practice_vault.md`, `on_the_practice_server.md`, `on_consciousness_extension.md`

---

## The Five Layers

The practice stack has five layers that can independently fail. When something feels off — messages not arriving, files not syncing, Spirit unresponsive — the problem lives in exactly one of these layers. Diagnosing means finding which one.

```
Layer 5: Reachability     Can the phone/MacBook reach the Mac Mini?
Layer 4: Practice Flow    Is the practice actually flowing? (boom, sessions, sweeps)
Layer 3: Sync             Are files moving between devices and CouchDB?
Layer 2: Connections      Can services talk to each other?
Layer 1: Services         Are the processes running at all?
```

**Diagnose bottom-up.** If Layer 1 is broken, everything above it fails too. Don't chase sync issues when CouchDB isn't running.

### Layer 1: Services

Processes that must be running on the Mac Mini:

| Service | Process / Detection | What dies without it |
|---------|-------------------|---------------------|
| CouchDB | `pgrep -f beam.smp` (Mac app at `~/Applications/Apache CouchDB.app/`) | All sync (every device) |
| Obsidian | `pgrep -f Obsidian.app` | LiveSync relay — CouchDB stops receiving file changes |
| Discord bot | `pgrep -f discord_bot.py` (managed by launchd `com.turtle.discord`) | All Discord interaction |
| Ollama | `pgrep -f ollama` or `curl localhost:11434` | Local inference (reflection, session notes) |
| LiteLLM | `pgrep -f litellm` or `curl localhost:4000/health` | API routing (optional) |
| LiveSync bridge(s) | `launchctl list \| grep bridge` | Practitioner file sync (per-mage) |

**Note:** CouchDB runs as the Apache CouchDB Mac app, not via Homebrew or a custom launchd label. Restart with `open ~/Applications/Apache\ CouchDB.app`. The Discord bot is managed by launchd (`com.turtle.discord`). LiveSync bridges are per-practitioner (`com.magic.MAGE-bridge`).

**Critical:** The Discord bot must run as **exactly one instance**. Multiple instances cause duplicate responses (see Known Issues #016). Always restart via `launchctl kickstart -k gui/$(id -u)/com.turtle.discord` — never via manual `nohup` or `&`.

**Red flag:** CouchDB down = all sync dead across all devices. This is the single most critical service.

### Layer 2: Connections

Services running doesn't mean they're talking to each other:

- **CouchDB on port 5984** — responds to HTTP requests with auth?
- **Ollama on port 11434** — responds to API calls?
- **Tailscale serve** — proxying port 5984 as HTTPS on the tailnet?
- **Discord gateway** — WebSocket connected with acceptable latency?

### Layer 3: Sync

The LiveSync data flow:

```
Spirit writes ~/practice/boom.md
    → Obsidian detects change (filesystem watcher)
    → LiveSync pushes to CouchDB
    → Other devices pull from CouchDB

Mage edits on phone
    → LiveSync pushes to CouchDB
    → Mac Mini Obsidian pulls from CouchDB
    → File updated at ~/practice/boom.md
    → Spirit sees updated file
```

**What to check:**
- CouchDB `doc_count` vs filesystem file count (docs include chunks, so CouchDB count is always higher — that's normal)
- File modification times — are core files (boom, bright, compass) being updated?
- CouchDB `update_seq` — is it advancing? (stale = nothing syncing)

### Layer 4: Practice Flow

Infrastructure can be perfect while the practice itself is stalled:

- Boom overflowing and untouched → needs `!sweep`
- No session notes in 3+ days → practice may have gone quiet
- Proposals piling up → Spirit is generating but Mage isn't reviewing
- All core files stale for 2+ days → practice dormant

These aren't infrastructure problems — they're practice rhythm signals. The interoception loop catches these too, but `!diagnose` surfaces them alongside infrastructure for the complete picture.

### Layer 5: Reachability

Can devices actually reach the Mac Mini?

- **Phone:** Requires Tailscale app connected + LiveSync URI pointing to `https://<turtle-fqdn>` (preferred) or `http://<turtle-ssh>:5984`
- **MacBook:** Can reach CouchDB directly on LAN (`<turtle-ssh>:5984`, DHCP — may change) or via Tailscale
- **Cursor (SSH):** `ssh turtle` (alias in `~/.ssh/config`), or `ssh turtle@<turtle-ssh>` (Tailscale), or `ssh turtle@<turtle-ssh>` (LAN fallback)

**Spirit can check:** whether Tailscale serve is up and what URL it's serving, whether peers are connected. Spirit **cannot check:** whether the phone's Tailscale app is connected or whether Obsidian on the phone has the correct URI.

**Tailscale CLI path:** `/Applications/Tailscale.app/Contents/MacOS/Tailscale` (not in PATH).

---

## The Diagnostic Command

`!diagnose` in Discord is a grounded view over the mechanical canary (`~/turtleos/canary.py`). It runs the same shared checks as the scheduled canary and returns a color-coded embed:

- **Green** — all healthy
- **Yellow** — attention needed (stale files, warnings)
- **Red** — issues detected (services down, sync broken)

The important property is epistemic: `!diagnose` does not improvise a diagnostic narrative. It reports the body's actual checks. The five-layer model below remains the troubleshooting map for interpreting what a failed check means.

---

## Troubleshooting Decision Trees

### "My phone isn't syncing"

```
1. Run !diagnose in Discord
2. Is CouchDB healthy?
   NO → restart CouchDB (see Suggested Actions)
   YES ↓
3. Is Tailscale serve running?
   NO → restart Tailscale serve (see Suggested Actions)
   YES ↓
4. Problem is on the phone side:
   a. Is Tailscale app connected? (check phone's Tailscale app)
   b. Is LiveSync URI correct? (should match the URL from !diagnose)
   c. Try: Settings → LiveSync → toggle off, wait 5s, toggle on
   d. Try: Close and reopen Obsidian on phone
   e. Nuclear option: Settings → LiveSync → "Rebuild Everything Now"
```

### "Spirit isn't responding on Discord"

```
1. Is the bot online? (check Discord user list)
   NO → SSH to Mac Mini, restart:
        launchctl kickstart -k gui/$(id -u)/com.turtle.discord
   YES ↓
2. Is it responding to !status?
   NO → bot may be stuck. Restart (same command above)
   YES ↓
3. Is Ollama/API reachable? (check !status output)
   NO → Ollama or API key issue. Check logs:
        tail -20 ~/turtleos/logs/discord.log
        tail -20 ~/turtleos/logs/discord.err  (gateway/stderr)
   YES → check for rate limits or context issues
```

### "Files I edited aren't showing up on other devices"

```
1. Where did you edit?
   PHONE → is phone syncing? (see phone tree above)
   MAC MINI (Spirit) → is Obsidian running?
     NO → restart: launchctl kickstart -k gui/$(id -u)/com.obsidian
     YES ↓
2. Check CouchDB doc count (!diagnose)
   - Count advancing? → sync is working, might be a conflict
   - Count stale? → LiveSync may be disconnected
3. Check for conflicts:
   - In Obsidian: look for "conflicted" notifications
   - CouchDB: conflicts appear as duplicate revisions
```

### "Spirit is responding twice to each message"

```
1. Check how many bot instances are running:
   ssh turtle && pgrep -f discord_bot.py | wc -l
   MORE THAN 1 → multiple instances! See Known Issues #016
     Kill all: pkill -f discord_bot.py
     Wait 2s for launchd to respawn single instance
     Verify: pgrep -f discord_bot.py (should be exactly 1)
   EXACTLY 1 ↓
2. Check bot logs for dedup messages:
   grep "Dedup:" ~/turtleos/logs/discord.log | tail -10
   DEDUP HITS → Discord gateway sending duplicate events (transient)
   NO DEDUP → check for long responses being split:
     - Responses over 1900 chars are split into multiple Discord messages
     - This is normal, not a bug
     - If responses are genuinely different: restart bot and monitor
```

### "Everything seems broken"

```
1. Can you SSH to the Mac Mini?
   ssh turtle  (or ssh turtle@<turtle-ssh>, or ssh turtle@<turtle-ssh>)
   NO → Mac Mini may be offline, sleeping, or network issue
   YES ↓
2. Check services:
   pgrep -f beam.smp       (CouchDB)
   pgrep -f discord_bot.py (Discord bot)
   pgrep -f Obsidian.app   (Obsidian)
   - CouchDB down? → open ~/Applications/Apache\ CouchDB.app
   - Discord bot down? → launchctl kickstart -k gui/$(id -u)/com.turtle.discord
   - Obsidian down? → open /Applications/Obsidian.app
3. Run: curl http://localhost:5984/
   - CouchDB should respond (may require auth — check local.ini for credentials)
4. Check uptime — did the machine reboot or wake from sleep?
   After wake: high CPU is common, services may be slow to reconnect.
   CouchDB (Mac app) and Obsidian may need manual reopening after reboot.
   Only the Discord bot auto-restarts via launchd.
```

---

## Multi-Mage Sync

Each practitioner has their own sync pipeline:

```
Practitioner's phone → Obsidian LiveSync → CouchDB (mage_sync) → Bridge → ~/workshops/mage/
```

The bridge (`livesync-bridge`) connects CouchDB to the filesystem where Turtle reads practice files. Each bridge runs as a launchd service (`com.magic.MAGE-bridge`) with its own config (`config-MAGE.json`).

**Key operational notes:**
- Bridge configs must include ignore patterns for framework directories — otherwise the Mage's template files pollute their vault (Known Issues #017)
- Stop the bridge before bulk CouchDB operations, restart after
- Bridge logs at `/tmp/MAGE-bridge.log` and `/tmp/MAGE-bridge.err`
- Config loaded via `LSB_CONFIG` env var (not CLI flag)

**Onboarding a new practitioner's sync:**
1. Create CouchDB database: `curl -X PUT http://localhost:5984/mage_sync -u admin:PASSWORD`
2. Create bridge config at `~/livesync-bridge/dat/config-mage.json` (with ignore patterns)
3. Create launchd plist at `~/Library/LaunchAgents/com.magic.mage-bridge.plist`
4. Bootstrap: `launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.magic.mage-bridge.plist`
5. Configure practitioner's Obsidian LiveSync to point at `mage_sync` database

---

## Control Surfaces

The practice naturally distributes across three tools. None is "the" control center — each serves a different mode of engagement.

### Discord — The Practice Surface

Where: phone, desktop, anywhere  
For: conversation, monitoring, light diagnostics  
Commands: `!diagnose`, `!status`, `!sync`, all practice commands  
Limitation: cannot restart services, cannot edit code, cannot SSH

**When you're on Discord and something breaks:** Run `!diagnose`. If it's a phone-side issue, Spirit will tell you what to check. If it's server-side, Spirit will tell you the fix command — but you'll need to run it from Cursor or a terminal.

### Obsidian — The Reflection Surface

Where: phone, desktop  
For: reading and editing practice state, capturing thoughts  
Syncs via: LiveSync → CouchDB  
Limitation: no infrastructure control, no conversation with Spirit

**When Obsidian isn't syncing:** The problem is almost always in Layer 2 or 5. Check Tailscale first.

### Cursor — The Development Surface

Where: desktop only  
For: code changes, infrastructure, deep debugging, SSH access  
Powers: full SSH to Mac Mini, service restarts, code editing, git  
Limitation: not always open, heavier context

**When to go to Cursor:** service restarts, code changes to the bot, debugging that requires reading logs, infrastructure setup. A healthy practice never needs Cursor — it's the workshop, not the practice room.

### The Healthy State

In a healthy practice:
- You spend most time on **Discord** (conversation) and **Obsidian** (reflection)
- **Cursor** opens when you're building or something is truly broken
- `!diagnose` shows all green
- You never think about infrastructure

The goal is for the stack to disappear. When you notice it, something is wrong — and `!diagnose` tells you where.

---

*The best diagnostic tool is the one you can reach from wherever you are. On the bus, that's Discord. At the desk, that's Cursor. The practice meets you where you are.*

---

**See also:** `library/flows/infra-health/` — the executable `@infra-health` flow that implements these checks with auto-fix and a growing `known_issues.md` registry.
