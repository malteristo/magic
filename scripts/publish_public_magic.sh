#!/bin/bash
# publish_public_magic.sh — Publish allowlisted framework subset to public github remote.
#
# Two Chronicles: full tree lives on `turtle`; this script is the only supported path
# to update the public `github` remote.
#
# Usage:
#   ./scripts/publish_public_magic.sh --dry-run   # show what would ship
#   ./scripts/publish_public_magic.sh             # commit + push to github main

set -euo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m'

DRY_RUN=false
REMOTE="${MAGIC_PUBLIC_REMOTE:-github}"
BRANCH="${MAGIC_PUBLIC_BRANCH:-main}"
STAGING_BRANCH="${MAGIC_PUBLIC_STAGING_BRANCH:-publish/staging}"
WORKTREE=".publish-worktree"

for arg in "$@"; do
  case "$arg" in
    --dry-run) DRY_RUN=true ;;
    -h|--help)
      sed -n '2,12p' "$0"
      exit 0
      ;;
    *)
      echo "Unknown option: $arg" >&2
      exit 1
      ;;
  esac
done

ROOT="$(git rev-parse --show-toplevel 2>/dev/null || true)"
if [ -z "$ROOT" ]; then
  echo "Not inside a git repository." >&2
  exit 1
fi
cd "$ROOT"

if ! git remote get-url "$REMOTE" >/dev/null 2>&1; then
  echo "Remote '$REMOTE' not configured." >&2
  exit 1
fi

# What may be public is defined once, in scripts/public_surface.conf, and shared
# with the pre-push guard and the sanitiser. This script used to carry four of
# its own lists (ALLOWLIST_DIRS / ROOT_FILES / REGISTRY_FILES / RSYNC_EXCLUDES)
# plus a BLOCKED regex, and they had drifted: `system/config/sanitize_exceptions.txt`
# and `declared_listeners.txt` were created 2026-08-01, marked sensitive in
# .gitignore, and named in none of them — `system/` is rsync'd wholesale from the
# working tree, and rsync does not read .gitignore.
# shellcheck source=/dev/null
. "$ROOT/scripts/public_surface.sh"

echo "Resolving public surface..."
SURFACE="$(mktemp)"
trap 'rm -f "$SURFACE"' EXIT
ps_list_surface | sort > "$SURFACE"
echo "  $(wc -l < "$SURFACE" | tr -d ' ') path(s) on the public surface"

echo "Fetching $REMOTE..."
git fetch "$REMOTE" "$BRANCH"

worktree_exists() {
  [ -e "$WORKTREE/.git" ] || git worktree list --porcelain | grep -q "^worktree $ROOT/$WORKTREE$"
}

if ! worktree_exists; then
  echo "Creating publish worktree at $WORKTREE..."
  git worktree add -B "$STAGING_BRANCH" "$WORKTREE" "$REMOTE/$BRANCH"
else
  echo "Updating publish worktree..."
  git -C "$WORKTREE" fetch "$REMOTE" "$BRANCH"
  git -C "$WORKTREE" checkout -q "$STAGING_BRANCH"
  git -C "$WORKTREE" reset -q --hard "$REMOTE/$BRANCH"
fi

echo "Deriving worktree from the surface..."
# A derivation, not an accumulation. The previous version rsync'd five
# directories and copied some root files; anything already in the public repo
# but no longer intended simply stayed there forever, which is why `archive/`
# and two live registry.yaml files are in the public tree today while
# public.gitignore claims to exclude them. Now the worktree is emptied of
# tracked content and rebuilt from the surface, so what is published is exactly
# what the config says. Removals show up in the diff below like any other change.
find "$WORKTREE" -mindepth 1 -path "$WORKTREE/.git" -prune -o -type f -print0 \
  | xargs -0 rm -f 2>/dev/null || true

while IFS= read -r rel; do
  [ -z "$rel" ] && continue
  mkdir -p "$WORKTREE/$(dirname "$rel")"
  cp "$ROOT/$rel" "$WORKTREE/$rel"
done < "$SURFACE"

cp "$ROOT/scripts/public.gitignore" "$WORKTREE/.gitignore"

cd "$WORKTREE"
git add -A

# Backstop. The staged tree is built from the surface, so this should never
# fire — which is the point: it is the check that proves the derivation, and a
# hit means the surface config and this script disagree about a path.
BLOCKED=""
while IFS= read -r path; do
  [ -z "$path" ] && continue
  [ "$path" = ".gitignore" ] && continue
  is_public_surface "$path" || BLOCKED="${BLOCKED}${path}"$'\n'
done < <(git diff --cached --name-only --diff-filter=ACM)

if [ -n "$BLOCKED" ]; then
  echo -e "${RED}BLOCKED: staged paths are not on the public surface:${NC}" >&2
  echo "$BLOCKED" | grep . | head -20 >&2
  exit 1
fi

if git diff --cached --quiet; then
  echo -e "${GREEN}Public remote already up to date — nothing to publish.${NC}"
  exit 0
fi

echo ""
echo "=== Changes to publish ==="
git diff --cached --stat
echo ""

if [ "$DRY_RUN" = true ]; then
  echo -e "${YELLOW}Dry run — no commit or push.${NC}"
  git diff --cached --name-only
  exit 0
fi

MSG="Publish framework subset from private workshop (Two Chronicles).

Allowlisted: system/, library/, scripts/, public root docs, infrastructure registries."
git commit -m "$MSG"
git push "$REMOTE" "$STAGING_BRANCH:$BRANCH"

echo -e "${GREEN}Published to $REMOTE/$BRANCH${NC}"
git log -1 --oneline
