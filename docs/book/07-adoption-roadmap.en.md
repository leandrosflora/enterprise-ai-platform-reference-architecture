# 8. Maturity model and adoption roadmap

## This is a principle.

The maturity of a AI Platform is not determined by the number of services deployed, but by the ability to deliver use cases with predictable quality, control, operation and cost.

## The maturity model

### Level 0  Isolated experiments

**Characteristics**

- Notebooks, scripts and SaaS without a common standard;
- credentials and local settings;
- pouca rastreabilidade;
- manual evaluation;
- unallocated costs;
- knowledge and prompts copied between projects.

** Goal to move forward**

Identify repeated patterns, owners and material risks.

### Level 1  Minimum standards

**Characteristics**

- design templates;
- appropriate identity and secrecy;
- basic logging;
- initial case inventory;
- approved providers and models;
- the publication checklist.

** Evidence of maturity**

The first low-risk cases reach production without ad hoc controls.

### Level 2  Golden path executable

**Characteristics**

- Agent Registry and life cycle;
- Model Gateway;
- Contracts and versioned events;
- CI/CD with assessments and policies;
- end-to-end observability;
- runbooks and rollback;
- first knowledge or tools service.

** Evidence of maturity**

Squads can publish controlled versions without relying on manual implementation from the central team.

### Level 3  Risk-based governance

**Characteristics**

- AI Catalog completo;
- risk tiers and proportional gates;
- RAG and lifecycle memory;
- versioned datasets and baselines;
- approval evidence;
- periodic review;
- incident management especializado.

** Evidence of maturity**

The organisation demonstrates why a version has been published and can quickly suspend or withdraw it.

### Level 4  Federated scale

**Characteristics**

- multiple units and tenants;
- the capacity marketplace;
- MCP and controlled tools;
- chargeback ou showback;
- capacity management;
- community of practice;
- platform product management maduro.

** Evidence of maturity**

Adoption grows without proportionate growth of exceptions, incidents or central effort.

### Level 5  Continuous optimisation

**Characteristics**

- quality, cost and availability-oriented routing;
- online assessments and shadow traffic;
- error budgets influenciam releases;
- the results of the evaluation shall be presented in accordance with the methodology set out in Annex II.
- automation of review and evidence;
- multi-regional resilience when justified.

** Evidence of maturity**

Quality, risk, cost and speed are managed as dimensions of the same platform product.

## Mature matrix

| Size | N0 | N1 | N2 | N3 | N4 | N5 |
|---|---|---|---|---|---|---|
| Delivery | artesanal | templates | golden path | Cat at risk | self-service federado | continuous optimisation |
| Governance | inexistente | Checklist | workflow | Evidence and review | policies at scale | The following information shall be provided: |
| Security | project to project | baseline | enforcement comum | threat model and testing | isolamento endurecido | continuous assurance |
| Evaluation | manual | amostras | datasets | Baselines and regression | online + offline | Optimization by outcome |
| Operations | best effort | logs | SLOs and runbooks | Incidents and reviews | capacity and DR | error-budget driven |
| FinOps | fatura agregada | tags | Cost per agent | budgets and quotas | showback/chargeback | economic routing |
| The Commission shall adopt implementing acts. | iniciativas | champions | platform team | Federated model | CoE and Community | product portfolio otimizado |

## Reference roadmap in 12 months

The timetable should be adapted to the context.The following sequence prioritizes operational learning before expansion.

### Quarter 1  Foundation and first golden path

**Entregas**

- platform charters and owners;
- capability map and backlog;
- the minimum Agent Registry;
- Agent Gatewayand Runtime;
- Model Gateway;
- identity, policies and telemetry;
- CI/CD with contracts;
- the first low- or medium-risk internal case.

** Results**

- the first version published by pipeline;
- draw a line from end to end;
- cost per known invocation;
- rollback exercitado;
- First squad feedback.

### Quarter 2  Knowledge, memory and evaluation

**Entregas**

- ingestion with quarantine;
- ACL per document and chunk;
- citations and groundedness;
- memory with TTL and consent;
- data sets and baseline;
- risk workflow proporcional;
- quality and cost dashboards.

** Results**

- a documentary agent operating with controlled access;
- blocked regressions in the pipeline;
- Tested exclusion and expiration;
- 30 or 60 day review carried out.

### Quarter 3  Tools and corporate integration

**Entregas**

- MCP Registry;
- onboarding of tools;
- idempotence, outbox and compensation;
- HITL for critical actions;
- tool metrics and audits;
- second and third use cases.

** Results**

- governed corporate shares;
- policy-blocking tools;
- failures and retries without duplicate effects;
- proven reuse between squads.

### Quarter 4  Scale, FinOps and operating model

**Entregas**

- quotas and budgets per tenant and agent;
- showback;
- marketplace interno;
- maturity assessment;
- community of practice;
- capacity tests;
- DR and incident simulation;
- the next year's roadmap based on adoption.

** Results**

- assigned costs;
- lead time reduzido;
- operation with SLOs;
- growth without a proportionate increase in the central team.

## Results-oriented backlog

Avoid a backlog composed only of components.

- reduce the onboarding of a squad from four weeks to five days;
- ensure that no unauthorised source is returned;
- detecting groundedness regression prior to deployment;
- allocate 95% of the costs to agents and areas;
- suspend a version in less than five minutes;
- execute a transaction without duplicity after retry.

The technical components are the necessary deliveries to achieve these results.

## Platform KPIs

### Adoption and experience

- squads onboarded;
- published agents and assets;
- time for first deployment;
- percentage on the golden path;
- the developer's satisfaction;
- capacity reuse rate.

### Quality and risk

- blocked regressions;
- policy denials by category;
- security or privacy incidents;
- respostas grounded;
- fallback and abstention rates;
- Open and expired exceptions.

### Operations

- Availability and p95 per workload;
- MTTR;
- saturation and backlog;
- the success rate of the invocation;
- incidents per agent and dependency;
- compliance with periodic reviews.

### FinOps and value

- cost per agent, area and model;
- cost per completed task;
- budget variance;
- time savings or reduction of effort;
- revenue, conversion or risk avoided where applicable;
- the cost of the platform per active consumer.

## Investment guardrails

Before expanding a capability, validate:

- at least two consumers or a strong corporate requirement;
- owner of the product and operation;
- SLO and expected cost;
- contract and versioning strategy;
- the depreciation plan;
- the success metric;
- managed or analyzed purchasable alternative.

## Roadmap anti-patterns

- deploy all components before the first actual case;
- measuring progress by number of tools;
- adopt multi-agent, long memory and fine-tuning at the same time;
- building a marketplace without consumers;
- expanding to HIGH cases before operating a simple case;
- ignore support, incidents and costs during the POC;
- to treat governance as a later stage.

## Next chapter

The [production checklists](08-production-checklists.md) convert maturity and lifecycle into objective checks for each release.
