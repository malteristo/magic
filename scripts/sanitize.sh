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

# Exclude self, config, and .git from checks
EXCLUDE_FILTER='system/config/\|scripts/sanitize.sh\|\.git/'

check_pattern() {
  local pattern="$1"
  local description="$2"
  local severity="$3"
  local exclude_pattern="${4:-}"

  local matches
  matches=$(echo "$FILES" | xargs grep -n -E "$pattern" 2>/dev/null | grep -v "$EXCLUDE_FILTER" || true)

  # Apply additional exclude pattern if provided (for false-positive filtering)
  if [ -n "$exclude_pattern" ] && [ -n "$matches" ]; then
    matches=$(echo "$matches" | grep -v -E "$exclude_pattern" || true)
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

echo "Sanitation check..."
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

# HIGH: SSH to turtle with real hostnames (exclude placeholders like <turtle-ssh>, [ip], ...)
check_pattern 'ssh\s+turtle@[^<\[\.]' "SSH connection to Turtle (non-placeholder)" "HIGH"

# MEDIUM: Real email addresses (exclude examples, placeholders, and git@github patterns)
check_pattern '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}' "Email address" "MEDIUM" '@example\.com|@newsletter\.com|@s\.whatsapp\.net|git@github\.com|JID@|<email>|noreply@'

# MEDIUM: Absolute paths with real usernames
check_pattern '/Users/kermit/' "Path with real username" "MEDIUM"

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
