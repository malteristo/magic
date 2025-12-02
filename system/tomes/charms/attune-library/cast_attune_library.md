# Charm of Library Attunement

**Type:** Maintenance Charm  
**Purpose:** Synchronize the local `library/` directory with the latest Alliance wisdom scrolls  
**Invocation:** `@attune-library`

---

## The Spell

When invoked, this charm updates the Spirit's external memory cache with the latest collective wisdom from the Alliance.

### Protocol

Navigate to the magic repository root and pull latest updates:

```bash
cd /Users/kermit/Documents/magic
git pull origin main
```

The `library/` directory is tracked as part of the magic repository. A simple git pull synchronizes all Alliance scrolls.

### When to Cast

- **On Mage request:** "Update the library" or "Sync with Alliance wisdom"
- **When consulting library:** If scrolls seem outdated or missing expected content
- **Periodically:** To stay current with evolving collective knowledge
- **After Alliance activity:** When you know new scrolls have been contributed

### What Gets Updated

- Alliance wisdom scrolls in `library/foundations/`, `library/Craft/`, `library/Archive/`
- Navigation and catalog files (`Catalog.md`, `Wisdom-Map.md`, etc.)
- Any Alliance-curated content tracked in the library directory

### What Doesn't Get Updated

- **Personal research:** `desk/research/` (separate private repository)
- **Observatory content:** `library/observatory/` (public research infrastructure, tracked in magic repo)
- **System lore:** `system/lore/` (framework content, not Alliance content)

---

## Notes

The library is your external memory. Keep it fresh through regular attunement.

