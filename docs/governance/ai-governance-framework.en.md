# Enterprise AI Governance Framework

## Objet

Determine how the organisation decides, approves, publishes, monitors and withdraws the AI solutions with clear and audited responsibility.

## Operative model

```mermaid
flowchart LR
    A[Demandante] --> B[AI Intake]
    B --> C[Risk Classification]
    C --> D[Architecture and Data Review]
    D --> E[Security, Privacy and Legal]
    E --> F[Evaluation Gate]
    F --> G[Release Approval]
    G --> H[Continuous Monitoring]
    H --> I[Reassessment or Retirement]
```

## Decision structure

| Papel | Responsabilidade |
|---|---|
| Business Owner | finality, benefit, impact and acceptance of residual risk |
| Product Owner | backlog, methods and experience of user |
| AI Architect | patterns, architecture, autonomia and integration |
| Data Owner | quality, access, finality and retention of data |
| Security | threat model, controls and response to incidents |
| Privacy / DPO | LGPD, legal basis, minimisation and rights of the owner |
| Legal / Compliance | regulatory, contractual and intellectual property obligations |
| Model Risk / Evaluation | methodology, datasets, thresholds and independence of evaluation |
| Platform Team | Guardrails, gateways, observability and policy the code |
| Operations | SLO, runbook, capacidade, continuidade e rollback |

## Artefatos governados

- AI use case, finalidade e Outcome Card;
- Agent Card ou Model Card;
- risk assessment;
- ADRs for architecture and model selection;
- data sources, data contracts and lineage;
- datasets, prompts, models, embeddings, tools and modified policies;
- knowledge snapshot e release manifest;
- golden dataset e evaluation report;
- threat model e privacy assessment;
- approvals, exemptions and residual risks;
- dashboards, incidents and withdrawal plan.

The detailed lifecycle of these assets is in [Data, Model, Prompt and Knowledge Lifecycle](model-lifecycle.md).

## Gates

| Gate | Entrada | Sahara |
|---|---|---|
| Intake | problema e sponsor | caso registrado e owner definido |
| Risk | impact, data and autonomy | LOW-CRITICAL classification |
| Design | architecture and contracts | ADRs and controls defined |
| Assurance | security, privacy, legal e evaluation | evidence and penalties |
| Release | readiness operacional | approved and imutable version |
| Operate | telemetria e feedback | monitoring and correctional actions |
| Retire | Decision of enlargement | access to unused, processed data and evidence provided |

## Adjustment of frameworks

| Reference | Application |
|---|---|
| NIST AI RMF | Go, Map, Measure and Manage as risk cycle |
| ISO/IEC 42001 | system of management of AI, paediatrics, controls and improvement of the content |
| ISO 27001 | Information security checks |
| LGPD | finality, need, transparency, security and rights of the owner |
| EU AI Act | risk classification and appropriate obligations when applicable |
| OWASP LLM | threat model and security tests for applications with LLM |

The above is conceptual. The operational rastreability between control, normative function, evidence, owner, gate and enforcement is in the [Government Crosswalk, Risco and Compliance](compliance-crosswalk.md).

## Control rassurability

Each applicable control shall be possible:

- stable identification;
- reference to the risk treated;
- owner and approver when applicable;
- minimum evidence;
- gate where it is checked;
- automatician, human or hybrid enforcement;
- exemption and expiry rule;
- indicator of effectiveness.

Documentation without evidence or enforcement is not considered to be implemented.

## Excusements

Excusements must be possible:

- unattended and justified control;
- risco residual e impacto;
- compensation control;
- owner e aprovador independente;
- time of validity;
- condition of revocation;
- evidence and a rastreable ticket.

Excusement without expiry date is invariable.

## Policy the code

Automated target controls:

- block artefacts without ownership or classification;
- preventing unapproved model, source or tool;
- require risk assessment and thresholds;
- validating function separation;
- to apply budgets, quotas and autonomous limits;
- keep copies published in exchange for;
- - I'll be able to negate by way of a time when there's no policy.

## Government indicators

- time of approval at risk level;
- percentage of solutions with full evidence;
- the coverage of crosswalk control;
- automated controls and manuals;
- open and vengeable exceptions;
- relapses and incidents by version;
- assessment coverage and network coverage;
- time for rollback or deactivation;
- percentage of models, prompts and tools out of the pattern;
- cost for use and for final task.
