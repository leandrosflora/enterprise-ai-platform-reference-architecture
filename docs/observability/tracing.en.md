# Tracing, Machines and SLOs

## Father

- OpenTelemetry for trace, tracing and corralled logs.
- W3C `traceparent` propagated by HTTP and in the envelope Kafka.
- `traceId`, `spanId`, `correlationId`, `causationId` and `tenant.id` on the applicable borders.
- Logs stored in JSON.
- Sensible data are wiped before export.

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

## - Please, please.

| Span | Componente | Obligatory attributes |
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

| Atributo | Regra |
|---|---|
| `tenant.id` | Thank you, without free cardinality. |
| `business_unit` | When applicable. |
| `agent.id` e `agent.version` | Thank you for the execution of the agent. |
| `session.id.hash` | Hash, it's never felt as if it was. |
| `user.id.hash` | It's stable only when necessary. |
| `data.classification` | `PUBLIC`, `INTERNAL`, `CONFIDENTIAL`, `RESTRICTED`. |
| `risk.classification` | `LOW`, `MEDIUM`, `HIGH`, `CRITICAL`. |
| `workload.class` | Class defined in the NFRs. |

## Mechanics

| Medicinal | Tipo | authorised dimensions |
|---|---|---|
| `agent_invocations_total` | Counter | Agent, tenant, status |
| `agent_invocation_duration_seconds` | Histogram | Agent, workload, status |
| `policy_decision_duration_seconds` | Histogram | policy, decision |
| `policy_denials_total` | Counter | policy, recurso, motivo controlado |
| `model_invocations_total` | Counter | driver, model, status |
| `model_tokens_total` | Counter | - a driver, model, type |
| `model_cost_usd_total` | Counter | Agent, unit, driver |
| `model_fallback_total` | Counter | provedor origem/destino |
| `tool_executions_total` | Counter | ferramenta, status, risco |
| `knowledge_retrieval_duration_seconds` | Histogram | base, strategy |
| `knowledge_authorization_filtered_total` | Counter | base, classification |
| `evaluation_score` | Gauge | agent, dataset, method |
| `dlq_events_total` | Counter | evento, consumidor |

Don't use user IDs, session, document or ID correlation as metric labels.

## SLOs reference

| Capacidade | SLI | SLO | Janela |
|---|---|---:|---|
| `INTERACTIVE_SIMPLE` | P95 end-to-end | <= 5 s | 30 dias |
| `INTERACTIVE_RAG` | P95 end-to-end | <= 8 s | 30 dias |
| `INTERACTIVE_TOOL` | P95 end-to-end | <= 15 s | 30 dias |
| Sncron operation | P95 of ac | <= 2 s | 30 dias |
| Knowledge retrieval | P95 | <= 2 s | 30 dias |
| Policy decision | P95 | <= 100 ms | 30 dias |
| Agent Gateway | Disponibilidade | >= 99,95% | 30 dias |
| Agent Runtime | Disponibilidade | >= 99,9% | 30 dias |
| Event publishing | Sucesso | >= 99,9% | 30 dias |
| Critical audit | Sucesso | >= 99,99% | 30 dias |

## Alertas

| Alerta | Condition | Severidade | Runbook |
|---|---|---|---|
| AgentErrorRateHigh | error > 5% for 10 min | Alta | troubleshooting-agent-invocation |
| SloBurnRateFast | burn rate > 14,4x for 5 min | Critics | troubleshooting-agent-invocation |
| ModelProviderLatencyHigh | P95 > limit for 15 min | Medicine | a tampering |
| ToolExecutionFailures | - 3% for 10 min | Alta | - Deabilitating critical tool |
| PolicyDenialsSpike | > 3x baseline | Medicine | Re-examine abuse/configure |
| CostBudgetExceeded | budget >= 100% | Alta | block/degrade agent |
| AuditRecordingFailure | any failure for 5 min | Critics | reducing critical actions |
| DLQBacklogGrowing | a growing backlog for 15 min | Alta | reprocessamento controlado |

## Telemetry safety

- not to register complete prompt with personal data or classification `CONFIDENTIAL`/`RESTRICTED`;
- mascarar CPF, e-mail, telefone, tokens, secrets e identificadores financeiros;
- auditory preserves functional evidence, not a brute-sensible payload;
- trace uses technical IDs or hashes;
- access to sensitive trace requires authorization and is audited.
