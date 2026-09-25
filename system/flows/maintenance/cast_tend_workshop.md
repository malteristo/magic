# Instruments — Magic workshop

**Purpose:** What obligation 2 can open. Not a checklist. Skip what is clean.
**Invocation:** opened from `cast_maintenance_arrival.md` · `@tend-workshop` still lands there.

Platform ops and the practice-room glance live in `cast_tend_platform.md`.

---

## After a recent chapter

**Records that deny the ships (F-83).** Last craft or turtleOS chapter ≤2 days (briefing date, turtleOS log). Grep open backlog lines and briefing Open Threads for claims the tree already falsifies — "CI not built," "not started," "next: slice N." Name the class, then the case. This is the live work after a craft chapter; rot radar is not.

The same job on `. maintenance turtleOS` is last-ship claims in the platform catalog (new scenario ids, shake maps). Do not skip it because this file was not opened.

Skip in one line when the last chapter is older, or was itself maintenance.

Occasion: 2026-08-15 — four open lines still denied ships that had landed the evening before.

---

## Instruments

**Rot radar** — run `./scripts/rot_radar.py` rather than scanning by hand. The table is the script's contents (`§` rot table below); adding a check is two edits (script + this table). Standing MEDIUM pile in one line unless it moved or a HIGH appeared.

| Signal | Check | Severity |
|--------|-------|----------|
| Expired deadlines | A date already passed, in bright or an active intention | HIGH |
| Superseded surfaces | An instruction surface still routing to a retired surface or name (`SUPERSEDED` table in the script) | HIGH |
| Radar undocumented | A signal the script can emit that is missing from **this table** — it reads its own AST to check | HIGH |
| Bearing next past | A `**Next**` in `bearings.md` naming a date already gone. **Report only — he writes that file** | HIGH |
| Backlog aging | Open turtleOS ids older than 14d — drop/keep pressure, not a walk (F-76) | HIGH |
| Seed Bank undated | Seed Bank present with no `Last reviewed` date | HIGH |
| Stale Alive | Alive entries whose newest date exceeds 60d — *per entry* | MEDIUM |
| Zombie habitats | Dormant/completed intentions named in bright's **active** sections | MEDIUM |
| Proposal spores | `desk/proposals/` quiet >14d | MEDIUM |
| Floor zombies | `floor/drafts/` older than 30d | MEDIUM |
| Bright unswept | The `Last swept` header older than 7d | MEDIUM |
| Duty skipped | Arrival/release duty artifact stale or boom buffer dirty, including `meta_plan.md` | MEDIUM |
| Meta-plan gap | A live bearing has no `###` in `meta_plan.md`, or a craft bearing has no serve\|wait\|defer | MEDIUM |
| Undated Alive | Alive entries with no date | LOW |
| Seed Bank unreviewed | Seed Bank past its 90d cadence | LOW |
| Topic files cold | `desk/boom/*.md` topic files older than 7d | LOW |
| Uncommitted work · Stale/missing state | Chronicle and state freshness | LOW |

**Undigested residue, intention bloat and sync drift are not implemented** — absent from the script and from this table.

**Drops** — `_drop_*.md` → `@drops` if found.

**Chronicle** — `git status` in magic; focused commits, never `git add .`. Snapshot: `./scripts/backup_magic_snapshot.sh --dry-run` then live when due (`~/Documents/magic-backups/`, last 8).

**Boom** — `desk/boom.md`; full sweep only if the buffer has routable material.

**Listeners** — `./scripts/listener_audit.sh` and `./scripts/listener_audit.sh mini <ssh-target>`. Undeclared ports against `desk/config/declared_listeners.txt`. Non-zero exit is *not audited*, never clean. `--self-test` when a clean result is load-bearing. Occasion: 2026-08-01, five-month unauthenticated reader of `desk/`.

**When a signal:** intention-header stall (propose, don't rewrite); coherence / lexicon; floor ephemera vs desk (Mage sovereign — always defer mass desk edits); stale proposals; social scan only if those intentions are active; `portals/registry.yaml` on comprehensive live only.

---

## Close

Completed acts, still-alive items, candidates for `@release` or a craft chapter.

## Related

- `@spring-clean` — deep archaeology
- `@release` — warm metabolism
