#!/usr/bin/env python3
"""Connect this computer's Cursor to the Mage's turtleOS without anyone seeing the key.

The Mage presses Connect in their private channel; the reply gives an address.
The Spirit runs this with that address within the pickup window. turtleOS hands
the credential only to the Mage's own Tailscale identity, once, and this tool
writes it straight into Cursor's MCP settings. The credential is never printed,
so it never reaches a chat or a transcript.

    python3 scripts/turtleos_connect.py https://<host>:8443
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

DEFAULT_CONFIG = Path.home() / ".cursor" / "mcp.json"

NOTHING = (
    "Nothing to pick up. Press Connect (Verbinden) in your private channel, "
    "then ask again within 15 minutes."
)
NO_IDENTITY = (
    "turtleOS could not see who you are on Tailscale. Open the Tailscale app and "
    "check that it says Connected, signed in as you."
)


def fetch(base: str) -> tuple[int, str]:
    r = subprocess.run(
        ["curl", "-sS", "-m", "20", "-X", "POST", "-o", "-", "-w", "\n%{http_code}", f"{base}/connect"],
        capture_output=True,
        text=True,
    )
    if r.returncode != 0:
        return 0, ""
    body, _, code = r.stdout.rpartition("\n")
    return (int(code) if code.isdigit() else 0), body


def merge(config: Path, name: str, entry: dict) -> None:
    data: dict = {}
    if config.is_file():
        text = config.read_text(encoding="utf-8").strip()
        if text:
            data = json.loads(text)
    if not isinstance(data, dict):
        raise ValueError("settings file is not a JSON object")
    servers = data.setdefault("mcpServers", {})
    if not isinstance(servers, dict):
        raise ValueError("mcpServers is not a JSON object")
    servers[name] = entry
    config.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=config.parent, prefix=".mcp.", suffix=".json")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            json.dump(data, fh, indent=2)
            fh.write("\n")
        os.chmod(tmp, 0o600)
        os.replace(tmp, config)
    except BaseException:
        Path(tmp).unlink(missing_ok=True)
        raise


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Connect Cursor to your turtleOS; the key is never shown.")
    p.add_argument("address", help="the address from the Connect reply, e.g. https://<host>:8443")
    p.add_argument("--config", type=Path, default=DEFAULT_CONFIG, help="MCP settings file (default: Cursor's)")
    a = p.parse_args(argv)

    base = a.address.strip().rstrip("/")
    base = base[: -len("/mcp")] if base.endswith("/mcp") else base
    if not base.startswith("https://"):
        print("The address should start with https:// — use the one from the Connect reply.")
        return 2

    code, body = fetch(base)
    if code == 0:
        print(f"Could not reach turtleOS at {base}. Is Tailscale connected?")
        return 1
    if code == 404:
        print(NOTHING)
        return 1
    if code == 403:
        print(NO_IDENTITY)
        return 1
    if code != 200:
        print(f"turtleOS answered {code}; nothing was written.")
        return 1
    try:
        data = json.loads(body)
        name, entry = str(data["name"]), dict(data["server"])
        reaches, expires = list(data.get("reaches") or []), str(data.get("expires") or "")
    except (ValueError, KeyError, TypeError):
        print("turtleOS answered in a shape this tool does not know; nothing was written.")
        return 1
    try:
        merge(a.config, name, entry)
    except (OSError, ValueError) as exc:
        print(f"Could not update {a.config} ({type(exc).__name__}); the connection was made but not saved. "
              "Press Connect again after the host revokes this one.")
        return 1
    print(f"connected: {name} — reaches {', '.join(reaches) or 'nothing'}; until {expires[:10]}; saved in {a.config}")
    print(f"In Cursor: Settings → MCP — switch {name} on if it is off. Then read {name}://brief.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
