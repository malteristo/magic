# Cast Tend Workshop

**Purpose:** Magic workshop tending — artifacts, intentions, chronicle, coherence.  
**Invocation:** `. maintenance magic` · `@tend-workshop` (on-demand) · second spell of comprehensive `. maintenance`

Platform ops and practice-room glance live in `cast_tend_platform.md` — not here.

---

## Execution

Spirit works through categories in suggested order. Skip what's clean. One dot-protocol proposal at a time.

### 1. Drops

- Scan for `_drop_*.md` across the workshop
- If found, run `@drops` triage

### 2. Chronicle hygiene

- Uncommitted tracked changes (`git status` in magic repo)
- Meaningful changes worth committing vs. noise
- Propose focused commits — never `git add .`

### 2b. Practice snapshot backup

- `./scripts/backup_magic_snapshot.sh --dry-run` then live when due
- Confirm archive in `~/Documents/magic-backups/`
- Note prune policy (script keeps last 8 by default)

### 3. Intention health

- Read active intention headers + `chains.md`
- Surface: stalled intentions, completed-but-not-closed, overdue phase transitions
- Do not rewrite intentions — propose field updates for Mage confirmation

### 4. Boom triage

- Read `desk/boom.md`, `desk/boom/bright.md`
- Surface stale, resolved, or intention-ready items
- Propose `bright.md` updates
- If buffer has routable material: run full sweep (`boom.flow.md`)

### 4a. Records that deny the ships

When the last craft chapter is in the last two days (briefing date, turtleOS log since last maintenance), grep **open** backlog lines and briefing Open Threads for claims the tree already falsifies — "CI not built," "not started," "next: slice N," a question the Seal already answered. Name the class, then the case. That scan is the live work after a craft chapter; rot radar is not.

Skip in one line when the last chapter is older, or was itself maintenance.

Occasion: 2026-08-15 — CI / Skip / offer-ledger / slice 3 / layers-"not started" still denied ships that had landed the evening before. One grep; four more cases.

### 4b. Context rot radar

```bash
./scripts/rot_radar.py
```

Run it rather than performing the scan by hand. The table below is what it checks; it was a hand-scan until 2026-08-01, and a hand-scan is how a passed deadline keeps reading as live — the first automated run found a funding deadline seventeen days gone from an active intention that still called it a strong candidate.

The script reports and changes nothing. Routing stays the Mage's, on the dot. Read its output as the input to this section, then propose:

| Signal | Check | Severity |
|--------|-------|----------|
| Expired deadlines | A date already passed, in bright or an active intention | HIGH |
| Superseded surfaces | An instruction surface still routing to a retired surface or name (`SUPERSEDED` table in the script) | HIGH |
| Radar undocumented | A signal the script can emit that is missing from **this table** — it reads its own AST to check | HIGH |
| Bearing next past | A `**Next**` in `bearings.md` naming a date already gone. Provenance marks stripped; German dates read. **Report only — he writes that file** | HIGH |
| Seed Bank undated | Seed Bank present with no `Last reviewed` date — exempt from every check | HIGH |
| Stale Alive | Alive entries whose newest date exceeds 60d — *per entry*, not the file header | MEDIUM |
| Zombie habitats | Dormant/completed intentions named in bright's **active** sections | MEDIUM |
| Proposal spores | `desk/proposals/` quiet >14d | MEDIUM |
| Floor zombies | `floor/drafts/` older than 30d | MEDIUM |
| Bright unswept | The `Last swept` header older than 7d | MEDIUM |
| Undated Alive | Alive entries with no date — unageable, invisible to every staleness rule | LOW |
| Seed Bank unreviewed | Seed Bank past its 90d quarterly cadence | LOW |
| Topic files cold | `desk/boom/*.md` topic files older than 7d | LOW |
| Uncommitted work · Stale/missing state · Turtle watch stale | Chronicle and state freshness | LOW |

