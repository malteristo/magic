#!/usr/bin/env python3
"""Render a clean outfacing Markdown artifact as a provenance-bound PDF."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CSS = REPO_ROOT / "system/templates/outfacing/a4.css"
DEFAULT_EXPORT_DIR = REPO_ROOT / "desk/outfacing/exports"
MANIFEST_SCHEMA = 1
MIN_PDF_BYTES = 1_000

CHROME_CANDIDATES = (
    Path("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"),
    Path("/Applications/Chromium.app/Contents/MacOS/Chromium"),
)

DRAFT_RESIDUE = (
    (re.compile(r"\*\[[^\]\n]+\]\*"), "italic placeholder"),
    (re.compile(r"\[(?:TODO|TBD|PLACEHOLDER)\]", re.IGNORECASE), "task placeholder"),
    (re.compile(r"^#{1,6}\s+Das Dokument\s*$", re.MULTILINE), "internal document divider"),
    (re.compile(r"^\*\*(?:Status|Flagged claims):\*\*", re.MULTILINE), "internal draft header"),
    (re.compile(r"\bFallback\b", re.IGNORECASE), "fallback drafting note"),
)


class RenderError(RuntimeError):
    """Raised when a source cannot safely be rendered."""


class VerificationError(RuntimeError):
    """Raised when a PDF no longer matches its declared inputs."""


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def manifest_path(pdf_path: Path) -> Path:
    return pdf_path.with_suffix(pdf_path.suffix + ".json")


def repo_relative(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(REPO_ROOT))
    except ValueError:
        return str(path.resolve())


def resolve_recorded_path(value: str, manifest: Path) -> Path:
    recorded = Path(value)
    if recorded.is_absolute():
        return recorded
    candidate = REPO_ROOT / recorded
    if candidate.exists():
        return candidate
    return manifest.parent / recorded


def command_version(command: list[str]) -> str:
    completed = subprocess.run(
        command,
        check=True,
        capture_output=True,
        text=True,
    )
    output = completed.stdout.strip() or completed.stderr.strip()
    return output.splitlines()[0]


def find_pandoc() -> Path:
    executable = shutil.which("pandoc")
    if not executable:
        raise RenderError("pandoc is not installed; run `brew install pandoc`.")
    return Path(executable)


def find_chrome() -> Path:
    override = os.environ.get("OUTFACING_PDF_CHROME")
    if override:
        candidate = Path(override).expanduser()
        if candidate.is_file() and os.access(candidate, os.X_OK):
            return candidate
        raise RenderError(f"OUTFACING_PDF_CHROME is not executable: {candidate}")
    for candidate in CHROME_CANDIDATES:
        if candidate.is_file() and os.access(candidate, os.X_OK):
            return candidate
    executable = shutil.which("google-chrome") or shutil.which("chromium")
    if executable:
        return Path(executable)
    raise RenderError(
        "Google Chrome or Chromium was not found. "
        "Set OUTFACING_PDF_CHROME to its executable."
    )


def validate_source(source: Path) -> str:
    if not source.is_file():
        raise RenderError(f"Source does not exist: {source}")
    if not source.name.endswith("_clean.md"):
        raise RenderError(
            "Only files ending in `_clean.md` may be rendered as sendable artifacts."
        )
    text = source.read_text(encoding="utf-8")
    if not text.strip():
        raise RenderError("Source is empty.")
    for pattern, label in DRAFT_RESIDUE:
        match = pattern.search(text)
        if match:
            line = text.count("\n", 0, match.start()) + 1
            raise RenderError(f"Refusing {label} at {source}:{line}.")
    return text


def default_output_for(source: Path) -> Path:
    return DEFAULT_EXPORT_DIR / f"{source.stem.removesuffix('_clean')}.pdf"


def render_pdf(
    source: Path,
    output: Path | None = None,
    css: Path = DEFAULT_CSS,
) -> tuple[Path, Path]:
    source = source.expanduser().resolve()
    output = (output or default_output_for(source)).expanduser().resolve()
    css = css.expanduser().resolve()

    validate_source(source)
    if not css.is_file():
        raise RenderError(f"Stylesheet does not exist: {css}")
    if output.suffix.lower() != ".pdf":
        raise RenderError("Output path must end in .pdf.")

    pandoc = find_pandoc()
    chrome = find_chrome()
    output.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix="outfacing-pdf-") as temp_dir:
        temporary = Path(temp_dir)
        html_path = temporary / "document.html"
        pdf_path = temporary / "document.pdf"

        subprocess.run(
            [
                str(pandoc),
                str(source),
                "--from=gfm+smart+fenced_divs",
                "--to=html5",
                "--standalone",
                "--embed-resources",
                f"--css={css}",
                "--variable=lang:de",
                f"--variable=pagetitle:{source.stem}",
                f"--output={html_path}",
            ],
            check=True,
        )
        subprocess.run(
            [
                str(chrome),
                "--headless=new",
                "--disable-gpu",
                "--no-pdf-header-footer",
                f"--print-to-pdf={pdf_path}",
                html_path.as_uri(),
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        _assert_pdf_file(pdf_path)

        staged_pdf = output.with_suffix(output.suffix + ".tmp")
        shutil.copyfile(pdf_path, staged_pdf)
        os.replace(staged_pdf, output)

    renderer = Path(__file__).resolve()
    manifest = manifest_path(output)
    payload: dict[str, Any] = {
        "schema": MANIFEST_SCHEMA,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source": repo_relative(source),
        "source_sha256": sha256_file(source),
        "stylesheet": repo_relative(css),
        "stylesheet_sha256": sha256_file(css),
        "renderer": repo_relative(renderer),
        "renderer_sha256": sha256_file(renderer),
        "pdf": repo_relative(output),
        "pdf_sha256": sha256_file(output),
        "pandoc_version": command_version([str(pandoc), "--version"]),
        "chrome_version": command_version([str(chrome), "--version"]),
    }
    staged_manifest = manifest.with_suffix(manifest.suffix + ".tmp")
    staged_manifest.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    os.replace(staged_manifest, manifest)
    return output, manifest


def _assert_pdf_file(path: Path) -> None:
    if not path.is_file():
        raise VerificationError(f"PDF was not created: {path}")
    if path.stat().st_size < MIN_PDF_BYTES:
        raise VerificationError(f"PDF is unexpectedly small: {path.stat().st_size} bytes")
    with path.open("rb") as handle:
        if handle.read(5) != b"%PDF-":
            raise VerificationError(f"Output is not a PDF: {path}")


def verify_pdf(pdf: Path, manifest: Path | None = None) -> dict[str, Any]:
    pdf = pdf.expanduser().resolve()
    manifest = (manifest or manifest_path(pdf)).expanduser().resolve()
    _assert_pdf_file(pdf)
    if not manifest.is_file():
        raise VerificationError(f"Manifest is missing: {manifest}")

    try:
        payload = json.loads(manifest.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as error:
        raise VerificationError(f"Manifest is unreadable: {manifest}") from error

    if payload.get("schema") != MANIFEST_SCHEMA:
        raise VerificationError("Manifest schema is unsupported.")

    checks = (
        ("source", "source_sha256"),
        ("stylesheet", "stylesheet_sha256"),
        ("renderer", "renderer_sha256"),
        ("pdf", "pdf_sha256"),
    )
    for path_key, digest_key in checks:
        value = payload.get(path_key)
        expected = payload.get(digest_key)
        if not isinstance(value, str) or not isinstance(expected, str):
            raise VerificationError(f"Manifest lacks {path_key}/{digest_key}.")
        checked_path = (
            pdf
            if path_key == "pdf"
            else resolve_recorded_path(value, manifest)
        )
        if not checked_path.is_file():
            raise VerificationError(f"Recorded {path_key} is missing: {checked_path}")
        actual = sha256_file(checked_path)
        if actual != expected:
            raise VerificationError(
                f"{path_key} has changed since rendering: {checked_path}"
            )
    return payload


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Render a `_clean.md` outfacing artifact as a verified PDF."
    )
    parser.add_argument("source", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--css", type=Path, default=DEFAULT_CSS)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        pdf, manifest = render_pdf(args.source, args.output, args.css)
        verify_pdf(pdf, manifest)
    except (RenderError, VerificationError, subprocess.CalledProcessError) as error:
        print(f"ERROR: {error}")
        return 1
    print(f"PDF: {pdf}")
    print(f"Manifest: {manifest}")
    print("Verified: output matches source, stylesheet, and renderer.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
