# Enterprise AI Platform Book

This book is a reference guide to the design, governance, implementation and operation of an AI corporate platform. It connects strategy, architecture, security, delivery and operation through models, decisions, contracts and controls that are adaptable to the context of each organization.

The proposal is not to deliver a ready-made platform, a software distribution or a mandatory technological implementation, but to provide a mental model, explicit decisions, minimum controls and evolutionary pathways that support each organisation in building its own platform.

The components and services described represent a logical decomposition of capabilities. They can be implemented with different products, providers, topologies and levels of granularity.

## What You'll Find

- A narrative that starts with the organizational problem, before technology.
- a capability map to define the scope of the platform;
- an operating model with responsibilities and decision-making forums;
- an agent life cycle based on risk and evidence;
- a complete case study of a documentary agent with RAG;
- decision guides for recurring architectural choices;
- a maturity model and adoption roadmap;
- readiness checklists for production;
- contracts, diagrams, policies and technical samples as reference material.

## Reading paths

| Perfil | Recommended route | Expected result |
|---|---|---|
| Executivo ou sponsor | Chapter 1, 2, 3 and 7 | Understand the value, scope, investment, risks and sequence of adoption |
| Arquiteto | Chapter 1 to 7 | master capabilities, decisions, borders and trade-offs |
| Platform engineering | Chapter 2, 4, 5, 6 and 8 | Transform the reference into a deployable and operable backlog |
| Security, Legal and LGPD | Chapters 3, 4, 5 and 8 | identify gates, evidence, classification and responsibilities |
| Product squad | Chapters 1, 4, 5 and 8 | Structuring a use case and publishing it on the golden path |
| SRE and FinOps | Chapters 2, 4, 7 and 8 | define SLOs, capacity, incidents, budgets and accountability |

## Parts of the book

1. [Why one ?AI Platform?](01-why-ai-platform.md)
2. [Capability Map](02-capability-map.md)
3. [Operating Model](03-operating-model.md)
4. [Life cycle of agents](04-agent-lifecycle.md)
5. [Case study: documentary agent with RAG](05-case-study-document-agent.md)
6. [Decision Guides](06-decision-guides.md)
7. [Maturity model and adoption roadmap](07-adoption-roadmap.md)
8. [Checklists of production](08-production-checklists.md)
9. [Glossary of terms](glossary.md)

## How to Use Technical Artifacts

The chapters explain context, decisions and consequences.

| Assunto | Technical reference |
|---|---|
| Principles,C4and NFRs | [`../architecture/`](../architecture/principles/principles.md) |
| APIs, events and MCP | [`../contracts/`](../contracts/apis.md) |
| Logical capabilities and services | [`../services/`](../services/agent-gateway.md) |
| Governance and risk | [`../governance/`](../governance/ai-governance-framework.md) |
| Security | [`../security/`](../security/ai-security-architecture.md) |
| Observability and SLOs | [`../observability/`](../observability/tracing.md) |
| FinOps | [`../finops/`](../finops/ai-finops.md) |
| Reference runbooks | [`../runbooks/`](../runbooks/onboarding-agent.md) |
| Validation sample | [`../../samples/vertical-slice/`](https://github.com/leandrosflora/enterprise-ai-platform-demo-arch/tree/main/samples/vertical-slice) |

The technical sample exists to verify contracts and some documented controls. It does not represent a recommended physical architecture or a productive implementation of the platform.

## Convention of Chapters

Each chapter seeks to answer five questions:

1. What problem is being solved?
2. What decision or model is recommended?
3. Quais trade-offs foram assumidos?
4. How do you make sure the decision works?
5. What's the next technical artifact to consult?

## Scope and limits

This material is a reference architecture for implementation. It does not replace specific threat modeling, legal analysis, sizing, supplier homologation, load testing or detailed infrastructure design. Decisions must be reassessed when risk, volume, criticism or regulation change.
