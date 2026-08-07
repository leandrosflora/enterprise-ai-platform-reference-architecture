# Model Gateway

## General view

Model Gateway centralizes access to foundation models and prevents agent runtimes from calling providers directly.

## Responsabilidades

- apply allowlist of providers, models and regions;
- routing by capacity, cost, latency, availability and data classification;
- validate budgets, allowances and limits for tokens;
- carry out redaction and entry and exit guardrails;
- standardise timeout, retry, circuit breaker and fallback;
- record the actual model version, tokens, cost and latency;
- block unapproved models or regions;
- support synchronous responses and streaming.

## Out of scope

- the orchestration of the agent;
- the management of the agent catalogue;
- the response's business assessment;
- persistent conversational memory.

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

## Routing policies

Standard order:

1. compatibility with data classification and residence;
2. the model approved for the agent;
3. availability of the provider;
4. the minimum recorded quality;
5. budget restante;
6. the lower cost within the SLO.

## Security

- the workload identity authentication;
- authorisation by agent, model and tenant;
- No provider secrets are exposed to Runtime;
- sensitive prompts are not stored by default;
- logs use hashes and metadata, never secret;
- exit passes through guardrails before returning to Runtime.

## Observability

Compulsory spans:

- `model.gateway.authorize`
- `model.gateway.route`
- `model.gateway.redact`
- `model.provider.invoke`
- `model.gateway.guardrail`

Minimum metrics:

- invocations by model and status;
- entry and exit tokens;
- cost per agent and unit;
- the latency per provider;
- the fallback rate;
- political blockades;
- Budget violations.

## Events

- `model.invoked`
- `model.fallback.executed`
- `model.policy.blocked`
- `budget.threshold.reached`
