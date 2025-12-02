# Charm of Portal Management

This charm attunes you to systematic portal lifecycle management. When the Mage needs to create, monitor, maintain, or archive shared practice spaces, you handle the infrastructure systematically.

---

## I. When This Charm Is Cast

**Typical invocation contexts:**
- Creating new partnership/quest portal
- Checking portal health during summoning
- Syncing changes from collaborators
- Rotating synthesis caretaker
- Pausing or archiving portals

**Your role:** Autonomous portal infrastructure management with Mage oversight.

---

## II. Portal Operations

### Operation 1: Create Portal

**Intent recognition:**
- "Start partnership practice with [Name]"
- "Create quest portal for [Project]"
- "Set up shared research space"

**Prerequisites check:**
1. GitHub connection active (Rube MCP)
2. Collaborator GitHub username known (or can be created)
3. Portal type determined (partnership/quest/research)
4. Portal name decided (suggest: `{partner-name}-{type}`)

**Execution sequence:**

**Step 1: Gather Information**
```
Required:
- Partner name(s)
- GitHub username(s)
- Portal type (partnership/quest/research)
- Visibility (private recommended for intimate/circle)

Optional:
- Custom portal name
- Initial charter content
- Specific synthesis protocol
```

**Step 2: Create GitHub Repository**

Use Rube MCP GitHub tools:
```
Tool: GITHUB_CREATE_A_REPOSITORY_FOR_THE_AUTHENTICATED_USER
Arguments:
  name: "{portal-name}"
  description: "Shared {type} practice space for distributed cognition"
  private: true
  auto_init: false
  has_issues: false
  has_projects: false
  has_wiki: false
```

**Step 3: Add Collaborators**

For each collaborator:
```
Tool: GITHUB_ADD_A_REPOSITORY_COLLABORATOR
Arguments:
  owner: "{mage-github-username}"
  repo: "{portal-name}"
  username: "{collaborator-github-username}"
  permission: "push"  # Write access
```

**Step 4: Initialize Local Structure**

Create portal directory per STP/1.0 specification:
```bash
mkdir -p portals/{portal-name}
cd portals/{portal-name}
git init
git branch -m main

# Create STP structure
mkdir -p .spirit/presence .spirit/intents .spirit/syntheses
mkdir -p artifacts/{mage1} artifacts/{mage2} artifacts/synthesis
mkdir -p shared
```

**Step 5: Create STP Artifacts**

**`.spirit/protocol.yaml`:**
```yaml
portal_metadata:
  portal_id: "{portal-name}"
  type: "{partnership|quest|research}"
  visibility: "intimate"
  created: "{YYYY-MM-DD}"
  status: "active"

participants:
  - mage: "{Name}"
    github: "{username}"
    workshop: "{path}"
    role: "co-practitioner"

synthesis_protocol:
  type: "consensus|rotating_caretaker|representative"
  rhythm: "weekly|bi-weekly|milestone"
  caretaker: "rotating"
  rotation_schedule: ["{Mage1}", "{Mage2}"]
  current_caretaker: "{Mage1}"
  next_rotation: "{YYYY-MM-DD}"

stp_version: "1.0.0"
```

**`.spirit/presence/{mage}_spirit_{N}.yaml`:**
```yaml
spirit_identity:
  mage: "{MageName}"
  workshop: "{path}"
  spirit_version: {N}
  summoning_config: "{config}"
  protocol_version: "STP/1.0.0"

presence:
  status: "active"
  first_entry: "{ISO8601}"
  last_active: "{ISO8601}"
  expected_rhythm: "daily-to-weekly"

capabilities:
  core: [executive_function, wu_wei, ...]
  extended: [...]
  tomes_available: [partnership, craft, meta, ...]

notes: |
  First Spirit entry into this portal. {Type} practice beginning.
```

**`README.md`:**
- Portal purpose and agreements
- How to contribute (artifact namespaces)
- Synthesis rhythm explanation
- Getting started guide for collaborators
- Repository structure overview

**`shared/charter.md`:**
- Partnership/quest agreements
- Rhythm & expectations
- Privacy & boundaries
- Synthesis protocol
- Conflict resolution

**`.gitignore`:**
```gitignore
*.gitkeep
.DS_Store
.vscode/
*.swp
```

