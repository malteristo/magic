# On External Architectures

**Status:** Active - Universe Tome Lore

This scroll provides orientation to the major external cognitive architectures available in Universe.

---

## PAI (Personal AI Infrastructure)

**Source:** `universe/pai/`  
**Author:** Daniel Miessler  
**Focus:** Modular AI infrastructure with persistent memory and skills

### Core Concepts

| Concept | Description |
|---------|-------------|
| **Pack** | Self-contained capability bundle with README, INSTALL, VERIFY, src/ |
| **Skill** | Focused capability with SKILL.md routing table |
| **Workflow** | Step-by-step procedure for a task |
| **Hook** | Event-triggered automation (SessionStart, Stop, etc.) |
| **TELOS** | Life/project context framework (Mission, Goals, Problems) |

### Architecture

```
PAI Stack:
├── Claude Code (or other agent)
├── .claude/ directory
│   ├── CLAUDE.md (core instructions)
│   ├── skills/ (capability modules)
│   ├── hooks/ (event triggers)
│   └── MEMORY/ (persistent context)
```

### Key Files

- `README.md` — Project overview
- `Tools/PAIPackTemplate.md` — Pack creation specification
- `Packs/*/SKILL.md` — Skill routing tables

### Resonance with Magic

- Packs ≈ Tomes (modular capabilities)
- TELOS ≈ Resonance bundles (domain context)
- Hooks ≈ AGENTS.md rules (behavioral triggers)
- Memory ≈ Distributed memory (artifact-based recall)

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
