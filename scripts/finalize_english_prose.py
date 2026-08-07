#!/usr/bin/env python3
"""Normalize residual Portuguese in published English prose.

This one-off migration helper only edits prose outside fenced code blocks. Inline
code, URLs and Markdown link destinations are protected byte-for-byte. The goal is
to remove mixed PT/EN phrases left by machine translation without touching
contracts, commands or technical identifiers.
"""

from __future__ import annotations

import re
from pathlib import Path

DOCS_DIR = Path("docs")

PROTECTED_RE = re.compile(r"`[^`\n]*`|https?://[^\s)>]+|(?<=\]\()[^)\n]+(?=\))")
ACCENTED_PT_RE = re.compile(r"[áàâãéêíóôõúçÁÀÂÃÉÊÍÓÔÕÚÇ]")

PHRASES = (
    (r"\bO \*\*book\*\*", "The **book**"),
    (r"\bA \*\*reference architecture\*\*", "The **reference architecture**"),
    (r"\bA \*\*technical sample\*\*", "The **technical sample**"),
    (r"\bControl plan and date plan\b", "Control plane and data plane"),
    (r"\bOnboarding of agent\b", "Agent onboarding"),
    (r"\bTroubleshooting of invocation\b", "Invocation troubleshooting"),
    (r"\bUsing Pandoc\b", "using Pandoc"),
    (r"\bStage 6 — Government\b", "Stage 6 — Governance"),
    (r"\bThis paste\b", "This folder"),
    (r"\bCanon sources\b", "Canonical sources"),
    (r"\bO workflow\b", "The workflow"),
    (r"\bO Model Gateway\b", "The Model Gateway"),
    (r"## Por que\b", "## Rationale"),
    (r"\bDecision Support Agent com grounding\b", "Decision Support Agent with grounding"),
    (r"\bsupport a GitHub OIDC\b", "support for GitHub OIDC"),
    (r"\bbackend compartilhado\b", "shared backend"),
    (r"\bJornadas implementadas\b", "Implemented journeys"),
    (r"\bcanal interno apenas\b", "internal channel only"),
    (r"\brisk assessment inicial\b", "initial risk assessment"),
    (r"\brollback testado\b", "tested rollback"),
    (r"\bramp-up progressivo\b", "progressive ramp-up"),
    (r"\bOperar significa observar simultaneamente\b", "Operations require simultaneous observation of"),
    (r"\bincidente relevante\b", "significant incident"),
    (r"\bHallucination risk máximo\b", "Maximum hallucination risk"),
    (r"\bRevisão Security\b", "Security review"),
    (r"\bAudit recording crítico\b", "Critical audit recording"),
    (r"\bmarketplace interno\b", "internal marketplace"),
    (r"\batendimento interno\b", "internal support"),
    (r"\bportal interno\b", "internal portal"),
    (r"\b1,5 segundo\b", "1.5 seconds"),
    (r"\bdates used in the tests\b", "datasets used in the tests"),
    (r"\bO \[case study of document agent\]\(05-case-study-document-agent\.md\) it applies\b", "The [document agent case study](05-case-study-document-agent.md) applies"),
)

TECHNICAL_FIXES = (
    (r"\bAGR\b", "RAG"),
    (r"\bPPA\b", "API"),
    (r"\bdatesets\b", "datasets"),
    (r"\bdateset\b", "dataset"),
    (r"\bpublicated\b", "published"),
    (r"\bpublicate\b", "publish"),
    (r"\bcompost\b", "compose"),
    (r"\bcross-rest\b", "cross-repo"),
    (r"\btip-to-end\b", "end-to-end"),
    (r"\bexplanability\b", "explainability"),
)

