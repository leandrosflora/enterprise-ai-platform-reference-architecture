#!/usr/bin/env python3
"""Clean residual Portuguese in English docs without exposing Markdown to the model.

The current English pages are preserved line-by-line unless editorial validation
finds residual Portuguese or a known translation defect. Reworked lines are rebuilt
from the canonical Portuguese source while links, code, URLs and Markdown syntax
remain outside model control.
"""

from __future__ import annotations

import re
from pathlib import Path

import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

import validate_docs_i18n as i18n

DOCS_DIR = Path("docs")
MODEL_ID = "unicamp-dl/translation-pt-en-t5"
TASK_PREFIX = "translate Portuguese to English: "
BATCH_SIZE = 12

LINK_RE = re.compile(r"!?\[[^\]\n]+\]\([^)\n]+\)")
INLINE_CODE_RE = re.compile(r"`[^`\n]*`")
URL_RE = re.compile(r"https?://[^\s)>]+")
FORMAT_RE = re.compile(r"\*\*|__|~~")

SUSPICIOUS_EN = re.compile(
    r"\b(?:AGR|PPA|staff|Impotence|impotence|execuble|premises)\b|"
    r"\bThis paste\b|\bCanon sources\b",
    re.IGNORECASE,
)

EXACT_TRANSLATIONS = {
    "Comece pelo book": "Start with the book",
    "Entrada do livro": "Book entry",
    "Por que uma AI Platform?": "Why an AI Platform?",
    "Estrutura": "Structure",
    "Relação entre book e artefatos": "Relationship between the book and artifacts",
    "Fontes canônicas": "Canonical sources",
    "Assunto": "Subject",
    "Fonte": "Source",
    "Arquitetura": "Architecture",
    "Capacidades e serviços de referência": "Reference capabilities and services",
    "Operação de referência": "Reference operations",
    "Gerar o book": "Generate the book",
    "Validação": "Validation",
    "Objetivo": "Objective",
    "Contexto": "Context",
    "Decisão": "Decision",
    "Decisões": "Decisions",
    "Alternativas": "Alternatives",
    "Consequências": "Consequences",
    "Evidências mínimas": "Minimum evidence",
    "Fronteiras obrigatórias": "Mandatory boundaries",
    "Por que": "Rationale",
    "Estados canônicos": "Canonical states",
    "Estado": "State",
    "Significado": "Meaning",
    "Etapa 1 — Idea": "Stage 1 — Idea",
    "Etapa 2 — Assessment": "Stage 2 — Assessment",
    "Etapa 3 — Design": "Stage 3 — Design",
    "Etapa 4 — Build": "Stage 4 — Build",
    "Etapa 5 — Evaluate": "Stage 5 — Evaluate",
    "Etapa 6 — Govern": "Stage 6 — Govern",
    "Etapa 7 — Publish": "Stage 7 — Publish",
    "Etapa 8 — Operate": "Stage 8 — Operate",
    "Etapa 9 — Review e Retire": "Stage 9 — Review and Retire",
    "Perguntas": "Questions",
    "Atividades": "Activities",
    "Artefatos": "Artifacts",
    "Saída mínima": "Minimum output",
    "Decisões obrigatórias": "Mandatory decisions",
    "Controles por padrão": "Default controls",
    "Evidências geradas automaticamente": "Automatically generated evidence",
    "Dimensão": "Dimension",
    "Exemplos de métricas": "Example metrics",
    "Próximo capítulo": "Next chapter",
}

WORD_FIXES = (
    (re.compile(r"\bAGR\b"), "RAG"),
    (re.compile(r"\bPPA\b"), "API"),
    (re.compile(r"\bIA\b"), "AI"),
    (re.compile(r"\bexecuble\b", re.IGNORECASE), "executable"),
    (re.compile(r"\bCanon sources\b", re.IGNORECASE), "Canonical sources"),
    (re.compile(r"\bThis paste\b", re.IGNORECASE), "This folder"),
)


def canonical_pages() -> list[Path]:
    return sorted(
        path for path in DOCS_DIR.rglob("*.md") if not path.name.endswith(".en.md")
    )


def english_variant(source: Path) -> Path:
    return source.with_name(f"{source.stem}.en.md")


