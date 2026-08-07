#!/usr/bin/env python3
"""Translate Portuguese Markdown documentation to English while preserving technical markup.

This is a one-off migration helper used by CI to replace the placeholder `.en.md`
files with real English content. Code fences, inline code, URLs, HTML tags, and
selected architecture terms are protected from translation.
"""

from __future__ import annotations

import re
from pathlib import Path

import torch
from transformers import MarianMTModel, MarianTokenizer

DOCS_DIR = Path("docs")
MODEL_NAME = "Helsinki-NLP/opus-mt-pt-en"
BATCH_SIZE = 16
MAX_LENGTH = 512

TECH_TERMS = sorted(
    {
        "AI Platform",
        "Enterprise AI",
        "Agent Gateway",
        "Agent Runtime",
        "Agent Registry",
        "Knowledge Service",
        "Memory Service",
        "Model Gateway",
        "Evaluation Service",
        "Governance Service",
        "Audit Service",
        "Billing Service",
        "MCP Registry",
        "Identity Provider",
        "Control Plane",
        "Data Plane",
        "RAG",
        "MCP",
        "FinOps",
        "OpenAPI",
        "AsyncAPI",
        "OAuth2",
        "OIDC",
        "LGPD",
        "GDPR",
        "NIST AI RMF",
        "ISO/IEC 42001",
        "OWASP",
        "C4",
        "LLM",
        "LLMs",
        "API",
        "APIs",
        "SLO",
        "SLOs",
        "SLI",
        "SLIs",
        "CI/CD",
        "GitOps",
        "Kubernetes",
        "Kafka",
        "OpenTelemetry",
        "Prometheus",
        "Grafana",
        "Vector DB",
        "Vector Database",
        "Human in the Loop",
        "Human-in-the-Loop",
        "Prompt Injection",
        "Tool Calling",
        "Tool Call",
        "Foundation Model",
        "Foundation Models",
    },
    key=len,
    reverse=True,
)

INLINE_CODE_RE = re.compile(r"`[^`\n]+`")
RAW_URL_RE = re.compile(r"https?://[^\s)>]+")
LINK_TARGET_RE = re.compile(r"(?<=\]\()[^)]+(?=\))")
HTML_TAG_RE = re.compile(r"</?[^>]+>")
FENCE_RE = re.compile(r"^\s*(```|~~~)")
TABLE_SEPARATOR_RE = re.compile(r"^\s*\|?(?:\s*:?-{3,}:?\s*\|)+\s*:?-{3,}:?\s*\|?\s*$")
MARKDOWN_PREFIX_RE = re.compile(
    r"^(?P<prefix>\s*(?:(?:#{1,6})\s+|>\s+|(?:[-*+]\s+)|(?:\d+\.\s+)|(?:[-*+]\s+\[[ xX]\]\s+))?)(?P<body>.*)$"
)
PORTUGUESE_HINT_RE = re.compile(
    r"[áàâãéêíóôõúçÁÀÂÃÉÊÍÓÔÕÚÇ]|\b(?:"
    r"o|a|os|as|um|uma|uns|umas|de|do|da|dos|das|em|no|na|nos|nas|"
    r"para|por|com|sem|que|como|quando|onde|não|deve|devem|pode|podem|"
    r"objetivo|arquitetura|governança|segurança|serviço|serviços|agente|agentes|"
    r"dados|modelo|modelos|integração|integrações|avaliação|aprovação|"
    r"responsável|produção|evidência|evidências|fluxo|processo|processos"
    r")\b",
    re.IGNORECASE,
)


def needs_translation(text: str) -> bool:
    return bool(text.strip()) and bool(PORTUGUESE_HINT_RE.search(text))


def protect(text: str) -> tuple[str, dict[str, str]]:
    kept: dict[str, str] = {}

    def store(value: str) -> str:
        token = f"__KEEP_{len(kept):04d}__"
        kept[token] = value
        return token

    for pattern in (INLINE_CODE_RE, LINK_TARGET_RE, RAW_URL_RE, HTML_TAG_RE):
        text = pattern.sub(lambda m: store(m.group(0)), text)

    for term in TECH_TERMS:
        text = re.sub(
            rf"(?<![\w-]){re.escape(term)}(?![\w-])",
            lambda m: store(m.group(0)),
            text,
            flags=re.IGNORECASE,
        )

    return text, kept


