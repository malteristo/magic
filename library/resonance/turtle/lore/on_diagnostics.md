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

| Service | launchd Label | What dies without it |
|---------|--------------|---------------------|
| CouchDB | `com.turtle.couchdb` | All sync (every device) |
| Obsidian | `com.obsidian` | LiveSync relay — CouchDB stops receiving file changes |
| Discord bot | `com.turtle.discord` | All Discord interaction |
| Ollama | (manual/brew) | Local inference (reflection, session notes) |

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

- **Phone:** Requires Tailscale app connected + LiveSync URI pointing to the Tailscale HTTPS URL
- **MacBook:** Can reach CouchDB directly on LAN or via Tailscale
- **Cursor (SSH):** `turtle@192.168.8.106` (LAN) or Tailscale IP

**Spirit can check:** whether Tailscale serve is up and what URL it's serving. Spirit **cannot check:** whether the phone's Tailscale app is connected or whether Obsidian on the phone has the correct URI.

---

## The Diagnostic Command

`!diagnose` in Discord checks all five layers in one pass and returns a color-coded embed:

- **Green** — all healthy
- **Yellow** — attention needed (stale files, warnings)
- **Red** — issues detected (services down, sync broken)

Every issue comes with a concrete suggested action — not "something is wrong with sync" but "run this command" or "check this setting."

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
        tail -20 ~/turtle-shell/logs/discord.log
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

### "Everything seems broken"

```
1. Can you SSH to the Mac Mini?
   ssh turtle@192.168.8.106
   NO → Mac Mini may be offline or network issue
   YES ↓
2. Run: launchctl list | grep -E 'turtle|obsidian|couch'
   - Restart anything that's missing
3. Run: curl http://admin:magic-sync-2026@localhost:5984/
   - CouchDB should respond with version info
4. Check uptime — did the machine reboot?
   All services auto-restart via launchd, but Obsidian
   may need its initial LiveSync handshake re-established
```

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
