# Crosswalk of governance, risk and compliance

## Objective

Transform regulatory and market references into an operational matrix of Enterprise AI Platform controls, evidence, owners and gates.

This crosswalk is a traceability tool and does not replace legal interpretation, certification auditing, regulatory analysis or context-specific assessment of the organisation.

## How to use

1. select the controls applicable to the use case and risk level;
2. associate each control with an owner and verifiable evidence;
3. automate enforcement where the condition is objective;
4. record exceptions, residual risk, maturity and compensatory control;
5. review the mapping when legislation, norm, architecture or purpose changes.

## Covered references

| Reference | Paper on the crosswalk |
|---|---|
| NIST AI RMF | Govern, Map, Measure and Manage functions to structure the risk cycle |
| ISO/IEC 42001 | the management system, responsibilities, objectives, controls and continuous improvement; |
| ISO/IEC 27001 | information security, access management, suppliers, incidents and continuity |
| EU AI Act | risk classification and proportional liabilities where applicable |
| LGPD | purpose, necessity, transparency, security, accountability and rights of the holder |
| OWASPfor applications with LLM | Threats and technical testing of applications with generative models |

## Traceability matrix

| ID | Platform control | NIST AI RMF | ISO/IEC 42001 | EU AI Act | LGPD | Minimum evidence | Primary owner | Gate | Enforcement |
|---|---|---|---|---|---|---|---|---|---|
| CTRL-001 | Defined purpose, sponsor and owner | Govern / Map | context, leadership and accountability | purpose and role of the actors | purpose and accountability | Outcome Card, Agent Card, owner registrado | Business Owner | Intake | automatically |
| CTRL-002 | risk classification and impact | Map / Govern | the risk assessment of AI; | Classification and proportional obligations | impact report where applicable | risk assessment versionado | AI Architect / Risk | Risk | Other, not further worked than hot rolled |
| CTRL-003 | inventory and catalogue of AI assets | Govern | inventory, documentation and operational control | Registration and applicable documentation | recording of operations and accountability | AI Catalog with versions and owners | Platform Team | Intake / Release | automatically |
| CTRL-004 | classification, purpose and lineage of the data | Map / Manage | Data governance for AI | date governance and quality | purpose, necessity and quality | Date contract, lineage, classification and retention | Data Owner | Design | Other, not further worked than hot rolled |
| CTRL-005 | Unchanged model, prompt, dataset, policy and tool versioning | Govern / Measure | change control and documented information | technical documentation and traceability | accountability and security | hashes, manifests and release bundle | Platform Team | Build / Release | automatically |
| CTRL-006 | allowlist of models, sources, regions and tools | Govern / Manage | Operational controls and suppliers | risk-proportionate requirements | Security and international transfer | policy version and authorisation decision | Security / Platform | Design / Runtime | automatically |
| CTRL-007 | threat model and negative tests | Map / Measure | Risk management and controls | robustness, security and cyber security | Safety and prevention | threat model, red-team and attack results | Security | Assurance | Other, not further worked than hot rolled |
| CTRL-008 | quality, safety and regression evaluation | Measure | monitoring, measurement and evaluation | accuracy, robustness and quality as applied | quality and non-discrimination where applicable | the data set, baseline, thresholds and evaluation report; | Model Risk / Evaluation | Evaluation | Automatic + human |
| CTRL-009 | human-in-the-loop and autonomy limits | Govern / Manage | roles, competence and operational control | human supervision where applicable | review of automated decisions | Autonomy matrix, approvers and logs | Business Owner / Risk | Design / Runtime | Other, not further worked than hot rolled |
| CTRL-010 | authorisation by identity, tenant, resource and purpose | Govern / Manage | Access and operation controls | Control and traceability | security, necessity and access | authorisation matrix and denied access tests | Security | Assurance / Runtime | automatically |
| CTRL-011 | the provenance, citations and transparency of the response | Map / Measure | Communication and documented information | transparency and information to the user where applicable | transparency and quality | The Commission shall adopt delegated acts in accordance with the opinion of the Standing Committee on Planning and Development. | Product / Data Owner | Evaluation / Runtime | automatically |
| CTRL-012 | logging, tracing and related audit trail | Measure / Manage | monitoring, internal audit and records | logging and documentation at risk | accountability and security | Traces, events, retention and access audited | SRE / Security | Observability | automatically |
| CTRL-013 | continuous monitoring and drift detection | Measure / Manage | monitoring, analysis and improvement | Post-market where applicable | quality, safety and updating | The Commission shall adopt delegated acts in accordance with Article 21 of Regulation (EU) No 182/2011 and in accordance with Article 21 thereof. | Model Risk / Operations | Operate | Automatic + human |
| CTRL-014 | Incident management, suspension and rollback | Manage | non-compliance, corrective action and continuity | incidents and corrective actions where applicable | Safety and mitigation incident | Incident, decision, rollback and postmortem | Operations / Security | Operate | Other, not further worked than hot rolled |
| CTRL-015 | Budget, quotas and unit economics | Govern / Manage | objectives, resources and operational control | proportionality and operational sustainability | need for and indirect minimisation of processing | Budget, quota, cost per task and blocks | FinOps / Product | FinOps | automatically |
| CTRL-016 | Management of external suppliers and models | Govern / Map / Manage | control of external suppliers and services | obligations between provider and deployer | Operators, transfer and security | due diligence, contract, region and exit plan | Procurement / Legal / Security | Design | humano + policy |
| CTRL-017 | reassessment after material change | Manage | change management and continuous improvement | new evaluation when there is a relevant change | new purpose or relevant change | Change record and new evidence bundle | AI Architect / Risk | Change | Automatic + human |
| CTRL-018 | verifiable retention, exclusion and withdrawal | Manage | Lifecycle, information control and improvement | withdrawal and documentation where applicable | retention, disposal and rights of the holder | Retirement record, revocation and proof of exclusion | Data Owner / Operations | Retire | Other, not further worked than hot rolled |