**This table is the script's contents, and it is worth keeping honest.** *It went wrong again on 2026-08-25, in the other direction and within the same hour:* Spirit added the *Superseded surfaces* check and did not add its row — while working on a reroute whose whole finding was that documentation keeps answering retired questions. Caught only because the next command happened to print this section. **Adding a check is two edits, and the second one is this table.**

Until 2026-08-01 it listed four checks the script did not implement — *Stale Alive*, *Undigested residue*, *Intention bloat*, *Sync drift* — while omitting six it did. Reading the spell, you would believe Alive was being watched. It was not: the radar read bright's header timestamp and never looked inside, and 120 Alive entries, 54 of them last dated April and 57 undated, went unreported for four months while the report came back tidy. *Stale Alive* and *Undated Alive* were implemented that day. **Undigested residue, intention bloat and sync drift are still not implemented** — they are absent from the script and now absent from this table, which is the honest state rather than a promise.

Crucible cold/unmeasured checks were retired with the crucibles (2026-08-10). Topic-file coldness remains the boom-depth staleness signal.

Standing MEDIUM pile in **one line unless it moved** (count jump vs the previous `desk/state.md` snapshot, or a HIGH appeared). Do not list 33 Alive / 27 spores / 29 floor zombies when those numbers are the same pile as last time — that costs the attention the one real item deserved. Occasion: 2026-08-15. Do not mass-edit `desk/` without Mage dot.

### 4c. Network surface

```bash
./scripts/listener_audit.sh                      # this machine
./scripts/listener_audit.sh mini <ssh-target>    # the Mini (address in connections.md)
```

Every other check in this spell reads the working tree. This one asks what the machine is *serving* — the only category of exposure the repository guards structurally cannot see, because a service reads files directly and never touches git.

Undeclared listeners are reported against `desk/config/declared_listeners.txt`. Route each one: close it, rebind it to `127.0.0.1`, or declare it with a reason. **Declaring is a standing grant** — the audit will never mention that port again — so it is a Mage decision on the dot, not Spirit's tidy-up.

Non-zero exit means *not audited* (missing or malformed allowlist, unreachable host, `lsof` returned nothing). Read it as unknown, never as clean. `--self-test` plants a listener and confirms the audit still sees it; run it when a clean result is load-bearing.

*Added 2026-08-01. Before it existed, the spell had no step that would have found a five-month-old unauthenticated reader of `desk/` bound to every interface — and did not, across every tending pass in that window.*

### 5. Coherence (when appetite or signals warrant)

*Structural:* lore vs practice spot-check; contradictions in recently touched files — propose, don't silently fix.

*Conceptual:* lexicon drift, named tensions in bright, metaphor health, internal vs outfacing terms. *(The `conceptual-coherence` intention that used to own this pass was retired 2026-08-13 — the check survives it; lore's remaining jobs are canonical home for protocols and the part of the practice that ships.)*

*Report:* active / resolved / new tensions; tensions >30 days → "stalled — still real?"

### 6. Workshop metabolism

**Floor** (Spirit's domain — default release for stale ephemera):
- Ephemeral tags from recent release bundles — clear
- Files >30 days untied to active intentions → release / distill / keep

**Desk** (Mage sovereign — gentle):
- Surface desk artifacts untouched 30+ days; always defer

**Box** (visibility, not deletion):
- Sample 2–3 old box files; note age and whether mined

**Proposals** (`desk/proposals/`):
- Stale >14 days; integrated → `archived/`; overtaken → Mage decision

**Broken references** — surface when noticed.

### 7. Social scan (conditional)

- Only when social intentions are active
- Surface items needing attention; do not draft responses

### 8. Portal health (comprehensive maintenance only)

- Quick read of `portals/registry.yaml` if present

---

## Close

Brief summary: completed actions, still-alive items, propagation candidates worth `@release` or a craft chapter.

---

## Related

- `@spring-clean` — deep archaeology when this sweep isn't enough
- `@release` — warm metabolism every session end
- `floor/on_resonance_metabolism_draft.md` — promoted into `on_context_ecology.md` §Resonance Metabolism (2026-07-15); draft retained as archive
