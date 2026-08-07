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

- design templates;
- appropriate identity and secrets;
- basic logging;
- initial case inventory;
- approved providers and models;
- publication checklist.

**Maturity evidence**

First low-risk cases reach production without ad hoc controls.

### Level 2 — Implementable Golden path

**Characteristics**

- Agent Registry and life cycle;
- Model Gateway;
- contracts and events funded;
- IC/CD with evaluations and policies;
- tip-to-end observability;
- runbooks and rollbacks;
- first service of knowledge or tools.

**Maturity evidence**

Squads can publish controlled versions without depending on manual implementation of the central team.

### Level 3 — Risk-based Governance

**Characteristics**

- AI Catalog completo;
- risk tiers and proportional gates;
- RAG and lifecycle memory;
- datesets and versioned baselines;
- approval evidence;
- periodic review;
- specialized incident management.

**Maturity evidence**

The organization demonstrates why a version has been published and can quickly suspend or withdraw.

### Level 4 — Federal Scale

**Characteristics**

- multiple units and tenants;
- marketplace of capacities;
- MCP and governed tools;
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
- error budgets influence releases;
- optimization by outcome;
- review automation and evidence;
- multi-region resilience when justified.

**Maturity evidence**

Quality, risk, cost and speed are managed as dimensions of the same product platform.

## Matrix of maturity

| Dimension | N0 | N1 | N2 | N3 | N4 | N5 |
|---|---|---|---|---|---|---|
| Delivery | artesanal | templates | golden path | risk stutters | self-service federado | continuous optimization |
| Governance | none | Checklist | workflow | evidence and review | Policies on scale | Adaptive automation |
| Security | Project by Project | Baseline | Common enforcement | threat model and tests | hardened insulation | continuous assurance |
| Evaluation | manual | amostras | datasets | Baselines and regression | online + offline | outcome optimization |
| Operation | best effort | logs | SLOs and runbooks | Incidents and reviews | Capacity and DR | error-budget driven |
| FinOps | aggregate invoice | tags | cost per agent | budgets and quotas | showback/chargeback | economic routing |
| Organisation | Initiatives | champions | platform team | federal model | EC and community | product portfolio optimized |

## 12-month reference roadmap

The calendar should be adapted to the context. The following sequence prioritizes operational learning before expansion.

### Trimester 1 — Foundation and First golden path

**Entregas**

- platform charter and owners;
- capability map and backlog;
- Minimum Agent Registry;
- Agent Gateway and Runtime;
- Model Gateway;
- identity, policies and telemetry;
- IC/CD with contracts;
- first internal case of low or medium risk.

**Results**

- first version published by pipeline;
- trace ponta a ponta;
- cost per known invocation;
- rollback exercitado;
- feedback of the first squad.

### Trimester 2 — Knowledge, memory and evaluation

**Entregas**

- ingestion with quarantine;
- ACL by document and chunk;
- quotions and groundedness;
- memory with TTL and consent;
- datesets and baseline;
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
- onboarding of tools;
- idempotence, outbox and compensation;
- HITL for critical actions;
- tool metrics and audit;
- 2 and 3 cases of use.

**Results**

- governed corporate action;
- policy-locking tools;
- failures and retries without doubling effects;
- proven reuse between squads.

### Trimester 4 — Scale, FinOps and operating model

**Entregas**

- quotas and budgets by tenant and agent;
- showback;
- marketplace interno;
- maturity assessment;
- community of practice;
- capacity tests;
- DR and incident simulation;
- roadmap next year based on adoption.

**Results**

- costs allocated;
- lead time reduzido;
- operation with SLOs;
- growth without proportional increase of the central team.

## Backlog orientado a outcomes

Avoid a backlog composed of only components. Estruture epics such as:

- reduce the onboarding of a squad from four weeks to five days;
- ensure that no unauthorised source is returned;
- detect groundedness regression before deploy;
- attribute 95% of the costs to agents and areas;
- discontinue one version in less than five minutes;
- perform a transactional action without duplication after retry.

The technical components are the deliveries needed to achieve these outcomes.

## Platform KPIs

### Adoption and experience

- squads onboarded;
- published and active agents;
- time to first deploy;
- percentage in the golden path;
- developer satisfaction;
- capability reuse rate.

### Quality and risk

- blocked regressions;
- policy denials per category;
- security or privacy incidents;
- respostas grounded;
- fallback and abstention rate;
- exceptions opened and expired.

### Operation

- availability and p95 per workload;
- MTTR;
- saturation and backlog;
- rate of successful invocation;
- incidents by agent members and dependency;
- periodic reviews.

### FinOps and value

- cost per agent, area and model;
- cost per completed task;
- budget variance;
- saving time or reducing effort;
- revenue, conversion or avoided risk where applicable;
- platform cost per active consumer.

## Investment reservoirs

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
- building marketplace without consumers;
- expanding to HIGH cases before operating a simple case;
- ignore support, incidents and costs during OCP;
- treat governance as a later phase.

## Next chapter

Os [production checklists](08-production-checklists.md) they convert maturity and lifecycle into objective verifications for each release.
