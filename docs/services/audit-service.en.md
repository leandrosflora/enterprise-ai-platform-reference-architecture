# Audit Service

## Overview

The Audit Service maintains the immutable audit trail of the platform: use of agents, execution of tools and governance decisions. It consumes events of practically all other services and makes them available for conformity and research.

## responsibilities

- Consume events from all domains (agents, knowledge, memory, governance, evaluation)
- Persist audit trail immutable and research
- Publication of audit confirmation event
- Available track for consultation by conformity and safety teams
- Sending audit records to the Observability Stack

## Out of Scope

- Approval or rejection decision
- Calculation of cost (Role of Billing Service)
- Implementation or evaluation of agents

## Dependencies

| Dependence | Use |
|---|---|
| Kafka | Consumes events of all domains of the platform |
| Observability Stack | Publica logs and audit trails |

## Consumption Events

- `agent.created`, `agent.updated`, `agent.published`, `agent.retired`
- `agent.invoked`, `tool.executed`
- `knowledge.ingested`, `embedding.generated`, `document.indexed`
- `memory.updated`
- `evaluation.started`, `evaluation.completed`
- `governance.approved`, `governance.rejected`

## published events

- `audit.created`

## Non-functional requirements

| Requirements | Guideline |
|---|---|
| Importability | Audit records cannot be altered or erased |
| Retention | 5 years, according to regulatory policy (see [docs/contracts/events.md](../contracts/events.md)() |
| availability | Event consumption cannot lose messages (DLQ per domain) |
| Conformity | Supports investigation and reports for LGPD and regulatory audits |
