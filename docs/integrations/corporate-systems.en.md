# Corporate Systems Integration

## Objective

Defining standards for integrating agents with internal corporate systems.

## Typical Systems

- CRM
- ERP
- Core Banking
- Ticketing
- Document Management
- Data Platform
- Workflow/BPM

## Integration Patterns

| Pattern | Uso |
|---|---|
| REST | Synchronous consultations and commands |
| gRPC | Low latency internal integrations |
| Kafka | Domain events and asynchronous integration |
| MCP | Exposed tools for agents |
| Batch | Processamentos programados |

## Principles

- Agents do not access corporate banks directly
- Integrations should undergo PIA, events or PCM
- Tool calls devem ser autorizados e auditados
- Critical systems require approval of governance

## Requirements

- CorrelationId fim a fim
- Timeout e retry controlado
- Independence for critical commands
- Observability by integration
