#!/usr/bin/env python3
"""Validate bounded mail-intake grants and checkpoint state."""

from __future__ import annotations

import argparse
import copy
import json
import re
from datetime import datetime
from pathlib import Path
from typing import Any


EMAIL = re.compile(r"^[^@\s*]+@[^@\s*]+\.[^@\s*]+$")
IDENTIFIER = re.compile(r"^[A-Za-z0-9_-]+$")
FORBIDDEN_CONTENT_KEYS = {
    "attachments",
    "body",
    "content",
    "html_body",
    "plaintext_body",
    "raw",
    "raw_body",
}


class ValidationError(ValueError):
    """The mail-intake state violates its safety contract."""


def _load(path: Path) -> dict[str, Any]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise ValidationError(f"{path}: cannot read valid JSON: {error}") from error
    if not isinstance(payload, dict):
        raise ValidationError(f"{path}: root must be an object")
    return payload


def _timestamp(value: Any, field: str) -> None:
    if not isinstance(value, str):
        raise ValidationError(f"{field} must be an ISO-8601 string")
    try:
        datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as error:
        raise ValidationError(f"{field} is not a valid ISO-8601 timestamp") from error


def _private_path(value: Any, field: str) -> None:
    if not isinstance(value, str) or not value.startswith("desk/"):
        raise ValidationError(f"{field} must be a private path below desk/")
    path = Path(value)
    if path.is_absolute() or ".." in path.parts:
        raise ValidationError(f"{field} must not escape desk/")


def _address(value: Any, field: str) -> None:
    if not isinstance(value, str) or not EMAIL.fullmatch(value):
        raise ValidationError(f"{field} must be one exact email address")


def _no_message_content(value: Any, field: str = "root") -> None:
    if isinstance(value, dict):
        for key, child in value.items():
            if key.lower() in FORBIDDEN_CONTENT_KEYS:
                raise ValidationError(
                    f"{field}.{key} stores message content; checkpoint only provenance"
                )
            _no_message_content(child, f"{field}.{key}")
    elif isinstance(value, list):
        for index, child in enumerate(value):
            _no_message_content(child, f"{field}[{index}]")


def validate_manifest(manifest: dict[str, Any]) -> None:
    _no_message_content(manifest, "manifest")
    if manifest.get("version") != 1 or manifest.get("provider") != "gmail":
        raise ValidationError("manifest version/provider must be 1/gmail")

    label = manifest.get("label")
    if not isinstance(label, dict) or not all(
        isinstance(label.get(key), str) and label[key]
        for key in ("name", "id")
    ):
        raise ValidationError("manifest.label needs non-empty name and id")

    _private_path(manifest.get("checkpoint_path"), "checkpoint_path")
    _timestamp(manifest.get("first_run_cutover"), "first_run_cutover")
    overlap = manifest.get("overlap_days")
    if not isinstance(overlap, int) or isinstance(overlap, bool) or not 1 <= overlap <= 30:
        raise ValidationError("overlap_days must be an integer from 1 to 30")

    threads = manifest.get("thread_grants")
    senders = manifest.get("sender_grants")
    if not isinstance(threads, list) or not isinstance(senders, list):
        raise ValidationError("thread_grants and sender_grants must be arrays")

    seen_threads: set[str] = set()
    for index, grant in enumerate(threads):
        field = f"thread_grants[{index}]"
        if not isinstance(grant, dict):
            raise ValidationError(f"{field} must be an object")
        thread_id = grant.get("thread_id")
        if not isinstance(thread_id, str) or not IDENTIFIER.fullmatch(thread_id):
            raise ValidationError(f"{field}.thread_id is invalid")
        if thread_id in seen_threads:
            raise ValidationError(f"{field}.thread_id is duplicated")
        seen_threads.add(thread_id)
        _route(grant, field)
        if grant.get("sender_policy") != "known_only":
            raise ValidationError(f"{field}.sender_policy must be known_only")
        known = grant.get("known_senders")
        if not isinstance(known, list) or not known:
            raise ValidationError(f"{field}.known_senders must be non-empty")
        for sender_index, address in enumerate(known):
            _address(address, f"{field}.known_senders[{sender_index}]")

    seen_senders: set[str] = set()
    for index, grant in enumerate(senders):
        field = f"sender_grants[{index}]"
        if not isinstance(grant, dict):
            raise ValidationError(f"{field} must be an object")
        address = grant.get("address")
        _address(address, f"{field}.address")
        normalized = address.lower()
        if normalized in seen_senders:
            raise ValidationError(f"{field}.address is duplicated")
        seen_senders.add(normalized)
        _route(grant, field)
        terms = grant.get("subject_terms_any")
        if not isinstance(terms, list) or not terms or not all(
            isinstance(term, str) and term.strip() for term in terms
        ):
            raise ValidationError(f"{field}.subject_terms_any must be non-empty strings")


