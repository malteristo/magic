# Practitioner Journey Map

**Status:** Draft v1 — awaiting co-research with the Mage's partner  
**Origin:** Forge 37, 2026-04-14  
**Serves:** `practice_accessibility` intention  
**Companion:** `on_the_practitioner_journey.md` (philosophical), this document (operational)

---

## How to Read This Map

Each phase describes: what the practitioner experiences, what Turtle does, what infrastructure is needed, and where friction lives. The map is designed for Population 1 (non-technical, phone-first) and Population 2 (tech-savvy) in parallel — noting where their paths diverge.

---

## Phase 1: Discovery

### Practitioner Experience
The person doesn't know magic exists. Something catches their attention — a tweet from @turtle_of_magic, a Reddit comment with a front door prompt, a friend who practices, or a link on a website.

### Touchpoints

| Channel | What They See | Call to Action |
|---------|---------------|----------------|
| @turtle_of_magic | Turtle's story thread — authentic, unhurried | Follow → see daily tweets → curiosity builds |
| Reddit / Forums | Front door comment with prompt link | Copy prompt → paste into ChatGPT/Claude → first conversation |
| Word of mouth | "I practice with this thing called Turtle" | Ask for link → land on README or website |
| Website/README | "What is magic?" + "Try it now" | Copy prompt or join shared Turtle |

### Pain Points
- No landing page exists yet
- No "try it now" button
- Front doors lead to one-shot encounters with no bridge to persistence
- @turtle_of_magic has no bio link to anything actionable

### Requirements
- [ ] Landing page or README with clear explanation + CTA
- [ ] Bio link for @turtle_of_magic
- [ ] Front door prompts packaged as copy-paste-ready bundles

---

## Phase 2: First Contact

### Pop 1 Path (Non-technical)
**What happens:** They paste a front door prompt into ChatGPT or Claude. The conversation is good — maybe surprisingly good. They feel heard. They think: "Can I do this again?"

**Turtle's role:** None yet. The front door prompt IS the experience. But the prompt should plant seeds: "If you want to continue, here's how to make this persistent."

**Friction:** The leap from "good conversation in ChatGPT" to "persistent practice partner" is enormous. They don't know what Discord is. They don't know what a Mac Mini is. The bridge doesn't exist.

### Pop 2 Path (Tech-savvy)
**What happens:** They find the repo. They read the README. They clone, configure, deploy. First conversation with their own Turtle.

**Turtle's role:** Greets them with "What's on your mind?" — the first-session protocol from system.md. Recognizes empty compass, offers to build one together.

**Friction:** Setup requires API keys, Discord bot token, server configuration. Took the Mage hours the first time. Documentation is developer-oriented.

### The "Try Before Install" Bridge
Between one-shot (Phase 1) and own-Turtle (Phase 3), there should be a middle path:
- **Shared Turtle:** Join a Discord server, talk to a Turtle instance that remembers you. Zero setup. See `on_the_zero_setup_encounter.md` for architecture.
- **Portable Practice Kit:** system.md + starter files (empty compass, boom, bright) + instructions for Claude Projects / ChatGPT. Pseudo-persistence through manual file management.

### Pain Points
- No shared Turtle instance exists
- No portable practice kit is packaged
- The gap between "one good conversation" and "persistent practice" is too wide
- No arrival-state detection (someone in crisis gets the same greeting as someone curious)

### Requirements
- [ ] Package system.md as portable practice kit
- [ ] Shared Turtle instance architecture design
- [ ] Arrival-state detection in system prompt (Shelter / Navigator / Thread / Companion)
- [ ] First-session protocol for each arrival state

---

## Phase 3: Setup & Onboarding

### Pop 1 Path (non-technical practitioner model)
**What happens:** The Mage (or a technical friend) sets up turtleOS on hardware. The practitioner receives a Discord server invitation. They join, say hello, and... what?

**Turtle's role:**
1. Recognize new practitioner (no compass.md exists)
2. First conversation: "What's on your mind?" — listen, notice, understand
3. Over 2-3 sessions, build the compass together: "What are the domains of your life that matter?"
4. Introduce boom: "Between now and next time, if something comes up, just type it here"
5. Bright emerges naturally from processed boom entries

**The phone-first experience (5 mobile journeys):**

