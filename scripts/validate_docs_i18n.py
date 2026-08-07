#!/usr/bin/env python3
"""Validate one-to-one documentation coverage and reject untranslated EN prose."""

from __future__ import annotations

import re
import sys
from pathlib import Path


DOCS_DIR = Path("docs")

# Strong markers are domain/editorial words that should not remain in published
# English prose. One occurrence is enough to require review.
STRONG_PORTUGUESE_MARKERS = re.compile(
    r"\b(?:"
    r"arquitetura|governan[çc]a|seguran[çc]a|servi[çc]os?|agentes?|modelos?|"
    r"dados|integra[çc][ãa]o|integra[çc][õo]es|fluxos?|processos?|objetivo|"
    r"respons[áa]vel|decis[ãa]o|decis[õo]es|produ[çc][ãa]o|evid[êe]ncias?|"
    r"etapa|perguntas|atividades|artefatos?|identificar|efeitos?|colaterais|"
    r"definir|rota|registro|inicial|limites|contratos?|versionados?|usados?|testes?|"
    r"comece|entrada|livro|fontes?|can[oô]nicas?|gerar|assunto|padr[aã]o|"
    r"obrigat[oó]ri[oa]s?|opcionais?|opcional|anual|semestral|trimestral|"
    r"simplificado|detalhado|riscos?|custos?|mem[oó]ria|conhecimento|"
    r"autoriza[çc][ãa]o|autentica[çc][ãa]o|avalia[çc][ãa]o|aprova[çc][ãa]o|"
    r"publica[çc][ãa]o|retirada|revis[aã]o|mudan[çc]a|usu[aá]rios?|neg[oó]cio|"
    r"qualidade|ambiente|finalidade|documenta[çc][ãa]o|reposit[oó]rio|estrutura|"
    r"rela[çc][ãa]o|opera[çc][ãa]o|opera[çc][õo]es|implementa[çc][ãa]o|"
    r"estados?|significado|capacidades?|requisitos?|amea[çc]as?|identidade|"
    r"pol[ií]ticas?|resultados?|ferramentas?|sistemas?|depend[eê]ncias?|"
    r"idempot[eê]ncia"
    r")\b",
    re.IGNORECASE,
)

# Common words can occasionally occur in names or mixed technical expressions,
# so require several of them on the same page before rejecting the translation.
COMMON_PORTUGUESE_MARKERS = re.compile(
    r"\b(?:"
    r"este|esta|estes|estas|para|uma|umas|com|sem|n[ãa]o|deve|devem|podem|"
    r"quando|entre|sobre|pela|pelo|pelos|pelas|ser[aá]|ser[aã]o|cada|tamb[eé]m|"
    r"ainda|onde|antes|depois|durante|casos?|mesm[oa]s?|existem|existe"
    r")\b",
    re.IGNORECASE,
)

FENCED_BLOCK = re.compile(r"```.*?```|~~~.*?~~~", re.DOTALL)
INLINE_CODE = re.compile(r"`[^`]*`")
LINK_TARGET = re.compile(r"\]\([^)]*\)")
ACCENTED_PT = re.compile(r"[áàâãéêíóôõúçÁÀÂÃÉÊÍÓÔÕÚÇ]")


def prose(markdown: str) -> str:
    """Remove technical regions that may legitimately contain PT identifiers."""

    markdown = FENCED_BLOCK.sub(" ", markdown)
    markdown = INLINE_CODE.sub(" ", markdown)
    return LINK_TARGET.sub("]", markdown)


def marker_counts(markdown: str) -> tuple[int, int, int]:
    value = prose(markdown)
    return (
        len(STRONG_PORTUGUESE_MARKERS.findall(value)),
        len(COMMON_PORTUGUESE_MARKERS.findall(value)),
        len(ACCENTED_PT.findall(value)),
    )


def source_has_portuguese(markdown: str) -> bool:
    strong, common, accented = marker_counts(markdown)
    return strong > 0 or common >= 3 or accented > 0


def main() -> int:
    portuguese_pages = sorted(
        path for path in DOCS_DIR.rglob("*.md") if not path.name.endswith(".en.md")
    )
    english_pages = sorted(DOCS_DIR.rglob("*.en.md"))
    missing: list[Path] = []
    identical_untranslated: list[Path] = []
    editorial_review: list[tuple[Path, int, int, int]] = []

    for source in portuguese_pages:
        translation = source.with_name(f"{source.stem}.en.md")
        if not translation.exists():
            missing.append(translation)
            continue

        source_text = source.read_text(encoding="utf-8")
        translation_text = translation.read_text(encoding="utf-8")

        # Canonical pages already authored in English may legitimately have an
        # identical localized variant. Reject identity only for Portuguese source.
        if source_text == translation_text and source_has_portuguese(source_text):
            identical_untranslated.append(translation)

        strong, common, accented = marker_counts(translation_text)
        if strong > 0 or common >= 5 or accented >= 2:
            editorial_review.append((translation, strong, common, accented))

    print(f"Canonical pages: {len(portuguese_pages)}")
    print(f"English pages: {len(english_pages)}")
    print(f"Missing English pages: {len(missing)}")
    print(f"Identical untranslated PT/EN pages: {len(identical_untranslated)}")
    print(f"English pages requiring editorial review: {len(editorial_review)}")

    for heading, entries in (
        ("Missing English variants", missing),
        ("Identical untranslated PT/EN files", identical_untranslated),
    ):
        if entries:
            print(f"\n{heading}:")
            for path in entries:
                print(f"- {path}")

    if editorial_review:
        print("\nEnglish files requiring editorial review:")
        for path, strong, common, accented in editorial_review:
            print(
                f"- {path} (strong={strong}, common={common}, accented={accented})"
            )

    return 1 if missing or identical_untranslated or editorial_review else 0


if __name__ == "__main__":
    sys.exit(main())
