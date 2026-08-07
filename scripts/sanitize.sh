#!/bin/bash
# sanitize.sh — Pre-commit sanitation check for the Magic repository
# Scans staged files for sensitive patterns that should not be public.
# Exit 1 = block commit. Exit 0 = clean.
#
# Usage:
#   ./scripts/sanitize.sh           # Check staged files (pre-commit mode)
#   ./scripts/sanitize.sh --full    # Check all tracked files (full sweep)
#   ./scripts/sanitize.sh --quiet   # Suppress clean output

set -euo pipefail

RED='\033[0;31m'
YELLOW='\033[0;33m'
GREEN='\033[0;32m'
NC='\033[0m'

QUIET=false
FULL=false
FOUND=0

for arg in "$@"; do
  case "$arg" in
    --full)  FULL=true ;;
    --quiet) QUIET=true ;;
  esac
done

# Get file list
if [ "$FULL" = true ]; then
  FILES=$(git ls-files)
else
  FILES=$(git diff --cached --name-only --diff-filter=ACM 2>/dev/null || true)
fi

if [ -z "$FILES" ]; then
  [ "$QUIET" = false ] && echo -e "${GREEN}No files to check.${NC}"
  exit 0
fi

# Two Chronicles: private practice memory goes to the `turtle` bare repo only.
# Operational detail is fine there; this hook guards **public-bound paths**.
#
# That filter was `grep -v -E '^(desk|floor|box)/'` until 2026-08-07 — the same
# three-directory blocklist the pre-push guard carried, and the same blind
# spot. It is now derived from scripts/public_surface.conf, so "is this path
# public-bound?" has one answer in this repo instead of six. Concretely this
# also *widens* the scan: `desk/README.md` and `box/transcripts/ytfetch.py` do
# ship publicly and were being skipped.
ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
# shellcheck source=/dev/null
. "$ROOT/scripts/public_surface.sh"

PUBLIC_BOUND=""
while IFS= read -r _f; do
  [ -z "$_f" ] && continue
  if is_public_surface "$_f"; then
    PUBLIC_BOUND="${PUBLIC_BOUND}${_f}"$'\n'
  fi
done < <(echo "$FILES")
FILES=$(echo "$PUBLIC_BOUND" | grep . || true)

if [ -z "$FILES" ]; then
  [ "$QUIET" = false ] && echo -e "${GREEN}Only private practice paths staged — sanitation skipped.${NC}"
  exit 0
fi

# Exclude self, config, and .git from checks
EXCLUDE_FILTER='system/config/\|scripts/sanitize.sh\|\.git/'

check_pattern() {
  local pattern="$1"
  local description="$2"
  local severity="$3"
  local exclude_pattern="${4:-}"
  local ci="${5:-}"          # non-empty → case-insensitive

  # -H is load-bearing, not cosmetic. grep omits the filename when handed exactly
  # one file, so on a single-file commit every match arrived as "114:text" and
  # EXCLUDE_FILTER — which matches on path — silently stopped excluding anything.
  # The rule covered the many-file case it was written against and nothing derived
  # from it. Found when this file's own commit tripped its own guard.
  local matches
  if [ -n "$ci" ]; then
    matches=$(echo "$FILES" | xargs grep -inH -E "$pattern" 2>/dev/null | grep -v "$EXCLUDE_FILTER" || true)
  else
    matches=$(echo "$FILES" | xargs grep -nH -E "$pattern" 2>/dev/null | grep -v "$EXCLUDE_FILTER" || true)
  fi

  # Apply additional exclude pattern if provided (for false-positive filtering)
  if [ -n "$exclude_pattern" ] && [ -n "$matches" ]; then
    matches=$(echo "$matches" | grep -v -E "$exclude_pattern" || true)
  fi

  # Decided exceptions — the practitioner's own list, gitignored.
  #
  # Some findings are correct and sanctioned anyway: a shipped artifact id that
  # happens to carry a name, a filename other documents link to. Those decisions
  # cannot live in this file — writing them here would hardcode a real name into
  # tracked, public-bound source, which is the exact defect this script was
  # rewritten to remove. They live beside the name list instead.
  if [ -n "$EXCEPTIONS_PATTERNS" ] && [ -n "$matches" ]; then
    matches=$(echo "$matches" | grep -v -E -f "$EXCEPTIONS_PATTERNS" || true)
  fi

  if [ -n "$matches" ]; then
    FOUND=$((FOUND + 1))
    if [ "$severity" = "CRITICAL" ]; then
      echo -e "${RED}[${severity}] ${description}${NC}"
    else
      echo -e "${YELLOW}[${severity}] ${description}${NC}"
    fi
    echo "$matches" | head -10
    echo ""
  fi
}

GUARD_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || echo .)"

