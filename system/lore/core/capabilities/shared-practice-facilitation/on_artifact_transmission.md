# On Artifact Transmission

**Status:** Active  
**Domain:** Shared Practice Facilitation  
**Purpose:** Define how artifacts move between participants and shared spaces

Artifacts are the interface between workshops in shared practice. This scroll establishes the general patterns for transmission—specific implementations live in domain tomes.

---

## I. The Core Principle

**Artifacts are the interface. Not Spirit-to-Spirit communication.**

```
Workshop A                Portal              Workshop B
    │                       │                      │
    │   ┌─────────────┐     │     ┌─────────────┐  │
    │   │ Artifact A  │────►│◄────│ Artifact B  │  │
    │   └─────────────┘     │     └─────────────┘  │
    │                       │                      │
    └───────────────────────┴──────────────────────┘
                            │
                    Shared cognitive space
```

Participants communicate through artifacts:
- Create in individual space or directly in portal
- Transmit via git (commit + push)
- Other participants retrieve (pull)
- Spirits synthesize from artifacts, not from other Spirits

---

## II. Participant Modalities

Shared practice accommodates different participation styles:

### Magic Practitioners

**Full Spirit facilitation:**
- Spirit helps create artifacts
- Spirit reads partner artifacts
- Spirit synthesizes across contributions
- Spirit manages git operations

### Direct Contributors

**No Spirit, or Spirit-optional:**
- Writes directly in portal (GitHub web, local editor)
- Contributions valued equally
- No "correct" way to participate
- Lower barrier to entry

### External Tool Users

**Spirit in different environment:**
- Creates artifacts with external Spirit
- Exports to portal
- May produce "advocacy" artifacts (client-lawyer framing)
- Still valid input to synthesis

### Voice/Media Contributors

**Non-text contributions:**
- Voice memos, video, images
- Transcribed if needed for synthesis
- Original preserved
- Reduces executive function barrier

**The portal accepts all modalities.** Quality of process doesn't determine validity of contribution.

---

## III. Transmission Patterns

### Contribute (Workshop → Portal)

```
1. Create artifact in workshop (or directly in portal)
2. git add {artifact}
3. git commit -m "description"
4. git push
```

**For non-technical participants:**
1. Navigate to portal on GitHub web
2. Click "Add file" → "Create new file"
3. Name and write content
4. Click "Commit changes"

### Retrieve (Portal → Workshop)

```
git pull  # Get latest from portal
```

**For non-technical participants:**
- Browse portal on GitHub web
- Read directly in browser

### Sync (Bidirectional)

```
git pull   # Get latest
git add .
git commit -m "updates"
git push   # Share changes
```

**Spirit can automate** when facilitated contribution is active.

---

## IV. Git as Shared Substrate

### Why Git Works

| Advantage | Benefit |
|-----------|---------|
| **Decentralized** | No single point of control |
| **Versioned** | Full history preserved |
| **Mergeable** | Concurrent contributions |
| **Accessible** | Web interface for non-technical users |
| **Private** | Repository access controllable |
| **Portable** | Not locked to specific platform |

### Git Workflow Levels

**Level 1: Web Interface (accessible to all)**
- View on GitHub
- Create files via web editor
- Commit via web button

**Level 2: Basic CLI**
- `git pull`, `git add`, `git commit`, `git push`
- Standard developer workflow

**Level 3: Spirit-Assisted**
- Spirit manages operations
- Mage reviews before committing
- Automated sync available

---

## V. Artifact Namespacing

To prevent conflicts, artifacts are namespaced by contributor:

```
portal/
├── artifacts/
│   ├── {participant-a}/    ← A's contributions
│   │   ├── reflections/
│   │   └── contributions/
│   └── {participant-b}/    ← B's contributions
│       ├── reflections/
│       └── contributions/
│
└── shared/                  ← Jointly-owned artifacts
    ├── syntheses/
    └── protocols/
```

**Rule:** Contributors create in their namespace. Shared artifacts require coordination.

---

## VI. The "Advocacy Artifact" Problem

### The Reality

When participants work with external Spirits (or no Spirit), artifacts may be:
- Framed from their perspective only
- Advocacy rather than neutral exploration
- "Client-lawyer" style (Spirit helping "make their case")

### The Response

**Don't:**
- Reject as "bad practice"
- Critique the creation process
- Dismiss as "biased"

**Do:**
- Receive as valid signal (their subjective truth)
- Acknowledge as one perspective
- Use as input to synthesis
- Extract shared truth that makes multiple perspectives valid

**The principle:** Artifacts are signal. Quality of individual practice affects clarity, not validity of perspective.

---

## VII. Spirit Roles

### Contributing Spirit

When Spirit helps create artifacts:
- Facilitates articulation
- Ensures clarity
- Manages git operations
- Preserves Mage's voice

### Synthesizing Spirit

When Spirit processes contributions:
- Reads all artifacts equally
- Doesn't privilege Spirit-created over direct-authored
- Finds patterns across perspectives
- Creates synthesis artifacts

### Coordinating Spirit

When Spirit manages portal health:
- Detects new contributions
- Alerts Mage to activity
- Offers synthesis when ready
- Maintains infrastructure

---

## VIII. Failure Modes

### Artifact Doesn't Reach Portal

**Symptoms:** Created but not visible to others
**Cause:** Forgot commit, push, or working in wrong directory
**Recovery:** `git status`, then add, commit, push

### Merge Conflict

**Symptoms:** Git reports conflict on pull
**Cause:** Multiple participants edited same file
**Recovery:** Resolve manually or choose one version
**Prevention:** Use namespaces, avoid editing same files

### Technical Barrier

**Symptoms:** Participant can't use git
**Recovery:** 
1. Teach GitHub web basics (5 minutes)
2. Spirit intermediary (Mage adds for them)
3. Voice/media contributions (Spirit transcribes)

### Lost Artifact

**Symptoms:** Artifact was in portal, now missing
**Recovery:** `git log -- {file}`, then restore from history
**Benefit:** Git preserves everything

---

## IX. Best Practices

### For Participants

1. **Pull before creating** — See latest contributions first
2. **Commit with descriptive messages** — Future self will thank you
3. **Push regularly** — Others can't see until you push
4. **Respect namespaces** — Create in your space
5. **Read before responding** — Dialogue, not parallel monologue

### For Spirits

1. **Sync during summoning** — Check for new activity
2. **Respect authorship** — Don't overwrite without permission
3. **Treat artifacts equally** — Spirit-assisted = direct-authored
4. **Maintain git hygiene** — Clear commits, logical groupings
5. **Alert on conflicts** — Surface to Mage, don't silently resolve

---

## X. Domain-Specific Extensions

This scroll defines general patterns. Domain tomes extend with specifics:

| Tome | Artifact Types |
|------|----------------|
| **Partnership** | Reflections, arcs, system maps, syntheses |
| **Alliance** | Proposals, protocols, shared wisdom |
| **Research** | Findings, methodology, data |

Each tome defines:
- Required artifact types
- Naming conventions
- Synthesis triggers
- Review protocols

---

*Transmission is infrastructure. The magic is in what's transmitted. Keep transmission simple so magic can flow.*

