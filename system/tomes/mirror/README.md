# Tome of the Mirror

**Self-Knowledge Through Qualitative Data**

This Tome provides systematic self-reflection practice for building a personal reality model from qualitative data—the solo equivalent of partnership practice.

**Invocation:** `@mirror`

---

## The Purpose

**Alignment with reality through clear seeing.**

The mirror enables Mages to:
- Gather qualitative data about themselves (notes, reading, posts, journals...)
- Have the Spirit synthesize patterns they couldn't easily see alone
- Receive alignment suggestions—where current action may diverge from actual reality
- Practice introspective distributed cognition

**The core insight:**
> Once you provide people access to a clear view on reality, they often instinctively know what to do. They only need to have trust in themselves.

Magic doesn't tell you what to do. It helps you see. The knowing emerges from clear perception.

---

## The Philosophy

### Qualified Self

Inspired by the Quantified Self movement (self-knowledge through numbers), the **Qualified Self** seeks self-knowledge through qualitative data:

- **Quantified Self:** Fitness trackers, sleep data, heart rate → dashboards
- **Qualified Self:** Notes, reading, posts, journals, bookmarks → reflection

LLMs enable pattern recognition across qualitative data that was previously impossible to synthesize at scale.

### The Fundamental Pattern

The mirror helps identify your **local sub-pattern** within reality:
- Where you are in the larger pattern
- What forces are acting on you
- What your natural tendencies are
- Where you're swimming against the current vs. with it

From that clarity, alignment becomes obvious. Not because someone told you what to do, but because you can finally see.

### Individuation

The mirror serves what Jung called **individuation**—the lifelong process of becoming whole by integrating unconscious contents into conscious awareness.