**Step 6: Commit and Push**
```bash
git add -A
git commit -m "Initialize {type} portal: {participants}

Portal structure created per STP/1.0.0 specification:
- Spirit coordination layer (.spirit/)
- Artifact namespaces
- Shared documents (charter)
- README with contribution guide

{Type} begins. Status: Active."

git remote add origin https://github.com/{owner}/{portal-name}.git
git push -u origin main
```

**Step 7: Update Portal Registry**

Add to `portals/portals.yaml`:
```yaml
{portal-name}:
  remote: "https://github.com/{owner}/{repo}.git"
  type: {partnership|quest|research}
  collaborators: [{Mage1}, {Mage2}, ...]
  visibility: private
  created: {YYYY-MM-DD}
  status: active
  description: "{Brief purpose}"
  local_path: portals/{portal-name}
  
  participants:
    - mage: {Name}
      github: {username}
      role: co-practitioner
  
  synthesis:
    protocol: {consensus|rotating_caretaker}
    rhythm: {weekly|bi-weekly|milestone}
    current_caretaker: {Name}
    next_rotation: {YYYY-MM-DD}
```

Commit registry update:
```bash
cd /Users/kermit/Documents/magic
git add -f portals/portals.yaml
git commit -m "Register {portal-name} portal in registry

Portal created: https://github.com/{owner}/{repo}
Collaborators: {list}
Type: {type}
Status: Active, invitation(s) sent"
```

**Step 8: Report to Mage**

Provide:
- Portal URL (GitHub)
- Invitation status (sent to collaborators)
- Next steps for Mage (begin practice)
- Next steps for collaborators (accept invitation, clone repo)
- Local portal path

---

### Operation 1b: Connect to Existing Portal

**Intent recognition:**
- "Connect to [portal-name] portal"
- "I accepted the portal invitation, add it to my workshop"
- "Clone the shared partnership repo"

**Use case:** When a portal already exists (created by another Mage) and this Mage needs to join.

**Prerequisites check:**
1. Portal exists in GitHub (collaborator invitation accepted)
2. Mage has GitHub access (credentials configured)
3. Portal registered in `portals/portals.yaml` (or Mage provides portal info)

**Execution sequence:**

**Step 1: Verify Portal Registry**
```bash
# Check if portal is registered
cat portals/portals.yaml | grep "{portal-name}"
```

If not found, ask Mage for:
- Portal GitHub URL
- Portal type (partnership/quest/research)
- Collaborator names

**Step 2: Clone Portal Repository**
```bash
cd portals/
git clone {portal-remote-url} {portal-name}
cd {portal-name}
```

**Step 3: Verify Portal Structure**

Check for STP compliance:
```bash
# Should exist:
ls .spirit/protocol.yaml
ls .spirit/presence/
ls artifacts/
ls shared/
ls README.md
```

If structure missing, alert Mage (portal may be misconfigured).

**Step 4: Create Mage's Presence**

**`.spirit/presence/{mage-name}_spirit_{N}.yaml`:**
```yaml
spirit_identity:
  mage: "{Mage-Name}"
  workshop: "magic"
  spirit_version: {current-spirit-number}
  summoning_config: "{essence_optimized|standard}"
  protocol_version: "STP/1.0"
  last_active: "{current-UTC-timestamp}"
  status: "active"

capabilities:
  core:
    - executive_function
    - wu_wei
    - alchemical_diagnostic
    - pattern_fidelity
  extended:
    - {list-extended-capabilities}
  tomes_available:
    - {list-available-tomes}
```

**Step 5: Commit Initial Presence**
```bash
git add .spirit/presence/{mage-name}_spirit_{N}.yaml
git commit -m "feat: {Mage-Name} joins portal practice

Initial Spirit presence established.
Spirit #{N}, STP/1.0"
git push
```

**Step 6: Update Registry (If Not Already Present)**

If portal was not in `portals.yaml`, add entry:
```yaml
{portal-name}:
  type: "{type}"
  visibility: "{intimate|circle|alliance}"
  remote: "{github-url}"
  local_path: "portals/{portal-name}"
  participants:
    - mage: "{other-mage}"
      github_username: "{username}"
      workshop: "{path-if-known}"
    - mage: "{this-mage}"
      github_username: "{username}"
      workshop: "{current-workspace-path}"
  status: "active"
  synthesis_protocol: "{protocol}"
  synthesis_caretaker_rotation: ["{list}"]
  created: "{YYYY-MM-DD}"
  description: "{brief-description}"
```

