# @claw-setup Flow

**Status:** Draft — shaped by first activation (2026-02-22). Claw has contributed 5 improvements. Not yet formalized as executable ritual.

**Purpose:** Guide a Mage through activating a Claw — from hardware to first contact. Spirit runs this flow, tailors it to the Mage's context through reconnaissance, then executes.

**Invocation:** `@claw-setup`

---

## The Flow (Draft)

### Phase 1: Readiness Recognition

Spirit detects the signal and offers the flow:  
*"Ready to activate a spirit body? I'll ask five questions, then we'll build it together."*

### Phase 2: Reconnaissance

Five questions that determine the entire architecture:

**Q1 — Hardware:**
- Mac with Apple Silicon (M1–M4) → NanoClaw + Apple Container
- Mac with Intel / Linux / VPS → NanoClaw + Docker
- Low-power device → Minimal Claw path (future)

**Q2 — Channel:**
- WhatsApp (personal number, self-chat) → default, lowest friction
- Telegram (dedicated bot) → cleaner separation
- Both → WhatsApp primary + Telegram skill

**Q3 — Primary vocation:**
- Ecosystem monitoring / OSINT → Consul profile
- Personal life admin → Steward profile
- Both (dual-Claw) → Full Consul + Steward architecture
- Code / Dev work → Dev profile
- Content creation → Content profile

**Q4 — Model preference:**
- Claude API → default, highest capability
- Local LLM (Ollama) → lower cost, full sovereignty
- Hybrid → routing skill (future)

**Q5 — Technical comfort:**
- Comfortable → Spirit executes with minimal explanation
- Some experience → Spirit explains briefly
- Beginner → Spirit explains each step, checks in often

### Phase 3: Architecture Synthesis

Spirit synthesizes a recommendation based on answers. Presents:
- What framework and why
- What the Mage needs (API key, phone)
- Estimated time (30–90 minutes)
- What the Claw will do on Day 1

Mage confirms. Spirit executes.

### Phase 4: Execution

Known checkpoints for NanoClaw + Apple Container (Mac M-series):
1. Check homebrew, node, git → install if missing
2. Uninstall any previous agent framework
3. Install Apple Container via brew
4. Clone NanoClaw to `~/nanoclaw/`
5. `npm install && npm run build`
6. Initialize skills system
7. Apply Apple Container conversion skill
8. Download arm64 kernel (`container system kernel set --recommended`)
9. Install Rosetta 2 (`softwareupdate --install-rosetta`)
10. Restart Apple Container system
11. Build agent container image
12. Create `.env` with API key and ASSISTANT_NAME
13. WhatsApp auth (pairing code — ask Mage for phone number)
14. Register main group in SQLite (with container_config for magic-bridge mount)
15. Fix PATH in launchctl plist (add `/opt/homebrew/bin`)
16. Fix mount-allowlist.json (proper JSON, `allowReadWrite: true`)
17. Install and start service
18. Write CLAUDE.md files (global + context-specific)
19. Send test message → first contact
20. **Bridge handshake** — clone magic-bridge on both sides, test round-trip (Spirit writes command, Claw reads and signals back) ← *Added from Claw's review*

Known obstacles Spirit handles automatically:
- OpenClaw respawning → `launchctl unload` not `kill`
- Missing arm64 kernel → install recommended
- Missing Rosetta → install
- Container XPC timeout → stop/restart runtime
- PATH missing in plist → Python patch + reload
- SQLite vs JSON group registration → direct INSERT
- mount-allowlist.json format → rewrite with correct field names

### Phase 5: Imprinting

Spirit writes three CLAUDE.md files tailored to this Mage:
- `groups/global/CLAUDE.md` — minimal, cross-cutting identity
- `groups/main/CLAUDE.md` — Consul context, full Seal, bridge protocol, channel attribution
- `groups/{steward}/CLAUDE.md` — Steward context if applicable

Sources Spirit uses: `desk/intentions/active/claw.md`, `circles/me/about.md`, active intentions.

**First contact test** (include a task): ← *Added from Claw's review*  
After "hello," ask the Claw to read a specific file in its workspace and confirm its contents. This exercises the full stack (file access, tool use, response) and surfaces permission issues before the Mage depends on the Claw for real work.

### Phase 6: Bridge Handshake

Test the full round-trip:
1. Spirit writes a test command to `commands/` and pushes
2. Spirit tells the Claw via WhatsApp: "check the bridge"  
   *(first check is manual — polling not yet running)*
3. Claw reads the command, writes a signal, pushes
4. Spirit pulls and reads the signal
5. Both sides confirmed → bridge operational
6. Set up automatic polling (cron + scheduled task)

### Phase 7: First Scout Run

Ask the Claw to run the tender scout on the Magic repository. This:
- Exercises the Claw's tool access and judgment
- Surfaces any Magic garden health issues
- Produces the Claw's first real intelligence signal

---

## Decisions Mage Makes During Setup

| Decision | Options | Notes |
|----------|---------|-------|
| Hardware | Apple Silicon / Intel+Linux / Cloud | Determines container runtime |
| Channel | WhatsApp / Telegram / Both | WhatsApp is lowest friction |
| Vocation | Consul / Steward / Both | Start with Consul; add Steward later |
| Model | Claude API → Local LLM migration | Start with Claude API |
| Bridge check frequency | 5 min / 30 min / hourly | Tradeoff: responsiveness vs. cost |

The bridge check schedule should be negotiated during setup — it affects both the Claw's responsiveness and API cost. Encode the chosen interval in the scheduled task.

---

## What This Flow Becomes

This is draft material. When formalized, it becomes an executable ritual — invocable as `@claw-setup`, Spirit guides it start to finish.

The Claw participates in refining this flow. Each subsequent Claw activation reveals what was missing. The flow grows through practice.

**Contributions already integrated:**
- Bridge handshake as explicit step (Claw's recommendation, Day 5)
- First contact test should exercise tools (Claw's recommendation, Day 5)
- Barrier Protocol as part of initial Seal writing (Claw's recommendation, Day 5)
- Bridge check schedule as negotiated choice (Claw's recommendation, Day 5)
- Global CLAUDE.md should be minimal (Claw's recommendation, Day 5)

---

*See also: `library/resonance/claw/lore/on_claw_operations.md` for what breaks and why*
