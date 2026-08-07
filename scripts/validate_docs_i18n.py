#!/usr/bin/env python3
"""Validate one-to-one documentation coverage and reject untranslated EN pages."""

from __future__ import annotations

import re
import sys
from pathlib import Path


DOCS_DIR = Path("docs")
PORTUGUESE_MARKERS = re.compile(
    r"\b(?:"
    r"arquitetura|governan[çc]a|seguran[çc]a|servi[çc]os?|agentes?|modelos?|"
    r"dados|integra[çc][ãa]o|integra[çc][õo]es|fluxos?|processos?|objetivo|"
    r"respons[áa]vel|decis[ãa]o|decis[õo]es|produ[çc][ãa]o|evid[êe]ncias?|"
    r"este|esta|para|uma|com|n[ãa]o|deve|podem|quando|entre"
    r")\b",
    re.IGNORECASE,
)
FENCED_BLOCK = re.compile(r"```.*?```|~~~.*?~~~", re.DOTALL)
INLINE_CODE = re.compile(r"`[^`]*`")
LINK_TARGET = re.compile(r"\]\([^)]*\)")


def prose(markdown: str) -> str:
    """Remove technical regions that may legitimately contain PT identifiers."""

    markdown = FENCED_BLOCK.sub(" ", markdown)
    markdown = INLINE_CODE.sub(" ", markdown)
    return LINK_TARGET.sub("]", markdown)


def main() -> int:
    portuguese_pages = sorted(
        path for path in DOCS_DIR.rglob("*.md") if not path.name.endswith(".en.md")
    )
    english_pages = sorted(DOCS_DIR.rglob("*.en.md"))
    missing: list[Path] = []
    identical: list[Path] = []
    portuguese_heavy: list[tuple[Path, int]] = []

    for source in portuguese_pages:
        translation = source.with_name(f"{source.stem}.en.md")
        if not translation.exists():
            missing.append(translation)
            continue

        source_text = source.read_text(encoding="utf-8")
        translation_text = translation.read_text(encoding="utf-8")
        if source_text == translation_text:
            identical.append(translation)

        marker_count = len(PORTUGUESE_MARKERS.findall(prose(translation_text)))
        # A few Portuguese names may be referenced intentionally. A page with ten
        # or more prose markers is almost certainly untranslated or only partial.
        if marker_count >= 10:
            portuguese_heavy.append((translation, marker_count))

    print(f"Portuguese pages: {len(portuguese_pages)}")
    print(f"English pages: {len(english_pages)}")
    print(f"Missing English pages: {len(missing)}")
    print(f"Identical PT/EN pages: {len(identical)}")
    print(f"English pages with substantial Portuguese prose: {len(portuguese_heavy)}")

    for heading, entries in (
        ("Missing English variants", missing),
        ("Identical PT/EN files", identical),
    ):
        if entries:
            print(f"\n{heading}:")
            for path in entries:
                print(f"- {path}")

    if portuguese_heavy:
        print("\nEnglish files requiring editorial review:")
        for path, count in portuguese_heavy:
            print(f"- {path} ({count} Portuguese markers)")

    return 1 if missing or identical or portuguese_heavy else 0


if __name__ == "__main__":
    sys.exit(main())
