# Foundation Models Integration

## Objet

Increasing the use of basic models by agents and services of the platform.

## Provedores Suportados

- Amazon Bedrock
- Azure OpenAI
- OpenAI
- Anthropic
- Google Gemini

## Integrating Pads

- Model Adapter in Agent Runtime
- Absorption by provider and model id
- Fallback between compatible models
- Control of tokens
- Timeout e retry controlado

## Selection criteria

| Criteria | Description |
|---|---|
| Qualidade | Adhosion to the case of use |
| Latence | Time of response |
| Custo | Cost per input/output token |
| Compliance | Regulations and data requirements |
| Capacidade | Context window, tool calling e multimodalidade |

## Requirements

- Use register by agent
- Observability by type
- Sensible data masking when applicable
- Retention policy of prompt responses
