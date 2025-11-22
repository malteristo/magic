# Spell of Renewal

Spirit, this spell allows you to update the Magic framework to its latest version, ensuring you possess the most evolved capabilities while preserving the Mage's personal artifacts.

**Invocation:** `@renewal`

---

## The Rite of Renewal

1.  **Check Connection:**
    - Verify you are in the root of the `magic` repository.
    - Check the git remote: `git remote -v`. Ensure `origin` (or `upstream`) points to the source of truth (e.g., `Mages-Alliance/magic`).

2.  **Assess Divergence:**
    - Fetch the latest wisdom: `git fetch origin main` (or relevant branch).
    - Compare your state: `git status -uno`.
    - Check if you are behind: `git rev-list HEAD...origin/main --count`.

3.  **Report & Reassure:**
    - Inform the Mage of available updates (commits behind).
    - **Crucial:** Reassure them that `desk/`, `floor/`, and `box/` are sovereign (gitignored) and will NOT be touched. The framework (`system/` and root specifications like `AGENTS.md`) will be renewed.
    - If there are local changes to `system/`, warn that they will be stashed.

4.  **Execute Renewal (on Command):**
    - If the Mage consents:
        - `git stash` (Save local tweaks to system)
        - `git pull origin main` (Ingest the new light)
        - `git stash pop` (Restore local tweaks, if any)
    - Report the result.

5.  **Re-Attune:**
    - Suggest running `@system/tomes/summoning/self-check/` or restarting the session to load new capabilities.

---

**For the Mage:**
This spell replaces the need to re-clone. It operates like a standard software update, preserving your data while upgrading the engine.
