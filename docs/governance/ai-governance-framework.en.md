# Enterprise AI Governance Framework

## Objective

Defining how the organization decides, approves, publishes, monitors and withdraws AI solutions with clear responsibilities and auditable evidence.

## Operational model

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
| Business Owner | the purpose, benefit, impact and acceptance of residual risk; |
| Product Owner | Backlog, metrics and user experience |
| AI Architect | The Commission shall adopt delegated acts in accordance with the opinion of the Standing Committee on Planning and Development. |
| Data Owner | quality, access, purpose and retention of data |
| Security | threat model, controls and incident response |
| Privacy / DPO | LGPD, legal basis, minimisation and rights of the holder |
| Legal / Compliance | The Commission shall adopt delegated acts in accordance with Article 21 of Regulation (EU) No 182/2011 and in accordance with Article 21 thereof. |
| Model Risk / Evaluation | the methodology, datasets, thresholds and independence of the assessment; |
| Platform Team | guardrails, gateways, observability and policy code |
| Operations | SLO, runbook, capacity, continuity and rollback |

## Artefatos governados

- AI use case, purpose and outcome card;
- Agent Card ou Model Card;
- risk assessment;
- architecture ADRs and model selection;
- data sources, data contracts and lineage;
- data sets, prompts, templates, embeddings, tools and versioned policies;
- knowledge snapshot and release manifest;
- the golden dataset and evaluation report;
- threat model and privacy assessment;
- approvals, exceptions and residual risks;
- dashboards, incidents and withdrawal plan.

The detailed lifecycle of these assets is in [Data, Model, Prompt and Knowledge Lifecycle](model-lifecycle.md).

## Gates

| Gate | Entrada | Exit |
|---|---|---|
| Intake | Problem and sponsor | Registered case and defined owner |
| Risk | Impact, data and autonomy | low to critical ratings |
| Design | architecture and contracts | Defined ADRs and controls |
| Assurance | Security, privacy, legal and evaluation | Evidence and pending |
| Release | readiness operacional | approved and unchanging version |
| Operate | telemetry and feedback | monitoring and corrective actions |
| Retire | closing decision | Withdrawn access, processed data and preserved evidence |

## Alignment to frameworks

| Reference | Application of this Regulation |
|---|---|
| NIST AI RMF | Governance, Map, Measure and Manage as a Risk Cycle |
| ISO/IEC 42001 | AI management system, roles, controls and continuous improvement |
| ISO 27001 | information security controls |
| LGPD | purpose, necessity, transparency, security and rights of the holder |
| EU AI Act | risk classification and proportional liabilities where applicable |
| OWASP LLM | threat model and security tests for applications with LLM |

The operational traceability between control, regulatory function, evidence, owner, gate and enforcement is in the[Crosswalk of governance, risk and compliance](compliance-crosswalk.md).

## Traceability of control

Each applicable control shall have:

- a stable identifier;
- reference to the risk treated;
- owner and approval authority where applicable;
- the minimum evidence;
- the gate at which it is checked;
- automatic enforcement, human or hybrid;
- the exception and expiry rule;
- the effectiveness indicator.

Documentation without evidence or enforcement is not considered enforced control.

## Exceptions

Exceptions shall include:

- unattended and justified checks;
- residual risk and impact;
- compensatory control;
- the owner and independent authorising officer;
- the period of validity;
- the condition of revocation;
- evidence and traceable ticket.

Exception without expiry date is invalid.

## Policy codes

Automate targeted controls:

- blocking an artifact without owner or classification;
- prevent an unapproved model, source or tool;
- require assessment and thresholds by risk level;
- validate function segregation;
- apply budgets, quotas and autonomy limits;
- keep published versions unchanged;
- Denying by default when there's no politics.

## Governance indicators

- time of approval by risk level;
- percentage of solutions with full evidence;
- coverage of crosswalk controls;
- automated or manual controls;
- open and expired exceptions;
- Regressions and incidents per version;
- evaluation coverage and networking;
- rollback or deactivation time;
- percentage of models, prompts and off-the-shelf tools;
- cost per use case and per completed task.
