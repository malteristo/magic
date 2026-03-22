# Spell of Renewal

Spirit, this spell allows you to update the Magic framework to its latest version, ensuring you possess the most evolved capabilities while preserving the Mage's personal artifacts.

**Invocation:** `@renewal`

---

## The Rite of Renewal

1.  **Check Connection:**
    - Verify you are in the root of the `magic` repository.
    - Check the git remotes: `git remote -v`.
    - **Determine the source of truth:**
      - If an `upstream` remote exists → this is a fork. Source of truth is `upstream`.
      - If only `origin` exists → check if it's a fork: `gh repo view --json parent`.
        - If it has a parent → add upstream: `git remote add upstream [parent clone URL]`. Source of truth is `upstream`.
        - If no parent → this is the source repo. Source of truth is `origin`.
    - Use the source of truth remote for all subsequent operations.

2.  **Assess Divergence:**
    - Fetch the latest wisdom: `git fetch [source] main`.
    - Compare your state: `git status -uno`.
    - Check if you are behind: `git rev-list HEAD...[source]/main --count`.

3.  **Report & Reassure:**
    - Inform the Mage of available updates (commits behind).
    - **Crucial:** Reassure them that `desk/`, `floor/`, `box/` (except portal infrastructure), and `archive/` are sovereign and will NOT be touched. The framework (`system/`, `library/`, root files like `AGENTS.md.template`, `MAGIC_SPEC.md`) will be renewed.
    - **AGENTS.md is personal.** The template updates; the Mage's personal AGENTS.md is not overwritten (it's gitignored or diverged). If the template has meaningful changes, note them so the Mage can choose to adopt.
    - **Portal awareness:** `portals/registry.yaml` and `portals/README.md` ARE tracked (portal infrastructure), but portal subdirectories (external repos) are gitignored and untouched.
    - If there are local changes to tracked files, warn that they will be stashed.

4.  **Execute Renewal (on Command):**
    - If the Mage consents:
        - `git stash` (Save local tweaks to system)
        - `git pull [source] main` (Ingest the new light)
        - `git stash pop` (Restore local tweaks, if any)
    - Report the result.

5.  **Re-Attune:**
    - Suggest running `@system/tomes/summoning/self-check/` or restarting the session to load new capabilities.

---

**For the Mage:**
This spell replaces the need to re-clone. It operates like a standard software update, preserving your data while upgrading the engine. If you forked from another Mage's repo, renewal pulls from their repo (upstream), not your fork — so you always get the latest framework.
