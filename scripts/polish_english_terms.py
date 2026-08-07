#!/usr/bin/env python3
"""Apply deterministic editorial corrections to key English documentation terms."""

from __future__ import annotations

from pathlib import Path

DOCS = Path("docs")

REPLACEMENTS = {
    # README and navigation terminology
    "The content is a documental and architectural reference, it does not deliver": "The content is a documentation and architecture reference. It does not deliver",
    "Case study of a documentary agent": "Document agent case study",
    "| Subject matter | Source |": "| Subject | Source |",
    "| APIs HTTP |": "| HTTP APIs |",
    "each capacity to be implemented": "each capability to be implemented",
    "[Onboarding MCP]": "[MCP onboarding]",
    "book/                     Narrativa, operating model, casos, decisões e checklists": "book/                     Narrative, operating model, cases, decisions and checklists",
    "architecture/             Princípios, NFRs, C4 e separação de planos": "architecture/             Principles, NFRs, C4 and plane separation",
    "contracts/                OpenAPI, AsyncAPI, MCP, eventos e data stores": "contracts/                OpenAPI, AsyncAPI, MCP, events and data stores",
    "domains/                  Domínios funcionais da plataforma": "domains/                  Platform functional domains",
    "services/                 Capacidades e responsabilidades lógicas por serviço": "services/                 Logical capabilities and responsibilities by service",
    "governance/               Workflow, risco, catálogo e ciclo de modelos": "governance/               Workflow, risk, catalog and model lifecycle",
    "security/                 Autenticação, autorização, LGPD, RAG/memória e threat model": "security/                 Authentication, authorization, LGPD, RAG/memory and threat model",
    "observability/            Tracing, métricas, dashboards, alertas e SLOs": "observability/            Tracing, metrics, dashboards, alerts and SLOs",
    "finops/                   Custos, budgets, chargeback e showback": "finops/                   Costs, budgets, chargeback and showback",
    "runbooks/                 Procedimentos operacionais de referência": "runbooks/                 Reference operational procedures",
    "examples/                 Exemplos ponta a ponta": "examples/                 End-to-end examples",
    "reference-architectures/  Blueprints por caso de uso": "reference-architectures/  Blueprints by use case",
    "roadmap/                  Sequenciamento recomendado para implementação": "roadmap/                  Recommended implementation sequence",

    # Agent lifecycle editorial polish
    "operational strategy.The governed": "operational strategy. The governed",
    "- Why AI is needed?": "- Why is AI needed?",
    "- rating risk;": "- classifying risk;",
    "- estimate volume, latency and cost;": "- estimating volume, latency and cost;",
    "- check for existing solutions;": "- checking for existing solutions;",
    "- define delivery route.": "- defining the delivery route.",
    "Non-purpose cases, applicable legal basis, data owner or strategy for critical actions do not follow for design.": "Cases without a defined purpose, applicable legal basis, data owner, or strategy for critical actions do not proceed to design.",
    "- borders between runtime, registration systems and tools;": "- boundaries between runtime, systems of record and tools;",
    "- assessment strategy;": "- evaluation strategy;",
    "during the execution.Document-only": "during execution. Document-only",
    "- commit and build immutable;": "- immutable commit and build;",
    "| Cost | cost per invocation, task completed and user |": "| Cost | cost per invocation, completed task and user |",
    "- Daily budget;": "- daily budget;",
    "- 30 days review;": "- review after 30 days;",
    "- User feedback.": "- user feedback.",
    "and `correlationId` it is essential for diagnosis.": "and `correlationId` is essential for diagnosis.",
    "## Stage 10 — Remove": "## Stage 10 — Retire",
    "- elimination or anonymity of memory;": "- deletion or anonymization of memory;",
    "| quality assessment | sample | dates | dataset + baseline |": "| quality assessment | sample | dataset | dataset + baseline |",
    "O [case study of document agent](05-case-study-document-agent.md) it applies this problem cycle to the operation.": "The [document agent case study](05-case-study-document-agent.md) applies this lifecycle to an operational scenario.",

    # Risk framework terminology
    "| operational |": "| Operational |",
    "| Financial party |": "| Financial |",
    "| Reputacional |": "| Reputational |",
    "policy enforcement, inadequacy, human approval": "policy enforcement, idempotency, human approval",
    "| Quality requirement |": "| Quality regression |",
    "gate de deploy": "deployment gate",
    "| Owner definido |": "| Owner defined |",
    "runbook operational": "operational runbook",
    "rollback plane": "rollback plan",
    "## Publication banks": "## Publication gates",
    "blockades": "blocks",
    "case of use": "use case",

    # GRC crosswalk terminology
    "owner registrado": "registered owner",
    "date governance and quality": "data governance and quality",
    "date contract": "data contract",
    "dataet": "dataset",
    "Product / Date Owner": "Product / Data Owner",
    "Date Owner": "Data Owner",
    "rollout controlado": "controlled rollout",
    "| Date of lineage and classification |": "| Data lineage and classification |",
    "| Evaluation | sample | dates | dataset + baseline |": "| Evaluation | sample | dataset | dataset + baseline |",
    "## Evidence bundle de compliance": "## Compliance evidence bundle",

    # Recurring machine-translation artifacts
    "datesets": "datasets",
    "dateset": "dataset",
    "publicated": "published",
    "publicate": "publish",
    "AGR": "RAG",
    "PPA": "API",
}


def main() -> int:
    changed_files = 0
    replacements = 0
    for path in sorted(DOCS.rglob("*.en.md")):
        text = path.read_text(encoding="utf-8")
        updated = text
        file_replacements = 0
        for source, target in REPLACEMENTS.items():
            count = updated.count(source)
            if count:
                updated = updated.replace(source, target)
                file_replacements += count
        if updated != text:
            path.write_text(updated, encoding="utf-8")
            changed_files += 1
            replacements += file_replacements
            print(f"Polished {path}: {file_replacements} replacement(s)")
    print(f"English pages polished: {changed_files}")
    print(f"Editorial replacements applied: {replacements}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
