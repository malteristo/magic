# Known Issues Registry

*The flow's growing memory. Each entry is a diagnosed issue that the flow can now detect and fix automatically.*

**How entries are added:** When `@infra-health` encounters a novel issue and Spirit resolves it through extended troubleshooting, the solution is proposed as a new entry here. Mage approves. Next occurrence → automatic detection and fix.

---

## Issue #001: Tailscale IP Changed

**First diagnosed:** 2026-03-23
**Layer:** 5 (Reachability)

**Symptom:** Devices can't connect to CouchDB. SSH to the documented Tailscale IP fails. `!diagnose` shows "CouchDB unreachable" even though the service is running locally.

**Root cause:** Tailscale assigned a new IP to the Mac Mini. This can happen after Tailscale app updates, re-authentication, or network changes. All practice files and client configs reference the old IP.

**Detection:**
```bash
CURRENT_IP=$(/Applications/Tailscale.app/Contents/MacOS/Tailscale ip -4 2>/dev/null)
DOCUMENTED_IP="<turtle-ssh>"  # from system/config/connections.md
[ "$CURRENT_IP" != "$DOCUMENTED_IP" ] && echo "⚠️ Tailscale IP changed: $DOCUMENTED_IP → $CURRENT_IP"
```

**Fix:**
1. Update all practice files: `grep -rl "$OLD_IP" /path/to/magic/ | xargs sed -i '' "s/$OLD_IP/$NEW_IP/g"`
2. Update AGENTS.md (the canonical reference)
3. Update this file's reference table
4. Update client Obsidian LiveSync configs (if using IP instead of hostname)
5. **Prevention:** Configure clients to use MagicDNS hostname (`<turtle-fqdn>`) instead of IP

---

## Issue #002: Tailscale Serve Not Running

**First diagnosed:** 2026-03-23
**Layer:** 2 (Connections)

**Symptom:** Mobile devices can't sync via HTTPS. Obsidian LiveSync on phone shows connection errors. `tailscale serve status` returns "No serve config."

**Root cause:** `tailscale serve` doesn't persist across Tailscale app restarts or Mac Mini reboots by default unless `--bg` flag was used.

**Detection:**
```bash
STATUS=$(/Applications/Tailscale.app/Contents/MacOS/Tailscale serve status 2>&1)
echo "$STATUS" | grep -q "No serve config" && echo "❌ Tailscale serve not configured"
```

**Fix:**
```bash
/Applications/Tailscale.app/Contents/MacOS/Tailscale serve --bg --https=443 http://localhost:5984
```
The `--bg` flag makes it persistent. Verify: `tailscale serve status` should show the proxy.

---

## Issue #003: Client Pointing at Wrong Database

**First diagnosed:** 2026-03-23
**Layer:** 3 (Sync)

**Symptom:** Device appears connected but notes don't sync. CouchDB log shows requests to a database name that doesn't match the active database. Different devices may have different notes.

**Root cause:** During CouchDB setup iterations, the database name changed (from `obsidian-livesync` → `obsidian_livesync` → `workshop_sync`). Devices that were configured during earlier iterations still point to old names.

