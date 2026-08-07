# Non-functioning requirements

## Objet

Definition of the relevant metas for design, testing, operation and governance of Enterprise AI Platform. SLOs are classified as **load level**, not as a risk level.

## workload classes

| Classe | Exemplo | Modo recomendado | SLO of lattice P95 |
|---|---|---|---:|
| `INTERACTIVE_SIMPLE` | Chat without RAG or iron | Sncron | <= 5 s |
| `INTERACTIVE_RAG` | Retrieval + generation | Sing or streaming | <= 8 s |
| `INTERACTIVE_TOOL` | Consult the iron without colateral effect | Sncron | <= 15 s |
| `TRANSACTIONAL_AGENT` | Writing or human approval | Assyncron | Accept = 2 s; conclusion conforme process |
| `BATCH_INGESTION` | Ingestation and document index | Assyncron | Volume defined |
| `BATCH_EVALUATION` | Analysis of datasets | Assyncron | P95 = 15 min for the table dataset |

The risk defines controls, approvals and evidence, and it does not artificially alter the lativity class.

## Disponibilidade e continuidade

| Capacidade | Reference Meta |
|---|---:|
| Agent Gateway | 99,95% mensal |
| Agent Runtime | 99,9% mensal |
| Policy Decision Point | 99,99% mensal |
| Control plane | 99,5% mensal |
| Publication of events | 99.9% success |
| Critical auditory record | 99.99% success |
| RTO data plane | <= 2 h |
| RPO metadados transacionais | <= 15 min |

- critical services are multi-AZ;
- the data plane uses the last viable policy when the control plane is indisposible;
- non-applicable policy result in `deny by default`;
- backups and restoration are tested at least sequentially.

## Performance

| Requisito | Meta |
|---|---:|
| Agent Gateway without a foreign call | P95 <= 300 ms |
| Policy decision | P95 <= 100 ms |
| Knowledge retrieval | P95 <= 2 s |
| Model Gateway overhead | P95 =250 ms, excluding the driver |
| Tool execution of reading | P95 =4 s, special contract |
| Assyncrone operation | P95 <= 2 s |

Each tool contract defines its own timeout. The pattern is 30 and can only be amplified with justified meaning.

## Escalabilidade

- componentes stateless escalam horizontalmente;
- filas decompose ingest, evaluation, audit and billing;
- partition keys are preserved by agregated;
- autoscaling considers competition, latability, backlog and consumption of tokens;
- limits by tenant hinder noisy neighbor;
- Capacity tests valid the above-ground picobyte.

## Security

- OIDC/OAuth2 for human identities and identity workload for services;
- RBAC combined with context policies by tenant, resource, given and risk;
- mTLS or equivalent mechanism between critical services;
- secrets in secret manager, never in repository or variable pipelines of any kind;
- criptography in traffic and in reverse;
- a permit entry for external witnesses;
- separation between control plane and data plane;
- SAST, dependency scanning, secret scanning and image scanning in the pipeline.

## DATE and LGPD

- compulsory classification in documents, memory, events and trace;
- minimisation of data by default;
- ACL for document and file retrieval;
- TTL explended for memory;
- consult, exclude and anonimize;
- prompts and sensitive answers are not fully stored by a pattern;
- a line and checksum for ingerged documents;
- quarantine and validation before indexation.

## Resilience

| Mecanismo | Diretriz |
|---|---|
| Timeout | - I mean, the deadline for the call is higher. |
| Retry | Just for transitory errors and idempotent operations. |
| Circuit breaker | Thank you for external speakers and tools. |
| Bulkhead | Isolation by the driver, tenant and critical rail. |
| Fallback | Model, driver or alternate flow approved. |
| Idempotence | Thank you for commands and tools calls with colateral effect. |
| Outbox | Thank you for events resulting from critical transactions. |
| Graceful degradation | - Reject the shit or shit when safe. |

## Observability

- OpenTelemetry for trace, method and logs;
- W3C Trace Context in HTTP and events;
- `correlationId` for functional correction;
- methods of latability, error, tokens, cost, retrieval, quality and policy denials;
- alerts sent to runbooks;
- - Controlled cardinality; user IDs do not appear as metric labels.

## FinOps

- cost attributed by tenant, unit, agent, version, model and environment;
- budget and quota by agent;
- alerts in 70%, 90% and 100%;
- block or degraded when the limit is exceeded;
- comparison of cost and quality before changing the model pattern;
- The cost of embedding, storage and tools enters the total cost.

## Auditabilidade

- policy decisions shall register policy ID and version;
- administrative amendments shall register ator, before/after and justified;
- critical events use approved retention;
- access to auditory logs is also audited;
- Government evidence is mutable after publication.
