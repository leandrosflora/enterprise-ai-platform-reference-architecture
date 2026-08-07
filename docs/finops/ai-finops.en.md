# FinOps for AI

FinOps must connect technical consumption, business unit, agent, session and result; measuring only the provider's invoice does not allow for accountability or optimization.

## Cost model

### Cost per agent

```text
custo_agente = modelos + embeddings + retrieval + ferramentas + infraestrutura + observabilidade
```

Minimum dimensions: `tenant_id`, `agent_id`, `agent_version`, `environment`, `model`, `provider`, `cost_center` and period.

### Cost per session

```text
custo_sessao = soma(tokens_entrada, tokens_saida, chamadas_modelo, retrievals, tools, retries e infraestrutura_alocada)
```

Relating cost with successful workload, containment, conversion, saved time or satisfaction.

## Budget enforcement

Application of layered boundaries:

- organization and cost center;
- product or domain;
- agent and version;
- tenant, user and session;
- individual requisition.

Progressive actions: alert, reduce token limit, change model, disabling expensive tools, migrating to asynchronous and blocking with controlled response.

## Semantic cache

Use when semantically equivalent questions generate stable responses. The key should consider tenant, agent, version of the prompt, model, policies and version of knowledge. Do not cache customized, sensitive, or state-dependent responses without adequate scope.

## Routing per model

The Model Gateway must select model by task classification, risk, minimum quality, latency, availability and budget. A common policy:

1. economic model for classification and simple extraction;
2. intermediate model for RAG and common tool calling;
3. advanced model for complex or scaled cases.

## Fallback between models

Fallback should preserve tool calling compatibility, context size, data policy and minimum quality. Register reason, additional cost and outcome difference. Do not use fallback to circumvent security restrictions.

## Recommended metrics

| Metrics | Uso |
|---|---|
| cost per session completed | workload efficiency |
| cost per accepted response | economic quality |
| tokens per step | detection of swollen prompts |
| cache rate | potential economy |
| Retries/fallback cost | Unstableness and waste |
| cost per tool | Integration optimization |
| budget consumed/projected | control preventivo |

## Implementing controls

Issue standardized use events, calculate price per scale and reconcile estimates with the actual invoice of the provider.Costs should appear in the product dashboards, not only in the cloud panel.