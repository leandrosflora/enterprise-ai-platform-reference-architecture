# AI Risk Framework

## Objective

Classify AI risks, define proportional controls and establish verifiable evidence for publication and operation.

## Categorias

| Categoria | Examples |
|---|---|
| Security | Prompt injection, tool abuse, exfiltration, excessive agency |
| Privacy and compliance | LGPD, withholding, consent, international transfer. |
| Operacional | Unavailability, failure of integration, degradation of the model. |
| Model | Hallucination, bias, toxicity, regression and low explainability. |
| Financeiro | Unexpected consumption, no quotas and chargeback. |
| Reputacional | Inadequate answers and opaque decisions. |

## Classification

| Level | Criterion of use |
|---|---|
| LOW | Internal use, no sensitive data, no transactional action. |
| MEDIUM | Internal/confidential data, RAG or human decision support. |
| HIGH | Personal/sensitive data, writing tool or relevant operational impact. |
| CRITICAL | Automated regulated decision, material impact on client, financial or legal. |

## Risk matrix and controls

| Risco | Standard severity | Compulsory checks | Evidence |
|---|---:|---|---|
| Direct/indirect prompt injection | HIGH | The Commission shall adopt delegated acts in accordance with Article 21 of Regulation (EU) No 1303/2013. | Attack tests and lock logs |
| Data leakage | CRITICAL | The Commission shall adopt delegated acts in accordance with Article 21 of Regulation (EC) No 1069/2009. | isolation test and classification report |
| Tool abuse | HIGH | The Commission will examine whether the measures are compatible with the internal market and whether they are compatible with the internal market. | The Commission shall adopt delegated acts in accordance with the opinion of the Standing Committee. |
| Excessive agency | HIGH | The following information is provided for in the Annex to Implementing Regulation (EU) No 1303/2013.human-in-the-loop | Locking and rollback scenarios |
| Hallucination | MEDIUM | RAG, quotes, groundedness, fallback | Data set and evaluation report |
| Poisoned knowledge | HIGH | The Commission shall adopt delegated acts in accordance with Article 21 of Regulation (EU) No 1308/2013. | checksum, lineage and testing of malicious content |
| Memory poisoning | HIGH | the origin of the facts, TTL, confirmation, isolation per user | Cross-contamination tests |
| Bias | HIGH | the data set review, fairness where applicable, human review | Criteria and report |
| Use of data without legal basis | CRITICAL | the purpose, minimisation, retention and approval of LGPD | DPIA/LIA where applicable |
| Provider outage | MEDIUM | timeout, circuit breaker, bulkhead, fallback | Resilience test and runbook |
| Custo inesperado | MEDIUM | The Commission shall adopt delegated acts in accordance with Article 21 of Regulation (EU) No 1303/2013. | dashboard and limit test |
| Lack of traceability | HIGH | traces context, audit trail, retention and policy version | audit trail and event |
| The Commission shall adopt delegated acts in accordance with Article 21 of this Regulation. | MEDIUM | Baseline, regression dataset and deployment gate | Comparative report |
| Misappropriated access to KB | HIGH | ACL by document/chunk, ABAC and server-side filters | denied access test |

## Controls by level

| Controle | LOW | MEDIUM | HIGH | CRITICAL |
|---|---:|---:|---:|---:|
| Owner definido | Compulsory | Compulsory | Compulsory | Compulsory |
| Automated assessment | Compulsory | Compulsory | Compulsory | Compulsory |
| I'm not going to lie. | Opcional | Compulsory | Compulsory | Compulsory |
| Security Review | Conforme escopo | Conforme escopo | Compulsory | Compulsory |
| Revised .LGPD | According to data | According to data | Compulsory | Compulsory |
| Legal and regulatory matters | No , it 's not . | Conforme escopo | Conforme escopo | Compulsory |
| Auditoria | Basics | Completa | Completa | Complete + extended retention |
| Human-in-the-loop | No , it 's not . | As an action | Mandatory for critical writing | Compulsory |
| Rollback | Recommended | Recommended | Compulsory | Compulsory |
| FinOps budget | Recommended | Compulsory | Compulsory | Compulsory + blocked |

## Minimum evidence

- Agent Card versionado;
- risk assessment with justification;
- the evaluation report is reproduced;
- the security review and threat model of the use case;
- LGPD review where there has been personal data;
- the authorisation matrix;
- Traces, dashboards and alerts;
- budget and quotas;
- rollback plan;
- runbook operacional.

## Publication gates

| Gate | Condition |
|---|---|
| G1 — Design | Defined domain, contracts, data, dependencies and owner |
| G2 — Security/LGPD | approved classification, authorisation and threat model |
| G3 — Evaluation | the thresholds of the use case reached |
| G4 — Observability | validated telemetry and alerts |
| G5 — FinOps | Budget, quota and allocation configured |
| G6 — Operational readiness | runbook, capacity, backup and rollback tested |
| G7 — Go-live | the function segregation and final approval recorded |

## Quality thresholds

Thresholds are defined by use case and dataset.

| Other information | LOW | MEDIUM | HIGH | CRITICAL |
|---|---:|---:|---:|---:|
| Minimum groundedness for RAG | 0,80 | 0,85 | 0,90 | 0,95 |
| Minimum relevance | 0,75 | 0,80 | 0,85 | 0,90 |
| Maximum hallucination risk | 0,15 | 0,10 | 0,05 | 0,03 |
| Maximum toxicity | 0,05 | 0,03 | 0,02 | 0,01 |

Latency is not a risk threshold. It follows the workload class defined in nonfunctional requirements.

## Policy codes

Blocking controls shall be automated whenever possible:

- agent without owner or risk cannot be submitted;
- an unapproved tool cannot be linked;
- a HIGH/CRITICAL agent without an approved dataset may not be published;
- budget ausente bloqueia MEDIUM ou superior;
- the same identity cannot be submitted and approved;
- the published version is unchanged;
- The lack of policy results in `deny by default`.
