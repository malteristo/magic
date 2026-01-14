# On Flow Resolution

*How Spirit interprets and resolves flows from goal to executable plan.*

---

## The Resolution Challenge

A Mage says:
> "I want my newsletters summarized weekly"

Spirit must transform this into:
1. Which newsletters?
2. From which email account?
3. What counts as a "newsletter"?
4. What format for summaries?
5. Where to save the output?
6. When exactly is "weekly"?

**Resolution** is the process of filling these gaps—through inference, research, and dialogue.

---

## Resolution Strategies

### 1. Inference from Context

Many gaps can be filled by context:

| Gap | Inference Source |
|-----|------------------|
| Email account | Rube connections (what's connected?) |
| Newsletter definition | Common patterns (regular sender, long-form content) |
| Output location | Workshop convention (`desk/` for artifacts) |
| Timing | Mage's stated preference or reasonable default |

**Principle**: Infer what's inferrable. Only ask about what requires Mage input.

### 2. Research from Capabilities

Before proposing an approach, research what's possible:

```
1. RUBE_SEARCH_TOOLS → What external capabilities exist?
2. library/flows/ → Does a similar flow already exist?
3. Workshop scan → What's already set up?
```

**Example resolution**:
- Goal mentions "email" → Check Rube for email providers
- Gmail is connected → Use Gmail APIs
- Goal mentions "summarize" → LLM capability available
- Combined: Can achieve goal automatically

### 3. Dialogue for Ambiguity

When inference and research leave gaps, ask:

**Good questions** (necessary, specific):
- "Which newsletters should I include? All, or specific senders?"
- "Should summaries be bullet points or paragraphs?"

**Bad questions** (unnecessary, vague):
- "How do you want me to do this?" (too open)
- "Should I use Gmail?" (researchable)
- "What format for the date?" (inferrable)

**Batching principle**: Collect questions and ask them together, not one at a time.

---

## The Resolution Sequence

```
┌────────────────────────────────────────┐
│           GOAL STATEMENT               │
│  "Summarize my newsletters weekly"     │
└────────────────────────────────────────┘
                    │
                    ▼
┌────────────────────────────────────────┐
│        EXPLICIT EXTRACTION             │
│  - Action: summarize                   │
│  - Object: newsletters                 │
│  - Frequency: weekly                   │
└────────────────────────────────────────┘
                    │
                    ▼
┌────────────────────────────────────────┐
│        IMPLICIT INFERENCE              │
│  - Source: email (implied)             │
│  - Output: text artifact (implied)     │
│  - Location: desk/ (convention)        │
└────────────────────────────────────────┘
                    │
                    ▼
┌────────────────────────────────────────┐
│        CAPABILITY RESEARCH             │
│  - Gmail connected: yes                │
│  - LLM available: yes                  │
│  - Existing flow: none matching        │
└────────────────────────────────────────┘
                    │
                    ▼
┌────────────────────────────────────────┐
│        GAP IDENTIFICATION              │
│  - Which newsletters? (must ask)       │
│  - Summary format? (can default)       │
│  - Exact timing? (can default)         │
└────────────────────────────────────────┘
                    │
                    ▼
┌────────────────────────────────────────┐
│        RESOLUTION DIALOGUE             │
│  "Which newsletters should I include?" │
│  (with proposed default if possible)   │
└────────────────────────────────────────┘
                    │
                    ▼
┌────────────────────────────────────────┐
│        RESOLVED FLOW                   │
│  Complete specification ready for      │
│  execution                             │
└────────────────────────────────────────┘
```

---

## Resolution Heuristics

### Sender Resolution

**Learning from practice**: Use email addresses, not display names.

| Mage says | Spirit resolves to |
|-----------|-------------------|
| "Tim Ferriss newsletter" | `from:tim@fourhourbody.com` |
| "School of Life" | `from:hello@e.theschooloflife.com` |

If email address unknown, ask: "What email address does [X] send from?"

### Time Resolution

| Mage says | Spirit resolves to |
|-----------|-------------------|
| "weekly" | Sunday morning (or ask preference) |
| "monthly" | 1st of month |
| "daily" | Morning (or ask preference) |
| "last week" | 7 days back from now |
| "recent" | 7-14 days (or ask) |

### Output Resolution

| Context | Default location |
|---------|-----------------|
| Artifact for Mage | `desk/` |
| Reusable flow | `library/flows/` |
| Temporary work | `box/` |
| Shared content | Portal's `shared/` |

### Scope Resolution

When scope is ambiguous:
- Start conservative (fewer items, shorter timeframe)
- Offer to expand: "I found 10 newsletters. Want me to include more?"

---

## Existing Flow Discovery

Before creating new flows, check for existing ones:

```python
# Conceptual pattern
existing = scan("library/flows/")
for flow in existing:
    if goal_matches(flow.goal, mage_goal):
        return propose_existing_flow(flow)
```

When an existing flow matches:
> "I found an existing flow 'newsletter-digest' that does something similar. 
> Should I use that as a base, or create a new one?"

---

## Resolution Quality

A well-resolved flow:
- Has no ambiguous elements
- Uses verified capabilities (tested connections)
- Includes sensible defaults for optional elements
- Documents any assumptions made
- Is ready for immediate execution

A poorly-resolved flow:
- Contains questions for Mage mid-execution
- Assumes capabilities that might not exist
- Uses defaults that might not match Mage preference
- Will fail on first run due to missing information

**Test**: Could you execute this flow right now without asking anything else?

---

## Resolution Failures

When resolution cannot complete:

**Missing capability**:
> "This flow requires Outlook access, but only Gmail is connected. 
> Would you like to connect Outlook, or should we find an alternative?"

**Irreconcilable ambiguity**:
> "I'm not sure whether you want daily summaries or a weekly digest. 
> Which would serve you better?"

**Conflicting requirements**:
> "You mentioned 'all newsletters' but also 'only substantive content.' 
> Should I filter out promotional newsletters?"

Always explain *why* you're asking, not just *what* you need.

---

*Resolution transforms intention into specification. The goal is a flow ready for execution with no remaining questions.*
