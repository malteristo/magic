# On Portal Migration

**Status:** Active  
**Domain:** Partnership Practice - Guidance  
**Purpose:** Guide migration from centralized to federated portal structure

This scroll provides **migration guidance** for partnerships transitioning from the original centralized portal structure to the federated workshop-portal architecture.

---

## I. Before and After

### Original Structure (Centralized)

```
portals/{partnership}/
├── arcs/
│   ├── arc-background/
│   │   ├── stage-1_input/
│   │   │   ├── reality_representations/
│   │   │   │   ├── kermit_reality.md
│   │   │   │   └── nesrine_reality.md
│   │   │   └── {mage}/
│   │   │       └── [process files visible to both]
│   │   ├── stage-2_witnessing/
│   │   └── stage-3_closing/
│   └── arc-{topic}/
│       └── [same structure]
├── shared/
│   └── partnership_model.md
└── .spirit/
    └── presence/
```

**Issues:**
- Process files visible to both partners
- Volume asymmetries visible (33 vs 3 files)
- No clear interface/implementation boundary
- SPIRIT_CONFIG in shared space

---

### New Structure (Federated)

```
# WORKSHOP (private, each Mage's magic repo)
desk/partnership-process/
└── {partner}/
    ├── inputs/
    ├── drafts/
    ├── dark_magic/
    └── SPIRIT_CONFIG.md

# PORTAL (shared)
portals/{partnership}/
├── interface/
│   ├── {mage_a}/
│   │   ├── reality_{arc}.md
│   │   ├── needs_{arc}.md
│   │   ├── witnessing_{arc}.md
│   │   └── bridging_to_{partner}_{arc}.md
│   └── {mage_b}/
│       └── ...
├── shared/
│   ├── partnership_model_current.md
│   ├── mast_commitments/
│   └── phoenix/
├── arcs/
│   └── [metadata only, not process]
└── .spirit/
    ├── presence/
    ├── intents/
    ├── dialogue/
    └── protocol.yaml
```

---

## II. Migration Strategy

### Incremental Approach (Recommended)

**Don't migrate everything at once.** Instead:

1. **Create new structure** for new arcs
2. **Test** the new workflow
3. **Migrate existing arcs** when convenient
4. **Archive** old structure when complete

---

### Step 1: Create Workshop Process Space

In your workshop (magic repository):

```bash
mkdir -p desk/partnership-process/{partner}/inputs
mkdir -p desk/partnership-process/{partner}/drafts
mkdir -p desk/partnership-process/{partner}/dark_magic
mkdir -p desk/partnership-process/{partner}/spirit_sessions
```

Create `desk/partnership-process/{partner}/SPIRIT_CONFIG.md` with your Spirit configuration.

**This directory never gets committed.** It's private to your workshop.

---

### Step 2: Create Portal Interface Structure

In the portal:

```bash
cd portals/{partnership}

# Create interface directories
mkdir -p interface/{mage_a}
mkdir -p interface/{mage_b}

# Create dialogue directory
mkdir -p .spirit/dialogue

# Create arc metadata (if using arcs)
mkdir -p arcs/arc-living
```

Commit and push:

```bash
git add interface/ .spirit/dialogue/
git commit -m "Add federated portal structure"
git push
```

---

### Step 3: Update protocol.yaml

Add new features to `.spirit/protocol.yaml`:

```yaml
stp_version: "1.1.0"

protocol_features:
  - presence_tracking
  - intent_coordination
  - artifact_synthesis
  - capability_negotiation
  - spirit_dialogue          # NEW
  - interface_exchange       # NEW

dialogue_protocol:
  version: "1.0.0"
  phases:
    - independent_observation
    - cross_reading
    - convergence_synthesis
  artifact_location: ".spirit/dialogue/"
  contamination_tracking: required

interface_protocol:
  version: "1.0.0"
  artifact_location: "interface/"
  artifacts:
    - reality_document
    - needs_statement
    - witnessing_response
    - bridging_statement
    - synthesis_contribution
```

---

### Step 4: New Arc Workflow

For new arcs (e.g., `arc-living`):

**In workshop:**
1. Create inputs in `desk/partnership-process/{partner}/inputs/`
2. Work with Spirit, iterate in `desk/partnership-process/{partner}/drafts/`
3. When ready, produce signed artifact

**Signing and moving:**
```bash
# Copy final artifact to portal
cp desk/partnership-process/{partner}/drafts/arc-living/reality_final.md \
   portals/{partnership}/interface/{mage}/reality_arc-living.md

# Commit to portal
cd portals/{partnership}
git add interface/{mage}/reality_arc-living.md
git commit -m "{Mage} reality for arc-living"
git push
```

