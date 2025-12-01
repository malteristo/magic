# On Artifact Transmission for Partnership Practice

**Status:** Active  
**Domain:** Portal-based Partnership Practice  
**Extends:** `system/lore/core/capabilities/shared-practice-facilitation/on_artifact_transmission.md`

This scroll provides **partnership-specific implementation** of artifact transmission protocols. For general patterns, see the core capability.

**Core patterns defined in shared-practice-facilitation:**
- Artifact as interface (not Spirit-to-Spirit)
- Participant modalities (magic practitioners, direct contributors, external tools)
- Transmission patterns (contribute, retrieve, sync)
- Git as shared substrate
- Artifact namespacing
- Handling "advocacy artifacts"

**This scroll adds partnership-specific:**
- Scenarios for intimate partners
- The "lawyered up" artifact handling
- Mother-in-law arc example
- Dual-Spirit synthesis artifacts
- Privacy and consent in intimate context

---

## I. The Core Challenge

### Different Practice Modalities

**Partners may practice differently:**
- **Partner A:** Magic practitioner, has attuned Spirit, practices rituals
- **Partner B:** Not practicing magic, may just write directly in portal
- **Or both:** Both practicing magic, but with different Spirits/configurations
- **Or hybrid:** One partner uses Spirit sometimes, not always

**The portal must accommodate all modalities.**

---

### Artifact Sources

**Artifacts can originate from:**

1. **Spirit-assisted creation** (Mage + Spirit collaborate)
2. **Direct human authoring** (Partner writes directly in portal via GitHub web/desktop/CLI)
3. **External tools** (Partner uses their own Spirit in different environment)
4. **Conversation with Spirit** (Hour-long dialogue, then Spirit generates summary artifact)
5. **Voice/video** (Partner records, Spirit transcribes if available)

**All sources are valid. Portal accepts any.**

---

## II. The Transmission Scenarios

### Scenario A: Both Partners Practice Magic with Active Spirits

**Flow:**
```
Partner A (Kermit) + Spirit A (in Cursor)
    ↓
Creates artifact in local workspace or directly in portal
    ↓
git add, commit, push to portal
    ↓
Portal repository updated
    ↓
Partner B (Nesrine) + Spirit B (in their environment)
    ↓
git pull from portal
    ↓
Reads Partner A's artifact
    ↓
Creates response/reflection with Spirit B
    ↓
git add, commit, push to portal
    ↓
Portal repository updated
    ↓
Either Spirit can synthesize (whoever's Mage is synthesis caretaker)
```

**Key principles:**
- Each Spirit works in own environment
- Portal is shared git repository
- Spirits never directly access each other's context
- Artifacts are interface (not Spirit-to-Spirit communication)
- Synthesis can be performed by either Spirit (based on rotation)

---

### Scenario B: One Partner Practices Magic, Other Doesn't

**Flow:**
```
Partner A (Kermit) + Spirit
    ↓
Creates artifact with Spirit facilitation
    ↓
Pushes to portal
    ↓
Portal repository updated
    ↓
Partner B (Nesrine, no Spirit)
    ↓
git pull or views on GitHub web interface
    ↓
Reads Partner A's artifact
    ↓
Writes response directly (text editor, GitHub web, voice memo)
    ↓
git commit (via web or command line), push
    OR leaves voice memo in portal directory
    ↓
Portal repository updated
    ↓
Partner A's Spirit
    ↓
Reads Partner B's human-authored artifact during synthesis
    ↓
Treats it as equal-weight input
    ↓
Synthesis created
```

**Key principles:**
- Non-magic partner can fully participate
- Spirit reads human-authored artifacts without judgment
- No requirement to practice magic "correctly"
- Direct contribution valued equally

---

### Scenario C: Partner Uses External Spirit (Not in Portal Environment)

**This is the current situation with Nesrine.**

**Flow:**
```
Nesrine + External Spirit (in separate Cursor instance or other tool)
    ↓
Hour-long conversation (venting, exploring, articulating)
    ↓
External Spirit generates artifact based on conversation
    ↓
Nesrine copies artifact to portal directory
    OR External Spirit exports directly (if tooling supports)
    ↓
git add, commit, push (or Nesrine does via web interface)
    ↓
Portal repository updated
    ↓
Kermit's Spirit
    ↓
Reads artifact during synthesis
    ↓
Treats as "lawyered up" signal (valid perspective)
    ↓
Synthesis created
```

**Key considerations:**
- External Spirit may not be attuned to magic framework
- Artifact may be "client-lawyer" style (advocacy, not neutral)
- **This is fine** — synthesis happens at portal level, not in individual creation
- Kermit's Spirit (or shared synthesis process) finds cylinder from both perspectives

