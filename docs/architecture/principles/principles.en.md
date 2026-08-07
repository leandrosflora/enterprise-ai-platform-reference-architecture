# Agricultural principles

These principles are already in contract, domains and services documented in this repository. They are explicitly here as the only reference for which new domains, services or integrations are proposed.

## 1. Data ownership by service

Each service is part of its storage; there is no right access to other services. Integration between services occurs by Sncrone API or a sncrone event, never by comparing data.

Ver: [docs/contracts/data-stores.md](../../contracts/data-stores.md).

## 2. Integration oriented to events

Changes of relevant status (creation, publication, implementation, approval) are published as versions of events in Kafka, with a padrix envelope (`eventId`, `correlationId`, `causationId`, `schemaVersion`). Users return events instead of consulting the producer in a single manner as soon as possible.

Ver: [docs/contracts/events.md](../../contracts/events.md).

## 3. Security and governance by pattern

All the agent, tool or device is protected by authenticity (OIDC/OAuth2), authorisation by esthetic, and passes by the approval cycle of Governance Service before it goes to production. There is no "ungoverned" capacity on the platform.

Ver: [docs/governance/approval-workflow.md](../../governance/approval-workflow.md), [docs/security/authentication.md](../../security/authentication.md).

## 4. Auditoria and observability point to point

All relevant implementation (invocation of agent, called a tool, government decision) is auditable and is tracable via distributed trace. Auditoria and observability are not added after — are part of the event contract since the beginning.

Ver: [docs/observability/tracing.md](../../observability/tracing.md), [docs/security/authorization.md](../../security/authorization.md).

## 5. Cost awareness (FinOps) since the design

Use of models, tools and storage is measured and assigned by agent, time or unit of business, allowing chargeback/showback. Costs are not a sole concern — they are a requirement in the design stages of fields and services.

Ver: [docs/finops/token-costs.md](../../finops/token-costs.md).

## 6. Resistance against failures of external dependency

Compared to models, MCP and corporative services, they apply timeout, controlled retry and circuit breaker. No service assumes full availability of its external dependencies.

Ver: [docs/services/agent-runtime.md](../../services/agent-runtime.md).
