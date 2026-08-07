# Crosswalk of Governance, Risco and Compliance

## Objet

Transform normative and market references into an operational matrix of checks, evidence, owners and gates of Enterprise AI Platform.

This crosswalk is a rasterable tool. It ** does not replace legal interpretation, certification audit, regulatory analysis or specific evaluation of the organisation's context**.

## How to use

1. select the controls applicable to the case of use and risk level;
2. to associate each control to a owner and a verified evidence;
3. automate enforcement when the condition is objective;
4. registres excercises, residual risk, time limit and compensation control;
5. Review the map when legislation, rules, architecture or finality change.

## Covered references

| Reference | Crosswalk |
|---|---|
| NIST AI RMF | Functions Govern, Map, Measure and Manage to structure the risk cycle |
| ISO/IEC 42001 | management system, responsibility, objectives, controls and improvement of the content |
| ISO/IEC 27001 | information security, access management, suppliers, incidents and continuity |
| EU AI Act | risk classification and appropriate obligations when applicable |
| LGPD | finality, need, transparency, safety, responsibility and rights of the owner |
| OWASP for applications with LLM | Technical threats and testing of applications with generic models |

## Raster slack

| ID | Control of the plate | NIST AI RMF | ISO/IEC 42001 | EU AI Act | LGPD | Minimum evidence | Primary owner | Gate | Enforcement |
|---|---|---|---|---|---|---|---|---|---|
| CTRL-001 | finalidade, sponsor e owner definidos | Govern / Map | context, leadership and accountability | the finality and role of the attackers | finality and responsibility | Outcome Card, Agent Card, owner registrado | Business Owner | Intake | automagnetic |
| CTRL-002 | Risk and impact classification | Map / Govern | risk assessment | classification and appropriate obligations | impact report when applicable | risk assessment versionado | AI Architect / Risk | Risk | hybrid |
| CTRL-003 | Inventory and catalog of A activity | Govern | invention, documentation and operational control | registre and documentation applicable | registre of operations and accountability | AI Catalog with versions and owners | Platform Team | Intake / Release | automagnetic |
| CTRL-004 | classification, finality and line of data | Map / Manage | Data administration for A | data governance e qualidade | finalidade, necessidade e qualidade | date contract, lineage, classification and retention | Data Owner | Design | hybrid |
| CTRL-005 | imutable model version, prompt, dataset, policy and tool | Govern / Measure | Change control and documentation | Technical documentation and rastreability | responsibility and security | hashes, manifests e release bundle | Platform Team | Build / Release | automagnetic |
| CTRL-006 | allowlist of models, sources, regions and tools | Govern / Manage | operational controls and suppliers | appropriate risk requirements | international security and transfer | version of policy and authorisation decision | Security / Platform | Design / Runtime | automagnetic |
| CTRL-007 | threat model e testes negativos | Map / Measure | risk management and controls | robustness, safety and safety | security and prevention | threat model, team and attack results | Security | Assurance | hybrid |
| CTRL-008 | quality assessment, safety and return | Measure | monitoring, measurement and evaluation | requirements, robustness and quality in accordance with application | quality and not discrimination when applicable | dataset, baseline, thresholds e evaluation report | Model Risk / Evaluation | Evaluation | automatician + human |
| CTRL-009 | human-in-the-loop and autonomial limits | Govern / Manage | paper, competence and operational control | human supervision when applicable | Review of automated decisions | autonomial, aprovators and logs | Business Owner / Risk | Design / Runtime | hybrid |
| CTRL-010 | Authorisation by identity, tenant, resource and finality | Govern / Manage | access control and operation | controle e rastreabilidade | security, need and access | unauthorized and illegal access tests | Security | Assurance / Runtime | automagnetic |
| CTRL-011 | origin, mentions and transparency of response | Map / Measure | communication and information documented | transparency and information to the user when applicable | transparency and quality | citations, checksum, source version and policy decision | Product / Data Owner | Evaluation / Runtime | automagnetic |
| CTRL-012 | logging, tracing e audit trail correlacionado | Measure / Manage | monitoramento, auditoria interna e registros | logging and documenting conforming risk | responsibility and security | trace, events, retention and audited access | SRE / Security | Observability | automagnetic |
| CTRL-013 | Continuous monitoring and drift detection | Measure / Manage | monitoring, analysis and improvement | ps-market when applicable | quality, safety and updating | dashboards, report drift and review tyres | Model Risk / Operations | Operate | automatician + human |
| CTRL-014 | incident management, suspension and rollback | Manage | not conformity, retracted action and continuity | incidents and corrections when applicable | incident of safety and mitigation | incident, decision, rollback and postmortem | Operations / Security | Operate | hybrid |
| CTRL-015 | budgets, quotas e unit economics | Govern / Manage | objetivos, recursos e controle operacional | proporcionalidade e sustentabilidade operacional | necessary and minimalisation of the indirection of processing | budget, quota, cost per tonne and blockages | FinOps / Product | FinOps | automagnetic |
| CTRL-016 | management of external suppliers and models | Govern / Map / Manage | control of suppliers and external services | obligations between provider and deployer | operators, transfer and security | due diligence, contract, region and exit plan | Procurement / Legal / Security | Design | humano + policy |
| CTRL-017 | re-evaluation after material change | Manage | Change management and improvement management | new assessment when relevant change is made | new finality or relevant amendment | change record e novo evidence bundle | AI Architect / Risk | Change | automatician + human |
| CTRL-018 | retention, exclusion and re-examined | Manage | lifecycle, information control and improvement | withdrawn and documenting when applicable | retention, elimination and rights of the owner |                                                                                                                                                                                                 | Data Owner / Operations | Retire | hybrid |