WORDS = {
    "responsabilidade": "responsibility", "responsabilidades": "responsibilities",
    "aceito": "accepted", "indicador": "indicator", "indicadores": "indicators",
    "ponta": "end", "componentes": "components", "componente": "component",
    "entregas": "deliverables", "controle": "control", "pendente": "pending",
    "pendentes": "pending", "envolvidos": "involved", "envolvido": "involved",
    "envolvida": "involved", "envolvidas": "involved", "papel": "role",
    "papéis": "roles", "tipo": "type", "tipos": "types", "operacional": "operational",
    "operacionais": "operational", "escalabilidade": "scalability", "evento": "event",
    "eventos": "events", "escopo": "scope", "alternativa": "alternative",
    "alternativas": "alternatives", "vantagem": "advantage", "vantagens": "advantages",
    "privacidade": "privacy", "fraco": "weak", "exemplo": "example", "exemplos": "examples",
    "interno": "internal", "interna": "internal", "internos": "internal", "internas": "internal",
    "documentos": "documents", "documento": "document", "registrar": "record",
    "aplicar": "apply", "validar": "validate", "bloquear": "block", "reduzir": "reduce",
    "aprovar": "approve", "somente": "only", "suporte": "support", "reais": "actual",
    "completo": "complete", "completa": "complete", "completos": "complete", "completas": "complete",
    "manifesto": "manifest", "implementado": "implemented", "implementada": "implemented",
    "implementados": "implemented", "implementadas": "implemented", "configurados": "configured",
    "configuradas": "configured", "configurado": "configured", "configurada": "configured",
    "configurar": "configure", "promovido": "promoted", "promovida": "promoted",
    "promover": "promote", "aprovado": "approved", "aprovada": "approved",
    "aprovados": "approved", "aprovadas": "approved", "jornada": "journey", "jornadas": "journeys",
    "compartilhado": "shared", "compartilhada": "shared", "canal": "channel",
    "alçada": "approval authority", "máximo": "maximum", "crítico": "critical",
    "revisão": "review", "segundo": "second", "segundos": "seconds", "precisa": "needs",
    "precisam": "need", "possui": "has", "utiliza": "uses", "incidente": "incident",
    "relevante": "significant", "testado": "tested", "testada": "tested",
    "progressivo": "progressive", "progressiva": "progressive", "operar": "operate",
    "significa": "means", "observar": "observe", "simultaneamente": "simultaneously",
    "inicial": "initial", "apenas": "only", "rotear": "route", "atendimento": "support",
    "consumo": "consumption", "limite": "limit", "limites": "limits", "executar": "execute",
    "respeita": "respects", "versão": "version", "finalidade": "purpose", "ameaça": "threat",
    "ameaças": "threats", "exposição": "exposure", "dados": "data", "decisão": "decision",
    "decisões": "decisions", "condições": "conditions", "fonte": "source", "fontes": "sources",
    "memória": "memory", "conhecimento": "knowledge", "segurança": "security",
    "governança": "governance", "arquitetura": "architecture", "serviço": "service",
    "serviços": "services", "agente": "agent", "agentes": "agents", "processo": "process",
    "processos": "processes", "fluxo": "flow", "fluxos": "flows", "objetivo": "objective",
    "objetivos": "objectives", "evidência": "evidence", "evidências": "evidence",
    "etapa": "stage", "etapas": "stages", "perguntas": "questions", "atividades": "activities",
    "artefato": "artifact", "artefatos": "artifacts", "identificar": "identify",
    "efeito": "effect", "efeitos": "effects", "colateral": "side effect", "colaterais": "side effects",
    "definir": "define", "rota": "route", "registro": "record", "contrato": "contract",
    "contratos": "contracts", "versionado": "versioned", "versionados": "versioned",
    "usado": "used", "usados": "used", "usada": "used", "usadas": "used", "teste": "test",
    "testes": "tests", "comece": "start", "entrada": "entry", "livro": "book",
    "canônica": "canonical", "canônicas": "canonical", "gerar": "generate", "assunto": "subject",
    "padrão": "standard", "obrigatório": "mandatory", "obrigatórios": "mandatory",
    "obrigatória": "mandatory", "obrigatórias": "mandatory", "opcional": "optional",
    "opcionais": "optional", "semestral": "semiannual", "trimestral": "quarterly",
    "simplificado": "simplified", "simplificada": "simplified", "detalhado": "detailed",
    "detalhada": "detailed", "risco": "risk", "riscos": "risks", "custo": "cost",
    "custos": "costs", "autorização": "authorization", "avaliação": "evaluation",
    "aprovação": "approval", "publicação": "publication", "retirada": "retirement",
    "mudança": "change", "usuário": "user", "usuários": "users", "negócio": "business",
    "qualidade": "quality", "ambiente": "environment", "documentação": "documentation",
    "repositório": "repository", "estrutura": "structure", "relação": "relationship",
    "operação": "operation", "operações": "operations", "implementação": "implementation",
    "estado": "state", "estados": "states", "significado": "meaning", "capacidade": "capability",
    "capacidades": "capabilities", "requisito": "requirement", "requisitos": "requirements",
    "identidade": "identity", "política": "policy", "políticas": "policies", "resultado": "result",
    "resultados": "results", "ferramenta": "tool", "ferramentas": "tools", "sistema": "system",
    "sistemas": "systems", "dependência": "dependency", "dependências": "dependencies",
    "idempotência": "idempotency", "auditoria": "audit", "catálogo": "catalog",
    "produção": "production", "regra": "rule", "regras": "rules", "resposta": "response",
    "respostas": "responses", "disponibilidade": "availability", "isolamento": "isolation",
    "metadados": "metadata", "versionamento": "versioning", "conforme": "according to",
    "qual": "which", "quais": "which", "falha": "failure", "falhas": "failures",
}

