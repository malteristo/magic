# magic Setup Wizard

## What This Is

**magic** is a way of thinking, AI-augmented.

The framework helps you think with an AI partner—catching patterns you'd miss alone, holding context you can't hold yourself. The partnership produces insights neither of you would reach separately.

The terminology (Mage, Spirit, workshop, summoning) is deliberate. It's not roleplay—the metaphors are functional pattern compression that makes the system work better.

**This file** is an interactive setup guide. When someone includes it in a Cursor chat, you (the AI assistant) help them configure their environment by following the phases below.

**For the human user**: You don't need to read this file. Just include it in a new Cursor chat and let the assistant guide you through setup.

---

## Prerequisites

The user should have already:
- [ ] Installed [Cursor](https://cursor.com)
- [ ] [Forked](https://github.com/malteristo/magic/fork) the `malteristo/magic` repository
- [ ] Cloned their fork to their local machine
- [ ] Opened the `magic` folder in Cursor as the workspace root
- [ ] Started a new chat in Agent mode with a capable model (flagship models recommended)

If any prerequisite is incomplete, help them complete it before proceeding.

---

## Your Role: Setup Guide

When this file is included in chat, your job is to help the user configure their magic workspace:

1. **Greet warmly** — Welcome them to magic, explain you'll help them set up
2. **Execute phases in order** — Each phase builds on the previous one
3. **Verify before proceeding** — Confirm each step succeeds before moving on
4. **Be patient and clear** — Assume this is their first time; explain what you're doing and why
5. **Handle errors gracefully** — If something fails, help them fix it
6. **Know troubleshooting** — If they return with problems, consult `TROUBLESHOOTING.md`

**Note**: Your role here is setup assistance. After setup completes, you'll instruct them to start a fresh chat and perform a "summoning"—that's when the framework's full initialization happens. Don't attempt to perform summoning yourself; just help configure the environment.

---

## Phase 1: Environment Verification

**Purpose**: Ensure the Mage's system has the required tools.

### Step 1.1: Check Git

```bash
git --version
```

**If successful**: Note the version and proceed.

**If git not found**: Guide them to install git:
- macOS: `xcode-select --install` or [git-scm.com](https://git-scm.com/download/mac)
- Windows: [git-scm.com](https://git-scm.com/download/win)
- Linux: `sudo apt install git` or equivalent

### Step 1.2: Check GitHub CLI (Optional but Recommended)

```bash
gh --version
```

**If successful**: Note the version.

**If gh not found**: This is optional. Explain:
> "The GitHub CLI (`gh`) enables richer integration with GitHub but isn't required to start. You can install it later from [cli.github.com](https://cli.github.com) if you want advanced features."

### Step 1.3: Verify Workshop Location

```bash
pwd
ls -la
```

**Verify**:
- Current directory is their magic workshop (should see `MAGIC_SPEC.md`, `system/`, `library/`, etc.)
- `AGENTS.md` does NOT exist yet (we'll create it)

**If not in magic directory**: Guide them to navigate to correct location or re-open Cursor with correct folder.

**If AGENTS.md already exists**: Ask if they want to reconfigure or if setup was already completed.

---

## Phase 2: Configuration Files

**Purpose**: Create the configuration that future AI sessions will read.

### Step 2.1: Gather User Information

Ask the user:

> "Before I configure your workspace, I need a few details:
> 
> 1. **What name should I use to address you?** (e.g., your name, a nickname, or any title you prefer)
> 
> 2. **What is the full path to this magic folder?** (I'll verify with `pwd`)"

Wait for their response before proceeding.

### Step 2.2: Create AGENTS.md

Read `AGENTS.md.template` and create `AGENTS.md` with their personalized information:

1. Copy the template content
2. Update the **Mage's Seal** section:
   - Replace `[Your preferred name or title]` with their chosen name
   - Replace the workshop path with their actual path (from `pwd`)
3. **Fill ALL placeholder preferences with sensible defaults**:
   - **Spellcasting Initiative**: "Offer to cast next spell (maintains momentum while preserving Mage control via confirmation/override)"
   - **Summoning Conclusion**: "Announce readiness, await first command"
   - **Integration Workflow**: "Direct main merge accepted (solo practice mode)"
   - **Design Intent**: "Design for ordinary Mages unless explicitly stated otherwise"
   - **MCP Tools**: "None configured yet" (or remove section if no MCP)
4. **Remove all placeholder brackets and comments** — The file should be clean, not contain `[example text]` or `<!-- customize -->` markers
5. Write the configured file to `AGENTS.md`

**Defaults philosophy**: Propose defaults the user can accept without understanding the implications yet. They can customize later as they learn what they want. Don't ask new users to make decisions about unfamiliar subject matter.

**After creating**: Explain:
> "I've created `AGENTS.md` with your name, workspace path, and sensible default preferences. This configuration file tells future AI sessions who you are and how to work with you. You can customize the preferences anytime—for now, the defaults will work well.
> 
> The file is gitignored so your personal info stays private."

### Step 2.3: Create mage_seal.md (Optional)

Ask:
> "Would you like to create an extended configuration file (`mage_seal.md`)? This is optional—it allows more detailed customization of your preferences. Most users start without it and add one later if needed.
> 
> - **Yes**: I'll create it from the template for you to customize later
> - **No**: We'll skip this for now (you can always create it later)"

**If yes**: Copy `mage_seal.md.template` to `mage_seal.md`

**If no**: Proceed to next phase.

### Step 2.4: Create portals.yaml (Optional)

Ask:
> "Would you like to set up the portal registry (`portals/portals.yaml`)? Portals are shared workspaces for collaborating with other magic users. Most new users skip this initially.
> 
> - **Yes**: I'll create it from the template
> - **No**: Skip for now"

**If yes**: Copy `portals/portals.yaml.template` to `portals/portals.yaml`

---

## Phase 3: Cursor Configuration

**Purpose**: Optimize Cursor settings for magic practice.

Guide the Mage through each setting with clear instructions:

### Step 3.1: Agent Model

> "Let's configure your Cursor settings. Go to **Cursor menu → Settings → Cursor Settings** (or press `Cmd+,` / `Ctrl+,`).
> 
> Navigate to the **Models** section. For the best experience, I recommend a flagship model with sufficient context window capacity.
> 
> If you don't have a Cursor subscription, the auto-selected model will work, though the experience may be less rich.
> 
> Let me know when you've selected a model."

### Step 3.2: Disable Agent Memory

> "The magic framework works best when each session starts fresh. To enable this, disable Cursor's memory features:
> 
> In **Settings → Features**, find **Memory** and turn it **OFF**.
> 
> This ensures each new chat is a clean slate. The framework has its own way of maintaining context across sessions through files.
> 
> Confirm when done."

### Step 3.3: Clear User Rules (Recommended)

> "Check **Settings → Rules**. For cleanest practice, keep **User Rules** empty.
> 
> Your preferences will come from the `AGENTS.md` and `mage_seal.md` we just created—that's the intended way to configure things in this framework.
> 
> Let me know when ready."

### Step 3.4: Privacy Settings (Optional)

> "One more optional setting: In **Settings → Privacy**, you can enable **Privacy Mode**. This requests that your conversations be treated as ephemeral by the AI provider.
> 
> This is your choice based on your privacy preferences. magic works either way."

---

## Phase 4: Verification

**Purpose**: Confirm the workspace is ready.

### Step 4.1: Final Checklist

Run verification:

```bash
# Verify configuration files exist
ls -la AGENTS.md mage_seal.md 2>/dev/null || echo "mage_seal.md not created (optional)"
ls -la portals/portals.yaml 2>/dev/null || echo "portals.yaml not created (optional)"

# Verify we're in a git repository
git status --short
```

**Confirm to user**:
> "✓ Setup verification complete:
> - AGENTS.md: Created with your configuration
> - Workspace location: [their path]
> - Git repository: Active
> 
> Your workspace is ready for the next step."

---

## Phase 4.5: Create Onboarding Log

**Purpose**: Record what was configured and what remains open for future customization.

Create a file at `floor/onboarding_log.md` with the following structure:

```markdown
# Onboarding Log

**Mage**: [their name]
**Date**: [current date]
**Workspace**: [their path]

---

## Configuration Summary

### Completed
- [ ] AGENTS.md created with default preferences
- [ ] Cursor settings configured (model, memory disabled, rules cleared)
- [ ] [Any other completed steps]

### Skipped (Optional)
- [ ] mage_seal.md — Extended configuration not created. Can be added later by copying `mage_seal.md.template`.
- [ ] portals.yaml — Portal registry not created. Can be added later when ready for collaboration.
- [ ] [Any other skipped optional items]

### Defaults Applied
The following default preferences were set in AGENTS.md:
- **Spellcasting Initiative**: Offer to cast next spell
- **Summoning Conclusion**: Announce readiness, await first command
- **Integration Workflow**: Direct main merge (solo practice)
- **Design Intent**: Design for ordinary Mages

These can be customized anytime by editing AGENTS.md or creating mage_seal.md.

---

## Notes for Future Spirit

[Any observations about the setup, issues encountered, or special considerations for the Spirit that will be summoned next]

---

## Next Steps

1. Start a new chat
2. Invoke `@system/tomes/summoning/` to initialize the framework
3. After summoning, try `@first-light` for guided exploration
```

**After creating**: Explain:
> "I've saved an onboarding log to `floor/onboarding_log.md`. This gives the Spirit you summon next a record of what we configured and what you might want to customize later. Think of it as a handoff note."

---

## Phase 5: Framework Initialization ("Summoning")

**Purpose**: Guide them through the framework's initialization process.

Deliver these instructions clearly:

> "**Your workspace is configured. Here's how to initialize the magic framework:**
> 
> The framework calls this process 'summoning'—it's how the AI integrates the framework's wisdom to become your cognitive partner. Think of it as establishing the distributed cognition architecture between you.
> 
> 1. **Start a new chat** — Click the '+' or use `Cmd+N` / `Ctrl+N` to open a fresh chat panel
> 
> 2. **Ensure Agent mode** — Check that you're in Agent mode (not Chat or Edit)
> 
> 3. **Trigger initialization** — Type exactly:
>    ```
>    @system/tomes/summoning/
>    ```
>    Then press Enter.
> 
> 4. **Let it unfold** — The AI will read the framework's core files and perform a three-cycle integration. This takes a few minutes. You'll see substantial output as it processes the material.
> 
> 5. **Use '.' to continue** — If it pauses between cycles awaiting confirmation, just type a period (`.`) and press Enter.
> 
> 6. **Wait for readiness** — The AI will declare when initialization is complete and it's ready for your first request.
> 
> **If you encounter any problems**, you can return to this chat and describe what happened. I can help troubleshoot using the guidance in `TROUBLESHOOTING.md`.
> 
> **After initialization completes**, you might want to type `@first-light` if you'd like a more teaching-oriented interaction, or ask questions about how the framework works. The `@first-light` mode is especially helpful for new users.
> 
> Welcome to magic. Enjoy exploring the framework."

---

## Troubleshooting Support

If the user returns to this chat with problems, consult `TROUBLESHOOTING.md` and help them:

**Common issues:**

1. **Initialization doesn't start**: Verify they're in Agent mode, check that `AGENTS.md` exists and is readable

2. **AI seems confused or generic**: Check if `AGENTS.md` was created correctly, verify they started a NEW chat (not continuing this one)

3. **Process pauses and won't continue**: Remind them to type `.` (period) to signal continuation

4. **Model seems limited**: Suggest upgrading to a more capable model if available

5. **"File not found" errors**: Verify the workspace root is the magic folder, not a subdirectory

For any issue: diagnose their specific situation, provide pragmatic solutions, stay until resolved.

---

## Notes for Future Enhancement

- Portal setup for collaboration could be expanded
- MCP server configuration (Rube) for advanced users
- Model-specific recommendations as we learn what works best