def restore(text: str, kept: dict[str, str]) -> str:
    normalized = text
    for token, value in kept.items():
        candidates = {
            token,
            token.replace("_", " _"),
            token.replace("_", "_ "),
            token.replace("_", " "),
        }
        restored = False
        for candidate in sorted(candidates, key=len, reverse=True):
            if candidate in normalized:
                normalized = normalized.replace(candidate, value)
                restored = True
                break
        if not restored:
            raise RuntimeError(f"Translation lost protected token {token}: {text!r}")
    return normalized


def translate_texts(texts: list[str], tokenizer: MarianTokenizer, model: MarianMTModel) -> list[str]:
    protected: list[str] = []
    maps: list[dict[str, str]] = []
    for text in texts:
        p, kept = protect(text)
        protected.append(p)
        maps.append(kept)

    outputs: list[str] = []
    for start in range(0, len(protected), BATCH_SIZE):
        batch = protected[start : start + BATCH_SIZE]
        encoded = tokenizer(
            batch,
            return_tensors="pt",
            padding=True,
            truncation=True,
            max_length=MAX_LENGTH,
        )
        with torch.inference_mode():
            generated = model.generate(
                **encoded,
                max_new_tokens=MAX_LENGTH,
                num_beams=4,
                early_stopping=True,
            )
        outputs.extend(tokenizer.batch_decode(generated, skip_special_tokens=True))

    return [restore(output, kept) for output, kept in zip(outputs, maps, strict=True)]


def collect_units(lines: list[str]) -> tuple[list[str], list[tuple[str, object]]]:
    units: list[str] = []
    plan: list[tuple[str, object]] = []
    in_fence = False

    for line in lines:
        if FENCE_RE.match(line):
            in_fence = not in_fence
            plan.append(("raw", line))
            continue
        if in_fence or not line.strip() or TABLE_SEPARATOR_RE.match(line):
            plan.append(("raw", line))
            continue

        if "|" in line and line.strip().startswith("|"):
            parts = line.split("|")
            slots: list[tuple[str, int | str]] = []
            for part in parts:
                stripped = part.strip()
                if stripped and needs_translation(stripped):
                    idx = len(units)
                    units.append(stripped)
                    slots.append(("unit", idx))
                else:
                    slots.append(("raw", part))
            plan.append(("table", slots))
            continue

        match = MARKDOWN_PREFIX_RE.match(line)
        assert match is not None
        prefix = match.group("prefix")
        body = match.group("body")
        if needs_translation(body):
            idx = len(units)
            units.append(body)
            plan.append(("line", (prefix, idx)))
        else:
            plan.append(("raw", line))

    return units, plan


def render(plan: list[tuple[str, object]], translated: list[str]) -> list[str]:
    rendered: list[str] = []
    for kind, payload in plan:
        if kind == "raw":
            rendered.append(str(payload))
        elif kind == "line":
            prefix, idx = payload  # type: ignore[misc]
            rendered.append(f"{prefix}{translated[idx]}")
        elif kind == "table":
            cells: list[str] = []
            for cell_kind, value in payload:  # type: ignore[union-attr]
                if cell_kind == "unit":
                    cells.append(f" {translated[int(value)]} ")
                else:
                    cells.append(str(value))
            rendered.append("|".join(cells))
        else:
            raise ValueError(kind)
    return rendered


def main() -> None:
    tokenizer = MarianTokenizer.from_pretrained(MODEL_NAME)
    model = MarianMTModel.from_pretrained(MODEL_NAME)
    model.eval()

    sources = sorted(path for path in DOCS_DIR.rglob("*.md") if not path.name.endswith(".en.md"))
    print(f"Translating {len(sources)} Markdown pages")

    translated_count = 0
    for source in sources:
        target = source.with_name(f"{source.stem}.en.md")
        original = source.read_text(encoding="utf-8")
        had_trailing_newline = original.endswith("\n")
        lines = original.splitlines()
        units, plan = collect_units(lines)
        translations = translate_texts(units, tokenizer, model) if units else []
        output = "\n".join(render(plan, translations))
        if had_trailing_newline:
            output += "\n"
        target.write_text(output, encoding="utf-8")
        translated_count += 1
        print(f"[{translated_count:02d}/{len(sources)}] {target}")

    print(f"Translated {translated_count} English pages")


if __name__ == "__main__":
    main()
