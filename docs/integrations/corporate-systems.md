# Corporate Systems Integration

## Objetivo

Definir padrões para integração de agentes com sistemas corporativos internos.

## Sistemas Típicos

- CRM
- ERP
- Core Banking
- Ticketing
- Document Management
- Data Platform
- Workflow/BPM

## Padrões de Integração

| Padrão | Uso |
|---|---|
| REST | Consultas e comandos síncronos |
| gRPC | Integrações internas de baixa latência |
| Kafka | Eventos de domínio e integração assíncrona |
| MCP | Ferramentas expostas para agentes |
| Batch | Processamentos programados |

## Princípios

- Agentes não acessam bancos corporativos diretamente
- Integrações devem passar por APIs, eventos ou MCP
- Tool calls devem ser autorizados e auditados
- Sistemas críticos exigem aprovação de governança

## Requisitos

- CorrelationId fim a fim
- Timeout e retry controlado
- Idempotência para comandos críticos
- Observabilidade por integração