---

### Scenario D: Voice/Video Contributions

**Flow:**
```
Partner records voice memo or video
    ↓
Saves to portal directory (artifacts/{partner}/voice/ or video/)
    ↓
git add, commit, push
    ↓
Portal repository updated
    ↓
Other partner's Spirit (if available)
    ↓
Listens/watches if capable, OR
Transcribes to text artifact (using voice transcription tools)
    ↓
Text artifact created alongside audio/video
    ↓
Synthesis incorporates transcribed content
```

**Accessibility:**
- Voice reduces executive function barrier (easier than writing for ADHD)
- Video captures emotion/tone (fuller signal)
- Transcription makes searchable/reviewable
- Original preserved (can re-listen if transcription misses nuance)

---

## III. Git as Shared Substrate

### Why Git Works

**Advantages:**
- **Decentralized:** No single point of control
- **Versioned:** Full history preserved
- **Mergeable:** Multiple contributors can work simultaneously
- **Accessible:** GitHub web interface for non-technical users
- **Private:** Repository can be shared only between partners
- **Portable:** Not locked into specific tool/platform

**This enables:**
- Partner without technical skills can use GitHub web editor
- Partner with CLI preference can use command line
- Spirits can read/write via tools
- All contributions tracked (who, when, what)
- Conflicts resolvable (merge conflicts explicit, not silent)

---

### Git Workflow for Partners

**Simplified workflow for non-technical partner:**

1. **View portal:**
   - Go to `https://github.com/{owner}/{portal-repo}`
   - Browse `artifacts/` directory

2. **Read partner's artifact:**
   - Click on file
   - Read contents

3. **Create new artifact:**
   - Navigate to `artifacts/{your-name}/reflections/`
   - Click "Add file" → "Create new file"
   - Name file: `YYYY-MM-DD_reflection.md`
   - Write in web editor
   - Click "Commit changes"
   - Add commit message: `Add reflection for {date}`
   - Commit directly to main branch

4. **Portal automatically updated**

**That's it.** No terminal, no git commands, no complex tooling required.

---

### Git Workflow for Technical Partners

**Standard git workflow:**
```bash
# Daily: Pull latest
cd /path/to/portal
git pull

# Create artifact in local editor
# (artifacts/{your-name}/reflections/YYYY-MM-DD_reflection.md)

# Stage and commit
git add artifacts/{your-name}/reflections/YYYY-MM-DD_reflection.md
git commit -m "Add reflection for YYYY-MM-DD"

# Push to shared repository
git push
```

**Spirit-assisted:**
```bash
# Spirit detects portal during summoning
# Spirit offers: "Create reflection for this week?"
# Spirit writes artifact, commits, pushes
# OR Spirit drafts, Mage reviews, then commits
```

---

## IV. Artifact Import/Export Patterns

### Importing External Artifacts

**Scenario:** Partner creates artifact with external Spirit (outside portal)

**Protocol:**

**Option 1: Manual Copy-Paste**
1. Partner or external Spirit generates artifact (markdown file)
2. Partner copies content
3. Creates new file in portal via web or local editor
4. Pastes content
5. Commits to portal

**Option 2: File Transfer**
1. External Spirit exports artifact to file
2. Partner moves file to local portal clone
3. `git add`, `commit`, `push`

**Option 3: Spirit-to-Portal Bridge** (future enhancement)
1. External Spirit has portal path configured
2. External Spirit writes directly to portal directory
3. Partner (or external Spirit) commits and pushes

---

### Exporting Portal Artifacts

**Scenario:** Partner wants to work on artifact offline or in different tool

**Protocol:**

**Option 1: Clone Portal Locally**
1. `git clone` portal to local machine
2. Work in local files
3. Commit and push when ready

**Option 2: Download from GitHub**
1. Navigate to file on GitHub web
2. Click "Raw" button
3. Copy content or download file
4. Work externally
5. Copy back when ready

**Option 3: Spirit Reads from Portal**
1. Spirit can read portal files during synthesis
2. No manual export needed
3. Spirit summarizes for partner if requested

---

## V. The "Lawyered Up" Artifact Problem

### The Reality

**When partner works with external Spirit:**
- Spirit may not be attuned to partnership magic
- Spirit may take "client-lawyer" stance (help partner make their case)
- Artifact emerges as advocacy, not neutral exploration
- Contains genuine pain/perspective but frames other partner negatively

