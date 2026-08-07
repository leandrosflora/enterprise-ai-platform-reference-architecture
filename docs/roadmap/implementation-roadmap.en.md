# Implementation Roadmap

## Baseline delivered to this repository

The reference already contains:

- Enterprise AI Platform Book with journeys by profile;
- capability map and boundaries of responsibility;
- the operating model, RACI, forums and golden path;
- the life cycle of risk-based and evidence-based agents;
- the end-to-end case study of a documentary agent with RAG;
- decision guides and production checklists;
- Automated export of the book to Markdown and PDF;
- contracts OpenAPIand AsyncAPIcanonical;
- policies and contract validations in CI;
- the container C4 and deployment with control plane/data plane;
- Model Gatewayexplicitly;
- the executable security of RAG and memory;
- runbooks operacionais;
- a vertical slice executable with Docker Composite;
- documentation that can be published via MkDocs and GitHub Pages.

The vertical slice is deliberately small. The phases below describe the evolution of an actual implementation to production.

## Fase 1 — Foundation

### Objective

Create the minimum data plane for the controlled execution of agents.

### Entregas

- Agent Gateway;
- Agent Runtime;
- Agent Registry;
- OIDCand workload identity;
- Policy Decision Points and Policy Enforcement Points
- Model Gateway;
- baseline OpenTelemetry;
- backbone Kafka;
- CI/CD with contract tests.

### Criteria for success

- first agent issued by pipeline;
- draw a line from end to end;
- published canonical events;
- the `deny by default` authorisation has been exercised;
- rollback validado;
- The value of the measured SLO of `INTERACTIVE_SIMPLE`.

## Stage 2  Knowledge and Memory

### Entregas

- Knowledge Service;
- the intake pipeline with quarantine;
- ACL per document and chunk;
- embeddings versionados;
- hybrid search;
- quotes;
- Memory Service with TTL, consent and exclusion;
- separate retrieval and generation assessment.

### Criteria for success

- cross-tenant access blocked in tests;
- deleted documents no longer appear in retrieval;
- groundedness and retrieval metrics collected;
- memory poisoning covered by tests.

## Phase 3  MCP and corporate tools

### Entregas

- MCP Registry;
- onboarding automatizado;
- tool contracts versionados;
- idempotence and outbox for writing;
- human approval for critical actions;
- auditing and metrics per tool.

### Criteria for success

- limited agent and policy discovery;
- repetition does not duplicate effects;
- tools can be blocked without making Runtime unavailable;
- rollback or compensation tested.

## Stage 4  Governance and Evaluation

### Entregas

- AI Catalog;
- a workflow with function segregation;
- risk assessment automatizado;
- data sets and baselines;
- quality gates;
- the evidence is unchanging;
- model lifecycle.

### Criteria for success

- no HIGH/CRITICAL version published without evidence;
- the same identity does not submit and approve;
- the regression blocks deployment;
- thresholds are traceable to the dataset and version.

## Phase 5 Scale and FinOps

### Entregas

- multi-tenant isolation endurecido;
- competition and backlog autoscaling;
- budgets, quotas and chargeback;
- marketplace interno;
- disaster recovery;
- dashboards executivos;
- multi-regional operation where justified.

### Criteria for success

- costs assigned by area, agent and model;
- noisy neighbor controlado;
- capacity tests at 2x peak;
- RTO/RPO exercitados;
- error budgets used in release decisions.

## Sequencing of reference

| Fase | Horizonte inicial | Results |
|---|---|---|
| 1 | 0–3 meses | Internal controlled agent in production |
| 2 | 3–6 meses | RAG and memory with authorisation and discard |
| 3 | 6–9 meses | tools corporativas governadas |
| 4 | 9–12 meses | Risk-based and evidence-based publication |
| 5 | 12+ meses | Scale, marketplace and financial control |

For the organisational and adoption perspective, see [Maturity model and roadmap](../book/07-adoption-roadmap.md).
