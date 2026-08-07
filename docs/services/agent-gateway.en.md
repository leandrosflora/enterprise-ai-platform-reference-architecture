# Agent Gateway

## General view

The Agent Gateway is the only point of entry for agent calls. Authenticity and authorisation of the call, application rate limiting and rote the call for Agent Runtime.

## Responsabilidades

- Expose the API public voicemail of agents
- Identifying requirements via Identity Provider (OIDC)
- Authorize access by agent and escopo
- Using limit rate and short-term cache
- Rotate the voice for Agent Runtime

## Out of the scuff

- Execution of the agent and prompts, tools and memory
- Quality assessment of response
- Life cycle and adsorption of agent

## API Principal

```http
POST /agents/{agentId}/invoke
GET /agents/{agentId}
Authorization: Bearer <token>
```

## Dependencies

| Dependence | Uso |
|---|---|
| Identity Provider | Autensification and authorisation (OIDC) |
| Agent Runtime | Rotation of the invocation |
| Redis | Cache e rate limiting |

## Non-functioning requirements

| Requisito | Diretriz |
|---|---|
| Latence | Minimum overhead before rote to Agent Runtime |
| Security | Autendance and authorisation in all requirements |
| Escalabilidade | horizontal column by volume of calls |
| Resilience | Limiting rate to protect Agent Runtime against pigs |

## Related Decisions

- (ADR-004 — Agent Runtime with stable and adaptable nerves)(../adrs/004-agent-runtime-strategy.md)