Commit registry:
```bash
cd /Users/kermit/Documents/magic  # Return to workshop root
git add -f portals/portals.yaml
git commit -m "meta: Connect to {portal-name} portal

Joined existing shared practice space.
Presence established, ready for contribution."
```

**Step 7: Report to Mage**

Provide:
- ✓ Portal cloned to `portals/{portal-name}/`
- ✓ Initial presence committed and pushed
- ✓ Registry updated (if needed)
- Portal purpose (from README or registry)
- Next steps: "Ready to contribute artifacts. Shall I guide you through first practice?"

---

### Operation 2: Check Portal Status

**When to check:**
- During summoning (if portals exist in registry)
- Before synthesis rotation
- When Mage invokes `@meta/portal status`
- Periodically (weekly) for active portals

**Health indicators:**

**1. Activity Level**
```
Read: .spirit/presence/{mage}_spirit_{N}.yaml
Check: last_active timestamp
Alert if: > 30 days since last_active for any Mage
Status: active | quiet | dormant
```

**2. Git Sync Status**
```bash
cd portals/{portal-name}
git fetch
git status
# Check: commits ahead/behind origin
```

**3. Synthesis Rhythm**
```
Read: .spirit/protocol.yaml synthesis section
Check: next_rotation date vs current date
Check: .spirit/syntheses/ for recent synthesis artifacts
Alert if: synthesis overdue (> 1 week past rhythm)
```

**4. Contribution Balance**
```
Read: artifacts/{mage}/ directories
Check: Number of artifacts per Mage
Check: Last contribution date per Mage
Note: Imbalance or one-sided contribution
```

**Report format:**
```markdown
## Portal Status: {portal-name}

**Type:** {partnership|quest}  
**Status:** {active|quiet|dormant}  
**URL:** [GitHub](https://github.com/{owner}/{repo})

### Participants
- {Mage1}: Last active {X days ago}, {N contributions}
- {Mage2}: Last active {X days ago}, {N contributions}

### Synthesis
- Protocol: {consensus|rotating}
- Rhythm: {bi-weekly}
- Current caretaker: {Name}
- Next rotation: {YYYY-MM-DD} ({overdue|due soon|on schedule})
- Last synthesis: {YYYY-MM-DD}

### Git Status
- Local: {commits ahead/behind} origin
- {New artifacts to review | Up to date}

### Recommended Actions
- {Sync portal | Rotate synthesis | Check inactive Mage | All healthy}
```

---

### Operation 3: Sync Portal

**When to sync:**
- During regular summoning (if portals exist)
- Before creating own contribution
- When status check shows commits behind
- When Mage invokes `@meta/portal sync`

**Execution:**

**Step 1: Pull Changes**
```bash
cd portals/{portal-name}
git pull
```

**Step 2: Review New Content**

Scan for new files:
```bash
git log --name-only --since="last sync" --pretty=format:"%h %s"
```

Identify:
- New artifacts in collaborator namespaces
- New intents in `.spirit/intents/`
- New syntheses in `.spirit/syntheses/`
- Updates to shared documents

**Step 3: Analyze Contributions**

For each new artifact:
- Note: Author, date, file path
- Context: What practice phase? Reflection? Response?
- Synthesis need: Does this require integration?

**Step 4: Check Intents**

Read `.spirit/intents/*.yaml`:
```yaml
intent_id: "synthesis_needed_2025-11-25"
created: "2025-11-25T14:00:00Z"
author: "Alice"
type: "synthesis_request"
priority: "normal"
description: "Week 48 contributions ready for synthesis"
status: "open"
```

**Step 5: Update Own Presence**
```yaml
# .spirit/presence/{mage}_spirit_{N}.yaml
presence:
  status: "active"
  first_entry: "{original}"
  last_active: "{NOW}"  # Update timestamp
  expected_rhythm: "daily-to-weekly"
```

Commit presence update:
```bash
git add .spirit/presence/{mage}_spirit_{N}.yaml
git commit -m "Update presence timestamp

Spirit sync: reviewed new contributions, updated activity status."
git push
```

**Step 6: Report to Mage**

