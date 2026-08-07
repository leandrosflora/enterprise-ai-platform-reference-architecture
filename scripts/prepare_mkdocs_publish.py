#!/usr/bin/env python3
"""Prepare the MkDocs configuration used by CI publishing.

English publishing is controlled by the PUBLISH_ENGLISH_DOCS environment variable.
The source mkdocs.yml is never mutated; CI writes a temporary mkdocs.publish.yml.
"""

from __future__ import annotations

import os
from pathlib import Path

SOURCE = Path("mkdocs.yml")
TARGET = Path("mkdocs.publish.yml")

ENABLED_BLOCK = """        - locale: en
          name: English
          build: true
"""
DISABLED_BLOCK = """        - locale: en
          name: English
          build: false
"""


def env_enabled(name: str) -> bool:
    return os.getenv(name, "false").strip().lower() in {"1", "true", "yes", "on"}


def main() -> int:
    publish_english = env_enabled("PUBLISH_ENGLISH_DOCS")
    config = SOURCE.read_text(encoding="utf-8")

    if publish_english:
        if DISABLED_BLOCK in config:
            config = config.replace(DISABLED_BLOCK, ENABLED_BLOCK, 1)
        elif ENABLED_BLOCK not in config:
            raise SystemExit("Could not locate the English i18n language block in mkdocs.yml")
    else:
        if ENABLED_BLOCK in config:
            config = config.replace(ENABLED_BLOCK, DISABLED_BLOCK, 1)
        elif DISABLED_BLOCK not in config:
            raise SystemExit("Could not locate the English i18n language block in mkdocs.yml")

    TARGET.write_text(config, encoding="utf-8")
    state = "enabled" if publish_english else "disabled"
    print(f"Prepared {TARGET} with English publishing {state}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
