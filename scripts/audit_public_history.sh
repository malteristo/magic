#!/bin/bash
# audit_public_history.sh — What is actually retrievable from a public repo?
#
# Written 2026-08-01, after malteristo/magic was found carrying five months of
# private practice memory in history: absent from HEAD, present in every clone,
# and still served through five forks. Nothing in the framework would have told
# anyone that. This is that missing check.
#
# Reads only. Clones the remote fresh, scans EVERY blob in EVERY commit — not
# the working tree, which is where the reassuring answer lives — and reports
# what a stranger could pull out today.
#
# Usage:
#   ./scripts/audit_public_history.sh                # remote 'github'
#   ./scripts/audit_public_history.sh <remote|url>
#
# Exit 0 = nothing found. Exit 1 = findings. Exit 2 = could not run.

set -uo pipefail

RED='\033[0;31m'; YEL='\033[0;33m'; GRN='\033[0;32m'; DIM='\033[2m'; NC='\033[0m'

TARGET="${1:-github}"
ROOT="$(git rev-parse --show-toplevel 2>/dev/null || true)"
NAMES_FILE="${ROOT:-.}/system/config/private_names.txt"
FOUND=0

if [ -z "$ROOT" ]; then echo "Not inside a git repository." >&2; exit 2; fi

if URL="$(git remote get-url "$TARGET" 2>/dev/null)"; then
  echo "Auditing remote '$TARGET' → $URL"
else
  URL="$TARGET"
  echo "Auditing URL → $URL"
fi

TMP="$(mktemp -d)"
cleanup() { rm -rf "$TMP"; }
trap cleanup EXIT

echo "Cloning full history (bare, read-only)…"
if ! git clone -q --bare "$URL" "$TMP/r.git" 2>"$TMP/err"; then
  echo -e "${RED}Could not clone.${NC} $(head -1 "$TMP/err")" >&2; exit 2
fi
cd "$TMP/r.git" || exit 2

COMMITS=$(git rev-list --all --count)
echo "History: $COMMITS commits"
echo ""

# ---------------------------------------------------------------------------
# 1. Private practice paths ever committed
# ---------------------------------------------------------------------------
echo "── Private practice paths in history ──"
# Files still present at HEAD are published on purpose — a framework may well
# ship something under box/ or desk/ deliberately. What matters is the file that
# was removed from the tree and is therefore assumed gone, but is not.
git ls-tree -r --name-only HEAD 2>/dev/null | sort -u > "$TMP/at_head"
PRIV=$(git log --all --diff-filter=A --name-only --format="" 2>/dev/null \
        | grep -E '^(desk|floor|box)/' \
        | grep -vE '\.gitkeep$|/README\.md$|\.gitignore$' | sort -u \
        | comm -23 - "$TMP/at_head")
if [ -n "$PRIV" ]; then
  FOUND=$((FOUND+1))
  n=$(echo "$PRIV" | wc -l | tr -d ' ')
  echo -e "${RED}[EXPOSED] $n private-path file(s) exist in history${NC}"
  echo "$PRIV" | head -20 | sed 's/^/  /'
  [ "$n" -gt 20 ] && echo "  … and $((n-20)) more"
else
  echo -e "${GRN}none${NC}"
fi
echo ""

# ---------------------------------------------------------------------------
# 2. Content patterns across every unique blob
# ---------------------------------------------------------------------------
echo "── Content scan (every blob, every commit) ──"

BLOBS="$TMP/blobs"
git rev-list --objects --all 2>/dev/null \
  | awk 'NF>=2 { sha=$1; $1=""; sub(/^ /,""); print sha"\t"$0 }' \
  | grep -viE '\.(png|jpe?g|gif|pdf|zip|woff2?|ico|mp4|mov)$' \
  | sort -u -k1,1 > "$BLOBS"
echo -e "${DIM}$(wc -l < "$BLOBS" | tr -d ' ') unique text blobs — extracting once${NC}"

# Extract every unique blob ONCE into a single corpus, then grep the corpus.
# Scanning per-pattern would re-read the whole object store for every rule:
# eight patterns over thirteen thousand blobs is a hundred thousand subprocess
# spawns, and the tool nobody waits for is the tool nobody runs.
CORPUS="$TMP/corpus"
: > "$CORPUS"
while IFS=$'\t' read -r sha path; do
  # LC_ALL=C: some blobs are not valid UTF-8, and a locale-aware sed aborts on
  # them mid-stream. Byte semantics keep the sweep complete.
  git cat-file blob "$sha" 2>/dev/null \
    | LC_ALL=C sed "s|^|${path}$(printf '\t')|" 2>/dev/null >> "$CORPUS" || true
