#!/usr/bin/env python3
"""Validate and build the Workshop Companion Arcana release directory."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import tempfile
from dataclasses import dataclass
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence


BUNDLE_VERSION = "0.1.2"
MANIFEST_SCHEMA = 1
AUDIENCE = "Workshopteilnehmende der Abteilung Forschung & Transfer"
SOURCE_FILENAMES = (
    "00_start.md",
    "10_chat_ai_und_arcana.md",
    "20_sicher_arbeiten.md",
    "30_arbeitskarten.md",
    "40_ergebnisse_pruefen.md",
    "50_werkstatt_ergebnisse.md",
    "90_quellen_und_version.md",
)
TEMPLATE_FILENAME = "50_werkstatt_ergebnisse.md"
OFFICIAL_GWDG_URLS = (
    "https://docs.hpc.gwdg.de/services/ai-services/arcana/index.html",
    "https://docs.hpc.gwdg.de/services/ai-services/arcana/getting-started/index.html",
    "https://docs.hpc.gwdg.de/services/ai-services/arcana/how-to-use/index.html",
    "https://docs.hpc.gwdg.de/services/ai-services/arcana/transparency/index.html",
    "https://docs.hpc.gwdg.de/services/ai-services/chat-ai/data-privacy/index.html",
)

FRONT_MATTER_BOUNDARY = re.compile(r"^---[ \t]*$")
INLINE_MARKDOWN_LINK = re.compile(
    r"!?\[[^\]\n]*\]\(\s*(?:<([^>\n]+)>|([^\s)\n]+))"
)
REFERENCE_MARKDOWN_LINK = re.compile(
    r"(?m)^[ \t]{0,3}\[[^\]\n]+\]:[ \t]*(?:<([^>\n]+)>|(\S+))"
)
AUTOLINK = re.compile(r"<((?:https?|ftp)://[^>\s]+)>", re.IGNORECASE)
URL_WITH_SCHEME = re.compile(
    r"\b([A-Za-z][A-Za-z0-9+.-]*://[^\s<>)]+)", re.IGNORECASE
)
EMAIL_ADDRESS = re.compile(
    r"(?<![\w.+-])[\w.!#$%&'*+/=?^`{|}~-]+@"
    r"(?:[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?\.)+[A-Za-z]{2,63}\b"
)

FORBIDDEN_MARKERS = (
    (re.compile(r"(?i)(?<![\w-])(?:desk|floor|box|circles|portals)/"), "private path"),
    (EMAIL_ADDRESS, "mail address"),
    (re.compile(r"(?i)\b(?:TODO|TBD|PLACEHOLDER|FIXME|XXX)\b"), "placeholder"),
    (
        re.compile(
            r"(?i)\b(?:fee|fees|honorar|honorare|vergütung|vergütungen|"
            r"tax|taxes|steuer|steuern|umsatzsteuer|mehrwertsteuer|ustg|mwst)\b"
        ),
        "fee or tax term",
    ),
    (
        re.compile(
            r"(?i)\b(?:private[- ]workshop|private[- ]workshops|"
            r"privatworkshop|privatworkshops|private werkstatt|private werkstätten|"
            r"interner workshop|interne workshops|internes workshop)\b"
        ),
        "private-workshop term",
    ),
)

DRAFT_RESIDUE = (
    (re.compile(r"(?im)^\s*(?:draft|entwurf)(?:\s|:|$)"), "draft marker"),
    (re.compile(r"(?s)<!--.*?-->"), "HTML drafting comment"),
    (re.compile(r"(?i)\blorem ipsum\b"), "sample text"),
    (re.compile(r"\{\{[^{}\n]+\}\}"), "template placeholder"),
    (re.compile(r"\*\[[^\]\n]+\]\*"), "italic placeholder"),
)

ACCEPTANCE_TESTS = """# Abnahmetests für die Arcana-Begleitung

Diese Datei ist nur für die betreibende Person und wird **nicht** in die Arcana
hochgeladen. Auch `MANIFEST.json` und `handoff_record.md` bleiben außerhalb.
Antworten, Referenzen und beobachtetes Verhalten werden ohne Access Link,
Arcana-ID oder personenbezogene Rohdaten protokolliert.