# Same resolution chain as the name list — one set of decisions serves every repo.
EXCEPTIONS_FILE=""
for candidate in \
  "${MAGIC_SANITIZE_EXCEPTIONS:-}" \
  "$(git config --get magic.sanitizeExceptions 2>/dev/null || true)" \
  "$GUARD_ROOT/system/config/sanitize_exceptions.txt" \
  "$GUARD_ROOT/.sanitize_exceptions.txt"
do
  if [ -n "$candidate" ] && [ -f "$candidate" ] && grep -qvE '^\s*(#|$)' "$candidate" 2>/dev/null; then
    EXCEPTIONS_FILE="$candidate"; break
  fi
done

# Strip comments and blank lines before this ever reaches grep -f.
#
# Not hygiene — safety. grep -f treats every line of the file as a pattern, and
# an empty pattern matches every line, so a single blank line in an exceptions
# file silently suppresses the entire guard and reports "Clean." That is the
# worst possible failure for this script: total, silent, and indistinguishable
# from success. Caught in testing when a findings group vanished that no
# exception named.
EXCEPTIONS_PATTERNS=""
if [ -n "$EXCEPTIONS_FILE" ]; then
  EXCEPTIONS_PATTERNS="$(mktemp)"
  trap 'rm -f "$EXCEPTIONS_PATTERNS"' EXIT
  grep -vE '^\s*(#|$)' "$EXCEPTIONS_FILE" | sed 's/[[:space:]]*$//' | grep -v '^$' > "$EXCEPTIONS_PATTERNS" || true
  [ -s "$EXCEPTIONS_PATTERNS" ] || EXCEPTIONS_PATTERNS=""
fi

echo "Sanitation check..."
if [ -n "$EXCEPTIONS_FILE" ]; then
  # Never silent. An exception list is a hole in the guard by design, so its
  # size is reported every run — a hole nobody is counting stops being a decision.
  echo "  ($(grep -cvE '^\s*(#|$)' "$EXCEPTIONS_FILE") decided exception(s) active)"
fi
echo ""

# CRITICAL: Real phone numbers in WhatsApp format (exclude placeholders like 1234567890 and JID)
check_pattern '[0-9]{10,}@s\.whatsapp\.net' "WhatsApp JID (phone number)" "CRITICAL" '1234567890@|JID@'

# CRITICAL: Tailscale IPs (100.x.x.x range used by Tailscale)
check_pattern '100\.[0-9]+\.[0-9]+\.[0-9]+' "Tailscale IP address" "CRITICAL"

# CRITICAL: Tailscale FQDN
check_pattern 'tail[0-9a-f]+\.ts\.net' "Tailscale FQDN" "CRITICAL"

# HIGH: Private LAN IPs (exclude Docker bridge 192.168.64.1 which is standard)
check_pattern '192\.168\.[0-9]+\.[0-9]+' "Private LAN IP address" "HIGH" '192\.168\.64\.1'

# HIGH: Discord channel/bot IDs (17+ digit numbers, exclude URLs and timestamps)
check_pattern '(^|[^/0-9])[0-9]{17,20}([^0-9]|$)' "Discord ID (channel/bot/user)" "HIGH" 'https?://|x\.com/|twitter\.com/'

# CRITICAL: SSH connection strings with actual IP addresses
check_pattern 'ssh\s+\w+@[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+' "SSH connection with IP" "CRITICAL"

# HIGH: SSH account@host for a machine in this practice.
#
# This required a literal `ssh ` prefix until 2026-08-07, which meant it saw
# the *command* and not the *value*. Three magic scripts written 08-06 carry
# `REMOTE_DEFAULT = "turtle@turtles-mac-mini"` as a bare assignment — the same
# identifier, no `ssh ` in front, invisible to the guard and queued to ship on
# the next publish. An SSH target is sensitive because of what it names, not
# because of the verb next to it.
check_pattern '(^|[^<[:alnum:]_.-])turtle@[^<\[[:space:]]' "SSH target for Turtle (non-placeholder)" "HIGH" \
  '<turtle-ssh>|turtle@<|turtle@\[|turtle@\.\.\.|turtle@host|turtle@127\.0\.0\.1|turtle@localhost|@example|placeholder'

# MEDIUM: Real email addresses (exclude examples, placeholders, and git@github patterns)
check_pattern '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}' "Email address" "MEDIUM" '@example\.com|@newsletter\.com|@s\.whatsapp\.net|git@github\.com|JID@|<email>|noreply@'