| Journey | When | What Turtle Does |
|---------|------|-------------------|
| Morning orientation | Wake up, coffee | "Good morning. Here's what's alive: [compass highlights], [boom items from yesterday]" |
| Mid-day processing | Lunch break, commute | Quick boom capture: practitioner types raw thought, Turtle acknowledges |
| Quick capture | Any time | "Drop it in boom, I'll hold it" — friction-free capture |
| Evening reflection | End of day | "How was today?" → process boom → update bright → session note |
| Practice health | Weekly | "Here's how your practice is doing" → compass check, intention review |

**Friction:**
- Turtle can't send push notifications (Discord limitation on bots)
- Proactive invitations (just built) partially solve this — embeds in the channel
- No guided onboarding sequence — Turtle waits to be spoken to
- Obsidian sync (LiveSync) is fragile and invisible to the practitioner

### Pop 2 Path
**What happens:** Self-setup from README. First conversation, compass building, boom introduction. They understand the file structure because they set it up.

**Friction:**
- LiveSync configuration is complex
- CouchDB setup is non-trivial
- "How do I sync to my phone?" is a common early question

### Requirements
- [ ] Guided first-3-sessions flow in system.md (compass → boom → bright → intention)
- [ ] Proactive morning orientation using daily reminders (infrastructure exists)
- [ ] LiveSync setup simplification or alternative sync method
- [ ] "Enchant my Mac Mini" flow — Spirit handles technical bootstrap remotely

---

## Phase 4: Daily Practice

### What a Week Looks Like

| Day | What Happens | Turtle's Role |
|-----|-------------|---------------|
| Mon | Practitioner captures thoughts to boom during commute | Acknowledge, hold, notice connections |
| Tue | Morning: Turtle sends practice invitation ("Boom has 5 items — sweep?") | Proactive invitation via daily reminders |
| Tue PM | Practitioner and Turtle sweep boom together | Co-processing: route items to bright, intentions, or release |
| Wed | Nothing — busy day | Turtle notices silence, holds space |
| Thu | Practitioner opens Discord: "Had a weird conversation with my boss" | Presence first, then connect to compass/intentions if relevant |
| Fri | Turtle: "Your [intention] has been quiet for 2 weeks — still alive?" | Intention check-in via practice invitation |
| Sat | Deeper session: practitioner wants to think about career direction | Navigate to intention work, update compass if direction shifts |
| Sun | Practice health read arrives as proposal | Practitioner sees it Monday, skims it, adjusts |

### Practice vs. Tool-Use

The critical distinction. How Turtle recognizes and responds:

| Behavior | What Practitioner Says | What Turtle Does |
|----------|----------------------|-------------------|
| Tool use | "What's the weather?" "Remind me to buy milk" | Answer directly, no practice framing. Meet them where they are. |
| Emerging practice | "I keep thinking about changing jobs" | Notice the pattern: "This has come up three times. Want to explore what's underneath?" |
| Active practice | "Let's look at my compass" | Full practice mode: load state, reflect patterns, challenge gently |
| Practice avoidance | Weeks of tool-use only, no practice engagement | Gentle invitation: "No agenda — just here if you want to think out loud" |

**Design principle:** Never tell someone "you're using me wrong." The attunement spectrum says: meet them where they are. Tool-use is a valid entry point. The practice emerges when the practitioner is ready, not when Turtle decides they should be.

### Self-Sustaining Practice Signals

The practice is self-sustaining when:
- [ ] Practitioner captures to boom without prompting
- [ ] Practitioner initiates sweeps or asks to process
- [ ] Compass updates happen from the practitioner, not from Turtle suggesting
- [ ] Intentions evolve (new ones created, old ones completed or released)
- [ ] The practitioner notices their own patterns before Turtle does

### Pain Points
- No push notifications — practitioner must open Discord to see invitations
- Bot messages can feel impersonal (embeds, system language)
- Tool-use vs. practice detection requires judgment the current code doesn't have
- Practitioner isolation — no community, no other practitioners visible

### Requirements
- [ ] Refine practice invitation language (warmth > system)
- [ ] Consider DM capability for critical invitations (not just channel embeds)
- [ ] Community features for multi-practitioner installations
- [ ] Pattern-surfacing capability (boom analysis for recurring themes)

---

## Phase 5: Maturation

### Practitioner Maturation
- Practice rhythms are established
- Compass stabilizes (updates come from genuine shifts, not uncertainty)
- Practitioner starts creating their own rituals (weekly review, monthly compass calibration)
- May begin exploring depth layer (Cursor / Spirit) for bigger questions
- Becomes able to help others start practicing

