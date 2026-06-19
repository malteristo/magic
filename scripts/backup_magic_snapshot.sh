#!/bin/bash
# backup_magic_snapshot.sh — Weekly comfort snapshot of the magic workshop.
#
# Two Chronicles: git on turtle bare is canonical; this tar is an extra offsite
# layer via Google Drive (Documents/ sync). Run manually or during @sunday.
#
# Usage:
#   ./scripts/backup_magic_snapshot.sh
#   ./scripts/backup_magic_snapshot.sh --dry-run
#
# Output: ~/Documents/magic-backups/magic-snapshot-YYYYMMDD.tar.gz

set -euo pipefail

DRY_RUN=false
KEEP="${MAGIC_BACKUP_KEEP:-8}"

for arg in "$@"; do
  case "$arg" in
    --dry-run) DRY_RUN=true ;;
    -h|--help)
      sed -n '2,14p' "$0"
      exit 0
      ;;
    *)
      echo "Unknown option: $arg" >&2
      exit 1
      ;;
  esac
done

if ROOT="$(git rev-parse --show-toplevel 2>/dev/null)"; then
  :
else
  ROOT="${MAGIC_ROOT:-$HOME/Documents/magic}"
fi

if [ ! -d "$ROOT" ]; then
  echo "Workshop not found: $ROOT" >&2
  exit 1
fi

DEST="${MAGIC_BACKUP_DIR:-$HOME/Documents/magic-backups}"
STAMP="$(date +%Y%m%d)"
ARCHIVE="$DEST/magic-snapshot-${STAMP}.tar.gz"
NAME="$(basename "$ROOT")"
PARENT="$(dirname "$ROOT")"

mkdir -p "$DEST"

EXCLUDES=(
  --exclude="$NAME/.git"
  --exclude="$NAME/.publish-worktree"
  --exclude="$NAME/.obsidian"
  --exclude="$NAME/.trash"
  --exclude="$NAME/.DS_Store"
  --exclude="$NAME/portals"
  --exclude="$NAME/circles"
  --exclude="$NAME/node_modules"
  --exclude="$NAME/**/.DS_Store"
)

if [ "$DRY_RUN" = true ]; then
  echo "Would create: $ARCHIVE"
  echo "From: $ROOT"
  echo "Excludes: .git, .publish-worktree, .obsidian, .trash, portals, circles"
  exit 0
fi

tar -czf "$ARCHIVE" "${EXCLUDES[@]}" -C "$PARENT" "$NAME"
SIZE="$(du -h "$ARCHIVE" | awk '{print $1}')"
echo "Backup written: $ARCHIVE ($SIZE)"

if [ "$KEEP" -gt 0 ]; then
  ls -1t "$DEST"/magic-snapshot-*.tar.gz 2>/dev/null | tail -n +$((KEEP + 1)) | while read -r old; do
    rm -f "$old"
    echo "Pruned old backup: $(basename "$old")"
  done
fi
