# Billing Service

## General view

Billing Service is responsible for the FinOps of the platform: tokens, cost allocation by agent/time/business unit and chargeback/showback generation.

## Responsabilidades

- Consume use events (invocation of agent, machining, insertion)
- Calculate cost by model, agent, time and business unit
- - Gerar chargeback and showback reports
- Alert about consumption above defined limits

## Out of the scuff

- Execution of the agent or the tool
- Compliance audit (Audit Service)
- Definition of risk approval limits (Governance Service)

## Dependencies

| Dependence | Uso |
|---|---|
| Kafka | Confirmed use events for calculation of cost |
| PostgreSQL | Keep your charges and data |

## Eventos Consumidos

- `agent.invoked`
- `tool.executed`
- `embedding.generated`

## Non-functioning requirements

| Requisito | Diretriz |
|---|---|
| Retention | 24 months for use data and work, base for chargeback/showback |
| I need to get a job. | The calculated cost shall reflete real consumption of tokens and tools by invocation |
| Escalabilidade | High volume of use events without relevant delay in the period closure |
| Auditoria | Cost calculations must be rastered at the origin event |

## Related Decisions

- [docs/finops/token-costs.md](../finops/token-costs.md)
