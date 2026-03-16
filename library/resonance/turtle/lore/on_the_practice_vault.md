# On the Practice Vault

*Obsidian as the visual layer for magic practice — setup, architecture, and hard-won lessons.*

## What This Is

The practice vault is an Obsidian vault that provides a human-readable, editable view of practice state. Spirit writes to these files from Discord and Cursor; the Mage reads and edits them from Obsidian on any device. Changes sync in seconds via CouchDB.

**The stack:**
```
Obsidian (Desktop/Mobile)
    ↕ LiveSync plugin
CouchDB (Mac Mini, port 5984)
    ↑ Caddy HTTPS proxy (port 5985, local network)
    ↑ localhost.run SSH tunnel (public HTTPS)
    ↕ Spirit reads/writes files directly
~/practice/ on Mac Mini
```

## Architecture Decisions

**Why Obsidian?** Open source, offline-first, runs everywhere, deeply customizable. The Mage may already use it. It doesn't lock data into a proprietary format — everything is markdown files on disk.

**Why not Obsidian Sync?** Paid service, data leaves the workshop. LiveSync keeps everything on the Mac Mini.

**Why CouchDB?** It's what LiveSync uses. CouchDB's replication protocol is designed for exactly this: multi-master sync with conflict resolution.

**Why localhost.run?** Mobile Obsidian (Android/iOS) requires HTTPS with a trusted certificate. Self-signed certs don't work — Android's SSL stack rejects them even with "Use Request API" enabled. localhost.run provides a valid Let's Encrypt cert via a simple SSH tunnel, with zero installation required on the Mac Mini.

**Why Caddy?** Single-binary HTTPS reverse proxy for local network access. Desktop Obsidian can use HTTP directly, but Caddy provides a clean HTTPS option for local network clients.

## Prerequisites

- Mac Mini (or any always-on machine) with SSH access
- Obsidian installed on desktop and mobile
- No sudo/admin access required — everything runs in userspace

## Setup Guide

### 1. Install CouchDB