def next_token(text: str, start: int):
    candidates = []
    for kind, regex in (
        ("link", LINK_RE),
        ("code", INLINE_CODE_RE),
        ("url", URL_RE),
        ("format", FORMAT_RE),
    ):
        match = regex.search(text, start)
        if match:
            candidates.append((match.start(), kind, match))
    return min(candidates, key=lambda item: item[0]) if candidates else None


def parse_link(raw: str) -> tuple[str, str, str]:
    image = "!" if raw.startswith("!") else ""
    open_bracket = raw.find("[")
    close_bracket = raw.rfind("](")
    return image, raw[open_bracket + 1 : close_bracket], raw[close_bracket + 2 : -1]


def exact_translation(text: str) -> str | None:
    return EXACT_TRANSLATIONS.get(text.strip())


def collect_plain(text: str, segments: set[str]) -> None:
    core = text.strip()
    if not core or exact_translation(core) is not None:
        return
    segments.add(core)


def collect_inline(text: str, segments: set[str]) -> None:
    cursor = 0
    while cursor < len(text):
        token = next_token(text, cursor)
        if token is None:
            collect_plain(text[cursor:], segments)
            return
        start, kind, match = token
        if start > cursor:
            collect_plain(text[cursor:start], segments)
        if kind == "link":
            _, label, _ = parse_link(match.group(0))
            collect_inline(label, segments)
        cursor = match.end()


def body_and_prefix(line: str) -> tuple[str, str]:
    for pattern in (
        r"^(#{1,6}\s+)(.*)$",
        r"^(\s*[-*+]\s+)(.*)$",
        r"^(\s*\d+\.\s+)(.*)$",
        r"^(\s*>\s?)(.*)$",
    ):
        match = re.match(pattern, line)
        if match:
            return match.group(1), match.group(2)
    return "", line


def collect_line(line: str, segments: set[str]) -> None:
    if line.lstrip().startswith("|") and line.rstrip().endswith("|"):
        for cell in line.split("|"):
            collect_inline(cell, segments)
        return
    _, body = body_and_prefix(line)
    collect_inline(body, segments)


def line_needs_rework(source_line: str, english_line: str) -> bool:
    strong, common, accented = i18n.marker_counts(english_line)
    if strong > 0 or common > 0 or accented > 0 or SUSPICIOUS_EN.search(english_line):
        return True

    # Catch short mixed expressions that page-level language markers intentionally
    # ignore (for example "SLO e fallback").
    for connector in (" e ", " de ", " do ", " da ", " no ", " na "):
        if connector in source_line.lower() and connector in english_line.lower():
            return True

    source_lower = source_line.lower()
    english_lower = english_line.lower()
    expectations = (
        ("agente", "agent"),
        ("rag", "rag"),
        ("api", "api"),
        ("ia", "ai"),
        ("artefato", "artifact"),
        ("idempot", "idempot"),
        ("depend", "depend"),
    )
    return any(source in source_lower and expected not in english_lower for source, expected in expectations)


def generate_batches(segments: set[str], tokenizer, model) -> dict[str, str]:
    ordered = sorted(segments, key=len)
    translations: dict[str, str] = {}
    for start in range(0, len(ordered), BATCH_SIZE):
        batch = ordered[start : start + BATCH_SIZE]
        encoded = tokenizer(
            [f"{TASK_PREFIX}{text}" for text in batch],
            return_tensors="pt",
            padding=True,
            truncation=True,
            max_length=512,
        )
        with torch.inference_mode():
            generated = model.generate(
                **encoded,
                max_length=512,
                num_beams=2,
                early_stopping=True,
            )
        outputs = [tokenizer.decode(item, skip_special_tokens=True) for item in generated]
        translations.update(zip(batch, outputs))
        print(f"Translated cleanup fragments: {min(start + BATCH_SIZE, len(ordered))}/{len(ordered)}")
    return translations


