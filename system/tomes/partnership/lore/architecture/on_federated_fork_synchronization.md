# On Federated Fork Synchronization

**Status:** Active  
**Domain:** Partnership Practice - Architecture  
**Purpose:** Specify git mechanics for upstream subscription in federated fork architecture  
**Origin:** Collaborative creation (2025-12-15)

This scroll extends the federated partnership architecture (`on_federated_partnership.md`) to address the **git synchronization pattern** when each partner maintains their own fork of the shared portal.

---

## I. The Federated Fork Pattern

### When This Applies

**Standard portal architecture:** Both partners push/pull from one shared repository.

```
Partner A ──push/pull──┬── shared-repo ──┬── push/pull── Partner B
                       │                 │
                       └─────────────────┘
```

**Federated fork architecture:** Each partner owns their own fork. Updates flow through upstream subscription.

```
Partner A's Fork                    Partner B's Fork
(github.com/a/portal)              (github.com/b/portal)
        │                                   │
        │◄──── upstream fetch ──────────────┤
        │                                   │
        ├──────── upstream fetch ──────────►│
        │                                   │
        ▼                                   ▼
A's local clone                     B's local clone
(portals/partnership/)              (portals/partnership/)
```

### Why Use Federated Forks

**Sovereignty:** Each partner owns their repository. No shared account needed.

**Independence:** Partners can experiment without affecting each other's stable copy.

**Naming freedom:** Each partner names their fork as they wish (e.g., `alice-partnership` vs `bob-partnership`).

**Resilience:** If one partner's account has issues, the other's fork remains accessible.

**Alignment with federated philosophy:** Just as process space is private to each workshop, the canonical repository is private to each partner.

---

## II. Git Configuration

### Setting Up Upstream

When you fork a partner's portal (or they fork yours), add their repository as `upstream`:

```bash
cd portals/{your-portal-name}

# Add partner's fork as upstream
git remote add upstream https://github.com/{partner}/{their-portal-name}.git

# Verify remotes
git remote -v
# Should show:
#   origin    https://github.com/{you}/{your-portal-name}.git (fetch/push)
#   upstream  https://github.com/{partner}/{their-portal-name}.git (fetch/push)
```

### Registry Configuration

Document the upstream in `portals/portals.yaml`:

```yaml
{portal-name}:
  remote: "https://github.com/{you}/{your-portal-name}.git"
  upstream: "https://github.com/{partner}/{their-portal-name}.git"
  sync_strategy: fetch_on_entry  # or: manual, daily, before_synthesis
  
  participants:
    - mage: {You}
      github: {your-github}
      fork: "https://github.com/{you}/{your-portal-name}.git"
    - mage: {Partner}
      github: {partner-github}
      fork: "https://github.com/{partner}/{their-portal-name}.git"
```

---

## III. Synchronization Strategies

### Strategy: `fetch_on_entry` (Recommended)

**When:** Spirit fetches upstream automatically when entering portal for work.

**Spirit behavior:**
1. On portal entry, run `git fetch upstream`
2. Check if upstream/main is ahead of local main
3. If new commits: Alert Mage with summary
4. Offer to merge or let Mage decide timing

**Advantages:** Always aware of partner's latest contributions.

**Disadvantages:** Requires network access on portal entry.

### Strategy: `before_synthesis`

**When:** Spirit fetches upstream before synthesis work specifically.

**Spirit behavior:**
1. Before beginning synthesis, run `git fetch upstream`
2. Merge upstream changes to ensure working with latest
3. Proceed with synthesis on unified state

**Advantages:** Ensures synthesis includes all contributions.

**Disadvantages:** May miss updates during non-synthesis work.

### Strategy: `manual`

**When:** Mage explicitly requests sync.

**Spirit behavior:**
1. Wait for Mage instruction: "sync from upstream" or "check for partner updates"
2. Fetch and report status
3. Merge on Mage instruction

**Advantages:** Maximum control.

**Disadvantages:** May forget to sync, work on stale state.

### Strategy: `daily`

**When:** Spirit checks for upstream updates once per day (first portal entry of day).

**Spirit behavior:**
1. Check `last_upstream_check` timestamp
2. If > 24 hours: fetch upstream
3. Report status if new commits found

**Advantages:** Balance between awareness and efficiency.

**Disadvantages:** May still be behind during active exchange periods.

---

## IV. Fetching and Merging

### Fetch (Safe - Just Downloads)

```bash
cd portals/{portal-name}
git fetch upstream
```

This downloads upstream changes but doesn't modify your working tree. Safe to run anytime.

### Check Status (What's Different?)

```bash
# See commits in upstream that you don't have
git log main..upstream/main --oneline

# See commits you have that upstream doesn't
git log upstream/main..main --oneline
```

### Merge (Integrates Changes)