done < "$BLOBS"
echo -e "${DIM}$(wc -l < "$CORPUS" | tr -d ' ') lines${NC}"

scan() {           # scan <regex> <label> <severity> [exclude-regex]
  local pat="$1" label="$2" sev="$3" excl="${4:-}"
  local hits="$TMP/hits"
  grep -hoE "$pat" "$CORPUS" 2>/dev/null | sort -u > "$hits" || true
  if [ -n "$excl" ] && [ -s "$hits" ]; then
    grep -vE "$excl" "$hits" > "$hits.f" 2>/dev/null || true; mv -f "$hits.f" "$hits" 2>/dev/null || true
  fi
  if [ -s "$hits" ]; then
    FOUND=$((FOUND+1))
    local c; c=$(wc -l < "$hits" | tr -d ' ')
    if [ "$sev" = CRITICAL ]; then echo -e "${RED}[$sev] $label — $c distinct value(s)${NC}";
    else echo -e "${YEL}[$sev] $label — $c distinct value(s)${NC}"; fi
    head -8 "$hits" | sed 's/^/  /'
    # where it lives
    grep -hE "$pat" "$CORPUS" 2>/dev/null | cut -f1 | sort -u | head -4 \
      | sed 's/^/    in: /'
  fi
  rm -f "$hits"
}

scan '[0-9]{10,}@s\.whatsapp\.net'                    "WhatsApp JID (phone number)" CRITICAL '1234567890@|JID@|REDACTED'
scan '100\.[0-9]+\.[0-9]+\.[0-9]+'                    "Tailscale IP" CRITICAL
scan 'tail[0-9a-f]+\.ts\.net'                         "Tailscale FQDN" CRITICAL
scan '(sk-[A-Za-z0-9_-]{24,}|ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{30,}|xox[baprs]-[A-Za-z0-9-]{10,}|AKIA[0-9A-Z]{16})' "Credential-shaped token" CRITICAL
scan '192\.168\.[0-9]+\.[0-9]+'                       "Private LAN IP" HIGH '192\.168\.64\.1'
scan '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' "Email address" MEDIUM '@example\.|@newsletter\.|@s\.whatsapp\.net|git@github\.com|noreply@|<email>|@turtle\.local|@localhost'
scan '/Users/[a-z][a-z0-9_-]+/'                       "Absolute path with username" MEDIUM '/Users/username/|/Users/you/|/Users/mage/'

if [ -f "$NAMES_FILE" ]; then
  ALT=$(grep -vE '^\s*(#|$)' "$NAMES_FILE" | sed 's/[[:space:]]*$//' | paste -sd'|' -)
  [ -n "$ALT" ] && scan "\\b(${ALT})\\b" "Private name" MEDIUM
else
  echo -e "${DIM}(no system/config/private_names.txt — name scan skipped)${NC}"
fi
echo ""

# ---------------------------------------------------------------------------
# 3. Fork network — history rewrite does not reach it
# ---------------------------------------------------------------------------
echo "── Fork network ──"
SLUG=$(echo "$URL" | sed -E 's|.*github\.com[:/]||; s|\.git$||')
if command -v gh >/dev/null 2>&1 && [ -n "$SLUG" ]; then
  VIS=$(gh repo view "$SLUG" --json visibility -q .visibility 2>/dev/null || echo UNKNOWN)
  echo "visibility: $VIS"
  FORKS=$(gh api "repos/$SLUG/forks" --jq '.[].full_name' 2>/dev/null || true)
  if [ -n "$FORKS" ]; then
    FOUND=$((FOUND+1))
    echo -e "${YEL}$(echo "$FORKS" | wc -l | tr -d ' ') fork(s) — rewriting this repo's history will NOT remove objects from them${NC}"
    echo "$FORKS" | sed 's|^|  https://github.com/|'
  else
    echo -e "${GRN}no forks${NC}"
  fi
else
  echo -e "${DIM}gh not available or not a GitHub URL — fork check skipped${NC}"
fi
echo ""

# ---------------------------------------------------------------------------
if [ "$FOUND" -gt 0 ]; then
  echo -e "${RED}$FOUND finding group(s).${NC}"
  echo "Removal from history needs a rewrite (git filter-repo) AND a force-push;"
  echo "forks additionally need GitHub's private-information removal process."
  exit 1
fi
echo -e "${GRN}Clean — nothing private found in history.${NC}"
exit 0
