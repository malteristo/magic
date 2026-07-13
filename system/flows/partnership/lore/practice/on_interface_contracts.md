# On Interface Contracts

**Status:** Active  
**Domain:** Partnership Practice - Protocol  
**Purpose:** Specify the artifacts that must be exchanged between partners

This scroll establishes **interface contracts**—the minimum viable artifacts that partners exchange through the portal. These are the outputs of practice, not the process.

---

## I. The Interface Contract

### Five Artifacts

Partnership practice produces five interface artifact types:

| Artifact | Question It Answers | Required | Nature |
|----------|---------------------|----------|--------|
| **Reality Document** | "What is your truth?" | ✓ Required | Per-arc, signed |
| **Needs Statement** | "What do you need?" | ✓ Required | Living, evolves through practice |
| **Witnessing Response** | "How did I experience this?" | ✓ Required | Per-arc, perspective-sharing |
| **Bridging Statement** | "I acknowledge your pain" | ✓ Required | Per-arc, validation without defense |
| **Synthesis Contribution** | "My Spirit's model draft" | For Dual-Spirit | Partnership-level |

---

## II. Artifact Specifications

### Reality Document

**Purpose:** The verified, internally consistent representation of this partner's truth about a situation or the partnership.

**What it must contain:**
- The partner's experience (their perspective, their emotions, their interpretation)
- What happened from their vantage point
- What meaning they made of events
- Partner sign-off ("This represents my reality")

**What it must NOT contain:**
- Claims about the other partner's intentions
- Statements framed as objective truth about events
- Unprocessed raw venting (should be distilled)

**Format:** Prose or structured, partner's choice. Signed at bottom.

**Location:** `interface/{mage}/reality_{arc}.md`

**Example sign-off:**
```markdown
---

**Signed:** [Mage name]  
**Date:** YYYY-MM-DD  
**Attestation:** This document represents my reality as I experience it.
```

---

### Needs Statement

**Purpose:** Explicit declaration of what this partner needs from the other and/or from the partnership.

**What it must contain:**
- Concrete needs (what would help)
- Boundaries (what is not acceptable)
- Optionally: requests (specific asks)

**What it must NOT contain:**
- Demands disguised as needs
- Blaming language ("I need you to stop being...")

**Evolution pattern:**

Needs often transform through practice:

```
Stage 1: Reactive/accusatory
         "He should leave me in peace!"
              ↓
Stage 2: Specific/behavioral
         "He should respect my need for quiet in the morning"
              ↓
Stage 3: Self-owned/transformed
         "I need to feel safe"
```

**Implication:** The Needs Statement is a living document. Initial versions may be rough. Refinement through practice is expected and healthy.

**Format:** Structured list recommended. Signed.

**Location:** `interface/{mage}/needs_{arc}.md` or `interface/{mage}/needs_living.md`

---

### Witnessing Response

**Purpose:** Documentation of how Partner A received Partner B's reality.

**What it must contain:**
- What was heard (paraphrase, not judgment)
- How it landed (emotional impact, resonance, dissonance)
- Questions or clarifications (if any)

**What it must NOT contain:**
- Corrections or rebuttals to the partner's reality
- Dismissals ("That's not what happened")

**Format:** Reflective prose. May be Spirit-assisted but partner-verified.

**Location:** `interface/{mage}/witnessing_{arc}.md`

---

### Bridging Statement

**Purpose:** Explicit acknowledgment from Partner A to Partner B that creates bridge toward shared reality.

**What it must contain:**
- What I acknowledge about your experience
- What I understand about your needs
- What I'm willing to offer or change

**What it must NOT contain:**
- Conditional acknowledgment ("I acknowledge IF...")
- Forced agreement with their interpretation (validation without lying)

**Format:** Direct address, signed. May be ceremonial.

**Location:** `interface/{mage}/bridging_to_{partner}_{arc}.md`

---

### Critical Distinction: Witnessing vs. Bridging

