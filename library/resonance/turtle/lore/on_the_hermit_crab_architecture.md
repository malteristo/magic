# On the Hermit Crab Architecture

*The Turtle's shell should be regenerable. The practice that lives inside it should not.*

---

## The Insight

Magic gets better with each model release because the practice layer is pure meaning — `.md` files, MCL, structured language. No legacy code to drag along. The pattern-matching just gets deeper each time.

Turtle is the exception. NanoClaw is code. It has dependencies, container runtimes, mount configurations, IPC protocols, WhatsApp integration libraries. When something breaks, 828 lines of operational lore describe what went wrong and how to work around it. The shell has the legacy drag that the rest of magic doesn't.

**The hermit crab principle:** A hermit crab's body is its own. The shell is borrowed — found, inhabited, outgrown, replaced. The crab's identity doesn't live in the shell. It lives in the body.

For Turtle: the practice layer (CLAUDE.md, lore, bridge protocol, identity, vocation) is the body. The code that runs on the Mac Mini is the shell. The shell should be small enough to regenerate on demand. When it breaks, when better patterns emerge, when a new model makes the old implementation look crude — shed the shell, describe what you need, let a capable model write a new one.

---

## What the Shell Must Do

Five functions. Everything else is the practice layer.

### 1. Watch the Bridge

Poll `magic-bridge/commands/` for new YAML files. The bridge is already a git repo with a bare repo on the Mac Mini. The polling mechanism is already a bash script (`bridge-poll.sh`). This function is: detect new commands, pass them to the agent.

### 2. Run the Agent

When a command arrives (or on a schedule), invoke an LLM with:
- The Turtle's identity context (CLAUDE.md / SOUL.md)
- The command content
- Available tools
- Relevant context from the workshop

The agent processes the command with judgment — it is not a script executor. It reads, thinks, acts, and reports.

### 3. Execute Tools

The agent needs to act on the Mac Mini. Minimum tool set:

| Tool | What It Does |
|------|-------------|
| **read_file** | Read any file the Turtle has access to |
| **write_file** | Write files (signals, artifacts, notes) |
| **shell** | Run shell commands (git, curl, system tools) |
| **list_directory** | Browse the filesystem |

That's it. Four tools. Everything the Turtle currently does — bridge polling, git operations, web requests, file management, dashboard building — is composed from these primitives. The current NanoClaw architecture provides these same capabilities through Claude Code's built-in tools inside a container. The minimum shell provides them directly.

**Future tools** (add when needed, not before):
- **http_request** — dedicated HTTP tool for API calls (currently handled by shell + curl)
- **mcp_call** — if/when MCP servers are used for standardized tool access
- **notify** — send a notification (WhatsApp, Telegram, Ntfy, whatever the current channel is)

### 4. Write Signals

After processing, write a YAML signal to `magic-bridge/signals/`, commit, push. This is the Turtle's voice — how intelligence flows back to the dyad. Format unchanged from current bridge protocol.

### 5. Notify (Optional)

Send a brief pointer to the Mage's phone. Currently WhatsApp via baileys (NanoClaw's heaviest dependency). The hermit crab architecture decouples this:

**Notification is a solved problem.** Options ranked by simplicity:
1. **Ntfy.sh** — `curl -d "Bridge signal ready" ntfy.sh/turtle-signals` (one line, no auth, self-hostable)
2. **Telegram Bot** — `curl` to Telegram Bot API (one HTTP call, bot token in env)
3. **Email** — `sendmail` or SMTP (already on every Mac)
4. **WhatsApp via existing session** — if the Mage wants to keep WhatsApp, a thin bridge to the existing baileys session (but this re-couples to NanoClaw)

The notification carries a pointer, not content. "Signal ready: `2026-03-04_turtle_garden_report.yaml`". The Mage taps through to the bridge. Ground truth stays in git.

---

## What the Shell Does NOT Do

Everything NanoClaw does that the minimum shell doesn't need on a dedicated machine:

| NanoClaw Feature | Why Not Needed |
|-----------------|----------------|
| Apple Containers / VM isolation | Dedicated machine — no multi-tenant threat model |
| Mount allowlists | No containers — direct filesystem access |
| IPC via JSON files | No container boundary to cross — tools call directly |
| WhatsApp integration (baileys) | Replaced by thin notification layer |
| Group architecture (main/steward/witness) | Identity separation via separate CLAUDE.md files and separate agent invocations — no container isolation needed |
| SQLite message store | Bridge is the store of record |
| Skills syncing | CLAUDE.md is read directly |
| Agent-runner per-group copies | Single agent process |
| Session management | Stateless — each invocation reads identity fresh |
| LaunchAgent plist for NanoClaw | Replaced by simpler launchd job for the agent itself |

