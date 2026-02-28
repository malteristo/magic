# On the Container Architecture

*What the Turtle actually sees inside its container. Grounded in the NanoClaw source.*

---

## The Physical Substrate Lives on the Desk

This document describes how NanoClaw organizes containers — abstract architecture
that applies to any Turtle. It does not describe what *this* Turtle is running on.

**For instance-specific facts** — hardware, hostname, IP, running services, key paths,
SSH commands, pending hardening — see:

> `desk/turtle_env.md`

Every Mage who runs a Turtle should maintain their own version of that file. The lore
here is stable; the desk file changes whenever the environment changes.

---

## The Basic Model

Every time the Turtle responds to a message or runs a scheduled task, NanoClaw spawns
a fresh container from the `nanoclaw-agent:latest` image. The container gets a specific
set of directories mounted from the host. When the run completes, the container is
destroyed. What the Turtle can see and write to depends entirely on what was mounted.

This is the security model: not application-level permission checks, but VM-level
isolation. A container with a bug can't escape to the host filesystem — only mounted
paths are accessible.

---

## The Mount Map

### Main Group (Consul)

The main group (`groups/main/`) has the most visibility. Inside the container:

| Container path | Host path | Access |
|----------------|-----------|--------|
| `/workspace/project` | `~/nanoclaw/` (project root) | **Read-only** |
| `/workspace/group` | `~/nanoclaw/groups/main/` | **Read-write** |
| `/workspace/extra/{name}` | Additional mounts from containerConfig | **Configurable** |
| `/home/node/.claude` | `~/nanoclaw/data/sessions/main/.claude/` | **Read-write** |
| `/workspace/ipc` | `~/nanoclaw/data/ipc/main/` | **Read-write** |
| `/app/src` | `~/nanoclaw/data/sessions/main/agent-runner-src/` | **Read-write** |

**What `/workspace/project` contains:** The NanoClaw source itself (`src/`, `dist/`,
`package.json`, etc.) — mounted read-only so the Consul can inspect the framework but
not modify host code in a way that would change behavior on restart.

