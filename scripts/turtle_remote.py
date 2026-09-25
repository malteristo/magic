"""One resolver for the Mini's SSH target — every address in connections.md, first reachable wins.

Until 2026-09-21 ten scripts each took the *first* `<turtle-ssh>` target in
`desk/config/connections.md` (the Tailscale address) and stopped. When the
Mini's Tailscale logged itself out, every Forge-side pull failed the same way
for five days while the LAN address two lines below would have worked — and
the nightly report, fresh and PASS on the Mini, read as "5 days stale" from
Forge. The fix is not a second literal; it is trying the list.

Order is the file's order (Tailscale first — the preferred route stays
preferred). A probe is one `ssh … true` with a short connect timeout. If no
candidate answers, the first is returned so callers fail with the SSH error
they would have shown anyway, not with a new one from here.

CLI: `python3 scripts/turtle_remote.py` prints the resolved target (shell
scripts use this). `--list` prints every candidate without probing.
"""

from __future__ import annotations

import os
import re
import subprocess
import sys
from pathlib import Path

_CANDIDATE = re.compile(r"turtle@[^\s`<\[\]>)]+")
PROBE_TIMEOUT_SECONDS = 4
ENV_OVERRIDES = ("REMOTE", "TURTLE_SSH_TARGET")


def candidate_remotes(text: str) -> list[str]:
    """Every `turtle@host` in the text, file order, deduplicated."""
    return list(dict.fromkeys(m.group(0).rstrip(".,;:") for m in _CANDIDATE.finditer(text)))


def probe(remote: str, *, timeout: int = PROBE_TIMEOUT_SECONDS) -> bool:
    try:
        result = subprocess.run(
            [
                "ssh",
                "-o", "BatchMode=yes",
                "-o", f"ConnectTimeout={timeout}",
                "-o", "StrictHostKeyChecking=accept-new",
                remote,
                "true",
            ],
            capture_output=True,
            timeout=timeout + 4,
        )
        return result.returncode == 0
    except (OSError, subprocess.TimeoutExpired):
        return False


def reachable_remote(candidates: list[str], *, probe_fn=probe) -> str | None:
    """First candidate that answers; the first candidate if none does; None if empty."""
    for remote in candidates:
        if probe_fn(remote):
            return remote
    return candidates[0] if candidates else None


def reachable_remote_from(connections: Path | str, *, probe_fn=probe) -> str | None:
    path = Path(connections)
    if not path.is_file():
        return None
    return reachable_remote(candidate_remotes(path.read_text(errors="ignore")), probe_fn=probe_fn)


def resolve_turtle_remote(
    connections: Path | str, *, env: dict | None = None, probe_fn=probe
) -> str | None:
    """Env override first (`REMOTE`, `TURTLE_SSH_TARGET`), then the reachable candidate."""
    env = os.environ if env is None else env
    for name in ENV_OVERRIDES:
        value = (env.get(name) or "").strip()
        if value:
            return value
    return reachable_remote_from(connections, probe_fn=probe_fn)


def main(argv: list[str]) -> int:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from workshop_paths import config_file

    root = Path(__file__).resolve().parents[1]
    connections = config_file("connections.md", root)
    if "--list" in argv:
        text = connections.read_text(errors="ignore") if connections.is_file() else ""
        for remote in candidate_remotes(text):
            print(remote)
        return 0
    remote = resolve_turtle_remote(connections)
    if not remote:
        print(
            "No Turtle remote. Put a `turtle@<host>` line in desk/config/connections.md, "
            "or set REMOTE.",
            file=sys.stderr,
        )
        return 1
    print(remote)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
