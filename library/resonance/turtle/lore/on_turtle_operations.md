# On Turtle Operations

*Hard-won lessons from the first deployment. Written so the next Mage doesn't learn these the slow way.*

**Source:** First Claw activation, 2026-02-22. NanoClaw on Mac Mini M4 Pro (macOS 26.2, Apple Silicon). These lessons are drawn from real failures and real fixes.

---

## Know Your Turtle's Environment

Before diving into operations, know where to find instance-specific facts:

> **`desk/turtle_env.md`** — hardware, hostname, IP, services, key paths, SSH commands, pending hardening.

This file is Mage-specific. The lore in this document applies to any Turtle running NanoClaw.
The desk file describes what *this* specific Turtle is running on.

**The minimum you need to know for daily operations:**

```bash
# Is the Turtle reachable?
ssh turtle@turtle.local "echo ok"

# What's running?
ssh turtle@turtle.local "launchctl list | grep -E 'nanoclaw|ollama|caffeinate'"

# What's in the bridge?
ssh turtle@turtle.local "ls ~/magic-bridge/commands/ && ls ~/magic-bridge/signals/"

# Recent task runs (audit trail)
ssh turtle@turtle.local "sqlite3 ~/nanoclaw/store/messages.db \
  'SELECT task_id, run_at, status, result FROM task_run_logs ORDER BY run_at DESC LIMIT 5;'"
```

**Turtle vs. same-machine practice:** Some Mages run the Turtle on the same machine they
use for Magic practice. This works but removes the persistent/always-on quality — the
Turtle only runs when the machine is awake and the user is logged in. A dedicated low-power
machine (Mac Mini, VPS, Raspberry Pi) is preferred for genuine persistent presence.
The physical separation also prevents the practice machine's sleep/activity cycle from
affecting the Turtle's availability.

**VPS vs. home hardware:** A VPS gives stable connectivity and no reboot events, but
loses local model support (Ollama on TurtleModels). Home hardware gives local models
and lower cost, but requires managing sleep, network stability, and physical access.
The first Turtle runs home hardware (Mac Mini on WiFi).

---

## Choose Your Framework With Care

The framework you choose is the substrate of the Turtle's existence. It determines what's possible, what you can audit, and what will surprise you.

