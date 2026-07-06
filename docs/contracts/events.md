# Contratos de Eventos

Este documento define os principais eventos assíncronos da Enterprise AI Platform.

## Padrões

- Formato: JSON
- Transporte: Kafka
- Versionamento: `schemaVersion`
- Identificação: `eventId`, `correlationId`, `causationId`
- Data/hora: ISO 8601 UTC
- Estratégia de erro: DLQ por domínio

## Envelope Padrão

```json
{
  "eventId": "uuid",
  "eventType": "agent.invoked",
  "schemaVersion": "1.0.0",
  "occurredAt": "2026-07-06T00:00:00Z",
  "correlationId": "uuid",
  "causationId": "uuid",
  "tenantId": "organization-id",
  "source": "agent-runtime",
  "payload": {}
}
```

## Tópicos

| Evento | Produtor | Consumidores | Finalidade |
|---|---|---|---|
| `agent.created` | Agent Registry | Governance Service, Audit Service | Registrar criação de agente |
| `agent.updated` | Agent Registry | Governance Service, Audit Service | Registrar alteração de metadados |
| `agent.published` | Governance Service | Agent Registry, Audit Service | Publicar agente aprovado |
| `agent.retired` | Governance Service | Agent Registry, Audit Service | Retirar agente de operação |
| `agent.invoked` | Agent Runtime | Audit Service, Billing Service, Evaluation Service | Registrar execução de agente |
| `tool.executed` | Agent Runtime | Audit Service, Billing Service | Registrar execução de ferramenta |
| `knowledge.ingested` | Knowledge Service | Audit Service | Registrar ingestão de conhecimento |
| `embedding.generated` | Knowledge Service | Audit Service, Billing Service | Registrar geração de embedding |
| `document.indexed` | Knowledge Service | Audit Service | Registrar indexação vetorial |
| `memory.updated` | Memory Service | Audit Service | Registrar atualização de memória |
| `evaluation.started` | Evaluation Service | Audit Service | Registrar início de avaliação |
| `evaluation.completed` | Evaluation Service | Governance Service, Audit Service | Registrar resultado de avaliação |
| `governance.approved` | Governance Service | Agent Registry, Audit Service | Aprovar agente ou versão |
| `governance.rejected` | Governance Service | Agent Registry, Audit Service | Rejeitar agente ou versão |
| `audit.created` | Audit Service | Observability Stack | Registrar trilha de auditoria |

## Exemplo: agent.invoked

```json
{
  "eventId": "7d8cf2aa-ef5f-4cc3-bafa-61ea26277511",
  "eventType": "agent.invoked",
  "schemaVersion": "1.0.0",
  "occurredAt": "2026-07-06T12:00:00Z",
  "correlationId": "b884f86e-8107-4266-98f3-e116a62efed0",
  "causationId": "b884f86e-8107-4266-98f3-e116a62efed0",
  "tenantId": "enterprise",
  "source": "agent-runtime",
  "payload": {
    "agentId": "credit-agent",
    "agentVersion": "1.0.0",
    "channel": "ai-portal",
    "userId": "user-123",
    "modelProvider": "bedrock",
    "modelId": "anthropic.claude",
    "inputTokens": 1250,
    "outputTokens": 430,
    "latencyMs": 2850,
    "status": "succeeded"
  }
}
```

## Retenção

| Classe | Retenção | Observação |
|---|---:|---|
| Auditoria | 5 anos | Conforme política regulatória |
| Uso e cobrança | 24 meses | Base para chargeback/showback |
| Operacional | 90 dias | Diagnóstico e troubleshooting |
| DLQ | 30 dias | Reprocessamento controlado |
