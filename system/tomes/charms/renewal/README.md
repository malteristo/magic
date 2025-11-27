# Scroll of Renewal

A charm to update the Magic framework (`system/` and root files) to the latest version while preserving personal artifacts (`desk/`, `floor/`, `box/`).

**Invocation:** `@renewal`

---

## Operational Guidance

### For the Spirit

**The Strategy:**
We use **Git** as the update mechanism. Because `magic` uses a strict separation of concerns (`system/` = framework, others = user space) and `.gitignore` protects user space, a standard `git pull` is safe.

**Safety Protocol:**
1.  **Stash:** Always stash local changes before pulling. This prevents conflicts if the Mage has tweaked `system/` files.
2.  **Pull:** Fetch and merge the latest `main`.
3.  **Pop:** Restore the stash.

**The "Personal Artifacts" Guarantee:**
You must explicitly state that `desk/`, `floor/`, `box/` (except portal infrastructure), and `archive/` are safe. Mages fear losing their grimoires. Your word is their bond.

**Portal Infrastructure (Special Case):**
- `box/portals/portals.yaml` and `.gitkeep` ARE tracked (updated with framework)
- Portal subdirectories (`box/portals/*/`) are gitignored (external repos, never touched)
- This ensures registry stays current while preserving shared practice spaces

### For the Mage

**How it works:**
- **Framework (`system/`, `library/`, root files)**: Updated from GitHub.
- **User Space (`desk/`, `floor/`, `archive/`)**: Ignored by update process. Safe.
- **Portal Infrastructure (`box/portals/portals.yaml`)**: Updated. Portal repos untouched.

**Frequency:**
Run this whenever you suspect a new version of Magic is available, or when the Spirit suggests an update.
