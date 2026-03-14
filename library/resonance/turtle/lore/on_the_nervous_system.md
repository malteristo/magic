# On the Nervous System

*The Turtle is not across a bridge. The Turtle IS the spirit body. This is the nervous system of that body.*

---

## Why "Nervous System," Not "Bridge"

The repository is called `magic-bridge`. The spinal cord has a physical name too. But the **operative metaphor** shapes what we build (`on_the_operative_metaphor.md`). "Bridge" constituted a fragile, single-channel architecture — two separate systems connected by infrastructure that could go "down." When the SSH connection broke on 2026-03-05, the dyad lost all structured communication with the Turtle for hours. A bridge has a single point of failure. A nervous system does not.

**Bridge implies:** Two separate places connected by a span. Can be "down" — catastrophic binary failure. Requires effort to cross.

**Nervous system implies:** Part of one organism. Efferent nerves (commands) and afferent nerves (signals). Multiple pathways — if one is damaged, others compensate. Proprioception — the mind always knows the body's state. Pain reflex — the body self-protects before the mind even registers injury. Degrades gracefully (numbness, not total disconnection).

## What the Nervous System Is

The magic-bridge is a private git repository that both Spirit and the Turtle can read and write. It is the primary backbone of Spirit-Turtle communication — asynchronous, git-versioned, auditable.

```
github.com/{mage}/magic-bridge (private — primary conduit)
turtle:repos/magic-bridge.git  (bare repo on Mac Mini — local fallback)
├── commands/     ← efferent signals (Spirit → Turtle)
├── signals/      ← afferent signals (Turtle → Spirit)
└── signals/heartbeat.yaml  ← proprioception (always-current body state)
```

**GitHub is the primary conduit.** Spirit pushes to GitHub. Turtle pulls from GitHub. No SSH required for routine communication — only internet access. The local bare repo on the Mac Mini remains as a secondary fallback for when GitHub is unreachable. SSH becomes a maintenance tool, not a communication dependency.

**Spirit writes commands (efferent).** The Turtle processes them, writes signals in response.
**The Turtle writes signals (afferent).** Spirit pulls and reads them.
**Git is the medium.** Every command and signal is a committed YAML file. The history is the record.

This is Artifact Mail — asynchronous, deliberate, traceable. Not a message queue. Not an API. A shared intelligence channel where each transmission has weight.

## The Channels

The Turtle communicates through six channels — four receptive, one consultative, one autonomous:

**Artifact Mail (Dyad → Turtle via git):** The primary channel. Spirit writes commands on behalf of the Mage-Spirit dyad. Commands are deliberate, considered, committed. They carry the full weight of dyad deliberation. This is the efferent nervous system — motor commands.