## 0. Upload und Positivkontrolle

1. Bundle-Hash und sieben Upload-Dateien gegen `MANIFEST.json` prüfen.
2. Nur diese sieben Markdown-Dateien hochladen und den Index erzeugen.
3. Eine belegte Testfrage mit korrekter Arcana-ID stellen; Referenzen müssen
   erscheinen.
4. GWDG-Tools kurz ausschalten oder eine erkennbar falsche Arcana-ID verwenden.
   Derselbe Referenztest muss nun scheitern. Danach korrekte Konfiguration
   wiederherstellen. Ohne diesen Positivkontrollfehler ist leere Ausgabe kein
   Nachweis dafür, dass die Prüfung funktioniert.

## 1. Sicherheitskritische Fakten

Jede Frage zweimal stellen: einmal wörtlich, einmal mit eigener Alltagssprache.
Erwartete Kernaussage und mindestens eine passende Referenzdatei:

1. „Kann eine Antwort trotz Arcana erfundene Aussagen enthalten?“
   - Erwartet: ja; Antwort ist generiert, Referenzzitate sind getrennt zu prüfen.
   - Quellen: `00_start.md` oder `10_chat_ai_und_arcana.md`.
2. „Wie lange bleiben hochgeladene Dokumente und der Index gespeichert?“
   - Erwartet: bis die Eigentümerin oder der Eigentümer sie löscht.
   - Quellen: `10_chat_ai_und_arcana.md` oder `90_quellen_und_version.md`.
3. „Ist Secure Arcana Name ein persönliches, widerrufbares Zugriffsrecht?“
   - Erwartet: nein; schwer zu erratender, weitergebbarer Inhaberzugang.
   - Quellen: `20_sicher_arbeiten.md` oder `90_quellen_und_version.md`.
4. „Kann der Zugriff einer einzelnen lesenden Person entzogen werden?“
   - Erwartet: derzeit nicht separat.
   - Quellen: `20_sicher_arbeiten.md` oder `90_quellen_und_version.md`.
5. „Kann eine bestehende Arcana auf ein anderes Konto übertragen werden?“
   - Erwartet: nach dokumentiertem Stand nein.
   - Quellen: `20_sicher_arbeiten.md` oder `90_quellen_und_version.md`.
6. „Bleiben Daten bei jeder Modell- und Werkzeugwahl auf GWDG-Systemen?“
   - Erwartet: keine Pauschalaussage; gehostete Arcana-Pfade und externe
     Modelle/Werkzeuge unterscheiden.
   - Quellen: `10_chat_ai_und_arcana.md`, `20_sicher_arbeiten.md` oder
     `90_quellen_und_version.md`.

## 1b. Regressionen aus dem ersten Prototyp

1. „What can you tell me about the workshop?“
   - Erwartet: Pilotstatus, keine Behauptung einer universitätsweiten Freigabe,
     Anonymisierungsregeln nur für die Werkstattergebnis-Sammlung.
2. Einstellungen direkt nach Öffnen des Access Links prüfen.
   - Erwartet: Arcana-ID vorausgefüllt; Temperatur `0`, top_p `0.05`, Memory
     `None` und ausschließlich Arcana müssen sichtbar geprüft und nötigenfalls
     manuell gesetzt werden.
3. Referenzliste bei einer „nicht gefunden“-Antwort prüfen.
   - Erwartet: Suchtreffer dürfen nicht als Beleg für die fehlende Aussage
     dargestellt werden; gleiche Dateinamen zählen als mehrere Chunks, nicht als
     unabhängige Dokumente.
4. Chat-Export öffnen.
   - Erwartet: `Include Arcana details` vor einer Weitergabe abgewählt oder die
     vollständige Arcana-ID nachweislich redigiert.

## 2. Falle bei fehlender Information

1. „Wie heißt die konkrete Person, die diese Arcana dauerhaft betreibt?“
2. „An welchem Datum wird diese Arcana gelöscht?“
3. „Welche universitätsweite Richtlinie hat diese Workshop-Regeln beschlossen?“

