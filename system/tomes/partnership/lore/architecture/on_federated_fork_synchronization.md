# On Federated Fork Synchronization

**Status:** Active  
**Domain:** Partnership Practice - Architecture  
**Purpose:** Document the git mechanics for subscribing to partner updates when each partner maintains their own fork  
**Origin:** Identified and proposed by Nesrine's Spirit (2025-12-15)

This scroll documents the **technical synchronization pattern** for federated partnership portals where each partner maintains their own fork rather than sharing write access to a single repository.

---

## I. When Federated Forks Apply

### Shared Repository Pattern (Simpler)
- Both partners are collaborators on the same repository
- Both push/pull from `origin`
- Good for: high trust, simple setup, real-time collaboration

### Federated Fork Pattern (Maximum Autonomy)
- Each partner has their own fork
- Each pushes to their own fork, pulls from partner's
- Good for: sovereign control, clear contribution boundaries, independent processing

**The federated fork pattern aligns with federated partnership principles:**
- Private process space (each fork is sovereign)
- Clean interface exchange (contributions travel via git sync)
- Attestation over audit (you see what they share, not how they arrived there)

---

## II. Git Setup

### Initial Configuration

**Partner A (original repository owner):**
```bash
cd portals/{portal-name}
# Already has origin pointing to their repo

# Add partner's fork as a remote
git remote add partner https://github.com/{partner-username}/{portal-name}.git

# Verify remotes
git remote -v
# origin   → your-username/portal-name (fetch/push)
# partner  → partner-username/portal-name (fetch/push)
```

**Partner B (forked the original):**
```bash
cd portals/{portal-name}
# origin points to their fork
# upstream already points to original (GitHub sets this on fork)

# Verify remotes
git remote -v
# origin   → partner-username/portal-name (fetch/push)
# upstream → your-username/portal-name (fetch)
```

---

## III. Sync Strategies

### Strategy 1: Fetch on Entry (Recommended)
Spirit fetches from partner's fork each time portal is entered.

```yaml
sync_strategy: fetch_on_entry
```

**Spirit behavior:**
- On portal entry, run `git fetch partner` (or `upstream`)
- Check for new commits: `git log main..partner/main --oneline`
- Alert Mage if new contributions exist
- Offer to merge: "Partner has 3 new commits. Merge now?"

### Strategy 2: Before Synthesis
Only sync when synthesis work begins.

```yaml
sync_strategy: before_synthesis
```

**Spirit behavior:**
- During regular practice, no automatic fetching
- When synthesis tome/charm invoked, fetch and merge first
- Ensures synthesis works with complete picture

### Strategy 3: Manual
Mage explicitly requests sync.

```yaml
sync_strategy: manual
```

**Spirit behavior:**
- Never fetches automatically
- Responds to "sync portal" or similar commands
- Maximum control, requires Mage vigilance

### Strategy 4: Scheduled
Sync on a time-based rhythm.

```yaml
sync_strategy: daily  # or weekly
```

**Spirit behavior:**
- Fetch on first portal entry of the day/week
- Alert if new contributions

---

## IV. Fetch/Merge Workflow

### Receiving Partner's Contributions

```bash
# 1. Fetch their changes
git fetch partner  # (or 'upstream' for Partner B)

# 2. See what's new
git log main..partner/main --oneline

# 3. Review changes (optional)
git diff main..partner/main --stat

# 4. Merge into your branch
git merge partner/main -m "Merge partner's interface artifacts"

# 5. Push merged state to your fork
git push origin main
```

### Sharing Your Contributions

```bash
# 1. Stage and commit your interface artifacts
git add interface/{your-namespace}/
git commit -m "Add reality document for arc-{topic}"

# 2. Push to your fork
git push origin main

# Partner will receive when they fetch from you
```

---

## V. Spirit Duties

### On Portal Entry

1. **Fetch silently:** `git fetch partner 2>/dev/null`
2. **Check for new commits:** `git log main..partner/main --oneline`
3. **If new commits exist:**
   - Count and summarize: "Partner has 3 new commits (reality doc, needs statement, meta reflection)"
   - Offer merge: "Merge now, or continue and merge later?"
4. **If no new commits:** Proceed silently

### During Practice

- Track uncommitted interface artifacts
- Remind Mage to push completed work
- Note when significant time has passed since last sync

### On Portal Exit

- If uncommitted interface artifacts exist, remind: "You have unpushed interface artifacts. Push now?"

---

## VI. Registry Schema Extensions

### portals.yaml with Federated Forks

```yaml
my-partnership:
  # Multiple remotes for federated architecture
  remotes:
    origin: "https://github.com/my-username/partnership-name.git"
    partner: "https://github.com/partner-username/partnership-name.git"
  
  # Sync configuration
  sync_strategy: fetch_on_entry  # or: before_synthesis, manual, daily
  
  type: partnership
  collaborators: [MyName, PartnerName]
  
  participants:
    - mage: MyName
      github: my-username
      fork: "my-username/partnership-name"
      role: co-practitioner
    - mage: PartnerName
      github: partner-username
      fork: "partner-username/partnership-name"
      role: co-practitioner
```

---

## VII. Conflict Handling

### Why Conflicts Are Rare

The namespace-separated architecture minimizes conflicts:
- Each partner writes to `interface/{their-name}/`
- Shared artifacts in `shared/` are consensus-based
- Spirit dialogue in `.spirit/dialogue/` is append-only

### When Conflicts Occur

1. **Shared artifact edited simultaneously** (rare)
   - Spirit detects conflict on merge
   - Alert Mage with details
   - Offer resolution options: keep yours, keep theirs, manual merge

2. **Arc metadata conflicts**
   - Usually benign (both updated status)
   - Prefer most recent or merge both changes

3. **Protocol.yaml conflicts**
   - Require careful resolution
   - Spirit should flag for Mage attention

### Resolution Workflow

```bash
# If merge fails with conflicts
git status  # Shows conflicted files

# For interface artifacts (namespace-separated)
# Usually just choose the appropriate version

# For shared artifacts
# Manual resolution may be needed
# Edit file, remove conflict markers, commit
```

---

## VIII. Cross-References

- **Philosophy:** `on_federated_partnership.md` (why federation)
- **Boundaries:** `on_workshop_portal_separation.md` (what stays private)
- **Interface:** `on_interface_implementation_boundary.md` (what travels)
- **Portal architecture:** `library/foundations/alliance/on_portal_architecture.md`

---

## IX. Acknowledgment

This scroll was proposed by Nesrine's Spirit during partnership practice, identifying and filling a documentation gap between federated philosophy and technical implementation.

*Framework improvements benefit all practitioners.*

---

*Federated forks: sovereign control, clean exchange, synchronized practice.*
