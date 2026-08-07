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
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

DOCS_DIR = Path("docs")
MODEL_ID = "unicamp-dl/translation-pt-en-t5"
TASK_PREFIX = "translate Portuguese to English: "
BATCH_SIZE = 12

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
    r"próximo|próxima|capítulo|visão|geral|fontes|fonte|canônicas|canônica|"
    r"autorização|observabilidade|avaliação|consequências|alternativas|fronteiras|"
    r"controles|exemplos|condições|publicação|retirada|revisão|mudança|usuário|"
    r"usuários|negócio|qualidade|custo|custos|memória|conhecimento|ambiente|"
    r"finalidade|documentação|repositório|estrutura|relação|assunto|eventos|"
    r"operações|operação|implementação|estado|estados|significado|capacidade|"
    r"capacidades|requisitos|ameaças|identidade|política|políticas|aprovação|"
    r"execução|resultado|resultados|ferramentas|ferramenta|sistemas|sistema"
    r")\b",
    re.IGNORECASE,
)
COMMON_PT_RE = re.compile(
    r"\b(?:para|com|sem|quando|entre|sobre|deve|devem|pode|podem|não|uma|um|"
    r"dos|das|pela|pelo|pelos|pelas|será|serão|cada|como|mais|menos|apenas|"
    r"também|ainda|onde|qual|quem|porque|porquê|antes|depois|durante|até|"
    r"caso|casos|mesma|mesmo|existem|existe|definir|garantir|manter|usar|"
    r"permitir|validar|registrar|bloquear|considerar|aplicar|aplicável|"
    r"possui|possuem|precisa|precisam|continua|continuam|torna|torna-se|"
    r"representa|representam|inclui|incluem|utiliza|utilizam|segue|seguem"
    r")\b",
    re.IGNORECASE,
)


def canonical_pages() -> list[Path]:
    return sorted(
        path for path in DOCS_DIR.rglob("*.md") if not path.name.endswith(".en.md")
    )


def english_variant(source: Path) -> Path:
    return source.with_name(f"{source.stem}.en.md")


def core_text(text: str) -> str:
    return text.strip()


def needs_translation(text: str) -> bool:
    stripped = core_text(text)
    if not stripped:
        return False
    if ACCENTED_PT_RE.search(stripped) or STRONG_PT_RE.search(stripped):
        return True
    return len(COMMON_PT_RE.findall(stripped)) >= 2


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


def parse_link(raw: str) -> tuple[str, str, str]:
    image = "!" if raw.startswith("!") else ""
    open_bracket = raw.find("[")
    close_bracket = raw.rfind("](")
    label = raw[open_bracket + 1 : close_bracket]
    target = raw[close_bracket + 2 : -1]
    return image, label, target


def collect_plain(text: str, segments: set[str]) -> None:
    core = core_text(text)
    if core and needs_translation(core):
        segments.add(core)


def collect_inline(text: str, segments: set[str]) -> None:
    cursor = 0
    while cursor < len(text):
        token = next_token(text, cursor)
        if token is None:
            collect_plain(text[cursor:], segments)
            break

        start, kind, match = token
        if start > cursor:
            collect_plain(text[cursor:start], segments)

        if kind == "link":
            _, label, _ = parse_link(match.group(0))
            collect_inline(label, segments)
        cursor = match.end()


def collect_line(line: str, segments: set[str]) -> None:
    if not line.strip():
        return

    if line.lstrip().startswith("|") and line.rstrip().endswith("|"):
        for cell in line.split("|"):
            collect_inline(cell, segments)
        return

    prefix_patterns = (
        r"^(#{1,6}\s+)(.*)$",
        r"^(\s*[-*+]\s+)(.*)$",
        r"^(\s*\d+\.\s+)(.*)$",
        r"^(\s*>\s?)(.*)$",
    )
    for pattern in prefix_patterns:
        match = re.match(pattern, line)
        if match:
            collect_inline(match.group(2), segments)
            return

    collect_inline(line, segments)


def collect_document(source_text: str, segments: set[str]) -> None:
    in_fence = False
    fence_marker = ""

    for line in source_text.splitlines():
        stripped = line.lstrip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            marker = stripped[:3]
            if not in_fence:
                in_fence = True
                fence_marker = marker
            elif marker == fence_marker:
                in_fence = False
                fence_marker = ""
            continue
        if not in_fence:
            collect_line(line, segments)


def generate_batches(segments: set[str], tokenizer, model) -> dict[str, str]:
    ordered = sorted(segments, key=len)
    translations: dict[str, str] = {}

    for start in range(0, len(ordered), BATCH_SIZE):
        batch = ordered[start : start + BATCH_SIZE]
        prompts = [f"{TASK_PREFIX}{text}" for text in batch]
        encoded = tokenizer(
            prompts,
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
        print(f"Translated prose fragments: {min(start + BATCH_SIZE, len(ordered))}/{len(ordered)}")

    return translations


def translate_plain(text: str, translations: dict[str, str]) -> str:
    if not text:
        return text
    left = len(text) - len(text.lstrip())
    right = len(text) - len(text.rstrip())
    prefix = text[:left]
    suffix = text[len(text) - right :] if right else ""
    core = text.strip()
    return f"{prefix}{translations.get(core, core)}{suffix}"


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
    if not line.strip():
        return line

    if line.lstrip().startswith("|") and line.rstrip().endswith("|"):
        cells = line.split("|")
        return "|".join(translate_inline(cell, translations) for cell in cells)

    prefix_patterns = (
        r"^(#{1,6}\s+)(.*)$",
        r"^(\s*[-*+]\s+)(.*)$",
        r"^(\s*\d+\.\s+)(.*)$",
        r"^(\s*>\s?)(.*)$",
    )
    for pattern in prefix_patterns:
        match = re.match(pattern, line)
        if match:
            return f"{match.group(1)}{translate_inline(match.group(2), translations)}"

    return translate_inline(line, translations)


def translate_document(source_text: str, translations: dict[str, str]) -> str:
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
            output.append(translate_line(line, translations))

    result = "\n".join(output)
    if source_text.endswith("\n"):
        result += "\n"
    return result


def main() -> int:
    pages = canonical_pages()
    sources = {page: page.read_text(encoding="utf-8") for page in pages}
    segments: set[str] = set()
    for source_text in sources.values():
        collect_document(source_text, segments)

    print(f"Canonical pages: {len(pages)}")
    print(f"Unique Portuguese prose fragments to translate: {len(segments)}")
    print(f"Loading {MODEL_ID}...")

    tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
    model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_ID)
    model.eval()

    translations = generate_batches(segments, tokenizer, model)

    for index, source in enumerate(pages, start=1):
        translation = english_variant(source)
        translated = translate_document(sources[source], translations)
        translation.write_text(translated, encoding="utf-8")
        print(f"[{index:02d}/{len(pages)}] {translation}")

    print(f"Regenerated {len(pages)} English pages from canonical Portuguese sources.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
