# AI Risk Framework

## Objective

To classify risks of AI, to define proportional controls and to establish verifiable evidence for publication and operation.

## Categorias

| Categoria | Examples |
|---|---|
| Security | Prompt injection, tool abuse, exfiltration, excessive agency. |
| Privacidade e compliance | LGPD, retention, consent, international transfer. |
| Operacional | Unavailability, integration failures, model degradation. |
| Model | Hallucination, bias, toxicity, regression and low explanability. |
| Financeiro | Unexpected consumption, lack of quotas and chargeback. |
| Reputacional | Inadequate responses and opaque decisions. |

## Classification

| Level | Criteria |
|---|---|
| LOW | Internal use, no sensitive data, no transactional action. |
| MEDIUM | Internal/confidential data, AGR or support for human decision. |
| HIGH | Personal/sensitive data, writing tool or relevant operational impact. |
| CRITICAL | Automated regulated decision, material impact on customer, financial or legal. |

## Risk matrix and controls

| Risk | Standard severity | Compulsory controls | Evidence |
|---|---:|---|---|
| Direct/indirect prompt injection | HIGH | Instruction segmentation, content scanning, tool allowlist, adversarial evaluation | testes de ataque e logs de bloqueio |
| Data leakage | CRITICAL | classification, masking, tenant isolation, DLP, output filtering | isolation test and classification report |
| Tool abuse | HIGH | minimum scopes, policy enforcement, inadequacy, human approval | approved contract, authorisation matrix, events |
| Excessive agency | HIGH | limites de autonomia, transaction boundary, human-in-the-loop | blockage and rollback scenarios |
| Hallucination | MEDIUM | RAG, citations, groundedness, fallback | dateset and assessment report |
| Poisoned knowledge | HIGH | provenance, quarantine, source approval, controlled re-indexation | checksum, lineage and malicious content test |
| Memory poisoning | HIGH | origin of facts, TTL, confirmation, user isolation | cross-contamination tests |
| Bias | HIGH | review of dateset, fairness where applicable, human review | Criteria and report |
| Uso de dado sem base legal | CRITICAL | purpose, minimisation, retention and approval LGPD | IAD/ALI when applicable |
| Provider outage | MEDIUM | timeout, circuit breaker, bulkhead, fallback | resilience test and runbook |
| Unexpected cost | MEDIUM | quotas, budgets, rate limits, alertas e bloqueio | dashboard e teste de limite |
| Falta de rastreabilidade | HIGH | trace context, audit trail, retention and policy version | trace e evento de auditoria |
| Quality requirement | MEDIUM | baseline, regression dataset e gate de deploy | comparative report |
| Acesso indevido a KB | HIGH | ACL por documento/chunk, ABAC e filtros server-side | teste de acesso negado |

## Level controls

| Controle | LOW | MEDIUM | HIGH | CRITICAL |
|---|---:|---:|---:|---:|
| Owner definido | Obligatory | Obligatory | Obligatory | Obligatory |
| Automatic assessment | Obligatory | Obligatory | Obligatory | Obligatory |
| AI Architect Review | Option | Obligatory | Obligatory | Obligatory |
| Revisão Security | Conforme escopo | Conforme escopo | Obligatory | Obligatory |
| LGPD Review | According to data | According to data | Obligatory | Obligatory |
| Legal/Regulatory | No | Conforme escopo | Conforme escopo | Obligatory |
| Auditoria | Basic | Completa | Completa | Complete + extended retention |
| Human-in-the-loop | No | According to action | Obligation for critical writing | Obligatory |
| Rollback | Recommended | Recommended | Obligatory | Obligatory |
| FinOps budget | Recommended | Obligatory | Obligatory | Obligatory + blockade |

## Minimum evidence

- Agent Card versionado;
- risk assessment com justificativa;
- reproducible evaluation report;
- security review e threat model do caso de uso;
- LGPD review quando houver dado pessoal;
- authorisation matrix;
- traces, dashboards e alertas;
- budget e quotas;
- plano de rollback;
- runbook operacional.

## Publication banks

| Gate | Condition |
|---|---|
| G1 — Design | domain, contracts, data, dependencies and owner defined |
| G2 — Security/LGPD | approved classification, authorisation and threat model |
| G3 — Evaluation | thresholds do caso de uso atingidos |
| G4 — Observability | telemetria e alertas validados |
| G5 — FinOps | budget, quota and allocation |
| G6 — Operational readiness | runbook, capacity, backup and rollback tested |
| G7 — Go-live | Segregation of function and final approval recorded |

## Quality Thresholds

Thresholds are defined by case of use and dateset.

| Metrics | LOW | MEDIUM | HIGH | CRITICAL |
|---|---:|---:|---:|---:|
| Minimum Groundedness for AGR | 0,80 | 0,85 | 0,90 | 0,95 |
| Minimum relevance | 0,75 | 0,80 | 0,85 | 0,90 |
| Hallucination risk máximo | 0,15 | 0,10 | 0,05 | 0,03 |
| Toxicity maximum | 0,05 | 0,03 | 0,02 | 0,01 |

Latency is not a risk threshold, it follows the class of workload defined in non-functional requirements.

## Policy as code

Blocking controls should be automated whenever possible:

- agent without owner or risk cannot be subjected to;
- non-approved tool cannot be linked;
- HIGH/CRITICAL agent without approved dates cannot be published;
- budget ausente bloqueia MEDIUM ou superior;
- the same identity may not submit and approve;
- published version is unchangeable;
- non-existent policy results in `deny by default`.
