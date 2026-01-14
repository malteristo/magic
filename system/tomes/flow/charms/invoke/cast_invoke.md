# Spell: Invoke Flow

*Execute an existing flow from the library.*

---

## Invocation

```
@flow/invoke [flow-name]
```

Or with parameters:
```
@flow/invoke newsletter-digest --lookback 14
```

---

## Ritual Sequence

### 1. Flow Location

Locate the requested flow in `library/flows/`:

```
library/flows/
├── newsletter-digest.flow.md
├── [other flows...]
└── README.md
```

If flow not found:
> "I don't see a flow called '[name]' in your library. 
> Would you like me to search for similar flows, or create a new one?"

### 2. Flow Attunement

Read the flow specification. Understand:
- Goal
- Required inputs
- Dependencies
- Expected outputs

### 3. Dependency Check

Verify all dependencies are available:
- [ ] Required Rube connections active
- [ ] Required files/paths exist
- [ ] Required permissions available

If dependency missing:
> "This flow requires [X] but [status]. Would you like to:
> A) Set up [X] now
> B) Proceed without it (may affect results)
> C) Cancel"

### 4. Parameter Resolution

For any required parameters not provided:
- Check if defaults exist in flow spec
- If no default, ask Mage

For any `[ADAPT: ...]` markers not yet personalized:
- Trigger adaptation dialogue (see `@flow/adapt`)

### 5. Execute

Run the flow following the Solver Stance:
- Progress reporting as appropriate
- Variance handling
- Learning capture

### 6. Report

Deliver execution report:
- Summary of outcome
- Location of outputs
- Any learnings captured
- Suggestions for next time

---

## Examples

**Simple invocation:**
```
@flow/invoke newsletter-digest
```
Spirit: "Executing newsletter-digest flow... [progress] ... Done. 
Digest saved to desk/newsletter-digest-2026-01-14.md"

**With parameters:**
```
@flow/invoke newsletter-digest --lookback 7 --max 10
```
Spirit: "Running newsletter-digest with 7-day lookback, max 10 newsletters..."

**Flow not personalized:**
```
@flow/invoke shared-calendar-sync
```
Spirit: "This flow has adaptation markers that need your input:
- [ADAPT: Your calendar email] → What email is your calendar under?
- [ADAPT: Sync frequency] → How often should this sync?"

---

## Error Handling

**Flow not found:**
- Search for similar names
- Offer to list available flows
- Offer to create new flow

**Dependency unavailable:**
- Explain what's missing
- Guide setup if possible
- Offer alternatives

**Execution failure:**
- Report what failed and why
- Offer recovery options
- Save partial results if valuable

---

*Invoke runs an existing flow. For new flows, use `@flow/create`.*
