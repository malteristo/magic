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

ALLOWLIST_DIRS=(
  system
  library
  scripts
  .claude
  .cursor
)

ROOT_FILES=(
  README.md
  MAGIC_SPEC.md
  ONBOARDING.md
  CLAUDE.md
  CONTRIBUTING.md
  FAQ.md
  LICENSE
  ACKNOWLEDGMENTS.md
  TROUBLESHOOTING.md
  TRANSLATION_AND_INTEGRATION_GUIDE.md
  AGENTS.md.template
  mage_seal.md.template
  .gitmodules
)

REGISTRY_FILES=(
  portals/registry.yaml
  portals/README.md
  circles/registry.yaml
  circles/README.md
  universe/README.md
)

RSYNC_EXCLUDES=(
  --exclude '.DS_Store'
  --exclude '.obsidian/'
  --exclude '.trash/'
  --exclude 'system/config/connections.md'
  --exclude 'mage_seal.md'
  --exclude 'AGENTS.md'
)

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

echo "Syncing allowlisted paths..."
for dir in "${ALLOWLIST_DIRS[@]}"; do
  if [ ! -d "$ROOT/$dir" ]; then
    echo "  skip missing dir: $dir"
    continue
  fi
  mkdir -p "$WORKTREE/$dir"
  rsync -a --delete "${RSYNC_EXCLUDES[@]}" "$ROOT/$dir/" "$WORKTREE/$dir/"
done

for file in "${ROOT_FILES[@]}"; do
  if [ -f "$ROOT/$file" ]; then
    cp "$ROOT/$file" "$WORKTREE/$file"
  fi
done

for file in "${REGISTRY_FILES[@]}"; do
  if [ -f "$ROOT/$file" ]; then
    mkdir -p "$WORKTREE/$(dirname "$file")"
    cp "$ROOT/$file" "$WORKTREE/$file"
  fi
done

cp "$ROOT/scripts/public.gitignore" "$WORKTREE/.gitignore"

cd "$WORKTREE"
git add -A

BLOCKED=$(
  git diff --cached --name-only --diff-filter=ACM \
    | grep -E '^(desk|floor|box)/|(^|/)connections\.md$|^AGENTS\.md$|^mage_seal\.md$' \
    || true
)
if [ -n "$BLOCKED" ]; then
  echo -e "${RED}BLOCKED: private paths would be published:${NC}" >&2
  echo "$BLOCKED" >&2
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
