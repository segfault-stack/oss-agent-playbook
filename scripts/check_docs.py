#!/usr/bin/env python3
"""Validate repository Markdown without third-party dependencies."""

from __future__ import annotations

import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parent.parent
IGNORED_PARTS = {".git", ".agent"}
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
DECISION_NAME_RE = re.compile(r"^\d{4}-[a-z0-9]+(?:-[a-z0-9]+)*\.md$")
DECISION_STATUS_RE = re.compile(r"^- Status: (Proposed|Accepted|Superseded|Rejected)$", re.MULTILINE)
DECISION_DATE_RE = re.compile(r"^- Date: (\d{4}-\d{2}-\d{2})$", re.MULTILINE)
DECISION_SUPERSEDES_RE = re.compile(r"^- Supersedes: \S.+$", re.MULTILINE)
MEMORY_ID_RE = re.compile(r"^### (MM-\d{3})\s+—\s+", re.MULTILINE)


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


def check_repository_contract(files: list[Path]) -> list[str]:
    errors: list[str] = []
    required = [
        ROOT / "AGENTS.md",
        ROOT / "PROJECT_AGENT_CONTEXT.md",
        ROOT / "MAINTAINER_MEMORY.md",
        ROOT / "docs" / "decisions" / "README.md",
    ]
    for path in required:
        if not path.is_file():
            errors.append(f"{path.relative_to(ROOT)}: required repository document is missing")

    temporary = [path for path in files if path.name.endswith(".tmp.md")]
    for path in temporary:
        errors.append(f"{path.relative_to(ROOT)}: temporary Markdown must not remain in the repository")

    decision_dir = ROOT / "docs" / "decisions"
    decisions = sorted(decision_dir.glob("*.md")) if decision_dir.is_dir() else []
    decisions = [path for path in decisions if path.name != "README.md"]
    if not decisions:
        errors.append("docs/decisions: expected at least one numbered decision record")
    decision_numbers: list[str] = []
    for path in decisions:
        relative = path.relative_to(ROOT)
        if not DECISION_NAME_RE.fullmatch(path.name):
            errors.append(f"{relative}: expected NNNN-short-kebab-case-title.md")
        else:
            decision_numbers.append(path.name[:4])
        text = path.read_text(encoding="utf-8")
        if len(DECISION_STATUS_RE.findall(text)) != 1:
            errors.append(f"{relative}: expected exactly one valid Status metadata field")
        decision_dates = DECISION_DATE_RE.findall(text)
        if len(decision_dates) != 1:
            errors.append(f"{relative}: expected exactly one ISO Date metadata field")
        else:
            try:
                date.fromisoformat(decision_dates[0])
            except ValueError:
                errors.append(f"{relative}: invalid calendar date: {decision_dates[0]}")
        if len(DECISION_SUPERSEDES_RE.findall(text)) != 1:
            errors.append(f"{relative}: expected exactly one non-empty Supersedes metadata field")
    if len(decision_numbers) != len(set(decision_numbers)):
        errors.append("docs/decisions: duplicate four-digit decision number")

    memory_path = ROOT / "MAINTAINER_MEMORY.md"
    if memory_path.is_file():
        memory_ids = MEMORY_ID_RE.findall(memory_path.read_text(encoding="utf-8"))
        if not memory_ids:
            errors.append("MAINTAINER_MEMORY.md: expected at least one MM-NNN accepted lesson")
        if len(memory_ids) != len(set(memory_ids)):
            errors.append("MAINTAINER_MEMORY.md: duplicate accepted lesson ID")

    return errors


def main() -> int:
    files = markdown_files()
    errors = [error for path in files for error in check_file(path)]
    errors.extend(check_repository_contract(files))
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Documentation checks passed for {len(files)} Markdown files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
