# FinOpsfor AI

FinOps must connect technical consumption, business unit, agent, session and result.

## Cost model

### Cost per agent

```text
custo_agente = modelos + embeddings + retrieval + ferramentas + infraestrutura + observabilidade
```

The minimum dimensions are `tenant_id`, `agent_id`, `agent_version`, `environment`, `model`, `provider`, `cost_center` and the period.

### Cost per session

```text
custo_sessao = soma(tokens_entrada, tokens_saida, chamadas_modelo, retrievals, tools, retries e infraestrutura_alocada)
```

Relate cost to journey success, containment, conversion, time saved or satisfaction.

## Budget enforcement

Apply layered limits:

- organisation and cost centre;
- product or domain;
- agent and version;
- tenant, user and session;
- individual request.

Progressive actions: alert, reduce token limit, change model, disable expensive tools, migrate to asynchronous and block with controlled response.

## Caching semantics

Use when semantically equivalent questions generate stable answers. The key should consider tenant, agent, prompt version, model, policies and knowledge version. Do not hide personalized, sensitive or state-dependent answers without adequate scope.

## Routing by model

The Model Gateway shall select the model by task classification, risk, minimum quality, latency, availability and budget.

1. the economic model for simple classification and extraction;
2. the intermediate model for the common RAG and tool calling;
3. advanced model for complex or staggered cases.

## Fallback between models

Fallback must preserve tool calling compatibility, context size, data policy and minimum quality. Record reason, additional cost and result difference. Do not use fallback to circumvent security restrictions.

## Recommended metrics

| Other information | Uso |
|---|---|
| Cost per session completed | Travel efficiency |
| Cost per accepted response | economic quality |
| tokens by stage | detection of swollen prompts |
| Cache rate | economia potencial |
| the cost of retries/fallback | instability and waste |
| Cost per tool | Optimization of integrations |
| Budget used/designed | controle preventivo |

## Implementation controls

Broadcast standardized usage events, calculate price per versioned table, and reconcile estimates with the actual invoice of the provider. Costs should appear in product dashboards, not just in the cloud panel.