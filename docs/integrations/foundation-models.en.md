# Foundation Models Integration

## Objective

Standardize the consumption of foundation models by platform agents and services.

## Supported providers

- Amazon Bedrock
- Azure OpenAI
- OpenAI
- Anthropic
- Google Gemini

## The Commission shall adopt delegated acts in accordance with Article 21 of this Regulation.

- Model Adapter in the Agent Runtime
- Abstraction by provider and model id
- Fallback between compatible models
- Control of tokens
- Timeout and retry controlled

## Selection criteria

| Criterion of use | Other information |
|---|---|
| Qualidade | Adherence to the use case |
| Latency | Expected response time |
| Custo | Cost of input/output tokens |
| Compliance | Regulatory and data requirements |
| Capacity | Context window, tool calling and multimodality |

## Requirements

- Registration of use by agent
- Observability by model call
- Masking of sensitive data where applicable
- Prompt and reply retention policy
