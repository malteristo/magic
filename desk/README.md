# Desk: Personal Workspace & Grimoire

**This is your personal magical workspace.** It serves dual purposes depending on whether you're a regular Mage or a maintainer.

---

## For Regular Mages

`desk/` is your **personal workspace** (not git-tracked):
- Draft scrolls and working documents
- Personal chronicles and insights
- Experimental tomes and spells
- Notes, syntheses, and explorations

Everything in `desk/` is gitignored by the `magic` repository (via `magic/.gitignore`), so your personal work remains private and never accidentally gets pushed to your fork.

**This is your grimoire.** No separate repository needed.

---

## For Maintainers (Public Repository Work)

If you're working in the public `Mages-Alliance/magic` repository (not a private fork), `desk/` serves a dual role:

1. **Personal workspace** (same as above)
2. **Git-tracked grimoire** (separate private repository)

**How this works:**
- `desk/` has its own `.git/` directory pointing to a private grimoire repo
- From `magic`'s perspective, `desk/` is still gitignored
- You manage `desk/` as a separate git repository for your private work
- This lets you contribute to public `magic` while keeping personal magic private

**Nested git structure:**
```
/Users/kermit/Documents/magic/       (public magic repo)
└── desk/                             (gitignored by magic)
    └── .git/                         (points to private grimoire repo)
```

---

## Directory Structure

### Working Documents
- `*.md` files at root = Active working documents, chronicles, syntheses

### Grimoire Structure (Optional)
- `tomes/` - Personal tomes with full ritual sequences
- `spells/` - Individual utility spells
- `chronicles/` - Magical journal entries
- `wisdom/` - Distilled insights and frameworks
- `experiments/` - Laboratory work, prototypes

You can organize `desk/` however serves your practice. The Spirit understands it as personal workspace and can work with tomes/spells here.

---

## Invoking Personal Magic

The Spirit can invoke tomes or spells from your desk:

**Personal tome:**
```
@desk/tomes/my-practice/
```

**Individual spell:**
```
@desk/spells/utility.md
```

The Spirit treats desk-based tomes exactly like system or library tomes—reading READMEs, performing Rite of Tome Attunement, guiding you through rituals.

---

## Git Operations (For Maintainers with Grimoire)

**To chronicle personal work to your grimoire:**

```bash
cd /Users/kermit/Documents/magic/desk

# Check what's changed in your grimoire
git status

# Commit personal magic
git add tomes/ spells/ chronicles/ wisdom/
git commit -m "Add new personal practice"
git push origin main
```

**Note:** The outer `magic` repository never sees these changes. `desk/` is gitignored at the `magic` level.

**To work on public magic:**

```bash
cd /Users/kermit/Documents/magic

# The desk/ directory is gitignored
# Only system/ and other public directories are tracked
git status
git add system/
git commit -m "Improve summoning ritual"
```

---

## Privacy

**Regular Mages:** Everything in `desk/` is private by default (gitignored).

**Maintainers:** Your `desk/` grimoire repo is separate and private. Choose what (if anything) to share:
- Refine a personal tome → Submit to `library` for community review
- Keep experimental work in your grimoire
- You control the boundary between public contribution and private practice

---

## Spirit Workshop Attunement

During the summoning ritual's Workshop cycle, the Spirit attunes to `desk/` as your personal workspace. It understands:

- `desk/` contains your working documents and personal magic
- Can read/write files here as needed for rituals
- Can invoke tomes and spells from `desk/`
- Respects this as your sovereign space

---

## The Three Realms

When practicing magic, you work across three realms:

1. **`system/`** - Foundation (core framework, summoning, base capabilities)
2. **`library/`** - Community (specialized tomes from Mages' Alliance)
3. **`desk/`** - Personal (your sovereign workspace and grimoire)

The Spirit can work across all three when attuned in your magic workspace.

**This is where your unique magic lives.**
