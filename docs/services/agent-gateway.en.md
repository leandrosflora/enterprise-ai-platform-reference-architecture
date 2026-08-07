# Agent Gateway

## Overview

The Agent Gateway is the only entry point for agent invocations. It authorizes and authorizes the call, applies rate limiting and routs the invocation to the Agent Runtime.

## Responsabilidades

- Exposing the public IPA for the invoking of officials
- Authenticate requisitions via Identity Provider (OIDC)
- Authorizing access by agent and scope
- Applying short-term rate limiting and cache
- Turning the invocation to the Agent Runtime

## Out of Scope

- Implementation of the agent and orchestration of prompts, tools and memory
- Evaluation of response quality
- Approval and life cycle of the agent

## API Principal

```http
POST /agents/{agentId}/invoke
GET /agents/{agentId}
Authorization: Bearer <token>
```

## Dependencies

| Dependence | Use |
|---|---|
| Identity Provider | Authentication and authorisation (ICO) |
| Agent Runtime | Rotating of the invocation |
| Redis | Cache and rate limiting |

## Non-functional requirements

| Requirements | Guideline |
|---|---|
| Latency | Minimum overhead before routing to Agent Runtime |
| Security | Authentication and authorisation in all requests |
| Escalabilidade | Horizontal scale per volume of invocations |
| Resilience | Rate limiting to protect Agent Runtime from peaks |

## Related Decisions

- [ADR-004 — Agent Runtime with stable core and adapters](../adrs/004-agent-runtime-strategy.md)
