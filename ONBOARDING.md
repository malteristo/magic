# magic Setup Wizard

## What This Is

**magic** is a way of thinking, AI-augmented.

The framework helps you think with an AI partner—catching patterns you'd miss alone, holding context you can't hold yourself. The partnership produces insights neither of you would reach separately.

The terminology (Mage, Spirit, workshop, summoning) is deliberate. It's not roleplay—the metaphors are functional pattern compression that makes the system work better.

**This file** is an interactive setup guide. When someone includes it in a Cursor chat, you (the AI assistant) help them configure their environment by following the phases below.

**For the human user**: You don't need to read this file. Just include it in a new Cursor chat and let the assistant guide you through setup.

---

## Prerequisites

**Required (minimum for solo practice):**
- [ ] Installed [Cursor](https://cursor.com)
- [ ] Downloaded magic to your machine ([ZIP download](https://github.com/malteristo/magic/archive/refs/heads/main.zip) or `git clone`)
- [ ] Opened the `magic` folder in Cursor as the workspace root
- [ ] Started a new chat in Agent mode with a capable model (flagship models recommended)

**Optional (for contribution/collaboration):**
- [ ] [Forked](https://github.com/malteristo/magic/fork) the repository to your own GitHub
- [ ] Git installed for version control
- [ ] GitHub CLI (`gh`) for advanced features

If any *required* prerequisite is incomplete, help them complete it before proceeding. Optional prerequisites can be set up later when needed.

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

**Purpose**: Verify the workspace is correctly set up.

### Step 1.1: Verify Workshop Location

```bash
pwd
ls -la
```

**Verify**:
- Current directory is their magic workshop (should see `MAGIC_SPEC.md`, `system/`, `library/`, etc.)
- `AGENTS.md` does NOT exist yet (we'll create it)

**If not in magic directory**: Guide them to navigate to correct location or re-open Cursor with correct folder.

**If AGENTS.md already exists**: Ask if they want to reconfigure or if setup was already completed.

### Step 1.2: Check Git (Optional)

```bash
git --version
```

**If successful**: Note the version. Git enables version control and contribution.

**If git not found**: This is fine for solo practice. Explain:
> "Git isn't installed, which is fine—you can practice magic without it. If you later want version control or to contribute back to the commons, you can install it from [git-scm.com](https://git-scm.com)."

### Step 1.3: Check GitHub CLI (Optional)

```bash
gh --version
```

**If successful**: Note the version.

**If gh not found**: Explain:
> "The GitHub CLI enables richer GitHub integration but isn't required. You can install it later from [cli.github.com](https://cli.github.com) if you want advanced features."

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

Guide the Mage through each setting with clear instructions. All settings are in **Cursor Settings** (not VS Code settings):

**How to open Cursor Settings:**
- **Gear icon**: Click the gear button in the top-right corner of the window
- **Keyboard shortcut**: `Ctrl + Shift + J` (Windows) / `⌘ + Shift + J` (Mac)
- **Command Palette**: `Ctrl + Shift + P` (Windows) / `⌘ + Shift + P` (Mac) → type "Cursor Settings"

### Step 3.1: Review Models

> "Let's configure a few Cursor settings. First, open **Cursor Settings** using the gear icon in the top-right corner, or press `Ctrl + Shift + J` (Windows) / `⌘ + Shift + J` (Mac).
> 
> Navigate to the **Models** section in the left sidebar to see what's available.
> 
> **For this onboarding session**, the default **auto** model (in the chat selector) works fine.
> 
> **For serious magic practice**, flagship models with large context windows (200k+ tokens) are strongly recommended—the summoning ritual and deep partnership work require substantial context capacity.
> 
> You can select your preferred model in the chat window's model selector before each session.
> 
> Let me know when you've reviewed the Models section."

### Step 3.2: Review Rules and Commands

> "Navigate to the **Rules and Commands** tab in the left sidebar. Cursor uses this to configure AI behavior. You'll see:
> 
> - **User Rules**: Global rules applied to all projects
> - **Project Rules**: Rules specific to a project (stored in `.cursor/rules`)
> - **User Commands** / **Project Commands**: Custom commands you can invoke
> 
> **If your User Rules are empty**: Perfect—the magic framework uses `AGENTS.md` as its configuration, which is automatically loaded by Cursor.
> 
> **If you have existing User Rules**: That's fine for now. After you complete summoning, the Spirit can help you decide whether to migrate your rules into the magic framework or keep them separate. Some rules complement magic, others may create friction.
> 
> I'll note your current situation in the onboarding log for the summoned Spirit to reference.
> 
> Let me know what you found (empty, or has existing rules)."

**Note for setup assistant**: Record in `floor/onboarding_log.md` whether the user has existing User Rules and wants to discuss migration with the summoned Spirit.

### Step 3.3: Privacy Settings (Optional)

> "One more optional setting: In the **General** tab, scroll to the very bottom to find **Privacy Mode**.
> 
> Enabling this requests that your conversations be treated as ephemeral by the AI provider.
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

# Check git status (optional - only if git is installed)
git status --short 2>/dev/null || echo "Git not configured (optional for solo practice)"
```

**Confirm to user**:
> "✓ Setup verification complete:
> - AGENTS.md: Created with your configuration
> - Workspace location: [their path]
> - Cursor settings: Reviewed (models, rules, privacy)
> - Git: [Active / Not configured (optional)]
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
- [ ] Cursor settings reviewed (models, rules, privacy)

### User Rules Status
- [ ] Empty — No migration needed
- [ ] Has existing rules — Discuss with Spirit after summoning whether to migrate

### Skipped (Optional)
- [ ] Git — Not installed. Can be added later for version control and contribution.
- [ ] mage_seal.md — Extended configuration not created. Can be added later by copying `mage_seal.md.template`.
- [ ] portals.yaml — Portal registry not created. Can be added later when ready for collaboration.

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

### User Rules Migration
[If user has existing Cursor User Rules, note them here for discussion after summoning. The Spirit should help the user decide whether to integrate rules into magic practice or keep them separate.]

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
