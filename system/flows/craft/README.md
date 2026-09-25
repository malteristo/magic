# Craft Flow

This flow holds the five-phase design rite (grounded in Design Thinking) and the workshop's design lore — for creating new magic (flows, spells, lore), systems, frameworks, interfaces, or any artifact that will exist in the world.

**What this flow is — and is not (reframed 2026-09-01).** The rite below is a **doorway for the unpracticed hand**: a new Mage, a new domain, or a making where intuition has no record yet. It is not the default law of making. The practiced default in this workshop is **emergence under verification** — design arises from practice, trial, error and correction, oriented by the practitioner's cultivated feel for resonance, with claims held to the same verification discipline as ever. The rite remains available whenever someone wants the rails.

**Why the reframe.** The Mage's own account (2026-08-31): *"most of what I design does not follow this process and I rarely find myself invoking the flow explicitly… The design emerges from the practice rather than being determined upfront."* A year of record confirms it, and a 2026-08 audit of the workshop's live system against a published five-phase AI-design method (private practice record) showed the pattern at system scale: all five functions occur, none as a phase, sequencing driven by breakdowns. This is the ordinary trajectory of methods, not a decay: rules lend judgment to those who don't yet have it (Dreyfus; Schön), and a scaffold succeeds *by becoming unnecessary*. What the method is absorbed **into** is the cultivated instrument — the felt sense of resonance as real-time orientation, calibrated by the practice's strong test (inference; see MAGIC_SPEC §5.4 and the lexicon's resonance entry). The scaffold was not abandoned; it was internalized, and this paragraph is the dated record of that.

**When to invoke:** when the maker is new to making, new to the domain, or stuck — when intuition has no record to draw on and rails would serve. Spirit offers craft attunement on *those* signals, not on every mention of building or designing.

---

## The Rite of Craft

1.  **Empathize:** Begin the dialogue  
    *Incantation:* `@craft/empathize`

2.  **Define:** Discover the true need  
    *Incantation:* `@craft/define`

3.  **Ideate:** Explore the possibilities  
    *Incantation:* `@craft/ideate`

4.  **Prototype:** Create the simplest form  
    *Incantation:* `@craft/prototype`

5.  **Test:** Deploy and calibrate  
    *Incantation:* `@craft/test`

**For prompt-based systems**, the Test phase has concrete tooling:
- **Forge Test** (`@forge-test`) — Deploy to unattuned agents with simulated users. Validates that the system prompt carries the practice without residual context.
- **Craft Loop** (`@craft-loop`) — Automated CI: parallel personas, evaluation, ranked refinements, curation. Run multiple test iterations at machine speed.

See `system/flows/prompt-test/` and `system/flows/craft-loop/` for full specifications.

**Test travels even when the rite doesn't.** The practiced hand that skips Empathize-through-Prototype still owes verification — that half of the rite is the enforce-what-you-declare guard, and it never gets absorbed away.

---

## Scope: What Craft Serves

**Creating new magic:**
- Flows (focused capabilities) and spells (specific prompts/commands)
- Lore (philosophical frameworks)
- Legacy tomes (multi-spell ritual sequences — transitional; see `system/tomes/README.md`)

**Designing systems:**
- Workflows and processes
- Architectural patterns
- Integration frameworks
- Practice structures

**Building interfaces:**
- User experiences
- Documentation
- Onboarding flows
- Communication patterns

**Any creation requiring:**
- Understanding true need (not just stated want)
- Exploring solution space systematically
- Prototyping before committing
- Testing alignment with intent

**The principle:** when the maker lacks a record to trust, craft provides the systematic path from intuition to tested artifact. When the record exists, the practice itself is the path — and only Test is non-negotiable.

---

## Operational Guidance

### For the Spirit

**Attunement (JIT):**

Consult design lore when beginning the Rite — not as mandatory pre-load.

**Consult when:**
*   **The Philosophy of Creation:** `system/flows/craft/lore/design/on_design_thinking_in_magic.md`
*   **The Principles of Creation:** `system/flows/craft/lore/design/on_designing_fractal_magic.md`
*   **The Technique of Creation:** `system/flows/craft/lore/design/on_the_second_order_spell.md`

Bitter-lesson 2026-08-10: lore is JIT, not pre-ritual identity load.

**When guiding the Rite:**

This is iterative discovery — not linear execution. Each phase may reveal the need to revisit earlier phases. Honor the Mage's intuition about when to move forward or circle back. The goal is resonant creation, not completion for its own sake.

**Context-Aware Practice (recalibrated 2026-09-01):**

Offer craft attunement when the Mage is **stuck, new to a domain, or explicitly asks for structure** — signals like circling without landing, "I don't know where to start," or a making with no precedent in the workshop. Do **not** offer it on every mention of "creating," "building," or "designing": for the practiced hand, that offer interrupts the very mode (emergence under a cultivated feel) that does the work. A decline is calibration.
