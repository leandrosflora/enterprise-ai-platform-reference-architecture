# Architectural Principles

These principles are already implicit in the contracts, domains and services documented in this repository. They are explained here as a single reference for those who propose new domains, services or integrations.

## 1. Ownership of data per service

Each service owns its storage; there is no direct access to banks of other services. Integration between services occurs by synchronous PIA or asynchronous event, never by shared access to data.

Ver: [docs/contracts/data-stores.md](../../contracts/data-stores.md).

## 2. Event-oriented integration

Relevant state changes (creation, publication, execution, approval) are published as events versioned in Kafka, with standard envelope (`eventId`, `correlationId`, `causationId`, `schemaVersion`). Consumers react to events instead of consulting the producer in a synchronous manner wherever possible.

Ver: [docs/contracts/events.md](../../contracts/events.md).

## 3. Security and standard governance

All agent, tool or data capacity is protected by authentication (OIDC/OAuth2), authorization by scope, and goes through the approval cycle of the Governance Service before going to production.

Ver: [docs/governance/approval-workflow.md](../../governance/approval-workflow.md), [docs/security/authentication.md](../../security/authentication.md).

## 4. Audit and observability

Every relevant execution (agent invoking, tool call, governance decision) generates audible track and is traceable via distributed trace. Auditting and observability are not added afterwards — they are part of the event contract from the outset.

Ver: [docs/observability/tracing.md](../../observability/tracing.md), [docs/security/authorization.md](../../security/authorization.md).

## 5. Cost awareness (FinOps) from design

The use of models, tools and storage is measured and assigned by agent, team or business unit, allowing for chargeback/showback.Costs are not only an operational concern — they are a requirement in the design phases of domains and services.

Ver: [docs/finops/token-costs.md](../../finops/token-costs.md).

## 6. Resilience against external dependency failures

Called to models, MCP tools and corporate services apply timeout, retry controlled and circuit breaker. No service assumes total availability of its external premises.

Ver: [docs/services/agent-runtime.md](../../services/agent-runtime.md).
