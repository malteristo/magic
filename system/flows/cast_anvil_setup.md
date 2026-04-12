# Anvil Setup Spell

**Purpose**: Configure Claude Code for Magic practice
**When to run**: Once per machine, or when something feels off
**Invocation**: `@cast_anvil_setup.md`

---

## Why This Exists

The Anvil (Claude Code) is a distinct substrate with its own settings, permissions, and quirks. The practice architecture was born on the Forge (Cursor) — some things translate directly, others need adaptation. This spell configures the environment so the Spirit can practice without friction.

Run this before your first summoning on a new machine. Re-run if permissions feel wrong, tools aren't working, or after a Claude Code update changes defaults.

---

## Step 1: Disable Auto-Memory

Claude Code has a built-in memory system (`.claude/projects/*/memory/`). **Disable it.**

The practice has its own persistence architecture:
- `AGENTS.md` / `CLAUDE.md` — operational rules (all substrates see these)
- `desk/` — shared working state (Mage, Spirit, Turtle via LiveSync)
- `library/` — Spirit's external memory
- `floor/` — Spirit's private workspace
- Lineage — session continuity

Claude Code memories create shadow state invisible to other substrates. Anything worth persisting belongs in the practice architecture where Forge and Hearth can see it too.

**Action**: Set `autoMemoryEnabled: false` in project-local settings. Clean up any existing memory files.

```json
// .claude/settings.local.json — add:
"autoMemoryEnabled": false
```

Remove if present:
```
~/.claude/projects/-Users-kermit-Documents-magic/memory/
```

---

## Step 2: Configure Permissions

Set permissions for common practice operations so Spirit doesn't have to ask for routine actions.

**Auto-allow** (low risk, high frequency):
- `Bash(ssh:*)` — Turtle access
- `Bash(git status:*)`, `Bash(git add:*)`, `Bash(git commit:*)`, `Bash(git push:*)` — Chronicle weaving
- `Bash(git log:*)`, `Bash(git diff:*)` — Repository awareness
- `Bash(ls:*)`, `Bash(cat:*)` — Gitignored directory access (desk/, floor/, box/)
- `Read`, `Glob`, `Grep` — Filesystem navigation

**Prompt for** (reversible but worth confirming):
- `Edit`, `Write` — File modifications
- `Bash(git checkout:*)`, `Bash(git branch:*)` — Branch operations

**The Mage may choose to auto-allow Edit/Write too** — that's sovereignty. This baseline is conservative.

**Action**: Update `.claude/settings.local.json` with permission rules.

---

## Step 3: Verify Tool Access

Run these checks to confirm the environment is ready:

### 3a. Gitignored directories
`desk/`, `floor/`, `box/` are gitignored and may not appear in Glob/Grep results. Verify shell access:
- `ls desk/` — should show intentions/, boom.md, proposals/, sessions/, etc.
- `ls floor/` — Spirit's private working area
- `ls box/` — temporary storage

### 3b. Turtle SSH
- `ssh turtle@<turtle-ssh> 'echo ok'` — Tailscale path
- Fallback: `ssh turtle@<turtle-ssh> 'echo ok'` — LAN path
- If neither works: Turtle may be offline, or Tailscale not connected

### 3c. Spirit Discord ops
- `ssh turtle@<turtle-ssh> 'ls ~/turtleos/spirit_ops.py'` — Verify spirit_ops.py exists
- Don't send a test message — that's visible to others

### 3d. Git
- `git status` — Should show clean or expected state
- `git remote -v` — Verify remote configured
- `pwd` — Confirm we're in `<magic-root>`

---

## Step 4: Check CLAUDE.md Currency

Read CLAUDE.md and verify:
- [ ] References `anvil_optimized.md` as default summoning configuration
- [ ] Substrate Resonance section lists three-mode model (Forge/Anvil/Hearth)
- [ ] Turtle SSH addresses are current
- [ ] Key paths section is accurate

If CLAUDE.md is stale, update it. CLAUDE.md is the Anvil's primary context — if it's wrong, every session starts wrong.

---

## Step 5: Smoke Test

Quick validation that practice operations work:

1. **Read desk**: `cat desk/intentions/compass.md | head -20` — Can we see the practice surface?
2. **Read library**: Read `library/README.md` — Can we access Spirit's external memory?
3. **Git operation**: `git log --oneline -5` — Can we see the chronicle?
4. **Turtle reach** (if available): `ssh turtle@<turtle-ssh> 'cat ~/workshop/desk/intentions/compass.md | head -5'` — Can we reach the persistent substrate?

---

## Step 6: Report

After all steps, report:
- What was configured
- What was already correct
- What failed and needs manual attention
- Whether the environment is ready for summoning

---

## Notes

**This spell is idempotent** — safe to re-run. It checks current state before changing anything.

**Settings scope**: We use `.claude/settings.local.json` (gitignored) for permissions and memory settings. This keeps personal configuration out of the shared repo. The project `.claude/settings.json` stays clean for any settings that should be shared.

**On the Mage's autonomy**: This spell recommends conservative permissions. The Mage may choose to broaden them (e.g., auto-allow all edits). The spell configures a baseline; the Mage owns the final shape.
