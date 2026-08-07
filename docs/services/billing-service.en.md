# Billing Service

## Overview

The Billing Service is responsible for FinOps of the platform: token tracking, cost allocation by agent/time/trade unit and generation of chargeback/showback.

## Responsabilidades

- Consume events of use (agent invoking, tool execution, embedding generation)
- Calculating cost per model, agent, team and business unit
- Generate chargeback and showback reports
- Alert on consumption above defined limits

## Out of Scope

- Implementation of the agent or tool
- Conformity audit ( Audit Service role)
- Definition of risk approval limits (Role of the Governance Service)

## Dependencies

| Dependence | Use |
|---|---|
| Kafka | Consumes use events for cost calculation |
| PostgreSQL | Costs and chargeback data persist |

## Consumption Events

- `agent.invoked`
- `tool.executed`
- `embedding.generated`

## Non-functional requirements

| Requirements | Guideline |
|---|---|
| Retention | 24 months for data on use and charge, base for chargeback/showback |
| Precision | Calculated cost should reflect actual consumption of tokens and invocation tools |
| Escalabilidade | It processes a high volume of use events without relevant delay in closing periods |
| Audit | Cost calculations should be traceable to the event of origin |

## Related Decisions

- [docs/finops/token-costs.md](../finops/token-costs.md)
