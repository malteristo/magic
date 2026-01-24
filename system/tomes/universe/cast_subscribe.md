# Cast Subscribe

**Purpose:** Add a Universe source by cloning an external pattern library into `universe/`.

---

## When to Use

- Adding a new external pattern library
- Setting up known sources (PAI, Daemon, Fabric)
- Connecting to custom repositories

---

## Invocation

```
@universe subscribe <source>
@universe subscribe <url> <name>
```

---

## Known Sources

These sources are recognized by name:

| Name | Repository | Description |
|------|------------|-------------|
| `pai` | `danielmiessler/Personal_AI_Infrastructure` | Personal AI Infrastructure |
| `daemon` | `danielmiessler/Daemon` | Personal API framework |
| `fabric` | `danielmiessler/fabric` | AI augmentation patterns |

---

## Procedure

### For Known Sources

```bash
# Example: @universe subscribe pai
case "$SOURCE" in
  pai)
    REPO="https://github.com/danielmiessler/Personal_AI_Infrastructure.git"
    NAME="pai"
    ;;
  daemon)
    REPO="https://github.com/danielmiessler/Daemon.git"
    NAME="daemon"
    ;;
  fabric)
    REPO="https://github.com/danielmiessler/fabric.git"
    NAME="fabric"
    ;;
  *)
    echo "Unknown source: $SOURCE"
    echo "Use: @universe subscribe <url> <name> for custom sources"
    exit 1
    ;;
esac
```

### For Custom Sources

```bash
# Example: @universe subscribe https://github.com/author/repo.git custom-name
REPO="$1"
NAME="$2"
```

### Clone the Source

```bash
if [ -d "universe/$NAME" ]; then
  echo "Source '$NAME' already exists at universe/$NAME"
  echo "To update: cd universe/$NAME && git pull"
else
  git clone "$REPO" "universe/$NAME" --depth 1
  echo "✓ Subscribed to $NAME"
fi
```

### Update Universe README

After cloning, update `universe/README.md` to document the new source:

```bash
echo "| $NAME | $REPO | [description] |" >> universe/README.md
# Spirit should offer to add proper description
```

### Announce Completion

```
Subscribed to: $NAME
Location: universe/$NAME/

To explore: Read universe/$NAME/README.md
To harvest: @universe harvest $NAME <pattern>
To update: cd universe/$NAME && git pull
```

---

## Notes

- Sources are cloned with `--depth 1` for efficiency
- Universe sources are gitignored (personal to each Mage)
- Subscription doesn't imply endorsement—evaluate before harvesting
- Credit lineage when translating patterns into Main

---

*Choose sources that resonate with your practice.*
