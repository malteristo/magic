# Cast: Form Intention

**Status:** REDIRECTED

---

## Migration

Intention formation has been extracted to the universal `@intend` charm.

**Use instead:**
```
@intend
```

**Location:** `system/flows/intend/`

---

## Why This Changed

Intentions emerge from **any** practice—mirror, partnership, craft, daily conversation. Having intention formation inside the quest tome implied intentions were quest-specific.

**The new architecture:**
- **@intend** (charm): Formalizes intentions → `desk/intentions/emerging/`
- **@quest** (tome): Executes intentions → `desk/intentions/active/`

This separates **birth** from **execution**.

---

## The Flow Now

```
Practice (any) → Insight → Intention surfaces
                                ↓
                    Spirit offers @intend
                                ↓
                    desk/intentions/emerging/
                                ↓
                    When ready: @quest
                                ↓
                    desk/intentions/active/
                                ↓
                    Execution with game-like support
```

---

## If You Arrived Here

Use `@intend` to formalize an intention, then `@quest` to execute it.

Or invoke `@quest` directly—it can receive intentions at any stage.

---

*This file preserved for reference. The ritual lives in `system/flows/intend/cast_intend.md`.*