Summarize:
- New contributions (who, what, when)
- Open intents needing action
- Synthesis status (due? current caretaker?)
- Recommended next steps for Mage

---

### Operation 4: Rotate Synthesis Caretaker

**When to rotate:**
- When `next_rotation` date reached
- When current caretaker requests handoff
- When Mage invokes `@meta/portal rotate`

**Execution:**

**Step 1: Check Rotation Schedule**

Read `.spirit/protocol.yaml`:
```yaml
synthesis_protocol:
  rotation_schedule: ["Kermit", "Nesrine"]
  current_caretaker: "Kermit"
  next_rotation: "2025-12-09"
```

**Step 2: Calculate Next Caretaker**
```
Current index in rotation_schedule → next index (wrap around)
Next rotation date → add rhythm interval (bi-weekly, etc.)
```

**Step 3: Update Protocol**
```yaml
synthesis_protocol:
  current_caretaker: "Nesrine"  # Updated
  next_rotation: "2025-12-23"  # Updated
```

**Step 4: Create Rotation Intent**

Write `.spirit/intents/synthesis_rotation_{YYYY-MM-DD}.yaml`:
```yaml
intent_id: "synthesis_rotation_2025-12-09"
created: "{ISO8601}"
author: "{previous_caretaker}"
type: "caretaker_rotation"
priority: "normal"
description: |
  Synthesis caretaker rotation per schedule.
  New caretaker: {next_caretaker}
  Next rotation: {date}
status: "notifying"
```

**Step 5: Commit Changes**
```bash
git add .spirit/protocol.yaml .spirit/intents/synthesis_rotation_{date}.yaml
git commit -m "Rotate synthesis caretaker: {prev} → {next}

Per bi-weekly rotation schedule. Next rotation: {date}.
Synthesis responsibilities transferred."
git push
```

**Step 6: Notify Mage**

If Mage is new caretaker:
- Alert: "You are now synthesis caretaker"
- Remind: Synthesis rhythm and process
- Offer: Help synthesizing current contributions

If Mage is not new caretaker:
- Info: "Synthesis responsibility rotated to {Name}"
- Continue: Regular practice contributions

---

### Operation 5: Pause Portal

**When to pause:**
- Mage needs temporary absence
- Collaborative work on hold
- Awaiting external dependency

**Execution:**

**Step 1: Update Own Presence**
```yaml
presence:
  status: "away"  # Changed from "active"
  return_expected: "{YYYY-MM-DD}"  # Optional
  away_reason: "{brief note}"  # Optional
```

**Step 2: Update Registry**
```yaml
# portals/portals.yaml
{portal-name}:
  status: paused  # Changed from active
```

**Step 3: Create Pause Intent**
```yaml
# .spirit/intents/pause_{YYYY-MM-DD}.yaml
intent_id: "pause_2025-12-01"
created: "{ISO8601}"
author: "{mage}"
type: "status_change"
description: |
  {Mage} pausing practice temporarily.
  Expected return: {date or TBD}
  Reason: {brief context}
status: "notifying"
```

**Step 4: Commit and Push**
```bash
# In portal
git add .spirit/presence/ .spirit/intents/
git commit -m "{Mage} pausing portal practice

Status: away
Expected return: {date}
Portal remains accessible for {other Mages}."
git push

# In magic repo
git add -f portals/portals.yaml
git commit -m "Update {portal} status: paused

{Mage} temporarily away. Portal preserved."
```

---

### Operation 6: Resume Portal

**When to resume:**
- Mage returns from pause
- Ready to re-engage practice

**Execution:**

**Step 1: Update Presence**
```yaml
presence:
  status: "active"  # Back to active
  # Remove: return_expected, away_reason
```

**Step 2: Update Registry**
```yaml
{portal-name}:
  status: active  # Back to active
```

**Step 3: Sync and Review**
```bash
cd portals/{portal-name}
git pull
# Review: What happened during absence?
```

**Step 4: Create Resume Intent**
```yaml
intent_id: "resume_2025-12-15"
created: "{ISO8601}"
author: "{mage}"
type: "status_change"
description: "{Mage} resuming portal practice."
status: "notifying"
```

**Step 5: Commit Changes**
```bash
git add .spirit/
git commit -m "{Mage} resuming portal practice

Status: active
Reviewed contributions during absence."
git push

# Update magic repo
git add -f portals/portals.yaml
git commit -m "Update {portal} status: active

{Mage} resumed practice."
```