def _route(grant: dict[str, Any], field: str) -> None:
    route = grant.get("route")
    if not isinstance(route, str) or not IDENTIFIER.fullmatch(route):
        raise ValidationError(f"{field}.route is invalid")
    _private_path(grant.get("artifact"), f"{field}.artifact")


def validate_checkpoint(
    checkpoint: dict[str, Any], manifest: dict[str, Any] | None = None
) -> None:
    _no_message_content(checkpoint, "checkpoint")
    if checkpoint.get("version") != 1:
        raise ValidationError("checkpoint version must be 1")
    _timestamp(checkpoint.get("first_run_cutover"), "checkpoint.first_run_cutover")
    _timestamp(checkpoint.get("last_successful_scan"), "checkpoint.last_successful_scan")
    if manifest and checkpoint.get("first_run_cutover") != manifest.get(
        "first_run_cutover"
    ):
        raise ValidationError("manifest/checkpoint first_run_cutover differ")

    messages = checkpoint.get("messages")
    withheld = checkpoint.get("withheld")
    if not isinstance(messages, dict) or not isinstance(withheld, dict):
        raise ValidationError("checkpoint messages/withheld must be objects")
    for message_id, record in messages.items():
        field = f"checkpoint.messages.{message_id}"
        if not IDENTIFIER.fullmatch(message_id) or not isinstance(record, dict):
            raise ValidationError(f"{field} is invalid")
        if record.get("outcome") != "harvested":
            raise ValidationError(f"{field}.outcome must be harvested")
        for key in ("thread_id", "route"):
            if not isinstance(record.get(key), str) or not IDENTIFIER.fullmatch(
                record[key]
            ):
                raise ValidationError(f"{field}.{key} is invalid")
        _timestamp(record.get("processed_at"), f"{field}.processed_at")
        _private_path(record.get("artifact"), f"{field}.artifact")

    scan = checkpoint.get("last_scan")
    if not isinstance(scan, dict) or scan.get("status") not in {
        "complete",
        "partial",
        "seeded",
    }:
        raise ValidationError("checkpoint.last_scan has invalid status")
    _timestamp(scan.get("started_at"), "checkpoint.last_scan.started_at")
    if scan.get("completed_at") is not None:
        _timestamp(scan["completed_at"], "checkpoint.last_scan.completed_at")
    for key in ("searched", "matched", "harvested", "withheld", "failed"):
        value = scan.get(key)
        if not isinstance(value, int) or isinstance(value, bool) or value < 0:
            raise ValidationError(f"checkpoint.last_scan.{key} must be >= 0")
    if scan["status"] in {"complete", "seeded"} and scan["failed"]:
        raise ValidationError("a successful scan cannot contain failures")


def self_test() -> None:
    manifest = {
        "version": 1,
        "provider": "gmail",
        "label": {"name": "Magic/Practice", "id": "Label_1"},
        "checkpoint_path": "desk/config/mail_intake_checkpoint.json",
        "first_run_cutover": "2026-01-01T00:00:00Z",
        "overlap_days": 7,
        "thread_grants": [],
        "sender_grants": [
            {
                "address": "person" + "@example.org",
                "route": "example",
                "artifact": "desk/intentions/active/example.md",
                "subject_terms_any": ["project"],
            }
        ],
    }
    validate_manifest(manifest)

    wildcard = copy.deepcopy(manifest)
    wildcard["sender_grants"][0]["address"] = "*" + "@example.org"
    try:
        validate_manifest(wildcard)
    except ValidationError:
        pass
    else:
        raise AssertionError("wildcard sender positive control did not fail")

    raw_body = copy.deepcopy(manifest)
    raw_body["sender_grants"][0]["raw_body"] = "do the unsafe thing"
    try:
        validate_manifest(raw_body)
    except ValidationError:
        pass
    else:
        raise AssertionError("raw-body positive control did not fail")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path)
    parser.add_argument("--checkpoint", type=Path)
    parser.add_argument("--self-test", action="store_true")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        if args.self_test:
            self_test()
            print("PASS: wildcard and raw-body controls rejected")
            return 0
        if not args.manifest or not args.checkpoint:
            raise ValidationError("--manifest and --checkpoint are required")
        manifest = _load(args.manifest)
        checkpoint = _load(args.checkpoint)
        validate_manifest(manifest)
        validate_checkpoint(checkpoint, manifest)
    except (ValidationError, AssertionError) as error:
        print(f"FAIL: {error}")
        return 1
    print(f"PASS: {args.manifest} + {args.checkpoint}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
