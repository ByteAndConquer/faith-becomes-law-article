#!/usr/bin/env python3
"""Validate article assembly and bibliography integrity before a release build."""
from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAIN = ROOT / "main.md"
ABSTRACT = ROOT / "abstract.md"
SECTIONS = ROOT / "sections"
BIB = ROOT / "references.bib"


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)


def main() -> int:
    errors: list[str] = []
    for path in (MAIN, ABSTRACT, SECTIONS, BIB):
        if not path.exists():
            errors.append(f"Required path is missing: {path.relative_to(ROOT)}")
    if errors:
        for message in errors:
            fail(message)
        return 1

    article = MAIN.read_text(encoding="utf-8")
    abstract_file = ABSTRACT.read_text(encoding="utf-8").strip()
    abstract_body = re.sub(r"^# Abstract\s*", "", abstract_file, count=1).strip()
    abstract_match = re.search(
        r"^## Abstract\s*\n(.*?)\n## Table of Contents",
        article,
        flags=re.MULTILINE | re.DOTALL,
    )
    if not abstract_match or abstract_match.group(1).strip() != abstract_body:
        errors.append("abstract.md does not match the Abstract embedded in main.md")

    section_files = sorted(SECTIONS.glob("[0-9][0-9]-*.md"))
    if not section_files:
        errors.append("No numbered section files were found")
    for section_file in section_files:
        section_text = section_file.read_text(encoding="utf-8").strip()
        heading_match = re.match(r"^# (.+)$", section_text, flags=re.MULTILINE)
        if not heading_match:
            errors.append(f"{section_file.relative_to(ROOT)} has no level-one heading")
            continue
        heading = heading_match.group(1)
        embedded = re.search(
            rf"^# {re.escape(heading)}\s*\n.*?(?=^# |\Z)",
            article,
            flags=re.MULTILINE | re.DOTALL,
        )
        if not embedded or embedded.group(0).strip() != section_text:
            errors.append(
                f"{section_file.relative_to(ROOT)} does not exactly match its section in main.md"
            )

    citation_keys = set(re.findall(r"@([A-Za-z0-9_:\-.]+)", article))
    bib_text = BIB.read_text(encoding="utf-8")
    bib_keys = re.findall(r"@\w+\s*\{\s*([^,\s]+)", bib_text)
    duplicate_keys = sorted(key for key, count in Counter(bib_keys).items() if count > 1)
    missing_keys = sorted(citation_keys - set(bib_keys))
    uncited_keys = sorted(set(bib_keys) - citation_keys)

    if duplicate_keys:
        errors.append("Duplicate bibliography keys: " + ", ".join(duplicate_keys))
    if missing_keys:
        errors.append("Missing bibliography entries: " + ", ".join(missing_keys))
    if uncited_keys:
        errors.append("Uncited bibliography entries: " + ", ".join(uncited_keys))

    if errors:
        for message in errors:
            fail(message)
        return 1

    print(f"Validated {len(section_files)} sections.")
    print(f"Validated {len(citation_keys)} citation keys and {len(bib_keys)} bibliography entries.")
    print("Article sources are synchronized and release-ready.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
