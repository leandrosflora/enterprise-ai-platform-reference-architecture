# External Tools Integration

## Objective

Defining criteria for using external tools by platform agents and services.

## Types of tools

- SaaS APIs
- Search APIs
- Document Processing APIs
- OCR Services
- Communication Channels
- Ticketing Tools

## Approval Criteria

| Criteria | Description |
|---|---|
| Security | Authentication, authorisation and secrecy management |
| Data | Classification and location of data |
| LGPD | Legal basis, retention and sharing |
| Cost | Charging model and predictability |
| SLA | Disponibilidade e suporte |

## Standards

- Prefer integration via controlled MCP Server
- Do not expose secrets to agents
- Registrar todos os tool calls
- Aplicar rate limiting
- Defining fallback for unavailability

## Requirements

- Approval of governance for critical tools
- Contrato versionado
- Observability by external call
- Discontinuation plan