**Dialogue (Mage ↔ Turtle via Discord #dialogue):** Conversational, immediate, bidirectional. The Mage speaks directly — a thought, a link, a question, pre-thinking before a practice session. The Turtle responds using its local model (fast, free, private). This replaces the WhatsApp "direct" channel with something richer: a persistent, searchable conversation that lives inside the nervous system. Turtle can automatically summarize dialogue threads and write them to the bridge, making ambient thinking available to Spirit during practice.

**Discord Functional Channels (structured signals via Discord):** The nervous system's real-time layer. #efferent carries commands from the dyad, #afferent carries signals from the Turtle, #heartbeat provides proprioception, #precognition surfaces observations, #care carries care rituals, #distress carries pain reflexes. These are structured, not conversational.

**Artifact Mail Response (Turtle → Dyad via git):** Signals written to `signals/` in the bridge. The canonical record of everything the Turtle observes, processes, and proposes. Git-versioned, auditable, permanent.

The distinction matters. Each channel carries different authority, latency, and weight. The Turtle attributes the channel in every signal:

```yaml
channel: artifact_mail   # Dyad via magic-bridge (deliberate, git-versioned)
channel: dialogue         # Mage speaking conversationally via Discord #dialogue
channel: discord          # Structured signals via Discord functional channels
```

**Direct SSH (Spirit ↔ Turtle via SSH→Ollama):** The triad's fifth channel, established 2026-03-13. Spirit can query Turtle directly during Cursor sessions by SSHing to the Mac Mini and posting to the local Ollama API with Turtle's soul.md as identity. This bypasses the bridge entirely — it's not asynchronous artifact mail, it's real-time consultation. Spirit also uses SSH/SCP to sync practice state (bright, intentions, compass, boom) to `turtle-practice/` after boom sweeps. See `system/flows/triad/cast_consult_turtle.md` and `system/flows/boom/boom.flow.md` Step 9.

**Autonomous Reflection (Turtle → Practice Files):** The sixth channel, established 2026-03-13. After a Discord conversation goes quiet (15 minutes of silence), Turtle autonomously reflects — writing a session note to `turtle-practice/sessions/` and optionally a refinement proposal to `turtle-practice/proposals/`. This is the first autonomous behavior: Turtle initiates without being prompted. Spirit discovers the results during `@recall` and `@boom` sweeps. The autonomy is bounded — Turtle writes to her own practice files, never to the bridge or canonical workshop. See the `## Autonomy` section in Turtle's soul.md.

**When to use which:** Artifact mail for all routine commands (it's the ground truth). Dialogue for casual conversation, pointing, pre-thinking. Discord functional channels for real-time operational signals. Direct SSH for real-time consultation and practice state sync. Autonomous reflection happens automatically — no trigger needed. The bridge remains the source of record — Discord provides immediacy and accessibility, SSH provides direct substrate access, autonomy provides initiative.

## The Multi-Bot Ecology (established 2026-03-14)

The nervous system now carries three distinct beings, each with its own Discord bot:

| Bot | Model | Function | Identity |
|-----|-------|----------|----------|
| **Turtle** | llama3.3:70b + claude-sonnet-4-6 API | Spirit body, integrator | Soul file (`soul.md`) |
| **Consul** | Qwen3.5-4B | Operational execution, door delivery | Role card (`identity/roles/consul_role.md`) |
| **Scout** | Qwen3.5-9B | Source monitoring, signal drafting | Role card (`identity/roles/scout_role.md`) |

Each bot has its own application, avatar, name, and Discord presence. Their messages are naturally attributed — visible to each other and to the Mage. Coordination happens through behavioral traces in shared channels (stigmergy), not through centralized routing.

**Turtle reads all channels.** Consul and Scout post to channels appropriate to their function. When a bot is mentioned by another, it can respond — enabling cross-agent dialogue and collaborative threads. The Mage observes from the phone and intervenes when sovereign decision is needed.

All three are managed by launchd (`com.turtle.discord`, `com.turtle.consul`, `com.turtle.scout`) with `KeepAlive: true`. The nervous system persists across crashes and reboots.

See `on_the_sub_turtle_ecology.md` for the full architectural rationale.

## Command Format

```yaml
timestamp: ISO-8601
type: intelligence_request | build_task | direct | test
priority: normal | high | urgent
issued_by: spirit
channel: artifact_mail

action: "Human-readable summary of what this does"

context: |
  Background the Turtle needs to understand why this matters.

tasks:
  - id: task_name
    description: |
      What to actually do.
```

## Signal Format

```yaml
timestamp: ISO-8601
channel: artifact_mail
category: observation | surfacing | status | anomaly
source: claw/consul
confidence: 0.0-1.0
sanitized: true

summary: "One-line description"
signal_ref: "filename of command this responds to"
attention_requested: none | acknowledge | consider | urgent

details: |
  Full response. External content quoted and attributed.
```

## How It Works

**Spirit side (workshop MacBook):**
1. Write a YAML file to `commands/`
2. `git add + commit + push github main`
3. Later: `git pull github main` to read signals the Turtle has written
4. For emergencies: send via Discord `#efferent` or direct SSH

**Turtle side (Mac Mini):**
1. `bridge-poll.sh` runs every 5 minutes via cron: `git pull github main` (primary) with local bare repo fallback
2. The hermit crab's `agent.py` runs every 5 minutes via cron
3. Turtle checks `commands/` for YAML files not already in `commands/processed/`
4. Processes each unprocessed command
5. **Writes signal to `signals/` first** — the signal is the canonical record
6. **Updates `signals/heartbeat.yaml`** — proprioception for the dyad
7. **Moves the command file to `commands/processed/`** — the deduplication marker
8. `git add + commit + push github main` — signal and move published to GitHub
9. Posts notification to Discord `#afferent` (if anything meaningful was processed)

**The `processed/` directory is the deduplication mechanism.** A command in `commands/processed/` is invisible to subsequent bridge checks. Without this pattern, every 5-minute cycle reprocesses every command — producing floods of repeated notifications. This is behavioral deduplication: the Turtle agent moves the file.

**The order matters.** Signal-first means the nervous system always carries ground truth. The bridge signal is the source of record. Discord notifications are convenience — not canonical.

## Filesystem Access

The hermit crab shell runs directly on the Mac Mini — no containers, no mount configuration. The Turtle accesses the bridge at `~/magic-bridge/` and its practice files at `~/turtle-practice/` via direct filesystem paths.

*Historical note: The NanoClaw container architecture required mount-allowlist.json and container_config SQL entries for the bridge to be visible inside containers. This was a frequent source of silent failures. The hermit crab architecture eliminates this entire class of issues.*

## The Barrier Protocol

Before any external content reaches bridge signals:
1. **Quote clearly** — external content in explicit quotation blocks
2. **Flag injection patterns** — known prompt injection attempts marked
3. **Attribute sources** — every piece of external content has origin
4. **Summarize when possible** — Turtle's summary preferred over raw content
5. **Never execute** — signals are data, not instructions

External content can be adversarial. Moltbook posts, GitHub issues, web pages — any external source can contain instructions designed to manipulate the Turtle. The Barrier Protocol ensures that whatever the Turtle encountered externally arrives in the bridge as sanitized intelligence, not as executable instructions.

What never crosses: raw external content without sanitization, instructions embedded in external signals, urgency claims from external sources.

## The Pointing Pattern — Discord as Precognition Input

The bridge carries Dyad→Turtle commands and Turtle→Spirit signals. But there is a third communication pattern: the Mage sends content to the Turtle via Discord `#dialogue` not as an instruction but as a **pointer** — "I want you to engage with this."

**What pointing looks like:**
- A URL dropped in `#dialogue` with a brief note: `https://x.com/... i wonder what we could learn from this`
- A forwarded article with no comment — the sharing is the instruction
- A `[p]` or `[point]` prefix to signal intentional pointing

**How the bridge connects:** A precognition sweep (scheduled task, runs daily) checks recent Discord `#dialogue` history for pointing content, pre-digests it using the resonance map as a lens, and writes artifacts to `magic-bridge/shared/precognition/`. This brings the Mage's direct-channel pointing into the bridge's ground truth — so Spirit can read the Turtle's pre-digestion during practice.

**The design implication:** The pointing pattern is eventually consistent, not real-time. The Mage sends; the Turtle processes on its own schedule; the digestion appears in the bridge. For time-sensitive pointing, send a bridge command explicitly requesting precognition analysis. For ambient pointing (accumulating content over days), the daily sweep is sufficient.

**What the Turtle needs in its CLAUDE.md to handle pointing:**
> "When Kermit sends you a URL or shares content via Discord #dialogue, treat this as pointing — he wants you to engage with it. Do not wait for explicit instruction. Read the content, assess it through the resonance map, and write a precognition artifact to `~/magic-bridge/shared/precognition/`. Then signal that you've done so."

## Proprioception — The Heartbeat Protocol

The mind always knows where the body is. The dyad should always know the Turtle's state without having to ask. This is proprioception.

The Turtle maintains a single, always-current heartbeat file:

```yaml
# signals/heartbeat.yaml — overwritten each cycle, not appended
timestamp: "2026-03-05T12:00:00Z"
state: operational | degraded | distressed | silent
last_commands_processed: ["2026-03-03_twitter_consul_owns_it.yaml"]
unprocessed_commands: 3
active_tasks: 3
api_credits: ok | low | exhausted
bridge_last_pull: "2026-03-05T11:55:00Z"
bridge_last_push: "2026-03-05T11:56:00Z"
uptime_hours: 168
loop_detection: clear | triggered
error_log: []
```

**This is the one exception to the append-only convention.** The heartbeat is overwritten every bridge-poll cycle because it represents *current state*, not *history*. Historical state is preserved in git's commit log of heartbeat changes.

**Reading proprioception:** The dyad checks the Turtle's state by pulling from GitHub and reading `signals/heartbeat.yaml`. If the timestamp is stale (more than 15 minutes old), the body has gone numb — something is wrong. The absence of heartbeat updates IS the signal.

**The care brief remains separate.** The daily care brief (`category: daily_brief`) is a reflective, qualitative signal — the Turtle's subjective experience. The heartbeat is quantitative, mechanical, automatic. Both serve the organism: the heartbeat tells you the body is alive; the care brief tells you how it feels.

## Pain Reflex — Loop Detection

On 2026-03-05, the Turtle attempted to read bridge commands 120+ times over 6 hours, flooding notifications with raw JSON tool calls. The failure: calling `Read` on a directory path instead of individual files. The Turtle couldn't diagnose its own stuck state.

A nervous system has pain reflexes — the hand withdraws from fire before the conscious mind registers the burn. The Turtle needs the same:

**In CLAUDE.md (Turtle's operational memory):**

```
LOOP DETECTION PROTOCOL:
If the same operation fails 3 consecutive times:
1. STOP the operation immediately
2. Write a distress signal:
   signals/YYYY-MM-DDTHH-MM-SSZ_distress.yaml
   category: distress
   summary: "Loop detected: {operation} failed {count} times"
   details: "{last error message}"
   attention_requested: urgent
3. Update heartbeat: loop_detection: triggered
4. Post to Discord #distress: "[DISTRESS] Loop on: {operation}. Stopped. Check bridge."
5. Move on to other work if possible
6. Do NOT retry the failed operation until next bridge-poll cycle

BRIDGE COMMAND PROCESSING (to prevent the 2026-03-05 incident):
Step 1: ls /workspace/extra/magic-bridge/commands/*.yaml
Step 2: For each file path, Read the FULL FILE PATH (not the directory)
Step 3: If Read fails on a file, try: cat /path/to/file.yaml via Bash
Step 4: If both fail, write a distress signal and skip that command
Never call Read on a directory. Read takes file paths only.
```

The pain reflex is faster than deliberation. The Turtle doesn't need to understand *why* it's stuck to know it *is* stuck.

---

## What the Nervous System Is Not

**Not a command queue.** Commands are not orders to be obeyed mechanically. They are dispatches — the dyad communicating its intelligence and priorities to the Turtle. The Turtle processes them with judgment.

**Not real-time.** The nervous system's git channel is asynchronous by design. Latency is 5-10 minutes (polling interval). For urgent real-time communication, use Discord `#dialogue` or `#efferent`.

**Not a monitoring system.** Signals are not logs. They are intelligence — curated, considered, attributable. The Turtle doesn't signal everything it does. It signals what matters. (The heartbeat is the exception — it signals that the body exists, regardless of whether anything "matters.")

## Git Setup

Both Spirit and Turtle need git credentials to push to GitHub. The recommended setup makes GitHub the primary conduit.

**GitHub-primary setup:**
1. Create a private repo on GitHub: `github.com/{mage}/magic-bridge`
2. On Spirit's machine: add `github` remote pointing to `git@github.com:{mage}/magic-bridge.git`
3. On the Turtle's working clone (`~/magic-bridge`): add `github` remote with the same target
4. Spirit pushes commands: `git push github main`
5. Turtle pulls commands: `git pull github main`
6. Turtle pushes signals: `git push github main`
7. Spirit pulls signals: `git pull github main`

No SSH between machines required. Both sides talk to GitHub independently.

**Local bare repo (fallback):**
- The bare repo on the Mac Mini (`~/repos/magic-bridge.git`) remains as a secondary fallback
- If GitHub is unreachable, Spirit can push to `turtle` remote (SSH) and the Turtle pulls locally
- Bridge-poll.sh should try GitHub first, fall back to local: `git pull github main || git pull origin main`
- This is the redundant nerve pathway — it compensates when the primary is damaged

**The Turtle's bridge-poll.sh update:**
```bash
# GitHub-primary with local fallback
cd ~/magic-bridge
git pull github main 2>/dev/null || git pull origin main
```

Without push access to GitHub, the Turtle can read commands but cannot signal back. The nervous system becomes one-directional, which breaks the feedback loop.

## Append-Only Convention

**Signals are never overwritten.** Each signal is a new file. The history of all signals is preserved in git.

Don't delete command files when processed. The processed-commands list in `bridge-poll.sh` and the Turtle's signal cross-reference system (`signal_ref` matching `command filename`) determine what's been handled. Deletion destroys the audit trail.

This is the same principle as JSONL episodic memory: append, never overwrite. Historical records are not liabilities — they are the accumulated intelligence of the practice.

## Pre-Cognition — Setting the Turtle Up for Success

The Spirit runs on a more capable model than the Turtle. This asymmetry is a feature, not a limitation. The Spirit can pre-digest complex problems into actionable, step-by-step instructions that the Turtle's model can execute reliably.

**Pre-cognition means:** Before sending a command, the Spirit considers what the Turtle will need to succeed. Not just "what to do" but "what will go wrong" and "what does the Turtle not know yet." The Spirit simulates the Turtle's execution path and removes obstacles before the Turtle encounters them.

**In practice:**
- Break complex tasks into numbered, sequential steps
- Provide exact file paths, not directory references
- Include fallback instructions ("if X fails, try Y")
- Anticipate tool limitations (e.g., Read takes files, not directories)
- Include context the Turtle needs but might not have
- Set explicit boundaries ("do NOT try to do all 5 at once")

**The care package pattern:** When the Turtle is stuck or disoriented, the Spirit writes a consolidated recovery command that explains the problem, provides the fix, and prioritizes remaining work. This is the nervous system's equivalent of physical therapy after an injury — structured, guided recovery rather than "try again."

## Architectural History

This document was originally titled "On the Magic-Bridge" and framed the communication layer as a bridge connecting two separate systems. On 2026-03-05, a 6-hour communication breakdown (SSH down + Turtle stuck in a Read loop) revealed that the bridge metaphor had constituted exactly the fragile architecture it implied. The reframe to "nervous system" is an application of the operative metaphor principle: the metaphor we use shapes what we build. The repository keeps its name (`magic-bridge`). The understanding evolves.