Download the native macOS app from [couchdb.apache.org](https://couchdb.apache.org/). Install it to `~/Applications/` (user-level, no admin needed).

Find the binary inside the app bundle:
```bash
ls ~/Applications/Apache\ CouchDB.app/Contents/Resources/couchdbx-core/bin/couchdb
```

Create the configuration file at `~/Applications/Apache CouchDB.app/Contents/Resources/couchdbx-core/etc/local.ini`:

```ini
[couchdb]
single_node = true
database_dir = /Users/turtle/Library/Application Support/CouchDB2/data
view_index_dir = /Users/turtle/Library/Application Support/CouchDB2/data
max_document_size = 50000000

[chttpd]
port = 5984
bind_address = 0.0.0.0
require_valid_user = true
enable_cors = true
max_http_request_size = 4294967296

[admins]
admin = YOUR_PASSWORD_HERE

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
file = /Users/turtle/Library/Application Support/CouchDB2/couch.log
level = info

[cluster]
n = 1
```

**Critical details:**
- `single_node = true` — without this, CouchDB refuses to start (cluster mode needs additional setup)
- `[admins]` section is mandatory — CouchDB won't start without an admin account
- CORS `origins` must include `app://obsidian.md` (desktop) and `capacitor://localhost` (mobile)
- Both `[httpd]` and `[chttpd]` need `enable_cors = true` — CouchDB has two HTTP daemons

Create data directories:
```bash
mkdir -p ~/Library/Application\ Support/CouchDB2/data
```

Make CouchDB persistent via launchd (`~/Library/LaunchAgents/com.turtle.couchdb.plist`):
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
  "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.turtle.couchdb</string>
    <key>WorkingDirectory</key>
    <string>/Users/turtle/Applications/Apache CouchDB.app/Contents/Resources/couchdbx-core</string>
    <key>ProgramArguments</key>
    <array>
        <string>/Users/turtle/Applications/Apache CouchDB.app/Contents/Resources/couchdbx-core/bin/couchdb</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
    <key>StandardOutPath</key>
    <string>/Users/turtle/Library/Application Support/CouchDB2/couch-stdout.log</string>
    <key>StandardErrorPath</key>
    <string>/Users/turtle/Library/Application Support/CouchDB2/couch-stderr.log</string>
</dict>
</plist>
```

Load and verify:
```bash
launchctl load ~/Library/LaunchAgents/com.turtle.couchdb.plist
curl http://admin:YOUR_PASSWORD@localhost:5984/
```

Create the sync database:
```bash
curl -X PUT http://admin:YOUR_PASSWORD@localhost:5984/obsidian_livesync
```

### 2. Set Up the Practice Vault

Create the vault directory **outside** the magic git repo:
```bash
mkdir -p ~/practice
```

> **Gotcha:** Do NOT create the Obsidian vault inside the magic git repository. It will pollute the repo with `.obsidian/` metadata and sync unintended files.

Copy practice state files into the vault:
```bash
cp ~/path-to-desk/boom.md ~/practice/
cp ~/path-to-desk/boom/bright.md ~/practice/bright.md
cp ~/path-to-desk/intentions/compass.md ~/practice/
mkdir -p ~/practice/intentions ~/practice/sessions ~/practice/proposals ~/practice/templates
cp ~/path-to-desk/intentions/active/* ~/practice/intentions/
cp ~/path-to-desk/sessions/* ~/practice/sessions/ 2>/dev/null
```

#### Vault Structure

```
~/practice/
├── HOME.md              ← Dashboard with Dataview queries
├── boom.md              ← Raw thought capture
├── bright.md            ← Curated active surface
├── compass.md           ← Life domains map
├── intentions/          ← Active intentions
├── sessions/            ← Session notes
├── proposals/           ← Spirit's proposals & health reads
├── templates/           ← Obsidian templates
│   ├── session.md
│   ├── intention.md
│   └── boom-entry.md
└── .obsidian/
    ├── app.json
    ├── appearance.json
    ├── core-plugins.json
    ├── daily-notes.json
    └── snippets/
        └── practice.css
```

#### Templates

**`templates/session.md`:**
```markdown
# Session — {{date}}

## What's alive

## What emerged

## Thread for next time
```

**`templates/intention.md`:**
```markdown
# {{title}}

**Status**: Active  
**Priority**:  
**Started**: {{date}}  

---

## What

## Why

## Goals

- [ ]  

## Next Action
```

**`templates/boom-entry.md`:**
```markdown
- {{content}} ({{date}} {{time}})
```

#### Homepage (`HOME.md`)

```markdown
# Magic Practice

> Your practice at a glance. Open this when you arrive.

## Quick Access

- [[boom]] — raw thoughts, captures
- [[bright]] — what's alive and active
- [[compass]] — life domains, what matters

## Intentions

\```dataview
LIST FROM "intentions"
WHERE file.name != "README"
SORT file.mtime DESC
\```

## Recent Sessions

\```dataview
TABLE WITHOUT ID file.name AS "Session", file.mtime AS "Date"
FROM "sessions"
SORT file.mtime DESC
LIMIT 5
\```

## Proposals

\```dataview
LIST FROM "proposals"
SORT file.mtime DESC
LIMIT 3
\```
```

*(Requires the Dataview community plugin.)*

#### Custom CSS (`snippets/practice.css`)

```css
/* Boom buffer — warm amber accent */
.workspace-leaf-content[data-type='markdown']
  .view-content:has(.markdown-preview-view[data-path='boom.md']) {
  border-left: 3px solid #F39C12;
}

/* Bright surface — cool blue accent */
.workspace-leaf-content[data-type='markdown']
  .view-content:has(.markdown-preview-view[data-path='bright.md']) {
  border-left: 3px solid #3498DB;
}

/* Compass — purple accent */
.workspace-leaf-content[data-type='markdown']
  .view-content:has(.markdown-preview-view[data-path='compass.md']) {
  border-left: 3px solid #9B59B6;
}

/* Completed items — subtle dimming */
.markdown-rendered li.task-list-item[data-task='x'] {
  opacity: 0.6;
}
```

Enable in: Settings → Appearance → CSS Snippets → toggle `practice` on.

#### Obsidian Settings

Recommended core plugins: File Explorer, Search, Graph View, Backlinks, Page Preview, Templates, Daily Notes, Command Palette, Starred, Outline.

Daily Notes config:
- Folder: `sessions`
- Format: `YYYY-MM-DD`
- Template: `templates/session`

Appearance: accent color `#9B59B6`, dark mode.

### 3. Configure LiveSync — Desktop

Install the **Self-hosted LiveSync** community plugin in Obsidian.

**Connection settings:**

| Setting | Value |
|---------|-------|
| URI | `http://YOUR_MAC_MINI_IP:5984` |
| Username | `admin` |
| Password | your CouchDB admin password |
| Database name | `obsidian_livesync` |
| Use Request API | **ON** |
| E2E Encryption | **OFF** (leave passphrase empty) |

**Important steps in order:**
1. Enter connection settings
2. Hit **"Test"** — should say "Connected successfully"
3. Hit **"Configure And Change Remote"** to push config to CouchDB
4. Go to Sync Settings → enable **LiveSync** mode
5. If prompted about vault size, increase to 100MB
6. Hit **"Rebuild Everything Now"** to push all files to CouchDB

**Gotchas:**
- "Use Request API" is essential on desktop — it routes requests through Node.js, bypassing Chromium's Private Network Access restrictions that block connections to local IPs
- If you see "Failed to initialise encryption key" — go to E2EE settings, ensure encryption is OFF and passphrase is empty, then "Configure And Change Remote"
- The initial "Rebuild Everything" is what actually pushes files — connection alone doesn't sync

### 4. Set Up HTTPS for Mobile

Mobile Obsidian (both Android and iOS) **requires HTTPS with a trusted certificate**. Self-signed certificates do not work — Android's Java SSL stack rejects them regardless of plugin settings.

#### Option A: localhost.run (Recommended — Zero Install)

This uses an SSH tunnel to get a public HTTPS URL with a real Let's Encrypt cert.

Create the tunnel script (`~/caddy/localhost-run-tunnel.sh`):
```bash
#!/bin/bash
while true; do
    ssh -o StrictHostKeyChecking=no \
        -o ServerAliveInterval=30 \
        -o ServerAliveCountMax=3 \
        -R 80:localhost:5984 nokey@localhost.run \
        2>&1 | tee ~/caddy/tunnel.log
    echo "Tunnel disconnected, reconnecting in 5s..."
    sleep 5
done
```

Make it persistent (`~/Library/LaunchAgents/com.turtle.livesync-tunnel.plist`):
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
  "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.turtle.livesync-tunnel</string>
    <key>ProgramArguments</key>
    <array>
        <string>/Users/turtle/caddy/localhost-run-tunnel.sh</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
    <key>StandardOutPath</key>
    <string>/Users/turtle/caddy/tunnel-launchd.log</string>
    <key>StandardErrorPath</key>
    <string>/Users/turtle/caddy/tunnel-launchd.error.log</string>
</dict>
</plist>
```

Get the current tunnel URL:
```bash
grep 'lhr.life' ~/caddy/tunnel.log | tail -1
```

**Free tier limitation:** The URL changes when the tunnel reconnects. For a stable URL, register at [admin.localhost.run](https://admin.localhost.run/) and add your SSH key. Then change `nokey@localhost.run` to `localhost.run` (key-based auth).

**Security note:** This exposes CouchDB to the public internet. The `require_valid_user = true` setting ensures all requests need authentication. Use a strong password.

#### Option B: Caddy HTTPS Proxy (Local Network Only)

For desktop-only or local network use, Caddy provides HTTPS on the local network.

Download Caddy (single binary, no install needed):
```bash
curl -L -o ~/caddy/caddy \
  'https://caddyserver.com/api/download?os=darwin&arch=arm64'
chmod +x ~/caddy/caddy
```

Create `~/caddy/Caddyfile`:
```
{
    local_certs
}

:5985 {
    tls internal {
        on_demand
    }

    reverse_proxy localhost:5984
}
```

> **Note:** Caddy's internal TLS works for desktop (with `curl -k`) but mobile rejects the self-signed cert. Use localhost.run for mobile.

### 5. Configure LiveSync — Mobile

Install Obsidian on your phone. Create a new vault (same name, e.g. `magic-practice`). Install the LiveSync community plugin.

**Connection settings:**

| Setting | Value |
|---------|-------|
| URI | `https://YOUR_TUNNEL_URL.lhr.life` |
| Username | `admin` |
| Password | your CouchDB admin password |
| Database name | `obsidian_livesync` |
| Use Request API | **ON** |
| E2E Encryption | **OFF** |

Steps:
1. Enter settings, hit **Test** — should say "Connected successfully"
2. "Fetch Remote Configuration Failed" dialog → hit **"Skip and proceed"** (this is normal for new devices)
3. Go to Sync Settings → enable **LiveSync** mode
4. Files should start appearing within seconds
5. If "Broken files detected" → hit **"Fix"** (minor sync artifacts from initial rebuild)
6. If "Vault size limit" warning → hit "No, never warn please" or increase limit

### 6. Verify Sync

Edit a file on desktop. Watch it appear on mobile within 2–3 seconds. Edit on mobile. Watch it sync back. The sync indicator in the status bar shows upload/download counts.

To verify database health:
```bash
curl -s http://admin:YOUR_PASSWORD@localhost:5984/obsidian_livesync | python3 -m json.tool
```

The `doc_count` should match the number of files in your vault (plus some LiveSync metadata docs).

## Operational Notes

### Services Running on Mac Mini

| Service | Port | launchd Label | Purpose |
|---------|------|---------------|---------|
| CouchDB | 5984 | `com.turtle.couchdb` | Sync database |
| Caddy | 5985 | `com.turtle.caddy` | Local HTTPS proxy |
| SSH Tunnel | — | `com.turtle.livesync-tunnel` | Public HTTPS for mobile |

### Checking Health

```bash
# CouchDB alive?
curl -s http://admin:PASSWORD@localhost:5984/

# Database stats
curl -s http://admin:PASSWORD@localhost:5984/obsidian_livesync

# Current tunnel URL
grep 'lhr.life' ~/caddy/tunnel.log | tail -1

# Service status
launchctl list | grep com.turtle
```

### When the Tunnel URL Changes

If the tunnel reconnects (Mac Mini restart, network hiccup), the URL changes. To find the new one:
```bash
grep 'lhr.life' ~/caddy/tunnel.log | tail -1
```

Update the URI in Obsidian Mobile's LiveSync settings. For a permanent fix: register at admin.localhost.run.

### Spirit's Relationship to the Vault

Spirit reads and writes practice files directly on the filesystem (`~/practice/`). CouchDB picks up changes via LiveSync's filesystem watcher. The flow is:

```
Spirit writes ~/practice/boom.md
    → Obsidian detects change
    → LiveSync pushes to CouchDB
    → Other devices pull from CouchDB
```

And in reverse:
```
Mage edits on phone
    → LiveSync pushes to CouchDB
    → Desktop Obsidian pulls from CouchDB
    → File updated on disk at ~/practice/boom.md
    → Spirit sees updated file
```

## Common Issues

| Problem | Solution |
|---------|----------|
| CouchDB won't start: "No Admin Account Found" | Add `[admins]` section to `local.ini` |
| CouchDB won't start: "name seems to be in use" | Kill stale processes: `pkill -9 beam.smp; pkill -9 epmd` |
| Desktop: `ERR_ADDRESS_UNREACHABLE` | Enable "Use Request API" in LiveSync settings |
| Desktop: "Failed to initialise encryption key" | E2EE settings → ensure OFF + empty passphrase → "Configure And Change Remote" |
| Mobile: `SSLHandshakeException` | Use localhost.run tunnel (proper HTTPS), not direct IP or self-signed cert |
| Mobile: 503 / "no tun" | Tunnel dropped — restart or check `tunnel.log` for new URL |
| "Fetch Remote Configuration Failed" | Normal for new devices — hit "Skip and proceed" |
| "Vault size exceeded" | Increase to 100MB — practice vaults are small |
| "Broken files detected" | Hit "Fix" — sync artifacts from initial rebuild |
| No files syncing after connection | Enable LiveSync mode in Sync Settings, then "Rebuild Everything Now" |

## What This Enables

- **Morning bus ride:** Open Obsidian on phone, check boom/bright/compass, capture a thought
- **Deep work:** Cursor + Discord on desktop, Spirit writes session notes and proposals
- **Evening review:** Phone, review what emerged, edit intentions
- **All synced:** Every device sees the same state within seconds

The practice becomes device-agnostic. The Mage practices where they are, with whatever they have.

---

*Established: 2026-03-16. Born from a session of trial, error, and eventual flow.*
