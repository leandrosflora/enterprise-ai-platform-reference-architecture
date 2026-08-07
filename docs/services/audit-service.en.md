# Audit Service

## General view

Audit Service maintains the unchanging audit trail of the platform: use of agents, implementation of tools and governance decisions. It consumes events from virtually all other services and makes them available for compliance and research.

## Responsabilidades

- Consuming events in all areas (agents, knowledge, memory, governance, evaluation)
- Continuing the audit trail that is unchanging and researchable
- Publish an audit confirmation event
- Provide a consultation track for compliance and safety teams
- To forward audit records to the Observability Stack

## Out of scope

- Decision approving or rejecting agents
- Cost calculation (paper from theBilling Service)
- Execution or evaluation of agents

## Dependencies

| Dependence | Uso |
|---|---|
| Kafka | Consume events from all platform domains |
| Observability Stack | Publish logs and audit trails |

## Events consumed

- `agent.created`, `agent.updated`, `agent.published`, `agent.retired`
- `agent.invoked`, `tool.executed`
- `knowledge.ingested`, `embedding.generated`, `document.indexed`
- `memory.updated`
- `evaluation.started`, `evaluation.completed`
- `governance.approved`, `governance.rejected`

## Events Published

- `audit.created`

## Non-functional requirements

| Requisito | Diretriz |
|---|---|
| Imutabilidade | Audit records may not be altered or deleted |
| Retention | 5 years, according to the regulatory policy (see [docs/contracts/events.md](../contracts/events.md)) |
| Disponibilidade | Event consumption cannot lose messages (DLQ per domain) |
| Conformidade | Support research and reporting for LGPD and regulatory audits |
