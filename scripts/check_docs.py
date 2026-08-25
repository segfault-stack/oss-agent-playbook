#!/usr/bin/env python3
"""Validate repository Markdown without third-party dependencies."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parent.parent
IGNORED_PARTS = {".git", ".agent"}
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")


def markdown_files() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*.md")
        if not IGNORED_PARTS.intersection(path.relative_to(ROOT).parts)
    )


def anchor(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text).strip().lower()
    text = re.sub(r"[^\w\- ]", "", text, flags=re.UNICODE)
    return re.sub(r"[\s-]+", "-", text).strip("-")


def anchors(path: Path) -> set[str]:
    found: set[str] = set()
    counts: dict[str, int] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        match = HEADING_RE.match(line)
        if not match:
            continue
        base = anchor(match.group(2))
        number = counts.get(base, 0)
        counts[base] = number + 1
        found.add(base if number == 0 else f"{base}-{number}")
    return found


def check_file(path: Path) -> list[str]:
    relative = path.relative_to(ROOT)
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    errors: list[str] = []

    if sum(line.startswith("# ") for line in lines) != 1:
        errors.append(f"{relative}: expected exactly one H1")
    if sum(line.startswith("```") for line in lines) % 2:
        errors.append(f"{relative}: unbalanced fenced code blocks")
    for number, line in enumerate(lines, 1):
        if line.rstrip() != line:
            errors.append(f"{relative}:{number}: trailing whitespace")

    for raw_link in LINK_RE.findall(text):
        link = raw_link.strip().split(maxsplit=1)[0].strip("<>")
        if not link or re.match(r"^(?:https?://|mailto:)", link):
            continue
        target_text, separator, fragment = link.partition("#")
        target = path if not target_text else (path.parent / unquote(target_text)).resolve()
        try:
            target.relative_to(ROOT)
        except ValueError:
            errors.append(f"{relative}: local link escapes repository: {raw_link}")
            continue
        if not target.exists():
            errors.append(f"{relative}: missing local link target: {raw_link}")
            continue
        if separator and target.is_file() and target.suffix.lower() == ".md":
            if unquote(fragment).lower() not in anchors(target):
                errors.append(f"{relative}: missing Markdown anchor: {raw_link}")
    return errors


def main() -> int:
    files = markdown_files()
    errors = [error for path in files for error in check_file(path)]
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Documentation checks passed for {len(files)} Markdown files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
