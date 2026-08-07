# 8. Maturity model and adoption roadmap

## Principle

The maturity of a Platform IA is not defined by the number of services implemented; it is demonstrated by the ability to deliver cases of use with quality, control, operation and predictable cost.

## Maturity model

### Level 0 — Isolated experiments

**Characteristics**

- notebooks, scripts and SaaS without common standards;
- Credentials and local settings;
- pouca rastreabilidade;
- manual evaluation;
- costs not allocated;
- knowledge and prompts copied between projects.

**Objective to move forward**

To identify repeated patterns, owners and material risks.

### Level 1 — Minimum standards

**Characteristics**

- templates de projeto;
- appropriate identity and secrets;
- basic logging;
- initial case inventory;
- approved providers and models;
- publication checklist.

**Maturity evidence**

First low-risk cases reach production without ad hoc controls.

### Level 2 — Implementable Golden path

**Characteristics**

- Agent Registry e ciclo de vida;
- Model Gateway;
- contracts and events funded;
- IC/CD with evaluations and policies;
- tip-to-end observability;
- runbooks e rollback;
- first service of knowledge or tools.

**Maturity evidence**

Squads can publish controlled versions without depending on manual implementation of the central team.

### Level 3 — Risk-based Governance

**Characteristics**

- AI Catalog completo;
- risk tiers e gates proporcionais;
- AGR and lifecycle memory;
- datasets e baselines versionados;
- approval evidence;
- periodic review;
- incident management especializado.

**Maturity evidence**

The organization demonstrates why a version has been published and can quickly suspend or withdraw.

### Level 4 — Federal Scale

**Characteristics**

- multiple units and tenants;
- marketplace of capacities;
- MCP e tools governadas;
- chargeback ou showback;
- capacity management;
- community of practice;
- platform product management maduro.

**Maturity evidence**

Adoption grows without proportional growth of exceptions, incidents or central effort.

### Level 5 — Continuous optimisation

**Characteristics**

- quality, cost and availability-oriented routing;
- online assessments and shadow traffic;
- error budgets influenciam releases;
- optimization by outcome;
- review automation and evidence;
- multi-region resilience when justified.

**Maturity evidence**

Quality, risk, cost and speed are managed as dimensions of the same product platform.

## Matriz de maturidade

| Dimension | N0 | N1 | N2 | N3 | N4 | N5 |
|---|---|---|---|---|---|---|
| Delivery | artesanal | templates | golden path | risk stutters | self-service federado | continuous optimization |
| Governance | inexistente | checklist | workflow | evidence and review | policies em escala | Adaptive automation |
| Security | projeto a projeto | baseline | enforcement comum | threat model e testes | isolamento endurecido | continuous assurance |
| Evaluation | manual | amostras | datasets | Baselines and regression | online + offline | outcome optimization |
| Operation | best effort | logs | SLOs e runbooks | incidentes e reviews | capacity e DR | error-budget driven |
| FinOps | fatura agregada | tags | cost per agent | budgets e quotas | showback/chargeback | economic routing |
| Organisation | iniciativas | champions | platform team | federal model | CoE e comunidade | product portfolio otimizado |

## 12-month reference roadmap

The calendar should be adapted to the context. The following sequence prioritizes operational learning before expansion.

### Trimestre 1 — Foundation e primeiro golden path

**Entregas**

- platform charter e owners;
- capability map e backlog;
- Minimum Agent Registry;
- Agent Gateway e Runtime;
- Model Gateway;
- identity, policies and telemetry;
- CI/CD com contratos;
- first internal case of low or medium risk.

**Results**

- first version published by pipeline;
- trace ponta a ponta;
- cost per known invocation;
- rollback exercitado;
- feedback da primeira squad.

### Trimester 2 — Knowledge, memory and evaluation

**Entregas**

- ingestion with quarantine;
- ACL por documento e chunk;
- citations e groundedness;
- memory with TTL and consent;
- datasets e baseline;
- risk workflow proporcional;
- quality and cost dashboards.

**Results**

- documentary agent operating with controlled access;
- regressions blocked in pipeline;
- exclusion and expiration tested;
- review of 30 or 60 days.

### Trimester 3 — Tools and corporate integration

**Entregas**

- MCP Registry;
- onboarding de tools;
- idempotence, outbox and compensation;
- HITL for critical actions;
- tool metrics e audit;
- segundo e terceiro casos de uso.

**Results**

- governed corporate action;
- policy-locking tools;
- falhas e retries sem duplicar efeitos;
- proven reuse between squads.

### Trimestre 4 — Escala, FinOps e operating model

**Entregas**

- quotas and budgets by tenant and agent;
- showback;
- marketplace interno;
- maturity assessment;
- community of practice;
- capacity tests;
- DR e incident simulation;
- roadmap next year based on adoption.

**Results**

- costs allocated;
- lead time reduzido;
- operation with SLOs;
- crescimento sem aumento proporcional do time central.

## Backlog orientado a outcomes

Avoid a backlog composed of only components. Estruture epics such as:

- reduce the onboarding of a squad from four weeks to five days;
- ensure that no unauthorised source is returned;
- detect groundedness regression before deploy;
- attribute 95% of the costs to agents and areas;
- discontinue one version in less than five minutes;
- perform a transactional action without duplication after retry.

The technical components are the deliveries needed to achieve these outcomes.

## KPIs da plataforma

### Adoption and experience

- squads onboarded;
- published and active agents;
- tempo para primeiro deploy;
- percentual no golden path;
- developer satisfaction;
- taxa de reuso de capabilities.

### Quality and risk

- blocked regressions;
- policy denials por categoria;
- security or privacy incidents;
- respostas grounded;
- taxa de fallback e abstention;
- exceptions opened and expired.

### Operation

- disponibilidade e p95 por workload;
- MTTR;
- saturation and backlog;
- rate of successful invocation;
- incidents by staff members and dependency;
- periodic reviews.

### FinOps e valor

- cost per agent, area and model;
- cost per completed task;
- budget variance;
- saving time or reducing effort;
- revenue, conversion or avoided risk where applicable;
- platform cost per active consumer.

## Guardrails de investimento

Before expanding a capability, valid:

- at least two consumers or a strong corporate requirement;
- product owner and operation;
- SLO and expected costs;
- contract and strategy of detention;
- depreciation plan;
- success metric;
- alternative managed or useful analyzed.

## Roadmap anti-patterns

- implement all components before the first real case;
- measure progress by quantity of tools;
- adopt multi-agent, long memory and fine-tuning simultaneously;
- construir marketplace sem consumidores;
- expanding to HIGH cases before operating a simple case;
- ignore support, incidents and costs during OCP;
- treat governance as a later phase.

## Next chapter

Os [production checklists](08-production-checklists.md) they convert maturity and lifecycle into objective verifications for each release.
