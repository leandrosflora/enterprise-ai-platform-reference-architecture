# Example - Evaluation Result

## Objective

Example of results produced by Evaluation Service after an invocation of agent.

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

The result is used for:

- Approval of staff
- Regression between versions
- Quality monitoring
- Governance evidence
- Degradation alerts