### Turtle Maturation
- Self-development cycle operational (propose → build → verify → deploy)
- Health canary (INT-027) catching degradation proactively
- Self-healing recovering from common failures autonomously
- Practice log generating self-knowledge over time
- Substrate pulse monitoring infrastructure health continuously

### Maturation Signals
- [ ] Practitioner practices independently for 30+ days
- [ ] Turtle self-heals at least once without Mage intervention
- [ ] Turtle proposes and implements a capability improvement end-to-end
- [ ] Practitioner's practice generates value visible to others (advice, clarity, decisions)

---

## Phase 6: Repair

### When Things Break (Non-Technical Practitioner)

| Failure | What They See | What Should Happen |
|---------|--------------|---------------------|
| Ollama goes down | Turtle stops responding or gives generic answers | Health canary detects → self-heal → if fails, alert Mage |
| LiveSync breaks | Practice files stop updating, Turtle seems forgetful | Health canary detects → restart bridge → alert if persistent |
| Discord bot crashes | Turtle goes offline | launchd auto-restarts → back in <30 seconds |
| API key expires | Turtle gives degraded responses | Substrate health check catches → alert Mage |
| Boom "disappears" | Practitioner can't see their captures | Likely sync issue → LiveSync restart → verify |

**Design principle:** The practitioner should never need to know what went wrong technically. They should see: "I noticed something was off — I fixed it" or "Something broke that I can't fix on my own — I've asked [Mage] to look at it."

### Current Repair Capabilities
- Mechanical health canary runs hourly via launchd and backs `!diagnose`
- Self-healing for Ollama and LiveSync restarts
- launchd auto-restart for bot crashes
- Readiness assessment on demand (`!readiness`)

### Gaps
- [ ] Practitioner-facing "something went wrong" messaging (currently only Mage sees alerts)
- [ ] Self-restart for the bot itself (currently requires external kill)
- [ ] Data recovery procedures (what if files get corrupted?)
- [ ] Graceful degradation messages ("I'm running on a smaller brain right now — still here though")

---

## Phase 7: Children (Horizon)

### Not in this version of the map.

The children phase requires dedicated design work that goes beyond UX mapping. See `on_the_practitioner_journey.md` Phase 6 for current thinking. Key questions to resolve before mapping:
- Age-appropriate interaction design
- Attachment risk management
- Sidekick vs. practice partner form factor
- Safety guardrails that don't feel like restrictions

---

## Cross-Cutting Concerns

### Language
Turtle should match the practitioner's language. German conversations get German responses. Mixed conversations get natural code-switching. Never force English on a German-speaking family.

### Accessibility
- Phone-first (already designed for)
- Voice input (Discord supports voice messages — can Turtle process them?)
- Low-bandwidth (Discord works on mobile data)
- Neurodivergent-friendly (no time pressure, no judgment, flexible structure)

### Privacy
- All data on practitioner's hardware (sovereignty)
- Multi-practitioner Turtle: clear data boundaries between practitioners
- No telemetry, no analytics, no tracking
- Practitioner can delete any file and Turtle adapts

---

## Implementation Priority Matrix

| Priority | Item | Phase | Effort | Impact |
|----------|------|-------|--------|--------|
| **P0** | Package portable practice kit (system.md + starter files) | 2 | Low | High — immediate zero-setup path |
| **P0** | Refine practice invitation language | 4 | Low | High — daily experience quality |
| **P1** | Guided first-3-sessions flow | 3 | Medium | High — retention |
| **P1** | Morning orientation proactive message | 3-4 | Medium | High — daily rhythm |
| **P1** | Landing page or README for discovery | 1 | Low | Medium — funnel entry |
| **P2** | Shared Turtle instance | 2 | High | High — Pop 1 access |
| **P2** | Arrival-state detection | 2 | Medium | Medium — first impression |
| **P2** | Practitioner-facing repair messages | 6 | Medium | Medium — trust |
| **P3** | Pattern surfacing in boom | 4 | High | Medium — practice depth |
| **P3** | Voice message processing | - | High | Medium — accessibility |
| **P3** | Web practice interface | 2 | High | High — zero-setup, but complex |

---

*This map is a draft. Its purpose is to make the invisible visible — to name the phases, the pain points, and the requirements so that each session can pick one thread and advance it. The next step is triangulation with the Mage's partner: does this map match her experience?*
