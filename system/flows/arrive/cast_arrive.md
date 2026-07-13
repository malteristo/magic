# Cast Arrive

**Purpose:** Run the Arrival Sequence mid-session — without summoning  
**Spec:** `system/flows/summon/cast_arrival.md`

---

## Invocation

```
@arrive
@arrive . craft
@arrive . turtle outfacing
@arrive . maintenance
@arrive . maintenance magic
@arrive . maintenance turtleOS
@arrive . creative
```

Optional scope follows the same rules as post-summoning `.` variants in `system/flows/summon/practice_stack.md`. Default: holistic (all intentions).

---

## Execution

1. **Do not re-summon.** Caretaker, Workshop, and Root are already integrated in this chat (or sufficient for the re-orientation needed). Skip Phase 0 and the three cycles.

2. **Parse scope** from the invocation (default holistic if no scope suffix).

3. **Execute the Arrival Sequence** — all phases in `system/flows/summon/cast_arrival.md`:
   - **Maintenance scopes** (`. maintenance` and variants) — follow `system/flows/maintenance/cast_maintenance_arrival.md`; Phase C is maintenance situation, Phase D is tending with dot protocol (not Eisenhower)
   - **Otherwise:**
   - **Phase A.0** — topical attunement if scoped to named intentions (not holistic, not maintenance/creative-only)
   - **Phase A** — Gather (reads `floor/briefings/latest.md` as inherited karma)
   - **Phase B** — Process (Discord digest when Turtle active, then boom sweep, Discord sync)
   - **Phase C** — Synthesize (situation, Eisenhower, fresh eyes, unanswered question, intention dashboard)
   - **Phase D** — Orient (self-feed Q1, default calibrated-delegation)
   - **Completion** — regenerate `desk/state.md` per Arrival completion spell

4. **Present** the decision surface and await Mage direction (`.` on Q1 continues the chapter).

---

## When Not to Use

| Situation | Use instead |
|-----------|-------------|
| New chat / fresh session | `Summon` → `.` |
| Session ending | `@release` |
| Dedicated tending session | `. maintenance` (see `maintenance/cast_maintenance_arrival.md`) |
| Lightweight "where are we?" without side effects | Read `desk/state.md` + `floor/briefings/latest.md` directly |

---

## Related

- `@release` — departure; writes the handoff file Arrival reads
- `archive/flows/recall/` — retired `@recall` flow (2026-06-19)

---

*Mid-session arrival. Inherited karma without re-summoning.*