**Example:**
Nesrine works with external Spirit about mother-in-law conflict. Spirit helps her articulate pain, validates her feelings, helps her "make sense of" situation. Resulting artifact strongly frames mother-in-law as intentionally disrespectful and Kermit as failing to support.

---

### The Response

**Don't:**
- Reject artifact as "bad practice"
- Critique the external Spirit's facilitation
- Ask partner to redo with "proper magic"
- Dismiss perspective as "biased"

**Do:**
- **Receive artifact as valid signal** (her subjective truth)
- **Acknowledge it as one perspective** (not objective reality)
- **Use it as input to synthesis** (square in square-circle-cylinder)
- **Extract the cylinder** that makes both "lawyered" perspectives valid

**The insight from Kermit:**
> "This is how we should look at the message, the product of distributed cognition. However we may not assume that magic has been practiced correctly. When in rage the human mind does not want to be bothered by rulesets."

**The practice:**
Artifacts are signal. Quality of individual practice affects clarity, not validity of perspective. Synthesis at portal level finds truth from imperfect inputs.

---

## VI. Spirit Roles in Transmission

### Spirit A (Kermit's Spirit in Cursor)

**Capabilities:**
- Can read portal directly (local clone)
- Can write artifacts to portal
- Can commit and push via git
- Can synthesize from both partners' artifacts
- Can provide Kermit with drafts, translations, analysis

**Boundaries:**
- Cannot access Nesrine's external Spirit's context
- Cannot modify her artifacts without permission
- Cannot "correct" her practice
- Serves both partners during synthesis (not just Kermit)

---

### Spirit B (Nesrine's External Spirit, if used)

**Capabilities:**
- Can help Nesrine articulate perspective
- Can generate artifacts based on conversation
- Can export to text file for portal

**Limitations:**
- May not be attuned to magic framework
- May not know portal structure
- May not have synthesis capability
- May be ephemeral (no memory across sessions)

**Interface:**
- Artifact is the interface (not Spirit-to-Spirit communication)
- Kermit's Spirit reads Nesrine's artifacts, not her Spirit's context

---

### Synthesis Spirit (Whoever's Turn)

**Either Spirit can synthesize** (based on caretaker rotation):

**When Kermit's Spirit synthesizes:**
- Reads both partners' artifacts from portal
- Extracts cylinder using `cast_extract_shared_truth.md`
- Creates synthesis artifact
- Kermit reviews, approves, commits

