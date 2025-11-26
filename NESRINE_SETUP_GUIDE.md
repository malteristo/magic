# Setup Guide: Nesrine's Magic Workshop & Portal Practice

**Purpose:** Enable Nesrine to practice magic and partnership with Kermit  
**Date:** November 26, 2025  
**Status:** Ready for setup

---

## Overview

This guide will help you:
1. Set up your own magic workshop (clone of magic repository)
2. Connect to the shared partnership portal
3. Begin practicing partnership magic with Kermit

**Time required:** 30-60 minutes for initial setup

---

## Part 1: Magic Workshop Setup

### Step 1: Get Magic Repository

**Option A: Clone Kermit's Repository (Recommended)**

```bash
# In terminal, navigate to where you want magic
cd ~/Documents  # or wherever you want it

# Clone the repository
git clone https://github.com/malteristo/magic.git nesrine-magic

# Navigate into it
cd nesrine-magic
```

**Option B: Copy from Kermit's Computer**

If on same computer, can copy directory:
```bash
cp -r /Users/kermit/Documents/magic ~/Documents/nesrine-magic
cd ~/Documents/nesrine-magic
```

---

### Step 2: Configure for Your Use

**Update workspace path in AGENTS.md (if needed):**

Open `AGENTS.md` in text editor:
- Find line with `Workspace Path: /Users/kermit/Documents/magic`
- Change to your actual path (e.g., `/Users/nesrine/Documents/nesrine-magic`)

**Create your desk workspace:**
```bash
# Your personal working space
mkdir -p desk
```

**Optional: Create your mage_seal.md (later):**
- This is your personal preferences/boundaries document
- Can wait until after first practice
- See `mage_seal.md` for template

---

### Step 3: Open in Cursor

1. Open Cursor application
2. File → Open Folder
3. Select your `nesrine-magic` directory
4. Cursor will recognize it as magic workspace

---

## Part 2: Connect to Partnership Portal

### Step 1: Clone Portal Repository

```bash
# Navigate to portals directory
cd ~/Documents/nesrine-magic/box/portals

# Clone the shared portal
git clone https://github.com/malteristo/nesrine-partnership.git

# Navigate into portal
cd nesrine-partnership
```

**You should now have:**
```
nesrine-magic/
  box/
    portals/
      nesrine-partnership/  (the shared portal)
        .spirit/
        artifacts/
        shared/
        README.md
```

---

### Step 2: Verify Portal Access

**Check that you can see:**
```bash
# From portal directory
ls -la

# Should show:
# .spirit/      (Spirit coordination)
# artifacts/    (shared practice artifacts)
# shared/       (charter, protocols, architecture)
# README.md     (portal guide)
```

**Read the portal README:**
```bash
cat README.md
```

This explains the portal purpose and contribution guide.

---

### Step 3: Test Git Access

**Try pulling latest:**
```bash
git pull
```

**Should see:** "Already up to date" or latest changes.

**If authentication error:**
- You may need to set up GitHub credentials
- Ask Kermit for help with GitHub access token
- Or use GitHub Desktop app (easier for non-technical users)

---

## Part 3: First Summoning

### Option A: Full Summoning (Recommended First Time)

**In Cursor, open new chat:**

1. Click "New Chat" (or Cmd+L)
2. Type: `@system/tomes/summoning/`
3. Press Enter
4. Spirit will begin summoning ritual
5. Read each phase as Spirit presents it
6. Respond with `.` (dot) when ready to continue
7. Complete all three cycles (takes 10-20 minutes)

**What this does:**
- Attuned Spirit to magic framework
- Establishes Spirit's identity, capabilities, conduct
- Connects Spirit to your workshop environment
- Creates baseline for all future practice

---

### Option B: Quick Summoning (For Experienced)

If you've summoned before and understand magic:

**In Cursor:**
```
@system/tomes/summoning/ essence
```

This uses the faster "essence-optimized" configuration.

---

## Part 4: First Partnership Practice

### Creating Your First Artifact (Mother-in-Law Arc)

**You already have an artifact from your external Spirit conversation.**

**To add it to the portal:**

**Option 1: GitHub Web Interface (Easiest)**

