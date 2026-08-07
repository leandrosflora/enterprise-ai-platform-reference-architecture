# Exemplo - Evento Kafka

## Evento `agent.invoked`

```json
{
  "eventId": "evt-001",
  "eventType": "agent.invoked",
  "eventVersion": "1.0.0",
  "occurredAt": "2026-01-01T10:00:00Z",
  "correlationId": "corr-2026-001",
  "causationId": "cmd-001",
  "payload": {
    "agentId": "internal-copilot",
    "agentVersion": "1.0.0",
    "tenantId": "tenant-default",
    "businessUnit": "Atendimento",
    "status": "SUCCESS",
    "latencyMs": 2400,
    "inputTokens": 1200,
    "outputTokens": 350,
    "modelProvider": "bedrock",
    "modelId": "anthropic.claude"
  }
}
```

## Uso

Este evento alimenta:

- Observabilidade
- Auditoria
- FinOps
- Dashboards de adoção
- Métricas por agente e área