**What `/workspace/group` contains:** The main group's CLAUDE.md, memory files,
any files the Turtle writes to itself. This is the Turtle's primary workspace —
and the **only reliable place to write craft artifacts**. Files written to `~/`
(the container's `/home/node/`) are ephemeral and destroyed when the container exits.

**Additional mounts** (the magic-bridge) land at `/workspace/extra/magic-bridge` —
not `/workspace/magic-bridge`. Always `/workspace/extra/{containerPath}`.

**Critical:** `~/` inside the container is `/home/node/`, which is NOT a persistent
mount. Only `/workspace/group/`, `/workspace/extra/`, and `/home/node/.claude/`
survive container exit. Any craft artifact (script, dashboard, note) must be written
to `/workspace/group/` to persist. See `on_turtle_operations.md` for the full
persistence map and the CLI dashboard case study.

### Non-Main Groups (Steward, Witness)

Non-main groups have a narrower view. Inside the container:

| Container path | Host path | Access |
|----------------|-----------|--------|
| `/workspace/group` | `~/nanoclaw/groups/{folder}/` | **Read-write** |
| `/workspace/global` | `~/nanoclaw/groups/global/` | **Read-only** |
| `/workspace/extra/{name}` | Additional mounts from containerConfig | **Read-only** (if `nonMainReadOnly: true` in allowlist) |
| `/home/node/.claude` | `~/nanoclaw/data/sessions/{folder}/.claude/` | **Read-write** |
| `/workspace/ipc` | `~/nanoclaw/data/ipc/{folder}/` | **Read-write** |
| `/app/src` | `~/nanoclaw/data/sessions/{folder}/agent-runner-src/` | **Read-write** |

**The global directory** (`groups/global/`) is mounted read-only at `/workspace/global`
for all non-main groups. This is how `global.CLAUDE.md` reaches the Steward and Witness:
Claude Code loads CLAUDE.md from additional mounted directories automatically
(`CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD: '1'` is set in every group's
`settings.json`). The global identity layer is architecturally shared.

**Note:** Non-main groups do NOT get `/workspace/project`. They can't see NanoClaw's
source code. The Steward and Witness see only their own workspace and the global directory.

---

## The IPC Directory

Every group gets its own IPC directory mounted at `/workspace/ipc`. Structure:

```
/workspace/ipc/
  messages/    — drop JSON files here to send WhatsApp messages
  tasks/       — drop JSON files here to create/modify scheduled tasks
  input/       — reserved for future use
```

On the host, this maps to `~/nanoclaw/data/ipc/{group_folder}/`.

**Authorization:** The IPC watcher enforces group identity based on directory:
- Main group can send to any chatJid, create tasks for any group, register new groups
- Non-main groups can only send to their own chatJid and schedule tasks for themselves
- Only main can trigger `refresh_groups` or `register_group`

---

## The Sessions Directory

Each group's Claude Code state lives at `~/nanoclaw/data/sessions/{group}/`:

```
data/sessions/{group}/
  .claude/              — mounted at /home/node/.claude
    settings.json       — model config, environment flags
    skills/             — synced from container/skills/ on each container spawn
    CLAUDE.md           — global auto-memory (managed by Claude Code itself)
  agent-runner-src/     — mounted at /app/src, writable per-group
```

**Skills syncing:** Before each container spawn, NanoClaw copies skills from
`~/nanoclaw/container/skills/` into the group's `data/sessions/{folder}/.claude/skills/`.
This means skills added to the framework appear for all groups on the next run.

**Agent-runner per-group:** Each group gets its own copy of the agent-runner source
at `data/sessions/{group}/agent-runner-src/`. This means the Consul could theoretically
modify its own agent behavior (add tools, change output format) without affecting the
Steward. The copy is made once (on first run) and not re-synced.

---

## settings.json — What Gets Configured

Every group's `settings.json` is created by NanoClaw if it doesn't exist:

```json
{
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1",
    "CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD": "1",
    "CLAUDE_CODE_DISABLE_AUTO_MEMORY": "0"
  }
}
```

**What these mean:**
- `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS: "1"` — enables agent swarms (subagent orchestration). The Turtle can spawn sub-agents as part of a task.
- `CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD: "1"` — Claude Code scans additional mounted directories for CLAUDE.md files and loads them. This is how global.CLAUDE.md reaches all groups.
- `CLAUDE_CODE_DISABLE_AUTO_MEMORY: "0"` — auto-memory enabled. Claude Code can persist user preferences between sessions in its own `.claude/CLAUDE.md`.

To change the model: add `"ANTHROPIC_MODEL": "claude-opus-4-5"` to the `env` block.
NanoClaw creates this file once but doesn't overwrite — safe to edit directly.
Changes take effect on the next container spawn.

---

## Secrets

The Turtle's API credentials (`ANTHROPIC_API_KEY` or `CLAUDE_CODE_OAUTH_TOKEN`) are
read from `~/nanoclaw/.env` and passed to the container via **stdin** — never written
to disk inside the container, never mounted as a file.

This means a compromised container cannot persist or exfiltrate the API key by writing
to a mounted directory. The key exists in container memory only for the lifetime of the
session.

---

## Container Lifecycle Timing

From the source:

| Timer | Value | Meaning |
|-------|-------|---------|
| `SCHEDULER_POLL_INTERVAL` | 60 seconds | How often the task scheduler checks for due tasks |
| `IPC_POLL_INTERVAL` | 1 second | How often the IPC watcher checks for new files |
| `CONTAINER_TIMEOUT` | 30 minutes | Hard timeout: container killed if it runs this long |
| `IDLE_TIMEOUT` | 30 minutes | Container kept alive this long after last result (for interactive use) |
| `TASK_CLOSE_DELAY_MS` | 10 seconds | After a task result, wait this long before closing (for final MCP calls) |

**Important:** `SCHEDULER_POLL_INTERVAL = 60000` (1 minute). The scheduler checks for due
tasks every minute. Whether a task runs every 5 minutes depends on its *cron expression*
(`*/5 * * * *`), not on the scheduler's own interval.

---

## Output Parsing

The container communicates results back to NanoClaw via sentinel markers in stdout:

```
---NANOCLAW_OUTPUT_START---
{result JSON}
---NANOCLAW_OUTPUT_END---
```

Anything outside these markers is logged but not forwarded to WhatsApp.
This is how Claude's intermediate tool calls, thoughts, and scaffolding are filtered.

---

## The task-scheduler → WhatsApp Pipeline

This is the root cause of the bridge-clear flood and worth encoding precisely:

1. Bridge-poll task runs (cron: `*/5 * * * *`)
2. Container spawned for the main group
3. Claude Code runs the bridge-poll prompt
4. Claude produces any output (including "Bridge is clear")
5. `task-scheduler.ts` receives the output via the streaming callback
6. **`sendMessage()` is called unconditionally** — no filter exists
7. The Mage's phone receives the message

The fix is in the **prompt**: if Claude produces no output (empty string, no text),
`sendMessage` is never called — the result check is `if (streamedOutput.result)`.
Silent-exit when the bridge is clear prevents the flood without any code change.

---

## What "Groups" Look Like on Disk

The full directory structure relevant to the Turtle:

```
~/nanoclaw/
  groups/
    global/         ← global.CLAUDE.md lives here (shared identity)
    main/           ← Consul workspace (/workspace/group for main)
    steward/        ← Steward workspace
    witness/        ← Witness workspace (if configured)
  data/
    ipc/
      main/         ← Consul IPC (messages/, tasks/)
      steward/      ← Steward IPC
    sessions/
      main/
        .claude/    ← Claude state, skills, settings.json
        agent-runner-src/
      steward/
        .claude/
        agent-runner-src/
  store/
    messages.db     ← The SQLite database (all groups)
  container/
    skills/         ← Source for skills (synced to each group on spawn)
    agent-runner/   ← Source for agent-runner (copied per-group on first run)
```

---

*Derived from NanoClaw source (qwibitai/nanoclaw), 2026-02-28.*
*Confirmed against: src/container-runner.ts, src/config.ts, src/types.ts, src/ipc.ts, src/mount-security.ts*