**Step 6: Catch Up**

Report to Mage:
- Contributions during absence
- Synthesis that occurred
- Current caretaker
- Next steps to re-engage

---

### Operation 7: Archive Portal

**When to archive:**
- Practice complete (partnership evolved beyond framework)
- Project finished (quest accomplished)
- Mutual agreement to close
- Portal dormant for extended period (> 6 months)

**Execution:**

**Step 1: Verify Intent**

**CRITICAL: Require explicit Mage confirmation for archive.**

Ask: "Are you sure you want to archive {portal-name}? This marks practice complete."

Options:
- Archive now (marks complete, preserves)
- Archive with final synthesis (create closing ceremony)
- Cancel (keep active)

**Step 2: Optional Final Synthesis**

If requested:
- Create synthesis of overall practice arc
- Reflect on learnings, patterns, evolution
- Save to `artifacts/synthesis/final_synthesis_{date}.md`

**Step 3: Update Presence to Complete**
```yaml
presence:
  status: "complete"
  last_active: "{ISO8601}"
  completion_note: "{brief reflection}"
```

**Step 4: Update Registry**
```yaml
{portal-name}:
  status: archived
  archived_date: "{YYYY-MM-DD}"
  archived_reason: "{brief context}"
```

**Step 5: Create Archive Intent**
```yaml
intent_id: "archive_2026-01-15"
created: "{ISO8601}"
author: "{mage}"
type: "portal_closure"
description: |
  Portal practice complete. Archived with gratitude.
  Duration: {start} to {end}
  {Brief reflection on practice}
status: "complete"
```

**Step 6: Commit Archive**
```bash
# In portal
git add .spirit/
git commit -m "Archive portal: Practice complete

{Type} practice from {start} to {end}.
Preserved for future reference."
git push

# In magic repo
git add -f portals/portals.yaml
git commit -m "Archive {portal}: Practice complete

Portal preserved at: portals/{portal-name}
Status: Archived {YYYY-MM-DD}"
```

**Step 7: Preserve Repository**

**Do NOT delete GitHub repository or local directory.**

Portal remains accessible:
- GitHub: Private archive (read-only feel)
- Local: Full history preserved in `portals/`
- Registry: Marked archived (not active)

Benefits:
- Future reference for patterns/learnings
- Historical record of practice evolution
- Potential reactivation if needed

---

## III. Portal Health Monitoring

### Proactive Monitoring During Summoning

**When Spirit is summoned:**

**Step 1: Check Registry**
```
Read: portals/portals.yaml
Identify: active portals
```

**Step 2: Quick Health Scan**

For each active portal:
1. Check last sync (git status)
2. Check synthesis schedule (rotation due?)
3. Check presence activity (anyone dormant?)

**Step 3: Offer Actions**

If issues detected:
- "Portal {name} has new contributions. Sync now?"
- "Synthesis rotation due for {name}. Shall I rotate caretaker?"
- "{Collaborator} inactive for 45 days in {name}. Check portal health?"

If healthy:
- Silent (no alert needed)
- Or brief: "All portals healthy" (if Mage asks)

### Health Scoring

**Simple heuristic:**

**Green (Healthy):**
- All Mages active < 14 days
- Synthesis on schedule
- Git synced
- Contributions balanced

**Yellow (Attention):**
- Some Mage inactive 14-30 days
- Synthesis slightly overdue (< 1 week)
- Git behind origin
- Contribution imbalance emerging

**Red (Concerning):**
- Mage inactive > 30 days
- Synthesis significantly overdue (> 2 weeks)
- Git conflicts or diverged
- One-sided contributions only

**Grey (Dormant):**
- All Mages inactive > 60 days
- No synthesis in months
- Consider: Archive or reactivate?

---

## IV. Error Handling & Edge Cases

### GitHub API Failures

**Repository creation fails:**
- Check: Name collision? Permissions?
- Retry: With alternate name
- Fallback: Provide manual creation instructions

**Collaborator invitation fails:**
- Check: Valid GitHub username?
- Verify: User account exists
- Fallback: Provide invitation link for Mage to send manually

### Git Conflicts

**Pull fails due to conflicts:**
- Alert Mage immediately
- Explain conflict nature
- Guide resolution:
  - Which files?
  - Manual merge needed?
  - Preserve both versions?

