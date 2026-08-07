# Foundation Models Integration

## Objective

Standardizing the consumption of foundational models by platform agents and services.

## Provedores Suportados

- Amazon Bedrock
- Azure OpenAI
- OpenAI
- Anthropic
- Google Gemini

## Integration Patterns

- Model Adapter no Agent Runtime
- Abstraction by provider and model id
- Fallback between compatible models
- Controle de tokens
- Timeout e retry controlado

## Selection Criteria

| Criteria | Description |
|---|---|
| Quality | Adherence to use case |
| Latency | Tempo de resposta esperado |
| Cost | Cost per input/output tokens |
| Compliance | Regulatory and data requirements |
| Capacity | Context window, tool calling e multimodalidade |

## Requirements

- Registry of use by agent
- Observability by model call
- Sensitive data masking when applicable
- Prompts retention policy and responses
