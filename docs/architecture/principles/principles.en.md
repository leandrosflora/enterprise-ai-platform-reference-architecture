# Architectural principles

These principles are already embedded in the contracts, domains and services documented in this repository and are explained here as a unique reference for those proposing new domains, services or integrations.

## 1. Ownership of data by service

Each service owns its own storage; there is no direct access to banks of other services.APIsynchronous or asynchronous event, never by shared data access.

Ver: [docs/contracts/data-stores.md](../../contracts/data-stores.md).

## 2. Events-oriented integration

Relevant status changes (creation, publication, execution, approval) are published as events versioned in Kafka, with a standard envelope (`eventId`, `correlationId`, `causationId`, `schemaVersion`).

Ver: [docs/contracts/events.md](../../contracts/events.md).

## 3. Security and governance by default

Any agent, tool or data capability is protected by authentication (OIDC/OAuth2), scope authorisation, and undergoes the Governance Service approval cycle before going into production.

Ver: [docs/governance/approval-workflow.md](../../governance/approval-workflow.md), [docs/security/authentication.md](../../security/authentication.md).

## 4. Auditing and end-to-end traceability

Every relevant execution (agent call, tool call, governance decision) generates an auditable track and is traceable via distributed trace.

Ver: [docs/observability/tracing.md](../../observability/tracing.md), [docs/security/authorization.md](../../security/authorization.md).

## 5. Cost awareness (FinOps) from the design

The use of models, tools and storage is measured and assigned by agent, team or business unit, allowing for chargeback/showback.

Ver: [docs/finops/token-costs.md](../../finops/token-costs.md).

## 6. resilience to failures of external dependencies

Model calls, MCP tools and corporate services apply timeout, controlled retry and circuit breaker.

Ver: [docs/services/agent-runtime.md](../../services/agent-runtime.md).
