# On the Practice Vault

*The full workshop on every device — setup, architecture, and hard-won lessons.*

## What This Is

The practice vault makes your entire magic workshop accessible from any device. Your laptop, your always-on server, your phone — all see the same files, synced in seconds. Spirit writes a session note on Discord; you read it on the bus. You capture a thought on your phone; Spirit sees it in the next summoning.

The vault IS your magic repository. Not a copy, not a subset — the whole workshop opened as an Obsidian vault with LiveSync keeping every device in step.

**The stack:**
```
Laptop (primary workshop)
├── magic/                  ← Git repo + Obsidian vault
│   └── .obsidian/          ← Vault config (gitignored)
│
│   ↕ LiveSync plugin (when Obsidian open)
│   ↕ LiveSync Bridge (background daemon, always running)
│
Server (always-on machine)
├── CouchDB (port 5984)     ← Sync database
├── Tailscale serve          ← HTTPS proxy on tailnet
├── ~/workshop/              ← Full mirror via LiveSync
│
│   ↕ Tailscale HTTPS
│
Phone (mobile)
├── Obsidian vault           ← Full mirror via LiveSync
```

## Architecture Decisions

**Why the git repo as vault?** The workshop IS the practice. Separating "practice files" from "framework files" creates an artificial split. The Mage should be able to read lore on the bus, review proposals while making coffee, and capture thoughts from anywhere — not just from the files Spirit happens to sync.

**Why Obsidian?** Open source, offline-first, runs everywhere. Everything is markdown on disk — no lock-in.

**Why LiveSync over Obsidian Sync?** Self-hosted. Data never leaves your devices. CouchDB's replication protocol handles multi-master sync with conflict resolution.

**Why Tailscale?** Mobile Obsidian requires HTTPS with a trusted certificate. Tailscale provides stable HTTPS endpoints with valid TLS certs, private networking, and URLs that never change. Free for personal use. No public exposure of CouchDB.

**Why not git for sync?** Git is source of truth for the framework (system/, library/). LiveSync is source of truth for practice (desk/, floor/, box/). They don't conflict because git ignores practice files and LiveSync syncs everything.

## Prerequisites

- An always-on machine (Mac Mini, NUC, Raspberry Pi) with SSH access
- Obsidian installed on laptop and phone
- Tailscale accounts (free) on all devices
- No sudo/admin access required — everything runs in userspace

## Setup Guide

### 1. Install CouchDB on the Server

