#!/usr/bin/env python3
"""Validate structural ADR conventions without third-party dependencies."""

from __future__ import annotations

import re
import sys
from pathlib import Path


STATUSES = {"draft", "accepted", "rejected", "withdrawn", "deprecated", "superseded"}
REQUIRED_KEYS = {
    "number",
    "title",
    "status",
    "date",
    "decision-makers",
    "consulted",
    "informed",
    "supersedes",
    "superseded-by",
}
REQUIRED_HEADINGS = {
    "Context and problem statement",
    "Decision drivers",
    "Considered options",
    "Decision outcome",
    "Consequences",
    "Confirmation",
    "Links",
}
FILENAME = re.compile(r"^(?P<number>\d{4})-(?P<slug>[a-z0-9]+(?:-[a-z0-9]+)*)\.md$")
H1 = re.compile(r"^# ADR (?P<number>\d{4}): (?P<title>.+?)\s*$", re.MULTILINE)
HEADING = re.compile(r"^## (?P<title>.+?)\s*$", re.MULTILINE)
LINK = re.compile(r"\[[^\]]+\]\((?P<target>[^)]+\.md(?:#[^)]*)?)\)")


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}, text
    values: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if not line.strip() or line.lstrip().startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip('"\'')
    return values, text[end + 5 :]


def parse_ref_list(raw: str) -> list[str]:
    value = raw.strip()
    if value in {"", "[]", "null", "~"}:
        return []
    if value.startswith("[") and value.endswith("]"):
        value = value[1:-1]
    return [part.strip().strip('"\'') for part in value.split(",") if part.strip()]


def validate_file(path: Path, seen: dict[str, Path]) -> tuple[list[str], dict[str, str]]:
    errors: list[str] = []
    match = FILENAME.fullmatch(path.name)
    if not match:
        errors.append("filename must match NNNN-short-title.md")
        file_number = None
    else:
        file_number = match.group("number")
        if file_number in seen:
            errors.append(f"duplicate ADR number; also used by {seen[file_number].name}")
        else:
            seen[file_number] = path

    text = path.read_text(encoding="utf-8")
    meta, body = parse_frontmatter(text)
    if not meta:
        errors.append("missing or malformed YAML frontmatter")
    for key in sorted(REQUIRED_KEYS - meta.keys()):
        errors.append(f"missing frontmatter key: {key}")

    meta_number = meta.get("number", "").zfill(4)
    if file_number and meta_number != file_number:
        errors.append(f"frontmatter number {meta.get('number')!r} differs from filename")
    if meta.get("status") and meta["status"] not in STATUSES:
        errors.append(f"unknown status: {meta['status']}")
    if meta.get("date") and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", meta["date"]):
        errors.append("date must use YYYY-MM-DD")

    h1 = H1.search(body)
    if not h1:
        errors.append("missing H1 '# ADR NNNN: Title'")
    else:
        if file_number and h1.group("number") != file_number:
            errors.append("H1 number differs from filename")
        if meta.get("title") and h1.group("title").strip('"\'') != meta["title"]:
            errors.append("H1 title differs from frontmatter title")

    headings = {m.group("title") for m in HEADING.finditer(body)}
    for heading in sorted(REQUIRED_HEADINGS - headings):
        errors.append(f"missing section: ## {heading}")

    for link in LINK.finditer(text):
        target = link.group("target").split("#", 1)[0]
        if "://" in target:
            continue
        resolved = (path.parent / target).resolve()
        if not resolved.exists():
            errors.append(f"broken Markdown link: {target}")

    status = meta.get("status")
    replacement = meta.get("superseded-by", "")
    empty_replacement = replacement in {"", "null", "~", "[]"}
    if status == "superseded" and empty_replacement:
        errors.append("superseded ADR must set superseded-by")
    if status != "superseded" and not empty_replacement:
        errors.append("only superseded ADR may set superseded-by")
    return errors, meta


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    adr_dir = root / "docs" / "adrs"
    if not adr_dir.is_dir():
        print(f"ERROR {adr_dir}: directory does not exist")
        return 2

    files = sorted(p for p in adr_dir.glob("*.md") if p.name != "README.md")
    seen: dict[str, Path] = {}
    failures = 0
    metadata: dict[Path, dict[str, str]] = {}
    for path in files:
        errors, meta = validate_file(path, seen)
        metadata[path] = meta
        for error in errors:
            failures += 1
            print(f"ERROR {path.relative_to(root)}: {error}")

    for path, meta in metadata.items():
        superseded_by = meta.get("superseded-by", "").strip().strip('"\'')
        if superseded_by not in {"", "null", "~", "[]"}:
            target = (path.parent / superseded_by).resolve()
            if target not in metadata:
                failures += 1
                print(f"ERROR {path.relative_to(root)}: superseded-by target does not exist: {superseded_by}")
            elif path.name not in parse_ref_list(metadata[target].get("supersedes", "")):
                failures += 1
                print(f"ERROR {path.relative_to(root)}: replacement lacks reciprocal supersedes entry")

        for old_ref in parse_ref_list(meta.get("supersedes", "")):
            old = (path.parent / old_ref).resolve()
            if old not in metadata:
                failures += 1
                print(f"ERROR {path.relative_to(root)}: supersedes target does not exist: {old_ref}")
                continue
            old_meta = metadata[old]
            old_backlink = old_meta.get("superseded-by", "").strip().strip('"\'')
            if old_meta.get("status") != "superseded" or old_backlink != path.name:
                failures += 1
                print(f"ERROR {path.relative_to(root)}: supersedes target lacks reciprocal superseded state/link: {old_ref}")
    if failures:
        print(f"FAIL {failures} issue(s) across {len(files)} ADR(s)")
        return 1
    print(f"OK {len(files)} ADR(s) validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