def post_correct(source: str, output: str) -> str:
    result = output
    for pattern, replacement in WORD_FIXES:
        result = pattern.sub(replacement, result)

    src = source.lower()
    if "agentes" in src:
        result = re.sub(r"\bstaff members?\b|\bstaff\b", "agents", result, flags=re.IGNORECASE)
    elif "agente" in src:
        result = re.sub(r"\bstaff member\b|\bstaff\b", "agent", result, flags=re.IGNORECASE)

    if "artefatos" in src:
        result = re.sub(r"\barticles\b", "artifacts", result, flags=re.IGNORECASE)
    elif "artefato" in src:
        result = re.sub(r"\barticle\b", "artifact", result, flags=re.IGNORECASE)

    if "idempot" in src:
        result = re.sub(r"\bimpotence\b", "idempotency", result, flags=re.IGNORECASE)
    if "depend" in src:
        result = re.sub(r"\bpremises\b", "dependencies", result, flags=re.IGNORECASE)
    if "pasta" in src:
        result = re.sub(r"\bpaste\b", "folder", result, flags=re.IGNORECASE)

    if " e " in src:
        result = re.sub(r"\s+e\s+", " and ", result)
    return result


def translate_plain(text: str, translations: dict[str, str]) -> str:
    if not text:
        return text
    left = len(text) - len(text.lstrip())
    right = len(text) - len(text.rstrip())
    prefix = text[:left]
    suffix = text[len(text) - right :] if right else ""
    core = text.strip()
    value = exact_translation(core) or translations.get(core, core)
    return f"{prefix}{post_correct(core, value)}{suffix}"


def translate_inline(text: str, translations: dict[str, str]) -> str:
    pieces: list[str] = []
    cursor = 0
    while cursor < len(text):
        token = next_token(text, cursor)
        if token is None:
            pieces.append(translate_plain(text[cursor:], translations))
            break
        start, kind, match = token
        if start > cursor:
            pieces.append(translate_plain(text[cursor:start], translations))
        raw = match.group(0)
        if kind == "link":
            image, label, target = parse_link(raw)
            pieces.append(f"{image}[{translate_inline(label, translations)}]({target})")
        else:
            pieces.append(raw)
        cursor = match.end()
    return "".join(pieces)


def translate_line(line: str, translations: dict[str, str]) -> str:
    if line.lstrip().startswith("|") and line.rstrip().endswith("|"):
        return "|".join(translate_inline(cell, translations) for cell in line.split("|"))
    prefix, body = body_and_prefix(line)
    return f"{prefix}{translate_inline(body, translations)}"


def main() -> int:
    pages = canonical_pages()
    plans: dict[Path, tuple[list[str], list[str], list[bool]]] = {}
    segments: set[str] = set()
    total_lines = 0

    for source in pages:
        translation = english_variant(source)
        source_text = source.read_text(encoding="utf-8")
        english_text = translation.read_text(encoding="utf-8")
        source_lines = source_text.splitlines()
        english_lines = english_text.splitlines()
        if len(source_lines) != len(english_lines):
            raise SystemExit(
                f"Line count differs before cleanup: {translation}: "
                f"PT={len(source_lines)} EN={len(english_lines)}"
            )

        flags: list[bool] = []
        in_fence = False
        fence_marker = ""
        for source_line, english_line in zip(source_lines, english_lines, strict=True):
            stripped = source_line.lstrip()
            if stripped.startswith("```") or stripped.startswith("~~~"):
                marker = stripped[:3]
                flags.append(False)
                if not in_fence:
                    in_fence = True
                    fence_marker = marker
                elif marker == fence_marker:
                    in_fence = False
                    fence_marker = ""
                continue
            rework = False if in_fence else line_needs_rework(source_line, english_line)
            flags.append(rework)
            if rework:
                total_lines += 1
                collect_line(source_line, segments)

        plans[source] = (source_lines, english_lines, flags)

    print(f"Canonical pages: {len(pages)}")
    print(f"Lines selected for editorial cleanup: {total_lines}")
    print(f"Unique prose fragments to translate: {len(segments)}")

    tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
    model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_ID)
    model.eval()
    translations = generate_batches(segments, tokenizer, model) if segments else {}

    changed_pages = 0
    for source, (source_lines, english_lines, flags) in plans.items():
        output: list[str] = []
        changed = False
        for source_line, english_line, rework in zip(
            source_lines, english_lines, flags, strict=True
        ):
            candidate = translate_line(source_line, translations) if rework else english_line
            if candidate != english_line:
                changed = True
            output.append(candidate)

        if changed:
            target = english_variant(source)
            original = target.read_text(encoding="utf-8")
            final = "\n".join(output)
            if original.endswith("\n"):
                final += "\n"
            target.write_text(final, encoding="utf-8")
            changed_pages += 1
            print(f"Cleaned {target}")

    print(f"Editorial cleanup changed {changed_pages} English pages.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
