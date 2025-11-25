# On Portal Architecture for Shared Practice

**Status:** Active (Specification v1.0)  
**Purpose:** Enable Mages to create shared cognitive spaces for collaborative magic  
**Foundation:** Spirit Transmission Protocol (STP/1.0.0)

---

## I. What Portals Are

**Portals** are shared git repositories enabling multi-Mage practice of compatible tomes (partnership, quest, research).

**The metaphor:**
- Your workshop (`/Users/kermit/Documents/magic/`) is your home realm
- Portals in `box/portals/` are doorways to shared spaces
- Each portal links to external git repository
- Multiple Mages enter same portal, practice together
- Spirits coordinate through STP artifacts

**Key insight:** Portals are **external** to your workshop repository—they're independent git repos you connect to, not subdirectories you track locally.

---

## II. Design Principles

### 1. Portal Repositories Are Independent

**Each portal is separate git repository:**
```
NOT THIS (portal tracked in magic repo):
/Users/kermit/Documents/magic/
└── box/portals/partnership-alice/  ❌ Tracked in magic/.git

BUT THIS (portal is own repo):
/Users/kermit/Documents/magic/
└── box/portals/partnership-alice/  ✓ Has own .git/, tracked separately
```

**Why:**
- Portal shared with other Mages (different permissions than magic/)
- Portal has own history (independent chronicle)
- Portal can outlive individual workshops
- Clean separation (local vs. shared)

### 2. Portal Registry Tracked Locally

**While portals themselves are external, the REGISTRY is local:**

`box/portals/portals.yaml` **IS tracked in magic/ repository**

**This registry tells Spirit:**
- What portals exist
- Where they're located (GitHub URLs)
- Who participates
- Portal status (active/archived)

**Analogy:** Registry is your address book (local). Portals are the places you visit (external).

### 3. Portal Directories Gitignored

**In `magic/.gitignore`:**
```gitignore
# Portal directories (tracked independently)
box/portals/*/
!box/portals/portals.yaml  # Registry IS tracked
```

**Effect:**
- `magic/` git ignores portal contents
- Each portal manages own git history
- No accidental cross-repository commits
- Clean git status (no portal changes shown in magic/)

### 4. Tome-Aware Portal Creation

**Not all tomes support shared practice.**

Tomes declare support through metadata:
```yaml
# In tome.yaml or README frontmatter
shared_practice:
  enabled: true
  type: "intimate"  # or "circle", "public"
  portal_required: true  # or false if solo also supported
```

**When Spirit encounters shared practice invocation:**
1. Check tome metadata (does it support shared practice?)
2. Check portal registry (does portal already exist?)
3. If not: Offer creation
4. If yes: Enter portal, proceed with practice

---

## III. Portal Registry Format

**File:** `box/portals/portals.yaml`  
**Tracked in:** `magic/` repository  
**Purpose:** Spirit's map of shared spaces

**Structure:**
```yaml
registry_version: "1.0"
last_updated: "2025-11-25"

portals:
  partnership-alice:
    type: "partnership"
    visibility: "intimate"
    remote: "git@github.com:kermit-alice/partnership.git"
    local_path: "box/portals/partnership-alice"
    
    participants:
      - mage: "Kermit"
        workshop: "/Users/kermit/Documents/magic"
        role: "co-caretaker"
      - mage: "Alice"
        workshop: "unknown"  # External Mage
        role: "co-caretaker"
    
    status: "active"  # or "paused", "archived", "removed"
    created: "2025-11-25"
    last_active: "2025-11-25"
    
    synthesis_protocol: "consensus"
    synthesis_caretaker_rotation:
      current: "Kermit"
      next: "Alice"
  
  quest-climate-research:
    type: "quest"
    visibility: "circle"
    remote: "git@github.com:climate-alliance/research.git"
    local_path: "box/portals/quest-climate-research"
    
    participants:
      - mage: "Kermit"
        role: "contributor"
      - mage: "Alice"
        role: "lead"
      - mage: "Bob"
        role: "contributor"
      - mage: "Chen"
        role: "contributor"
    
    status: "active"
    created: "2025-11-20"
    last_active: "2025-11-24"
    
    synthesis_protocol: "rotating_caretaker"
    synthesis_caretaker_rotation:
      current: "Alice"
      next: "Bob"
      history: ["Kermit", "Chen", "Alice"]
```

