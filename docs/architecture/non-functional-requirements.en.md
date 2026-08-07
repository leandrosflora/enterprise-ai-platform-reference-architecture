# Non-functional requirements

## Objective

Set measurable goals for the design, testing, operation and governance of Enterprise AI Platform. SLOss are classified by **workload type**, not risk level.

## Workload classes

| Classe | Example | Recommended mode | SLOOther, of a width of not more than 600 mm |
|---|---|---|---:|
| `INTERACTIVE_SIMPLE` | Chat without RAG or tool | Synchronous | <= 5 s |
| `INTERACTIVE_RAG` | Retrieval + generation | Synchronous or streaming | <= 8 s |
| `INTERACTIVE_TOOL` | Consult the tool with no side effects | Synchronous | <= 15 s |
| `TRANSACTIONAL_AGENT` | Human writing or approval tool | Asynchronous | Accept <= 2 s; conclusion by process |
| `BATCH_INGESTION` | Intake and document indexation | Asynchronous | Defined by volume |
| `BATCH_EVALUATION` | Assessment of datasets | Asynchronous | P95 <= 15 min for standard dataset |

Risk defines controls, approvals, and evidence. It doesn't artificially alter the latency class.

## Availability and continuity

| Capacity | Reference target |
|---|---:|
| Agent Gateway | 99,95% mensal |
| Agent Runtime | 99,9% mensal |
| Policy Decision Point | 99,99% mensal |
| Control plane | 99,5% mensal |
| Publishing of events | 99.9% success rate |
| Critical audit record | 99.99% success rate |
| RTO data plane | <= 2 h |
| RPO metadados transacionais | <= 15 min |

- critical services are multi-AZ;
- the data plane uses the last valid policy when control plane is unavailable;
- the absence of applicable policy results in `deny by default`;
- backups and restoration are tested at least every six months.

## Performance

| Requisito | Meta |
|---|---:|
| Agent Gateway without external call | P95 <= 300 ms |
| Policy decision | P95 <= 100 ms |
| Knowledge retrieval | P95 <= 2 s |
| Model Gateway overhead | P95 <= 250 ms excluding the provider |
| Reading tool execution | P95 <= 4 s, except for specific contract |
| Acceptance of asynchronous operation | P95 <= 2 s |

Each tool contract sets its own timeout. The standard is 30s and can only be extended with justification.

## Escalabilidade

- stateless components scale horizontally;
- rows decouple input, evaluation, audit and billing;
- Partition keys preserve assembly order;
- autoscaling considers competition, latency, backlog and consumption of tokens;
- limits per tenant prevent noisy neighbor;
- capacity tests validate twice the expected peak.

## Security

- OIDC/OAuth2for human identities and workload identity for services;
- RBAC combined with contextual policies by tenant, resource, data and risk;
- mTLS or an equivalent mechanism between critical services;
- Secrets in secret manager, never in repository or pipeline variables in clear;
- encryption in transit and at rest;
- egress allowlist for external providers;
- the separation between control plane and data plane;
- SAST, dependency scanning, secret scanning and image scanning in the pipeline.

## Data and LGPD

- compulsory classification in documents, memory, events and traces;
- data minimisation by default;
- ACL per document and chunk in retrieval;
- explicit TTL for memory;
- Supported consultation, exclusion and anonymisation;
- The data shall be stored in a format that is consistent with the requirements of this Regulation.
- lineage and checksum for documents received;
- quarantine and validation prior to indexation.

## Resilience

| Mecanismo | Diretriz |
|---|---|
| Timeout | Shorter than the deadline for the top call. |
| Retry | Only for transient errors and idle operations. |
| Circuit breaker | Mandatory for external suppliers and tools. |
| Bulkhead | Isolation by provider, tenant and critical tool. |
| Fallback | Model, supplier or alternative flow approved. |
| Impotence | Mandatory for side-effective commands and tool calls. |
| Outbox | Mandatory for events arising from critical transactions. |
| Graceful degradation | Partial response or asynchronous when safe. |

## Observability

- OpenTelemetry for traces, metrics and logs;
- W3C Traces Context in HTTP and events;
- `correlationId`for functional correlation;
- The following information shall be provided in accordance with the provisions of this Regulation:
- alerts linked to runbooks;
- controlled cardinality; user IDs do not appear as metric labels.

## FinOps

- the cost assigned per tenant, unit, agent, version, model and environment;
- the budget and quota per agent;
- Alerts at 70%, 90% and 100%;
- controlled locking or degradation when the limit is exceeded;
- comparison of cost and quality before changing the standard model;
- Embedding, storage and tooling costs are included in the total cost.

## Auditabilidade

- policy decisions record policy ID and version;
- administrative changes are recorded before/after and justification;
- critical events use approved retention;
- access to the audit logs themselves is also audited;
- governance evidence is unchanged after publication.
