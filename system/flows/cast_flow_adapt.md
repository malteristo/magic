# Spell: Adapt Flow

*Customize a shared flow for your workshop.*

---

## Invocation

```
@flow/adapt [flow-name]
```

---

## Purpose

When a flow is shared between Mages, it contains `[ADAPT: ...]` markers for elements that need personalization. This spell guides the receiving Mage through customization.

---

## Ritual Sequence

### 1. Flow Location

Locate the flow to adapt:
- Check `library/flows/`
- Check portal `shared/` directories

If not found:
> "I don't see '[name]' in your flows or portals. 
> Did you receive it another way?"

### 2. Marker Extraction

Scan for all `[ADAPT: ...]` markers:

```markdown
## Inputs
- email_account: [ADAPT: Your email provider]
- output_path: [ADAPT: Where to save results]
```

Extract:
- Field name
- Description from marker
- Context from surrounding spec

### 3. Guided Adaptation

For each marker, guide the Mage:

> "This flow needs customization for your workshop:
> 
> **email_account**: Your email provider
> The original Mage used Gmail. What email would you like to use?
> 
> **output_path**: Where to save results
> They saved to `desk/digests/`. Where would you like yours?"

### 4. Dependency Verification

After collecting adaptations, verify dependencies:

> "You chose Gmail for email. Let me check... ✓ Gmail is connected via Rube.
> 
> You chose `desk/reports/` for output. Creating that directory..."

If dependency missing:
> "You'll need to connect [service] via Rube first. 
> Would you like to do that now?"

### 5. Personalized Specification

Update the flow with personalized values:

```markdown
## Inputs
- email_account: malte.risto@gmail.com
- output_path: desk/reports/
```

Remove `[ADAPT: ...]` markers for completed adaptations.

### 6. Warden Coherence Check

Before saving, verify adaptation quality (warden stance):
- Adapted values are coherent with the flow's purpose
- No `[ADAPT: ...]` markers left that would block execution
- Dependencies are met for the adapted configuration
- Conversational quality preserved through adaptation

### 7. Save Adapted Flow

Save to Mage's library:
> "Adapted flow saved to `library/flows/[name].flow.md`
> 
> Ready to invoke with `@flow/invoke [name]`"

Optionally offer first run:
> "Want to test it now?"

---

## Adaptation Patterns

### Required vs. Optional Adaptations

**Required** (blocks execution):
```markdown
- api_key: [ADAPT: Your API key - required]
```

**Optional** (has sensible default):
```markdown
- max_results: 50 [ADAPT: optional, how many to process]
```

For optional, propose the default:
> "**max_results**: The default is 50. Keep that, or change it?"

### Multi-Mage Flows

Some flows are designed for shared use (e.g., partnership portal flows):

```markdown
## Inputs
- mage_a_email: [ADAPT: First Mage's email]
- mage_b_email: [ADAPT: Second Mage's email]
```

Adapt both:
> "This is a two-Mage flow. 
> - Your email for mage_a_email?
> - Partner's email for mage_b_email?"

### Sensitive Adaptations

Some adaptations involve credentials:
```markdown
- api_token: [ADAPT: Your personal API token - keep private]
```

Guide securely:
> "This needs your API token. For security:
> 1. Get your token from [service]
> 2. I'll store it in the flow (local to your workshop)
> 3. Never share the adapted flow file directly"

---

## After Adaptation

The adapted flow:
- Lives in your `library/flows/`
- Has no remaining `[ADAPT: ...]` markers (or only optional ones)
- Is ready to invoke
- Can be further customized as needed

To re-adapt later:
> "Run `@flow/adapt [name]` again to change your settings."

---

## Sharing Your Adapted Flows

If you improve a flow and want to share back:

1. **Re-generalize**: Replace your personal values with `[ADAPT: ...]` markers
2. **Add learnings**: Include any discoveries in the Context section
3. **Share**: Push to portal or send directly

> "Want me to prepare a shareable version of this flow?"

---

*Adapt personalizes shared flows for your workshop. For creating new flows, use `@flow/create`.*