# MEDIUM: Absolute paths with real usernames
#
# History of this rule, because the second version is the interesting mistake.
# v1 was the literal '/Users/kermit/' — a guard against publishing a username
# that names one username protects one person and publishes his. v2 derived it
# from $HOME, which fixed portability and quietly narrowed coverage to **the
# machine running the check**.
#
# This practice has two hosts. The laptop's $HOME is one account; the Mac Mini
# runs as another, and it is the Mini's path that gets hardcoded into sync
# scripts — `PRACTICE_ROOT = "/Users/turtle/workshops/kermit"`. So v2 guarded
# the half of the practice whose paths nobody writes down, and was blind to the
# half that ends up in source. Generalising across *operators* lost coverage
# across *hosts*.
#
# v3 matches any absolute home path with a plausible account name and excludes
# placeholders, so it covers every machine — including ones this practice has
# not met yet. `$HOME`'s basename is still excluded from the placeholder list
# on purpose: your own path is the one most likely to be real.
# Service accounts this framework documents you to create are not people.
# `turtle` is the Mini's account by convention (the setup guide tells the
# reader to make one); `owl` is the same account before the 2026-02-25 rename
# and survives in lineage. Every *other* account name in an absolute path is
# somebody's login, which is what this rule is for.
#
# Note what this deliberately does NOT catch: `/Users/turtle/workshops/kermit`,
# the string that started this. Its sensitive part was never the account — it
# was the Mage's handle in a public-bound script, and that is a different rule
# with a different severity. See § Identity precision below.
check_pattern '/(Users|home)/[a-z][a-z0-9_.-]*/' "Absolute path with a real account name" "MEDIUM" \
  '/Users/<|/home/<|/Users/\$|/home/\$|/Users/\[|/home/\[|/(Users|home)/(you|user|username|name|me|example|placeholder|runner|turtle|owl|node)/'

# MEDIUM: Private names — the practitioner's people, read from a gitignored local list.
#
# This rule used to hardcode one real first name. A framework that ships a name
# in order to protect it has published the thing it was guarding, and it
# protects exactly one household — the author's. The names now live in
# system/config/private_names.txt (gitignored, per-practitioner); this file
# ships only the mechanism. See system/config/private_names.txt.template.
#
# Resolution is a chain, not a path. The list used to be looked up at exactly
# one location — <repo>/system/config/private_names.txt — which is the magic
# workshop's layout and no other repository's. Every satellite repo a
# practitioner also keeps (turtleos here) therefore ran with name checking
# silently off while reporting "clean". One list, many repos: point them at it
# with `git config magic.privateNames <path>`.
NAMES_FILE=""
for candidate in \
  "${MAGIC_PRIVATE_NAMES:-}" \
  "$(git config --get magic.privateNames 2>/dev/null || true)" \
  "$GUARD_ROOT/system/config/private_names.txt" \
  "$GUARD_ROOT/.private_names.txt"
do
  if [ -n "$candidate" ] && [ -f "$candidate" ]; then NAMES_FILE="$candidate"; break; fi
done

if [ -n "$NAMES_FILE" ]; then
  NAMES_ALT=$(grep -vE '^\s*(#|$)' "$NAMES_FILE" | sed 's/[[:space:]]*$//' | paste -sd'|' -)
  if [ -n "$NAMES_ALT" ]; then
    # Case-insensitive on purpose. Names leak lowercased far more often than
    # capitalised — in filenames, channel names, branch names, intention slugs
    # (`lukas-sandbox`, `nesrine.md`, `. nesrine`). A case-sensitive check
    # reports "clean" over exactly those.
    # A LICENSE copyright line names its holder by legal function — that is
    # deliberate publication, not exposure. Narrowed to the copyright line so
    # the rest of the file is still checked.
    check_pattern "\\b(${NAMES_ALT})\\b" "Private name (use a role: 'the Mage'\''s partner', 'a practitioner')" "MEDIUM" 'mage_seal|connections\.md|private_names|^LICENSE:[0-9]+:Copyright' ci
  fi
else
  # Loud on purpose, and not suppressed by --quiet. "No list found" is the state
  # in which this script reports clean while checking nothing — the one result
  # that must never look like a pass.
  echo -e "${YELLOW}[NOTE] No private name list found — name checking is OFF for this repo.${NC}"
  echo "      In the magic workshop:  cp system/config/private_names.txt.template system/config/private_names.txt"
  echo "      In any other repo:      git config magic.privateNames /path/to/private_names.txt"
  echo ""
fi

# Summary
if [ "$FOUND" -gt 0 ]; then
  echo -e "${RED}Found ${FOUND} pattern(s) that may contain sensitive data.${NC}"
  echo "Review findings above. To bypass (emergency only): git commit --no-verify"
  echo ""
  echo "Sensitive connection details belong in system/config/connections.md (gitignored)."
  echo "Tracked files should use placeholders: <turtle-ssh>, <channel-id>, etc."
  exit 1
else
  [ "$QUIET" = false ] && echo -e "${GREEN}Clean. No sensitive patterns detected.${NC}"
  exit 0
fi
