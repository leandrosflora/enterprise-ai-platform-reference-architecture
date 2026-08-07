# Knowledge Service

## General view

Knowledge Service ingests, classifies, quarantines, indexes and retrieves corporate knowledge for RAG flows. Security is applied by document and by chunk; the service never relies on retrieved content as instruction.

Mandatory standard: [Security of RAGand Memory](../security/rag-memory-security.md).

## Responsabilidades

- validate type, size, checksum and origin;
- run antivirus and active payload detection;
- detectar indirect prompt injection;
- keep documents in quarantine until approved;
- extract text and metadata;
- the spread of tenant, classification, ACL, purpose and retention to chunks;
- generate embeddings and version the model used;
- index content in aliases/indices isolated by tenant;
- applying authorisation before and after the search;
- return quotations with provenance and policy decision;
- delete, re-index and invalidate old embeddings.

## Injection pipeline

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

| State of origin | Significado |
|---|---|
| `QUEUED` | Request is accepted. |
| `QUARANTINED` | Waiting for approval or blocked by control. |
| `INGESTING` | Extraction and chunking in progress. |
| `INDEXED` | Available for authorised retrieval. |
| `FAILED` | Technical or policy failure not recoverable. |

A `QUARANTINED` or expired document never participates in the search.

## Security of the document

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

All chunks inherit the policy. Reducing the classification or expanding the ACL requires new approval and re-indexation.

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

### Rules

- tenant and subject are derived from identity, not payload;
- ACL is applied to the document and to the chunk;
- the clearance shall be equal to or greater than the classification;
- the purpose of the consultation must be authorised;
- negative results are removed without revealing their existence;
- the quote returns `policyDecisionId`, checksum and origin;
- only authorised chunks may be sent to the model;
- the recovered content is limited and does not change the system/developer instructions.

## APIs

```http
POST /v1/knowledge-bases/{knowledgeBaseId}/documents
POST /v1/knowledge-bases/{knowledgeBaseId}:search
```

## Events Published

- `knowledge.ingested`
- `knowledge.quarantined`
- `document.indexed`
- `document.deleted`
- `embedding.generated`

Events do not contain full text, they must contain IDs, classification, checksum, status and quarantine grounds.

## Exclusion and re-indexation

The deletion removes:

1. documento original;
2. chunks;
3. embeddings;
4. caches;
5. references in derived datasets where applicable.

The index must support removal by `documentId` and `tenantId`

## Dependencies

| Dependence | Uso |
|---|---|
| Object Storage | Originals quarantined and approved |
| Malware/DLP Scanner | Content analysis |
| Policy Decision Point | ACL, purpose and classification |
| OpenSearch | Vector search and hybrid search |
| PostgreSQL | Metadata, origin and retention |
| Foundation Models | Embeddings aprovados |
| Kafka | Auditable events |

## Non-functional requirements

| Requisito | Diretriz |
|---|---|
| Security | Deny by default, ACL by chunk and quarantine-first |
| Privacidade | Minimization, retention and verifiable exclusion |
| Rastreabilidade | Origin, checksum, version and policy decision |
| Qualidade | Assess retrieval separately from generation |
| Resilience | Impotent reprocessing and DLQ |
| Escalabilidade | Asynchronous intake separate from consultation |

## Related Decisions

- [ADR-005  Vector and hybrid search strategy](../adrs/005-vector-search-strategy.md)
- [ADR-007  Hybrid and continuous assessment of AI](../adrs/007-evaluation-strategy.md)
