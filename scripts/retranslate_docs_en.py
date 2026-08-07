#!/usr/bin/env python3
"""Regenerate English docs from canonical Portuguese with Markdown-safe translation.

This is a one-off editorial repair for the bilingual rollout. The translation model
only receives prose fragments. Markdown links, link destinations, inline code,
URLs, formatting delimiters, lists, tables and fenced code blocks are preserved by
construction instead of relying on model placeholders.
"""

from __future__ import annotations

import re
from pathlib import Path

import torch
from transformers import MarianMTModel, MarianTokenizer

DOCS_DIR = Path("docs")
MODEL_ID = "Helsinki-NLP/opus-mt-pt-en"

LINK_RE = re.compile(r"!?\[[^\]\n]+\]\([^)\n]+\)")
INLINE_CODE_RE = re.compile(r"`[^`\n]*`")
URL_RE = re.compile(r"https?://[^\s)>]+")
FORMAT_RE = re.compile(r"\*\*|__|~~")
ACCENTED_PT_RE = re.compile(r"[áàâãéêíóôõúçÁÀÂÃÉÊÍÓÔÕÚÇ]")
STRONG_PT_RE = re.compile(
    r"\b(?:"
    r"objetivo|contexto|decisão|decisões|arquitetura|governança|segurança|"
    r"serviço|serviços|agente|agentes|modelo|modelos|dados|integração|integrações|"
    r"fluxo|fluxos|processo|processos|responsável|produção|evidência|evidências|"
    r"etapa|perguntas|atividades|artefatos|saída|mínima|risco|riscos|obrigatório|"
    r"obrigatória|obrigatórios|obrigatórias|recomendado|recomendada|opcional|"
    r"próximo|próxima|capítulo|visão|geral|fontes|canônicas|autorização|"
    r"observabilidade|avaliação|consequências|alternativas|fronteiras|controles|"
    r"exemplos|condições|publicação|retirada|revisão|mudança|usuário|usuários|"
    r"negócio|qualidade|custo|custos|memória|conhecimento|ambiente|finalidade"
    r")\b",
    re.IGNORECASE,
)
COMMON_PT_RE = re.compile(
    r"\b(?:para|com|sem|quando|entre|sobre|deve|devem|pode|podem|não|uma|um|"
    r"dos|das|pela|pelo|pelos|pelas|será|serão|cada|como|mais|menos|apenas|"
    r"também|ainda|onde|qual|quem|porque|porquê|antes|depois|durante|até|"
    r"caso|casos|mesma|mesmo|existem|existe|definir|garantir|manter|usar|"
    r"usarão|permitir|validar|registrar|bloquear|considerar"
    r")\b",
    re.IGNORECASE,
)


def canonical_pages() -> list[Path]:
    return sorted(
        path for path in DOCS_DIR.rglob("*.md") if not path.name.endswith(".en.md")
    )


def english_variant(source: Path) -> Path:
    return source.with_name(f"{source.stem}.en.md")


def needs_translation(text: str) -> bool:
    stripped = text.strip()
    if not stripped:
        return False
    if ACCENTED_PT_RE.search(stripped) or STRONG_PT_RE.search(stripped):
        return True
    return len(COMMON_PT_RE.findall(stripped)) >= 2


def generate(texts: list[str], tokenizer, model) -> list[str]:
    if not texts:
        return []
    encoded = tokenizer(
        texts,
        return_tensors="pt",
        padding=True,
        truncation=True,
        max_length=512,
    )
    with torch.inference_mode():
        generated = model.generate(
            **encoded,
            max_length=512,
            num_beams=4,
            early_stopping=True,
        )
    return [tokenizer.decode(item, skip_special_tokens=True) for item in generated]


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
    if not candidates:
        return None
    return min(candidates, key=lambda item: item[0])


def translate_plain(text: str, tokenizer, model) -> str:
    if not needs_translation(text):
        return text
    return generate([text], tokenizer, model)[0]


def translate_inline(text: str, tokenizer, model) -> str:
    pieces: list[str] = []
    cursor = 0

    while cursor < len(text):
        token = next_token(text, cursor)
        if token is None:
            pieces.append(translate_plain(text[cursor:], tokenizer, model))
            break

        start, kind, match = token
        if start > cursor:
            pieces.append(translate_plain(text[cursor:start], tokenizer, model))

        raw = match.group(0)
        if kind == "link":
            image = "!" if raw.startswith("!") else ""
            open_bracket = raw.find("[")
            close_bracket = raw.rfind("](")
            label = raw[open_bracket + 1 : close_bracket]
            target = raw[close_bracket + 2 : -1]
            pieces.append(f"{image}[{translate_inline(label, tokenizer, model)}]({target})")
        else:
            pieces.append(raw)
        cursor = match.end()

    return "".join(pieces)


def translate_line(line: str, tokenizer, model) -> str:
    if not line.strip():
        return line

    # Markdown tables: keep cell boundaries immutable.
    if line.lstrip().startswith("|") and line.rstrip().endswith("|"):
        cells = line.split("|")
        translated = [translate_inline(cell, tokenizer, model) for cell in cells]
        return "|".join(translated)

    prefix_patterns = (
        r"^(#{1,6}\s+)(.*)$",
        r"^(\s*[-*+]\s+)(.*)$",
        r"^(\s*\d+\.\s+)(.*)$",
        r"^(\s*>\s?)(.*)$",
    )
    for pattern in prefix_patterns:
        match = re.match(pattern, line)
        if match:
            return f"{match.group(1)}{translate_inline(match.group(2), tokenizer, model)}"

    return translate_inline(line, tokenizer, model)


def translate_document(source_text: str, tokenizer, model) -> str:
    output: list[str] = []
    in_fence = False
    fence_marker = ""

    for line in source_text.splitlines():
        stripped = line.lstrip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            marker = stripped[:3]
            output.append(line)
            if not in_fence:
                in_fence = True
                fence_marker = marker
            elif marker == fence_marker:
                in_fence = False
                fence_marker = ""
            continue

        if in_fence:
            output.append(line)
        else:
            output.append(translate_line(line, tokenizer, model))

    result = "\n".join(output)
    if source_text.endswith("\n"):
        result += "\n"
    return result


def main() -> int:
    print(f"Loading {MODEL_ID}...")
    tokenizer = MarianTokenizer.from_pretrained(MODEL_ID)
    model = MarianMTModel.from_pretrained(MODEL_ID)
    model.eval()

    pages = canonical_pages()
    for index, source in enumerate(pages, start=1):
        translation = english_variant(source)
        translated = translate_document(source.read_text(encoding="utf-8"), tokenizer, model)
        translation.write_text(translated, encoding="utf-8")
        print(f"[{index:02d}/{len(pages)}] {translation}")

    print(f"Regenerated {len(pages)} English pages from canonical Portuguese sources.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
