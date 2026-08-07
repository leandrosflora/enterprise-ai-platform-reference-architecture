# Agent Runtime

## Overview

The Agent Runtime is the heart of the Enterprise AI Platform, it executes agents, orchestrates calls for models, consults memory, retrieves knowledge, executes tools via MCP and publishes operational events.

## Responsabilidades

- Implementing published staff
- To orchestrate prompts, tools, memory and RAG
- Invocar foundation models
- Implementing timeout, retry and circuit breaker policies
- Publishing use, audit and charging events
- To activate assessment of response quality

## Fora de Escopo

- Approval of staff
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
| MCP Client | Integra com MCP Registry e MCP Servers |
| Memory Adapter | Reads and updates memory |
| Knowledge Adapter | Consulta Knowledge Service |
| Model Adapter | Abstrai provedores de LLM |
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

| Dependence | Uso |
|---|---|
| Agent Registry | Load the agent configuration |
| MCP Registry | Discovering available tools |
| Knowledge Service | Recovering knowledge for AGR |
| Memory Service | Persist conversational context |
| Evaluation Service | Avaliar resposta |
| Foundation Models | Perform inference |
| Kafka | Publicate events |
| Redis | Cache e rate limit |

## Publicated events

- `agent.invoked`
- `tool.executed`
- `evaluation.started`

## Non-functional requirements

| Requisito | Diretriz |
|---|---|
| Latency | P95 less than 5s for simple agents |
| Resilience | Controlled retry for transient calls |
| Security | Authorisation by agent, tool and scope |
| Observability | Trace por invocation, model call e tool call |
| Escalabilidade | Horizontal scale per volume of invocations |
| Auditoria | Complete entry, exit and relevant decision record |

## Related Decisions

- [ADR-004 — Agent Runtime with stable core and adapters](../adrs/004-agent-runtime-strategy.md)
- [ADR-001 — MCP para tool calling governado](../adrs/001-mcp-vs-rest.md)
- [ADR-006 — OpenTelemetry as observability standard](../adrs/006-observability-strategy.md)
