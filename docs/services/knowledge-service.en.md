# Knowledge Service

## General view

The Knowledge Service ingere, classifies, places in quarentena, index and recuperates corporative knowledge for fluxes RAG. Security is applied by document and by chunk; the service never trusts in the content recovered as instruction.

The following shall be required: (Security of RAG and Memory)(../security/rag-memory-security.md).

## Responsabilidades

- validar tipo, tamanho, checksum e origem;
- execute antivivirus and active payload detection;
- detectar indirect prompt injection;
- keep documents in quarantine until approval;
- extrair texto e metadados;
- to propagate tenant, classification, ACL, finality and retention for chunks;
- generating embeddings and modifying the used model;
- indexing content in indexes/isolated indexes by tenant;
- apply authorisation before and after the search;
- reciting quotes with provenance and policy decision;
- excluir, reindexar e invalidar embeddings antigos.

## Pipeline of Ingest

```text
Source
  ↓
Content type / size validation
  ↓
Malware and active-content scan
  ↓
Checksum and provenance validation
  ↓
Classification, ACL, purpose and retention
  ↓
Indirect prompt injection scan
  ↓
QUARANTINED
  ↓ approval
Extraction
  ↓
Chunking with inherited security metadata
  ↓
Embedding
  ↓
Indexing
```

### Estados

| Estado | Significado |
|---|---|
| `QUEUED` | Appropriation accepted. |
| `QUARANTINED` | Waiting approval or blocked by control. |
| `INGESTING` | Extradition and slacking in the slack. |
| `INDEXED` | Available for authorized retrieval. |
| `FAILED` | No technical or political communication. |

A `QUARANTINED` document or expired never participates in the search.

## Document security

```yaml
documentId: policy-001
classification: INTERNAL
accessPolicy:
  allowedRoles: [employee]
  allowedSubjects: []
  deniedRoles: []
  allowedPurposes: [ASSISTANCE]
provenance:
  sourceSystem: policy-repository
  sourceUri: s3://policies/policy-001.pdf
  checksum: sha256:...
  approvedSource: true
retentionPolicy:
  retentionDays: 365
  deletionMode: DELETE
```

All chunks inherit the policy. The reduction in classification or extension of ACL requires new approval and reindexation.

## Retrieval seguro

```text
Authenticated identity
  ↓ tenant, roles, subject, clearance
Query
  ↓ tenant pre-filter
Vector / hybrid search with ACL
  ↓
Knowledge Service post-filter
  ↓
Prompt-injection sanitization
  ↓
<untrusted_document> context
```

### Regras

- tenant and suit are derived from identity, not from the payload;
- ACL is applied in the document and in the chunk;
- clearance must be equal or greater to classification;
- the finality of the consultation should be authorized;
- a result of the infringement shall be removed without revealing its existence;
- the retracted `policyDecisionId`, checksum and origin;
- only auto-generated chunks may be sent to the model;
- the content recovered is delimited and does not change system/develop instructions.

## APIs

```http
POST /v1/knowledge-bases/{knowledgeBaseId}/documents
POST /v1/knowledge-bases/{knowledgeBaseId}:search
```

## Eventos Publicados

- `knowledge.ingested`
- `knowledge.quarantined`
- `document.indexed`
- `document.deleted`
- `embedding.generated`

Event does not carry full text. It must contain IDs, classification, checksum, status and quarantine motives.

## Exclusive and Reindexation

The excluding removes:

1. documento original;
2. chunks;
3. embeddings;
4. caches;
5. reference in datasets derived when applicable.

Reindexation creates a new mutable and invalid version of the previous. The index needs to support remuneration by `documentId` and `tenantId`.

## Dependencies

| Dependence | Uso |
|---|---|
| Object Storage | Origins in quarentine and approved |
| Malware/DLP Scanner | Context analysis |
| Policy Decision Point | ACL, finality and classification |
| OpenSearch | Veterinary and hybrid bust |
| PostgreSQL | Metadating, origin and retention |
| Foundation Models | Embeddings aprovados |
| Kafka | Audits |

## Non-functioning requirements

| Requisito | Diretriz |
|---|---|
| Security | Deny by default, ACL by chunk and quarantine-first |
| Privacidade | Minimisation, retention and unauthorized access |
| Rastreabilidade | Origin, checksum, version and policy decision |
| Qualidade | Taking separate retrieval from the generation |
| Resilience | Reprocessamento idempotente e DLQ |
| Escalabilidade | Separate consultation ingestive infection |

## Related Decisions

- (ADR-005 — Veterinary and Hybrid procurement strategy)(../adrs/005-vector-search-strategy.md)
- (ADR-007 — Hybrid and IA summary assessment)(../adrs/007-evaluation-strategy.md)