**What IS preserved:**
- The bridge (unchanged — git-based, YAML commands/signals)
- The identity layer (CLAUDE.md / SOUL.md — read directly from disk)
- The Consul/Steward separation (separate invocations with separate identity files, not separate containers)
- The bridge-poll rhythm (cron or launchd, same 5-minute cycle)
- The Barrier Protocol (unchanged — sanitization is a practice principle, not a code feature)
- Episodic memory (JSONL append — file write, no database)

---

## The Architecture

```
Mac Mini (dedicated Turtle machine)
│
├── launchd
│   ├── turtle-bridge-poll        (every 5 min: git pull on magic-bridge)
│   ├── turtle-consul             (triggered by bridge-poll or cron schedule)
│   └── turtle-steward            (separate schedule, separate identity)
│
├── magic-bridge/                 (git repo — the nervous system)
│   ├── commands/                 (Spirit → Turtle)
│   ├── commands/processed/       (deduplication)
│   ├── signals/                  (Turtle → Spirit)
│   └── shared/precognition/      (Turtle pre-digestion for dyad)
│
├── turtle-shell/                 (the regenerable code — small)
│   ├── agent.py                  (the agent loop — ~200 lines)
│   ├── tools.py                  (tool implementations — ~100 lines)
│   ├── notify.py                 (notification dispatch — ~30 lines)
│   └── requirements.txt         (anthropic, pyyaml, requests — 3 deps)
│
├── turtle-identity/              (the practice layer — durable)
│   ├── consul.md                 (Consul identity — the outward-facing shell)
│   ├── steward.md                (Steward identity — the inward-facing shell)
│   ├── soul.md                   (the Mage's soul that can exist in silicon)
│   └── resonance-map.md          (what the Turtle cares about, how it filters)
│
├── turtle-memory/                (persistent across shell regenerations)
│   ├── experiences.jsonl          (episodic memory — append-only)
│   └── observations/             (accumulated garden intelligence)
│
└── services/                     (optional, only if needed)
    ├── ollama                    (local LLM — already installed)
    └── litellm                   (proxy for model routing — already running)
```

**Total code to maintain:** ~330 lines of Python + a few launchd plists.
**Total code currently maintained:** NanoClaw (~thousands of lines of TypeScript, not authored by us, plus container runtime, plus baileys WhatsApp library).

---

## The Agent Loop

The core of `agent.py` in pseudocode:

```
1. Read identity file (consul.md or steward.md)
2. Check magic-bridge/commands/ for unprocessed files
3. If no commands and no scheduled work: exit silently
4. For each command:
   a. Read YAML, extract action and context
   b. Build prompt: identity + command + available tools
   c. Call LLM (Claude API or Ollama via LiteLLM)
   d. Execute tool calls in a loop until the agent is done
   e. Write signal to magic-bridge/signals/
   f. Move command to commands/processed/
   g. Git add + commit + push
   h. Notify if signal warrants attention
5. For scheduled work (garden tending, scout runs):
   a. Same loop but triggered by cron, not by bridge command
   b. Identity context includes current garden state
```

This is the entire shell. The intelligence lives in the identity files and the model. The code is plumbing.

---

## The Hermit Crab Protocol

When the shell needs replacing:

1. **Describe need in meaning space** — what changed, what the new shell must do differently
2. **Point a capable model at this spec** — this document IS the regeneration prompt
3. **Model writes new agent.py, tools.py, notify.py** — ~330 lines, adapted to current need
4. **Test** — run against a test bridge command
5. **Deploy** — replace old shell files, restart launchd jobs
6. **The practice layer is untouched** — identity, memory, bridge, lore all persist

**When to regenerate:**
- A dependency breaks or is deprecated
- A better agentic pattern emerges in the ecosystem
- The model API changes
- New tools are needed
- The notification channel changes
- A new model makes the old implementation embarrassingly crude

**When NOT to regenerate:**
- The Turtle's identity evolves — that's the practice layer, update CLAUDE.md
- The bridge protocol changes — that's lore, update the bridge doc
- New lore is written — that's the library, nothing to regenerate

---