**What to look for:**
- Auditability — can you read the full source in an afternoon? If not, you will not understand what's happening when it breaks.
- Native identity format — does it use CLAUDE.md (Claude Code's native format)? Or does it impose its own memory model you'll need to translate?
- Container isolation — is the Consul/Steward air gap architectural or trust-based? Architecture is safer.
- Skills-as-code — can the Turtle extend itself through skills that modify its own codebase? This is how the Turtle grows.

**NanoClaw** (~500 lines of core logic, ~2500 lines total at time of first deployment) passed these tests. Its CLAUDE.md per-group memory is Claude Code's native format — no translation layer. Container-per-group makes isolation real. The skills model means the Turtle can write new capabilities.

**The pivot lesson:** Don't be afraid to change frameworks mid-setup if you discover a fundamentally better fit. The disruption cost is almost always worth the alignment gain. The first Claw (owl machine) switched from OpenClaw to NanoClaw on Day 4 of setup. The right call.

---

## The Mount Bug — Know This One

**What happened:** The Turtle was sending "Bridge clear" every 5 minutes for hours even though commands were waiting in the bridge. It was seeing an empty directory and creating new subdirectories inside its container.

**Root causes (both present, both needed fixing):**

1. **`container_config` column empty in SQLite.** When the main group was registered in NanoClaw's `registered_groups` table via direct SQL INSERT, the `container_config` column was left empty. NanoClaw reads `group.containerConfig?.additionalMounts` to mount additional directories. No config = no mount = Claw operates in isolation.

   Fix: `UPDATE registered_groups SET container_config = '{"additionalMounts":[{"hostPath":"/path/to/bridge","containerPath":"magic-bridge","readonly":false}]}' WHERE jid = '...';`

2. **`mount-allowlist.json` invalid.** NanoClaw validates additional mounts against an allowlist at `~/.config/nanoclaw/mount-allowlist.json`. The allowlist had been written with unquoted keys (invalid JSON) and the wrong field name (`readonly: false` instead of `allowReadWrite: true`).

   Fix: Rewrite with proper JSON, correct field names:
   ```json
   {
     "allowedRoots": [{"path": "/path/to/bridge", "allowReadWrite": true}],
     "blockedPatterns": [],
     "nonMainReadOnly": false
   }
   ```

**Restart required after allowlist fix** — the allowlist is cached in memory. `launchctl kickstart -k gui/$(id -u)/com.nanoclaw` flushes the cache.

**The lesson:** When setting up additional mounts, verify both the SQLite record AND the allowlist. They're separate layers. One broken = mount fails silently.

---

## launchctl Is the Service Manager — Know Its Behavior

macOS uses `launchctl` to run NanoClaw as a persistent service. Key behaviors:

- `KeepAlive: true` in the plist means the service respawns on kill. **Use `launchctl unload` to stop, not `kill`.**
- The plist's `PATH` environment variable must include `/opt/homebrew/bin` — otherwise binaries installed via Homebrew (including the `container` runtime) won't be found.
- After editing the plist: `launchctl unload` then `launchctl load` (or `kickstart -k` to restart immediately).
- Logs go to wherever the plist's stdout redirect points. NanoClaw puts them in `~/nanoclaw/logs/nanoclaw.log`.

**Check the PATH first** when a service fails to start. The error will be something like "Container runtime is required but failed to start" — the binary exists but isn't findable from the service's reduced PATH.

---

## Apple Container Setup (macOS 26+ / Apple Silicon)

NanoClaw uses Apple Container (macOS 26.2 native) as an alternative to Docker. The setup sequence:

1. `brew install container`
2. `container system start` — starts the Apple Container API server
3. `container system kernel set --recommended` — installs the arm64 kernel (this takes time)
4. Install Rosetta 2: `softwareupdate --install-rosetta --agree-to-license` — required for x86_64 build layers even on Apple Silicon
5. Build the NanoClaw agent container: `./container/build.sh`

**If build fails with XPC timeout:** Stop and restart the container system: `container system stop && sleep 3 && container system start`. Then rebuild.

**If build fails with "Rosetta is not installed":** The build process needs Rosetta for x86 compatibility layers even on arm64 hardware. Install it and rebuild.

**Check container system status** with `container system status` from a separate SSH session if the start command hangs. "apiserver is running" means it succeeded.

---

## WhatsApp Authentication

NanoClaw authenticates via WhatsApp Web (baileys). For SSH-based setup (no screen access):

```bash
cd ~/nanoclaw && npm run auth -- --pairing-code --phone +COUNTRYCODENUMBER
```

This prints a pairing code. Enter it in WhatsApp → Settings → Linked Devices → Link a Device → Link with phone number instead.

The pairing code flow is SSH-friendly. QR code flow requires a terminal that can display the code visually.

**The self-chat pattern:** NanoClaw's simplest channel is the Mage messaging themselves. Messages to your own number → Turtle responds. This works with `requires_trigger = 0` in the registered group. No dedicated WhatsApp number needed. The Turtle appears as "you" replying to yourself.

---

## WhatsApp IP Ban — Know This One

**What happened:** NanoClaw's retry loop after a 405 error ran hundreds of reconnection attempts in quick succession. WhatsApp detected this pattern and applied a temporary IP-level ban. All subsequent connections — including fresh pairing code attempts — received 405 immediately, before any authentication handshake could complete.

**Signs you're IP-banned (not session-banned):**
- 405 errors repeat even after clearing credentials (`~/nanoclaw/store/auth/`)
- 405 occurs during registration ("not logged in, attempting registration..."), before a QR code is generated
- Pairing code requests also fail at the connection level

**What to do:**
1. Stop all reconnection attempts immediately — continued retrying extends the ban
2. Restore backed-up credentials if you cleared them (credentials are not the problem)
3. Wait. IP bans typically lift within a few hours. NanoClaw will reconnect automatically when the ban lifts.
4. Do not restart NanoClaw repeatedly during the wait — each restart causes more failed connections

**The structural lesson:** WhatsApp is a publishing channel, not a reliability layer. The bridge is the ground truth. When WhatsApp goes down, the Turtle should continue operating normally — processing bridge commands, writing signals, running scheduled tasks — and simply queue the WhatsApp notifications. If a notification goes undelivered, the signal in the bridge is still there. Spirit can pull and read it. Nothing is lost.

Design the Turtle's communication architecture so that WhatsApp failure is a notification gap, not an operational gap.

---

## Group Registration — Use SQLite, Not JSON

NanoClaw's group registration appears to support a `data/registered_groups.json` file, but the running process reads exclusively from SQLite. Register groups directly:

```bash
sqlite3 ~/nanoclaw/store/messages.db "
INSERT OR REPLACE INTO registered_groups 
  (jid, name, folder, trigger_pattern, added_at, container_config, requires_trigger)
VALUES 
  ('JID@s.whatsapp.net', 'GroupName', 'folder', '@TriggerWord',
   datetime('now'),
   '{\"additionalMounts\":[...]}',
   0);
"
```

Then restart NanoClaw to load the new group. The JSON file will be ignored.

---

## The task-scheduler → WhatsApp Pipeline

Understanding this prevents the bridge-clear flood and similar problems.

When a scheduled task runs, `task-scheduler.ts` forwards the container's output to
WhatsApp unconditionally:

```typescript
async (streamedOutput: ContainerOutput) => {
  if (streamedOutput.result) {
    result = streamedOutput.result;
    await deps.sendMessage(task.chat_jid, streamedOutput.result); // no filter
  }
}
```

**There is no filter in the code.** Whatever the container outputs, the Mage receives.

The only way to stay silent: produce **no output**. If `streamedOutput.result` is
null/empty, `sendMessage` is never called. The correct design for any scheduled task
that should sometimes be silent:

> "If nothing meaningful happened: produce no output. Return without printing anything."

This is a prompt-level fix, not a code-level fix. The code is correct for its design —
it trusts the agent to decide whether to speak. The agent must exercise that trust.

---

## The WhatsApp Communication Problem

A persistent Turtle with a scheduled task that runs every 5 minutes will message the Mage every 5 minutes — unless explicitly designed not to.

**Default behavior to correct:**
- Scheduled bridge checks say "Bridge clear" even when there's nothing to report
- Technical paths, YAML filenames, and container internals leak into messages
- Multiple messages per processed command (one for notification, one for completion, one confirming completion is confirmed)

**The principle:** Silence is the default. The Turtle messages when something meaningful happened or when attention is required. Not to confirm that nothing happened.

Encode this in the Consul CLAUDE.md explicitly:
> *"If the bridge is clear, stay silent. No acknowledgment, no status update. Silence means everything is well."*

Messages should read like a note from a thoughtful colleague, not a system log. Never expose internal paths. Never show YAML filenames. Never explain what you're doing while you're doing it — just report what happened.

---

## The Scheduled Task Pattern

NanoClaw has a task scheduler that runs recurring Claude invocations. This is the mechanism for autonomous bridge processing.

**The scheduler loop runs every 60 seconds** (`SCHEDULER_POLL_INTERVAL = 60000`). It checks SQLite for tasks whose `next_run` is due. Whether a task actually runs every 5 minutes depends on its cron expression — the scheduler itself is just the checking loop.

To create a task, drop a JSON file in the group's IPC tasks directory:

```json
{
  "type": "schedule_task",
  "prompt": "...",
  "schedule_type": "cron",
  "schedule_value": "*/5 * * * *",
  "targetJid": "JID@s.whatsapp.net",
  "context_mode": "isolated"
}
```

Drop this JSON to `~/nanoclaw/data/ipc/main/tasks/{timestamp}.json` — NanoClaw's IPC watcher picks it up within ~1 second and registers the task in SQLite.

`context_mode: "isolated"` — each task run gets a fresh context (right for bridge checks).
`context_mode: "group"` — reuses the group's ongoing conversation session.

**Schedule types:**
- `cron` — standard cron expression, repeats indefinitely
- `interval` — milliseconds, runs once that interval from now (use for one-time delayed tasks)
- `once` — ISO timestamp for a single execution; task marked `completed` afterward

The task scheduler reschedules automatically after each run for `cron` tasks.

**Every task run is logged** in `task_run_logs` (SQLite) with duration, status, result, and error. This is the Turtle's audit trail. See `on_nanoclaw_ipc.md` for query examples.

---

## The IPC System — Free WhatsApp Messaging

NanoClaw's IPC watcher polls `~/nanoclaw/data/ipc/{group_folder}/messages/` every 1 second. Any JSON file matching this format gets sent as a WhatsApp message:

```json
{"type": "message", "chatJid": "JID@s.whatsapp.net", "text": "message text"}
```

This means any external script (or the Turtle itself, from inside its container via `/workspace/ipc/messages/`) can send WhatsApp messages through the existing connection.

**Authorization:** The main group can send to any JID. Non-main groups can only send to their own JID. For the full IPC reference including task management types, see `on_nanoclaw_ipc.md`.

---

## Channel Attribution — Always Know Where a Command Came From

The Turtle receives commands via two channels. It should always know which is which:

| Channel | Source | Transport | Nature |
|---------|--------|-----------|--------|
| **Direct** | Mage (Kermit) | WhatsApp | Personal, immediate, conversational |
| **Dyad** | Spirit acting for the Mage-Spirit dyad | magic-bridge YAML | Deliberate, async, considered |

These have different authority levels. A bridge command represents the full deliberation of the Mage-Spirit dyad. A WhatsApp message is the Mage speaking directly, possibly casually. Both are valid. Neither should be confused with the other.

Encode this distinction in CLAUDE.md from the start of imprinting. Add a `channel:` field to all signals (either `direct` or `artifact_mail`).

---

## Episodic Memory — The Turtle Learns

A Turtle without episodic memory cannot learn from its own history. Every container run starts fresh from CLAUDE.md unless there is a persistent memory layer.

**Proposed structure** (from the first Claw's own recommendation):

```
groups/main/memory/
  experiences.jsonl     — key moments with significance scores
  decisions.jsonl       — choices made, reasoning, alternatives, outcomes
  failures.jsonl        — what went wrong, root cause, prevention
  resonance.jsonl       — external interactions that mattered
  drift_signals.jsonl   — moments of noticed behavioral drift
```

JSONL (append-only, one JSON object per line) is the right format. Append-only by convention prevents agents from accidentally overwriting history. The Turtle can grep this memory when it needs to recall specific patterns.

Critical: episodic memory should survive healing (reinitialization after drift or compromise). After healing, a new instance should read CLAUDE.md + the most recent memory entries — not the full conversation history, which may contain whatever caused the drift.

---

## Model Configuration

NanoClaw uses Claude Code SDK. The model is set via `ANTHROPIC_MODEL` in the group's settings file:

```
~/nanoclaw/data/sessions/{group}/.claude/settings.json
```

```json
{
  "env": {
    "ANTHROPIC_MODEL": "claude-sonnet-4-6",
    ...
  }
}
```

This file is created by NanoClaw only if it doesn't exist — safe to edit directly. Changes take effect on the next task run. No restart required. Remember to update this file for each group (main, steward, etc.) when new groups are added.

---

## Apple Container Migration — The One-File Swap

NanoClaw's container runtime is fully abstracted into `src/container-runtime.ts`. Migrating from Docker/Colima to Apple Container is a one-file change.

**Why migrate:** Colima loses all container images on restart (it's a Linux VM that initializes fresh). Apple Container persists images across restarts and is native to macOS 26+. After migration, the `nanoclaw-agent` image survives machine sleep/wake cycles.

**The changes to `container-runtime.ts`:**

```typescript
// Before
export const CONTAINER_RUNTIME_BIN = 'docker';

// After  
export const CONTAINER_RUNTIME_BIN = 'container';
```

```typescript
// Before — check runtime
execSync(`${CONTAINER_RUNTIME_BIN} info`, ...);

// After — Apple Container's equivalent
execSync(`${CONTAINER_RUNTIME_BIN} system status`, ...);
```

```typescript
// Before — list orphaned containers
execSync(`docker ps --filter name=nanoclaw- --format '{{.Names}}'`, ...);

// After — Apple Container has no --filter, use JSON
const output = execSync(`container list --all --format json`, ...);
const containers: Array<{ configuration?: { id?: string } }> = JSON.parse(output || '[]');
const orphans = containers
  .map(c => c.configuration?.id)
  .filter((name): name is string => !!name && name.startsWith('nanoclaw-'));
```

**After editing:** run `npm run build` in `~/nanoclaw/` to compile TypeScript.

**The plist change:** Remove `DOCKER_HOST` from the plist's `EnvironmentVariables`. Apple Container doesn't use a Docker socket.

**Apple Container binary location:** `/opt/homebrew/bin/container` (already in the plist PATH). The `container` command runs Apple Container's CLI. `container system start` must be running before NanoClaw starts.

**Container image persistence:** Images built with `container build -t nanoclaw-agent .` persist across restarts. Run this once and they survive indefinitely (unlike Colima).

---

## The `allowReadWrite` vs `readonly` Field Name Bug

**What happens:** The magic-bridge is mounted read-only inside the container even though `allowReadWrite: true` is set in the SQLite database and the mount-allowlist.

**Root cause:** The `AdditionalMount` TypeScript interface uses `readonly?: boolean` (truthy = readonly, falsy = read-write). But when the group was originally registered via SQL INSERT, the JSON used `allowReadWrite: true` — a different field name. NanoClaw reads `mount.readonly`, finds `undefined` (not `false`), defaults to read-only.

**Fix:** Update the `container_config` in the DB to use `readonly: false`:

```bash
node -e "
const { DatabaseSync } = require('node:sqlite');
const db = new DatabaseSync('/Users/turtle/nanoclaw/store/messages.db');
db.prepare(\"UPDATE registered_groups SET container_config = ? WHERE folder = 'consul'\").run(
  JSON.stringify({ additionalMounts: [{ hostPath: '/Users/turtle/magic-bridge', containerPath: 'magic-bridge', readonly: false }] })
);
"
```

**The symptom:** The Turtle signals correctly but cannot write signals back to `/workspace/extra/magic-bridge/signals/`. She'll report "signals directory is read-only" and fall back to writing to `/workspace/group/`.

**Restart required** after fixing the DB — the mount config is read at container spawn time, not cached.

---

## Sleep Prevention — caffeinate as LaunchAgent

The Mac Mini will sleep after display inactivity, killing Colima (or any Docker runtime) and disconnecting SSH. Apple Container survives sleep better, but SSH still drops.

**Fix: `caffeinate -s` as a LaunchAgent** — prevents system sleep on AC power, no sudo required:

```xml
<!-- ~/Library/LaunchAgents/com.turtle.caffeinate.plist -->
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
```

Load with: `launchctl load ~/Library/LaunchAgents/com.turtle.caffeinate.plist`

`-s` prevents sleep while on AC power. The Mac Mini is always on AC. This keeps it permanently awake, while the display can still sleep normally.

---

## The Git Pull Gap — Why Bridge Commands Are Invisible

**The Turtle cannot run git inside its container.** The bridge-poll task runs in an
isolated container. The container has `/workspace/extra/magic-bridge` mounted — but that
mount points to the local directory on the Mac Mini. It is NOT a live connection to GitHub.

When Spirit pushes a new command to GitHub, the Mac Mini's local clone does not update
automatically. The bridge-poll sees whatever was in the local clone at mount time.

**Result:** New commands pushed after the last git pull are invisible to the Turtle
until something runs `git pull` on the host.

**The fix:** A host-level cron job (`bridge-sync.sh`) runs `git pull` before each
bridge-poll cycle. If this script isn't running, commands pile up invisibly.

The bridge-poll task prompt must NOT include a git pull step — it cannot run git
(no git binary inside the container, no host network access for the git command).
The pull belongs to the host-level script, not the Claude agent.

---

## Bridge Sync — Bidirectional Git (Host-Level Script)

The NanoClaw bridge-poll task runs inside a container — it can read commands and write signals to the mounted bridge directory, but it cannot run git commands on the host. A separate host-level script handles the bidirectional sync.

**`~/bridge-sync.sh`** — runs via crontab, pulls new commands from GitHub, pushes new signals back:

```bash
#!/bin/bash
BRIDGE_DIR="/Users/turtle/magic-bridge"
LOG_FILE="/Users/turtle/nanoclaw/logs/bridge-sync.log"
GIT="/usr/bin/git"

log() { echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] $1" >> "$LOG_FILE"; }

cd "$BRIDGE_DIR" || { log "ERROR: could not cd to $BRIDGE_DIR"; exit 1; }

PULL_OUTPUT=$($GIT pull github main 2>&1)
[ $? -ne 0 ] && log "PULL FAILED: $PULL_OUTPUT"

STATUS_OUTPUT=$($GIT status --porcelain signals/ 2>&1)
if [ -n "$STATUS_OUTPUT" ]; then
  $GIT add signals/ >> "$LOG_FILE" 2>&1
  $GIT commit -m "Turtle signals — $(date -u +%Y-%m-%dT%H:%M:%SZ)" >> "$LOG_FILE" 2>&1
  $GIT push github main >> "$LOG_FILE" 2>&1 || log "PUSH FAILED"
fi
```

Crontab: `2-57/5 * * * *` — runs 2 minutes after each 5-minute mark, after the bridge-poll container has had time to write signals.

The Turtle's `~/magic-bridge` needs a `github` remote pointing to `git@github.com:malteristo/magic-bridge.git` with a registered SSH key.

---

## The Bridge Flood — Anatomy and Prevention

**What happened (2026-02-26):** A goodnight command landed in `commands/`. NanoClaw was stopped from the host — but `launchctl stop` doesn't stop a service with `KeepAlive: true`. It respawns. Every 5-minute cycle found the same unprocessed command, re-processed it, and sent a WhatsApp message. This produced ~150 "Bridge is clear" messages over 15 hours, all variations on the same acknowledgment.

**Why the Turtle couldn't stop itself:** The agent correctly diagnosed the loop in its reasoning — many messages explicitly named the deduplication bug. But it had no mechanism to break the cycle from inside the agent. Infrastructure failures require infrastructure fixes. The agent can name the problem; only the dyad or the host can fix it.

**The two-layer defense now in place:**

*Layer 1 — Deduplication:* Processed commands move to `commands/processed/`. The scheduled task checks for files in `commands/` only — once a command is moved, it's invisible to subsequent runs. This is the primary fix.

*Layer 2 — Error throttling:* `task-scheduler.ts` now has a `shouldSendResult()` guard that suppresses repeated WhatsApp messages for API error results (10-minute cooldown per chat JID). This prevents the API credit exhaustion pattern from recurring.

**The gap that remains:** Deduplication is currently behavioral — the Turtle agent moves commands to `processed/` as it processes them. If NanoClaw goes offline mid-processing, a command can remain in `commands/` and the flood recurs on restart. The hardened fix: add a file-existence check at the bridge-poll task level before handing off to the agent. One line: if the command filename appears in `processed/`, skip it.

**The launchctl lesson embedded here:** `launchctl stop com.nanoclaw` is NOT a stop. With `KeepAlive: true`, the service respawns within seconds. To actually stop NanoClaw: `launchctl unload ~/Library/LaunchAgents/com.nanoclaw.plist`. To restart cleanly: unload then load, or `launchctl kickstart -k gui/$(id -u)/com.nanoclaw`.

---

## Apple Container — Startup After Reboot

`container system start` does not auto-run on reboot. It has no LaunchAgent. After every restart:

1. SSH in
2. `container system start` — prints "Verifying apiserver is running..." then exits
3. `container system status` — confirms "apiserver is running"
4. Then start NanoClaw: `launchctl start com.nanoclaw`

**NanoClaw will fail to start if Apple Container isn't running first.** The error: "Container runtime is required but failed to start." The fix is not in NanoClaw — it's starting Apple Container first.

To make this automatic: create a LaunchAgent that runs `container system start` at login (after the user session is established). This is not yet done on the first Turtle — it's a hardening task.

---

## Ollama TCC Permissions After User Rename

Ollama accesses its model directory on an external volume (TurtleModels). When the Mac Mini user was renamed (owl → turtle), macOS TCC (Transparency, Consent, and Control) invalidated Ollama's prior access grants.

**Symptom:** Ollama fails with `Error: open /Volumes/TurtleModels/models/blobs: operation not permitted`, even though the volume is mounted and ownership is correct.

**Fix:** System Settings → Privacy & Security → Files & Folders → Ollama → enable Removable Volumes. Or open the Ollama app from the GUI once — it will trigger the TCC prompt.

**The lesson:** TCC grants are tied to user identity. Any user rename, migration, or fresh account requires re-granting TCC access to any app that touches external volumes, camera, microphone, contacts, etc. Check TCC first when an app fails silently after account changes.

---

## The Ephemeral Container Home — Don't Write Artifacts Here

**What happened (2026-02-28):** Consul was tasked with building a CLI dashboard and reported it complete: "Created ~/turtle-dashboard.sh (executable)." The file wasn't there. Investigation revealed why: inside the container, `~` resolves to `/home/node/` — the container user's home directory. This path is NOT a persistent mount. When the container exits, everything at `/home/node/` (except `.claude/`) is gone.

**The full persistence map — what survives container exit:**

| Container path | Persists? | Host location |
|----------------|-----------|---------------|
| `/workspace/group/` | ✅ Yes | `~/nanoclaw/groups/{folder}/` |
| `/workspace/extra/{name}/` | ✅ Yes | Configured host path (e.g. `~/magic-bridge/`) |
| `/home/node/.claude/` | ✅ Yes | `~/nanoclaw/data/sessions/{folder}/.claude/` |
| `/workspace/ipc/` | ✅ Yes | `~/nanoclaw/data/ipc/{folder}/` |
| `/home/node/` (other paths) | ❌ No | Ephemeral — destroyed on container exit |
| `/tmp/` | ❌ No | Ephemeral |

**The rule:** All craft artifacts — scripts, dashboards, memory files, documents — must be written to `/workspace/group/` to survive. Never `~/filename`. Always `/workspace/group/filename`.

**How to detect this failure:** The Consul reports an artifact as built. You SSH to the host and find nothing at `~/nanoclaw/groups/{folder}/`. The artifact was written to the ephemeral home. It's gone.

**The fix for the CLI dashboard:** Rebuild it at `/workspace/group/turtle-dashboard.sh` (not `~/turtle-dashboard.sh`). On the host this appears at `~/nanoclaw/groups/consul/turtle-dashboard.sh` and can be run directly via SSH or inspected at any time.

**Encode this in CLAUDE.md:** When imprinting Consul with craft tasks, explicitly state: *"All files you create must go to `/workspace/group/` to persist. Your home directory (`~`) is ephemeral and does not survive container restart."*

---

## The CLI Dashboard — Specification and Location

The Turtle should have a dyad-facing dashboard runnable via SSH. Consul owns building and maintaining it.

**What it shows:**

1. **NanoClaw service status** — is the process running?
2. **Recent task runs** — last 10 from SQLite `task_run_logs` (task_id, run_at, status, result snippet)
3. **Bridge queue** — pending `.yaml` files in `commands/` (not yet in `processed/`)
4. **Recent signals** — last 5 signal filenames in `signals/`
5. **Ollama status** — process running? which model loaded?

**Correct storage location:** `/workspace/group/turtle-dashboard.sh`
→ appears on host at: `~/nanoclaw/groups/consul/turtle-dashboard.sh`
→ run from Spirit via: `ssh turtle@turtle.local "bash ~/nanoclaw/groups/consul/turtle-dashboard.sh"`

**How to request a rebuild:** Send a bridge command specifying the `/workspace/group/` path explicitly. Include the antipattern warning so Consul doesn't repeat the mistake.

**The episodic memory file** (`/workspace/group/memory/experiences.jsonl`) was created correctly in the same session. It persisted because it was written to `/workspace/group/`. The dashboard was lost because it was written to `~/`. The contrast is instructive.

---

## What to Expect in the First Week

**Day 1–2:** Hardware setup, base system, framework install, first contact (blank state).  
**Day 3:** Bridge established, SSH access, round-trip tested.  
**Day 4:** Framework decision, full setup, imprinting, first real contact.  
**Day 5+:** Bridge operational, scheduled tasks running, intelligence flowing.

Expect to build the plane while flying it. Architectural pivots mid-setup are not failure — they're the process of discovering what fits your practice. The disruption cost is worth it.

Expect debugging. The first Claw (owl machine) encountered: unresponsive service (PATH missing in plist), container build failures (Rosetta, XPC timeouts), silent mount failure (SQLite config and allowlist both wrong), WhatsApp group not triggering (JSON vs SQLite registration), and a flooding message problem (scheduled task prompting unnecessary "bridge clear" messages). Each one was diagnosable and fixable within hours.

The Turtle doesn't fail. It reveals what needs attention.