## Mapping by function of NIST AI RMF

### Govern

This Regulation shall be binding in its entirety and directly applicable in all Member States.

Expected evidence:

- operating model and RACI;
- policies adopted;
- a catalogue of cases, agents, models and tools;
- the risk classification;
- the recording of exceptions and residual risk;
- governance indicators.

### Map

This Regulation shall be binding in its entirety and directly applicable in all Member States.

Expected evidence:

- purpose and context of use;
- population and stakeholders affected;
- data sources and lineage;
- dependencies and suppliers;
- expected impacts and misuse scenarios.

### Measure

This Regulation shall enter into force on the twentieth day following that of its publication in the Official Journal.

Expected evidence:

- data sets and baselines;
- functional, adverse and safety tests;
- metrics by size;
- Observability and sampling;
- drift and regression analysis.

### Manage

This Regulation shall be binding in its entirety and directly applicable in all Member States.

Expected evidence:

- decisions on acceptance, mitigation or blocking;
- limits of autonomy;
- rollout controlado;
- incident response and rollback;
- reassessment and withdrawal.

## Applicability by risk level

| Controle | LOW | MEDIUM | HIGH | CRITICAL |
|---|---:|---:|---:|---:|
| Owner, purpose and catalogue | compulsory | compulsory | compulsory | compulsory |
| Date lineage and classification | according to data | compulsory | compulsory | compulsory + independent review |
| Threat model | simplificado | compulsory | detalhado | Detailed + formal review |
| Assessment | amostra | dataset | dataset + baseline | Baseline + independent review |
| Human oversight | opcional | by share | mandatory for critical actions | compulsory for permitted actions |
| Logging and auditing | basic | completo | completo | Full + extended retention |
| Monitoring of drift | periodical | periodical | continuous by metric | Continuous + blocking triggers |
| Rollback and suspension | recommended | compulsory | Compulsory and tested | Compulsory, tested and independent |
| Reassessment | anual | semestral | quarterly or per event | continuous or per material event |

## Evidence bundle of compliance

```text
outcome-card.yaml
agent-card.yaml
risk-assessment.yaml
data-contracts/
lineage.json
architecture/
adrs/
model-manifest.json
prompt-manifest.json
dataset-manifest.json
policy-bundle/
threat-model.md
security-tests.json
evaluation-report.json
human-oversight-plan.md
observability-evidence.json
supplier-assessment.md
approval-decision.json
release-manifest.json
runbook.md
retirement-record.json
```

Not all artifacts need to use these formats, but the information must be identifiable, versioned and traceable.

## Exceptions

An exception shall record:

- unattended control;
- justification and impact;
- risco residual;
- compensatory control;
- the owner and independent authorising officer;
- the expiry date;
- the condition of revocation;
- evidence and traceable ticket.

Exemption without deadline or owner is invalid.

## Maintenance cadence

Check out the crosswalk:

- at least quarterly for internal references and policies;
- after a relevant regulatory change;
- after a material incident;
- when a new agent class, model or autonomy is introduced;
- when the audit identifies a lack of evidence or enforcement.
