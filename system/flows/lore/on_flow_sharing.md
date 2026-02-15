# On Flow Sharing

*Portability and adaptation—how flows move between Mages.*

---

## The Sharing Challenge

A flow created by Mage A contains:
- **Universal elements**: Goal, logic, structure, learnings
- **Personal elements**: Their email, their paths, their preferences

For Mage B to use it, they need the universal elements intact while substituting their personal elements.

---

## The Adaptation Marker

The solution: `[ADAPT: description]` markers.

```markdown
## Inputs
- email_account: [ADAPT: Your email provider]
- output_path: [ADAPT: Where to save the digest]
- newsletter_senders: [ADAPT: Email addresses of newsletters you want]
```

These markers:
- Identify what needs customization
- Explain what's needed
- Are easy to spot and process
- Preserve the flow's logic while allowing personalization

---

## Creating Shareable Flows

When creating a flow intended for sharing:

### 1. Identify Personal Elements

Ask: "What would another Mage need to change?"

Common personal elements:
- Email addresses
- File paths
- API credentials
- Personal preferences (format, timing)
- Service-specific IDs

### 2. Add Markers

Replace personal values with markers:

**Before (personal):**
```markdown
- email: mage@example.com
- output: desk/newsletter-digest.md
```

**After (shareable):**
```markdown
- email: [ADAPT: Your Gmail address]
- output: [ADAPT: Where to save the digest, e.g., desk/digests/]
```

### 3. Include Context

Add learnings and context that help any Mage:

```markdown
## Context
This flow processes newsletter emails and creates a summary digest.

**Learning:** Use exact sender email addresses (e.g., `tim@fourhourbody.com`) 
rather than display names for reliable Gmail queries.

**Tip:** Run monthly for best results; weekly may have few newsletters.
```

### 4. Document Dependencies

Be explicit about what's needed:

```markdown
## Dependencies
- Gmail: Read access via Rube MCP
- LLM: For summarization (available by default)

## Adaptations
**Required before first use:**
- Connect Gmail via Rube (RUBE_MANAGE_CONNECTIONS)
- Provide your newsletter sender list
```

---

## Sharing Channels

### Portal Sharing

For partnership portals or circles:

1. Place shareable flow in `shared/flows/`
2. Partner runs `@flow/adapt [name]`
3. Spirit guides them through personalization

```
portals/
└── partner-partnership/
    └── shared/
        └── flows/
            └── weekly-reflection.flow.md
```

### Direct Sharing

For one-off sharing:

1. Send the `.flow.md` file directly
2. Recipient saves to their `library/flows/`
3. Runs `@flow/adapt [name]`

### Publishing Flows

For wider distribution (future capability):

1. Flows could be published to a shared repository
2. Other Mages browse and import
3. Automatic adaptation on import

---

## Receiving Shared Flows

When you receive a flow:

### 1. Save to Library

Place in `library/flows/[name].flow.md`

### 2. Run Adaptation

```
@flow/adapt [name]
```

Spirit will:
- Find all `[ADAPT: ...]` markers
- Guide you through each one
- Verify your dependencies
- Save the personalized version

### 3. Test Run

```
@flow/invoke [name]
```

Verify it works with your configuration.

### 4. Iterate

Adjust as needed. Your version is now yours to modify.

---

## Sharing Back

If you improve a shared flow:

### 1. Re-generalize

Replace your personal values with markers again:
```
@flow/adapt [name] --prepare-for-sharing
```

### 2. Add Your Learnings

Update the Context section with what you discovered:

```markdown
**Learning (from Mage B):** The flow works better when run 
on Monday morning after weekend emails have settled.
```

### 3. Share

Push back to portal or send directly.

---

## Multi-Mage Flows

Some flows involve multiple Mages (e.g., partnership check-ins):

```markdown
## Inputs
- mage_a_email: [ADAPT: First Mage's email]
- mage_b_email: [ADAPT: Second Mage's email]
- shared_artifact_path: [ADAPT: Path in shared portal space]
```

Both Mages adapt the same flow, but with complementary values.

---

## Privacy Considerations

### What to Share

- Flow logic and structure
- Generic learnings
- Helpful context

### What NOT to Share

- Personal email addresses
- API keys or tokens
- Private file paths
- Personal preferences (unless helpful as examples)

### Marker Guidance

For sensitive fields, add notes:

```markdown
- api_token: [ADAPT: Your personal API token - keep private, never share]
```

---

## Flow Versioning

When flows evolve:

```markdown
## Origin
Created by: [Mage name]
Version: 2.0
Created: 2026-01-14
Updated: 2026-01-20 — Added parallel fetching, improved error handling

## Changelog
- v2.0: Added parallel fetching for faster execution
- v1.1: Added email address learning
- v1.0: Initial version
```

Receiving Mages can see what changed and decide whether to update.

---

*Sharing multiplies the value of flows. What one Mage discovers, all can benefit from.*
