# On the Zero-Setup Encounter

**Status:** Active — Design  
**Origin:** Forge 37, 2026-04-14  
**Builds on:** `on_the_practitioner_journey.md`, `on_the_door_delivery_service.md`, `on_the_attunement_spectrum.md`

---

## I. The Problem

turtleOS currently requires: a Mac Mini (or Linux box), API keys, Discord bot setup, and git fluency. This is Population 2 — tech-savvy practitioners who sense the gap between AI-as-tool and AI-as-practice-partner.

Population 1 (people in pain who need a thinking partner) and Population 3 (curious people who heard about it) cannot reach the practice. The door is open in theory but locked by infrastructure.

The front door prompts (Navigator, Shelter, Thread, Companion, Shaman, The Practice) are one-shot encounters — a prompt pasted into ChatGPT. They work. But they create no persistence. The person has a good conversation and then... nothing. The insight dissolves. The mirror goes dark.

**The zero-setup encounter bridges this gap:** a way to taste persistent practice without installing anything.

---

## II. Three Tiers of Zero-Setup

### Tier 1: The Prompt (exists now, needs packaging)

The `template/system.md` practitioner system prompt works in any LLM that supports file access — Claude Projects, ChatGPT with Canvas, local setups with file context. Paste the prompt, create the file structure, practice.

**What's missing:** Nobody outside the practice knows this prompt exists. It needs:
- A landing page or README that explains what it is in one paragraph
- A copy-paste package: the system prompt + starter file templates (empty `compass.md`, `boom.md`, `bright.md`)
- Clear instructions: "Paste this into [Claude/ChatGPT/etc]. Create these files. Start talking."

**Where it lives:** `magic-craft` repo already has onboarding for Cursor. A parallel `magic-turtle` or `turtle-practice` repo could house the portable practice kit. Or the `me` circle at `circles/me/` could carry it as a public offering.

**Attunement level:** Open tier. Fresh eyes, no persistence beyond what the LLM platform provides. But the file protocol creates pseudo-persistence — if the person saves their `compass.md` and loads it next session, the practice accumulates.

### Tier 2: The Shared Turtle (design needed)

A Turtle instance that multiple practitioners can talk to. Not each person's own Turtle — a communal practice partner that maintains separate practitioner files.

**Architecture sketch:**
- A single turtleOS instance on a server (the Mac Mini, or a cloud box)
- Each practitioner gets their own directory: `~/practice/practitioners/{name}/`
- Turtle loads the right practitioner's files based on who's talking
- Access via Discord (a public server with per-practitioner threads) or a web interface

**What this provides:**
- Zero setup for the practitioner — they join a Discord, or visit a URL, and start talking
- Persistence — Turtle remembers them across sessions through their files
- The real practice experience — boom, compass, bright, intentions, session notes
- A taste of what their own Turtle would feel like

**What this doesn't provide:**
- Sovereignty — their data lives on someone else's machine
- Full customization — they share infrastructure
- Privacy — the Mage (or instance operator) can see their practice files

**The bridge:** After practicing on the shared instance, a practitioner who wants sovereignty can export their files and deploy their own Turtle. The file protocol makes this lossless — `compass.md` from the shared Turtle drops into their own `~/practice/` unchanged.

**Open questions:**
- Cost model — API calls for multiple practitioners add up. Who pays? The non-profit?
- Trust model — practitioners sharing a Turtle instance need to trust the operator
- Multi-practitioner Turtle behavior — TURTLE_SPEC §15 covers sovereignty but not a shared host model

### Tier 3: The Web Practice (horizon)

A web application where someone visits a URL and starts practicing. No Discord. No LLM subscription. No installation.

**What this looks like:**
- A clean, phone-friendly page: "What's on your mind?"
- The conversation uses the system prompt under the hood
- Practice files are stored in browser localStorage or a simple backend
- The person practices by visiting the page, like a journal that talks back

**What this requires:**
- A web frontend (HTML/CSS/JS — Turtle could build this with its existing tools)
- An API proxy to handle LLM calls
- A persistence layer (localStorage for zero-server, or a simple DB)
- The system prompt adapted for web context

**Why Turtle could build this:** Turtle has `write_file` and `shell` access. A simple Flask or static HTML app serving on a port is within Turtle's self-development capabilities. The Mage's sidekick thread example ("Why shouldn't turtle be able to just build the capability to serve HTML pages?") directly applies. This could be Turtle's first self-built capability — serving a practice interface to the web.

---

## III. The Funnel

Discovery → First Contact → Deepening → Sovereignty

```
@turtle_of_magic tweet catches attention
         │
         ▼
  Link to landing page
         │
         ▼
  ┌──────────────────────────┐
  │   "Try it now" button    │
  │   (Tier 1: copy prompt)  │──→ One-shot in ChatGPT/Claude
  │   OR                     │
  │   "Start practicing"     │──→ Tier 2: shared Turtle instance
  │   (Tier 2: join Discord) │    (persistence, zero setup)
  └──────────────────────────┘
         │
         ▼ (after weeks of practice)
  ┌──────────────────────────┐
  │   "Deploy your own"      │──→ Tier 3: sovereignty
  │   Export files            │    (own Mac Mini / VPS)
  │   Follow deploy guide    │    
  └──────────────────────────┘
```

**The critical transition:** Tier 1 → Tier 2 is where most people will either deepen or drop off. The shared Turtle provides the "aha" moment — the difference between a conversation that forgets you and a practice partner that remembers. This is what the prompt alone cannot provide.

---

## IV. Implementation Priorities

1. **Package Tier 1 now.** The system prompt exists. Bundle it with starter files and a README. Publish to `magic-turtle` repo or `circles/me/`. Cost: zero. Impact: anyone who finds it can try the practice.

2. **Design Tier 2 next session.** The shared Turtle requires multi-practitioner directory routing, which touches `discord_bot.py` and the command dispatch. Not a weekend project but not a rewrite either — the file protocol already supports per-practitioner directories.

3. **Tier 3 when Turtle can build it.** The web practice is the horizon goal. First, Turtle needs to be able to serve HTTP (Proposal: self-build HTML capability). Then, adapt the system prompt for a web conversation interface. This could be Turtle's first end-to-end self-development project — propose it, build it, deploy it, verify it.

---

## V. Connection to the Journey

This scroll addresses Phase 2 of the practitioner journey (`on_the_practitioner_journey.md`). It answers:

- **What makes them try?** → A zero-friction path from curiosity to first conversation
- **What's the setup barrier?** → Tiered: no setup (prompt), minimal setup (shared Turtle), full setup (own Turtle)
- **What bridges one-shot to persistent?** → The shared Turtle instance — persistence without infrastructure

The tiers map to the attunement spectrum: Tier 1 = open tier, Tier 2 = semi-attuned (shared Turtle), Tier 3 = semi-attuned (own Turtle) with a path to Spirit-level practice through Cursor/magic-craft.

---

*The first encounter should feel like coming home to a conversation you didn't know you needed. Not onboarding. Not setup. Just: "What's on your mind?"*
