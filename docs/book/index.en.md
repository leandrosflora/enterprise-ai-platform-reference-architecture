# Enterprise AI Platform Book

This book is a **reference to guide the development, governance, implementation and operation of a corporative A* platform. It connects strategy, architecture, security, delivery and operation by means of models, decisions, contracts and controls adaptable to the context of each organisation.

The proposal is not to deliver a ready platform, a software distribution or a compulsory technological implementation. The objective is to provide a mental model, explicit decisions, minimum controls and paths of evolution that support each organisation in building its own platform.

The components and services described represent a linear decomposition of capacity, which can be implemented with different products, testers, topologists and granularity levels.

## What will you find

- a narrative that begins by the organisational problem before technology;
- a capability map to define the scalability of the plate;
- a model operating with responsibility and decisions;
- a life cycle of agents based on risk and evidence;
- a complete case study of documentary agent with RAG;
- decision guides for recorrent architectural selections;
- a model of maturity and adoption roadmap;
- readiness checklists for production;
- contracts, diagrams, policies and technical samples as reference material.

## Lethargy paths

| Perfil | Caminho recomendado | Resultado esperado |
|---|---|---|
| Executivo ou sponsor | Chapters 1, 2, 3 and 7 | understand value, scope, investment, risks and the following adoption |
| Arquiteto | Chapters 1 to 7 | - Doing power, decisions, borders and tradeoffs |
| - Plateform engineering | Chapters 2, 4, 5, 6 and 8 | transform the reference into implementing and operational backlog |
| Security, Jury and LGPD | Chapters 3, 4, 5 and 8 | identify gates, evidence, classification and responsibility |
| Product squad | Chapters 1, 4, 5 and 8 | to build a case of use and publish it by the golden path |
| SRE e FinOps | Chapters 2, 4, 7 and 8 | definir SLOs, capacidade, incidentes, budgets e accountability |

## Parts of the book

1. [Why a AI Platform?](01-why-ai-platform.md)
2. [Capability Map](02-capability-map.md)
3. [Operating Model](03-operating-model.md)
4. [Life cycle of agents](04-agent-lifecycle.md)
5. [Assault study: documentary agent with RAG](05-case-study-document-agent.md)
6. [Decision Guides](06-decision-guides.md)
7. (Model of maturity and adoption roadmap)(07-adoption-roadmap.md)
8. (production checklists)(08-production-checklists.md)
9. [Glossary](glossary.md)

## How to use technical tools

The chapters explain context, decisions and consequences. Technical guidelines remain as canonical sources of reference:

| Assunto | Technical reference |
|---|---|
| Principles, C4 and NFRs | [`../architecture/`](../architecture/principles/principles.md) |
| APIs, eventos e MCP | [`../contracts/`](../contracts/apis.md) |
| Liquidity and services | [`../services/`](../services/agent-gateway.md) |
| Government and risk | [`../governance/`](../governance/ai-governance-framework.md) |
| Security | [`../security/`](../security/ai-security-architecture.md) |
| Observability and SLOs | [`../observability/`](../observability/tracing.md) |
| FinOps | [`../finops/`](../finops/ai-finops.md) |
| Reference Runbooks | [`../runbooks/`](../runbooks/onboarding-agent.md) |
| Validation sample | [`../../samples/vertical-slice/`](https://github.com/leandrosflora/enterprise-ai-platform-demo-arch/tree/main/samples/vertical-slice) |

The technical sample exists to verify contracts and some documented checks, and it does not represent a recommended physical arquivalence or a product-based implementation of the platform.

## Convention on Chapters

Each chapter seeks to answer five questions:

1. What's the problem?
2. What decision or model is recommended?
3. Quais trade-offs foram assumidos?
4. How do you check that the decision works?
5. What's the next technical instrument to consult?

## Escopo e limites

This material is a reference tool for implementation. It does not substitute specific threat modeling, legal analysis, sizing, homologation of suppliers, cargo tests or detailed inspection design. Decisions should be reviewed when the risk, volume, criticity or regulation change.
