#!/usr/bin/env python3
"""Run the one-off English documentation translation with Markdown-safe fallback.

The base translator protects link targets during normal batch translation. When a
model loses a placeholder, its segmented fallback must not expose partial
Markdown syntax such as ``](`` to the model. This wrapper translates link labels
and surrounding prose separately while preserving link destinations byte-for-byte.
"""

from __future__ import annotations

import re

from scripts import translate_docs_en as translator


MARKDOWN_LINK_RE = re.compile(
    r"(?P<image>!?)\[(?P<label>[^\]\n]+)\]\((?P<target>[^)\n]+)\)"
)


def translate_plain(text: str, tokenizer, model, target_lang_id: int) -> str:
    """Translate prose without exposing protected technical spans to the model."""

    ranges = translator.protected_ranges(text)
    if not ranges:
        if translator.needs_translation(text):
            return translator.generate([text], tokenizer, model, target_lang_id)[0]
        return text

    pieces: list[str] = []
    cursor = 0
    for start, end in ranges:
        plain = text[cursor:start]
        if translator.needs_translation(plain):
            plain = translator.generate([plain], tokenizer, model, target_lang_id)[0]
        pieces.append(plain)
        pieces.append(text[start:end])
        cursor = end

    tail = text[cursor:]
    if translator.needs_translation(tail):
        tail = translator.generate([tail], tokenizer, model, target_lang_id)[0]
    pieces.append(tail)
    return "".join(pieces)


def translate_segmented_safe(text: str, tokenizer, model, target_lang_id: int) -> str:
    """Translate Markdown text while preserving complete link syntax and targets."""

    matches = list(MARKDOWN_LINK_RE.finditer(text))
    if not matches:
        return translate_plain(text, tokenizer, model, target_lang_id)

    pieces: list[str] = []
    cursor = 0
    for match in matches:
        pieces.append(translate_plain(text[cursor : match.start()], tokenizer, model, target_lang_id))

        label = translate_plain(match.group("label"), tokenizer, model, target_lang_id)
        pieces.append(
            f"{match.group('image')}[{label}]({match.group('target')})"
        )
        cursor = match.end()

    pieces.append(translate_plain(text[cursor:], tokenizer, model, target_lang_id))
    return "".join(pieces)


# Replace only the fallback path. The normal batch path and all other behavior
# remain in the canonical one-off translator.
translator.translate_segmented = translate_segmented_safe


if __name__ == "__main__":
    translator.main()
