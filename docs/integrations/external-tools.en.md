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
| Security | Authentication, authorization and secrecy management |
| Data | Classification and location of data |
| LGPD | Legal basis, retention and sharing |
| Cost | Charging model and predictability |
| SLA | Availability and support |

## Standards

- Prefer integration via controlled MCP Server
- Do not expose secrets to agents
- record todos the tool calls
- apply rate limiting
- Defining fallback for unavailability

## Requirements

- Approval of governance for critical tools
- Versioned contract
- Observability by external call
- Discontinuation plan
