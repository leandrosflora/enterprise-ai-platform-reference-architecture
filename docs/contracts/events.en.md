# Event contracts

## Canon source

The archive [`async-api.yaml`](async-api.yaml) is the feasible source of events. This document defines the normative conventions. Examples and implementations cannot create alternative envelopes or enums.

## Transport and versioning

- Reference transport: Kafka.
- Reference serialization: JSON UTF-8.
- Topics use the format `<evento>.v<major>`, by example `agent.invoked.v1`.
- `schemaVersion` usa SemVer.
- Incompatible changes require new major and new topic.
- Producers do not remove fields during the lifetime of a major.
- Consumidores ignoram campos desconhecidos.

## Compulsory avelope

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

| Campo | rule |
|---|---|
|  `eventId`  | Single UID used for deduplication. |
|  `eventType`  | Name without version, equal to domain without suffix of topic. |
|  `schemaVersion`  | Do not use `eventVersion`. |
|  `occurredAt`  | ISO 8601 UTC. |
|  `correlationId`  | Functional correlation of the entire implementation. |
|  `tenantId`  | Tenant is derived from identity or reliable context. |
|  `source`  | Producer service. |
|  `dataClassification`  |  `PUBLIC`, `INTERNAL`, `CONFIDENTIAL` or `RESTRICTED`. |
|  `payload`  | Payload typed by AsyncAPI. |

`causationId` and `traceparent` they are mandatory when there is a previously distributed cause or context.

## Enums compartilhados

### Risk

`LOW`, `MEDIUM`, `HIGH`, `CRITICAL`.

### State of execution

`SUCCESS`, `FAILED`, `BLOCKED`, `PARTIAL`.

### Data classification

`PUBLIC`, `INTERNAL`, `CONFIDENTIAL`, `RESTRICTED`.

## Topic catalog

| event | Topic | Produtor principal | Typical consumers |
|---|---|---|---|
|  `agent.created`  |  `agent.created.v1`  | Agent Registry | Governance, Audit |
|  `agent.updated`  |  `agent.updated.v1`  | Agent Registry | Governance, Audit |
|  `agent.published`  |  `agent.published.v1`  | Governance | Registry, Runtime, Audit |
|  `agent.retired`  |  `agent.retired.v1`  | Governance | Registry, Runtime, Audit |
|  `agent.invoked`  |  `agent.invoked.v1`  | Agent Runtime | Audit, Billing, Evaluation |
|  `tool.executed`  |  `tool.executed.v1`  | Agent Runtime | Audit, Billing |
|  `model.invoked`  |  `model.invoked.v1`  | Model Gateway | Billing, Observability |
|  `knowledge.ingested`  |  `knowledge.ingested.v1`  | Knowledge Service | Audit |
|  `embedding.generated`  |  `embedding.generated.v1`  | Knowledge Service | Billing, Audit |
|  `document.indexed`  |  `document.indexed.v1`  | Knowledge Service | Audit |
|  `memory.updated`  |  `memory.updated.v1`  | Memory Service | Audit |
|  `evaluation.started`  |  `evaluation.started.v1`  | Evaluation Service | Audit |
|  `evaluation.completed`  |  `evaluation.completed.v1`  | Evaluation Service | Governance, Audit |
|  `governance.approved`  |  `governance.approved.v1`  | Governance | Registry, Audit |
|  `governance.rejected`  |  `governance.rejected.v1`  | Governance | Registry, Audit |
|  `audit.created`  |  `audit.created.v1`  | Audit Service | Observability / Archive |

## Delivery, immobility and ordering

- Standard semantic: **at-least-once**.
- Consumidores deduplicam por `eventId`.
- Partition keys:
  - Agent: `tenantId + agentId`;
  - session: `tenantId + sessionId`;
  - document: `tenantId + knowledgeBaseId + documentId`.
- There is no overall assurance of ordering between topics.
- Critical commands use transactional outbox in the producer.
- Consumers persist offset only after completing the inadequate processing.

## Mistakes and DLQ

- Retry with backoff only for transient failures.
- Disabled events are not repeated indefinitely.
- DLQ per domain with original payload, sanitized error and metadata of attempt.
- Reprocessing requires authorization, audit and preservation of the `eventId` original.

## Security

- Payloads must not carry complete prompts or personal data when metadata is sufficient.
- Sensitive fields are masked before publication.
- Topic ACLs follow least privilege.
- Events `CONFIDENTIAL` and `RESTRICTED` they use cryptography and retention compatible with the classification.

## Reference retention

| Class | Initial retention | Remark |
|---|---:|---|
| Operational | 90 days | Diagnosis and limited replay. |
| Billing | 24 months | Showback and chargeback. |
| Audit | 5 years | Adjust to the applicable regulatory obligation. |
| DLQ | 30 days | Controlled reprocessing. |

Time limits are references and should be approved by Legal, Security and LGPD for each organization.
