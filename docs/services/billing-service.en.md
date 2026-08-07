# Billing Service

## General view

Billing Service is responsible for the platform FinOps: token tracking, cost allocation per agent/time/business unit and chargeback/showback generation.

## Responsabilidades

- Consume use events (agent invoking, tool execution, embedding generation)
- Calculate cost per model, agent, team and business unit
- Generate chargeback and showback reports
- Warning of consumption above defined limits

## Out of scope

- Execution of the agent or tool
- Conformity audit (paper from theAudit Service)
- Definition of risk approval limits (Governance Service paper)

## Dependencies

| Dependence | Uso |
|---|---|
| Kafka | Consume use events for cost calculation |
| PostgreSQL | Persistent costs and chargeback data |

## Events consumed

- `agent.invoked`
- `tool.executed`
- `embedding.generated`

## Non-functional requirements

| Requisito | Diretriz |
|---|---|
| Retention | 24 months for usage and billing data, basis for chargeback/showback |
| Accuracy | Calculated cost shall reflect actual consumption of tokens and tools per invocation |
| Escalabilidade | Processed high volume of use events without significant delay in the closing period |
| Auditoria | Cost calculations shall be traceable to the event of origin |

## Related Decisions

- [docs/finops/token-costs.md](../finops/token-costs.md)
