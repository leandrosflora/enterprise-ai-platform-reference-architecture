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
- Token control
- Timeout and controlled retry

## Selection Criteria

| Criteria | Description |
|---|---|
| Quality | Adherence to use case |
| Latency | Expected response time |
| Cost | Cost per input/output tokens |
| Compliance | Regulatory and data requirements |
| Capacity | Context window, tool calling and multimodality |

## Requirements

- Registry of use by agent
- Observability by model call
- Sensitive data masking when applicable
- Prompts retention policy and responses
