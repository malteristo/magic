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
- If buffer has routable material: run full sweep including **§3.5 crucible stir** (`boom.flow.md`)

### 4b. Context rot radar

```bash
./scripts/rot_radar.py
```

Run it rather than performing the scan by hand. The table below is what it checks; it was a hand-scan until 2026-08-01, and a hand-scan is how a passed deadline keeps reading as live — the first automated run found a funding deadline seventeen days gone from an active intention that still called it a strong candidate.

The script reports and changes nothing. Routing stays the Mage's, on the dot. Read its output as the input to this section, then propose:

| Signal | Check | Severity |
|--------|-------|----------|
| Expired deadlines | A date already passed, in bright or an active intention | HIGH |
| Crucibles unmeasured | A crucible with no parseable `Last stirred` header — unchecked, not clean | HIGH |
| Seed Bank undated | Seed Bank present with no `Last reviewed` date — exempt from every check | HIGH |
| Stale Alive | Alive entries whose newest date exceeds 60d — *per entry*, not the file header | MEDIUM |
| Zombie habitats | Dormant/completed intentions named in bright's **active** sections | MEDIUM |
| Crucibles cold | `desk/boom/crucibles/` unstirred >30d, read from `Last stirred`, not mtime | MEDIUM |
| Proposal spores | `desk/proposals/` quiet >14d | MEDIUM |
| Floor zombies | `floor/drafts/` older than 30d | MEDIUM |
| Bright unswept | The `Last swept` header older than 7d | MEDIUM |
| Undated Alive | Alive entries with no date — unageable, invisible to every staleness rule | LOW |
| Seed Bank unreviewed | Seed Bank past its 90d quarterly cadence | LOW |
| Topic files cold | `desk/boom/*.md` topic files older than 7d | LOW |
| Uncommitted work · Stale/missing state · Turtle watch stale | Chronicle and state freshness | LOW |

**This table is the script's contents, and it is worth keeping honest.** Until 2026-08-01 it listed four checks the script did not implement — *Stale Alive*, *Undigested residue*, *Intention bloat*, *Sync drift* — while omitting six it did. Reading the spell, you would believe Alive was being watched. It was not: the radar read bright's header timestamp and never looked inside, and 120 Alive entries, 54 of them last dated April and 57 undated, went unreported for four months while the report came back tidy. *Stale Alive* and *Undated Alive* were implemented that day. **Undigested residue, intention bloat and sync drift are still not implemented** — they are absent from the script and now absent from this table, which is the honest state rather than a promise.

The same pass found the check named *"Crucibles unstirred"* globbing `desk/boom/*.md` — the eight **topic** files — while the eight actual crucibles sit one directory down in `desk/boom/crucibles/`, untouched by it since it was written. Stirring a crucible left its output byte-identical. The two surfaces are now separate signals with separate cadences, and the crucible check reads the `Last stirred` header the keeper maintains rather than mtime, which moves on any edit. The first honest run found **zero** cold crucibles: the *"7 crucibles dormant"* that briefings and `state.md` had carried for weeks was always the topic files wearing the crucibles' name.

Report count + top 3 items. Do not mass-edit `desk/` without Mage dot.

### 4c. Network surface

```bash
./scripts/listener_audit.sh                      # this machine
./scripts/listener_audit.sh mini <ssh-target>    # the Mini (address in connections.md)
```

Every other check in this spell reads the working tree. This one asks what the machine is *serving* — the only category of exposure the repository guards structurally cannot see, because a service reads files directly and never touches git.

Undeclared listeners are reported against `system/config/declared_listeners.txt`. Route each one: close it, rebind it to `127.0.0.1`, or declare it with a reason. **Declaring is a standing grant** — the audit will never mention that port again — so it is a Mage decision on the dot, not Spirit's tidy-up.

Non-zero exit means *not audited* (missing or malformed allowlist, unreachable host, `lsof` returned nothing). Read it as unknown, never as clean. `--self-test` plants a listener and confirms the audit still sees it; run it when a clean result is load-bearing.

*Added 2026-08-01. Before it existed, the spell had no step that would have found a five-month-old unauthenticated reader of `desk/` bound to every interface — and did not, across every tending pass in that window.*

### 5. Coherence (when appetite or signals warrant)

*Structural:* lore vs practice spot-check; contradictions in recently touched files — propose, don't silently fix.

*Conceptual (`conceptual-coherence` intention):* lexicon drift, named tensions in bright, metaphor health, internal vs outfacing terms.

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
