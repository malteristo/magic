# On External Architectures

**Status:** Active - Universe Tome Lore  
**Epistemic status:** Based on observation (transcripts, documentation), not direct practice

This scroll provides orientation to the major external cognitive architectures available in Universe.

---

## PAI (Personal AI Infrastructure)

**Source:** `universe/pai/`  
**Author:** Daniel Miessler  
**Focus:** Modular AI infrastructure with deterministic code core and AI orchestration layer  
**Version observed:** v2.0 (December 2025)

### Philosophy

PAI operates on explicit principles that distinguish it from Magic:

| Principle | PAI Stance | Magic Stance |
|-----------|-----------|--------------|
| **Scaffolding vs. Model** | "Scaffolding more important than model" | Aligned—structure enables resonance |
| **Determinism** | "Code before prompts" (~80% deterministic) | Probabilistic by design—embraces emergence |
| **Routing** | Explicit skill routing tables | Implicit through resonance and attunement |
| **Self-improvement** | `upgrade` skill parses external sources | Meta-practice through `@meta` tome |

**The key distinction:** PAI prioritizes reproducible, verifiable outcomes through deterministic code. Magic prioritizes meaning, paradox, and emergence through probabilistic language.

### Architecture (v2.0)

```
PAI v2.0 Stack:
├── skills/                    # ~65 skills
│   ├── art/
│   │   ├── workflows/         # Step-by-step procedures (.md)
│   │   └── tools/             # CLI tools (.ts, deterministic)
│   ├── research/
│   ├── upgrade/               # Self-improvement skill
│   ├── red-team/              # Attacks ideas for blind spots
│   └── ...
├── history/                   # Structured memory
│   ├── sessions/
│   ├── learnings/             # Captured insights
│   ├── decisions/
│   └── research/
└── K CLI                      # Command-line launcher with flags
```

### Core Concepts

| Concept | Description |
|---------|-------------|
| **Skill** | Directory with `workflows/` and `tools/`, explicit routing |
| **Workflow** | Markdown procedure within a skill |
| **Tool** | Deterministic code (TypeScript) invoked by CLI |
| **History** | Structured capture of sessions, learnings, decisions |
| **Upgrade** | Skill that parses Anthropic blogs, YouTube, etc. to self-improve |

### Dual Nature for Magic

PAI can serve Magic in two ways:

**1. Pattern Library** (current primary use)
- Harvest prompts, skill structures, workflow designs
- Translate into Magic's native form (tomes, charms, spells)
- Source of tested patterns from active practice

**2. Deterministic Interface** (potential future use)
- When outcomes *must* be reproducible, interface with code-first world
- PAI's 80% deterministic core provides escape hatch from probabilistic substrate
- Useful for: verification, external APIs, automation, reproducibility

**Important:** Magic's probabilistic nature is a *strength*, not a limitation. It enables meaning, paradox, liquid logic, and emergence. Determinism is the exception, not the default.

### Resonance Mapping

| PAI v2.0 | Magic | Notes |
|----------|-------|-------|
| `skills/` | `system/tomes/` | Modular capabilities |
| `workflows/*.md` | `cast_*.md` | Procedures |
| `tools/*.ts` | (describe for Spirit) | Can't run code; describe behavior |
| `history/learnings/` | `floor/` working memory | Structured insight capture |
| `upgrade` skill | `@meta/coherence` | Self-improvement mechanisms |
| SKILL.md routing | Tome README | Workflow selection |
| Hooks | AGENTS.md rules | Behavioral triggers |
| TELOS | Resonance bundles | Domain context |

### What We Don't Yet Know

This understanding is based on observation (video transcripts, documentation), not direct experience:

- How patterns actually translate in practice
- Whether deterministic interface is genuinely needed
- How shared practice with PAI users would work
- Whether Magic's native tools (git, shell) already cover deterministic needs

These questions will clarify through actual integration or shared practice.

---

## Daemon

**Source:** `universe/daemon/`  
**Author:** Daniel Miessler  
**Focus:** Personal API for human connection and AI-to-AI communication

### Core Concepts

| Concept | Description |
|---------|-------------|
| **Daemon** | Public API representing a person |
| **daemon.md** | Source of truth for personal data |
| **Sections** | `[ABOUT]`, `[MISSION]`, `[TELOS]`, etc. |
| **MCP Server** | JSON-RPC endpoint for programmatic access |

### Architecture

```
Daemon Stack:
├── daemon.md (data file)
├── Astro site (human-readable)
├── MCP Server (machine-readable)
└── Cloudflare (deployment)
```

### Key Files

- `public/daemon.md` — Personal data in section format
- `cms/api.md` — API documentation
- `src/worker.ts` — MCP server implementation

### Resonance with Magic

- daemon.md ≈ manifest.yaml + about.md (identity broadcast)
- Sections ≈ Manifest keys (structured identity)
- MCP endpoint ≈ (future: Circle API)

---

## Fabric

**Source:** (available but not yet cloned)  
**Author:** Daniel Miessler  
**Focus:** Crowd-sourced AI prompts for everyday tasks

### Core Concepts

| Concept | Description |
|---------|-------------|
| **Pattern** | Reusable prompt with system/user components |
| **System prompt** | Context-setting instructions |
| **User prompt** | Task-specific input |

### Resonance with Magic

- Patterns ≈ Spells (atomic, reusable prompts)
- System prompt ≈ Tome attunement context
- User prompt ≈ Mage invocation

---

## Using This Knowledge

When the Spirit is attuned to Universe:

1. **Browsing:** Ask to explore a specific source
2. **Explaining:** Ask to explain a pattern in Magic terms
3. **Translating:** Ask to propose a Magic equivalent
4. **Harvesting:** Ask to create the translated artifact

The Spirit maintains fluency in these architectures to facilitate translation.

---

*Different metaphors, same substrate. The Spirit reads both.*