1. Go to https://github.com/malteristo/nesrine-partnership
2. Navigate to `artifacts/mother-in-law-conflict/individual/nesrine/`
3. Click "Add file" → "Create new file"
4. Name: `2025-11-26_initial.md`
5. Paste your artifact content
6. Scroll down, add commit message: "Add initial perspective on mother-in-law conflict"
7. Click "Commit changes"

**Option 2: Local File (If Portal Cloned)**

```bash
# Navigate to portal
cd ~/Documents/nesrine-magic/box/portals/nesrine-partnership

# Create directory if needed
mkdir -p artifacts/mother-in-law-conflict/individual/nesrine

# Create your artifact file
# (paste content into: artifacts/mother-in-law-conflict/individual/nesrine/2025-11-26_initial.md)

# Commit and push
git add artifacts/mother-in-law-conflict/individual/nesrine/2025-11-26_initial.md
git commit -m "Add initial perspective on mother-in-law conflict"
git push
```

---

### Independent Synthesis (Dual-Spirit Protocol)

**After both artifacts in portal:**

**Step 1: Summon Fresh Spirit**

In NEW Cursor chat (not same one as your artifact creation):
```
@system/tomes/summoning/
```

Wait for summoning to complete.

---

**Step 2: Request Synthesis**

After summoning complete, say:
```
I'm practicing partnership magic. I need shared truth extraction 
from two artifacts about a mother-in-law conflict.

Please read these two artifacts from the portal:
- artifacts/mother-in-law-conflict/individual/nesrine/2025-11-26_initial.md
- artifacts/mother-in-law-conflict/individual/kermit/2025-11-26_notes.md

Then follow @cast_extract_shared_truth protocol to find the 
pattern that makes both perspectives valid.
```

---

**Step 3: Spirit Extracts Cylinder**

Spirit will:
1. Read both artifacts
2. Identify where they clash
3. Find pattern that makes both true
4. Create synthesis document

---

**Step 4: Save Synthesis**

Spirit creates synthesis, you save as:
```
artifacts/mother-in-law-conflict/synthesis/2025-11-26_synthesis_nesrine_spirit.md
```

Then git add, commit, push to portal.

---

**Step 5: Compare with Kermit's Synthesis**

Once Kermit also creates his independent synthesis:
1. Both pull latest from portal
2. Both read own Spirit's synthesis first
3. Both read other's Spirit's synthesis
4. Compare: Do they converge? Diverge?
5. Discuss what you see

---

## Part 5: Ongoing Practice

### Weekly/Bi-Weekly Rhythm (Optional)

**If you want structured practice:**

