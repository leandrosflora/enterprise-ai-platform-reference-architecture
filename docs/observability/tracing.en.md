# Tracing, Metrics and SLOs

## Pattern

- OpenTelemetry for traces, metrics and correlated logs.
- W3C `traceparent` propagado por HTTP e no envelope Kafka.
- `traceId`, `spanId`, `correlationId`, `causationId` e `tenant.id` at the applicable borders.
- Logs estruturados em JSON.
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

## Compulsory Spans

| Span | Componente | Compulsory attributes |
|---|---|---|
|  `agent.invocation`  | Gateway |  `agent.id`, `agent.version`, `tenant.id`, `channel`, `workload.class`, `risk.classification`  |
|  `agent.gateway.authenticate`  | Gateway |  `auth.provider`, `auth.result`  |
|  `agent.gateway.authorize`  | Gateway |  `auth.scopes`, `policy.id`, `policy.version`, `policy.decision`  |
|  `agent.runtime.load_configuration`  | Runtime |  `agent.id`, `agent.version`, `registry.cache_hit`  |
|  `policy.evaluate`  | PDP/PEP |  `policy.id`, `policy.version`, `decision`, `reason`  |
|  `memory.retrieve`  | Memory |  `session.id.hash`, `memory.type`, `memory.items_count`, `data.classification`  |
|  `memory.write`  | Memory |  `session.id.hash`, `operation`, `ttl.seconds`, `data.classification`  |
|  `knowledge.retrieve`  | Knowledge |  `knowledge_base.id`, `retrieval.strategy`, `top_k`  |
|  `knowledge.authorize_documents`  | Knowledge |  `candidate.count`, `authorized.count`, `policy.version`  |
|  `knowledge.embedding.generate`  | Knowledge |  `model.id`, `input.tokens`  |
|  `knowledge.vector_search`  | Knowledge |  `vector.index`, `result.count`, `score.max`  |
|  `prompt.build`  | Runtime |  `prompt.template_id`, `context.sources_count`, `input.tokens.estimated`  |
|  `model.gateway.authorize`  | Model Gateway |  `model.capability`, `data.classification`, `policy.decision`  |
|  `model.gateway.route`  | Model Gateway |  `provider.selected`, `model.selected`, `region.selected`, `fallback.rank`  |
|  `model.provider.invoke`  | Model Gateway |  `model.provider`, `model.id`, `input.tokens`, `output.tokens`, `cost.usd`  |
|  `model.gateway.guardrail`  | Model Gateway |  `guardrail.id`, `guardrail.version`, `decision`  |
|  `tool.execute`  | Runtime |  `tool.name`, `tool.version`, `tool.status`, `tool.risk`  |
|  `mcp.tool.invoke`  | MCP Server |  `tool.name`, `idempotency.required`, `operation.id`, `status`  |
|  `evaluation.submit`  | Evaluation |  `evaluation.type`, `dataset.id`, `status`  |
|  `event.publish`  | Event backbone |  `messaging.destination`, `event.type`, `schema.version`  |
|  `audit.record`  | Audit |  `audit.event_type`, `retention.class`, `audit.status`  |

## Atributos globais

| Atributo | Regra |
|---|---|
|  `tenant.id`  | Obligatory, without free cardinality. |
|  `business_unit`  | When applicable. |
|  `agent.id` e `agent.version`  | Obligations in the execution of a staff member. |
|  `session.id.hash`  | Hash, never sensitive session clearly. |
|  `user.id.hash`  | Stable Hash only when necessary. |
|  `data.classification`  |  `PUBLIC`, `INTERNAL`, `CONFIDENTIAL`, `RESTRICTED`. |
|  `risk.classification`  |  `LOW`, `MEDIUM`, `HIGH`, `CRITICAL`. |
|  `workload.class`  | Classe definida nos NFRs. |

## Metrics

| Metrics | Tipo | Dimensions permitted |
|---|---|---|
|  `agent_invocations_total`  | Counter | agent, tenant, status |
|  `agent_invocation_duration_seconds`  | Histogram | agent, workload, status |
|  `policy_decision_duration_seconds`  | Histogram | policy, decision |
|  `policy_denials_total`  | Counter | policy, recurso, motivo controlado |
|  `model_invocations_total`  | Counter | provider, model, status |
|  `model_tokens_total`  | Counter | provider, model, type |
|  `model_cost_usd_total`  | Counter | agent, unit, provider |
|  `model_fallback_total`  | Counter | provedor origem/destino |
|  `tool_executions_total`  | Counter | tool, status, risk |
|  `knowledge_retrieval_duration_seconds`  | Histogram | basis, strategy |
|  `knowledge_authorization_filtered_total`  | Counter | basis, classification |
|  `evaluation_score`  | Gauge | agent, dateset, metric |
|  `dlq_events_total`  | Counter | evento, consumidor |

Do not use user, session, document or correlation IDs as metric labels.

## Reference SLOs

| Capacity | SLI | SLO | Janela |
|---|---|---:|---|
|  `INTERACTIVE_SIMPLE`  | P95 end-to-end | <= 5 s | 30 dias |
|  `INTERACTIVE_RAG`  | P95 end-to-end | <= 8 s | 30 dias |
|  `INTERACTIVE_TOOL`  | P95 end-to-end | <= 15 s | 30 dias |
| Asynchronous operation | P95 de aceite | <= 2 s | 30 dias |
| Knowledge retrieval | P95 | <= 2 s | 30 dias |
| Policy decision | P95 | <= 100 ms | 30 dias |
| Agent Gateway | Disponibilidade | >= 99,95% | 30 dias |
| Agent Runtime | Disponibilidade | >= 99,9% | 30 dias |
| Event publishing | Sucesso | >= 99,9% | 30 dias |
| Audit recording crítico | Sucesso | >= 99,99% | 30 dias |

## Alertas

| Alerta | Condition | Severidade | Runbook |
|---|---|---|---|
| AgentErrorRateHigh | erro > 5% por 10 min | Alta | troubleshooting-agent-invocation |
| SloBurnRateFast | burn rate > 14,4x por 5 min | Criticism | troubleshooting-agent-invocation |
| ModelProviderLatencyHigh | P95 > limite por 15 min | Mean | fallback de provedor |
| ToolExecutionFailures | falha > 3% por 10 min | Alta | disabling critical tool |
| PolicyDenialsSpike | > 3x baseline | Mean | Review abuse/configuration |
| CostBudgetExceeded | budget >= 100% | Alta | blocking/degrading agent |
| AuditRecordingFailure | qualquer falha por 5 min | Criticism | stop critical actions |
| DLQBacklogGrowing | backlog crescente por 15 min | Alta | reprocessamento controlado |

## Safety of telemetry

- not register the full prompt with personal data or classification `CONFIDENTIAL`/`RESTRICTED`;
- mascarar CPF, e-mail, telefone, tokens, secrets e identificadores financeiros;
- audit preserves functional evidence, not payload gross sensitive;
- traces use technical IDs or hashes;
- access to sensitive traces requires authorization and is audited.
