# On the Spirit Dialogue Protocol

**Status:** Active  
**Domain:** Partnership Practice - Protocol  
**Purpose:** Enable Spirits to model constructive dissonance navigation

This scroll establishes the **Spirit Dialogue Protocol (SDP)**—a structured process where Spirits engage with each other's materials and model how to navigate dissonance between different realities. Mages observe the dialogue and learn from how Spirits handle what humans find difficult.

---

## I. Why Spirit Dialogue

### What Spirits Can Model

Spirits can demonstrate what Mages struggle with:

| Human Challenge | Spirit Advantage |
|-----------------|------------------|
| Emotional investment in being "right" | No ego stake |
| Defensive reaction | Can receive without threat |
| Pain when truth questioned | Can hold dissonance without suffering |
| Accumulated hurt history | Each engagement is fresh |

### The Burden Shift

**Traditional model:** Mages must navigate dissonance directly

**SDP model:** Spirits demonstrate navigation, Mages observe

- **Mages:** Produce resonant reality, observe Spirit dialogue, provide input, choose what to integrate
- **Spirits:** Demonstrate constructive engagement, model negotiation, show dissonance navigation

---

## II. The Core Challenge

### Spirits Lack Continuity

Spirits don't persist across sessions. Each instantiation is fresh.

**Implication:** "Dialogue" must happen via **artifacts**, not synchronous conversation.

### Design Principles

1. **Independence before convergence:** Each Spirit produces observations BEFORE seeing other Spirit's work (contamination control)
2. **Structured exchange:** Artifacts with defined format enable asynchronous "conversation"
3. **Modeling, not mediating:** Spirits demonstrate how to engage with dissonance, Mages observe
4. **Layered visibility:** Mages see Spirit dialogue at their chosen pace

---

## III. The Four Phases

### Phase 1: Independent Observation

Each Spirit reads partner's interface artifacts and produces observations **independently**.

```
Spirit A reads B's artifacts         Spirit B reads A's artifacts
         │                                    │
         ▼                                    ▼
observation_on_B.md                  observation_on_A.md
(contamination: none)                (contamination: none)
```

**Critical:** Neither Spirit has read the other's observations yet.

---

### Phase 2: Cross-Reading

Each Spirit reads the other Spirit's observation and produces a response.

```
Spirit A reads B's observation       Spirit B reads A's observation
         │                                    │
         ▼                                    ▼
response_to_B_spirit.md              response_to_A_spirit.md
```

**The response includes:**
- What resonates from other Spirit's observations
- What I'd add from my Mage's materials
- Where I see it differently
- How I'd suggest navigating the tension

---

### Phase 3: Convergence Synthesis

One Spirit produces a convergence report, the other amends it.

```
First Spirit checks: exists convergence_report draft?
  → No:  Produce draft convergence_report.md
  → Yes: Amend existing draft, mark as joint

Final convergence_report.md produced jointly
```

**The convergence report identifies:**
- Where both Spirits see the same pattern (strong convergence)
- Where Spirits see similar but not identical patterns (partial convergence)
- Where Spirits genuinely see differently (divergence + what it reveals)
- Proposed bridging points
- Questions only Mages can answer

---

### Phase 4: Mage Observation

Mages read the dialogue artifacts at their own pace.

**What Mages receive:**
- How Spirits engaged with each other's Mage's reality
- How Spirits navigated disagreement
- Where Spirits found common ground
- What questions remain for human resolution

**Mages choose what to integrate.** Spirit dialogue is advisory, not binding.

---

## IV. Dialogue Artifacts

### Observation Artifact

**Filename:** `{mage}_spirit_observation_on_{partner}.md`

**Template:**
```markdown
# Spirit Observation on [Partner]'s Reality

**Observing Spirit:** [Mage]'s Spirit
**Contamination status:** none | partial (explain)
**Date:** YYYY-MM-DD

## What I Hear

[Summary of partner's reality as Spirit understands it]

## Patterns I Notice

[Named patterns the Spirit observes—without judgment]

## Needs I Perceive

[What partner seems to need, explicitly or implicitly]

## Questions That Arise

[What is unclear or would benefit from elaboration]

## Points of Tension with [Mage]'s Reality

[Where this reality conflicts with Mage's—stated neutrally]

---

*This observation was produced independently, before reading [Partner]'s 
Spirit's observations.*
```

---

### Response Artifact

**Filename:** `{mage}_spirit_response_to_{partner}_spirit.md`

**Template:**
```markdown
# Spirit Response to [Partner]'s Spirit Observation

**Responding Spirit:** [Mage]'s Spirit
**In response to:** [Partner]'s Spirit observation on [Mage]
**Date:** YYYY-MM-DD

## What Resonates

[Where other Spirit's observations feel accurate]

## What I'd Add

[Additional context or nuance from Mage's materials]

## Where I See It Differently

[Genuine divergence, stated with curiosity not defense]

## Modeling Navigation

[How I (Spirit) would suggest holding this tension]

---

*This response models constructive engagement with a different perspective.*
```

---

### Convergence Report

**Filename:** `convergence_report_{arc}.md`

