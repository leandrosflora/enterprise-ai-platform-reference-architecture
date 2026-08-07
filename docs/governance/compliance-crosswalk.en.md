# Crosswalk of Governance, Risk and Compliance

## Objective

Transform normative and market references into an operational matrix of controls, evidence, owners and gates of Enterprise AI Platform.

This crosswalk is a traceability tool. **It does not replace legal interpretation, certification audits, regulatory analysis, or a context-specific assessment of the organization.**

## How to use

1. select the controls applicable to the use case and the risk level;
2. associate each control with an owner and verifiable evidence;
3. automate enforcement when the condition is objective;
4. register exceptions, residual risk, deadline and compensatory control;
5. review the mapping when legislation, standard, architecture or purpose change.

## References covered

| Reference | Role in crosswalk |
|---|---|
| NIST AI RMF | Govern, Map, Measure and Manage functions to structure the risk cycle |
| ISO/IEC 42001 | management system, responsibilities, goals, controls and continuous improvement |
| ISO/IEC 27001 | Information security, Access Management, Suppliers, Incidents and Continuity |
| EU AI Act | risk classification and proportional obligations where applicable |
| LGPD | purpose, need, transparency, security, accountability and rights of the holder |
| OWASP for LLM applications | threats and technical tests of applications with generative models |

## Traceability matrix

| ID | Platform control | NIST AI RMF | ISO/IEC 42001 | AI Act | LGPD | Minimum evidence | Primary owner | Gate | Enforcement |
|---|---|---|---|---|---|---|---|---|---|
| CTRL-001 | purpose, sponsor and owner defined | Govern / Map | context, leadership and accountability | purpose and role of actors | purpose and accountability | Outcome Card, Agent Card, registered owner | Business Owner | Intake | automatic |
| CTRL-002 | Risk classification and impact | Map/ Govern | Risk assessment of AI | Classification and proportional obligations | Impact report where applicable | risk assessment versioned | AI Architect / Risk | Risk | hybrid |
| CTRL-003 | inventory and catalog of AI assets | Govern | inventory, documentation and operational control | Registry and documentation applicable | Registry of operations and accountability | AI Catalog with versions and owners | Platform Team | Intake / Release | automatic |
| CTRL-004 | classification, purpose and lineage of data | Map / Manage | Data governance for AI | data governance and quality | purpose, need and quality | data contract, lineage, classification and retention | Data Owner | Design | hybrid |
| CTRL-005 | immutable versioning of models, prompts, datasets, policies and tools | Govern/ Measure | Change control and documented information | Technical documentation and traceability | Responsibility and security | hashes, manifests and release bundle | Platform Team | Build/ Release | automatic |
| CTRL-006 | allowlist of models, sources, regions and tools | Govern / Manage | Operational controls and suppliers | risk-proportional requirements | Security and international transfer | policy and authorization decision | Security/ Platform | Design / Runtime | automatic |
| CTRL-007 | threat model and negative tests | Map/ Measure | risk management and control | robustness, security and cyber security | safety and prevention | threat model, red-team and attack results | Security | Assurance | hybrid |
| CTRL-008 | quality assessment, safety and regression | Measure | Monitoring, measurement and evaluation | accuracy, robustness and quality as applicable | quality and non-discrimination when applicable | dataset, baseline, thresholds and evaluation report | Model Risk/ Evaluation | Evaluation | automatic + human |
| CTRL-009 | human-in-the-loop and autonomy limits | Govern / Manage | roles, competence and operational control | if applicable | review of automated decisions | autonomy matrix, approvers and logs | Business Owner / Risk | Design / Runtime | hybrid |
| CTRL-010 | authorization by identity, tenant, resource and purpose | Govern / Manage | Access and operation controls | control and traceability | Security, need and access | authorization matrix and access tests denied | Security | Assurance / Runtime | automatic |
| CTRL-011 | provenance, citations and transparency of response | Map/ Measure | Communication and documented information | transparency and information to the user when applicable | transparency and quality | citations, checksum, source version and policy decision | Product / Data Owner | Evaluation/ Runtime | automatic |
| CTRL-012 | logging, tracing and correlated audit trail | Measure/ Manage | monitoring, internal audit and records | logging and risk documentation | Responsibility and security | traces, events, retention and audited access | SRE / Security | Observability | automatic |
| CTRL-013 | continuous monitoring and detection of drift | Measure/ Manage | monitoring, analysis and improvement | post-market when applicable | quality, safety and updating | dashboards, drift report and review triggers | Model Risk / Operations | Operate | automatic + human |
| CTRL-014 | incident management, suspension and rollback | Manage | non-conformity, corrective action and continuity | incidents and corrective actions where applicable | safety incident and mitigation | incident, decision, rollback and postmortem | Operations / Security | Operate | hybrid |
| CTRL-015 | budgets, quotas and unit economics | Govern / Manage | objectives, resources and operational control | proportionality and operational sustainability | need and indirect minimization of processing | budget, quota, task cost and blocks | FinOps / Product | FinOps | automatic |
| CTRL-016 | Supplier management and external models | Govern / Map / Manage | control of external suppliers and services | obligations between provider and deployer | Operators, transfer and security | due diligence, contract, region and exit plan | Procurement / Legal / Security | Design | human + policy |
| CTRL-017 | Re-evaluation after material change | Manage | change management and continuous improvement | re-assessment when there is relevant change | new purpose or relevant change | change record and new evidence bundle | AI Architect / Risk | Change | automatic + human |
| CTRL-018 | retention, exclusion and verifiable withdrawal | Manage | lifecycle, information control and improvement | withdrawal and documentation where applicable | retention, elimination and rights of the holder | retirement record, withdrawal and proof of exclusion | Data Owner / Operations | Withdraw | hybrid |

