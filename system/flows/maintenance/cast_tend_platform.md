# Cast Tend Platform

**Purpose:** turtleOS platform tending — ops plane, deploy hygiene, functional gate, Discord health, practice-room glance.  
**Invocation:** `. maintenance turtleOS` · `@tend-platform` (on-demand)

Spirit fixes plumbing; Mage dogfoods UX only when a capability chapter closes (`functional-gate-protocol.md`). Relic `@turtle-care` is retired into this spell's encounter glance (2026-08-02) — not a separate wellbeing ritual.

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
- Slot after vitals known

### 7. Thread eddies

- `!eddy-check` or programmatic dissolution scan
- Surface flagged threads; Mage decides via buttons or verbally
- See `on_thread_eddies.md`

### 8. Turtle proposal triage (technical)

- Review recent `desk/proposals/*` from Turtle
- Route: adopt / close / defer / craft chapter
- Platform friction closure — not the practice-room glance

### 9. Workshop sync note

- Native topology: ops reports → `{practice_root}/state/notes/automation-reports/` → Forge pull
- No `~/workshop` clone required for harvest when sync script mapped
- Note if magic↔github remote diverged (separate merge chapter)

### 10. Retired substrate / fossil sweep

Retired infrastructure leaves listeners, env keys, disabled plists, and canary helpers that still look like product. Sweep when signals appear (or at least once per deep platform tend).

**Signals (any one is enough to open this category):**

- A port or Caddy route proxies a service that is down or retired (e.g. `:5985` → dead `:5984`)
- `.env` keys for a path the spec marks retired (`COUCHDB_*`, LiveSync, etc.)
- `*.plist.disabled` whose resurrection is forbidden without sanction
- **Live** `launchctl list` rows whose label or program path still names a retired substrate (`bridge`, `livesync`, `couch`, …) — including agents that are not `.disabled` and are failing to spawn
- Canary / heal registry entries that measure a retired path (or would go green/red for the wrong reason)
- Doc rows that still treat the fossil as optional current ops

**Pass (smallest responsible prune):**

1. Confirm retirement in law — `TURTLE_SPEC` / `docs/architecture.md` / learnings. If not retired, stop and open a chapter.
2. Kill live exposure first — public Funnel/Serve paths, Caddy reverse proxies, listening ports.
3. Remove operator config — `.env` keys; **`launchctl bootout` + delete** any live retired LaunchAgents; then disabled plists that will never reload. Do not trust `*.disabled` alone — a still-loaded label can point at a tree you already deleted.
4. Remove code that only served the fossil — unused canary checks, self-heal restart paths, stale matrix "optional" rows.
5. Leave large binaries/data dirs for a second proposal unless the Mage already sanctioned deletion (CouchDB.app, `livesync-bridge/` trees).
6. Record the prune in `docs/learnings.md` (one paragraph: what was fossil, what was removed, what was kept on purpose).

**Do not:** resurrect a retired path to "verify" it; funnel or serve an unauthenticated leftover; delete another practitioner's sync database without an explicit act on the sanction list.

Occasion that earned this category: 2026-08-02 — Funnel for the practice viewer would have published CouchDB at `/` had the old Serve map still pointed there; the process was already down, but Caddy `:5985`, `COUCHDB_*` env, and disabled plists were still furniture.

### 11. Practice-room glance (was `@turtle-care`)

See what the ambient partner has been *in* — not tend a soul. Skip in one line when quiet.

**Read (cheap):** recent `story/eddies/` on active roots (operator + shared + hosted if live); latest Turtle-authored note in `desk/proposals/` if newer than last maintenance.

**Surface (short):**

- Heat vs silence — where practice actually happened
- Hard terrain — misnames, overwhelm, trust burns (name the shape; don't re-litigate)
- Living verify — dogfood items that need a human eye, not a Spirit panel stack

**Not this category:** Mage→Turtle acknowledgment messages. Those are optional and Mage-initiated in Discord when something moves him — never a scheduled climax of maintenance.

---

## Close

Platform summary: ops verdict, SHAs, services, open FAILs, fossils pruned, practice-room glance (or "quiet").

Comprehensive `. maintenance` continues to workshop tend. No care-spell handoff.

---

## Related

- `turtleos/docs/automation/registry.md`
- `library/resonance/turtle/lore/operations/on_the_sovereign_ops_plane.md`
- `system/flows/turtle/cast_shake.md` · `cast_calibrate.md`
- Retired: `system/flows/turtle/cast_turtle_care.retired.md`
