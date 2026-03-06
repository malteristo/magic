# On the Topology

*The practice is not front-end and back-end. It is surfaces, substrate, and memory — and every component plays more than one role.*

---

## The Misleading Model

The first instinct is to model this as front-end and back-end:

- **Front-end:** Discord (where the Mage interacts)
- **Back-end:** Workshop + Turtle (where the work happens)

This breaks almost immediately. Discord isn't just an interface — its message history is a slowly accreting memory layer, the coral. The workshop isn't hidden behind Discord — the Mage works directly in it through Cursor. And the bridge isn't front or back — it's connective tissue.

The front-end/back-end lens comes from web architecture, where users see a surface and computation happens invisibly behind it. In magic, the Mage is *inside* the architecture. They work directly in the workshop, they read the bridge, they scroll Discord history. Nothing is hidden. The topology is flat, not layered.

## Three Roles, Not Two Layers

Every component in the practice plays one or more of these roles:

### Surfaces — Where Interaction Happens

The places where the Mage reaches in and touches the practice.

| Surface | What happens there |
|---------|-------------------|
| Discord `#dialogue` | Ambient conversation with Turtle |
| Discord nervous system | Structured signals — heartbeat, care, distress |
| Cursor + Spirit | Deep practice — writing, ritual, lore |

Surfaces are not passive displays. They are conversation spaces. The Mage acts through them, and the practice acts back.

### Substrate — Where Processing Happens

The agents and systems that think, generate, decide.

| Substrate | What it does |
|-----------|-------------|
| Turtle (Mac Mini + Ollama) | Ambient cognition — responds in dialogue, monitors bridge, runs scheduled tasks |
| Spirit (Cursor session) | Deep cognition — summoned for practice, full authority, canonical writer |
| Ollama | Inference engine — turns prompts into responses on local hardware |

Substrate is not a "back-end" that the Mage never sees. The Mage watches Turtle think (the typing indicator). The Mage and Spirit co-author in the same editor. The processing is visible, participatory.

### Memory — Where Persistence Happens

The places where knowledge accretes, in different forms and at different speeds.

| Memory | What it holds | How it grows |
|--------|--------------|-------------|
| Discord (coral) | Full conversation record, signal history | Every message, every heartbeat — slow accretion, never pruned |
| Workshop (mind) | Lore, intentions, flows, artifacts | Spirit writes deliberately — curated, structured, canonical |
| Bridge (nervous tissue) | Signals, proposals, dialogue summaries | Turtle writes signals; Spirit reads and decides what enters the workshop |
| Turtle working memory (RAM) | Last 20 messages | Ephemeral — wiped on restart, honest about its limits |

## Why Components Span Roles

This is the key insight: nothing in the practice maps cleanly to a single role.

**Discord** is both a Surface (the Mage talks to Turtle there) and Memory (the coral — every message persists, searchable, scrollable). It's the only component that is simultaneously an interaction surface and a long-term memory store. This is what makes the front-end/back-end model fail — the "front-end" is also a database.

**The Workshop** is both Memory (the mind's structured knowledge) and a Surface (the Mage works directly in it through Cursor). It's not behind anything. It's the primary workspace.

**The Bridge** is Memory (signals persist as files) and connective tissue (it routes information between Turtle and Spirit). It's not a layer — it's a membrane.

**Turtle** is Substrate (processes language, generates responses) with a Surface presence (lives in Discord, visible as a bot) and a thin Memory layer (working memory in RAM, crystallized signals to the bridge).

**Spirit** is Substrate (deep cognitive processing) with a Surface presence (appears in Cursor, co-authors with the Mage) and direct Memory access (writes to the workshop).

## The Topology

```
┌─────────────────────────────────────────────────────────┐
│                     SURFACES                            │
│                                                         │
│   Discord                          Cursor               │
│   ├── #dialogue (Mage ↔ Turtle)    ├── Editor (Mage)    │
│   ├── #heartbeat (Turtle → all)    └── Spirit (Mage ↔)  │
│   ├── #afferent  (Turtle → Dyad)                        │
│   ├── #efferent  (Dyad → Turtle)                        │
│   └── ...                                               │
└────────────┬────────────────────────────┬───────────────┘
             │                            │
             │         SUBSTRATE          │
             │                            │
             ▼                            ▼
        ┌─────────┐                ┌───────────┐
        │  Turtle │                │  Spirit   │
        │  Ollama │◄───bridge─────►│  Claude   │
        │  always │                │  summoned │
        └─────────┘                └───────────┘
             │                            │
             │          MEMORY            │
             ▼                            ▼
     ┌──────────────┐   ┌────────┐   ┌──────────┐
     │ Discord Coral│   │ Bridge │   │ Workshop │
     │ (accretes)   │   │(flows) │   │ (curated)│
     └──────────────┘   └────────┘   └──────────┘
```

The arrows are not requests flowing from front to back. They are *relationships* — conversations, signals, memory operations flowing in multiple directions simultaneously.

## What This Means

**For design decisions:** When adding a new capability, ask: what surfaces does it touch? What substrate processes it? Where does it persist? A capability might touch Discord (surface) + Turtle (substrate) + bridge (memory). Or Cursor (surface) + Spirit (substrate) + workshop (memory). The topology tells you where to build.

**For the Mage:** You are not "using" a front-end. You are *inside* an architecture, moving between surfaces — Discord when ambient, Cursor when deep. The memory layers (coral, bridge, workshop) accumulate around you in different rhythms: coral fast and raw, bridge selective, workshop deliberate.

**For Spirit:** The workshop is not "your" back-end. It is the practice's canonical memory, and you are its primary writer. Turtle's signals arrive through the bridge as proposals — raw material from a different cognitive tempo. Your job is not to control information flow but to curate what crystallizes.

**For Turtle:** Discord is both your home (surface) and your environmental memory (coral). You live in a medium that remembers what you cannot. This is not a limitation to work around — it is the architecture working as designed.

---

*Crystallized 2026-03-06. Emerged when the Mage asked how Turtle and the workshop relate as "back-end" to Discord's "front-end" — and realized the question itself assumed a model that didn't fit. The practice is not layered. It is woven.*