**Detection:**
Check CouchDB stderr log for the database name in recent requests:
```bash
tail -50 ~/Library/Application\ Support/CouchDB2/couch-stderr.log | grep -oP '(?:GET|PUT|POST) /\K[^/_ ]+' | sort -u
```
If anything other than `workshop_sync` appears (and it's not a system database), a client is misconfigured.

**Fix:** On each device → Obsidian → Settings → Self-hosted LiveSync → Database name → change to `workshop_sync`.

**Prevention:** When changing the CouchDB database name, update all devices immediately. Document the active database name in `cast_infra_health.md` reference table.

---

## Issue #004: CouchDB Authentication Failure

**First diagnosed:** 2026-03-23
**Layer:** 2 (Connections)

**Symptom:** CouchDB responds with `{"error":"unauthorized","reason":"Name or password is incorrect."}`. The `!diagnose` command shows "CouchDB: cannot connect."

**Root cause:** CouchDB was reinstalled or the admin password was changed. Old configs (including the Discord bot's diagnose function) still reference old credentials.

**Detection:**
```bash
tail -20 ~/Library/Application\ Support/CouchDB2/couch-stderr.log | grep "Authentication failed"
```

**Fix:**
1. The admin password is set in CouchDB's `local.ini` under `[admins]` — the stored value is hashed, so you can't read it. Ask the Mage for the current password.
2. Update the Discord bot's diagnose function in `~/turtle-shell/discord_bot.py` (search for the CouchDB curl command).
3. Update any scripts or configs that use the old credentials.

**Prevention:** Store CouchDB credentials in a single `.env` file that all scripts reference, rather than hardcoding in multiple places.

---

## Issue #005: Tailscale CLI Not in PATH

**First diagnosed:** 2026-03-23
**Layer:** N/A (operational knowledge)

**Symptom:** `tailscale status` returns "command not found" when SSHed into Mac Mini.

**Root cause:** On macOS, Tailscale is installed as a GUI app at `/Applications/Tailscale.app/`. The CLI binary is inside the app bundle, not in PATH.

**Detection:** Automatic — if `which tailscale` fails.

**Fix:** Use full path: `/Applications/Tailscale.app/Contents/MacOS/Tailscale`

**Note:** Do NOT add this to PATH system-wide — it can conflict with updates. Just use the full path in scripts and commands.

---

## Issue #006: CouchDB Not Managed by launchd

**First diagnosed:** 2026-03-23
**Layer:** 1 (Services)

**Symptom:** `launchctl list | grep couch` returns nothing. CouchDB is running but not as a managed service.

**Root cause:** CouchDB was installed as the standalone Mac app (`Apache CouchDB.app`), not via Homebrew. It runs as `beam.smp` and doesn't register with launchd.

**Detection:** `pgrep -la beam.smp` (process check, not launchd check)

**Fix for restart:** `open ~/Applications/Apache\ CouchDB.app` (or wherever the app is installed)

**Note:** The `!diagnose` Discord command checks `_check_launchd("com.turtle.couchdb")` which will always fail for the Mac app version. The bot's diagnose function should be updated to check `pgrep beam.smp` instead.

---

## Issue #007: LiveSync "Failed to initialise encryption key"

**First documented:** 2026-03-16 (from `on_the_practice_vault.md`)
**Layer:** 3 (Sync)

**Symptom:** LiveSync shows "Failed to initialise encryption key" on connection. Sync does not start.

**Root cause:** E2EE negotiation is in an inconsistent state. This happens when encryption settings were changed or when a new device connects to an existing database without matching encryption config.

**Fix:**
1. Obsidian → Settings → Self-hosted LiveSync → E2EE settings
2. Set encryption **OFF**, passphrase **empty**
3. Hit **"Configure And Change Remote"** — this pushes the clean config to CouchDB
4. Reconnect. Sync should start.

**Note:** Step 2-3 must be done in that order — disable E2EE first, then push config. Doing it backward leaves the negotiation in a broken state.

---

## Issue #008: CouchDB Account Lockout

**First documented:** 2026-03-16 (from `on_the_practice_vault.md`)
**Layer:** 2 (Connections)

**Symptom:** CouchDB returns 401 unauthorized even with correct credentials. Logs show repeated "Authentication failed" entries.

**Root cause:** Too many failed authentication attempts. CouchDB has a lockout mechanism.

**Detection:**
```bash
grep "Authentication failed" ~/Library/Application\ Support/CouchDB2/couch-stderr.log | tail -20
```

**Fix:** Restart CouchDB to clear the lockout. For Mac app: quit and reopen `~/Applications/Apache CouchDB.app`.

---

## Issue #009: Desktop LiveSync ERR_ADDRESS_UNREACHABLE

**First documented:** 2026-03-16 (from `on_the_practice_vault.md`)
**Layer:** 3 (Sync)

**Symptom:** Desktop Obsidian shows `ERR_ADDRESS_UNREACHABLE` in LiveSync. Server is running and reachable from other tools.

**Root cause:** Obsidian's default HTTP handler has issues with some network configurations.

**Fix:** LiveSync settings → enable **"Use Request API"** toggle. This switches to a different HTTP handler.

---

## Issue #010: Mobile LiveSync UnknownHostException

**First documented:** 2026-03-16 (from `on_the_practice_vault.md`)
**Layer:** 5 (Reachability)

**Symptom:** Mobile Obsidian shows `UnknownHostException`. Cannot resolve the server hostname.

**Root cause:** Tailscale is not connected on the phone. Without Tailscale, the MagicDNS hostname can't be resolved.

**Fix:**
1. Open Tailscale app on phone, ensure VPN is active
2. If Tailscale is active but still failing: try the server's LAN IP (`http://SERVER_LAN_IP:5984`) as a temporary fallback (works on home WiFi only)

---

## Issue #011: Mobile LiveSync SSLHandshakeException

**First documented:** 2026-03-16 (from `on_the_practice_vault.md`)
**Layer:** 2 (Connections)

**Symptom:** Mobile Obsidian shows `SSLHandshakeException` when connecting.

**Root cause:** `tailscale serve` is not running on the server, so there's no HTTPS endpoint with a valid TLS certificate.

**Detection:** Same as Issue #002 (check `tailscale serve status`).

**Fix:** Same as Issue #002 (run `tailscale serve --bg --https=443 http://localhost:5984`).

---

## Issue #012: Mac Mini Sleeping — Services Unreachable

**First documented:** 2026-03-05 (from `on_turtle_operations.md`)
**Layer:** 1 (Services) / 5 (Reachability)

**Symptom:** SSH connections timeout or fail. All services unreachable. Mac Mini responds to ping but SSH hangs during banner exchange.

**Root cause:** Mac Mini goes to sleep after display inactivity. Upon wake, services start simultaneously, causing high CPU load that blocks SSH.

**Detection:** `ping` succeeds but `ssh` hangs → sleep/wake cascade.

**Fix (immediate):**
1. Wake the Mac Mini physically (keyboard/mouse)
2. Wait 30-60 seconds for load to settle
3. SSH in, check `uptime` and `top -l 1 | head -5` for load average

**Prevention:** Install a `caffeinate` LaunchAgent to prevent sleep on AC power:
```xml
<!-- ~/Library/LaunchAgents/com.turtle.caffeinate.plist -->
<plist version="1.0">
<dict>
    <key>Label</key><string>com.turtle.caffeinate</string>
    <key>ProgramArguments</key>
    <array><string>/usr/bin/caffeinate</string><string>-s</string></array>
    <key>RunAtLoad</key><true/>
    <key>KeepAlive</key><true/>
</dict>
</plist>
```
Load: `launchctl load ~/Library/LaunchAgents/com.turtle.caffeinate.plist`

---

## Issue #013: Ollama TCC Permissions After Account Change

**First documented:** 2026-02-28 (from `on_turtle_operations.md`)
**Layer:** 1 (Services)

**Symptom:** Ollama fails with `operation not permitted` when accessing models, even though the volume is mounted and ownership is correct.

**Root cause:** macOS TCC (Transparency, Consent, and Control) grants are tied to user identity. User rename, migration, or fresh account invalidates prior access grants for apps accessing external volumes.

**Detection:** Check Ollama logs for "operation not permitted" errors.

**Fix:** System Settings → Privacy & Security → Files & Folders → Ollama → enable Removable Volumes. Or: open the Ollama app from the GUI once to trigger the TCC prompt.

---

## Issue #014: LiteLLM Hung After Sleep/Wake

**First documented:** 2026-03-05 (from `on_turtle_operations.md`)
**Layer:** 2 (Connections)

**Symptom:** LiteLLM process is running but `curl localhost:4000/health` never responds. AI inference via LiteLLM routing fails silently.

**Root cause:** LiteLLM doesn't recover cleanly from system sleep. The proxy enters a hung state.

**Detection:**
```bash
pgrep -f litellm > /dev/null && curl -s -m 5 http://localhost:4000/health > /dev/null 2>&1 || echo "⚠️ LiteLLM running but not responding"
```

**Fix:** Restart LiteLLM: `brew services restart litellm` or kill and relaunch via its LaunchAgent.

**Prevention:** Add a health check to the LiteLLM LaunchAgent that restarts on failure.

---

## Issue #015: "Fetch Remote Configuration Failed" on New Device

**First documented:** 2026-03-16 (from `on_the_practice_vault.md`)
**Layer:** 3 (Sync)

**Symptom:** New device shows "Fetch Remote Configuration Failed" when first connecting to LiveSync.

**Root cause:** This is **normal behavior** — the new device has no stored remote config to fetch. Not an error.

**Fix:** Click **"Skip and proceed"**. Then configure sync settings manually and choose LiveSync mode.

---

## Issue #016: Discord Bot Duplicate Responses (Multiple Instances)

**First diagnosed:** 2026-03-29
**Layer:** 1 (Services)

**Symptom:** Turtle sends two (or more) different responses to a single user message. The responses are genuinely different — not split chunks of one long reply. Reply-to-message ratio exceeds 1.0 (e.g. 1.6x observed: 27 replies to 17 messages).

**Root cause:** Multiple `discord_bot.py` processes running simultaneously. Each receives every message from the Discord gateway and processes it independently. The per-channel `asyncio.Lock` only prevents concurrency *within a single process* — it cannot coordinate across OS processes.

**How it happens:** A manual restart (e.g. `nohup python3 discord_bot.py &`) while the launchd-managed instance (`com.turtle.discord`) is still running — or launchd respawns while a manual instance is already up. After a crash, both launchd and a manual restart can race.

**Detection:**
```bash
PIDS=$(pgrep -f discord_bot.py)
COUNT=$(echo "$PIDS" | wc -l | tr -d ' ')
[ "$COUNT" -gt 1 ] && echo "⚠️ $COUNT bot instances running: $PIDS"
```

**Fix:**
1. Kill all instances: `pkill -f discord_bot.py`
2. Wait 2 seconds for launchd to respawn the managed instance
3. Verify single instance: `pgrep -f discord_bot.py` should return exactly one PID
4. If launchd doesn't respawn: `launchctl kickstart gui/$(id -u)/com.turtle.discord`

**Prevention:**
- **Always** restart via launchd: `launchctl kickstart -k gui/$(id -u)/com.turtle.discord`
- **Never** use `nohup` or `&` to start the bot manually — launchd manages it
- The bot now has a message-ID dedup guard (`_processed_message_ids`) that prevents double-processing within a single process (defense against Discord gateway replays), but this does not help across multiple processes

---

## Issue #017: Multi-Mage Vault Pollution (Framework Files in Practice CouchDB)

**First diagnosed:** 2026-03-29
**Layer:** 3 (Sync)

**Symptom:** A practitioner's Obsidian vault shows hundreds of unfamiliar files — `system/`, `library/`, `archive/`, `AGENTS.md`, etc. Their vault is cluttered with framework internals they never created.

**Root cause:** The practitioner's Obsidian vault was initialized from a template or copied from an existing workshop that included the full Magic framework tree. LiveSync faithfully synced all of it to their CouchDB database. If a LiveSync bridge is then connected, framework files propagate bidirectionally between CouchDB and filesystem.

**Detection:**
```bash
# Check for framework directories in a practitioner's CouchDB
DB="nesrine_sync"  # or whatever the practitioner's database name is
curl -s "http://localhost:5984/$DB/_all_docs" -u admin:PASSWORD | \
  python3 -c "import json,sys; docs=json.load(sys.stdin); \
  cruft=[r['id'] for r in docs['rows'] if not r['id'].startswith('h:') and \
  any(r['id'].startswith(p) for p in ['library/','system/','archive/','circles/','box/','desk/','portals/'])]; \
  print(f'{len(cruft)} framework docs found') if cruft else print('Clean')"
```

**Fix:**
1. **Stop the bridge** (if running): `launchctl bootout gui/$(id -u)/com.magic.MAGE-bridge`
2. **Bulk-delete framework docs from CouchDB** using `_bulk_docs` with `_deleted: true`
3. **Remove framework dirs from filesystem**: `rm -rf ~/workshops/MAGE/{archive,box,circles,desk,library,portals,proposals,system,universe}`
4. **Update bridge config** (`config-MAGE.json`) with ignore patterns for framework paths
5. **Restart the bridge**: `launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.magic.MAGE-bridge.plist`

**Prevention:**
- When onboarding a new practitioner, start with a **clean vault** — only practice files (boom.md, bright.md, compass.md, mirror.md, system.md, resonance.md, intentions/, sessions/)
- Bridge configs should include ignore patterns for framework directories from day one
- Template ignore patterns for bridge config:
  ```json
  "ignoredPatterns": [
      "^\\.git/", "^\\.obsidian/", "\\.DS_Store$",
      "^archive/", "^box/", "^circles/", "^desk/",
      "^library/", "^portals/", "^proposals/",
      "^system/", "^universe/", "^thread-state/",
      "^AGENTS", "^LICENSE", "^README", "^FAQ",
      "^MAGIC_SPEC", "^ONBOARDING", "^TROUBLESHOOTING", "^mage_seal"
  ]
  ```

---

*Add new issues below this line. Number sequentially. Include all fields: symptom, root cause, detection, fix, prevention (if applicable).*
