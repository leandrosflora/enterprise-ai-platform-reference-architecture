# Corporate Systems Integration

## Objet

Definite rules for integrating agents with inter-personal systems.

## Technical systems

- CRM
- ERP
- Core Banking
- Ticketing
- Document Management
- Data Platform
- Workflow/BPM

## Integrating Pads

| Father | Uso |
|---|---|
| REST | Single-comanding consultations |
| gRPC | Internal ties of low-level lativity |
| Kafka | - Domain and integration events |
| MCP | Exposed grenades for agents |
| Batch | Processamentos programados |

## Principles

- Agents do not access corporate banks directly
- Integrations shall pass by APIs, events or MCP
- Tool calls must be auto-reported and audited
- Critical systems require government approval

## Requirements

- Correlation
- Timeout e retry controlado
- Idempotence for critical commands
- Integrated observation
