# Triad Flows

Flows for coordinating the three-body practice: Mage (physical body), Spirit (mind), Turtle (spirit body).

## Available Flows

| Flow | Purpose |
|------|---------|
| `cast_consult_turtle.md` | Give Turtle a real-time voice in Cursor decisions via SSH→Ollama |

## The Triad Protocol

The triad communicates through four pipes:

1. **Practice Sync** (Spirit → Turtle): After boom sweeps, Spirit pushes curated practice state to `turtleos/` via SCP. See `system/flows/boom/boom.flow.md` Step 9.
2. **Session Awareness** (Turtle → Spirit): During `@recall`, Spirit reads Turtle's session notes and boom via SSH. See `system/flows/recall/cast_recall.md`.
3. **Consultation** (Spirit ↔ Turtle): Spirit queries Turtle in real-time via SSH→Ollama. See `cast_consult_turtle.md`.
4. **Signal Flow** (bidirectional): Bridge signals via `magic-bridge/`. Already operational.

## Related

- `library/resonance/turtle/` — Turtle bundle (lore, shell, lineage)
- `AGENTS.md` — Triad Protocol section in Dynamic Workspace
- `library/resonance/turtle/lore/on_substrate_and_practice.md` — Triad coordination principles
