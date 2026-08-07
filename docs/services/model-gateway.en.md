# Model Gateway

## Overview

Model Gateway centralizes access to foundation models and prevents agents from calling providers directly.

## responsibilities

- apply allowlist of providers, models and regions;
- routing by capacity, cost, latency, availability and data classification;
- validate budgets, quotas and token limits;
- perform redaction and entry and exit guardrails;
- standardize timeout, retry, circuit breaker and fallback;
- register the effective version of the model, tokens, cost and latency;
- blocking unapproved models or regions;
- support synchronous responses and streaming.

## Out of Scope

- orchestration of the agent;
- management of the catalogue of agents;
- response business assessment;
- persistence of conversational memory.

## API internal

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

## Routing policies

Standard order

1. compatibility with classification and residence of data;
2. approved model for the agent;
3. availability of the provider;
4. minimum quality registered;
5. budget restante;
6. lower cost within the SLO.

## Security

- authentication by workload identity;
- authorisation by agent, model and tenant;
- no provider secret is exposed to Runtime;
- sensitive prompts are not stored by pattern;
- logs use hashes and metadata, never secrets;
- outflow through guardrails before returning to Runtime.

## Observability

Compulsory Spans:

- `model.gateway.authorize`
- `model.gateway.route`
- `model.gateway.redact`
- `model.provider.invoke`
- `model.gateway.guardrail`

Minimum metrics:

- claims by model and status;
- input and output tokens;
- cost per agent and unit;
- Provider latency;
- fall rate;
- policy blocks;
- budget violations.

## Events

- `model.invoked`
- `model.fallback.executed`
- `model.policy.blocked`
- `budget.threshold.reached`
