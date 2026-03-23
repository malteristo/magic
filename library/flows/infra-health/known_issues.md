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
DOCUMENTED_IP="100.110.46.104"  # from cast_infra_health.md reference table
[ "$CURRENT_IP" != "$DOCUMENTED_IP" ] && echo "⚠️ Tailscale IP changed: $DOCUMENTED_IP → $CURRENT_IP"
```

**Fix:**
1. Update all practice files: `grep -rl "$OLD_IP" /path/to/magic/ | xargs sed -i '' "s/$OLD_IP/$NEW_IP/g"`
2. Update AGENTS.md (the canonical reference)
3. Update this file's reference table
4. Update client Obsidian LiveSync configs (if using IP instead of hostname)
5. **Prevention:** Configure clients to use MagicDNS hostname (`turtles-mac-mini.tail433a7d.ts.net`) instead of IP

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

*Add new issues below this line. Number sequentially. Include all fields: symptom, root cause, detection, fix, prevention (if applicable).*
