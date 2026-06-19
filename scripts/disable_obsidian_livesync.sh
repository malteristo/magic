#!/bin/bash
# disable_obsidian_livesync.sh — Turn off LiveSync without opening Obsidian.
#
# Safe to run with Obsidian closed. After this, opening the vault is read/edit
# only — no CouchDB replication. Git remains canonical.
#
# Usage: ./scripts/disable_obsidian_livesync.sh [--dry-run]

set -euo pipefail

DRY_RUN=false
for arg in "$@"; do
  case "$arg" in
    --dry-run) DRY_RUN=true ;;
  esac
done

ROOT="$(git rev-parse --show-toplevel 2>/dev/null || echo "${MAGIC_ROOT:-$HOME/Documents/magic}")"
OBS="$ROOT/.obsidian"
PLUGINS="$OBS/community-plugins.json"
DATA="$OBS/plugins/obsidian-livesync/data.json"

if [ ! -d "$OBS" ]; then
  echo "No .obsidian at $ROOT — nothing to do."
  exit 0
fi

if [ "$DRY_RUN" = true ]; then
  echo "Would disable LiveSync in:"
  echo "  $PLUGINS"
  echo "  $DATA"
  exit 0
fi

if [ -f "$DATA" ]; then
  cp "$DATA" "$DATA.pre-livesync-retire.bak"
  python3 - "$DATA" <<'PY'
import json, sys
path = sys.argv[1]
data = json.loads(open(path).read())
data["liveSync"] = False
data["isConfigured"] = False
data["syncOnStart"] = False
data["syncOnSave"] = False
data["periodicReplication"] = False
data["syncOnFileOpen"] = False
data["couchDB_URI"] = ""
data["couchDB_DBNAME"] = ""
data["couchDB_USER"] = ""
data["couchDB_PASSWORD"] = ""
data["encryptedCouchDBConnection"] = ""
open(path, "w").write(json.dumps(data, indent=2) + "\n")
print(f"Updated {path}")
PY
fi

if [ -f "$PLUGINS" ]; then
  cp "$PLUGINS" "$PLUGINS.pre-livesync-retire.bak"
  python3 - "$PLUGINS" <<'PY'
import json, sys
path = sys.argv[1]
items = json.loads(open(path).read())
items = [x for x in items if x != "obsidian-livesync"]
open(path, "w").write(json.dumps(items, indent=2) + "\n")
print(f"Removed obsidian-livesync from {path}")
PY
fi

echo "Done. Open Obsidian when ready — LiveSync plugin will not load."