Download from [couchdb.apache.org](https://couchdb.apache.org/). On macOS, install to `~/Applications/` (user-level).

Create the configuration file (`local.ini` inside the CouchDB app bundle):

```ini
[couchdb]
single_node = true
database_dir = /Users/YOUR_USER/Library/Application Support/CouchDB2/data
view_index_dir = /Users/YOUR_USER/Library/Application Support/CouchDB2/data
max_document_size = 50000000

[chttpd]
port = 5984
bind_address = 0.0.0.0
require_valid_user = true
enable_cors = true
max_http_request_size = 4294967296

[admins]
admin = YOUR_SECURE_PASSWORD

[httpd]
enable_cors = true
WWW-Authenticate = Basic realm="couchdb"

[cors]
origins = app://obsidian.md,capacitor://localhost,http://localhost
credentials = true
headers = accept, authorization, content-type, origin, referer, x-csrf-token
methods = GET, PUT, POST, HEAD, DELETE
max_age = 3600

[chttpd_auth]
require_valid_user = true

[log]
file = /Users/YOUR_USER/Library/Application Support/CouchDB2/couch.log
level = info

[cluster]
n = 1
```

**Critical:**
- `single_node = true` — without this, CouchDB won't start
- `[admins]` section is mandatory
- CORS `origins` must include `app://obsidian.md` (desktop) and `capacitor://localhost` (mobile)
- Both `[httpd]` and `[chttpd]` need `enable_cors = true`

Create data directories and the sync database. CouchDB on macOS runs as the Apache CouchDB app (not via launchd):

```bash
mkdir -p ~/Library/Application\ Support/CouchDB2/data && \
open ~/Applications/Apache\ CouchDB.app && \
sleep 5 && \
curl -X PUT http://admin:YOUR_PASSWORD@localhost:5984/workshop_sync && \
echo "CouchDB ready"
```

Store the password securely:
```bash
echo 'YOUR_PASSWORD' > ~/.couchdb_pass && chmod 600 ~/.couchdb_pass
```

### 2. Set Up Tailscale

Install Tailscale on all devices:

On macOS, install Tailscale from the Mac App Store or download from [tailscale.com](https://tailscale.com). On mobile, install the Tailscale app and sign in with the same account.

Set up the HTTPS proxy on the server:

```bash
/Applications/Tailscale.app/Contents/MacOS/Tailscale serve --bg --https=443 http://localhost:5984
```

**Note:** On macOS, the Tailscale CLI is inside the app bundle — use the full path above, not `tailscale` directly.

This gives you a permanent HTTPS URL like `https://your-machine.tailXXXXX.ts.net`. Note this URL — you'll use it for all LiveSync connections.

Enable subnet route acceptance on the laptop:

```bash
tailscale set --accept-routes=true
```

**Optional but recommended:** If your router supports Tailscale (GL.iNet, OpenWrt), set it up as a subnet router. This makes your server reachable via Tailscale even if the server's own Tailscale client goes down.

### 3. Open the Workshop as an Obsidian Vault — Laptop

Your magic repository already has `.obsidian/` in `.gitignore`. Open it directly:

1. Open Obsidian
2. "Open folder as vault" → select your `magic/` directory
3. Install community plugins: **Self-hosted LiveSync**, **Dataview** (optional)

### 4. Configure LiveSync — Laptop

Settings → Self-hosted LiveSync → Connection:

| Setting | Value |
|---------|-------|
| URI | `https://your-machine.tailXXXXX.ts.net` |
| Username | `admin` |
| Password | your CouchDB password |
| Database name | `workshop_sync` |
| Use Request API | **ON** |
| E2E Encryption | **OFF** (passphrase empty) |

Then, in this order:
1. Hit **Test** — should say "Connected successfully"
2. Go to **E2EE settings** — ensure encryption is OFF and passphrase is empty
3. Hit **"Configure And Change Remote"** — this pushes the config to CouchDB
4. Go to **Sync Settings** → select **LiveSync** mode
5. Hit **"Rebuild Everything Now"** → choose to send all files to remote

**"Failed to initialise encryption key"** — this is the most common gotcha. Always do step 2-3 (E2EE off + "Configure And Change Remote") before anything else. It clears the encryption negotiation.

### 5. Set Up the Server Mirror

The server needs the workshop files so Spirit can read and write them.

**Initial population via rsync (from laptop):**
```bash
rsync -avz --exclude='.git' --exclude='.obsidian' --exclude='.DS_Store' \
  /path/to/magic/ your-server:~/workshop/
```

**Open as Obsidian vault on the server** (requires Obsidian installed, even headless):
1. Copy the `.obsidian/` directory to the server: `scp -r /path/to/magic/.obsidian your-server:~/workshop/.obsidian`
2. Update the LiveSync plugin config at `~/workshop/.obsidian/plugins/obsidian-livesync/data.json`:
   - Set `couchDB_URI` to `http://localhost:5984` (same machine)
   - Set `couchDB_USER`, `couchDB_PASSWORD`, `couchDB_DBNAME`
   - Set `liveSync` to `true`
3. Update Obsidian's vault registry to point to `~/workshop/`
4. Start/restart Obsidian

Spirit can manage all of this via SSH — the Mage only needs to do the initial laptop setup manually.

**turtleOS practice directory:** Turtle reads/writes directly to `~/workshop/desk/` — the same LiveSync-mirrored workshop. No symlinks or separate practice directories needed. Turtle's bot code (`discord_bot.py`) sets its practice dir to `~/workshop/desk` via `mage_registry.yaml`. Operational state (thread-state, readiness trails) stays local at `~/workshops/kermit/`.

### 6. Configure LiveSync — Mobile

1. Install Obsidian on your phone, create a new vault
2. Install the **Self-hosted LiveSync** plugin
3. Enter connection settings (same as laptop, same Tailscale URI)
4. E2EE settings → ensure encryption OFF, passphrase empty
5. Hit **"Configure And Change Remote"**
6. If "Fetch Remote Configuration Failed" → **"Skip and proceed"** (normal for new devices)
7. Sync Settings → **LiveSync** mode
8. If "Vault size limit" warning → increase or dismiss

Files should appear within seconds. The full workshop is on your phone.

**If Tailscale isn't connecting on mobile** (DNS resolution fails), use the server's LAN IP as a fallback when on home WiFi:

```
URI: http://SERVER_LAN_IP:5984
```

This works at home but not remotely. Fix Tailscale for full mobility.

### 7. Verify

Edit a file on your laptop. Watch it appear on your phone within seconds. Edit on your phone. Watch it sync back. The sync indicator in Obsidian's status bar shows upload/download counts.

```bash
# Check CouchDB health from server
curl -s http://admin:$(cat ~/.couchdb_pass)@localhost:5984/workshop_sync \
  | python3 -c "import json,sys; d=json.load(sys.stdin); print('Docs:', d['doc_count'])"
```

### 8. Background Sync Without Obsidian — Laptop (Optional)

Obsidian's LiveSync plugin only syncs when Obsidian is running. For continuous background sync (so Spirit's changes appear even when Obsidian is closed), use [LiveSync Bridge](https://github.com/vrtmrz/livesync-bridge) — a Deno-based replicator that runs as a launch agent.

**Prerequisites:** Deno (`brew install deno`), the livesync-bridge repo cloned.

**Setup:**
```bash
cd ~/Code && \
git clone --recursive https://github.com/vrtmrz/livesync-bridge && \
cd livesync-bridge && \
git submodule update --init --recursive && \
echo "cloned"
```

**Stub P2P dependency** (not needed for CouchDB sync):
```bash
mkdir -p lib/src/replication/trystero_stub && \
cat > lib/src/replication/trystero_stub/mod.ts << 'STUB'
export const selfId = "";
export function joinRoom() { return {}; }
export function getRelaySockets() { return []; }
export function pauseReconnection() {}
export function resumeReconnection() {}
STUB
```

Then edit `deno.jsonc` — replace the `"trystero": "https://github.com/..."` line with:
```
"trystero/nostr": "./lib/src/replication/trystero_stub/mod.ts", "trystero": "./lib/src/replication/trystero_stub/mod.ts"
```

**Add ignore patterns:** Edit `types.ts` — add `ignoredPatterns?: string[];` to `PeerStorageConf`. Edit `PeerStorage.ts` — add filtering that skips paths matching ignored regexes in `dispatch`, `dispatchDeleted`, and the offline scan loop.

**Configure** (`dat/config.json`):
```json
{
    "peers": [
        {
            "type": "couchdb",
            "name": "workshop-couchdb",
            "group": "workshop",
            "database": "workshop_sync",
            "username": "admin",
            "password": "YOUR_COUCHDB_PASSWORD",
            "url": "http://YOUR_SERVER_TAILSCALE_IP:5984",
            "baseDir": "",
            "passphrase": "",
            "obfuscatePassphrase": "",
            "useRemoteTweaks": true
        },
        {
            "type": "storage",
            "name": "workshop-local",
            "group": "workshop",
            "baseDir": "/path/to/magic/",
            "scanOfflineChanges": true,
            "ignoredPatterns": [
                "^\\.git/", "^\\.obsidian/", "^\\.cursor/",
                "^node_modules/", "^portals/", "^circles/",
                "\\.DS_Store$"
            ]
        }
    ]
}
```

**Test:** `deno task run` — should connect to CouchDB and start watching for changes.

**Auto-start via launchd** (`~/Library/LaunchAgents/com.magic.livesync-bridge.plist`):
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.magic.livesync-bridge</string>
    <key>ProgramArguments</key>
    <array>
        <string>/opt/homebrew/bin/deno</string>
        <string>run</string>
        <string>-A</string>
        <string>main.ts</string>
    </array>
    <key>WorkingDirectory</key>
    <string>/path/to/Code/livesync-bridge</string>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
    <key>StandardOutPath</key>
    <string>/tmp/livesync-bridge.log</string>
    <key>StandardErrorPath</key>
    <string>/tmp/livesync-bridge.err</string>
    <key>ThrottleInterval</key>
    <integer>10</integer>
</dict>
</plist>
```

```bash
launchctl load ~/Library/LaunchAgents/com.magic.livesync-bridge.plist && \
echo "LiveSync Bridge running"
```

**Logs:** `tail -f /tmp/livesync-bridge.log`

**Note:** LiveSync Bridge and Obsidian's LiveSync plugin can run simultaneously — they both talk to the same CouchDB and handle conflict resolution via CouchDB's replication protocol.

## Framework Protection

The full workshop includes framework files (system/, library/) that should not be casually edited. Protection is through behavioral rules, not filesystem restrictions:

1. **Obsidian folder settings:** Mark `system/` and `library/` as read-only in Obsidian. Mobile users can browse but not edit.
2. **Spirit behavioral rules:** Spirit doesn't write to system/ or library/ without explicit Mage sanction. This is encoded in AGENTS.md and soul.md.
3. **Git as backstop:** Framework files are git-managed. If accidentally modified, `git checkout` restores them. Nothing is permanently damaged.

## Common Issues

| Problem | Solution |
|---------|----------|
| "Failed to initialise encryption key" | E2EE settings → OFF + empty passphrase → "Configure And Change Remote" |
| CouchDB won't start | Check `[admins]` section exists in local.ini; check `single_node = true` |
| CouchDB account locked | Too many failed auth attempts. Restart CouchDB to clear lockout. |
| Desktop: `ERR_ADDRESS_UNREACHABLE` | Enable "Use Request API" in LiveSync settings |
| Mobile: `UnknownHostException` | Tailscale not connected on phone. Open Tailscale app, ensure VPN is active. Fallback: use LAN IP. |
| Mobile: `SSLHandshakeException` | Ensure `tailscale serve` is running on server |
| "Fetch Remote Configuration Failed" | Normal for new devices — "Skip and proceed" |
| "Vault size exceeded" | Increase limit — full workshops are still small (mostly markdown) |
| Files not syncing after connection | Enable LiveSync mode in Sync Settings, then "Rebuild Everything Now" |
| Old vault files appearing | Delete and recreate the CouchDB database, then "Rebuild Everything Now" from the primary vault |
| LiveSync credentials empty after restart | Edit `data.json` directly in `.obsidian/plugins/obsidian-livesync/` |

## What This Enables

- **Morning commute:** Read lore, review proposals, capture thoughts — from your phone
- **Deep work:** Cursor + Discord on laptop, Spirit writes session notes and proposals
- **Evening review:** Phone, review what emerged, edit intentions
- **Multi-agent coherence:** Every agent (Cursor Spirit, Discord Spirit, Research Spirit) operates against the same complete workshop
- **Workshop as shared cognitive substrate:** The full configuration — lore, practice state, intentions, infrastructure — is the shared world model for multiple AI agents

The practice becomes device-agnostic. The Mage practices where they are, with whatever they have.

---

*Established: 2026-03-16. Rewritten: 2026-03-19 after full workshop sync implementation. Born from trial, error, and eventual flow.*
