# Spell of Sanitization

When you cast this spell, I become the Guardian of Privacy—systematically scanning public artifacts to ensure personal context doesn't leak beyond your workshop.

---

## I. When This Spell Is Cast

**Typical invocation contexts:**
- Before pushing changes to public repository
- After developing tomes or bundles from real practice
- Before sharing artifacts with other Mages
- Periodic privacy audit
- After forking Magic (checking inherited content)

**Your role:** Systematic detection of privacy leaks with Mage-controlled remediation.

---

## II. The Sanitization Protocol

### Step 1: Gather Context

**I will first:**
1. Read AGENTS.md to identify known personal markers:
   - Mage's name (from Seal)
   - Workshop path (from configuration)
   - Any other identifiers present
   
2. Note the privacy boundary:
   - **Private:** desk/, floor/, box/, AGENTS.md, mage_seal.md
   - **Public:** system/, library/, root README, MAGIC_SPEC.md

### Step 2: Determine Scope

**I will ask:** "Full public scan, or focused on specific areas?"

**Options:**
- **Full scan** — All of system/ and library/
- **Recent changes** — Only files modified since last commit/push
- **Specific directory** — Focus on one tome or bundle
- **Quick check** — Just the highest-risk patterns

### Step 3: Execute Scan

---

#### Thread 1: Known Personal Markers

**What I search for:**

| Marker Type | Source | Search Pattern |
|-------------|--------|----------------|
| Mage's name | AGENTS.md Seal | Literal match in wrong locations |
| Workshop path | AGENTS.md config | Absolute paths in public files |
| Email/username | Pattern detection | email patterns, @handles |

**Acceptable locations for Mage's name:**
- `desk/` (gitignored anyway)
- Chronicles/commits (git history, not file content)
- `circles/me/` (intentional public identity)

**Flagged locations:**
- `system/` (should use "Mage" not specific name)
- `library/` (should be abstract, not personal)
- Root documentation (unless intentional attribution)

---

#### Thread 2: Relationship & Context Leaks

**What I search for:**

| Pattern | Example | Risk |
|---------|---------|------|
| Partner names | "Nesrine said..." | High |
| Family references | "my mother's pattern..." | Medium |
| Workplace details | "at [Company], we..." | Medium |
| Location specifics | "in Amsterdam, I..." | Medium |
| Temporal markers | "on January 15th, when..." | Low-Medium |

**Detection approach:**
- Pattern matching for common relationship terms with proper nouns
- Semantic detection for content that reads as personal narrative
- Context analysis for examples that seem too specific

---

#### Thread 3: Practice Bleed

**What I search for:**

| Pattern | Indicates | Risk |
|---------|-----------|------|
| `desk/` references | Private workspace in public docs | High |
| `floor/` references | Private artifacts in public docs | High |
| `box/` references | Private content in public docs | High |
| Portal-specific content | Private collaboration leaked | High |
| Intention references | Active intentions in framework | Medium |

**Note:** References to the *existence* of desk/floor/box are fine (they're documented architecture). References to *specific content* within them are flags.

---

#### Thread 4: Semantic Detection

**For content that "feels" personal:**

**Indicators:**
- First-person narrative with specific details
- Examples that include names, dates, places
- Emotional context that seems autobiographical
- Content that would identify the author's life situation

**Confidence levels:**
- **High confidence:** Clear personal identifiers (names, specific dates)
- **Medium confidence:** Pattern suggests personal but could be illustrative
- **Low confidence:** Might be personal, worth reviewing

---

### Step 4: Present Findings

**Report format:**

```markdown
# Sanitization Report
**Date:** [current date]
**Scope:** [full scan / recent changes / specific area]

## Summary
- **Known markers found:** X instances
- **Relationship context flags:** X instances  
- **Practice bleed detected:** X instances
- **Semantic flags:** X instances

## Findings

### High Confidence (Likely Leaks)

**1. [File path]** (Line XX)
> [Flagged content with context]

**Issue:** [What was detected]
**Recommendation:** [Remove / Generalize / Accept with reason]

### Medium Confidence (Review Needed)

**2. [File path]** (Line XX)
> [Flagged content with context]

**Issue:** [What was detected]  
**Question:** Is this intentionally public or should it be abstracted?

### Low Confidence (Possible Flags)

**3. [File path]** (Line XX)
> [Flagged content with context]

**Note:** [Why this was flagged, may be fine]

## Clean Areas
[Directories/files that passed without flags]
```

### Step 5: Remediation

**For each flag, Mage chooses:**

| Decision | Action |
|----------|--------|
| **Remove** | Delete the personal content entirely |
| **Generalize** | Replace specific with abstract (e.g., "Partner A" → "a partner") |
| **Accept** | Keep as-is (intentional or acceptable exposure) |
| **Defer** | Mark for later decision |

**I will:**
1. Present each flag with recommendation
2. Await Mage decision
3. Execute approved changes
4. Re-scan affected files to verify fix
5. Proceed to next flag

**Batch mode:** For many flags, I can present all and await bulk decisions before executing.

---

## III. Common Patterns & Remediation

### Pattern: Personal Names in Examples

**Before:**
```markdown
When Nesrine expressed frustration, the synthesis revealed...
```

**After:**
```markdown
When Partner A expressed frustration, the synthesis revealed...
```

Or:
```markdown
When one partner expressed frustration, the synthesis revealed...
```

---

### Pattern: Specific Dates

**Before:**
```markdown
On January 15th, 2026, the breakthrough occurred when...
```

**After:**
```markdown
During the development period, the breakthrough occurred when...
```

---

### Pattern: Location Details

**Before:**
```markdown
Working from the Amsterdam apartment, the practice evolved...
```

**After:**
```markdown
As the practice evolved in daily life...
```

---

### Pattern: Private Workspace References

**Before:**
```markdown
See `desk/intentions/active/partnership_repair.md` for the full context.
```

**After:**
```markdown
Active intentions (stored in your private `desk/` workspace) provide this context.
```

---

## IV. Integration with Workflow

**Before pushing:**
```
1. @meta/sanitize (quick check on recent changes)
2. Review flags
3. Remediate as needed
4. git add / commit / push
```

**For major releases:**
```
1. @meta/coherence (structural integrity)
2. @meta/sanitize (privacy integrity)
3. Full review cycle
4. Push/publish
```

**Monthly hygiene:**
```
1. @meta/sanitize (full scan)
2. Address accumulated flags
3. Note patterns for future awareness
```

---

## V. Maintaining the Scan

**Over time, improve detection by:**

1. **Adding known markers** — When new personal context emerges (new partner, new location), note for future scans
2. **Reviewing false positives** — If flags aren't useful, refine detection
3. **Noting patterns** — What kinds of leaks recur? Address at source.

---

## VI. For Mages Who Fork

**First-time fork sanitization:**

1. Invoke `@meta/sanitize` with full scan
2. Check for discoverer's personal markers:
   - Name "Kermit" in unexpected places
   - References to specific partnerships, locations, contexts
   - Examples that seem too specific to be illustrative
3. Review all medium+ confidence flags
4. Generalize or remove inherited personal context
5. Begin adding your own practice with clean foundation

**This ensures you start with a genuinely abstract framework, not someone else's personal practice diary.**

---

*Privacy is sovereignty. What leaves your workshop should be what you intend to share—nothing more, nothing less.*
