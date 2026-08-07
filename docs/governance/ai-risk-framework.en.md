# AI Risk Framework

## Objective

To classify risks of AI, to define proportional controls and to establish verifiable evidence for publication and operation.

## Categories

| Category | Examples |
|---|---|
| Security | Prompt injection, tool abuse, exfiltration, excessive agency. |
| Privacy and compliance | LGPD, retention, consent, international transfer. |
| operational | Unavailability, integration failures, model degradation. |
| Model | Hallucination, bias, toxicity, regression and low explainability. |
| Financial party | Unexpected consumption, lack of quotas and chargeback. |
| Reputacional | Inadequate responses and opaque decisions. |

## Classification

| Level | Criteria |
|---|---|
| LOW | Internal use, no sensitive data, no transactional action. |
| MEDIUM | Internal/confidential data, RAG or support for human decision. |
| HIGH | Personal/sensitive data, writing tool or relevant operational impact. |
| CRITICAL | Automated regulated decision, material impact on customer, financial or legal. |

## Risk matrix and controls

| Risk | Standard severity | Compulsory controls | Evidence |
|---|---:|---|---|
| Direct/indirect prompt injection | HIGH | Instruction segmentation, content scanning, tool allowlist, adversarial evaluation | attack tests and blocking logs |
| Data leakage | CRITICAL | classification, masking, tenant isolation, DLP, output filtering | isolation test and classification report |
| Tool abuse | HIGH | minimum scopes, policy enforcement, inadequacy, human approval | approved contract, authorisation matrix, events |
| Excessive agency | HIGH | limits of autonomy, transaction boundary, human-in-the-loop | blockage and rollback scenarios |
| Hallucination | MEDIUM | RAG, citations, groundedness, fallback | dataset and assessment report |
| Poisoned knowledge | HIGH | provenance, quarantine, source approval, controlled re-indexation | checksum, lineage and malicious content test |
| Memory poisoning | HIGH | origin of facts, TTL, confirmation, user isolation | cross-contamination tests |
| Bias | HIGH | review of dataset, fairness where applicable, human review | Criteria and report |
| Use of data without a legal basis | CRITICAL | purpose, minimisation, retention and approval LGPD | IAD/ALI when applicable |
| Provider outage | MEDIUM | timeout, circuit breaker, bulkhead, fallback | resilience test and runbook |
| Unexpected cost | MEDIUM | quotas, budgets, rate limits, alerts and blocks | dashboard and limit test |
| Lack of traceability | HIGH | trace context, audit trail, retention and policy version | trace and audit event |
| Quality requirement | MEDIUM | baseline, regression dataset and gate de deploy | comparative report |
| Inappropriate access to KB | HIGH | ACL per document/chunk, ABAC and server-side filters | Access test denied |

## Level controls

| control | LOW | MEDIUM | HIGH | CRITICAL |
|---|---:|---:|---:|---:|
| Owner definido | Obligatory | Obligatory | Obligatory | Obligatory |
| Automatic assessment | Obligatory | Obligatory | Obligatory | Obligatory |
| AI Architect Review | Option | Obligatory | Obligatory | Obligatory |
| Security review | According to scope | According to scope | Obligatory | Obligatory |
| LGPD Review | According to data | According to data | Obligatory | Obligatory |
| Legal/Regulatory | No | according to scope | according to scope | Obligatory |
| Audit | Basic | Complete | Complete | Complete + extended retention |
| Human-in-the-loop | No | According to action | Obligation for critical writing | Obligatory |
| Rollback | Recommended | Recommended | Obligatory | Obligatory |
| FinOps budget | Recommended | Obligatory | Obligatory | Obligatory + blockade |

## Minimum evidence

- Agent Card versioned;
- risk assessment with justification;
- reproducible evaluation report;
- security review and threat model of the case of use;
- LGPD review when there is personal data;
- authorisation matrix;
- traces, dashboards and alerts;
- budget and quotas;
- rollback plane;
- runbook operational.

## Publication banks

| Gate | Condition |
|---|---|
| G1 — Design | domain, contracts, data, dependencies and owner defined |
| G2 — Security/LGPD | approved classification, authorisation and threat model |
| G3 — Evaluation | thresholds of the case of use achieved |
| G4 — Observability | telemetry and validated warnings |
| G5 — FinOps | budget, quota and allocation |
| G6 — Operational readiness | runbook, capacity, backup and rollback tested |
| G7 — Go-live | Segregation of function and final approval recorded |

## Quality Thresholds

Thresholds are defined by case of use and dataset.

| Metrics | LOW | MEDIUM | HIGH | CRITICAL |
|---|---:|---:|---:|---:|
| Minimum Groundedness for RAG | 0.80 | 0.85 | 0.90 | 0.95 |
| Minimum relevance | 0,75 | 0,80 | 0,85 | 0,90 |
| Maximum hallucination risk | 0.15 | 0.10 | 0.05 | 0.03 |
| Toxicity maximum | 0,05 | 0,03 | 0,02 | 0,01 |

Latency is not a risk threshold, it follows the class of workload defined in non-functional requirements.

## Policy as code

Blocking controls should be automated whenever possible:

- agent without owner or risk cannot be subjected to;
- non-approved tool cannot be linked;
- HIGH/CRITICAL agent without approved dates cannot be published;
- Absent budget blocks MEDIUM or higher;
- the same identity may not submit and approve;
- published version is unchangeable;
- non-existent policy results in `deny by default`.
