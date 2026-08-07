# Agent Runtime

## Overview

The Agent Runtime is the heart of the Enterprise AI Platform, it executes agents, orchestrates calls for models, consults memory, retrieves knowledge, executes tools via MCP and publishes operational events.

## Responsabilidades

- Implementing published agents
- To orchestrate prompts, tools, memory and RAG
- Invocar foundation models
- Implementing timeout, retry and circuit breaker policies
- Publishing use, audit and charging events
- To activate assessment of response quality

## Out of Scope

- Approval of agents
- Catalogue management
- Document management
- User management
- Consolidated financial calculation

## Principais Componentes Internos

| Componente | Responsabilidade |
|---|---|
| Agent Executor | Checks the worker's execution cycle |
| Prompt Engine | Monta prompts, system instructions and context |
| Tool Executor | Performs allowed tools |
| MCP Client | Integrates with MCP Registry and MCP Servers |
| Memory Adapter | Reads and updates memory |
| Knowledge Adapter | Consulta Knowledge Service |
| Model Adapter | Abstracts MLL providers |
| Evaluation Adapter | Referrals for evaluation |
| Event Publisher | Publish Kafka events |

## API Principal

```http
POST /agents/{agentId}/invoke
Content-Type: application/json
Authorization: Bearer <token>
```

### Request

```json
{
  "input": "Quais contratos vencem este mês?",
  "channel": "ai-portal",
  "sessionId": "session-123",
  "context": {
    "businessUnit": "credit",
    "locale": "pt-BR"
  }
}
```

### Response

```json
{
  "conversationId": "conv-123",
  "messageId": "msg-456",
  "answer": "Foram encontrados 12 contratos com vencimento neste mês.",
  "citations": [],
  "toolCalls": [],
  "evaluationStatus": "queued"
}
```

## Dependencies

| Dependence | Use |
|---|---|
| Agent Registry | Load the agent configuration |
| MCP Registry | Discovering available tools |
| Knowledge Service | Recovering knowledge for RAG |
| Memory Service | Persist conversational context |
| Evaluation Service | Evaluating response |
| Foundation Models | Perform inference |
| Kafka | Publicate events |
| Redis | Cache and rate limit |

## Publicated events

- `agent.invoked`
- `tool.executed`
- `evaluation.started`

## Non-functional requirements

| Requirements | Guideline |
|---|---|
| Latency | P95 less than 5s for simple agents |
| Resilience | Controlled retry for transient calls |
| Security | Authorisation by agent, tool and scope |
| Observability | Trace por invocation, model call and tool call |
| Escalabilidade | Horizontal scale per volume of invocations |
| Audit | Complete entry, exit and relevant decision record |

## Related Decisions

- [ADR-004 — Agent Runtime with stable core and adapters](../adrs/004-agent-runtime-strategy.md)
- [ADR-001 — MCP for governed tool calling](../adrs/001-mcp-vs-rest.md)
- [ADR-006 — OpenTelemetry as observability standard](../adrs/006-observability-strategy.md)
