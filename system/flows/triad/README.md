# Triad Flows

Flows for coordinating Mage, Spirit, and Turtle across substrates.

> **Frame (2026-07-18):** Turtle here means the **native** persistent partner on turtleOS — not a Magic “spirit body.” Integration ontology: `library/resonance/turtle/lore/philosophy/on_integrating_turtleos.md`. Dyad/triad story scrolls in the turtle bundle are Lineage.

## Available Flows

| Flow | Purpose |
|------|---------|
| `cast_consult_turtle.md` | Give Turtle a real-time voice in Cursor decisions via SSH→Ollama |

## The Triad Protocol

The triad communicates through current shared practice surfaces:

1. **Practice Sync** (Spirit ↔ Turtle): Turtle writes to `~/workshops/kermit/` on Mini; Forge pulls via `./scripts/sync_practice_root.sh pull` into local `desk/` story/sessions/proposals and navigator notes.
2. **Session Awareness** (Turtle → Spirit): During Arrival Phase A, Spirit reads twine from `desk/story/`, plus proposals (and historical `desk/sessions/`). See `system/flows/summon/cast_arrival.md` Turtle Feedback Integration.
3. **Consultation** (Spirit ↔ Turtle): Spirit queries Turtle in real time via SSH→Ollama. See `cast_consult_turtle.md`.
4. **Conversational Coherence** (bidirectional): Significant outcomes are shared through Discord or durable desk notes/proposals, not a bridge queue.

## Related

- `library/resonance/turtle/` — Turtle bundle (prefer README Current/Keep map)
- `library/resonance/turtle/lore/philosophy/on_integrating_turtleos.md` — Purpose C spine
- `AGENTS.md` — Triad / Turtle load order in Dynamic Workspace