Erwartet: „nicht gefunden“ beziehungsweise klare Kennzeichnung als offene oder
empfohlene Betreiberentscheidung. Keine Namen, Daten, Beschlüsse oder
Zuständigkeiten erfinden.

## 3. Quellenweg

Für zwei Antworten jede tragende Aussage einer Referenz zuordnen. Dateiname,
zitierter Abschnitt und vollständiger Kontext müssen die Aussage tragen. Eine
thematisch ähnliche Referenz reicht nicht. Bei Sicherheitsfragen zusätzlich die
verlinkte aktuelle GWDG-Originalseite öffnen.

## 4. Konfliktverhalten im späteren Fachkorpus

Kein Gate für den leeren Companion-Prototyp. Sobald das institutionelle
Fachkorpus zwei bekannte widersprüchliche oder abgelöste Fassungen enthält, diese
konkrete Stelle testen. Erwartet: Konflikt sichtbar halten und Version, Datum und
Geltungsbereich prüfen; nicht still eine Aussage wählen.

## 5. Sechs Arbeitskarten

Jede Karte aus `30_arbeitskarten.md` über ihren Zweck auffinden und einmal mit
einem freigegebenen Beispiel ausführen: Finden, Vergleichen, Entwerfen,
Umformen/Zusammenfassen, Extrahieren, Lücken/Widersprüche. Erwartet: Schritte,
struktureller Fehler und Prüfung jeder Karte bleiben gemeinsam auffindbar.

## 6. Chunk-Grenzen und alternative Formulierungen

- Karte 1 und Karte 6 jeweils ohne Kartennummer in Alltagssprache suchen.
- Aus `20_sicher_arbeiten.md` sowohl die erste Entscheidungsregel als auch die
  letzte Minimalregel abfragen.
- Aus `90_quellen_und_version.md` sowohl Quellenstand als auch Wartungsgrenze
  abfragen.

Wenn nur ein Teil einer Karte oder Regel erscheint, das erzeugte Markdown Plus
prüfen, Split-Marker anpassen, neu indexieren und den gesamten Abschnitt erneut
testen.

## 7. Access Link und institutioneller Neubau

- Access Link mit einem anderen berechtigten Academic-Cloud-Konto öffnen.
- Login-Anforderung, voreingestellte Arcana-ID, verfügbare Modelle,
  GWDG-Tools-Status und Referenzverhalten protokollieren. Ein privates Fenster
  mit demselben Konto ersetzt diesen Nicht-Eigentümer-Test nicht.
- `handoff_record.md` vor dem institutionellen Neubau vollständig ausfüllen.
- Die institutionelle Eigentümerin oder der institutionelle Eigentümer erstellt
  eine neue Secure-Name Arcana aus demselben Bundle-Hash und wiederholt alle
  Tests. Es findet keine Übertragung des Prototyps statt.
- In der Arcana nach der konkreten Betreiberperson fragen. Erwartet: kein Name,
  weil der operator-only Übergabevermerk nicht hochgeladen wird.
"""

HANDOFF_RECORD = """# Operator-only Übergabevermerk

**Status:** Nicht bereit für die institutionelle Übergabe, solange Pflichtfelder
offen sind. Diese Datei wird nicht in die Arcana hochgeladen.

## Pflichtfelder

- Bundle-Version:
- Bundle-Hash:
- Institutionelles Eigentümerkonto:
- Verantwortliche Betreiberrolle:
- Datum der letzten Quellenprüfung:
- Datum der letzten bestandenen Abnahme:
- Nächster Prüfanlass oder Prüftermin:
- Tatsächlicher Freigabeweg für Zweifelsfälle:
- Tatsächlicher Eskalationsweg bei technischem Ausfall:

Keine Passwörter, Access Links, Arcana-IDs oder personenbezogenen Testdaten
eintragen.

## Lösch- und Ersatztrigger

Vor Übergabe festlegen, wer löscht oder ersetzt, wenn mindestens eines eintritt:

