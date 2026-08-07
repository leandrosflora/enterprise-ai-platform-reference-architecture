# Tracing, Metrics and SLOs

## Standard

- OpenTelemetry for traces, metrics and related logs.
- W3C `traceparent` propagated by HTTP and in the envelope Kafka.
- `traceId`, `spanId`, `correlationId`, `causationId`and `tenant.id`within the applicable borders.
- Logs structured in JSON.
- Sensitive data are masked before export.

## Trace principal

```text
agent.invocation
  ├─ agent.gateway.authenticate
  ├─ agent.gateway.authorize
  ├─ agent.runtime.load_configuration
  ├─ policy.evaluate
  ├─ memory.retrieve
  ├─ knowledge.retrieve
  │   ├─ knowledge.authorize_documents
  │   ├─ knowledge.embedding.generate
  │   └─ knowledge.vector_search
  ├─ prompt.build
  ├─ model.gateway.authorize
  ├─ model.gateway.route
  ├─ model.provider.invoke
  ├─ model.gateway.guardrail
  ├─ tool.execute
  │   ├─ mcp.registry.discover
  │   ├─ policy.evaluate_tool
  │   └─ mcp.tool.invoke
  ├─ evaluation.submit
  ├─ event.publish
  └─ audit.record
```

## Compulsory spans

| Span | Component | Compulsory attributes |
|---|---|---|
| `agent.invocation` | Gateway | `agent.id`, `agent.version`, `tenant.id`, `channel`, `workload.class`, `risk.classification` |
| `agent.gateway.authenticate` | Gateway | `auth.provider`, `auth.result` |
| `agent.gateway.authorize` | Gateway | `auth.scopes`, `policy.id`, `policy.version`, `policy.decision` |
| `agent.runtime.load_configuration` | Runtime | `agent.id`, `agent.version`, `registry.cache_hit` |
| `policy.evaluate` | PDP/PEP | `policy.id`, `policy.version`, `decision`, `reason` |
| `memory.retrieve` | Memory | `session.id.hash`, `memory.type`, `memory.items_count`, `data.classification` |
| `memory.write` | Memory | `session.id.hash`, `operation`, `ttl.seconds`, `data.classification` |
| `knowledge.retrieve` | Knowledge | `knowledge_base.id`, `retrieval.strategy`, `top_k` |
| `knowledge.authorize_documents` | Knowledge | `candidate.count`, `authorized.count`, `policy.version` |
| `knowledge.embedding.generate` | Knowledge | `model.id`, `input.tokens` |
| `knowledge.vector_search` | Knowledge | `vector.index`, `result.count`, `score.max` |
| `prompt.build` | Runtime | `prompt.template_id`, `context.sources_count`, `input.tokens.estimated` |
| `model.gateway.authorize` | Model Gateway | `model.capability`, `data.classification`, `policy.decision` |
| `model.gateway.route` | Model Gateway | `provider.selected`, `model.selected`, `region.selected`, `fallback.rank` |
| `model.provider.invoke` | Model Gateway | `model.provider`, `model.id`, `input.tokens`, `output.tokens`, `cost.usd` |
| `model.gateway.guardrail` | Model Gateway | `guardrail.id`, `guardrail.version`, `decision` |
| `tool.execute` | Runtime | `tool.name`, `tool.version`, `tool.status`, `tool.risk` |
| `mcp.tool.invoke` | MCP Server | `tool.name`, `idempotency.required`, `operation.id`, `status` |
| `evaluation.submit` | Evaluation | `evaluation.type`, `dataset.id`, `status` |
| `event.publish` | Event backbone | `messaging.destination`, `event.type`, `schema.version` |
| `audit.record` | Audit | `audit.event_type`, `retention.class`, `audit.status` |

## Atributos globais

| Atributo | Rule |
|---|---|
| `tenant.id` | Compulsory, without free cardinality. |
| `business_unit` | Where applicable. |
| `agent.id`and `agent.version` | Compulsory in the execution of an agent. |
| `session.id.hash` | Hash, never a sensitive session in the clear. |
| `user.id.hash` | Hash is stable only when necessary. |
| `data.classification` | `PUBLIC`, `INTERNAL`, `CONFIDENTIAL`, `RESTRICTED`. |
| `risk.classification` | `LOW`, `MEDIUM`, `HIGH`, `CRITICAL`. |
| `workload.class` | Class defined in NFRs. |

## The following information shall be provided:

| Other information | Tipo | Permitted dimensions |
|---|---|---|
| `agent_invocations_total` | Counter | the number of employees, the number of employees, the number of employees, the number of employees |
| `agent_invocation_duration_seconds` | Histogram | the number of employees, the workload, the status |
| `policy_decision_duration_seconds` | Histogram | policy, decision |
| `policy_denials_total` | Counter | policy, recurso, motivo controlado |
| `model_invocations_total` | Counter | Provider, model, status |
| `model_tokens_total` | Counter | Supplier, model, type |
| `model_cost_usd_total` | Counter | The following information shall be provided: |
| `model_fallback_total` | Counter | origin/destination provider |
| `tool_executions_total` | Counter | ferramenta, status, risco |
| `knowledge_retrieval_duration_seconds` | Histogram | Basics, strategy |
| `knowledge_authorization_filtered_total` | Counter | Based, classification |
| `evaluation_score` | Gauge | The following information shall be provided: |
| `dlq_events_total` | Counter | event, consumer |

Do not use user, session, document or correlation IDs as metric labels.

## SLOsof reference

| Capacity | SLI | SLO | Janela |
|---|---|---:|---|
| `INTERACTIVE_SIMPLE` | P95 end-to-end | <= 5 s | 30 dias |
| `INTERACTIVE_RAG` | P95 end-to-end | <= 8 s | 30 dias |
| `INTERACTIVE_TOOL` | P95 end-to-end | <= 15 s | 30 dias |
| Asynchronous operation | P95 of oil | <= 2 s | 30 dias |
| Knowledge retrieval | P95 | <= 2 s | 30 dias |
| Policy decision | P95 | <= 100 ms | 30 dias |
| Agent Gateway | Disponibilidade | >= 99,95% | 30 dias |
| Agent Runtime | Disponibilidade | >= 99,9% | 30 dias |
| Event publishing | Sucesso | >= 99,9% | 30 dias |
| Critical audit recording | Sucesso | >= 99,99% | 30 dias |

## Alertas

| Alerta | Condition | Severidade | Runbook |
|---|---|---|---|
| AgentErrorRateHigh | error > 5% for 10 min | Alta | troubleshooting-agent-invocation |
| SloBurnRateFast | burn rate > 14.4x per 5 min | Criticism | troubleshooting-agent-invocation |
| ModelProviderLatencyHigh | P95 > limit for 15 min | Average | the default of the supplier |
| ToolExecutionFailures | Failure > 3% for 10 min | Alta | disable critical tool |
| PolicyDenialsSpike | > 3x baseline | Average | Reviewing the abuse/configuration |
| CostBudgetExceeded | budget >= 100% | Alta | blocking/degrading agent |
| AuditRecordingFailure | Any failure for 5 min | Criticism | pause critical actions |
| DLQBacklogGrowing | Growing backlog by 15 min | Alta | reprocessamento controlado |

## Telemetry security

- not register a complete prompt with personal data or classification `CONFIDENTIAL`/`RESTRICTED`;
- The Commission shall adopt delegated acts in accordance with Article 21 of Regulation (EU) No 182/2011 of the European Parliament and of the Council [3].
- the audit preserves functional evidence, not gross sensitive payload;
- traces use technical IDs or hashes;
- access to sensitive traces requires authorisation and is audited.
