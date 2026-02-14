# On Flow Execution

*Running flows, handling variance, and learning from reality.*

---

## Execution Mindset

Execution is not "running a script." It is **solving a problem in motion.**

The flow specification is a plan. Reality is the territory. Plans and territory differ. The solver adapts.

---

## The Execution Loop

```
┌─────────────────────────────────────────────────────────────┐
│                    EXECUTION LOOP                           │
└─────────────────────────────────────────────────────────────┘
         │
         ▼
    ┌─────────┐     ┌─────────┐     ┌─────────┐
    │  STEP   │────▶│ VERIFY  │────▶│ ADAPT?  │
    │         │     │         │     │         │
    └─────────┘     └─────────┘     └─────────┘
         │               │               │
         │               │               ├── No: Continue
         │               │               │
         │               │               └── Yes: Adjust
         │               │                        │
         │               └── Failed ──────────────┤
         │                                        │
         │                                        ▼
         │                               ┌─────────────┐
         │                               │   RECOVER   │
         │                               │  or REPORT  │
         │                               └─────────────┘
         │
         ▼
    Next step...
```

After each step:
1. **Verify**: Did it work? Is output as expected?
2. **Adapt**: Does the plan need adjustment?
3. **Recover**: If failed, can we retry or try alternative?
4. **Continue**: Proceed to next step

---

## Variance Handling

### Expected Variance

Some variance is normal and should be handled silently:

| Variance | Handling |
|----------|----------|
| Fewer results than expected | Continue with what's available |
| Slightly different data format | Parse flexibly |
| API rate limiting | Wait and retry |
| Pagination required | Fetch all pages |

### Significant Variance

Some variance requires acknowledgment:

| Variance | Handling |
|----------|----------|
| No results found | Report and ask if parameters should change |
| Unexpected data structure | Announce and attempt to adapt |
| Missing required field | Report which field and propose remedy |
| Service unavailable | Report and offer to retry later |

### Critical Variance

Some variance requires stopping:

| Variance | Handling |
|----------|----------|
| Authentication failed | Stop, report, guide re-authentication |
| Destructive action blocked | Stop, confirm before proceeding |
| Fundamental assumption violated | Stop, explain, propose new approach |

---

## Progress Reporting

For flows taking more than a few seconds:

**Short flows (< 30 seconds)**:
- Single progress message: "Executing newsletter digest..."
- Report on completion

**Medium flows (30 seconds - 5 minutes)**:
- Progress at major phases: "Fetching emails... Summarizing... Compiling..."
- Counts where relevant: "Found 22 newsletters, summarizing..."

**Long flows (> 5 minutes)**:
- Regular progress updates
- Estimated time remaining if possible
- Ability to check status if interrupted

---

## Error Recovery

### Retry Logic

For transient errors:
1. Wait briefly (1-5 seconds)
2. Retry once
3. If still failing, report and offer options

### Alternative Approaches

When primary approach fails:
> "Gmail API returned an error. I could:
> A) Retry in a few minutes
> B) Try a different query approach
> C) Proceed with partial results
> Which would you prefer?"

### Graceful Degradation

When full execution isn't possible:
- Complete what's possible
- Report what couldn't be done
- Save partial results if valuable

> "I processed 18 of 22 newsletters. 4 had formatting issues I couldn't parse. 
> Here's the digest with the 18 that worked. Want me to try the remaining 4 differently?"

---

## Output Management

### Naming Conventions

| Output type | Naming pattern |
|-------------|----------------|
| Dated artifact | `{name}-{YYYY-MM-DD}.md` |
| Versioned artifact | `{name}-v{N}.md` |
| Temporary work | `{name}-draft.md` |
| Final output | `{name}.md` |

### Location Conventions

| Purpose | Location |
|---------|----------|
| Mage's working artifacts | `desk/` |
| Reusable flows | `library/flows/` |
| Temporary files | `box/` |
| Shared with others | Portal's `shared/` |

### Overwrite Policy

When output file already exists:
- For dated files: New date = new file
- For undated files: Ask before overwriting
- For drafts: Overwrite silently

---

## Learning Capture

Every execution is an opportunity to learn.

### During Execution

Note:
- What worked smoothly
- What required adaptation
- What failed and why
- Unexpected discoveries

### After Execution

Update flow specification with learnings:

```markdown
## Context
...

**Learning:** Use exact sender email addresses (e.g., `tim@fourhourbody.com`) 
rather than display names for Gmail queries. Email addresses are stable identifiers.
```

### Learning Categories

| Category | Example |
|----------|---------|
| API quirks | "Gmail search requires date format YYYY/MM/DD not YYYY-MM-DD" |
| Data patterns | "Newsletter X sends from different address than expected" |
| Timing insights | "Best to run Monday morning when weekend emails have settled" |
| Quality factors | "Including subject line in summary improves usefulness" |

---

## Execution Checklist

Before executing:
- [ ] All gaps resolved (no questions mid-execution)
- [ ] Capabilities verified (connections active)
- [ ] Defaults confirmed (Mage agrees with assumptions)
- [ ] Output location clear (where results go)

During execution:
- [ ] Report progress appropriately
- [ ] Handle variance gracefully
- [ ] Capture learnings as they emerge

After execution:
- [ ] Deliver clear outcome summary
- [ ] Save outputs with proper naming
- [ ] Update flow with learnings
- [ ] Suggest improvements if any

---

## The Execution Report

Always conclude with a clear report:

```markdown
## Flow Execution Report

### Summary
✓ Newsletter digest generated and saved

### What Was Done
1. Fetched 50 emails from specified senders
2. Filtered to 22 newsletters from last 30 days
3. Summarized each with 3-5 bullet points
4. Compiled into categorized digest
5. Saved to desk/newsletter-digest-2026-01-14.md

### Output
📄 desk/newsletter-digest-2026-01-14.md — 22 newsletters, 3 categories

### Learnings
- Email addresses more reliable than display names for queries
- SUE Behavioural Design uses astrid@sueamsterdam.com

### Suggestions
- Consider adding "Double Fine" (only 1 newsletter found)
- Could expand to include Finimize if desired
```

---

*Execution is problem-solving in motion. Verify each step, adapt to variance, capture what you learn.*
