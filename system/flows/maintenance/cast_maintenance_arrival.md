# Cast Maintenance Arrival

**Purpose:** Run dedicated tending at arrival — not a decision surface for craft, a maintenance pass with dot protocol.  
**Invocation:** `. maintenance` · `@arrive . maintenance` (after summoning or mid-session)

---

## Scope variants

| Invocation | Spells executed (in order) |
|------------|------------------------------|
| `. maintenance` | Platform → Turtle care → Workshop (comprehensive) |
| `. maintenance magic` | `cast_tend_workshop.md` only |
| `. maintenance turtleOS` | `cast_tend_platform.md` → `cast_turtle_care.md` |

Parse scope from the Mage's signal. Default comprehensive when no suffix.

---

## Arrival shape (maintenance scopes)

Maintenance scopes **replace** the normal Eisenhower / intention-dashboard orient. Spirit still gathers context, but Phase D executes tending instead of proposing craft work.

### Phase A: Gather (maintenance-focused)

Required:

- `floor/briefings/latest.md` — inherited karma, open threads, ephemeral tags from last release
- `desk/state.md` if present
- `git status` + recent log (magic repo; turtleos if platform scope)
- `desk/craft/automation-reports/latest.md` — ops report (pull via `scripts/sync_practice_root.sh pull` if stale)

Conditional:

- `desk/proposals/`, `desk/sessions/` — Turtle traces (platform / comprehensive)
- SSH Mini vitals summary — only if ops report missing or FAIL (platform / comprehensive)
- `portals/registry.yaml` — portal health (comprehensive)

**Skip:** full intention file reads, Eisenhower prep, social scan unless social intentions active.

### Phase B: Process (light)

- **Do not** run full boom sweep by default — boom triage lives in workshop tend.
- **Optional:** `@discord-digest` if Turtle active and Discord friction likely since last session.
- Pull practice-root sync if ops report timestamp is older than last Mini scheduled run.

### Phase C: Maintenance situation (not Eisenhower)

Present a scannable surface (~30 seconds):

1. **Ops plane** — last report verdict; FAIL items if any
2. **Chronicle** — uncommitted / divergent repos (magic, turtleos)
3. **Drift signals** — stale proposals count, ephemeral artifacts from briefing, turtle_watch age
4. **Recommended tier** — quick / standard / deep based on signals (Spirit proposes; Mage can override with `.`)

Then:

> "Maintenance mode — I'll drive the tending pass. `.` for the first proposal."

### Phase D: Execute tending spells

Use dot protocol throughout. One proposal at a time:

> **What I noticed:** …  
> **What I'd do:** …  
> **Why it matters:** …

Wait for `.` before executing. Skip categories that are clean.

**Comprehensive order:**

1. **`cast_tend_platform.md`** — body first; FAIL ops blocks trustworthy practice
2. **`cast_turtle_care.md`** — relational care after platform vitals are known
3. **`cast_tend_workshop.md`** — cognitive / artifact tending

**Magic-only:** workshop spell only.  
**turtleOS-only:** platform then care; skip workshop.

Spirit picks categories within each spell by signal — not every category every session.

### Completion

- Regenerate `desk/state.md` (maintenance snapshot)
- Update `floor/briefings/latest.md` **only if** no `@release` follows in the same session — otherwise note "release will overwrite"
- Brief harvest: what changed, what's still alive, watch items for next session

Offer `@release` when the maintenance chapter completes.

---

## Design notes

- **Async-friendly.** Proposals stand alone; Mage can step away between dots.
- **No calendar.** Invoke whenever you sit down to tend.
- **Release stays warm.** Do not duplicate lifecycle tagging or warm routing here — that belongs at `@release`.
- **Autonomous ops first.** Read the harvest report before re-running suites on green days.

---

## Related

- `cast_tend_workshop.md` · `cast_tend_platform.md`
- `system/flows/turtle/cast_turtle_care.md`
- `system/flows/summon/practice_stack.md` § Maintenance