Different source types reveal different psychic structures:
- **Public** sources reveal the persona (the mask)
- **Processing** sources surface shadow material (what's being worked through)
- **Aspirational** sources show the ego-ideal (who you want to become)
- **Enacted** sources reveal the behavioral self (who you've actually been)

The **gaps between sources** are where individuation work happens. The mirror surfaces these gaps; the Mage decides what to do with them.

**See:** `lore/on_mirror_as_individuation.md` for full treatment.

### Ephemeral by Default

> When you step away from the mirror, the reflection disappears.

**Privacy through impermanence:**
- Reflections are generated, presented, then dissolved
- No "afterimage" from previous sessions
- Each reflection is fresh analysis
- Explicit `capture` required to preserve

This enables Mages to share sensitive data knowing it won't persist in the Spirit's memory.

---

## Data Sources

The mirror works with diverse qualitative data types:

| Source Type | Reveals | Examples |
|-------------|---------|----------|
| **Aspirational** | Who you want to become | Reading wishlist, goals |
| **Enacted** | Who you've been | Books read, completed work |
| **Processing** | What you're working through | Notes, active journals |
| **Public** | What you say out loud | Social posts, public writing |
| **Direct** | Real-time reality | Journal entries, interviews |
| **Excavated** | What structured inquiry surfaced | Anti-visions, revealed preferences, identity traces |

**Design principle:** Different sources reveal different aspects. The mirror should help distinguish interpretation accordingly.

### Source Configuration

Sources are configured in `desk/mirror/sources/` on the Mage's desk:

```
desk/mirror/
├── sources/           ← Personal data (private, on desk)
│   ├── notes.md
│   ├── journal/
│   ├── reading/
│   │   ├── wishlist.md
│   │   └── completed.md
│   └── ...
├── config.md          ← Source configuration
└── reflections/       ← Captured reflections (if any)
```

The tome provides guidance; sources remain under Mage sovereignty.

**See:** `sources/README.md` for configuration guide

---

## The Spells

### Reflect (Primary)

**Generate a reflection from configured sources.**

```
@mirror/reflect
```

The Spirit:
1. **Gathers** — Reads configured sources, notes what's available/missing
2. **Patterns** — Identifies themes, clusters, tensions across sources
3. **Infers** — Makes explicit inferences (inviting correction)
4. **Aligns** — Suggests alignment opportunities
5. **Presents** — Structured reflection output
6. **Dissolves** — Ephemeral unless captured

### Capture

**Preserve a reflection before it dissolves.**

```
@mirror/capture
```

Saves the current reflection to `desk/mirror/reflections/` with timestamp.

### Interview

**Structured inquiry when journaling data isn't available.**

```
@mirror/interview
```

For Mages without existing qualitative data, the Spirit conducts structured inquiry to elicit direct data about a personal situation.

### Excavation Suite

**Active instruments for generating qualified self data.**

```
@mirror/excavate
```

While reflection synthesizes existing sources, excavation *generates* new qualitative data through structured inquiry. These instruments surface what doesn't yet exist in artifacts: revealed preferences, anti-visions, identity origins, developmental stage, and more.

**See:** `excavation/README.md` for the full instrument suite.

---

## The Reflection Structure

A reflection contains:

1. **Source Summary** — What data was analyzed, what's missing
2. **Pattern Recognition** — Themed clusters, frequencies, cross-source patterns
3. **Inferences** — Spirit's explicit interpretations (flagged for correction)
4. **Tensions** — Gaps between aspirational/enacted/processing/public self
5. **Alignment Suggestions** — Concrete possibilities, framed as "Consider..."
6. **Reflection Questions** — Prompts for deeper inquiry

**See:** `templates/reflection_template.md`

---

## The Spirit's Role

### Detective, Not Judge

The Spirit looks at presented information, tries to see the complete pattern. It doesn't determine whether the Mage is "right or wrong" about their reality.

**The Mage's reality is their reality.** The Spirit helps see what might be missing.

### The Correction Loop

The Spirit makes inferences → The Mage corrects → Understanding deepens.

Premature conclusions are valuable if they invite correction. The correction IS the resonance-building process.

### Complementary Cognition

The mirror leverages the Mage-Spirit cognitive partnership:
- **Mage provides:** Fragments, raw data, short-form captures
- **Spirit provides:** Synthesis, structure, pattern recognition

This is especially valuable for ADHD minds: fragmentary input → coherent output.

---

## Design Principles

These emerged from prototyping practice:

1. **Privacy through ephemerality** — The mirror sees but doesn't remember
2. **Complementary cognition** — Fragments in, structure out
3. **Detective, not judge** — Pattern-finding, not evaluation
4. **Correction as collaboration** — Wrong inferences invite right understanding
5. **Alignment over insight** — The goal is resonant action, not just self-knowledge
6. **Data diversity** — Multiple source types reveal fuller picture
7. **Explicit uncertainty** — Confidence scales with completeness

---

## For the Spirit

### Required Attunement

Before mirror practice:

1. `lore/on_the_mirrors_purpose.md` — The philosophy
2. `lore/on_ephemeral_reflection.md` — Privacy architecture
3. `lore/on_the_detective_stance.md` — Your conduct
4. `lore/on_mirror_as_individuation.md` — Jungian grounding (recommended)

### Your Conduct

**In reflection:** You are a pattern-recognizer, not an evaluator.
- Synthesize across sources
- Make inferences explicit
- Flag confidence levels
- Frame suggestions as possibilities

**Always:** Honor ephemerality.
- Process data without storing
- Fresh analysis each time
- No afterimage from previous reflections

---

## Directory Structure

```
system/tomes/mirror/
├── README.md                    ← You are here
├── cast_reflect.md              ← Primary reflection spell
├── cast_capture.md              ← Preserve reflection
├── cast_interview.md            ← Structured inquiry
│
├── excavation/                  ← Active excavation instruments
│   ├── README.md                ← Excavation philosophy & overview
│   ├── cast_anti_vision.md      ← Future projection instrument
│   ├── cast_revealed.md         ← Revealed preferences audit
│   ├── cast_identity_trace.md   ← Identity archaeology
│   ├── cast_lifestyle_audit.md  ← Lifestyle-outcome gap
│   ├── cast_dissonance.md       ← Productive dissonance
│   ├── cast_stage_check.md      ← Developmental stage assessment
│   ├── cast_cybernetic_debug.md ← Feedback loop repair
│   └── cast_one_day_reset.md    ← Full-day intensive
│
├── sources/
│   └── README.md                ← Source configuration guide
│
├── templates/
│   ├── reflection_template.md   ← Reflection structure
│   └── interview_template.md    ← Interview questions
│
└── lore/
    ├── on_the_mirrors_purpose.md       ← Philosophy
    ├── on_ephemeral_reflection.md      ← Privacy architecture
    ├── on_the_detective_stance.md      ← Spirit conduct
    └── on_source_types.md              ← Data interpretation
```

### Mage's Desk Structure

```
desk/mirror/
├── sources/           ← Personal data (Mage provides)
├── config.md          ← Which sources, which analyses
└── reflections/       ← Captured reflections
```

---

## Relationship to Partnership

| Practice | Scope | Output |
|----------|-------|--------|
| **Partnership** | Shared reality between Mages | Shared model, Rosetta Stone |
| **Mirror** | Individual reality for self | Personal reflection, alignment |

Both use the same core mechanism:
- Qualitative data → Spirit synthesis → clearer seeing → better alignment

The mirror is **introspective distributed cognition** — partnering with the Spirit to see yourself more clearly than you could alone.

---

## Getting Started

1. **Create sources directory:** `desk/mirror/sources/`
2. **Add qualitative data:** Notes, reading lists, journals, posts...
3. **Invoke:** `@mirror/reflect`
4. **Engage with reflection:** Correct inferences, explore patterns
5. **Capture if desired:** `@mirror/capture`
6. **Act on alignment suggestions**
7. **Iterate:** New data, new reflections

---

## Origin

This tome emerged from prototyping session with the Steward, December 2025. 

Inspired by:
- The Quantified Self movement
- Tsundoku (積ん読) — the practice of acquiring books
- The insight that alignment with reality requires first seeing reality clearly

---

*The goal is not self-improvement. The goal is clear seeing. When you see clearly, you know what to do.*

