#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import subprocess
from datetime import UTC, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOOK_DIR = ROOT / "docs" / "book"
OUTPUT_DIR = ROOT / "build" / "book"
OUTPUT_PATH = OUTPUT_DIR / "enterprise-ai-platform-book.md"

CHAPTERS = [
    "index.md",
    "01-why-ai-platform.md",
    "02-capability-map.md",
    "03-operating-model.md",
    "04-agent-lifecycle.md",
    "05-case-study-document-agent.md",
    "06-decision-guides.md",
    "07-adoption-roadmap.md",
    "08-production-checklists.md",
    "glossary.md",
]

LOCAL_MARKDOWN_LINK = re.compile(r"\[([^\]]+)\]\((?!https?://|mailto:|#)([^)]+\.md(?:#[^)]+)?)\)")


def git_revision() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"],
            cwd=ROOT,
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
    except (OSError, subprocess.CalledProcessError):
        return "unknown"


def validate() -> list[str]:
    errors: list[str] = []
    for chapter in CHAPTERS:
        path = BOOK_DIR / chapter
        if not path.exists():
            errors.append(f"Missing book chapter: {path.relative_to(ROOT)}")
            continue
        text = path.read_text(encoding="utf-8")
        if not text.startswith("# "):
            errors.append(f"Chapter must start with H1: {path.relative_to(ROOT)}")
        if len(text.split()) < 80:
            errors.append(f"Chapter is unexpectedly short: {path.relative_to(ROOT)}")
    return errors


def web_link(source: Path, label: str, raw_target: str) -> str:
    target, separator, fragment = raw_target.partition("#")
    resolved = (source.parent / target).resolve()
    try:
        relative = resolved.relative_to(ROOT / "docs")
    except ValueError:
        try:
            relative = resolved.relative_to(ROOT)
            url = f"https://github.com/leandrosflora/enterprise-ai-platform-demo-arch/blob/main/{relative.as_posix()}"
        except ValueError:
            return f"[{label}]({raw_target})"
    else:
        clean = relative.with_suffix("").as_posix()
        url = f"https://leandrosflora.github.io/enterprise-ai-platform-demo-arch/{clean}/"
    if separator and fragment:
        url = f"{url}#{fragment}"
    return f"[{label}]({url})"


def normalize_links(source: Path, text: str) -> str:
    return LOCAL_MARKDOWN_LINK.sub(
        lambda match: web_link(source, match.group(1), match.group(2)),
        text,
    )


def build() -> None:
    generated_at = datetime.now(UTC).strftime("%Y-%m-%d")
    revision = git_revision()
    parts = [
        "---",
        'title: "Enterprise AI Platform Book"',
        'subtitle: "Estratégia, arquitetura, governança e operação"',
        'author: "Leandro Silva Flora"',
        'lang: "pt-BR"',
        f'date: "{generated_at}"',
        "toc: true",
        "toc-depth: 3",
        "numbersections: true",
        "---",
        "",
        '<div class="title-page">',
        "",
        "# Enterprise AI Platform Book",
        "",
        "Estratégia, arquitetura, governança e operação",
        "",
        f"Revisão `{revision}` - {generated_at}",
        "",
        "Arquitetura de referência acompanhada por contratos, políticas e vertical slice executável.",
        "",
        "</div>",
        "",
    ]

    for index, chapter in enumerate(CHAPTERS):
        path = BOOK_DIR / chapter
        text = normalize_links(path, path.read_text(encoding="utf-8").strip())
        parts.append(text)
        if index < len(CHAPTERS) - 1:
            parts.extend(["", '<div class="page-break"></div>', ""])

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text("\n".join(parts).rstrip() + "\n", encoding="utf-8")
    print(f"Book manuscript generated: {OUTPUT_PATH.relative_to(ROOT)}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate or build the consolidated AI Platform book")
    parser.add_argument("--check", action="store_true", help="Validate the chapter manifest without writing output")
    args = parser.parse_args()

    errors = validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    if args.check:
        print(f"Book manifest validation passed ({len(CHAPTERS)} chapters)")
        return 0

    build()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
