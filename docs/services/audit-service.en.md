# Audit Service

## General view

Audit Service maintains the mutable auditory trille of the platform: use of agents, implementation of tools and decisions of government. Concurrent events of practically all the same services and become available for compliance and research.

## Responsabilidades

- Consume events in all fields (agentes, knowledge, memory, government, evaluation)
- Maintain a stable and stable auditory trille
- Publication of auditor confirmation event
- Provide a trilha for consultation for time of conformity and safety
- Checking auditor records for Observability Stack

## Out of the scuff

- Decision of approval or rejection of agents
- Cost calculator (Billing Service)
- Implementation or evaluation of agents

## Dependencies

| Dependence | Uso |
|---|---|
| Kafka | Confirm events from all areas of the platform |
| Observability Stack | Public records and auditory journals |

## Eventos Consumidos

- `agent.created`, `agent.updated`, `agent.published`, `agent.retired`
- `agent.invoked`, `tool.executed`
- `knowledge.ingested`, `embedding.generated`, `document.indexed`
- `memory.updated`
- `evaluation.started`, `evaluation.completed`
- `governance.approved`, `governance.rejected`

## Eventos Publicados

- `audit.created`

## Non-functioning requirements

| Requisito | Diretriz |
|---|---|
| Imutabilidade | Audit records may not be amended or withdrawn |
| Retention | 5 years, according to regulatory policy (see [docs/contracts/events.md](../contracts/events.md)) |
| Disponibilidade | Consumption of events can't lose messages (DLQ for the purpose) |
| Conformidade | Reports and investigations for LGPD and regulatory audits |
