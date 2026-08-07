# Agent Runtime

## General view

Agent Runtime is the heart of Enterprise AI Platform. It runs agents, orchestrates model calls, query memory, retrieves knowledge, runs tools via MCP, and publishes operational events.

## Responsabilidades

- Execute published agents
- Orchestrating prompts, tools, memory and RAG
- Invocar foundation models
- Apply timeout, retry and circuit breaker policies
- Publishing use, audit and collection events
- Activate the quality assessment of the response

## Out of scope

- Approval of agents
- Catalogue management
- Documentary intake
- Management of users
- Consolidated financial calculation

## Main internal components

| Component | Responsabilidade |
|---|---|
| Agent Executor | Controls the execution cycle of the agent |
| Prompt Engine | Install prompts, system instructions and context |
| Tool Executor | Executa ferramentas permitidas |
| MCP Client | It is integrated with MCP Registry and MCP Servers |
| Memory Adapter | Check and update memory |
| Knowledge Adapter | Consulta Knowledge Service |
| Model Adapter | Abstracts from LLM suppliers |
| Evaluation Adapter | Send responses for evaluation |
| Event Publisher | Publishing events Kafka |

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
| Agent Registry | Loading the agent configuration |
| MCP Registry | Discover the tools available |
| Knowledge Service | Recover knowledge for RAG |
| Memory Service | Persistir contexto conversacional |
| Evaluation Service | Avaliar resposta |
| Foundation Models | Running inference |
| Kafka | Publishing events |
| Redis | Cache and rate limit |

## Events Published

- `agent.invoked`
- `tool.executed`
- `evaluation.started`

## Non-functional requirements

| Requisito | Diretriz |
|---|---|
| Latency | P95 less than 5s for simple agents |
| Resilience | Retry controlled for transient calls |
| Security | Authorization by agent, tool and scope |
| Observability | Invocation, model call and tool call trace |
| Escalabilidade | Horizontal scale by volume of invoices |
| Auditoria | Complete entry, exit and relevant decisions record |

## Related Decisions

- [ADR-004 — Agent Runtimewith a stable core and adapters](../adrs/004-agent-runtime-strategy.md)
- [ADR-001 — MCPto tool calling governado](../adrs/001-mcp-vs-rest.md)
- [ADR-006 — OpenTelemetryas a standard of observability](../adrs/006-observability-strategy.md)
