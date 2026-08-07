# External Tools Integration

## Objective

Establish criteria for the use of external tools by platform agents and services.

## Types of tools

- SaaS APIs
- Search APIs
- Document Processing APIs
- OCR Services
- Communication Channels
- Ticketing Tools

## Criteria for approval

| Criterion of use | Other information |
|---|---|
| Security | Authentication, authorisation and management of secrets |
| The data | Classification and location of data |
| LGPD | Legal basis, retention and sharing |
| Custo | Charging model and predictability |
| SLA | Availability and support |

## Standards

- Prefer integration via MCP Server controlled
- Do not expose secrets to agents
- Record all tool calls
- Aplicar rate limiting
- Define fallback to unavailability

## Requirements

- Approval of governance for critical tools
- Versioned contract
- Observability by external call
- Discontinuation plan
