# FinOps for IA

FinOps must connect technical consumption, business unit, agent, session and result. limiting the load of the tester does not allow responsibility or omission.

## Cost model

### Care by agent

```text
custo_agente = modelos + embeddings + retrieval + ferramentas + infraestrutura + observabilidade
```

Minimum dimensions: `tenant_id`, `agent_id`, `agent_version`, `environment`, `model`, `provider`, `cost_center` and period.

### Watch for sitting

```text
custo_sessao = soma(tokens_entrada, tokens_saida, chamadas_modelo, retrievals, tools, retries e infraestrutura_alocada)
```

Relacing costs with success of the story, content, conversation, economised time or satisfaction.

## Budget enforcement

Apply limits in bed:

- organisation and cost centre;
- product or area;
- agent and version;
- tenant, user and sitting;
- individual requirements.

Progressive actions: alert, reduce token limit, change model, degrade the face, migrate to a synchroon and block with control answers.

## Seductive cache

Use when semantically equivalent questions generate stable answers. The key must consider tenant, agent, prompt, model, policies and knowledge version. Don't cache personalised, sensitive or dependent responses without appropriate scope.

## Routing for model

Model Gateway must select model by task classification, risk, minimum quality, latability, availability and budget. A common policy:

1. economic model for simple classification and extraction;
2. the standard intermediary model for RAG and tool calling;
3. model advanced for complex or scaloned cases.

## Fallback between models

Fallback should preserve compatibility of tool calling, context size, data policy and minimum quality. Register motive, additional cost and result difference. Don't use fallback to contorn security restrictions.

## recommendated methods

| Medicinal | Uso |
|---|---|
| cost for the sitting concluded | efficacy of a newspaper |
| cost for accepted response | economic quality |
| tokens per phase | a delay of a slut |
| cache rate | economia potencial |
| retries/fallback cost | instability and despair |
| cost per sand | otimisation of integrations |
| budget consumed/proposed | controle preventivo |

## Implementing controls

Emit unused use events, calculate price by versioned table and reconcile estimates with the real weight of the tester. Costs must appear on product dashboards, not just in cloud screen.