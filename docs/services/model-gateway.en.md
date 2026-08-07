# Model Gateway

## General view

Model Gateway centralizes access to foundation models and prevents agents running directly to call witnesses.

## Responsabilidades

- implementing the allowlist of producers, models and regions;
- coding by capacity, cost, reliability, availability and data classification;
- establishing budgets, quotas and token limits;
- executing redaction and entry and exit guards;
- padronizar timeout, retry, circuit breaker e fallback;
- registrating a fetish version of the model, tokens, cost and consistency;
- block models or regions not approved;
- - Supporting single and streaming answers.

## Out of the scuff

- the order of the agent;
- management of the agent catalog;
- business valuation of the response;
- Continuity of conversational memory.

## API interna

```http
POST /internal/v1/model-invocations
Authorization: Bearer <workload-token>
X-Correlation-Id: <uuid>
Content-Type: application/json
```

```json
{
  "agentId": "policy-assistant",
  "agentVersion": "1.0.0",
  "riskClassification": "MEDIUM",
  "dataClassification": "INTERNAL",
  "requestedCapability": "TEXT_GENERATION",
  "stream": false,
  "messages": [
    {"role": "user", "content": "Resuma a política."}
  ],
  "constraints": {
    "maxInputTokens": 8000,
    "maxOutputTokens": 1200,
    "maxCostUsd": 0.05,
    "allowedRegions": ["us-east-1"]
  }
}
```

## roteaing policies

Order of course:

1. compatibility with classification and data retention;
2. model approved for the agent;
3. the availability of the driver;
4. minimum quality recorded;
5. budget restante;
6. - Lower cost in SLO.

## Security

- authentication by identity workload;
- authorisation by agent, model and tenant;
- no proofer secret is exposed to Runtime;
- sensitive prompts are not stored by a pattern;
- logs usam hashes e metadados, nunca secrets;
- 'Cause you're out of the way by guardrails before you return to Runtime.

## Observability

- Please:

- `model.gateway.authorize`
- `model.gateway.route`
- `model.gateway.redact`
- `model.provider.invoke`
- `model.gateway.guardrail`

Minimum methods:

- evocations by type and status;
- entry and exit tokens;
- care by agent and unit;
- a tyre by the driver;
- fallback rate;
- political blockades;
- budget violations.

## Eventos

- `model.invoked`
- `model.fallback.executed`
- `model.policy.blocked`
- `budget.threshold.reached`