COMMON = {
    "do": "of the", "da": "of the", "dos": "of the", "das": "of the", "em": "in",
    "e": "and", "ou": "or", "por": "by", "para": "for", "com": "with", "sem": "without",
    "não": "not", "nao": "not", "que": "that", "ao": "to the", "aos": "to the",
    "na": "in the", "nas": "in the", "nos": "in the", "um": "a", "uma": "a",
    "o": "the", "os": "the", "de": "of", "pode": "can", "podem": "can",
    "deve": "must", "devem": "must", "como": "as", "mais": "more", "menos": "less",
    "também": "also", "ainda": "still", "quando": "when", "onde": "where",
    "antes": "before", "depois": "after", "durante": "during", "cada": "each",
    "entre": "between", "sobre": "about", "pela": "by the", "pelo": "by the",
    "pelos": "by the", "pelas": "by the", "este": "this", "esta": "this",
    "estes": "these", "estas": "these",
}

TARGET_RE = re.compile(
    r"\b(?:" + "|".join(sorted((re.escape(key) for key in WORDS), key=len, reverse=True)) + r")\b",
    re.IGNORECASE,
)


def protect(text: str) -> tuple[str, list[str]]:
    values: list[str] = []

    def replace(match: re.Match[str]) -> str:
        values.append(match.group(0))
        return f"@@PROTECTED{len(values)-1:04d}@@"

    return PROTECTED_RE.sub(replace, text), values


def restore(text: str, values: list[str]) -> str:
    for index, value in enumerate(values):
        text = text.replace(f"@@PROTECTED{index:04d}@@", value)
    return text


def normalize_line(line: str) -> str:
    protected, values = protect(line)

    for pattern, replacement in PHRASES:
        protected = re.sub(pattern, replacement, protected, flags=re.IGNORECASE)
    for pattern, replacement in TECHNICAL_FIXES:
        protected = re.sub(pattern, replacement, protected, flags=re.IGNORECASE)

    if TARGET_RE.search(protected) or ACCENTED_PT_RE.search(protected):
        for source, target in sorted(WORDS.items(), key=lambda item: len(item[0]), reverse=True):
            protected = re.sub(rf"\b{re.escape(source)}\b", target, protected, flags=re.IGNORECASE)
        for source, target in COMMON.items():
            protected = re.sub(rf"\b{re.escape(source)}\b", target, protected, flags=re.IGNORECASE)

    return restore(protected, values)


def normalize_file(path: Path) -> int:
    original = path.read_text(encoding="utf-8")
    lines = original.splitlines()
    output: list[str] = []
    in_fence = False
    fence_marker = ""
    changed = 0

    for line in lines:
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

        candidate = line if in_fence else normalize_line(line)
        if candidate != line:
            changed += 1
        output.append(candidate)

    if changed:
        final = "\n".join(output)
        if original.endswith("\n"):
            final += "\n"
        path.write_text(final, encoding="utf-8")
    return changed


def main() -> int:
    files = sorted(DOCS_DIR.rglob("*.en.md"))
    changed_files = 0
    changed_lines = 0
    for path in files:
        changed = normalize_file(path)
        if changed:
            changed_files += 1
            changed_lines += changed
            print(f"Normalized {path}: {changed} line(s)")

    print(f"English pages checked: {len(files)}")
    print(f"English pages normalized: {changed_files}")
    print(f"Prose lines normalized: {changed_lines}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
