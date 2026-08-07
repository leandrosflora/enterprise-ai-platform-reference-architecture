# Non-functional requirements

## Objective

Defining measurable goals for design, testing, operation and governance of Enterprise AI Platform. The SLOs are classified by **workload type**, not by risk level.

## Workload classes

| Class | Example | Recommended way | P95 latency SLO |
|---|---|---|---:|
|  `INTERACTIVE_SIMPLE`  | Chat without RAG or tool | Synchronous | <= 5 s |
|  `INTERACTIVE_RAG`  | Retrieval + generation | Synchronous or streaming | <= 8 s |
|  `INTERACTIVE_TOOL`  | Refer to the tool without side effect | Synchronous | <= 15 s |
|  `TRANSACTIONAL_AGENT`  | Writing tool or human approval | Asynchronous | Accept <= 2 s; conclusion according to process |
|  `BATCH_INGESTION`  | Document management and indexing | Asynchronous | Definido por volume |
|  `BATCH_EVALUATION`  | Evaluation of dates | Asynchronous | P95 <= 15 min for standard dates |

Risk defines controls, approvals and evidence, and does not artificially alter the latency class.

## Availability and continuity

| Capacity | Reference target |
|---|---:|
| Agent Gateway | 99,95% mensal |
| Agent Runtime | 99,9% mensal |
| Policy Decision Point | 99,99% mensal |
| Control plane | 99,5% mensal |
| Publication of events | 99.9% success |
| Critical audit record | 99.89% success |
| RTO data plane | <= 2 h |
| RPO metadados transacionais | <= 15 min |

- critical services are multi-AZ;
- the data plane uses the latest valid policy when the control plane is unavailable;
- absence of applicable policy results in `deny by default`;
- backups and restoration are tested at least every six months.

## Performance

| Requirements | Target |
|---|---:|
| Agent Gateway without external call | P95 <= 300 ms |
| Policy decision | P95 <= 100 ms |
| Knowledge retrieval | P95 <= 2 s |
| Model Gateway overhead | P95 <= 250 ms, excluindo o provedor |
| Read tool execution | P95 < = 4 s, except for specific contract |
| Acceptance of asynchronous surgery | P95 <= 2 s |

Each tool contract defines its own timeout, the standard is 30 s and can only be extended with justification.

## Escalabilidade

- componentes stateless escalam horizontalmente;
- queues disattach intake, evaluation, audit and billing;
- partition keys preserve aggregate ordering;
- autoscaling considers competition, latency, backlog and token consumption;
- limits by tenant prevent noisy neighbor;
- capacity tests validate twice the predicted peak.

## Security

- ICDC/OAuth2 for human identities and workload identity for services;
- RBAC combined with contextual policies by tenant, resource, given and risk;
- mTLS or equivalent mechanism between critical services;
- secrets in secret manager, never in repository or pipeline variables in clear;
- cryptography in transit and at rest;
- egress allowlist for external providers;
- segregation between control plane and date plane;
- SAST, dependency scanning, secret scanning and pipeline image scanning.

## Data and LGPD

- mandatory classification into documents, memory, events and traces;
- Minimizing data by standard;
- ACL per document and chunk in retrieval;
- Explicit TTL for memory;
- consultation, exclusion and anonymization supported;
- prompts and sensitive responses are not fully stored by pattern;
- lineage and checksum for ingested documents;
- quarantine and validation before indexing.

## Resilience

| Mecanismo | Diretriz |
|---|---|
| Timeout | Less than the deadline of the higher call. |
| Retry | Only for transient errors and inadequate operations. |
| Circuit breaker | Obligatory for providers and external tools. |
| Bulkhead | Isolation by provider, tenant and critical tool. |
| Fallback | Model, provider or alternative flow approved. |
| idempotency | Obligatory for commands and tool calls with side effect. |
| Outbox | Obligatory for critical transactions. |
| Graceful degradation | Partial or asynchronous response when safe. |

## Observability

- OpenTelemetry for traces, metrics and logs;
- W3C Trace Context in HTTP and events;
- `correlationId` for functional correlation;
- latency metrics, error, tokens, cost, retrieval, quality and policy denials;
- alertas vinculados a runbooks;
- controlled cardinality; User DIs do not appear as metric labels.

## FinOps

- cost attributed by tenant, unit, agent, version, model and environment;
- budget and quota per agent;
- alerts in 70%, 90% and 100%;
- blocking or controlled degradation where the limit is exceeded;
- comparison of cost and quality before changing the standard model;
- embedding costs, storage and tools are included in the total cost.

## Auditabilidade

- policy decisions register policy ID and version;
- administrative changes register actor, before/after and justification;
- critical events use approved retention;
- Access to the audit logs is also audited;
- evidences of governance are immutable after publication.
