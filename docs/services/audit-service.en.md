# Audit Service

## Overview

The Audit Service maintains the immutable audit trail of the platform: use of agents, execution of tools and governance decisions. It consumes events of practically all other services and makes them available for conformity and research.

## Responsabilidades

- Consume events from all domains (agents, knowledge, memory, governance, evaluation)
- Persist audit trail immutable and research
- Publication of audit confirmation event
- Available track for consultation by conformity and safety teams
- Encaminhar registros de auditoria para o Observability Stack

## Fora de Escopo

- Approval or rejection decision
- Calculation of cost (Role of Billing Service)
- Implementation or evaluation of staff

## Dependencies

| Dependence | Uso |
|---|---|
| Kafka | Consumes events of all domains of the platform |
| Observability Stack | Publica logs e trilhas de auditoria |

## Consumption Events

- `agent.created`, `agent.updated`, `agent.published`, `agent.retired`
- `agent.invoked`, `tool.executed`
- `knowledge.ingested`, `embedding.generated`, `document.indexed`
- `memory.updated`
- `evaluation.started`, `evaluation.completed`
- `governance.approved`, `governance.rejected`

## Publicated events

- `audit.created`

## Non-functional requirements

| Requisito | Diretriz |
|---|---|
| Imutabilidade | Audit records cannot be altered or erased |
| Retention | 5 years, according to regulatory policy (see [docs/contracts/events.md](../contracts/events.md)) |
| Disponibilidade | Event consumption cannot lose messages (DLQ per domain) |
| Conformidade | Supports investigation and reports for LGPD and regulatory audits |
