#!/usr/bin/env python3
"""Verify that an outfacing PDF still matches its source and renderer."""

from __future__ import annotations

import argparse
from pathlib import Path

from render_outfacing_pdf import VerificationError, verify_pdf


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Check an outfacing PDF against its provenance manifest."
    )
    parser.add_argument("pdf", type=Path)
    parser.add_argument("--manifest", type=Path)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        payload = verify_pdf(args.pdf, args.manifest)
    except VerificationError as error:
        print(f"FAIL: {error}")
        return 1
    print(f"PASS: {args.pdf.expanduser().resolve()}")
    print(f"Source: {payload['source']}")
    print(f"Generated: {payload['generated_at']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
