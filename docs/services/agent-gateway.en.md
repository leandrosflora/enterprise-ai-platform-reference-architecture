# Agent Gateway

## General view

The Agent Gateway is the single point of entry for agent invocations, authenticates and authorises the call, applies rate limiting and routes the invocation to the Agent Runtime.

## Responsabilidades

- Exposure of the API public call for agents
- Authenticate requests via Identity Provider (OIDC)
- Authorise access by agent and scope
- Apply rate limiting and short-term cache
- Routing the invocation to Agent Runtime

## Out of scope

- Execution of the agent and orchestration of prompts, tools and memory
- Assessment of the quality of response
- Approval and life cycle of the agent

## API Principal

```http
POST /agents/{agentId}/invoke
GET /agents/{agentId}
Authorization: Bearer <token>
```

## Dependencies

| Dependence | Uso |
|---|---|
| Identity Provider | Authentication and authorisation (OIDC) |
| Agent Runtime | Routing the call |
| Redis | Cache and rate limiting |

## Non-functional requirements

| Requisito | Diretriz |
|---|---|
| Latency | Minimum overhead before routing to Agent Runtime |
| Security | Authentication and authorisation in all applications |
| Escalabilidade | Horizontal scale by volume of invoices |
| Resilience | Rate limiting to protect Agent Runtime against peaks |

## Related Decisions

- [ADR-004 — Agent Runtimewith a stable core and adapters](../adrs/004-agent-runtime-strategy.md)