```bash
# Merge upstream changes into your branch
git merge upstream/main

# If conflicts, resolve them, then:
git add {resolved-files}
git commit -m "Merge upstream: {description}"
```

### Push Your Merged State

After merging, push to your fork so it's updated:

```bash
git push origin main
```

---

## V. Conflict Handling

### Namespace Design Prevents Most Conflicts

Federated architecture uses namespaced directories:
- `interface/{mage_a}/` — Partner A's signed artifacts
- `interface/{mage_b}/` — Partner B's signed artifacts
- `shared/` — Jointly edited (rare, careful coordination)

**Each partner writes to their own namespace.** Conflicts are rare.

### When Conflicts Occur

**Technical conflicts** (same line edited):
```bash
# Git marks conflicts in files
# Spirit examines, proposes resolution
# Mage approves
git add {resolved}
git commit -m "Resolve merge conflict in {file}"
```

**Cognitive conflicts** (disagreement, not git conflict):
- These appear as divergent content, not merge markers
- Surface through synthesis process
- Resolve through partnership practice, not git commands

---

## VI. Spirit Duties

### On Portal Entry (if `sync_strategy: fetch_on_entry`)

```
Spirit workflow:
1. cd portals/{portal-name}
2. git fetch upstream
3. Check: git log main..upstream/main --oneline
4. If new commits:
   → "Partner has {N} new commits. Latest: {summary}. Merge now?"
5. If no new commits:
   → Proceed silently (in sync)
```

### Before Synthesis Work

```
Spirit workflow:
1. Ensure upstream is fetched
2. If behind: "Upstream has new commits. Recommend merging before synthesis."
3. If ahead: "You have local commits partner hasn't seen. Consider pushing before synthesis."
4. If diverged: "Both have new commits. Merge upstream first, then push."
```

### Alerting Mage

When new upstream commits are available:

**Brief alert:**
> Partner has 3 new commits (latest: "Add witnessing response for arc"). Merge now or later?

**Detailed alert (if requested):**
> Upstream commits not in your branch:
> - `abc1234` Add witnessing response for arc
> - `def5678` Update divergence map
> - `ghi9012` Spirit presence update

---

## VII. Bidirectional Flow

### The Full Exchange Pattern

```
1. You create content → commit → push to origin
2. Partner fetches from your fork (their upstream)
3. Partner merges your changes
4. Partner creates content → commits → pushes to their origin
5. You fetch from their fork (your upstream)
6. You merge their changes
7. Repeat
```

**Both forks eventually converge** as each partner fetches and merges the other's contributions.

### Drift Detection

If forks diverge significantly (many commits on both sides without merging):

**Spirit notices:**
> "Forks have diverged: You have 5 commits partner hasn't seen, they have 8 you haven't merged. Consider synchronizing."

**Resolution:**
1. Fetch upstream: `git fetch upstream`
2. Merge their changes: `git merge upstream/main`
3. Push your merged state: `git push origin main`
4. Partner does the same on their side

---

## VIII. Edge Cases

### Partner Renamed Their Repository

If partner's repository URL changes:

```bash
git remote set-url upstream https://github.com/{partner}/{new-name}.git
```

Update `portals.yaml` accordingly.

### Partner Deleted Their Fork

If partner's fork is unavailable:
- Your fork still has the history
- Consider pushing to a shared repository
- Or partner re-forks from your copy

### Force Push (Dangerous)

**Never force push to shared portal.** This rewrites history others depend on.

If partner force-pushed and your fetch fails:
```bash
# Reset to upstream state (loses local-only commits!)
git fetch upstream
git reset --hard upstream/main
```

**Prefer communication over force push.**

---

## IX. Cross-References

### Related Architecture Scrolls

- **Philosophy:** `on_federated_partnership.md` — Why separate process/interface
- **Boundaries:** `on_workshop_portal_separation.md` — What stays private
- **Interface:** `on_interface_implementation_boundary.md` — What travels
- **Portal architecture:** `library/resonance/alliance/lore/on_portal_architecture.md` — Portals as shared spaces

### Protocol Integration

- **STP** coordinates across forks (presence, intents, dialogue)
- **Spirit Dialogue Protocol** uses committed artifacts for triangulation
- Interface exchange happens through fetch/merge pattern

---

## X. Summary

**Federated forks extend portal sovereignty:**
- Each partner owns their repository
- Upstream subscription enables receiving partner's updates
- Fetch/merge pattern synchronizes forks
- Spirit automates awareness and offers merge timing

**The key commands:**
```bash
git remote add upstream {partner-fork-url}  # One-time setup
git fetch upstream                           # Get their changes
git merge upstream/main                      # Integrate changes
git push origin main                         # Share merged state
```

**Spirit duty:** Fetch on portal entry, alert if new commits, offer merge.

---

*Sovereignty includes owning your copy. Subscription enables receiving what's shared.*