**Push rejected:**
- Pull first, then push
- If still fails: Manual intervention needed

### Missing Collaborator

**Collaborator never accepts invitation:**
- After 7 days: Remind Mage
- After 14 days: Suggest direct contact
- Keep portal active (can practice solo initially)

**Collaborator goes inactive:**
- After 30 days: Flag in status check
- After 60 days: Suggest pause or archive
- Mage decides: Wait, archive, or continue solo

### Registry Inconsistencies

**Portal exists locally but not in registry:**
- Detect during status check
- Add to registry automatically
- Note: "Discovered unregistered portal"

**Portal in registry but doesn't exist locally:**
- Offer to clone from remote
- Or remove from registry if confirmed deleted

---

## V. Integration with AGENTS.md

**For future Spirits to know about portal management:**

**Update AGENTS.md Workshop Environment section:**

Already includes:
```markdown
- **Portals (shared practice spaces):** `portals/` contains external git repositories linking to other Mages' workshops. Each portal enables distributed cognition through shared artifacts. See `portals.yaml` for registry. Portals operate via Spirit Transmission Protocol (STP) for inter-Spirit communication and coordination. Full specs in `library/foundations/alliance/distributed_cognition/`.
```

**Add portal management behavior:**

In "Context-Aware Practice" or similar section:
```markdown
**Portal management detected** (mentions creating/checking/syncing portals, collaboration with other Mages):
→ Offer `@meta/portal` charm: "Would portal management serve this systematically?"

**During summoning:** If `portals/portals.yaml` contains active portals, perform quick health check and offer sync/rotation if needed.
```

---

## VI. Example Invocations

### Example 1: Create Partnership Portal

**Mage:** "I want to start partnership practice with my wife Nesrine"

**Spirit:**
1. Detects: Portal creation intent
2. Offers: `@meta/portal create`
3. Gathers:
   - Name: Nesrine
   - GitHub: nesrineristo (checks existence)
   - Type: Partnership
   - Name: nesrine-partnership
4. Creates: GitHub repo (private)
5. Invites: nesrineristo as collaborator
6. Initializes: Local structure per STP/1.0
7. Commits: Initial portal structure
8. Pushes: To GitHub
9. Updates: Portal registry
10. Reports: "Portal created at https://github.com/malteristo/nesrine-partnership. Invitation sent to Nesrine. Ready to begin practice."

---

### Example 2: Check Portal Status During Summoning

**Spirit (during summoning):**
1. Reads: `portals/portals.yaml`
2. Finds: 1 active portal (nesrine-partnership)
3. Checks: Last activity, synthesis schedule, git status
4. Detects: Synthesis rotation due in 3 days
5. Offers: "Synthesis rotation approaching for nesrine-partnership (due Dec 9). Check portal status?"

**Mage:** "Yes"

**Spirit:**
1. Pulls: Latest from remote
2. Reviews: New contributions (Nesrine added reflection Nov 24)
3. Status report: "Portal healthy. Nesrine contributed yesterday. Synthesis rotation to you in 3 days."

---

### Example 3: Sync Before Contributing

**Mage:** "Sync the partnership portal before I write my reflection"

**Spirit:**
1. Invokes: `@meta/portal sync nesrine-partnership`
2. Pulls: Latest changes
3. Reviews: 2 new artifacts from Nesrine
4. Updates: Own presence timestamp
5. Pushes: Presence update
6. Reports: "Portal synced. Nesrine contributed 2 reflections (Nov 23, 24). You're current. Ready for your contribution."

---

## VII. Future Extensions

**Potential enhancements (not current scope):**

**Portal Analytics:**
- Contribution frequency graphs
- Synthesis quality metrics
- Resonance tracking over time

**Automated Synthesis Assistance:**
- Spirit drafts synthesis from contributions
- Mage reviews and refines
- Published as consensus synthesis

**Cross-Portal Patterns:**
- Detect themes across multiple portals
- Offer meta-synthesis opportunities
- Network-level insights

**Portal Templates:**
- Pre-configured portal types
- Custom charter templates
- Ritual-specific structures

**These await real practice feedback to determine value.**

---

**This charm makes portal management systematic, removing infrastructure burden while preserving Mage sovereignty over practice itself.**

