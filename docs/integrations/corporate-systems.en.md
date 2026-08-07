# Corporate Systems Integration

## Objective

Set standards for the integration of agents with internal corporate systems.

## Typical systems

- CRM
- ERP
- Core Banking
- Ticketing
- Document Management
- Data Platform
- Workflow/BPM

## The Commission shall adopt delegated acts in accordance with Article 21 of this Regulation.

| Standard | Uso |
|---|---|
| REST | Synchronous queries and commands |
| gRPC | Low latency internal integrations |
| Kafka | Domain events and asynchronous integration |
| MCP | Tools exposed to agents |
| Batch | Processamentos programados |

## Principles

- Agents do not access corporate banks directly
- Integrations shall be through APIs, events or MCP
- Tool calls must be authorised and audited
- Critical systems require governance approval

## Requirements

- End to end correlation
- Timeout and retry controlled
- Idempotence for critical commands
- Observability by integration