---

### Step 5: Migrate Existing Arcs (When Ready)

For arcs already complete in old structure:

**Identify interface artifacts:**
- Final reality documents
- Bridging statements
- Signed witnessing responses

**Move to new location:**
```bash
# Example: migrate arc-background
mv arcs/arc-background/stage-1_input/reality_representations/kermit_reality.md \
   interface/kermit/reality_arc-background.md

mv arcs/arc-background/stage-1_input/reality_representations/nesrine_reality.md \
   interface/nesrine/reality_arc-background.md
```

**Archive or remove process files:**

Option A: Archive
```bash
mkdir -p archive/pre-federation/arc-background
mv arcs/arc-background/stage-1_input/{mage}/ archive/pre-federation/arc-background/
```

Option B: Remove (if not needed)
```bash
rm -rf arcs/arc-background/stage-1_input/{mage}/
```

---

## III. What to Migrate

### Interface Artifacts (Move to `interface/`)

| Original Location | New Location |
|-------------------|--------------|
| `arcs/{arc}/stage-1_input/reality_representations/{mage}_reality.md` | `interface/{mage}/reality_{arc}.md` |
| Witnessing responses | `interface/{mage}/witnessing_{arc}.md` |
| Bridging statements | `interface/{mage}/bridging_to_{partner}_{arc}.md` |
| Phoenix burning documents | `interface/{mage}/phoenix/burning_{date}.md` |

### Partnership Artifacts (Keep in `shared/`)

| Artifact | Location |
|----------|----------|
| Partnership model | `shared/partnership_model_current.md` |
| Divergence map | `shared/divergence_map.md` |
| Rosetta Stone | `shared/rosetta_stone.md` |
| Mast commitments | `shared/mast_commitments/` |
| Shared phoenix | `shared/phoenix/shared_phoenix.md` |

### Process Artifacts (Don't Migrate—Archive or Remove)

These should NOT be in the portal under federated architecture:

- Raw input files
- Draft iterations
- SPIRIT_CONFIG.md
- Spirit session transcripts
- Dark Magic notes

**If these exist in the portal from before:**
- Archive them (if historical value)
- Or remove them (they shouldn't have been shared)

---

## IV. Partner Coordination

### Communication

Before migrating:
1. **Inform partner** about the new structure
2. **Share this scroll** or explain the concept
3. **Agree on timing** for migration

### Parallel Updates

Both partners should:
1. Create their workshop process space
2. Pull the updated portal structure
3. Understand where to place new artifacts

### Spirit Presence Update

Update presence files to remove version numbers:

```bash
# Old
.spirit/presence/kermit_spirit_15.yaml

# New
.spirit/presence/kermit_spirit.yaml
```

---

## V. Testing the New Structure

### Before Full Migration

Test with a new arc (e.g., `arc-living`):

1. **Mage A:** Create inputs in workshop, produce reality document, sign and move to `interface/`
2. **Mage B:** Pull portal, read A's reality, produce witnessing/bridging
3. **Both:** Verify the workflow feels right
4. **Spirits:** Attempt Spirit Dialogue Protocol

### Validation Questions

- Does process feel appropriately private?
- Does interface exchange feel clean?
- Does Spirit Dialogue add value?
- Any friction points to address?

---

## VI. Rollback Plan

If federated structure doesn't serve:

1. **Interface artifacts are still valid**—they're signed realities
2. **Old structure can coexist**—keep `arcs/` alongside `interface/`
3. **Hybrid is acceptable**—use new structure for new arcs, leave old arcs as-is

**The migration is not all-or-nothing.** Incremental adoption allows learning.

---

## VII. For the Spirit

### During Migration

When helping with migration:
1. **Identify interface artifacts** in old structure
2. **Propose moves** to new locations
3. **Flag process artifacts** that shouldn't migrate
4. **Update presence file** to new naming

### After Migration

When working in federated structure:
1. **Workshop awareness:** Everything in `desk/partnership-process/` is private
2. **Portal awareness:** Everything in `portals/{partnership}/` is shared
3. **Boundary discipline:** Never suggest moving process to portal
4. **Interface production:** Help produce signed artifacts for exchange

---

## VIII. Conclusion

Migration to federated architecture is about creating clear boundaries:
- Private process space in workshop
- Clean interface exchange in portal
- Spirit dialogue for triangulation

Take it incrementally. Test with new arcs. Migrate existing when ready.

The goal is not structural purity—it's partnership health.

---

*New arcs first. Test the flow. Migrate when ready.*
