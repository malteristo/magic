# Infrastructure Health Check

**Execute this now.** Read all phases, then perform them in sequence. Report findings as you go.

---

## Phase 0: Establish Connection

**Determine the SSH target.** Try in order:

1. SSH config alias: `ssh turtle` (if configured in `~/.ssh/config`)
2. Tailscale hostname: `ssh turtle@<turtle-hostname>` (MagicDNS short name)
3. Tailscale IP: `ssh turtle@<turtle-ssh>`
4. LAN fallback: `ssh turtle@<turtle-ssh>`

> See `system/config/connections.md` for current addresses.

If none work → **STOP.** The Mac Mini is unreachable. Possible causes:
- Mac Mini is powered off or sleeping (check physically)
- Tailscale not connected on either end
- Network issue (router, ISP)

Report: which method succeeded, latency observed.

---

## Phase 1: Services (Layer 1)

SSH in and check all critical services:

```bash
echo "=== Services ===" && \
(pgrep -f beam.smp > /dev/null 2>&1 && echo "✅ CouchDB" || echo "❌ CouchDB NOT RUNNING") && \
(pgrep -f discord_bot.py > /dev/null 2>&1 && echo "✅ Discord bot" || echo "❌ Discord bot NOT RUNNING") && \
(pgrep -f ollama > /dev/null 2>&1 && echo "✅ Ollama" || echo "❌ Ollama not running (non-critical)") && \
(pgrep -f Obsidian.app > /dev/null 2>&1 && echo "✅ Obsidian" || echo "❌ Obsidian NOT RUNNING")
```

**Note:** The Discord bot runs as a Python process (`Python -u discord_bot.py`), not a binary named `discord_bot`. Always use `pgrep -f` (full command line match) rather than `pgrep -la` (process name match).

