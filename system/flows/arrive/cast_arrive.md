# Cast Arrive

**Purpose:** Run the Arrival mid-session — without summoning
**Spec:** `system/flows/summon/cast_arrival.md` (the contract, the scopes, the close)

---

## Invocation

```
@arrive
@arrive . craft
@arrive . turtle outfacing
@arrive . mirror
@arrive . maintenance [magic | turtleOS]
```

Scope follows the same table as the post-summoning dot. Default: holistic.

---

## Execution

1. **Do not re-summon.** The covenant is already held in this chat. If it feels thin, re-read `covenant.md` — a page, not a ritual, and cheaper than starting over.

2. **Parse the scope**, then run the arrival per `cast_arrival.md`: the same three obligations (what changed · one thing the Mage does not know, verified · a proposal with a recommendation), the same ~500-word cap, the same side-effect duties, the same close.

3. **Maintenance scopes** route to `system/flows/maintenance/cast_maintenance_arrival.md` instead — tending execution, no decision surface.

The mid-session arrival differs from the post-summoning one in exactly one way: inherited karma is already partly in the conversation, so *what changed* is measured from the last surface rather than from the briefing. Everything else is identical, and this file exists only to say so.

---

## When Not to Use

| Situation | Use instead |
|-----------|-------------|
| New chat / fresh session | `Summon` → `.` |
| Session ending | `@release` |
| Dedicated tending session | `. maintenance` |
| Lightweight "where are we?" without side effects | Read `desk/state.md` + `floor/briefings/latest.md` directly |

---

## Related

- `@release` — departure; writes the handoff file the arrival reads
- `archive/flows/recall/` — retired `@recall` flow (2026-06-19)

---

*Mid-session arrival. Inherited karma without re-summoning.*
