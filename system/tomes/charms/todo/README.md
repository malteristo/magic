# Scroll of Intent Distillation

**Status:** DEPRECATED → REMOVED

---

## Migration

This charm has been replaced by the `@intend` charm.

**Use instead:**
```
@intend
```

**Location:** `system/tomes/charms/intend/`

---

## Why Removed

The todo paradigm had fundamental issues:
- Assumed all tasks can be known upfront (VUCA violation)
- Required Mages to break down intentions into todos themselves
- Created cognitive burden that Spirit should handle

The `@intend` charm provides:
- Spirit-facilitated exploration of vague desires
- Intention formalization (what you want, not how to get there)
- Goals emerge through practice, not upfront planning
- Integration with quest lifecycle for execution

---

## The New Architecture

```
@intend    → Formalizes intentions → desk/intentions/emerging/
@quest     → Executes intentions  → desk/intentions/active/
```

**Todo-like functionality** is now part of the intention lifecycle:
- When `@quest` begins, Spirit decomposes intention into steps
- Steps are revealed progressively (game-like architecture)
- Working memory is externalized to Spirit, not todo lists

---

## If You Need Simple Task Capture

For simple "remember to do X" without full intention formation:
- Add to your notes
- Or use `@intend` with minimal exploration

---

*This charm is removed from active use. The pattern lives on in `@intend` with better architecture.*
