#!/usr/bin/env bash
# Copy Forge (Cursor) and Anvil (Claude Code) session transcripts to the Mini
# personal chronicle. Chat is transport; this is the keep-safe.
#
# Dest: practice-root story/sessions/ on the Turtle host (own git, not Magic).
# Never rsync into the Magic working tree.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
. "$ROOT/scripts/workshop_paths.sh"
CONNECTIONS="$(workshop_config connections.md "$ROOT")"

if [ -z "${REMOTE:-}" ] && [ -f "$CONNECTIONS" ]; then
  REMOTE=$(python3 "$ROOT/scripts/turtle_remote.py" 2>/dev/null || true)
fi
if [ -z "${REMOTE:-}" ]; then
  echo "No Turtle remote. Put a turtle@<host> line in desk/config/connections.md." >&2
  exit 1
fi
DEST="${SESSIONS_DEST:-}"
if [ -z "$DEST" ] && [ -f "$CONNECTIONS" ]; then
  DEST=$(grep -Eo '/Users/[^[:space:]\`]+/workshops/[^[:space:]\`]+' "$CONNECTIONS" | head -1 || true)
  [ -n "$DEST" ] && DEST="${DEST%/}/story/sessions"
fi
if [ -z "$DEST" ]; then
  echo "No practice root. Put the Mini workshops path in desk/config/connections.md." >&2
  exit 1
fi

FORGE_SRC="${HOME}/.cursor/projects/Users-kermit-Documents-magic/agent-transcripts"
ANVIL_MAGIC="${HOME}/.claude/projects/-Users-kermit-Documents-magic"
ANVIL_TOS="${HOME}/.claude/projects/-Users-kermit-Documents-turtleos"

usage() {
  cat <<'EOF'
Usage: archive_session_transcripts.sh [--dry-run]

  Copies Cursor agent transcripts and Claude Code project logs to the Mini
  personal sessions git. Commits if the tree changed.
EOF
}

DRY=0
if [ "${1:-}" = "--dry-run" ]; then
  DRY=1
elif [ "${1:-}" = "-h" ] || [ "${1:-}" = "--help" ]; then
  usage
  exit 0
fi

[ -d "$FORGE_SRC" ] || { echo "missing Forge transcripts: $FORGE_SRC" >&2; exit 1; }

rsync_flags=(-az --delete)
if [ "$DRY" = 1 ]; then
  rsync_flags+=(-n)
fi

echo "Archiving sessions → ${REMOTE}:${DEST}"
ssh "$REMOTE" "mkdir -p '${DEST}/forge' '${DEST}/anvil/magic' '${DEST}/anvil/turtleos'"

rsync "${rsync_flags[@]}" "${FORGE_SRC}/" "${REMOTE}:${DEST}/forge/"
if [ -d "$ANVIL_MAGIC" ]; then
  rsync "${rsync_flags[@]}" "${ANVIL_MAGIC}/" "${REMOTE}:${DEST}/anvil/magic/"
fi
if [ -d "$ANVIL_TOS" ]; then
  rsync "${rsync_flags[@]}" "${ANVIL_TOS}/" "${REMOTE}:${DEST}/anvil/turtleos/"
fi

if [ "$DRY" = 1 ]; then
  echo "dry-run: no commit"
  exit 0
fi

# stamp + README + commit on the Mini
PARENTS=$(find "$FORGE_SRC" -maxdepth 2 -name '*.jsonl' ! -path '*/subagents/*' | wc -l | tr -d ' ')
ssh "$REMOTE" "DEST='$DEST' PARENTS='$PARENTS' bash -s" <<'REMOTE'
set -euo pipefail
cd "$DEST"
if [ ! -f README.md ]; then
  cat > README.md <<'MD'
# Session ground truth

Personal chronicle of Forge (Cursor) and Anvil (Claude Code) conversations.
Not a Magic path. Not public. Chat is transport; this tree is the keep-safe.

See workshop note: desk/notes/session-ground-truth.md
MD
fi
date -u +"%Y-%m-%dT%H:%M:%SZ parents=$PARENTS" > .archive-stamp
if [ ! -d .git ]; then
  git init -b main
fi
git add -A
if git diff --cached --quiet; then
  echo "sessions: tree unchanged"
else
  GIT_AUTHOR_NAME=Kermit GIT_AUTHOR_EMAIL=kermit@local \
  GIT_COMMITTER_NAME=Kermit GIT_COMMITTER_EMAIL=kermit@local \
    git commit -m "archive sessions: ${PARENTS} Forge parent chats"
  echo "sessions: committed $(git rev-parse --short HEAD)"
fi
REMOTE

# Second copy: the Mini has no backup destination, so this laptop (FileVault)
# holds a mirror of the practitioner's own roots. Other practitioners' roots
# are theirs and are not mirrored without their word.
MIRROR_DEST="${MIRROR_DEST:-${HOME}/Backups/turtle-ground}"
WORKSHOPS="${DEST%/story/sessions}"
WORKSHOPS="${WORKSHOPS%/*}"
mkdir -p "$MIRROR_DEST" && chmod 700 "$MIRROR_DEST"
# --delete-after would carry a wiped source into the only other copy, so a root
# that has shrunk to under half of what the mirror holds is not mirrored.
for root in kermit health-kermit; do
  src_n=$(ssh "$REMOTE" "find '${WORKSHOPS}/${root}' -type f 2>/dev/null | wc -l" | tr -d ' ')
  dst_n=$(find "$MIRROR_DEST/$root" -type f 2>/dev/null | wc -l | tr -d ' ')
  if [ "${src_n:-0}" -eq 0 ] || [ $((src_n * 2)) -lt "$dst_n" ]; then
    echo "mirror: REFUSED ${root} — Mini has ${src_n:-0} files, mirror has ${dst_n}" >&2
    continue
  fi
  rsync -a --delete-after "${REMOTE}:${WORKSHOPS}/${root}" "$MIRROR_DEST/"
done
echo "mirror: ${MIRROR_DEST} ($(du -sh "$MIRROR_DEST" | cut -f1))"

echo "Done. Check: python3 scripts/check_session_archive.py --fresh"
