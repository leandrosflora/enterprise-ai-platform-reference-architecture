#!/usr/bin/env python3
"""Translate canonical Markdown docs from Portuguese to English.

One-off migration helper for the bilingual documentation rollout. It preserves
code fences, inline code, URLs, HTML tags and architecture terms while translating
headings, paragraphs, lists and table cells.
"""

from __future__ import annotations

import re
from pathlib import Path

import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

DOCS_DIR = Path("docs")
MODEL_NAME = "manueldeprada/t5-small-pt-en"
BATCH_SIZE = 48
MAX_INPUT_LENGTH = 512
MAX_NEW_TOKENS = 384

TECH_TERMS = sorted(
    {
        "AI Platform", "Enterprise AI", "Agent Gateway", "Agent Runtime",
        "Agent Registry", "Knowledge Service", "Memory Service", "Model Gateway",
        "Evaluation Service", "Governance Service", "Audit Service", "Billing Service",
        "MCP Registry", "Identity Provider", "Control Plane", "Data Plane", "RAG",
        "MCP", "FinOps", "OpenAPI", "AsyncAPI", "OAuth2", "OIDC", "LGPD", "GDPR",
        "NIST AI RMF", "ISO/IEC 42001", "OWASP", "C4", "LLM", "LLMs", "API", "APIs",
        "SLO", "SLOs", "SLI", "SLIs", "CI/CD", "GitOps", "Kubernetes", "Kafka",
        "OpenTelemetry", "Prometheus", "Grafana", "Vector DB", "Vector Database",
        "Human in the Loop", "Human-in-the-Loop", "Prompt Injection", "Tool Calling",
        "Tool Call", "Foundation Model", "Foundation Models",
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
    r"responsável|produção|evidência|evidências|fluxo|processo|processos|"
    r"princípios|requisitos|decisão|decisões|riscos|controles|catálogo|"
    r"observabilidade|custos|memória|busca|autorização|autenticação"
    r")\b",
    re.IGNORECASE,
)
PLACEHOLDER_RE = re.compile(
    r"Z\s*X\s*Q\s*K\s*E\s*E\s*P\s*0*(\d+)\s*Q\s*X\s*Z",
    re.IGNORECASE,
)
PROTECTED_PATTERNS = (INLINE_CODE_RE, LINK_TARGET_RE, RAW_URL_RE, HTML_TAG_RE)


def needs_translation(text: str) -> bool:
    return bool(text.strip()) and bool(PORTUGUESE_HINT_RE.search(text))


def technical_term_pattern(term: str) -> re.Pattern[str]:
    return re.compile(rf"(?<![\w-]){re.escape(term)}(?![\w-])", re.IGNORECASE)


def protected_ranges(text: str) -> list[tuple[int, int]]:
    ranges: list[tuple[int, int]] = []
    for pattern in PROTECTED_PATTERNS:
        ranges.extend((m.start(), m.end()) for m in pattern.finditer(text))
    for term in TECH_TERMS:
        ranges.extend((m.start(), m.end()) for m in technical_term_pattern(term).finditer(text))

    if not ranges:
        return []

    merged: list[list[int]] = []
    for start, end in sorted(ranges):
        if not merged or start >= merged[-1][1]:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)
    return [(start, end) for start, end in merged]


def protect(text: str) -> tuple[str, dict[int, str]]:
    ranges = protected_ranges(text)
    if not ranges:
        return text, {}

    kept: dict[int, str] = {}
    pieces: list[str] = []
    cursor = 0
    for index, (start, end) in enumerate(ranges):
        pieces.append(text[cursor:start])
        kept[index] = text[start:end]
        pieces.append(f"ZXQKEEP{index:04d}QXZ")
        cursor = end
    pieces.append(text[cursor:])
    return "".join(pieces), kept


def restore(text: str, kept: dict[int, str]) -> str:
    if not kept:
        return text

    restored: set[int] = set()

    def replace(match: re.Match[str]) -> str:
        index = int(match.group(1))
        if index not in kept:
            return match.group(0)
        restored.add(index)
        return kept[index]

    text = PLACEHOLDER_RE.sub(replace, text)
    missing = sorted(set(kept) - restored)
    if missing:
        raise RuntimeError(f"Translation lost protected tokens {missing}")
    return text


def generate(batch: list[str], tokenizer, model) -> list[str]:
    encoded = tokenizer(
        batch,
        return_tensors="pt",
        padding=True,
        truncation=True,
        max_length=MAX_INPUT_LENGTH,
    )
    with torch.inference_mode():
        output_ids = model.generate(
            **encoded,
            max_new_tokens=MAX_NEW_TOKENS,
            num_beams=1,
            do_sample=False,
        )
    return tokenizer.batch_decode(output_ids, skip_special_tokens=True)


def translate_segmented(text: str, tokenizer, model) -> str:
    """Fallback that never exposes protected spans to the translation model."""

    ranges = protected_ranges(text)
    if not ranges:
        return generate([text], tokenizer, model)[0] if needs_translation(text) else text

    pieces: list[str] = []
    cursor = 0
    for start, end in ranges:
        plain = text[cursor:start]
        if needs_translation(plain):
            plain = generate([plain], tokenizer, model)[0]
        pieces.append(plain)
        pieces.append(text[start:end])
        cursor = end

    tail = text[cursor:]
    if needs_translation(tail):
        tail = generate([tail], tokenizer, model)[0]
    pieces.append(tail)
    return "".join(pieces)


def translate_texts(texts: list[str], tokenizer, model) -> list[str]:
    protected: list[str] = []
    maps: list[dict[int, str]] = []
    for text in texts:
        value, kept = protect(text)
        protected.append(value)
        maps.append(kept)

    outputs: list[str] = []
    for start in range(0, len(protected), BATCH_SIZE):
        outputs.extend(generate(protected[start : start + BATCH_SIZE], tokenizer, model))

    results: list[str] = []
    for original, output, kept in zip(texts, outputs, maps, strict=True):
        try:
            results.append(restore(output, kept))
        except RuntimeError:
            print(f"Falling back to segmented translation: {original[:120]!r}", flush=True)
            results.append(translate_segmented(original, tokenizer, model))
    return results


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
            slots: list[tuple[str, int | str]] = []
            for part in line.split("|"):
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
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
    model.eval()
    torch.set_num_threads(max(1, min(4, torch.get_num_threads())))

    sources = sorted(path for path in DOCS_DIR.rglob("*.md") if not path.name.endswith(".en.md"))
    print(f"Translating {len(sources)} Markdown pages with {MODEL_NAME}", flush=True)

    for number, source in enumerate(sources, start=1):
        target = source.with_name(f"{source.stem}.en.md")
        original = source.read_text(encoding="utf-8")
        trailing_newline = original.endswith("\n")
        units, plan = collect_units(original.splitlines())
        translations = translate_texts(units, tokenizer, model) if units else []
        output = "\n".join(render(plan, translations))
        if trailing_newline:
            output += "\n"
        target.write_text(output, encoding="utf-8")
        print(f"[{number:02d}/{len(sources)}] {target} ({len(units)} translated units)", flush=True)

    print(f"Translated {len(sources)} English pages", flush=True)


if __name__ == "__main__":
    main()
