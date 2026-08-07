#!/usr/bin/env python3
"""Repair and validate Markdown structure in English documentation variants.

Portuguese pages remain the canonical structural source. The English variants may
translate prose and link labels, but they must preserve link destinations and
line-oriented Markdown structure closely enough for documentation validators and
MkDocs strict builds to remain deterministic.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

DOCS_DIR = Path("docs")
MARKDOWN_LINK_RE = re.compile(r"(?P<image>!?)\[(?P<label>[^\]\n]+)\]\((?P<target>[^)\n]+)\)")


def english_variant(source: Path) -> Path:
    return source.with_name(f"{source.stem}.en.md")


def canonical_pages() -> list[Path]:
    return sorted(
        path for path in DOCS_DIR.rglob("*.md") if not path.name.endswith(".en.md")
    )


def link_targets(line: str) -> list[str]:
    return [match.group("target") for match in MARKDOWN_LINK_RE.finditer(line)]


def find_target_position(text: str, target: str, cursor: int) -> int:
    """Find the destination occurrence, not a same-valued label occurrence."""

    positions: list[int] = []
    start = cursor
    while True:
        position = text.find(target, start)
        if position < 0:
            break
        positions.append(position)
        start = position + len(target)

    for position in positions:
        if text.rfind("]", cursor, position) >= cursor:
            return position

    return positions[-1] if positions else -1


def fallback_list_link(
    source_line: str,
    english_line: str,
    target: str,
    target_pos: int,
) -> str | None:
    """Rebuild a malformed bullet link when the model destroyed square brackets."""

    if not source_line.lstrip().startswith("- [") or not english_line.lstrip().startswith("- "):
        return None

    indent = english_line[: len(english_line) - len(english_line.lstrip())]
    bullet_prefix = f"{indent}- "
    raw_label = english_line[len(bullet_prefix) : target_pos].strip()
    label = raw_label.strip(" []()\t")
    if not label:
        return None

    suffix = english_line[target_pos + len(target) :]
    if suffix.startswith((")", "]")):
        suffix = suffix[1:]

    return f"{bullet_prefix}[{label}]({target}){suffix}"


def repair_link_line(source_line: str, english_line: str) -> tuple[str, list[str]]:
    """Restore canonical link targets while keeping translated English labels/prose."""

    source_links = list(MARKDOWN_LINK_RE.finditer(source_line))
    if not source_links:
        return english_line, []

    repaired = english_line
    cursor = 0
    errors: list[str] = []

    for index, source_link in enumerate(source_links, start=1):
        target = source_link.group("target")
        target_pos = find_target_position(repaired, target, cursor)
        if target_pos < 0:
            errors.append(f"link {index}: canonical target not found in EN: {target}")
            continue

        label_end = repaired.rfind("]", cursor, target_pos)
        if label_end < 0:
            fallback = fallback_list_link(source_line, repaired, target, target_pos)
            if fallback is None:
                errors.append(f"link {index}: translated link label has no closing ] for {target}")
                continue
            repaired = fallback
            cursor = repaired.find(target) + len(target) + 1
            continue

        label_start = repaired.rfind("[", cursor, label_end)
        if label_start < 0:
            fallback = fallback_list_link(source_line, repaired, target, target_pos)
            if fallback is None:
                errors.append(f"link {index}: translated link label has no opening [ for {target}")
                continue
            repaired = fallback
            cursor = repaired.find(target) + len(target) + 1
            continue

        # Replace whatever the translation model placed between the label and the
        # canonical target (missing/duplicated parentheses, spaces, etc.) with a
        # valid Markdown destination. Preserve translated label and surrounding prose.
        suffix = repaired[target_pos + len(target) :]
        if suffix.startswith((")", "]")):
            suffix = suffix[1:]

        prefix = repaired[: label_end + 1]
        repaired = f"{prefix}({target}){suffix}"
        cursor = len(prefix) + len(target) + 2

    return repaired, errors


def repair_pair(source: Path, translation: Path, write: bool) -> tuple[int, list[str]]:
    source_text = source.read_text(encoding="utf-8")
    translation_text = translation.read_text(encoding="utf-8")
    source_lines = source_text.splitlines()
    translation_lines = translation_text.splitlines()

    errors: list[str] = []
    if len(source_lines) != len(translation_lines):
        return 0, [
            f"line count differs: PT={len(source_lines)} EN={len(translation_lines)}"
        ]

    changed = 0
    output: list[str] = []

    for line_number, (source_line, english_line) in enumerate(
        zip(source_lines, translation_lines), start=1
    ):
        repaired_line, line_errors = repair_link_line(source_line, english_line)
        for error in line_errors:
            errors.append(f"line {line_number}: {error}")

        expected_targets = link_targets(source_line)
        actual_targets = link_targets(repaired_line)
        if expected_targets != actual_targets:
            errors.append(
                f"line {line_number}: link targets differ: PT={expected_targets!r} EN={actual_targets!r}"
            )

        if repaired_line != english_line:
            changed += 1
        output.append(repaired_line)

    if write and not errors and changed:
        final = "\n".join(output)
        if translation_text.endswith("\n"):
            final += "\n"
        translation.write_text(final, encoding="utf-8")

    return changed, errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--write",
        action="store_true",
        help="repair English Markdown files in place; default is check-only",
    )
    args = parser.parse_args()

    pages = canonical_pages()
    missing: list[Path] = []
    failures: list[str] = []
    changed_files = 0
    changed_lines = 0

    for source in pages:
        translation = english_variant(source)
        if not translation.exists():
            missing.append(translation)
            continue

        changed, errors = repair_pair(source, translation, args.write)
        if changed:
            changed_files += 1
            changed_lines += changed
        for error in errors:
            failures.append(f"{translation}: {error}")

    print(f"Canonical pages checked: {len(pages)}")
    print(f"Missing English pages: {len(missing)}")
    print(f"English files needing structural repair: {changed_files}")
    print(f"Markdown link lines needing repair: {changed_lines}")

    if missing:
        print("\nMissing English pages:")
        for path in missing:
            print(f"- {path}")

    if failures:
        print("\nUnresolved structural errors:")
        for failure in failures:
            print(f"- {failure}")

    if missing or failures:
        return 1

    if not args.write and changed_lines:
        print("\nRun with --write to apply the deterministic repairs above.")
        return 1

    print("English Markdown structure is consistent with canonical link targets.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
