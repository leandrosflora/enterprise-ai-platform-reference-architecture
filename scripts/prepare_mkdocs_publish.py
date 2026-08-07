#!/usr/bin/env python3
"""Prepare the MkDocs configuration used by CI publishing.

English is the canonical/default MkDocs language and is always published at the
site root. Portuguese remains enabled as the secondary localized site.
The source mkdocs.yml is never mutated; CI writes mkdocs.publish.yml.
"""

from __future__ import annotations

from pathlib import Path

SOURCE = Path("mkdocs.yml")
TARGET = Path("mkdocs.publish.yml")


def main() -> int:
    config = SOURCE.read_text(encoding="utf-8")

    required_fragments = (
        "theme:\n  name: material\n  language: en\n",
        "- locale: en\n          name: English\n          default: true\n          build: true\n",
        "- locale: pt\n          name: Português (Brasil)\n          build: true\n",
    )
    missing = [fragment for fragment in required_fragments if fragment not in config]
    if missing:
        raise SystemExit(
            "mkdocs.yml is not configured with English as the default bilingual publish shape"
        )

    TARGET.write_text(config, encoding="utf-8")
    print(f"Prepared {TARGET} with English as the default language and Portuguese enabled")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