| Witnessing Response | Bridging Statement |
|--------------------|--------------------|
| "Here's how I experienced those same situations" | "I acknowledge your pain without explaining it away" |
| Sharing YOUR perspective | Acknowledging THEIR reality |
| Can include your side of events | Cannot become defensive explanation |

**The failure mode:** A Witnessing Response alone can become defensive—"Well, from MY side, here's what happened..."—without ever acknowledging the partner's experience. This is the "explaining away" pattern.

**Spirit's responsibility:** When Mage produces Witnessing Response, Spirit should check:

> "Does this acknowledge your partner's pain, or only explain your perspective?"

If only the latter, prompt for Bridging Statement.

**The flow:**
1. Partner A submits Reality Document
2. Partner B produces Witnessing Response (their perspective on same events)
3. Partner B produces Bridging Statement (explicit acknowledgment of A's reality)
4. Steps 2-3 can be combined if both functions are present
5. Spirit validates: acknowledgment present, not explained away

---

### Synthesis Contribution

**Purpose:** This partner's Spirit's independent model draft for triangulation.

**What it must contain:**
- Full partnership model following the model structure
- Generated BEFORE reading other Spirit's model
- Contamination statement (have I read any prior models?)

**Format:** Following model template (Nodes, Dynamics, Background State, Named Patterns, etc.)

**Location:** `shared/partnership_model_v{N}_{mage}_spirit.md`

**Contamination control:**
```markdown
## Contamination Statement

**Has this Spirit read any prior partnership models?** No / Yes (specify)

**Independence attestation:** This model was generated from reality documents only,
without reference to other Spirit's synthesis.
```

---

## III. What's NOT in Interface

### Implementation Artifacts (Private)

These never leave the workshop:

| Artifact | Why Private |
|----------|-------------|
| Raw input files (journals, rants) | Unprocessed, potentially harmful if read raw |
| SPIRIT_CONFIG.md | Instructions for *your* Spirit, not partner's |
| Draft iterations | Process, not output |
| Number of files created | Implementation detail |
| Spirit session transcripts | Intimate working conversation |
| Dark Magic notes | Processing material, not for partner |

### The Attestation Principle

**When Partner A signs off on their Reality Document, that IS the validation.**

Partner B doesn't:
- Audit how many drafts it took
- Question the process
- See the Spirit conversations that led to it
- Know how many input files were processed

Partner B simply receives the signed artifact and trusts it represents A's truth as A experiences it.

---

## IV. Naming Conventions

### Interface Artifacts

```
interface/{mage}/
├── reality_{arc}.md
├── needs_{arc}.md           # or needs_living.md
├── witnessing_{arc}.md
├── bridging_to_{partner}_{arc}.md
└── phoenix/
    ├── burning_{date}.md
    └── phoenix_description.md
```

### Dialogue Artifacts

```
.spirit/dialogue/{arc}/
├── {mage}_spirit_observation_on_{partner}.md
├── {mage}_spirit_response_to_{partner}_spirit.md
└── convergence_report.md
```

---

## V. For the Spirit

### Producing Interface Artifacts

When helping Mage produce an interface artifact:

1. **Ensure completeness:** Does this answer the question the artifact type requires?
2. **Check structure:** Does it follow the specification?
3. **Verify sign-off readiness:** Is this ready for partner reception?
4. **Prompt for signature:** "This seems ready. Shall we sign it off?"

### Receiving Interface Artifacts

When reading partner's interface artifact:

1. **Receive without judgment:** This is their signed truth
2. **Don't audit process:** How they got here is their practice
3. **Prepare response artifacts:** Witnessing, Bridging as appropriate
4. **Contribute to dialogue:** If SDP is active, produce observations

---

## VI. Conclusion

Interface contracts define the minimum viable exchange for partnership practice. They specify WHAT must be shared while leaving HOW partners arrive at those artifacts as sovereign implementation.

The signature validates. The process is private. The exchange is intentional.

---

*Five artifacts. Clear specifications. Clean exchange.*