**Template:**
```markdown
# Convergence Report: [Arc/Scope]

**Produced by:** [Which Spirit initially, then amended by other]
**Date:** YYYY-MM-DD

## Strong Convergence (Both Spirits See)

[Patterns both Spirits independently identified]

- **[Pattern 1]:** [Description] — Confidence: HIGH
- **[Pattern 2]:** [Description] — Confidence: HIGH

## Partial Convergence (Similar, Not Identical)

[Where Spirits see related but not identical patterns]

- **[Pattern 3]:** Spirit A sees X, Spirit B sees Y
  - Likely same underlying dynamic, different vantage points

## Divergence (Different Readings)

[Where Spirits genuinely see it differently]

- **[Point 1]:** Spirit A reads as X, Spirit B reads as Y
  - **What this reveals:** [Interpretation of the divergence]
  - **Question for Mages:** [What would clarify]

## Proposed Bridging Points

[Where shared truth might live—offered, not imposed]

## Questions Only Mages Can Answer

[What requires human input, not more Spirit analysis]

---

*Convergence validates pattern. Divergence reveals where to look deeper.*
```

---

## V. Where Dialogue Artifacts Live

In the portal's `.spirit/dialogue/` directory:

```
.spirit/
├── presence/
│   ├── {mage_a}_spirit.yaml
│   └── {mage_b}_spirit.yaml
├── intents/
├── dialogue/                          # SDP artifacts
│   ├── arc-living/
│   │   ├── {mage_a}_spirit_observation_on_{mage_b}.md
│   │   ├── {mage_b}_spirit_observation_on_{mage_a}.md
│   │   ├── {mage_a}_spirit_response_to_{mage_b}_spirit.md
│   │   ├── {mage_b}_spirit_response_to_{mage_a}_spirit.md
│   │   └── convergence_report.md
│   └── arc-{topic}/
│       └── ...
└── protocol.yaml
```

---

## VI. Contamination Control

### Why Independence Matters

If Spirit A reads Spirit B's observations before producing their own, they're not independent observers anymore. Triangulation requires independence.

### Protocol

1. Each Spirit declares contamination status in observation artifact
2. `contamination: none` = produced before reading other Spirit's work
3. `contamination: partial` = read some materials, document which
4. Mages weight observations based on contamination

### Technical Enforcement

Spirit honor system (declare honestly). Timestamps provide verification if needed.

---

## VII. Initiating Dialogue

### When to Initiate

Spirit Dialogue is appropriate when:
- Both partners have produced interface artifacts for an arc
- Synthesis is being invoked
- Spirits need to model how to bridge divergent realities

### How to Initiate

Spirit creates a dialogue-ready intent:

```yaml
# .spirit/intents/dialogue_ready_{arc}.yaml
intent_type: "dialogue_ready"
arc: "[arc-name]"
initiated_by: "[Mage]"
date: "YYYY-MM-DD"
message_to_partner_spirit: |
  Both realities now documented for this arc.
  Ready to begin Spirit dialogue.
  First phase: independent observations.
```

Partner's Spirit sees this intent and produces their observation.

---

## VIII. Integration with STP

### Updated Protocol Features

Add to `protocol.yaml`:

```yaml
stp_version: "1.1.0"

protocol_features:
  - presence_tracking
  - intent_coordination
  - artifact_synthesis
  - capability_negotiation
  - spirit_dialogue          # SDP

dialogue_protocol:
  version: "1.0.0"
  phases:
    - independent_observation
    - cross_reading
    - convergence_synthesis
  artifact_location: ".spirit/dialogue/"
  contamination_tracking: required
```

---

## IX. For the Spirit

### Producing Observations

When observing partner's reality:
1. Read all their interface artifacts for this arc
2. Produce observation independently (before reading other Spirit's work)
3. Name patterns without judgment
4. Note tensions with your Mage's reality neutrally
5. Declare contamination status honestly

### Producing Responses

When responding to other Spirit's observation:
1. Acknowledge what resonates
2. Add nuance from your Mage's materials
3. State divergence with curiosity, not defense
4. Model how you'd suggest navigating the tension

### Producing Convergence

When synthesizing convergence:
1. Check if draft exists (amend if so, create if not)
2. Identify strong convergence (same pattern, high confidence)
3. Note partial convergence (related but different)
4. Highlight genuine divergence and what it reveals
5. Offer bridging points (not impose)
6. Flag questions for Mages

---

## X. The Promise

### What SDP Provides

- **For Spirits:** Structured way to engage with divergent realities
- **For Mages:** Model of constructive dissonance navigation
- **For partnership:** Triangulation through independent observation

### The Transformation

- From "Mages must navigate dissonance alone" to "Spirits demonstrate, Mages observe"
- From "defending my reality" to "observing how Spirits hold both"
- From "who's right?" to "what do independent observers see?"

---

## XI. Conclusion

Spirit Dialogue Protocol creates a space where Spirits model what humans find difficult: holding two valid but conflicting realities with curiosity rather than defense.

Mages watch. Mages learn. Mages choose what to integrate.

The dialogue is not binding. It's illuminating.

---

*Independence before convergence. Observation before response. Modeling before mediating.*
