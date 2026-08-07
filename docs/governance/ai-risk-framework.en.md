# AI Risk Framework

## Objet

Classifying risk of A, setting appropriate controls and establishing verified evidence for publication and operation.

## Categorias

| Categoria | Exemplos |
|---|---|
| Security | Prompt injection, tool abuse, exfiltration, excessive agency. |
| Privacidade e compliance | LGPD, retention, consent, international transfer. |
| Operacional | Indisponibility, lack of integration, model degradation. |
| Model | Hallucination, bias, toxicity, regressiveness and low explanation. |
| Financeiro | Unrelentless consumption, quotas failure and chargeback. |
| Reputacional | Unsuitable claims and opportune decisions. |

## Classification

| N-n-n- | Criteria |
|---|---|
| LOW | Internal use, without sensitive data, without transacional action. |
| MEDIUM | Intern/confidential data, RAG or support the human decision. |
| HIGH | Personal/sensitive data, writing tool or relevant operational impact. |
| CRITICAL | Regulated automated decision, impact material on client, financial or legal. |

## Risk and control slut

| Risco | Security padrix | Obligatory checks | Evidence |
|---|---:|---|---|
| Direct/indirect prompt injection | HIGH | systorage, content scanning, tool allowlist, adversarial evaluation | Attack and block tests |
| Data leakage | CRITICAL | classification, masking, tenant isolation, DLP, output filtering | Isolation test and classification report |
| Tool abuse | HIGH | minimum escophages, enforcement policy, idempotence, human adoption | approuvé, authorisation contract, events |
| Excessive agency | HIGH | limits of autonomia, transaction boundary, human-in-the-loop | bloke and rollback buttons |
| Hallucination | MEDIUM | RAG, quotes, groundedness, fallback | dataset and assessment report |
| Poisoned knowledge | HIGH | provenance, quarantine, source approval, controlled reindexation | checksum, lineage and a slut-contained test |
| Memory poisoning | HIGH | - tyre, TTL, confirmation, use-isolation | Cruzad contamination tests |
| Bias | HIGH | dataset review, fairness when applicable, human review | criteria and report |
| Use of a non-legal basis | CRITICAL | finality, minimisation, retention and approval LGPD | DPIA/LIA when applicable |
| Provider outage | MEDIUM | timeout, circuit breaker, bulkhead, fallback | resiliency test and runbook |
| Custo inesperado | MEDIUM | quotas, budgets, rate limits, alertas e bloqueio | dashboard and limit test |
| - Lack of rasability | HIGH | trace context, audit trail, retention and policy version | trace and auditory event |
| Quality return | MEDIUM | baseline, dataset regression and deployment gate | comparative report |
| KB's unacceptable access | HIGH | ACL for document/chunk, ABAC and server-side filters | - Negative access test |

## Controls at level

| Controle | LOW | MEDIUM | HIGH | CRITICAL |
|---|---:|---:|---:|---:|
| Owner definido | Thank you. | Thank you. | Thank you. | Thank you. |
| Auto-évaluation | Thank you. | Thank you. | Thank you. | Thank you. |
| AI Architect Review | Opcional | Thank you. | Thank you. | Thank you. |
| Security review | Conforme escopo | Conforme escopo | Thank you. | Thank you. |
| LGPD | According to data | According to data | Thank you. | Thank you. |
| Legal/Regulative | No | Conforme escopo | Conforme escopo | Thank you. |
| Auditoria | Logic | Completa | Completa | Complete + retention |
| Human-in-the-loop | No |  Conformation | Thank you for writing critical | Thank you. |
| Rollback | Recomendado | Recomendado | Thank you. | Thank you. |
| FinOps budget | Recomendado | Thank you. | Thank you. | Thank you + block |

## Minimum evidence

- Agent Card versionado;
- risk assessment justified;
- a reproducible evaluation report;
- security review and threat model of the use case;
- LGPD review when there are people;
- the authorisations mater;
- traces, dashboards e alertas;
- budget e quotas;
- rollback plan;
- runbook operacional.

## Publications gates

| Gate | Condition |
|---|---|
| G1 — Design | domain, contracts, data, dependencies and defined owner |
| G2 — Security/LGPD | classification, authorisation and threat model approved |
| G3 — Evaluation | thresholds for the use of a hit |
| G4 — Observability | telemetria e alertas validados |
| G5 — FinOps | budget, quota and allocated |
| G6 — Operational readiness | runbook, capacidade, backup e rollback testados |
| G7 — Go-live | a separation of function and final approval registered |

## Quality thresholds

Thresholds are defined by the use and dataset. Initial values:

| Medicinal | LOW | MEDIUM | HIGH | CRITICAL |
|---|---:|---:|---:|---:|
| Minimum Groundedness for RAG | 0,80 | 0,85 | 0,90 | 0,95 |
| Minimum relevance | 0,75 | 0,80 | 0,85 | 0,90 |
| Maximum risk of haludation | 0,15 | 0,10 | 0,05 | 0,03 |
| Maximum Toxicity | 0,05 | 0,03 | 0,02 | 0,01 |

Latability is not a risk threshold, she follows the workload class defined in the non-functioning requirements.

## Policy the code

Bloke controls must be automated whenever possible:

- a person without ownership or risk cannot be submitted;
- a non-adopted iron cannot be withdrawn;
- a HIGH/CRITICAL agent without a sample can't be published;
- budget ausente bloqueia MEDIUM ou superior;
- Identity can not be lowered and approved;
- the published version is imutable;
- inexistent policy results in `deny by default`.
