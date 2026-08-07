# Agent Runtime

## General view

Agent Runtime is the heart of Enterprise AI Platform. He executes agents, orders called for models, consults memory, recovers knowledge, executes via MCP and publics operational events.

## Responsabilidades

- Execute published agents
- Quicken, tools, memory and RAG
- Invocar foundation models
- Using timeout, retry and circuitbreaker policies
- Publicate use, audit and cobranza events
- Acknowledgement of the quality of the response

## Out of the scuff

- Agents' adsorption
- Catalog genus
- Documentary questionnaire
- User-generator system
- consolidated financial calculation

## Principais Componentes Internos

| Componente | Responsabilidade |
|---|---|
| Agent Executor | Control the execution cycle of the agent |
| Prompt Engine | Monta prompts, system instructions e contexto |
| Tool Executor | Executa ferramentas permitidas |
| MCP Client | Integrate with MCP Registry and MCP Servers |
| Memory Adapter | Consult and update memory |
| Knowledge Adapter | Consulta Knowledge Service |
| Model Adapter | Abstrai provedors of LLM |
| Evaluation Adapter | Get answers for evaluation |
| Event Publisher | Publica eventos Kafka |

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
| Agent Registry | - Carrier configuration of agent |
| MCP Registry | Find available tools |
| Knowledge Service | Recuperate knowledge for RAG |
| Memory Service | Persistir contexto conversacional |
| Evaluation Service | Avaliar resposta |
| Foundation Models | Execute infertility |
| Kafka | Publicar eventos |
| Redis | Cache e rate limit |

## Eventos Publicados

- `agent.invoked`
- `tool.executed`
- `evaluation.started`

## Non-functioning requirements

| Requisito | Diretriz |
|---|---|
| Latence | P95 less than 5 for simple agents |
| Resilience | Controlled retry for transit calls |
| Security | Authorisation by agent, tool and scop |
| Observability | Type call and tool call |
| Escalabilidade | horizontal column by volume of calls |
| Auditoria | Complete entry, exit and relevant decisions |

## Related Decisions

- (ADR-004 — Agent Runtime with stable and adaptable nerves)(../adrs/004-agent-runtime-strategy.md)
- [ADR-001 — MCP for tool calling Government)(../adrs/001-mcp-vs-rest.md)
- (ADR-006 — OpenTelemetry as a warning pad)(../adrs/006-observability-strategy.md)
