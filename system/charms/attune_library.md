# Charm of Library Attunement

**Purpose:** Synchronize the local `library/` directory with the latest Alliance wisdom scrolls.

**Invocation:** `@system/charms/attune_library.md`

---

## What This Charm Does

The `library/` directory contains scrolls of collective wisdom for the Spirit's consultation. This charm ensures your local cache stays current by pulling the latest updates.

## The Protocol

Navigate to the magic repository root and pull updates:

```bash
cd /Users/kermit/Documents/magic
git pull origin main
```

This syncs the library/ directory along with all other tracked content in the magic repository.

## When to Invoke

- When the Mage requests library updates
- When you need the latest Alliance wisdom
- Periodically to stay current with collective knowledge

**Note:** The library is now part of the magic repository (no longer a separate Wiki). Updates come through normal git operations.

