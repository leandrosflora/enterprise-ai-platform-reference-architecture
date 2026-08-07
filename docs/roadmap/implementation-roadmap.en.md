# Implementation Roadmap

## Baseline for this repository

The reference already contains:

- Enterprise AI Platform Book with a profile;
- capability map and responsibility borders;
- operating model, RACI, frogs and golden path;
- life cycle of agents based on risk and evidence;
- the case-by-case study of the documentary agent-point with RAG;
- decision guides and production checklists;
- automatic export of book to Markdown and PDF;
- contracts OpenAPI and AsyncAPI canonics;
- policies and contracts validating in CI;
- C4 container and deployment with control plane/data plane;
- Model Gateway explcito;
- executing security of RAG and memory;
- runbooks operacionais;
- vertical slice executable with Docker Compose;
- GitHub Pages and MkDocs.

The vertical slice is deliberately small, and the steps below describe the evolution of a real implementation for production.

## Fase 1 — Foundation

### Objet

Creating the data plane minimum for control-controlled execution of agents.

### Entregas

- Agent Gateway;
- Agent Runtime;
- Agent Registry;
- OIDC e workload identity;
- Policy Decision Point e Policy Enforcement Points;
- Model Gateway;
- baseline OpenTelemetry;
- backbone Kafka;
- CI/CD with contract tests.

### Success criteria

- first agent published by pipeline;
- trace the point;
- canopic events published;
- authorisation `deny by default` exercised;
- rollback validado;
- SLO of `INTERACTIVE_SIMPLE` as measured.

## Fase 2 — Knowledge e Memory

### Entregas

- Knowledge Service;
- pipeline of ingesting with quarantine;
- ACL for document and chunk;
- embeddings versionados;
- a hybrid;
- citations;
- Memory Service with TTL, consent and exclusion;
- separate evaluation of retrieval and generation.

### Success criteria

- cross-tenant access blocked in tests;
- documents deleted are not to appear in retrieval;
- groundedness e retrieval metrics coletadas;
- Memory poisoning covered by tests.

## Fase 3 — MCP e ferramentas corporativas

### Entregas

- MCP Registry;
- onboarding automatizado;
- tool contracts versionados;
- idempotence and box for writing;
- human approval for critical actions;
- auditory and tools by tool.

### Success criteria

- found only by agent and policy;
- repeating not double effects;
- tools can be blocked without indisposing Runtime;
- rollback or test compensation.

## Fase 4 — Governance e Evaluation

### Entregas

- AI Catalog;
- workflow with separate functions;
- risk assessment automatizado;
- datasets e baselines;
- quality gates;
- imutable evidence;
- model lifecycle.

### Success criteria

- no HIGH/CRITICAL version published without evidence;
- Identity does not submit and approve;
- regresses blocked deploy;
- thresholds are rastreatable to the dataset and version.

## Fase 5 — Scale e FinOps

### Entregas

- multi-tenant isolation endurecido;
- autoscaling for competition and backlog;
- budgets, quotas e chargeback;
- marketplace interno;
- disaster recovery;
- dashboards executivos;
- Multi-region operation when justified.

### Success criteria

- cost allocated by area, agent and model;
- noisy neighbor controlado;
- capacity tests at 2x of the pico;
- RTO/RPO exercitados;
- budget error used in release decisions.

## Reference sequence

| Fase | Horizonte inicial | Resultado |
|---|---|---|
| 1 | 0–3 meses | Internal agent controlled in production |
| 2 | 3–6 meses | RAG and memory with authorisation and discharge |
| 3 | 6–9 meses | tools corporativas governadas |
| 4 | 9–12 meses | published on the basis of risk and evidence |
| 5 | 12+ meses | escala, marketplace e controle financeiro |

For the organisational and adoption perspective, consult [Model of maturity and roadmap](../book/07-adoption-roadmap.md).