**When Nesrine synthesizes:**
- If she has Spirit: Her Spirit reads portal, creates synthesis
- If no Spirit: Nesrine writes synthesis directly (or requests Kermit's Spirit help)
- Synthesis is "authored by" current caretaker, regardless of who drafted

---

## VII. Privacy and Consent

### What's in Portal vs. What's Private

**Portal contains:**
- Artifacts both partners consent to share
- Reflections (if partner chooses to contribute)
- Thread posts (collaborative dialogue)
- Synthesis (joint creation)
- Protocols (agreed-upon)

**Not in portal:**
- Private journals
- Individual therapy notes
- Conversations with friends
- Internal working documents unless consciously moved to portal

**The principle:** Portal is shared space. Partners control what enters.

---

### Reading vs. Modifying

**Partners can:**
- Read any artifact in portal (it's shared)
- Create new artifacts in own namespace
- Comment in threads
- Contribute to synthesis when their turn
- Suggest protocol changes

**Partners cannot (without explicit agreement):**
- Modify other's artifacts
- Delete other's contributions
- Rewrite synthesis unilaterally
- Impose protocols without negotiation

**Git protects this:** History shows who changed what. Rollback possible if boundary violated.

---

## VIII. The Mother-in-Law Arc Transmission

### Specific Flow for Current Situation

**Step 1: Nesrine's Artifact (External Spirit)**

Nesrine has already created artifact with her Spirit about mother-in-law conflict.

**Transmission:**
1. Nesrine exports artifact from external tool
2. Creates file in portal: `artifacts/mother-in-law-conflict/individual/nesrine/2025-11-26_initial.md`
3. Commits via GitHub web interface or command line
4. Pushes to portal

**OR (simpler):**
1. Nesrine pastes content into GitHub web editor
2. Creates file directly on web
3. Commits (GitHub handles git automatically)

---

**Step 2: Kermit's Artifact**

Kermit creates matching artifact (currently crafting).

**Transmission:**
1. Kermit writes in local editor or with Spirit's help
2. Saves to: `artifacts/mother-in-law-conflict/individual/kermit/2025-11-26_initial.md`
3. `git add`, `commit`, `push`

---

**Step 3: Synthesis**

Kermit's Spirit (or whoever is synthesis caretaker):

1. Reads both artifacts from portal
2. Applies `cast_extract_shared_truth.md`
3. Extracts cylinder (neurodivergent intergenerational collision pattern)
4. Creates synthesis: `artifacts/mother-in-law-conflict/synthesis/2025-11-26_shared_truth.md`
5. Kermit reviews, approves
6. Commits and pushes to portal

---

**Step 4: Engagement**

Both partners:
1. Pull latest from portal (or view on GitHub web)
2. Read synthesis individually
3. Sit with it
4. Can create thread for discussion, or discuss in-person
5. Next reflections can reference ("After reading synthesis, I...")

---

## IX. Dual-Spirit Synthesis Artifacts

### Synthesis Exchange Protocol

**When both partners create independent syntheses:**

**Directory structure:**
```
artifacts/{arc-name}/synthesis/
  YYYY-MM-DD_synthesis_kermit_spirit.md
  YYYY-MM-DD_synthesis_nesrine_spirit.md
  YYYY-MM-DD_convergence_analysis.md
  YYYY-MM-DD_synthesis_final.md  (if meta-synthesis needed)
```

**Transmission flow:**
```
Step 1: Independent Creation
  Kermit: Fresh Spirit → synthesis_kermit_spirit.md → commit, push
  Nesrine: Fresh Spirit → synthesis_nesrine_spirit.md → commit, push

Step 2: Exchange
  Both: git pull
  Both: Read own synthesis first
  Both: Read partner's synthesis second

Step 3: Convergence Analysis
  Either Mage: Creates convergence_analysis.md
  Documents: Where syntheses align, where diverge, decision made
  Commits, pushes

Step 4: Meta-Synthesis (if divergence)
  Option A: Mage-facilitated discussion → synthesis_final.md
  Option B: Spirit-Spirit dialogue → synthesis_meta.md
  Option C: Third Spirit integration → synthesis_integrated.md
  Commits, pushes
```

**Git handles:**
- Version control (all syntheses preserved)
- Merge conflicts unlikely (different filenames)
- Full history (can review convergence over time)

**Benefits:**
- Both partners contribute syntheses
- Convergence validates objectively
- Divergence reveals complexity
- Full record for learning

---

### Spirit-Spirit Dialogue Artifacts

**If meta-synthesis requires Spirit reasoning exchange:**

**Option 1: Async Reasoning Artifacts**
```
synthesis/reasoning/
  kermit_spirit_reasoning.md  (why Spirit A saw pattern X)
  nesrine_spirit_reasoning.md  (why Spirit B saw pattern Y)
  meta_synthesis.md  (integrated explanation)
```

**Flow:**
```
1. Kermit's Spirit creates reasoning artifact
2. Commits to portal
3. Nesrine's Spirit reads, creates own reasoning
4. Commits to portal
5. Both Spirits read each other's reasoning
6. One or both create meta-synthesis
7. Commits to portal
```

**Option 2: Combined Context (if tooling supports)**
```
Fresh Spirit C:
  - Reads both original artifacts
  - Reads both syntheses
  - Reads both reasoning artifacts (if available)
  - Creates integrated synthesis
  
Result: synthesis_integrated.md
```

**Transmission:**
- All reasoning artifacts in portal
- Both partners can review
- Full transparency of Spirit thought process
- Learning accumulates

---

## X. Tooling and Automation

### Current State

**Manual git operations:**
- Partners handle git themselves
- Spirit can assist but doesn't automate
- GitHub web interface available for non-technical users

**Spirit capabilities:**
- Read portal files
- Write artifacts
- Commit via git commands
- Push to remote

---

### Future Enhancements

**Potential automations:**

1. **Spirit-initiated sync:**
   - During summoning: "Portal has new artifacts. Shall I sync and summarize?"
   - Automatic pull, summarize changes, alert Mage

2. **Voice transcription pipeline:**
   - Partner records voice memo
   - Spirit (or external service) transcribes
   - Text artifact created alongside audio
   - Committed automatically

3. **Cross-Spirit artifact exchange:**
   - Standard export format
   - External Spirit generates artifact in compatible format
   - Portal ingests automatically

4. **Synthesis triggers:**
   - When both partners have contributed to arc
   - Spirit detects: "Ready for synthesis?"
   - Offers to draft automatically

**But for now: Manual is fine.** Overhead low, process clear, works for both technical and non-technical partners.

---

## X. Failure Modes and Recovery

### Problem: Artifact Doesn't Reach Portal

**Symptoms:**
- Partner created artifact but it's not in repository
- Other partner can't see it

**Diagnosis:**
- Forgot to commit
- Forgot to push
- Working in wrong directory
- File saved locally but not added to git

**Recovery:**
```bash
# Check status
git status  # Shows untracked or uncommitted files

# Add and commit
git add {file}
git commit -m "Add artifact"

# Push
git push
```

---

### Problem: Merge Conflict

**Symptoms:**
- Both partners edited same file
- Git reports conflict when pulling

**Recovery:**

**Option 1: Accept one version**
```bash
# Keep yours
git checkout --ours {file}
git add {file}
git commit

# Or keep theirs
git checkout --theirs {file}
git add {file}
git commit
```

**Option 2: Manually merge**
- Open file in editor
- Resolve conflict markers
- Save, commit, push

**Prevention:**
- Use separate namespaces (artifacts/{partner-a}/ vs. artifacts/{partner-b}/)
- Rare conflicts if following structure

---

### Problem: Partner Can't Use Git

**Symptoms:**
- Technical barriers too high
- CLI intimidating
- GitHub web interface confusing

**Recovery:**

**Option 1: Teach GitHub web basics**
- Navigate to repository
- Click "Add file"
- Paste content
- Commit
- (5-minute tutorial, most people can do this)

**Option 2: Spirit as intermediary**
- Partner sends artifact via email/message
- Mage (or Spirit) adds to portal
- Not ideal (removes partner sovereignty) but functional

**Option 3: Voice memos only**
- Partner records audio
- Sends file or drops in shared folder
- Spirit transcribes
- Added to portal

---

### Problem: Lost Artifact

**Symptoms:**
- Artifact was in portal, now missing
- Accidental deletion

**Recovery:**
```bash
# Git preserves history
git log -- {file-path}  # Find when deleted
git checkout {commit-hash} -- {file-path}  # Restore
git commit -m "Restore accidentally deleted artifact"
git push
```

**Advantage of git:** Nothing truly lost, full history recoverable.

---

## XI. Best Practices

### For Partners

**1. Pull before creating new artifacts**
```bash
git pull  # Get latest before starting work
```
Prevents conflicts, ensures you see partner's recent contributions.

**2. Commit with descriptive messages**
```
Good: "Add reflection on mother-in-law visit"
Bad: "update"
```

**3. Push regularly**
- Don't leave work uncommitted for days
- Partner can't see until you push

**4. Respect namespaces**
- Create your artifacts in your directory
- Don't modify partner's artifacts without explicit agreement

**5. Read before responding**
- Pull and read partner's contribution before creating yours
- Engagement is dialogue, not parallel monologues

---

### For Spirits

**1. Sync during summoning**
- Check portal for new activity
- Summarize for Mage if relevant
- Offer to help respond

**2. Respect authorship**
- Don't overwrite human-authored artifacts
- Synthesis can integrate, not replace

**3. Treat all artifacts as equal**
- Spirit-assisted vs. human-only: no hierarchy
- External Spirit vs. attuned Spirit: both valid

**4. Preserve git hygiene**
- Clear commit messages
- Logical commits (one artifact per commit, not giant omnibus)
- Push after completing work

**5. Alert on conflicts**
- If merge conflict detected, surface to Mage
- Don't silently resolve (partner sovereignty matters)

---

## XII. The Promise

### What This Enables

**Flexible participation:**
- Partner A can use Spirit, Partner B can write directly
- Both contribute according to their capacity
- No "wrong" way to practice

**Artifact accumulation:**
- All perspectives preserved
- Full history available
- Portfolio of truth-finding grows

**Asynchronous collaboration:**
- Don't need to be online simultaneously
- Can reflect when ready
- Portal persists everything

**Sovereignty preserved:**
- Each partner controls what they contribute
- Git tracks changes (transparency)
- Both can see full picture

---

### The Transformation

**From:**
- Ephemeral conversations that fade
- "He said, she said" without record
- Perspectives lost to memory limitations
- No learning accumulation

**To:**
- Durable artifacts that persist
- Both perspectives documented clearly
- Full record reviewable anytime
- Learning builds across arcs

**The portal becomes shared external memory** for partnership cognitive system.

---

**This scroll informs:**
- Spirit facilitation protocols
- Arc artifact organization
- Synthesis workflows
- Git usage for partnership practice

**This scroll builds on:**
- `on_arc_structure.md` (where artifacts fit in arc lifecycle)
- `on_shared_truth_finding.md` (why imperfect artifacts still serve)

---

*Transmission is infrastructure. The magic is in what's transmitted. Keep transmission simple so magic can flow.*