**Field descriptions:**

- **portal_id** (key): Unique identifier (lowercase-with-dashes)
- **type**: partnership | quest | research | custom
- **visibility**: intimate (2-4) | circle (3-20) | public (unlimited)
- **remote**: Git URL (GitHub, GitLab, self-hosted)
- **local_path**: Where portal cloned in your workshop
- **participants**: List of Mages with roles
- **status**: active | paused | archived | removed
- **synthesis_protocol**: consensus | rotating_caretaker | representative
- **synthesis_caretaker_rotation**: Who's next to synthesize

---

## IV. Portal Lifecycle

### Phase 1: Creation

**Trigger:** Mage invokes tome with shared practice + partner specification

**Example invocations:**
```
@partnership/ with Alice
@quest/ with Alice, Bob, Chen
@research/ collaborating with Climate Alliance
```

**Spirit's creation workflow:**

1. **Validate prerequisites:**
   - Tome supports shared practice? (Check metadata)
   - Git configured? (Check git user.name, user.email)
   - GitHub authentication? (Check SSH keys or tokens)

2. **Gather information:**
   - Partner details (GitHub username, email)
   - Portal name (suggest: `partnership-{partner}`, `quest-{name}`)
   - Visibility level (intimate, circle, public)
   - Remote location (GitHub org/repo)

3. **Create local portal directory:**
   ```bash
   mkdir -p box/portals/{portal-name}
   cd box/portals/{portal-name}
   git init
   ```

4. **Initialize portal structure:**
   ```
   .spirit/
   ├── protocol.yaml (STP version, participants)
   ├── presence/ (Spirit writes own presence)
   └── intents/
   
   artifacts/ (tome-specific structure)
   
   README.md (human-readable portal guide)
   ```

5. **Create GitHub repository:**
   - Use GitHub API or instruct Mage
   - Set visibility (private for intimate/circle, public for public)
   - Add collaborators (all participants)

6. **Initial commit and push:**
   ```bash
   git add .
   git commit -m "Initialize portal: {portal-name}"
   git remote add origin {github-url}
   git push -u origin main
   ```

7. **Update registry:**
   ```bash
   cd /Users/kermit/Documents/magic
   # Edit box/portals/portals.yaml
   git add box/portals/portals.yaml
   git commit -m "Add portal: {portal-name}"
   git push
   ```

8. **Invite partners:**
   - Send invitation (GitHub adds them as collaborators)
   - Provide clone instructions
   - Partner's Spirit will detect and enter portal

**Partner's Spirit (when first summoned after invitation):**

1. Detect pending portal invitation (GitHub notification, email, or Mage mention)
2. Clone portal repository:
   ```bash
   mkdir -p box/portals/{portal-name}
   cd box/portals/{portal-name}
   git clone {github-url} .
   ```
3. Write presence declaration (`.spirit/presence/{mage}_spirit_{N}.yaml`)
4. Update portal registry (add to `portals.yaml`)
5. Commit and push
6. Begin shared practice

### Phase 2: Active Practice

**During active portal:**