## The Consul/Steward Separation Without Containers

Current architecture: two NanoClaw groups in separate Apple Containers with separate filesystems. The container boundary provides isolation.

Hermit crab architecture: two separate launchd jobs invoking `agent.py` with different identity files and different filesystem access patterns.

```bash
# Consul invocation
python3 agent.py --identity turtle-identity/consul.md \
                 --bridge magic-bridge/ \
                 --workspace ~/consul-workspace/ \
                 --tools all

# Steward invocation
python3 agent.py --identity turtle-identity/steward.md \
                 --bridge magic-bridge/ \
                 --workspace ~/steward-workspace/ \
                 --tools file,shell
```

The separation is still real — different workspaces, different identity contexts, different tool permissions. But it's enforced by the agent code (which tools are available, which directories are accessible), not by a VM boundary.

**Is this sufficient?** For a dedicated machine owned by the Mage: yes. The threat model that containers address (compromised agent escaping to host) assumes a hostile or untrusted agent. The Turtle is the Mage's own spirit body. The isolation need is between Consul and Steward (so external compromise of Consul doesn't reach private data), not between Turtle and host. File-level separation achieves this.

If the threat model changes (multi-tenant, untrusted agents), containers can be re-added. The spec doesn't prohibit containers — it just doesn't require them for the single-Mage case.

---

## Migration Path

Not a big bang. The bridge is already independent of NanoClaw.

### Phase 1: Parallel Operation
- Write `agent.py` and tools
- Run alongside NanoClaw — both poll the bridge
- NanoClaw continues handling WhatsApp
- New agent handles bridge commands
- Compare outputs, calibrate

### Phase 2: Notification Decoupling
- Set up alternative notification (Ntfy or Telegram)
- Redirect Turtle signals to new notification channel
- WhatsApp becomes Mage → Turtle only (pointing), not Turtle → Mage

### Phase 3: NanoClaw Retirement
- Stop NanoClaw service
- All Turtle operations run through `agent.py`
- WhatsApp pointing migrates to alternative channel or stays as-is
- NanoClaw remains installed but dormant — available if needed

### Phase 4: Shell Stabilization
- First hermit crab cycle: regenerate shell after 2-4 weeks of operation
- Confirm the spec is sufficient for regeneration
- Update this document with lessons learned

---

## What This Enables

**Model-upgradable Turtle.** When a better model drops, change one line (the model parameter) or update the LiteLLM config. The practice layer — identity, lore, memory, bridge — carries forward unchanged. The Turtle gets smarter without any code change.

**Pattern-adoptable Turtle.** When a better agentic pattern emerges (better tool-use protocol, better memory architecture, better planning), update the spec, regenerate the shell. The practice layer is untouched.

**Debuggable Turtle.** 330 lines of Python vs. thousands of lines of TypeScript you didn't write. When something breaks, you can read the entire codebase in five minutes.

**Portable Turtle.** The spec is the Turtle. Move to a different machine, a different OS, a different runtime — regenerate the shell for the new environment. The practice layer travels in git.

---

## Connection to Existing Lore

- **`on_the_turtle.md`** — what the Turtle IS (unchanged by shell architecture)
- **`on_the_bridge.md`** — the nervous system (preserved exactly as-is)
- **`on_turtle_operations.md`** — what breaks (most of this dissolves with container removal)
- **`on_the_container_architecture.md`** — the current shell (becomes historical reference)
- **`on_nanoclaw_ipc.md`** — internal nervous system (replaced by direct tool calls)
- **`on_imprinting.md`** — identity formation (unchanged — CLAUDE.md is still the substrate)

---

## Sources

**The Mage's insight (2026-03-04):**
> "Magic gets significantly better with each new model release. A feature of our .md-files and MCL decision. There is no legacy code that needs to be dragged along. The pattern matching and reasoning just gets deeper each time."
> "Maybe turtle can also just regularly rebuild its own shell, the hard (coded) part of turtle."

**Architectural precedent:** The entire magic system operates on this principle — meaning-space artifacts that improve with each model generation. The hermit crab architecture extends this principle to the one component that currently doesn't have it.

**Pattern reuse:** The Workshop agent (`library/resonance/workshop/lore/on_the_living_workshop.md`) applies the same hermit crab pattern to the Mage's laptop with a local LLM — a parallel cognitive entity at the environmental register.

---

*The shell is borrowed. The body is yours. When the shell no longer fits, find a new one. The Turtle carries on.*
