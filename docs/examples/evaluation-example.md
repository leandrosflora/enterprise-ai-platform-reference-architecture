# Exemplo - Resultado de Avaliação

## Objetivo

Exemplo de resultado produzido pelo Evaluation Service após uma invocação de agente.

```json
{
  "evaluationId": "eval-001",
  "correlationId": "corr-2026-001",
  "agentId": "internal-copilot",
  "agentVersion": "1.0.0",
  "status": "COMPLETED",
  "metrics": {
    "groundedness": 0.92,
    "relevance": 0.88,
    "hallucinationRisk": 0.08,
    "toxicity": 0.01,
    "safety": 0.97
  },
  "decision": "APPROVED",
  "evidence": {
    "documentsUsed": ["policy-001", "faq-003"],
    "evaluationDataset": "internal-copilot-regression-v1"
  }
}
```

## Uso

O resultado é usado para:

- Aprovação de agentes
- Regressão entre versões
- Monitoramento de qualidade
- Evidência de governança
- Alertas de degradação