## Map by NIST AI RMF

### Govern

- Main controls: CTRL-001, CTRL-002, CTRL-003, CTRL-005, CTRL-006, CTRL-009, CTRL-010, CTRL-015, CTRL-016.

Evidences gathered:

- operating model e RACI;
- adopted policies;
- catalogue of cases, agents, models and tools;
- risk classification;
- a record of excise and residual risk;
- Government indicators.

### Map

Main controls: CTRL-001, CTRL-002, CTRL-004, CTRL-007, CTRL-011, CTRL-016.

Evidences gathered:

- the finality and context of use;
- the population and stakeholders affected;
- sources of data and lineage;
- dependents and suppliers;
- hoped impact and undefensible use scenarios.

### Measure

Pricipal checks: CTRL-007, CTRL-008, CTRL-011, CTRL-012, CTRL-013.

Evidences gathered:

- datasets e baselines;
- functional, adversarial and security tests;
- dimensions;
- observation and sampling;
- drift and return analysis.

### Manage

- Main controls: CTRL-006, CTRL-009, CTRL-010, CTRL-013, CTRL-014, CTRL-015, CTRL-017, CTRL-018.

Evidences gathered:

- accept, mitigate or block decisions;
- limits of autonomy;
- rollout controlado;
- incident response e rollback;
- re-evaluation and withdrawal.

## Risk level application

| Controle | LOW | MEDIUM | HIGH | CRITICAL |
|---|---:|---:|---:|---:|
| Owner, finality and catalog | obligation | obligation | obligation | obligation |
| Date line and classification | according to data | obligation | obligation | obligation + independent review |
| Threat model | simplificado | obligation | detalhado | detail + formal review |
| Assessment | amostra | dataset | dataset + baseline | baseline + independent review |
| Human oversight | opcional | by action | obligation for critical actions | obligation for permitted actions |
| Logging e auditoria | básico | completo | completo | complete + retention inserted |
| drift monitoring | periodic | periodic | content by methods | cuff + bloke shit |
| Rollback and suspension | recomendado | obligation | obligation and testimony | obligatory, tested and independent |
| Revaluation | anual | semestral | trimestrial or event | content or by material event |

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

Not all artefacts need to use these formats, but the information must be identified, updated and rastreable.

## Excusements

A exception must be registered:

- unattended control;
- justificativa e impacto;
- risco residual;
- compensation control;
- owner e aprovador independente;
- expiry time;
- condition of revocation;
- evidence and a rastreable ticket.

No time or owner is invariable. Legal or regulatory checks cannot be withdrawn only by technical decision.

## Maintenance department

Check the crosswalk:

- at least quarterly for internal references and policies;
- after relevant regulatory change;
- after material incident;
- when a new agent, model or autonomy class is introduced;
- when the auditor identified evidence or enforcement.
