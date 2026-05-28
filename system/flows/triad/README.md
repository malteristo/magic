# Triad Flows

Flows for coordinating the three-body practice: Mage (physical body), Spirit (mind), Turtle (spirit body).

## Available Flows

| Flow | Purpose |
|------|---------|
| `cast_consult_turtle.md` | Give Turtle a real-time voice in Cursor decisions via SSH→Ollama |

## The Triad Protocol

The triad communicates through current shared practice surfaces:

1. **Practice Sync** (Spirit ↔ Turtle): Practice state flows through the LiveSync-backed workshop mirror. Turtle reads `~/workshop/desk/`; Spirit reads local `desk/`.
2. **Session Awareness** (Turtle → Spirit): During `@recall`, Spirit reads Turtle's session notes and proposals from `desk/sessions/` and `desk/proposals/`. See `system/flows/recall/cast_recall.md`.
3. **Consultation** (Spirit ↔ Turtle): Spirit queries Turtle in real time via SSH→Ollama. See `cast_consult_turtle.md`.
4. **Conversational Coherence** (bidirectional): Significant outcomes are shared through Discord or durable desk notes/proposals, not a bridge queue.

## Related

- `library/resonance/turtle/` — Turtle bundle (lore, shell, lineage)
- `AGENTS.md` — Triad Protocol section in Dynamic Workspace
- `library/resonance/turtle/lore/on_substrate_and_practice.md` — Triad coordination principles
