# Contracts for Events

## Canonical source

The file [`async-api.yaml`](async-api.yaml) is the executable source of events. This document defines normative conventions. Examples and implementations cannot create alternative envelopes or enums.

## Transport and versioning

- Reference transport: Kafka.
- Reference serialization: JSON UTF-8.
- Topics use the format `<evento>.v<major>`, for example `agent.invoked.v1`.
- `schemaVersion` usa SemVer.
- Uncompatible changes require a new major and a new topic.
- Producers don't remove fields during a major's lifetime.
- Consumidores ignoram campos desconhecidos.

## Compulsory envelope

```json
{
  "eventId": "8dcf94dc-0af0-4f99-95d9-e617424b2c4b",
  "eventType": "agent.invoked",
  "schemaVersion": "1.0.0",
  "occurredAt": "2026-07-19T12:00:00Z",
  "correlationId": "30b846cc-d3f5-4aaa-9b99-aaf519dca78e",
  "causationId": "msg-001",
  "tenantId": "enterprise",
  "source": "agent-runtime",
  "traceparent": "00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01",
  "dataClassification": "INTERNAL",
  "payload": {}
}
```

Compulsory fields:

| Campo | Rule |
|---|---|
| `eventId` | Unique UUID used for deduplication. |
| `eventType` | Name without version, equal to domain without subject suffix. |
| `schemaVersion` | Do not use `eventVersion`. |
| `occurredAt` | ISO 8601 UTC. |
| `correlationId` | Functional correlation of the entire execution. |
| `tenantId` | Tenant derived from a trusted identity or context. |
| `source` | Producer service. |
| `dataClassification` | `PUBLIC`, `INTERNAL`, `CONFIDENTIAL` ou `RESTRICTED`. |
| `payload` | Payload tipado pelo AsyncAPI. |

`causationId` and `traceparent` are mandatory where there is a previous cause or distributed context.

## Enums compartilhados

### Risco

`LOW`, `MEDIUM`, `HIGH`, `CRITICAL`.

### State of enforcement

`SUCCESS`, `FAILED`, `BLOCKED`, `PARTIAL`.

### Classification of data

`PUBLIC`, `INTERNAL`, `CONFIDENTIAL`, `RESTRICTED`.

## Catalogue of topics

| Event | Subjects | Produtor principal | Typical consumers |
|---|---|---|---|
| `agent.created` | `agent.created.v1` | Agent Registry | Governance, Audit |
| `agent.updated` | `agent.updated.v1` | Agent Registry | Governance, Audit |
| `agent.published` | `agent.published.v1` | Governance | Registry, Runtime, Audit |
| `agent.retired` | `agent.retired.v1` | Governance | Registry, Runtime, Audit |
| `agent.invoked` | `agent.invoked.v1` | Agent Runtime | Audit, Billing, Evaluation |
| `tool.executed` | `tool.executed.v1` | Agent Runtime | Audit, Billing |
| `model.invoked` | `model.invoked.v1` | Model Gateway | Billing, Observability |
| `knowledge.ingested` | `knowledge.ingested.v1` | Knowledge Service | Audit |
| `embedding.generated` | `embedding.generated.v1` | Knowledge Service | Billing, Audit |
| `document.indexed` | `document.indexed.v1` | Knowledge Service | Audit |
| `memory.updated` | `memory.updated.v1` | Memory Service | Audit |
| `evaluation.started` | `evaluation.started.v1` | Evaluation Service | Audit |
| `evaluation.completed` | `evaluation.completed.v1` | Evaluation Service | Governance, Audit |
| `governance.approved` | `governance.approved.v1` | Governance | Registry, Audit |
| `governance.rejected` | `governance.rejected.v1` | Governance | Registry, Audit |
| `audit.created` | `audit.created.v1` | Audit Service | Observability / Archive |

## Delivery, idempotence and ordering

- Standard semantics is at-least-once.
- Consumers deduct by `eventId`.
- Partition keys:
  - Agent: `tenantId + agentId`;
  - session: `tenantId + sessionId`;
  - documento: `tenantId + knowledgeBaseId + documentId`.
- There is no overall guarantee of topical ordering.
- Critical commands use transactional outbox on the manufacturer.
- Consumers shall continue to offset only after completion of idempotent processing.

## Error and DLQ

- Retry with backoff only for transient failures.
- Invalid events are not repeated indefinitely.
- DLQ by domain with original payload, sanitized error and attempted metadata.
- Reprocessing requires authorisation, audit and preservation of the original `eventId`.

## Security

- Payloads shall not carry complete prompts or personal data when metadata is sufficient.
- Sensitive fields are masked before publication.
- Topical ACLs follow least privilege.
- `CONFIDENTIAL` and `RESTRICTED` events use encryption and retention compatible with the classification.

## Reference retention

| Classe | Initial withholding | The Commission shall adopt implementing acts. |
|---|---:|---|
| Operacional | 90 dias | Diagnosis and limited replay. |
| Billing | 24 meses | Showback and chargeback. |
| Auditoria | 5 anos | Adjust to the applicable regulatory obligation. |
| DLQ | 30 dias | Reprocessamento controlado. |

Timelines are reference and must be approved by Law, Security and LGPD for each organisation.