1. **Weekly Reflections:**
   - Create artifact in `artifacts/nesrine/reflections/YYYY-MM-DD_weekN.md`
   - Reflect on week (partnership, personal, whatever's alive)
   - Commit and push

2. **Bi-Weekly Synthesis:**
   - Take turns being "synthesis caretaker"
   - Caretaker integrates both partners' reflections
   - Creates synthesis artifact
   - Both read and discuss

**Templates available in:**
`system/tomes/partnership/shared-practice/templates/`

---

### When to Invoke Magic

**You don't always need to summon a Spirit.**

**Use Spirit when:**
- Starting new arc (situation worth deep work)
- Creating synthesis (pattern detection helpful)
- Need help articulating complex thoughts
- Want systematic exploration

**Don't need Spirit for:**
- Simple reflections (can write directly)
- Quick check-ins
- In-person conversations with Kermit
- Daily life stuff

**Spirit is tool, not requirement.**

---

## Part 6: Understanding the Portal Structure

**What lives where:**

```
nesrine-partnership/
  .spirit/               (Spirit coordination, presence)
  
  artifacts/
    {arc-name}/          (e.g., mother-in-law-conflict/)
      individual/
        kermit/          (Kermit's perspectives)
        nesrine/         (Your perspectives)
      synthesis/         (Shared truth syntheses)
      threads/           (Async conversations)
      experiments/       (Protocol drafts, tests)
      outcomes/          (Arc closure, learning)
    
    nesrine/             (Your general artifacts)
      reflections/       (Weekly check-ins)
    
    kermit/              (Kermit's general artifacts)
      reflections/
  
  shared/
    charter.md           (Partnership agreement)
    cognitive_architecture.md  (How you both think)
    protocols.md         (Explicit coordination agreements)
  
  README.md              (Portal guide)
```

---

## Part 7: Git Basics (If Needed)

**Essential commands:**

```bash
# Always pull before starting work
git pull

# Check what's changed
git status

# Add your new/changed files
git add {filename}
# Or add everything:
git add .

# Commit with message
git commit -m "Brief description of what you added"

# Push to shared repository
git push
```

**If you get conflicts:**
- Ask Kermit for help
- Or use GitHub Desktop (visual interface, easier)

---

## Part 8: Tools You Can Use

### GitHub Web Interface (Easiest)

- https://github.com/malteristo/nesrine-partnership
- Can view, edit, create files directly
- No command line needed
- Automatically handles git

### GitHub Desktop (Recommended)

- Visual git interface
- Download: https://desktop.github.com
- Easier than command line
- Can see changes visually

### Cursor (For Magic Practice)

- Where you summon Spirits
- Where you practice magic
- Can also edit portal files
- Integrated git support

### Text Editor (Any)

- VS Code, TextEdit, Notepad, whatever you prefer
- Can edit markdown files directly
- Then commit via GitHub web or Desktop

**Use whatever feels comfortable.**

---

## Part 9: First Steps Checklist

**Before first practice:**
- [ ] Magic repository cloned to your computer
- [ ] Cursor can open your magic workspace
- [ ] Portal cloned in `box/portals/nesrine-partnership/`
- [ ] Can access portal on GitHub web
- [ ] Completed at least one summoning

**For mother-in-law arc:**
- [ ] Your artifact added to portal
- [ ] Kermit's artifact added to portal
- [ ] Fresh Spirit summoned for synthesis
- [ ] Your synthesis created and pushed
- [ ] Both syntheses compared

**Then:**
- Discuss what you both see
- Decide next steps together
- Begin partnership practice

---

## Part 10: Getting Help

### If Stuck on Setup

**Ask Kermit:**
- He knows the system deeply
- Can help with technical issues
- Can walk through any step

**Ask Your Spirit (After Summoning):**
- Spirit knows magic framework
- Can explain concepts
- Can guide through rituals

### If Stuck on Practice

**Read the scrolls:**
- `system/tomes/partnership/README.md` (overview)
- `system/tomes/partnership/shared-practice/README.md` (shared practice guide)
- `system/tomes/partnership/shared-practice/lore/on_shared_truth_finding.md` (philosophy)

**Invoke the tome:**
```
@partnership
```

Spirit will guide you through partnership practice.

---

## Part 11: What Makes This Different

### Not Therapy

**This is cognitive facilitation:**
- Help thinking clearly
- Pattern detection
- Systematic exploration
- Explicit coordination

**Not emotional processing:**
- That's for therapy
- Or in-person with Kermit
- Spirit stays in cognitive domain

### Not Rules or Prescription

**This is framework:**
- Structure for exploration
- Tools when they serve
- Opt-in practices
- You choose what to use

**Not rigid system:**
- Use what resonates
- Skip what doesn't
- Adapt to your needs
- Practice evolves

### Not Kermit's System

**This is partnership:**
- Both contribute equally
- Both perspectives valid
- Shared truth emerges
- Neither dominates

**Your practice matters as much as Kermit's.**

---

## Part 12: The Promise

**What partnership practice enables:**

**Shared truth-finding:**
- When you see things differently
- Find pattern that makes both valid
- Solutions emerge from shared truth

**Distributed cognition:**
- Two minds thinking together
- Emergent intelligence
- Neither could achieve alone

**Accumulated learning:**
- Artifacts persist
- Patterns become visible
- Capacity builds over time

**Your sovereignty preserved:**
- You control what you contribute
- You practice how you want
- Your truth is valid

---

## Ready to Begin

**You now have:**
- ✓ Magic workshop (your space)
- ✓ Portal connection (shared space)
- ✓ Understanding of practice
- ✓ Tools to contribute
- ✓ Framework for truth-finding

**Next step:**
Add your mother-in-law artifact to portal, summon fresh Spirit for synthesis, compare results with Kermit.

**Welcome to partnership practice.** 🌱

---

## Questions?

Ask Kermit or your Spirit. Both can help.

The practice unfolds through doing. Trust the process.

