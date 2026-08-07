# Enterprise AI Platform Book

This book is a **reference to guide the design, governance, implementation and operation of an AI corporate platform**. It connects strategy, architecture, security, delivery and operation through models, decisions, contracts and controls adapted to the context of each organization.

The proposal is not to deliver a ready platform, software distribution or mandatory technological implementation. The objective is to provide a mental model, explicit decisions, minimum controls and evolutionary paths that support each organization in building its own platform.

The components and services described represent a logical decomposition of capabilities, and they can be implemented with different products, providers, topology and granularity levels.

## What you will find

- a narrative that starts with the organizational problem, before technology;
- a capability map to delimit the scope of the platform;
- an operating model with responsibilities and decision forums;
- a risk-based life cycle of agents;
- a complete case study of a documentary agent with RAG;
- decision guides for recurrent architectural choices;
- a maturity model and adoption roadmap;
- checklists of readiness for production;
- contracts, diagrams, polycies and technical samples as reference material.

## Reading paths

| Perfil | Recommended path | Expected result |
|---|---|---|
| Executive or Sponsor | Chapters 1, 2, 3 and 7 | understand value, scope, investment, risks and adoption sequence |
| Arquiteto | Chapters 1 to 7 | mastering capacities, decisions, boundaries and trade-offs |
| Platform engineering | Chapters 2, 4, 5, 6 and 8 | Transforming the reference into implementing and operable backlog |
| Security, Legal and LGPD | Chapters 3, 4, 5 and 8 | identify gates, evidence, classification and responsibilities |
| Product squad | Chapters 1, 4, 5 and 8 | structure a case of use and publish it by golden path. |
| SRE and FinOps | Chapters 2, 4, 7 and 8 | define SLOs, capacity, incidents, budgets and accountability |

## Parts of the book

1. [Why an AI Platform?](01-why-ai-platform.md)
2. [Capability Map](02-capability-map.md)
3. [Operating Model](03-operating-model.md)
4. [Life cycle of agents](04-agent-lifecycle.md)
5. [Case study: documentary agent with RAG](05-case-study-document-agent.md)
6. [Decision Guides](06-decision-guides.md)
7. [Maturity model and adoption roadmap](07-adoption-roadmap.md)
8. [Production Checklists](08-production-checklists.md)
9. [Glossary](glossary.md)

## How to use technical artifacts

The chapters explain the context, decisions and consequences, and the technical directories remain as canonical reference sources:

| Subject | Technical reference |
|---|---|
| Principles, C4 and NFRs |  [`../architecture/`](../architecture/principles/principles.md)  |
| PIA, events and PCM |  [`../contracts/`](../contracts/apis.md)  |
| Capacities and logical services |  [`../services/`](../services/agent-gateway.md)  |
| Governance and risk |  [`../governance/`](../governance/ai-governance-framework.md)  |
| Security |  [`../security/`](../security/ai-security-architecture.md)  |
| Observability and SLOs |  [`../observability/`](../observability/tracing.md)  |
| FinOps |  [`../finops/`](../finops/ai-finops.md)  |
| Reference Runbooks |  [`../runbooks/`](../runbooks/onboarding-agent.md)  |
| Validation sample |  [`../../samples/vertical-slice/`](https://github.com/leandrosflora/enterprise-ai-platform-demo-arch/tree/main/samples/vertical-slice)  |

The technical sample exists to verify contracts and some documented controls, and it does not represent a recommended physical architecture or a productive implementation of the platform.

## Convention of Chapters

Each chapter seeks to answer five questions:

1. What problem is being solved?
2. Which decision or model is recommended?
3. Quais trade-offs foram assumidos?
4. How to check that the decision works?
5. What is the next technical artifact to consult?

## Score and limits

This material is a reference architecture for implementation. It does not replace specific threat modeling, legal analysis, sizing, supplier approval, load tests or detailed infrastructure design. Decisions should be reassessed when the risk, volume, criticism or regulation change.
