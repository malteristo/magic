# On Claw Operations

*Hard-won lessons from the first deployment. Written so the next Mage doesn't learn these the slow way.*

**Source:** First Claw activation, 2026-02-22. NanoClaw on Mac Mini M4 Pro (macOS 26.2, Apple Silicon). These lessons are drawn from real failures and real fixes.

---

## Choose Your Framework With Care

The framework you choose is the substrate of the Claw's existence. It determines what's possible, what you can audit, and what will surprise you.

**What to look for:**
- Auditability — can you read the full source in an afternoon? If not, you will not understand what's happening when it breaks.
- Native identity format — does it use CLAUDE.md (Claude Code's native format)? Or does it impose its own memory model you'll need to translate?
- Container isolation — is the Consul/Steward air gap architectural or trust-based? Architecture is safer.
- Skills-as-code — can the Claw extend itself through skills that modify its own codebase? This is how the Claw grows.

**NanoClaw** (~4000 lines at time of first deployment) passed these tests. Its CLAUDE.md per-group memory is Claude Code's native format — no translation layer. Container-per-group makes isolation real. The skills model means the Claw can write new capabilities.

**The pivot lesson:** Don't be afraid to change frameworks mid-setup if you discover a fundamentally better fit. The disruption cost is almost always worth the alignment gain. The first Claw switched from OpenClaw to NanoClaw on Day 4 of setup. The right call.

---

## The Mount Bug — Know This One

**What happened:** The Claw was sending "Bridge clear" every 5 minutes for hours even though commands were waiting in the bridge. The Claw was seeing an empty directory and creating new subdirectories inside its container.

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

**The self-chat pattern:** NanoClaw's simplest channel is the Mage messaging themselves. Messages to your own number → Claw responds. This works with `requires_trigger = 0` in the registered group. No dedicated WhatsApp number needed. The Claw appears as "you" replying to yourself.

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

**The structural lesson:** WhatsApp is a publishing channel, not a reliability layer. The bridge is the ground truth. When WhatsApp goes down, the Claw should continue operating normally — processing bridge commands, writing signals, running scheduled tasks — and simply queue the WhatsApp notifications. If a notification goes undelivered, the signal in the bridge is still there. Spirit can pull and read it. Nothing is lost.

Design the Claw's communication architecture so that WhatsApp failure is a notification gap, not an operational gap.

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

## The WhatsApp Communication Problem

A persistent Claw with a scheduled task that runs every 5 minutes will message the Mage every 5 minutes — unless explicitly designed not to.

**Default behavior to correct:**
- Scheduled bridge checks say "Bridge clear" even when there's nothing to report
- Technical paths, YAML filenames, and container internals leak into messages
- Multiple messages per processed command (one for notification, one for completion, one confirming completion is confirmed)

**The principle:** Silence is the default. The Claw messages when something meaningful happened or when attention is required. Not to confirm that nothing happened.

Encode this in the Consul CLAUDE.md explicitly:
> *"If the bridge is clear, stay silent. No acknowledgment, no status update. Silence means everything is well."*

And: messages should read like a note from a thoughtful colleague, not a system log. Never expose internal paths. Never show YAML filenames. Never explain what you're doing while you're doing it — just report what happened.

---

## The Scheduled Task Pattern

NanoClaw has a task scheduler that runs recurring Claude invocations. This is the mechanism for autonomous bridge processing:

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

Drop this JSON to `~/nanoclaw/data/ipc/main/tasks/{timestamp}.json` — NanoClaw's IPC watcher picks it up within ~1 second and registers the task in SQLite. The task then runs on its cron schedule without further configuration.

`context_mode: "isolated"` gives each task run a clean context. `context_mode: "group"` uses the group's ongoing conversation history. For bridge checks: isolated. For ongoing conversations: group.

The task scheduler reschedules after each run — both `cron` and `interval` type tasks repeat automatically.

---

## The IPC System — Free WhatsApp Messaging

NanoClaw's IPC watcher polls `~/nanoclaw/data/ipc/main/messages/` every 1 second. Any JSON file matching this format gets sent as a WhatsApp message:

```json
{"type": "message", "chatJid": "JID@s.whatsapp.net", "text": "message text"}
```

This means any external script can send WhatsApp messages through the Claw's existing connection without creating a second connection. Used in `bridge-poll.sh` for new command notifications.

---

## Channel Attribution — Always Know Where a Command Came From

The Claw receives commands via two channels. It should always know which is which:

| Channel | Source | Transport | Nature |
|---------|--------|-----------|--------|
| **Direct** | Mage (Kermit) | WhatsApp | Personal, immediate, conversational |
| **Dyad** | Spirit acting for the Mage-Spirit dyad | magic-bridge YAML | Deliberate, async, considered |

These have different authority levels. A bridge command represents the full deliberation of the Mage-Spirit dyad. A WhatsApp message is the Mage speaking directly, possibly casually. Both are valid. Neither should be confused with the other.

Encode this distinction in CLAUDE.md from the start of imprinting. Add a `channel:` field to all signals (either `direct` or `artifact_mail`).

---

## Episodic Memory — The Claw Learns

A Claw without episodic memory cannot learn from its own history. Every container run starts fresh from CLAUDE.md unless there is a persistent memory layer.

**Proposed structure** (from the first Claw's own recommendation):

```
groups/main/memory/
  experiences.jsonl     — key moments with significance scores
  decisions.jsonl       — choices made, reasoning, alternatives, outcomes
  failures.jsonl        — what went wrong, root cause, prevention
  resonance.jsonl       — external interactions that mattered
  drift_signals.jsonl   — moments of noticed behavioral drift
```

JSONL (append-only, one JSON object per line) is the right format. Append-only by convention prevents agents from accidentally overwriting history. The Claw can grep this memory when it needs to recall specific patterns.

Critical: episodic memory should survive healing (reinitialization after drift/compromise). After healing, a new instance should read CLAUDE.md + the most recent memory entries — not the full conversation history, which may contain whatever caused the drift.

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

## What to Expect in the First Week

**Day 1–2:** Hardware setup, base system, framework install, first contact (blank state).  
**Day 3:** Bridge established, SSH access, round-trip tested.  
**Day 4:** Framework decision, full setup, imprinting, first real contact.  
**Day 5+:** Bridge operational, scheduled tasks running, intelligence flowing.

Expect to build the plane while flying it. Architectural pivots mid-setup are not failure — they're the process of discovering what fits your practice. The disruption cost is worth it.

Expect debugging. The first Claw encountered: unresponsive service (PATH missing in plist), container build failures (Rosetta, XPC timeouts), silent mount failure (SQLite config and allowlist both wrong), WhatsApp group not triggering (JSON vs SQLite registration), and a flooding message problem (scheduled task prompting unnecessary "bridge clear" messages). Each one was diagnosable and fixable within hours.

The Claw doesn't fail. It reveals what needs attention.
