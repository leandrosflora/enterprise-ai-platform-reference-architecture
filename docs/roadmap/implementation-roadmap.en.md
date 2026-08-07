# Implementation Roadmap

## Baseline delivered to this repository

The reference already contains:

- Enterprise AI Platform Book com jornadas por perfil;
- capability map and liability boundaries;
- operating model, RACI, forums and golden path;
- risk and evidence-based life cycle of agents;
- case-to-case study of a documentary agent with RAG;
- decision guides and production checklists;
- automated export of the book to Markdown and PDF;
- OpenAPI and canonical AsyncAPI contracts;
- policies and contract validation in IC;
- C4 de container e deployment com control plane/data plane;
- Explicit model Gateway;
- feasible RAG security and memory;
- runbooks operacionais;
- vertical slice feasible with Docker Compose;
- publicizable documentation via MkDocs and GitHub Pages.

The vertical slice is deliberately small. The phases below describe the evolution of a real implementation for production.

## Fase 1 — Foundation

### Objective

Create the minimum planned date for the controlled execution of staff.

### Entregas

- Agent Gateway;
- Agent Runtime;
- Agent Registry;
- OIDC e workload identity;
- Policy Decision Point e Policy Enforcement Points;
- Model Gateway;
- baseline OpenTelemetry;
- backbone Kafka;
- CI/CD com contract tests.

### Success criteria

- first agent published by pipeline;
- trace ponta a ponta;
- published canonical events;
- authorisation `deny by default` exercitada;
- rollback validado;
- SLO de `INTERACTIVE_SIMPLE` medido.

## Fase 2 — Knowledge e Memory

### Entregas

- Knowledge Service;
- quarantine pipeline;
- ACL por documento e chunk;
- embeddings versionados;
- hybrid search;
- citations;
- Memory Service with TTL, consent and exclusion;
- separate evaluation of retrieval and generation.

### Success criteria

- acesso cross-tenant bloqueado em testes;
- documentos eliminados deixam de aparecer no retrieval;
- groundedness e retrieval metrics coletadas;
- memory poisoning coberto por testes.

## Phase 3 — PCM and corporate tools

### Entregas

- MCP Registry;
- onboarding automatizado;
- tool contracts versionados;
- idempotence and outbox for writing;
- human approval for critical actions;
- audit and metrics per tool.

### Success criteria

- discovery limited by agent and policy;
- repetition does not double effects;
- tools can be blocked without dismissing Runtime;
- rollback or compensation tested.

## Fase 4 — Governance e Evaluation

### Entregas

- AI Catalog;
- workflow with function segregation;
- risk assessment automatizado;
- datasets e baselines;
- quality gates;
- immutable evidence;
- model lifecycle.

### Success criteria

- no HIGH/CRITICAL version published without evidence;
- the same identity does not submit and approve;
- regressions block deploy;
- thresholds are traceable to dataset and version.

## Fase 5 — Scale e FinOps

### Entregas

- multi-tenant isolation endurecido;
- competition autoscaling and backlog;
- budgets, quotas e chargeback;
- marketplace interno;
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

| Fase | Horizonte inicial | Results |
|---|---|---|
| 1 | 0–3 meses | controlled internal agent in production |
| 2 | 3–6 meses | AGR and memory with authorisation and discard |
| 3 | 6–9 meses | tools corporativas governadas |
| 4 | 9–12 meses | evidence-based publication |
| 5 | 12+ meses | escala, marketplace e controle financeiro |

For the organizational and adoption perspective, see [Maturity model and roadmap](../book/07-adoption-roadmap.md).
