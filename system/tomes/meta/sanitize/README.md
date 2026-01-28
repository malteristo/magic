# Charm of Sanitization

A charm for ensuring personal context doesn't leak into public artifacts—protecting outbound privacy before sharing magic with other practitioners.

## Purpose

Magic emerges from authentic practice with real context. Partnership struggles, personal intentions, lived experiences—these inform the framework's development. But the framework is meant to be shared publicly while practice remains private.

**The risk:** Personal details accidentally bake into tomes, scrolls, and bundles during development. What was meant to illustrate becomes identifying. What was meant to teach reveals.

**This charm provides:** Systematic scanning of public-facing artifacts to catch privacy leaks before they leave your workshop.

**Invocation:** `@meta/sanitize`

---

## The Privacy Model

### What's Private (Stays Local)

| Location | Nature | Protection |
|----------|--------|------------|
| `desk/` | Working documents, intentions | Gitignored |
| `floor/` | Artifacts, outputs | Gitignored |
| `box/` | Unintegrated knowledge | Gitignored |
| `AGENTS.md` | Your Seal configuration | Gitignored |
| `mage_seal.md` | Your Seal source | Gitignored |

### What's Public (Shared)

| Location | Nature | Risk |
|----------|--------|------|
| `system/` | Core framework | Could contain leaked context |
| `library/` | Wisdom bundles | Could contain personal examples |
| `README.md` | Root documentation | Could reference private details |
| `MAGIC_SPEC.md` | Law | Should be abstract, not personal |

### What's Intentionally Shared

| Location | Nature | Consideration |
|----------|--------|---------------|
| `portals/` | Shared practice spaces | Controlled sharing with known Mages |
| `circles/` | Topic-centered collaboration | Public identity, machine-readable |

---

## What This Charm Detects

### Personal Identifiers

- **Names:** Your name, partner names, family, friends, colleagues
- **Locations:** Cities, addresses, workplaces, specific places
- **Temporal markers:** Specific dates that reveal personal timeline
- **Contact info:** Email addresses, phone numbers, usernames

### Relationship Context

- **Partner details:** Names, dynamics, specific incidents
- **Family patterns:** Identifying family situations
- **Workplace context:** Company names, colleague names, projects

### Practice Bleed

- **Private workspace references:** Links to desk/, floor/, box/ in public files
- **Portal artifacts:** Content from private portals appearing in public system
- **Intention content:** Active intentions referenced in shared artifacts
- **Seal content:** Personal configuration leaking into framework

### Pattern Recognition

The charm uses both explicit matching (known names) and semantic detection (content that "feels" personal). Spirit will flag uncertain cases for Mage review.

---

## Operational Guidance

### For the Spirit

When this charm is invoked:

1. **Gather context** — Check AGENTS.md for known personal markers (name, workshop path)
2. **Determine scope** — Full public scan, or focused on recent changes?
3. **Execute scan** — Search system/ and library/ for potential leaks
4. **Present findings** — Show flagged content with surrounding context
5. **Mage decides** — Remove, generalize, or accept each flag
6. **Execute remediation** — Make approved changes

**Detection heuristics:**

| Pattern | Confidence | Action |
|---------|------------|--------|
| Mage's name in wrong location | High | Flag |
| Partner/family names | High | Flag |
| Specific dates with personal context | Medium | Flag |
| desk/floor/box references | High | Flag |
| Content that "feels" personal | Low | Flag with note |

---

## When to Use

**Before publishing:**
- Before pushing changes to public repo
- Before sharing artifacts with other Mages
- Before opening new portals

**After development:**
- After creating tomes from real practice
- After developing bundles from lived experience
- After major additions to system/ or library/

**Periodically:**
- Monthly privacy audit
- When uncertain about what's in public artifacts
- Before onboarding new practitioners

---

## Integration with Other Charms

**Complements `@meta/coherence`:**
- Coherence verifies internal consistency
- Sanitize verifies external privacy
- Both prepare magic for sharing

**Complements security work:**
- Security protects inbound (attacks entering)
- Sanitize protects outbound (privacy leaving)
- Together they form complete sovereignty protection

---

## For Other Mages

**If you've forked Magic:** This charm helps you verify you haven't inherited the discoverer's personal context before adding your own. Run `@meta/sanitize` after forking to check for any residual personal details.

**If you're developing Magic:** Run this charm before any push to ensure your authentic practice hasn't leaked into shareable artifacts.

---

*Authentic development requires real context. Sharing requires abstraction. This charm bridges the gap.*