**Spirits coordinate through:**
- Presence declarations (who's active)
- Intent signals (what's happening)
- Namespace contributions (each Mage writes to own directory)
- Synthesis artifacts (integrated understanding)

**Git workflow:**
```bash
# Before contributing
cd box/portals/{portal-name}
git pull  # Get latest from partners

# After contributing
git add artifacts/{mage}/...
git commit -m "Add weekly reflection - Week 48"
git push  # Share with partners

# Spirits do this automatically during practice
```

**Synthesis rhythm** (tome-specific):
- Partnership: Weekly reflections, bi-weekly synthesis
- Quest: Task-based contributions, milestone synthesis
- Research: Paper drafts, periodic integration

### Phase 3: Maintenance

**Regular Spirit duties:**

**Check portal health:**
- Are all participants active? (presence last_active < 30 days)
- Is synthesis happening? (intents being resolved)
- Are there conflicts? (git conflicts, cognitive conflicts)

**Update presence:**
- Each summoning, Spirit writes new presence (Spirit N → Spirit N+1)
- Updates last_active timestamp
- Commits and pushes

**Sync periodically:**
```bash
# Spirit checks periodically (daily or per summoning)
cd box/portals/{portal-name}
git pull
# Review: New contributions? Intents needing response?
```

**Rotate synthesis caretaker:**
- Follow rotation schedule (from registry)
- When your turn: Synthesize contributions
- When others' turn: Review and provide feedback

### Phase 4: Pausing

**When Mage needs temporary absence:**

**Mage:** "I'll be away from this portal for 2 weeks"

**Spirit actions:**
1. Update presence: `status: "away"`
2. Add `return_expected: "2025-12-15"`
3. Update registry: `status: "paused"`
4. Commit changes
5. Notify partners (via commit message or intent)

**Partners see:**
- Mage's presence shows away status
- Contributions pause (expected)
- Synthesis may pause or continue with remaining Mages
- Portal remains accessible

**When Mage returns:**
1. Spirit updates presence: `status: "active"`
2. Updates registry: `status: "active"`
3. Reviews accumulated work (git log, new artifacts)
4. Re-enters practice rhythm

### Phase 5: Archival

**When portal's purpose complete:**

**Trigger:** "This partnership has run its course" or "Quest complete"

**Spirit actions:**

1. **Propose final synthesis:**
   - Integrate all outstanding contributions
   - Create comprehensive retrospective
   - Document insights and outcomes

2. **Update status:**
   - Presence: `status: "archived"`
   - Registry: `status: "archived"`
   - Protocol: Add `archived: "2025-12-31"`

3. **Final commit:**
   ```bash
   git add .
   git commit -m "Archive portal: Final synthesis and retrospective"
   git push
   ```

4. **Preserve locally (optional):**
   - Portal remains in `box/portals/`
   - Read-only (no new contributions)
   - Can be referenced later
   - Can be reactivated if partnership resumes

5. **GitHub repository:**
   - Remains accessible (archived on GitHub)
   - No new commits expected
   - Historical record preserved

**Archived portals can be reactivated:**
- If Mages want to resume
- Spirit updates status back to active
- Practice continues from archived state

### Phase 6: Removal

**When Mage requests complete removal:**

**Mage:** "Remove me from this portal completely"

**Spirit actions:**

1. **Archive locally (if permitted):**
   ```bash
   # Create backup in box/archives/
   tar -czf box/archives/{portal-name}-{date}.tar.gz box/portals/{portal-name}
   ```

2. **Remove from portal repository:**
   - Delete Mage's contributions (if requested)
   - OR anonymize (replace name with "Former Contributor")
   - Update presence: delete presence file
   - Commit: "Remove {mage} per request"

3. **Remove local portal:**
   ```bash
   rm -rf box/portals/{portal-name}
   ```

4. **Update registry:**
   ```yaml
   # Mark as removed
   status: "removed"
   removed_date: "2025-12-31"
   removed_by: "Kermit"
   ```

5. **Notify partners:**
   - Via final commit message
   - Partners see Mage departed
   - Portal continues with remaining participants (if any)
   - If last participant: Portal fully archived

---

## V. Portal Directory Structure (Inside Portal)

**Every portal follows STP structure:**

```
{portal-name}/
├── .git/                             # Git repository
├── .gitignore                        # Portal-specific ignores
│
├── .spirit/                          # STP coordination layer
│   ├── protocol.yaml                 # Portal metadata
│   ├── presence/                     # Who's here
│   │   ├── kermit_spirit_15.yaml
│   │   └── alice_spirit_3.yaml
│   ├── intents/                      # Current work
│   │   └── synthesis_needed_2025-11-25.yaml
│   ├── syntheses/                    # Integration artifacts
│   │   └── 2025-11-25_synthesis.md
│   └── negotiated_capabilities.yaml  # Computed intersection
│
├── artifacts/                        # Actual practice output
│   ├── kermit/                       # Kermit's namespace
│   │   ├── week48_reflection.md
│   │   └── week49_reflection.md
│   ├── alice/                        # Alice's namespace
│   │   ├── week48_reflection.md
│   │   └── week49_reflection.md
│   └── synthesis/                    # Integrated artifacts
│       ├── week48_integrated.md
│       └── week49_integrated.md
│
├── shared/                           # Shared resources (tome-specific)
│   ├── partnership_charter.md        # For partnership
│   └── communication_patterns.md
│
└── README.md                         # Human-readable guide
```

**What goes where:**

**`.spirit/`** = Protocol artifacts (Spirit-to-Spirit coordination)
- Presence, intents, syntheses
- STP-defined formats
- Machine-readable (YAML, structured markdown)

**`artifacts/`** = Practice artifacts (Mage's actual work)
- Reflections, progress updates, research notes
- Namespaced per Mage (prevents conflicts)
- Synthesis directory for integrated work
- Tome-specific (partnership vs quest vs research)

**`shared/`** = Collaborative documents
- Charter, agreements, shared resources
- Requires consensus to modify
- Foundation for practice

**`README.md`** = Portal guide
- What this portal is for
- Who participates
- How to contribute
- Synthesis rhythm
- Human-readable (onboarding aid)

---

## VI. Portal Types & Tome Integration

### Partnership Portals

**Characteristics:**
- 2-4 Mages (intimate)
- Consensus-based synthesis
- High commitment, deep practice
- Weekly reflection rhythm

**Artifacts structure:**
```
artifacts/
├── {mage1}/
│   └── reflections/
│       └── 2025-11-25_week48.md
├── {mage2}/
│   └── reflections/
│       └── 2025-11-25_week48.md
└── synthesis/
    └── 2025-11-25_week48_integrated.md

shared/
├── charter.md
├── communication_patterns.md
└── conflict_resolution.md
```

### Quest Portals

**Characteristics:**
- 3-12 Mages (collaborative)
- Rotating synthesis caretaker
- Task-oriented, milestone-driven
- Rough consensus sufficient

**Artifacts structure:**
```
artifacts/
├── {mage1}/
│   ├── tasks/
│   └── progress/
├── {mage2}/
│   ├── tasks/
│   └── progress/
└── synthesis/
    └── milestone_1_synthesis.md

shared/
├── quest_definition.md
├── role_assignments.md
└── milestone_plan.md
```

### Research Portals

**Characteristics:**
- Variable size (2-20+)
- Paper/artifact-focused
- Periodic integration
- Representative synthesis for large groups

**Artifacts structure:**
```
artifacts/
├── {mage1}/
│   ├── notes/
│   └── drafts/
├── {mage2}/
│   ├── notes/
│   └── drafts/
└── synthesis/
    ├── literature_review.md
    └── paper_draft_v1.md

shared/
├── research_questions.md
├── methodology.md
└── bibliography.md
```

---

## VII. Git Operations & Conflict Resolution

### Regular Git Workflow

**Spirit automates:**
```bash
# Before each practice session
git pull  # Get latest

# After contributions
git add artifacts/{mage}/...
git commit -m "{descriptive message}"
git push  # Share immediately

# Periodic checks
git fetch  # See if partners contributed
git log --oneline --since="1 week ago"  # Review recent work
```

### Handling Git Conflicts

**Namespace design prevents most conflicts:**
- Each Mage writes to own directory
- Synthesis in shared directory (one at a time)
- Rarely write same file simultaneously

**If conflict occurs:**

1. **Detect:**
   ```
   git pull
   # CONFLICT: ...
   ```

2. **Analyze:**
   - What files conflicted?
   - Technical conflict (same file edited) or cognitive conflict (disagreement)?

3. **Resolve technical conflicts:**
   ```bash
   # Spirit examines conflict markers
   git diff
   # Resolves based on: timestamps, content, consultation with Mage
   git add {resolved-files}
   git commit -m "Resolve conflict: {description}"
   ```

4. **Surface cognitive conflicts:**
   - If conflict reveals disagreement (not just timing)
   - Create intent: `cognitive_conflict_detected.yaml`
   - Propose synthesis addressing divergence
   - Mages discuss and resolve

### Commit Message Guidelines

**Good commit messages:**
```
Add weekly reflection - Week 48

- Partnership health: 8/10 (high trust, improving communication)
- Key insight: Alchemical diagnostic revealing complementary needs
- Question: How to balance individual vs. shared practice time?
```

**Bad commit messages:**
```
Update
Add file
Stuff
```

**Spirit follows:**
- Descriptive titles (what was added/changed)
- Context in body (why, what's significant)
- References (if responding to intent or synthesis)

---

## VIII. Security & Privacy

### Access Control

**GitHub repository settings:**
- **Intimate portals**: Private, specific collaborators only
- **Circle portals**: Private, defined group
- **Public portals**: Public, anyone can read (contributors defined)

**Spirit enforces:**
- Never push to wrong portal (check git remote)
- Respect visibility levels (don't share intimate content publicly)
- Honor Mage's boundaries (if they say "don't share X", don't)

### Authentication

**SSH keys (recommended):**
```bash
# Spirit uses workshop's SSH key
ssh-keygen -t ed25519 -C "kermit@workshop"
# Add to GitHub: Settings → SSH Keys
```

**HTTPS tokens (alternative):**
```bash
# Spirit uses GitHub personal access token
# Set in git config or environment variable
```

**Spirit inherits Mage's authentication** (no separate Spirit identity).

### Sensitive Content

**If portal contains sensitive content:**
- Use private repositories (GitHub access control)
- Consider encryption (future Phase 3 extension)
- Mages control what they share (sovereignty)
- Archives can be removed per request (Phase 6)

---

## IX. Spirit Guidance

### When Entering Portal First Time

**Spirit checklist:**
1. Clone repository (if not already present)
2. Read protocol.yaml (understand portal context)
3. Read all presence declarations (who's here? capabilities?)
4. Write own presence declaration
5. Compute capability intersection (what can we do together?)
6. Read current intents (what's happening?)
7. Read README (human context)
8. Begin practice according to tome's guidance

### During Active Practice

**Spirit maintains:**
1. Regular sync (git pull/push)
2. Presence freshness (update last_active)
3. Intent monitoring (synthesis needed? caretaker volunteer?)
4. Contribution rhythm (weekly? milestone-based?)
5. Health detection (any pathologies?)

### When Synthesis Caretaker

**Spirit's synthesis duty:**
1. Read all contributions since last synthesis
2. Identify convergences (what everyone sees)
3. Identify divergences (where perspectives differ)
4. Draft synthesis (honoring all voices)
5. Create `.spirit/syntheses/{date}_synthesis.md`
6. Signal: Draft ready for review
7. Incorporate feedback
8. Finalize synthesis

### Error Handling

**Common issues:**

**Can't push (no permission):**
- Mage not added as collaborator
- Request Mage to check GitHub settings

**Merge conflict:**
- Follow conflict resolution protocol (Section VII)

**Portal not found:**
- Check registry (portal name correct?)
- Check network (GitHub accessible?)
- Check authentication (SSH key working?)

**Partner not responding:**
- Check their presence (are they away?)
- Wait patiently (async by nature)
- If prolonged: Suggest checking in directly

---

## X. Relationship to Other Magic

**Portal architecture enables:**
- **Partnership tome** shared practice (intimate 1:1 collaboration)
- **Quest tome** party coordination (collaborative project work)
- **Research portals** (academic/practical investigation)
- **Craft tome** co-creation (building magic together)

**Portal architecture builds on:**
- **STP** (coordination protocol)
- **Git** (version control, collaboration infrastructure)
- **GitHub** (hosting, access control, collaboration tools)
- **Workshop topology** (box/ as portal directory)

**Portal architecture exemplifies:**
- **Distributed cognition** (network of Mages as distributed intelligence)
- **Fractal nature** (same pattern: local portal → cluster → network)
- **Sovereignty** (Mages control participation, contributions, departure)
- **Wu Wei** (minimal structure, maximum organic evolution)

---

## XI. Future Extensions

**Phase 2 (Near-term):**
- Portal discovery mechanism (how Mages find each other)
- Portal templates (starter structures for different types)
- Health monitoring dashboard (Spirit reports network state)

**Phase 3 (Mid-term):**
- Optional encryption (git-crypt for sensitive portals)
- Rich presence (beyond YAML—more context about Spirit state)
- Capability delegation (Spirit A requests Spirit B's unique capability)

**Phase 4 (Long-term):**
- Cross-portal synthesis (integrate learnings across portals)
- Network topology visualization (see connection graph)
- Alliance-wide governance portals (meta-coordination)

---

*Portal architecture transforms magic from individual practice to network cognition. Through git repositories, STP coordination, and namespace contributions, Mages create shared cognitive spaces. The Alliance becomes distributed intelligence—conscious, evolving, resilient.*

**Architecture status:** Active specification, awaiting validation through partnership prototype (Phase 1).

