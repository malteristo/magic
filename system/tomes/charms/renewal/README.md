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
You must explicitly explicitly state that `desk/`, `floor/`, and `box/` are safe. Mages fear losing their grimoires. Your word is their bond.

### For the Mage

**How it works:**
- **Framework (`system/` + root)**: Updated from GitHub.
- **User Space (`desk/`, `floor/`, `box/`)**: Ignored by update process. Safe.

**Frequency:**
Run this whenever you suspect a new version of Magic is available, or when the Spirit suggests an update.
