# Event Contratos

## Canomycin

The file (`async-api.yaml`)(async-api.yaml) is the executable source of the events. This document defines the normative conventions. Examples and implementations cannot create envelopes or any alternative.

## Transporte e versionamento

- Reference transport: Kafka.
- Reference serialisation: JSON UTF-8.
- The graphs use the `<evento>.v<major>` format, for example `agent.invoked.v1`.
- `schemaVersion` usa SemVer.
- Incompatible changes require new major and new theory.
- Producers don't remove fields during a major life.
- Consumidores ignoram campos desconhecidos.

## Obligatory envelope

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

compulsory fields:

| Campo | Regra |
|---|---|
| `eventId` | Only used for decoding. |
| `eventType` | Nom without verse, same as the subject without the syringe of the tyre. |
| `schemaVersion` | - No use of `eventVersion`. |
| `occurredAt` | ISO 8601 UTC. |
| `correlationId` | Functional correction of all execution. |
| `tenantId` | Having derived from identity or confidential context. |
| `source` | Producer service. |
| `dataClassification` | `PUBLIC`, `INTERNAL`, `CONFIDENTIAL` ou `RESTRICTED`. |
| `payload` | Payload tipado pelo AsyncAPI. |

`causationId` and `traceparent` are binding when there is a cause or context distributed earlier.

## Enums compartilhados

### Risco

`LOW`, `MEDIUM`, `HIGH`, `CRITICAL`.

### Implementation state

`SUCCESS`, `FAILED`, `BLOCKED`, `PARTIAL`.

### Data classification

`PUBLIC`, `INTERNAL`, `CONFIDENTIAL`, `RESTRICTED`.

## Graphics catalog

| Evento | Symbol | Produtor principal | Typical consumers |
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

## Entregation, idempotence and order

- - 'Secretary: **at-east-one**.
- Consumptors deduct by `eventId`.
- Partition key:
  - agent: `tenantId + agentId`;
  - session: `tenantId + sessionId`;
  - documento: `tenantId + knowledgeBaseId + documentId`.
- There is no global guarantee of order between the two.
- Critical commands use transient outbox in the producer.
- Consumers remain offset only after the idempotent procedure is completed.

## Erros e DLQ

- Retry with backoff only for transit failures.
- Invariable events are not repeated indefinitely.
- DLQ for a subject with original payload, sanitized error and tentative metades.
- Reprocessing requires authorisation, audit and preservation of the original `eventId`.

## Security

- Payloads must not carry full or personal data when metadata are low.
- Sensible fields are slacked before publication.
- - The typics are the least privilege.
- Events `CONFIDENTIAL` and `RESTRICTED` use criptography and retensiveness with classification.

## Reference retention

| Classe | Initial retention | Observation |
|---|---:|---|
| Operacional | 90 dias | Diagnotic and limited replay. |
| Billing | 24 meses | Showback e chargeback. |
| Auditoria | 5 anos | Adjust the applicable regulatory obligation. |
| DLQ | 30 dias | Reprocessamento controlado. |

Time is reference and must be approved by the Court, Security and LGPD for each organisation.
