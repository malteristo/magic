# Config templates

This folder ships **templates only**. Live instance files — addresses, private names, listener declarations, sanitize exceptions — live in `desk/config/` on a running workshop.

```bash
mkdir -p desk/config
cp system/config/connections.md.template desk/config/connections.md
cp system/config/private_names.txt.template desk/config/private_names.txt
cp system/config/sanitize_exceptions.txt.template desk/config/sanitize_exceptions.txt
cp system/config/declared_listeners.txt.template desk/config/declared_listeners.txt
```

`./scripts/configure_workshop_git.sh` creates the names file from its template if it is missing.

Scripts resolve `desk/config/` first (`scripts/workshop_paths.sh`, `scripts/workshop_paths.py`).
