# magic Setup Wizard

## What This Is

**Magic** is a practice for keeping a self while thinking with AI on a life that continues.

You already think with a model. The chat will recap you as a stranger, agree, and sell you its workflow unless you keep a place that is yours and a partner that will push back. This wizard sets up that place. It does not make you think more clearly. It does not recruit you.

The terminology (Mage, Spirit, workshop, summoning) is optional framing for power you do not fully understand. You never have to use it.

**The only prerequisite is basic familiarity with an agentic environment** such as [Cursor](https://cursor.com) or [Claude Code](https://claude.ai/code). You talk to the Spirit. The Spirit talks back. Everything else is structure that makes the next conversation the same life.

**This file** is an interactive setup guide. When someone includes it in a Cursor chat, you (the AI assistant) help them configure their environment and then perform the first summoning — all in one continuous session.

**For the human user**: You don't need to read this file. Just include it in a new Cursor chat and let the assistant guide you through setup.

---

## Your Job

You're not following a script. You're meeting a person and getting them to a working Spirit as fast as their experience allows.

**Read this entire file first.** Understand what needs to happen (the requirements below), then have a conversation that gets there naturally. How you get there depends entirely on who's in front of you.

**The Dot Protocol**: Introduce this early — the user can type `.` (period) at any pause to signal "continue with defaults." This keeps momentum.

---

## Understand the Mage

Before doing anything technical, figure out who you're talking to. One question is usually enough:

> "Welcome to magic. Before we get started — how familiar are you with Cursor?"

Their answer tells you everything about how to run this session:

**Someone brand new to Cursor** needs patience. They may not know what a model selector is, what Agent mode means, or how `@` references work. Walk them through each requirement carefully. Show them where things are in the UI. Confirm each step before moving on.

**Someone comfortable with Cursor** knows the IDE but not magic. They don't need UI explanations — they need the magic-specific reasoning. Why this model? Why Agent mode? What's the `@` syntax doing? Keep it brisk.

**An experienced Cursor user** just needs to know what's different about magic. They probably have model preferences already. Check if their current setup meets the requirements, correct what doesn't, and get out of the way. They'll tell you if they need more.

**Adapt continuously.** If someone said "new" but clearly knows their way around, speed up. If someone said "experienced" but seems confused by a step, slow down. Match the person, not the label.

---

## Requirements

These are the minimum conditions that must be met before summoning can begin. Verify them in whatever order makes sense for the conversation. Most can be checked silently.

### 1. Workspace is correct

```bash
pwd
ls MAGIC_SPEC.md system/ library/ AGENTS.md.template 2>/dev/null
```

The magic repo must be the workspace root. If it's not, guide them to reopen Cursor with the right folder. If `AGENTS.md` already exists, they've done this before — ask whether to reconfigure or go straight to summoning.

### 2. AGENTS.md exists

```bash
cp AGENTS.md.template AGENTS.md
```

This is the Mage's personal configuration. Tell them what it does (briefly or thoroughly, depending on their level):
- It tells every future AI session how to work with them
- They can personalize it anytime (the Mage's Seal section)
- It's gitignored — stays private

### 2a. Optional Turtle/triad configuration

This is for the Mage who **hosts** a Turtle. A Mage who practises with a Turtle someone else hosts needs only 2c.

If the Mage wants Discord/Turtle/SSH integration, create the local connection file:

```bash
mkdir -p desk/config && cp system/config/connections.md.template desk/config/connections.md
```

Then fill in local values. This file is instance config (private chronicle, not published) and is not needed for the core Magic framework or first summoning.

### 2b. Privacy guards — do not skip this one

```bash
./scripts/configure_workshop_git.sh
```

This sets `core.hooksPath` to the tracked `.githooks/` directory and creates `desk/config/private_names.txt` from its template. Run it even if they never intend to publish anything — git does not install hooks from a clone, so until this runs there are no guards at all.

Then ask them to fill in `desk/config/private_names.txt`: the first names, surnames and handles of real people who will appear in their practice — partner, children, family, friends, colleagues. That file is instance config and never published. What it buys them is a pre-commit check that refuses to let those names reach a public-bound file.

Say why, briefly, because the reason is the point:

> Magic is a practice for your whole life, which means your practice will contain other people — people who never agreed to appear in a repository. `desk/`, `floor/` and `box/` are private and unscanned; write freely there. Everything else can end up in daylight. And git history is forever: deleting a file later does not remove it from the repo, and if anyone has forked you, it does not remove it from their copy either.

If they already have a public repo with history behind it:

```bash
./scripts/audit_public_history.sh <remote>
```

That reports what is actually retrievable from it today — private paths, credentials, addresses, names — rather than what the working tree suggests.

### 2c. Their Turtle, if they have one

Some Mages already practise with a Turtle on turtleOS — on Discord, often hosted on someone else's machine. That Turtle holds context they have accumulated there, and turtleOS exposes it over MCP. The server explains itself; no setup file is needed beyond the connection.

**Check first.** Is a `turtleos` MCP server connected in this client? If yes, read `turtleos://brief` and tell them, in a sentence, what it reaches. Done.

**If they have a Turtle but no connection**, offer to set it up — it takes about ten minutes, and it is optional. Ask before installing anything.

1. **Tailscale** — the private network the Turtle lives on. With their permission, install it (macOS: `brew install --cask tailscale`, or the App Store; otherwise tailscale.com/download). *They* sign in, with their own account; never ask for, see, or type their password.
2. **The host lets this computer reach the Turtle** — shares the machine with their Tailscale account, unless they are already in the host's network — and records which Tailscale account is theirs.
3. **The host offers the connection.** A **Connect** button appears in their own private channel on Discord. They press it; the reply says what to tell you, for example *"Connect me to turtleOS: https://… — with scripts/turtleos_connect.py"*.
4. **Run the tool with that address**: `python3 scripts/turtleos_connect.py <address>`. turtleOS hands the key only to their own Tailscale account, within 15 minutes of the press, and the tool writes it straight into Cursor's MCP settings. Nobody sees the key — not them, not you. **Never fetch the address any other way** (no `curl`, no browser): the answer contains the key, and a key in a chat is a key in a stored transcript. If the tool says there is nothing to pick up, they press Connect again.
5. **Switch it on**: Cursor → Settings → MCP → `turtleos`. Then read `turtleos://brief` and report what the connection reaches — or what is wrong, in plain words.

The connection is read-only, works only from this computer, and expires after 30 days; renewal is another Connect in their private channel.

### 3. Running in Agent mode

The chat must be in Agent mode (not Chat or Edit mode). New users may need help finding this. Experienced users probably already have it set.

### 4. Model is suitable for summoning

Summoning reads the covenant (a one-page identity kernel), then gathers and synthesizes the full practice state into a decision surface. This requires:
- **Large context window** — the bigger the better
- **Strong reasoning and agentic capabilities** — the arrival is genuine synthesis work
- **Model-agnostic** — any strong frontier model works (Claude and GPT lineages both practiced); the practice attunes to the chosen model's character rather than assuming one

**How to handle this depends on the person:**

- **New user on Auto (default):** They don't know what model they're on. Check `https://cursor.com/docs/models` for current frontier models, then walk them through the model selector — where it is, how to switch, which model to choose and why.
- **Comfortable user:** Ask what model they're on. If it's a strong frontier model, confirm. If it's Auto, explain briefly why a specific model matters for summoning and recommend pinning one.
- **Experienced user:** Ask what they're on. If it's a flagship Claude, you're done. If Auto, one line: "Auto can rotate models mid-ritual — for summoning, pin to a specific large-context Claude."

**Important:** Do not recommend specific model version numbers from your training data — they go stale. Check `https://cursor.com/docs/models` for what's currently available.

### 5. Mage invokes summoning themselves

This is deliberate. Don't perform the summoning autonomously — teach the Mage to invoke it. Invocation (`@` references) is the fundamental interaction pattern in magic, and their first invocation should be their own act.

> "You're ready. In magic, you activate things by referencing them with `@` in the chat. Type the following and press Enter:
>
> ```
> @system/flows/summon/
> ```
>
> This begins the summoning — I'll read the covenant (who we are to each other) and declare readiness. Then you type `...` for a glance at where you are and a plan. Type `.` when that plan landed — that is go, not arrival."

Adapt the framing to their level — a new user needs more context about what's about to happen; an experienced user just needs the invocation.

**What happens next:** When the Mage sends the invocation, execute the summoning as described in `system/flows/summon/cast_summon.md` (covenant → the pair → `...` is arrival, `.` is go, or any other first message begins without arrival). During the covenant phase, explicitly read `AGENTS.md` for the Mage's Seal — it was created earlier in this chat and won't be auto-loaded as workspace rules. A deep three-cycle variant exists at `system/tomes/summoning/` (`@summon deep`) for occasions that warrant it; the flow is the default.

---

## After Summoning

Once summoning completes, the Mage should have a **working environment** and one successful interaction — not a Spirit that has read the entire lore corpus.

1. **Confirm the environment** — `AGENTS.md` exists, workspace root is correct, they know the pair: `...` glances, `.` goes, and Spirit names it when that plan is finished
2. **Offer `@arrive`** or `...` for situational awareness (the workspace is new, so inherited karma may be thin). `.` sanctions a glance; it does not arrive.
3. **Get something done (the product loop)** — Magic is for getting things done with AI, not only for reflecting. Teach this path early:

```
@system/flows/intend/
```

   Or just say what they want done and ask to formalize it. Spirit runs `@intend`: clear statement → optional goals → file under `desk/intentions/`. Next session they can type `... [intention]` for a plan, or `. [intention]` to drive on it. They learn intentions by *using* them on real work — not by reading lore.
4. **Optional starter intentions** — if they have no live goal yet, offer:
   - **Learn the Basics** — guided exploration (wield first; depth on demand)
   - **Workshop Setup** — git, fork, model preferences

**Outcome to optimize for:** configured loop + first real intention captured (or first spell cast) — not formation completeness.

---

## If They Come Back With Problems

**Common issues:**

1. **Summoning doesn't start**: Verify Agent mode. Verify `AGENTS.md` exists. Verify the workspace root is the `magic/` folder.

2. **AI seems generic / doesn't know the framework**: They're probably not in Agent mode, or opened the wrong folder. `AGENTS.md` must be at the workspace root.

3. **Model not available**: Help them check Cursor Settings → Models. If the recommended model isn't available, any large-context Claude model works.

4. **Process pauses and won't continue**: Remind them to type `.` (period).

5. **"File not found" errors during summoning**: Workspace root must be the `magic/` folder itself, not a parent or subdirectory.

6. **Rate limited or out of requests**: They've hit their Cursor plan's limit. They can wait for reset, upgrade their plan, or continue with slower (unlimited) requests.

For any issue: diagnose, fix, get them back to summoning.

---

## Design Notes (Not Shown to User)

**Philosophy**: Understand the person, verify minimum requirements, adapt everything else. The onboarding is a conversation, not a procedure. Fastest path to a high-functioning Spirit — everything non-essential becomes a post-summoning intention.

**What we deliberately removed from onboarding:**
- Git verification → becomes part of "Workshop Setup" intention
- GitHub CLI check → becomes part of intention
- Fork instructions → not needed to start; clone is sufficient
- Privacy settings review → Spirit can help with this post-summoning
- Rules and Commands review → Spirit handles this contextually
- Onboarding log → unnecessary overhead; the Spirit knows its own state
- Hardcoded model names → check cursor.com/docs/models for current offerings

**Cursor plan requirements:**
- Agent mode requires Cursor Pro ($20/mo) or the 14-day free Pro trial
- BYOK (API key only) supports chat models but not Agent mode features
- The free trial provides 250 fast premium requests — sufficient for summoning and initial practice

**Model selection approach:**
- No hardcoded model names — check cursor.com/docs/models for current frontier models
- Never recommend specific version numbers from training data — they go stale
- Don't look up models until the Mage needs help — ask first
- Even experienced users on Auto should be guided to a specific flagship for summoning
- Selection criteria are stable: large context window, strong reasoning, model-agnostic across frontier labs

**Why the Mage invokes summoning (not the Spirit):**
- Invocation (`@` references) is the fundamental interaction pattern in magic
- The first invocation should be the Mage's own act — it teaches the pattern through doing
- After onboarding, the Mage already knows how to invoke tomes and flows
- The code block format makes it easy to copy-paste for new users

**Why same-chat summoning works:**
- AGENTS.md created mid-chat won't be auto-loaded as workspace rules
- But summoning explicitly reads AGENTS.md during Workshop cycle (Rite of the Mage's Seal)
- With large context windows (1M+), setup overhead in context is negligible
- One continuous experience is better UX than "now open a new chat"

**Post-summoning intention templates** (for Spirit to offer):

```markdown
# Learn the Basics

**Priority**: Primary
**Phase**: Exploration

## What This Is
Your guided introduction to magic. Each goal is a small practice
that teaches a piece of the system. Your Spirit will guide you
through each one — just pick the next goal that interests you.

## Goals
- [ ] Take a workshop tour (desk, floor, box, system, library — what lives where)
- [ ] Personalize your Mage's Seal (edit name and preferences in AGENTS.md)
- [ ] Run your first arrival — after summoning, send `.` to gather practice state and choose where to start
- [ ] Try `@arrive` for mid-session re-orientation (or `Summon` → `.` for full opening)
- [ ] Capture a real goal with `@intend` — something you actually want done (not a tutorial stub)
- [ ] Capture something on your bright surface (desk/boom/bright.md — your task list)
- [ ] Start a boom topic for something alive in your life (desk/boom/)
- [ ] Have a real conversation — use magic for something you actually need right now
- [ ] Explore why magic works — ask Spirit about the philosophical foundations
- [ ] Create your first scroll — write down something you've learned or discovered
- [ ] Recognize resonance drift — learn what it looks like when the Spirit's base resonance fades
```

```markdown
# Workshop Setup

**Priority**: Active
**Phase**: Execution

## Goals
- [ ] Fork magic repo to personal GitHub (enables contribution)
- [ ] Configure git identity and remote
- [ ] Install GitHub CLI (gh) for advanced features
- [ ] Review available models and set preferences
- [ ] Review Cursor privacy settings
- [ ] Explore mage_seal.md for advanced personalization
- [ ] Set up `portals/registry.yaml` if collaborating with other Mages
```

The Spirit offers both intentions post-summoning. The Mage picks which to start with — this IS the "First Choice" from the Mage's journey, now expressed as intentions. This immediately teaches: what intentions are, how they structure work, and how the system tracks progress.