**Auto-fix for down services:**
- CouchDB: `open ~/Applications/Apache\ CouchDB.app` (it's a Mac app, not launchd)
- Discord bot: `launchctl kickstart -k gui/$(id -u)/com.turtle.discord`
- Obsidian: `open /Applications/Obsidian.app`
- Ollama: `brew services start ollama` or `ollama serve &`

After restarting, wait 10 seconds and re-check.

---

## Phase 2: Connections (Layer 2)

Check that running services are actually responding:

```bash
echo "=== CouchDB ===" && \
curl -s -m 5 http://localhost:5984/ && echo "" && \
echo "=== Ollama ===" && \
curl -s -m 5 http://localhost:11434/api/tags | head -c 200 && echo "" && \
echo "=== Tailscale ===" && \
/Applications/Tailscale.app/Contents/MacOS/Tailscale status 2>&1 | head -10 && \
echo "=== Tailscale Serve ===" && \
/Applications/Tailscale.app/Contents/MacOS/Tailscale serve status 2>&1
```

**Check CouchDB database state:**

The admin password is stored hashed in CouchDB's `local.ini`. To find the config:
```bash
cat ~/Applications/Apache\ CouchDB.app/Contents/Resources/couchdbx-core/etc/local.ini
```

Check the `[admins]` section for the username. The password itself is hashed — you cannot read it. The Mage knows the password. If authentication is needed, ask.

**Check which databases exist:**
```bash
ls ~/Library/Application\ Support/CouchDB2/data/shards/00000000-7fffffff/ 2>/dev/null
```

**Expected healthy state:**
- CouchDB responds on port 5984 (may require auth — that's normal if `require_valid_user = true`)
- `workshop_sync` database exists in shards
- Tailscale shows peer devices as connected
- Tailscale serve is proxying port 5984 as HTTPS

**Tailscale serve not running:**
```bash
/Applications/Tailscale.app/Contents/MacOS/Tailscale serve --bg --https=443 http://localhost:5984
```

**Known issue:** Tailscale CLI is NOT in PATH on Mac Mini. Always use the full path: `/Applications/Tailscale.app/Contents/MacOS/Tailscale`.

---

## Phase 3: Sync (Layer 3)

Check that data is actually flowing:

```bash
echo "=== CouchDB database sizes ===" && \
du -sh ~/Library/Application\ Support/CouchDB2/data/shards/00000000-7fffffff/*.couch 2>/dev/null && \
echo "=== Recent CouchDB activity ===" && \
tail -10 ~/Library/Application\ Support/CouchDB2/couch-stderr.log 2>/dev/null && \
echo "=== Workshop files freshness ===" && \
ls -lt ~/workshops/kermit/ 2>/dev/null | head -10 && \
echo "=== Practice state freshness ===" && \
ls -lt ~/practice/ 2>/dev/null | head -10
```

**What to look for:**
- CouchDB log shows recent 200 OK responses → sync is active
- CouchDB log shows 401 errors → wrong credentials on a client
- CouchDB log shows no recent entries → nothing is syncing
- Multiple databases exist → check if clients are pointing to the right one (currently `workshop_sync`)
- Workshop/practice files recently modified → practice is flowing

**Common issue: Client pointing at wrong database.**
Check the CouchDB log for the database name in requests. If a client is hitting `obsidian_livesync` instead of `workshop_sync`, the client's LiveSync settings need updating.

---

## Phase 4: Practice Flow (Layer 4)

Check that the practice itself is alive (not just infrastructure):

```bash
echo "=== Discord bot recent activity ===" && \
tail -20 ~/turtleos/logs/discord.log 2>/dev/null && \
echo "=== Session notes ===" && \
ls -lt ~/workshops/kermit/sessions/ 2>/dev/null | head -5 && \
echo "=== Proposals ===" && \
ls ~/workshops/kermit/proposals/ 2>/dev/null && \
echo "=== Boom state ===" && \
wc -l ~/practice/boom.md 2>/dev/null
```

**Signals:**
- No session notes in 3+ days → practice may be quiet (not necessarily broken)
- Proposals accumulating → Mage hasn't reviewed (mention during report)
- Boom growing without sweeps → suggest `@boom` or `!sweep`
- Discord log shows errors → investigate specific error

---

## Phase 5: Reachability (Layer 5)

Check that external devices can reach the Mac Mini:

```bash
echo "=== Tailscale devices ===" && \
/Applications/Tailscale.app/Contents/MacOS/Tailscale status 2>&1 && \
echo "=== CouchDB CORS config ===" && \
grep -A5 '\[cors\]' ~/Applications/Apache\ CouchDB.app/Contents/Resources/couchdbx-core/etc/local.ini && \
echo "=== Network interfaces ===" && \
ifconfig | grep 'inet ' | grep -v 127.0.0.1
```

**What to verify:**
- Peer devices show as connected (not "offline" or "idle" for too long)
- CouchDB CORS allows `app://obsidian.md` and `capacitor://localhost`
- The Mac Mini's Tailscale IP matches what's documented in the practice (AGENTS.md)
- Tailscale serve URL matches what's configured in Obsidian LiveSync on devices

**IP change detection:**
If the Tailscale IP has changed from what's documented, report this prominently. IP changes require updating:
1. AGENTS.md (the canonical reference)
2. All flow files that hardcode the IP (grep for the old IP across the workspace)
3. Client device LiveSync configurations (if using IP instead of hostname)

Prefer MagicDNS hostname (`<turtle-fqdn>`) over IP in client configs — it survives IP changes.

---

## Phase 6: Health Report

Produce a summary for the Mage:

```
Infrastructure Health Report
─────────────────────────────
Layer 1 (Services):     ✅/❌ [details]
Layer 2 (Connections):  ✅/❌ [details]
Layer 3 (Sync):         ✅/❌ [details]
Layer 4 (Practice):     ✅/⚠️/❌ [details]
Layer 5 (Reachability): ✅/❌ [details]

Issues found: [count]
Auto-fixed:   [count]
Needs attention: [list]
```

**Tone:** Non-technical where possible. "Your notes are syncing normally" not "CouchDB doc_count advancing at expected rate."

---

## Phase 7: Extended Troubleshooting (if needed)

When a check fails and the cause isn't in the known issues registry:

1. **Gather evidence.** Read logs, check configs, inspect network state. Be thorough — collect everything before hypothesizing.
2. **Form hypotheses.** What could cause this specific symptom? List 2-3 possible explanations ranked by likelihood.
3. **Test.** For each hypothesis, what would confirm or rule it out? Run the test.
4. **Fix.** Apply the fix. Verify it worked.
5. **Document.** Propose adding the issue to `known_issues.md` with:
   - **Symptom:** What the Mage sees / what the check reports
   - **Root cause:** What was actually wrong
   - **Detection:** How to check for this automatically
   - **Fix:** Step-by-step resolution
   - **Prevention:** How to avoid it in the future (if applicable)

The Mage approves the addition. The flow learns.

---

## Reference: Key Paths on Mac Mini

| What | Where |
|------|-------|
| CouchDB app | `~/Applications/Apache CouchDB.app/` |
| CouchDB config | `~/Applications/Apache CouchDB.app/Contents/Resources/couchdbx-core/etc/local.ini` |
| CouchDB data | `~/Library/Application Support/CouchDB2/data/` |
| CouchDB logs | `~/Library/Application Support/CouchDB2/couch-stderr.log` |
| Tailscale CLI | `/Applications/Tailscale.app/Contents/MacOS/Tailscale` |
| Discord bot | `~/turtleos/discord_bot.py` |
| Discord bot logs | `~/turtleos/logs/discord.log` |
| Workshop (Kermit) | `~/workshops/kermit/` |
| Practice state | `~/practice/` |
| Mage registry | `~/turtleos/mage_registry.yaml` |
| SSH config (client) | `~/.ssh/config` on Mage's machine |

---

## Reference: Current Infrastructure State

*Updated: 2026-03-23*

| Parameter | Value |
|-----------|-------|
| Mac Mini Tailscale IP | `<turtle-ssh>` |
| Mac Mini Tailscale hostname | `<turtle-fqdn>` |
| Mac Mini LAN IP | `<turtle-ssh>` (DHCP — may change) |
| CouchDB port | 5984 |
| CouchDB bind address | `0.0.0.0` (all interfaces) |
| Active database | `workshop_sync` |
| CouchDB admin user | `admin` |
| Tailscale serve | `https://<turtle-fqdn>/` → `http://localhost:5984` |
| Obsidian LiveSync URI (devices) | `https://<turtle-fqdn>` or `http://<turtle-ssh>:5984` |
| SSH user | `turtle` |

*When values change, update this table and AGENTS.md together.*
