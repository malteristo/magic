# Cast Tend Platform

**Purpose:** turtleOS platform tending — ops plane, deploy hygiene, functional gate, Discord health.  
**Invocation:** `. maintenance turtleOS` (first spell) · `@tend-platform` (on-demand)

Relational Turtle care follows in `cast_turtle_care.md` when scope is `. maintenance turtleOS` or comprehensive `. maintenance`.

Spirit fixes plumbing; Mage dogfoods UX only when a capability chapter closes (`functional-gate-protocol.md`).

---

## Execution

One dot-protocol proposal at a time. Skip what's green.

### 1. Ops report (read before re-run)

- `./scripts/sync_practice_root.sh pull` if Forge harvest may be stale
- Read `desk/craft/automation-reports/latest.md`
- If **pass** and no deploy since report → skip re-running full suite; note verdict
- If **fail** or stale deploy → triage FAIL lines; run targeted fixes on Forge/Mini

### 2. Mini checkout hygiene

- SSH: `~/turtleos` git status, current SHA vs `origin/main`
- Clean tree before pull; use venv python (`./venv/bin/python3`) for tests
- Pull + restart when runtime Python changed

### 3. Services (split-bot)

Restart **both** when runtime code changed:

```bash
launchctl kickstart -k gui/$(id -u)/com.turtle.discord
launchctl kickstart -k gui/$(id -u)/com.turtle.river
```

Verify process start times are **after** the pull (`docs/learnings.md` deploy pitfall).

### 4. Functional gate

**Green path:** trust ops report.

**After deploy or FAIL:** on Mini:

```bash
cd ~/turtleos && ./venv/bin/python3 -m unittest discover -s tests -q
./venv/bin/python3 scripts/shake_report.py --write --strict
```

Live shakes (`--live`) only for **changed surface** — see `docs/automation/functional-gate-protocol.md`.

### 5. Traceability & docs

- Closed capability chapters → update `docs/traceability-matrix.md` rows
- Append discoveries to `docs/learnings.md` when non-obvious
- Commit turtleos from Forge checkout; push; Mini pull

### 6. Discord health (when signals or fortnightly cadence)

- Run `@discord-health` flow or lightweight manual read
- Slot after vitals known; before relational `@turtle-care`

### 7. Thread eddies

- `!eddy-check` or programmatic dissolution scan
- Surface flagged threads; Mage decides via buttons or verbally
- See `on_thread_eddies.md`

### 8. Turtle proposal triage (technical)

- Review recent `desk/proposals/*` from Turtle
- Route: adopt / close / defer / craft chapter
- Distinct from relational care — this is platform friction closure

### 9. Workshop sync note

- Native topology: ops reports → `{practice_root}/state/notes/automation-reports/` → Forge pull
- No `~/workshop` clone required for harvest when sync script mapped
- Note if magic↔github remote diverged (separate merge chapter)

---

## Close

Platform summary: ops verdict, SHAs, services, open FAILs, proposals routed.

Hand off to **`cast_turtle_care.md`** when scope includes turtleOS or comprehensive maintenance.

---

## Related

- `turtleos/docs/automation/registry.md`
- `library/resonance/turtle/lore/operations/on_the_sovereign_ops_plane.md`
- `system/flows/turtle/cast_shake.md` · `cast_calibrate.md`