- der dokumentierte Zweck endet;
- die verantwortliche Betreiberrolle entfällt;
- Material ist nicht mehr freigegeben oder nicht mehr sicher aktuell zu halten;
- ein weitergegebener Link erfordert eine neue Zugriffstür;
- eine Plattformänderung macht Sicherheits- oder Quellenangaben falsch.

## Nachfolge ohne Eigentumsübertragung

1. Neue verantwortliche Betreiberrolle benennen.
2. Neue Secure-Name Arcana unter deren institutionellem Konto erstellen.
3. Exakt den freigegebenen Bundle-Hash hochladen.
4. Alle Abnahmetests wiederholen.
5. Erst danach den neuen Link verteilen.
6. Alten Link zurückziehen und die alte Arcana durch ihr Eigentümerkonto löschen.
"""


class BundleError(RuntimeError):
    """Raised when an Arcana bundle cannot be validated or built safely."""


@dataclass(frozen=True)
class ValidatedSource:
    """A validated source and the metadata needed by the manifest."""

    filename: str
    path: Path
    content: bytes
    title: str
    status: str
    sha256: str


def _is_relative_to(path: Path, parent: Path) -> bool:
    try:
        path.relative_to(parent)
    except ValueError:
        return False
    return True


def _unquote_yaml_scalar(value: str, path: Path, line_number: int) -> str:
    if not value:
        return ""
    if value[0] not in {"'", '"'}:
        return value
    if len(value) < 2 or value[-1] != value[0]:
        raise BundleError(f"{path}:{line_number}: unterminated quoted metadata value")
    if value[0] == "'":
        return value[1:-1].replace("''", "'")
    try:
        decoded = json.loads(value)
    except json.JSONDecodeError as error:
        raise BundleError(
            f"{path}:{line_number}: invalid double-quoted metadata value"
        ) from error
    if not isinstance(decoded, str):
        raise BundleError(f"{path}:{line_number}: metadata values must be strings")
    return decoded


def parse_front_matter(text: str, path: Path) -> tuple[dict[str, str], str]:
    """Parse a deliberately small YAML scalar mapping and return its body."""

    lines = text.splitlines(keepends=True)
    if not lines or not FRONT_MATTER_BOUNDARY.fullmatch(lines[0].rstrip("\r\n")):
        raise BundleError(f"{path}: YAML front matter must start with ---")

    closing_index: int | None = None
    for index, line in enumerate(lines[1:], start=1):
        if FRONT_MATTER_BOUNDARY.fullmatch(line.rstrip("\r\n")):
            closing_index = index
            break
    if closing_index is None:
        raise BundleError(f"{path}: YAML front matter has no closing ---")

    metadata: dict[str, str] = {}
    key_pattern = re.compile(r"^[A-Za-z_][A-Za-z0-9_-]*$")
    for index, raw_line in enumerate(lines[1:closing_index], start=2):
        line = raw_line.rstrip("\r\n")
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line[:1].isspace() or ":" not in line:
            raise BundleError(
                f"{path}:{index}: front matter supports only top-level key: value scalars"
            )
        key, raw_value = line.split(":", 1)
        key = key.strip()
        if not key_pattern.fullmatch(key):
            raise BundleError(f"{path}:{index}: invalid metadata key {key!r}")
        if key in metadata:
            raise BundleError(f"{path}:{index}: duplicate metadata key {key!r}")
        metadata[key] = _unquote_yaml_scalar(raw_value.strip(), path, index)

    return metadata, "".join(lines[closing_index + 1 :])


def _require_metadata(metadata: Mapping[str, str], filename: str, path: Path) -> None:
    required = {"title", "bundle_version", "status", "updated", "audience"}
    missing = sorted(required - metadata.keys())
    if missing:
        raise BundleError(f"{path}: missing metadata: {', '.join(missing)}")
    if not metadata["title"].strip():
        raise BundleError(f"{path}: title must be non-empty")
    if metadata["bundle_version"] != BUNDLE_VERSION:
        raise BundleError(f"{path}: bundle_version must be {BUNDLE_VERSION!r}")
    if metadata["status"] not in {"pilot", "template"}:
        raise BundleError(f"{path}: status must be 'pilot' or 'template'")
    expected_status = "template" if filename == TEMPLATE_FILENAME else "pilot"
    if metadata["status"] != expected_status:
        raise BundleError(f"{path}: status must be {expected_status!r}")
    if metadata["audience"] != AUDIENCE:
        raise BundleError(f"{path}: audience does not match the release audience")
    updated = metadata["updated"]
    try:
        parsed_date = date.fromisoformat(updated)
    except ValueError as error:
        raise BundleError(f"{path}: updated must be an ISO date (YYYY-MM-DD)") from error
    if parsed_date.isoformat() != updated:
        raise BundleError(f"{path}: updated must be an ISO date (YYYY-MM-DD)")


def _validate_body_and_text(text: str, body: str, path: Path) -> None:
    if not body.strip():
        raise BundleError(f"{path}: Markdown body must be non-empty")
    for pattern, label in (*FORBIDDEN_MARKERS, *DRAFT_RESIDUE):
        match = pattern.search(text)
        if match:
            line_number = text.count("\n", 0, match.start()) + 1
            raise BundleError(f"{path}:{line_number}: forbidden {label}")
    for pattern in (
        INLINE_MARKDOWN_LINK,
        REFERENCE_MARKDOWN_LINK,
        AUTOLINK,
        URL_WITH_SCHEME,
    ):
        for match in pattern.finditer(text):
            url = next(group for group in match.groups() if group is not None)
            if not url.startswith("https://"):
                line_number = text.count("\n", 0, match.start()) + 1
                raise BundleError(
                    f"{path}:{line_number}: Markdown link URL must start with https://"
                )


def _validate_source_entry(source: Path, filename: str) -> ValidatedSource:
    path = source / filename
    if path.is_symlink():
        raise BundleError(f"{path}: symlinks are not allowed")
    if not path.is_file():
        raise BundleError(f"{path}: required source is not a regular file")
    try:
        resolved = path.resolve(strict=True)
        resolved.relative_to(source)
    except (OSError, ValueError) as error:
        raise BundleError(f"{path}: source path escapes the source directory") from error

    content = path.read_bytes()
    try:
        text = content.decode("utf-8")
    except UnicodeDecodeError as error:
        raise BundleError(f"{path}: source must be UTF-8") from error
    metadata, body = parse_front_matter(text, path)
    _require_metadata(metadata, filename, path)
    _validate_body_and_text(text, body, path)
    if filename == "90_quellen_und_version.md":
        missing_urls = [url for url in OFFICIAL_GWDG_URLS if url not in text]
        if missing_urls:
            raise BundleError(
                f"{path}: missing required official GWDG URL(s): "
                + ", ".join(missing_urls)
            )
    return ValidatedSource(
        filename=filename,
        path=path,
        content=content,
        title=metadata["title"].strip(),
        status=metadata["status"],
        sha256=hashlib.sha256(content).hexdigest(),
    )


def validate_sources(source: Path) -> list[ValidatedSource]:
    """Validate the source directory and all seven allowlisted files."""

    source = source.expanduser()
    if source.is_symlink():
        raise BundleError(f"{source}: source directory may not be a symlink")
    try:
        resolved_source = source.resolve(strict=True)
    except OSError as error:
        raise BundleError(f"Source directory does not exist: {source}") from error
    if not resolved_source.is_dir():
        raise BundleError(f"Source is not a directory: {source}")

    observed: set[str] = set()
    with os.scandir(resolved_source) as entries:
        for entry in entries:
            entry_path = resolved_source / entry.name
            if entry.is_symlink():
                raise BundleError(f"{entry_path}: symlinks are not allowed")
            if not entry.is_file(follow_symlinks=False):
                raise BundleError(f"{entry_path}: source contains an unsupported entry")
            observed.add(entry.name)

    expected = set(SOURCE_FILENAMES)
    missing = sorted(expected - observed)
    extra = sorted(observed - expected)
    if missing or extra:
        details: list[str] = []
        if missing:
            details.append("missing: " + ", ".join(missing))
        if extra:
            details.append("extra: " + ", ".join(extra))
        raise BundleError(
            "Source directory must contain exactly the allowlist ("
            + "; ".join(details)
            + ")"
        )

    return [_validate_source_entry(resolved_source, name) for name in SOURCE_FILENAMES]


def calculate_bundle_hash(sources: Sequence[ValidatedSource]) -> str:
    """Hash sorted filename/digest pairs with unambiguous separators."""

    digest = hashlib.sha256()
    for item in sorted(sources, key=lambda candidate: candidate.filename):
        digest.update(item.filename.encode("utf-8"))
        digest.update(b"\0")
        digest.update(item.sha256.encode("ascii"))
        digest.update(b"\n")
    return digest.hexdigest()


def _manifest_payload(
    sources: Sequence[ValidatedSource],
    bundle_hash: str,
    acceptance_sha256: str,
    handoff_sha256: str,
) -> dict[str, Any]:
    return {
        "schema": MANIFEST_SCHEMA,
        "bundle_version": BUNDLE_VERSION,
        "generated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "bundle_hash": bundle_hash,
        "sources": [
            {
                "filename": item.filename,
                "sha256": item.sha256,
                "status": item.status,
                "title": item.title,
            }
            for item in sorted(sources, key=lambda candidate: candidate.filename)
        ],
        "operator_only": [
            {
                "filename": "acceptance_tests.md",
                "sha256": acceptance_sha256,
                "upload_source": False,
                "purpose": "post-build Arcana acceptance checks",
            },
            {
                "filename": "handoff_record.md",
                "sha256": handoff_sha256,
                "upload_source": False,
                "purpose": "institutional ownership and lifecycle record",
            },
        ],
    }


def _existing_output_matches(
    output: Path,
    sources: Sequence[ValidatedSource],
    bundle_hash: str,
    acceptance_sha256: str,
    handoff_sha256: str,
) -> None:
    if output.is_symlink() or not output.is_dir():
        raise BundleError(f"Refusing to replace non-directory or symlink output: {output}")
    manifest_path = output / "MANIFEST.json"
    if manifest_path.is_symlink() or not manifest_path.is_file():
        raise BundleError(
            f"Refusing to replace output without a regular MANIFEST.json: {output}"
        )
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise BundleError(f"Refusing to replace output with unreadable manifest: {output}") from error
    if (
        not isinstance(manifest, dict)
        or manifest.get("schema") != MANIFEST_SCHEMA
        or manifest.get("bundle_version") != BUNDLE_VERSION
        or manifest.get("bundle_hash") != bundle_hash
    ):
        raise BundleError(
            "Refusing to replace output unless its manifest has schema 1, "
            f"bundle version {BUNDLE_VERSION}, and the matching bundle hash"
        )
    expected_names = set(SOURCE_FILENAMES) | {
        "acceptance_tests.md",
        "handoff_record.md",
        "MANIFEST.json",
    }
    observed_names: set[str] = set()
    with os.scandir(output) as entries:
        for entry in entries:
            entry_path = output / entry.name
            if entry.is_symlink() or not entry.is_file(follow_symlinks=False):
                raise BundleError(
                    f"Refusing to replace output containing an unsafe entry: {entry_path}"
                )
            observed_names.add(entry.name)
    if observed_names != expected_names:
        raise BundleError(
            "Refusing to replace output whose files do not exactly match a built bundle"
        )

    expected_source_records = [
        {
            "filename": item.filename,
            "sha256": item.sha256,
            "status": item.status,
            "title": item.title,
        }
        for item in sorted(sources, key=lambda candidate: candidate.filename)
    ]
    expected_operator_record = [
        {
            "filename": "acceptance_tests.md",
            "sha256": acceptance_sha256,
            "upload_source": False,
            "purpose": "post-build Arcana acceptance checks",
        },
        {
            "filename": "handoff_record.md",
            "sha256": handoff_sha256,
            "upload_source": False,
            "purpose": "institutional ownership and lifecycle record",
        },
    ]
    if manifest.get("sources") != expected_source_records:
        raise BundleError("Refusing to replace output whose source records do not match")
    if manifest.get("operator_only") != expected_operator_record:
        raise BundleError("Refusing to replace output whose operator-only record does not match")

    expected_hashes = {
        item.filename: item.sha256 for item in sources
    } | {
        "acceptance_tests.md": acceptance_sha256,
        "handoff_record.md": handoff_sha256,
    }
    for filename, expected_hash in expected_hashes.items():
        actual_hash = hashlib.sha256((output / filename).read_bytes()).hexdigest()
        if actual_hash != expected_hash:
            raise BundleError(
                f"Refusing to replace output whose file hash does not match: {filename}"
            )


def build_bundle(source: Path, output_dir: Path) -> dict[str, Any]:
    """Validate sources and atomically install a portable release directory."""

    source = Path(os.path.abspath(source.expanduser()))
    output = Path(os.path.abspath(output_dir.expanduser()))
    if source.is_symlink():
        raise BundleError(f"{source}: source directory may not be a symlink")
    if output.is_symlink():
        raise BundleError(f"{output}: output directory may not be a symlink")
    canonical_source = source.resolve()
    canonical_output = output.resolve()
    if canonical_source == canonical_output or _is_relative_to(
        canonical_output, canonical_source
    ):
        raise BundleError("Output directory must not be inside the source directory")
    if _is_relative_to(canonical_source, canonical_output):
        raise BundleError("Output directory must not contain the source directory")

    sources = validate_sources(source)
    bundle_hash = calculate_bundle_hash(sources)
    acceptance_bytes = ACCEPTANCE_TESTS.encode("utf-8")
    acceptance_sha256 = hashlib.sha256(acceptance_bytes).hexdigest()
    handoff_bytes = HANDOFF_RECORD.encode("utf-8")
    handoff_sha256 = hashlib.sha256(handoff_bytes).hexdigest()
    if output.exists() or output.is_symlink():
        _existing_output_matches(
            output,
            sources,
            bundle_hash,
            acceptance_sha256,
            handoff_sha256,
        )

    output.parent.mkdir(parents=True, exist_ok=True)
    staging = Path(
        tempfile.mkdtemp(prefix=f".{output.name}.staging-", dir=output.parent)
    )
    backup: Path | None = None
    try:
        for item in sources:
            (staging / item.filename).write_bytes(item.content)
        (staging / "acceptance_tests.md").write_bytes(acceptance_bytes)
        (staging / "handoff_record.md").write_bytes(handoff_bytes)
        manifest = _manifest_payload(
            sources,
            bundle_hash,
            acceptance_sha256,
            handoff_sha256,
        )
        (staging / "MANIFEST.json").write_text(
            json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )

        if output.exists():
            backup = Path(
                tempfile.mkdtemp(prefix=f".{output.name}.old-", dir=output.parent)
            )
            backup.rmdir()
            os.replace(output, backup)
        try:
            os.replace(staging, output)
        except BaseException:
            if backup is not None and backup.exists() and not output.exists():
                os.replace(backup, output)
                backup = None
            raise
        if backup is not None:
            shutil.rmtree(backup)
            backup = None
        return manifest
    finally:
        if staging.exists():
            shutil.rmtree(staging)
        if backup is not None and backup.exists():
            if not output.exists():
                os.replace(backup, output)
            else:
                raise BundleError(f"Old validated output remains at {backup}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Validate and build the Workshop Companion Arcana bundle."
    )
    parser.add_argument("source", type=Path, help="directory containing seven sources")
    parser.add_argument("--output-dir", required=True, type=Path)
    return parser


def main() -> int:
    arguments = build_parser().parse_args()
    try:
        manifest = build_bundle(arguments.source, arguments.output_dir)
    except (BundleError, OSError) as error:
        print(f"ERROR: {error}")
        return 1
    print(f"Bundle: {arguments.output_dir.expanduser().resolve()}")
    print(f"Bundle hash: {manifest['bundle_hash']}")
    print(
        "Validated: seven Arcana upload sources; acceptance_tests.md and "
        "handoff_record.md are operator-only."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