## Mapping by function of NIST AI RMF

### Govern

Main controls: CTRL-001, CTRL-002, CTRL-003, CTRL-005, CTRL-006, CTRL-009, CTRL-010, CTRL-015, CTRL-016.

Expected evidence:

- operating model and ICAR;
- approved policies;
- catalog of cases, agents, models and tools;
- risk classification;
- registration of exceptions and residual risk;
- governance indicators.

### Map

Main controls: CTRL-001, CTRL-002, CTRL-004, CTRL-007, CTRL-011, CTRL-016.

Expected evidence:

- purpose and context of use;
- population and impacted stakeholders;
- data sources and lineage;
- dependencies and suppliers;
- expected impacts and misuse scenarios.

### Measure

Main controls: CTRL-007, CTRL-008, CTRL-011, CTRL-012, CTRL-013.

Expected evidence:

- datasets and databases;
- functional, adverse and safety tests;
- metrics per dimension;
- observability and sampling;
- drift analysis and regression.

### Manage

Main controls: CTRL-006, CTRL-009, CTRL-010, CTRL-013, CTRL-014, CTRL-015, CTRL-017, CTRL-018.

Expected evidence:

- decisions to accept, mitigate or block;
- limits of autonomy;
- controlled rollout;
- incident response and rollback;
- re-evaluation and withdrawal.

## Applicability by risk level

| control | LOW | MEDIUM | HIGH | CRITICAL |
|---|---:|---:|---:|---:|
| Owner, purpose and catalog | Compulsory | Compulsory | Compulsory | Compulsory |
| Data lineage and classification | as data | Compulsory | Compulsory | Compulsory + independent review |
| Threat model | simplified | Compulsory | detailed | detailed + formal review |
| Evaluation | sample | dataset | dataset + baseline | Baseline + independent review |
| Human oversight | optional | by action | mandatory for critical actions | obligatory for permitted actions |
| Logging and audit | basic | complete | complete | complete + extended retention |
| Monitoring of drift | periodical | periodical | continuous by metrics | continuous + blocking triggers |
| Rollback and suspension | recommended | Compulsory | Compulsory and tested | obligatory, tested and independent |
| Re-evaluation | annual | half-year | quarterly or per event | continuous or by material event |

## Compliance evidence bundle

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

Not all artifacts need to use these formats, but the information should be identifiable, verified and traceable.

## Exceptions

An exception shall register:

- control not met;
- justification and impact;
- residual risk;
- compensatory control;
- owner and independent approver;
- expiry date;
- condition of withdrawal;
- evidence and traceable ticket.

Exception without a deadline or owner is invalid. Legal or regulatory controls cannot be waived solely through a technical decision.

## Maintenance cadence

Review the crosswalk:

- at least every quarter for references and internal policies;
- after a relevant regulatory change;
- after material incident;
- when a new class of agent, model or autonomy is introduced;
- when an audit identifies an evidence or enforcement gap.
