# Implementation Roadmap

## Baseline delivered to this repository

The reference already contains:

- Enterprise AI Platform Book with journeys per profile;
- capability map and liability boundaries;
- operating model, RACI, forums and golden path;
- risk and evidence-based life cycle of agents;
- case-to-case study of a documentary agent with RAG;
- decision guides and production checklists;
- automated export of the book to Markdown and PDF;
- OpenAPI and canonical AsyncAPI contracts;
- policies and contract validation in IC;
- Container C4 and deployment with control plane/data plane;
- Explicit model Gateway;
- feasible RAG security and memory;
- runbooks operational;
- vertical slice feasible with Docker Compose;
- publicizable documentation via MkDocs and GitHub Pages.

The vertical slice is deliberately small. The phases below describe the evolution of a real implementation for production.

## Fase 1 — Foundation

### Objective

Create the minimum planned date for the controlled execution of agents.

### deliverables

- Agent Gateway;
- Agent Runtime;
- Agent Registry;
- ICDC and workload identity;
- Policy Decision Point and Policy Enforcement Points;
- Model Gateway;
- baseline OpenTelemetry;
- backbone Kafka;
- IC/CD with contract tests.

### Success criteria

- first agent published by pipeline;
- trace end a end;
- published canonical events;
- authorisation `deny by default` exercitada;
- rollback validado;
- SLO `INTERACTIVE_SIMPLE` measured.

## Phase 2 — Knowledge and Memory

### deliverables

- Knowledge Service;
- quarantine pipeline;
- ACL by document and chunk;
- versioned embeddings;
- hybrid search;
- citations;
- Memory Service with TTL, consent and exclusion;
- separate evaluation of retrieval and generation.

### Success criteria

- cross-tenant access blocked in tests;
- documents no longer appear in the retrieval;
- groundedness and retrieval metrics collected;
- memory poisoning covered by tests.

## Phase 3 — PCM and corporate tools

### deliverables

- MCP Registry;
- onboarding automatizado;
- tool contracts versioned;
- idempotence and outbox for writing;
- human approval for critical actions;
- audit and metrics per tool.

### Success criteria

- discovery limited by agent and policy;
- repetition does not double effects;
- tools can be blocked without dismissing Runtime;
- rollback or compensation tested.

## Phase 4 — Governance and Evaluation

### deliverables

- AI Catalog;
- workflow with function segregation;
- risk assessment automatizado;
- datasets and databases;
- quality gates;
- immutable evidence;
- model lifecycle.

### Success criteria

- no HIGH/CRITICAL version published without evidence;
- the same identity does not submit and approve;
- regressions block deploy;
- thresholds are traceable to dataset and version.

## Phase 5 — Scale and FinOps

### deliverables

- multi-tenant isolation endurecido;
- competition autoscaling and backlog;
- budgets, quotas and chargeback;
- internal marketplace;
- disaster recovery;
- dashboards executivos;
- multi-region operation when justified.

### Success criteria

- costs attributed by area, agent and model;
- noisy neighbor controlado;
- 2x peak capacity tests;
- RTO/RPO exercitados;
- error budgets used in release decisions.

## Reference sequencing

| Phase | Initial Horizonte | Results |
|---|---|---|
| 1 | 0–3 meses | controlled internal agent in production |
| 2 | 3–6 months | RAG and memory with authorisation and discard |
| 3 | 6–9 meses | tools corporativas governadas |
| 4 | 9–12 months | evidence-based publication |
| 5 | 12+ months | scale, marketplace and financial control |

For the organizational and adoption perspective, see [Maturity model and roadmap](../book/07-adoption-roadmap.md).
