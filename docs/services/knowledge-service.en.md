# Knowledge Service

## Overview

The Knowledge Service ingests, classifies, put in quarantine, indexes and retrieves corporate knowledge for RAG flows.Security is applied by document and by chunk; the service never trusts the content retrieved as instruction.

Compulsory standard: [RAG Security and Memory](../security/rag-memory-security.md).

## responsibilities

- validate type, size, checksum and origin;
- execute antivirus and detection of active payload;
- detectar indirect prompt injection;
- keep documents in quarantine until approval;
- extract text and metadata;
- spreading tenant, classification, ACL, purpose and retention for chunks;
- generate embeddings and verify the model used;
- index content in aliases/indexes isolated by tenant;
- apply authorisation before and after the search;
- return citations from and policy decision;
- exclude, reindex and invalidate old embeddings.

## Ingestion Pipeline

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

### States

| State | Meaning |
|---|---|
|  `QUEUED`  | Request accepted. |
|  `QUARANTINED`  | Pending approval or blocked by control. |
|  `INGESTING`  | Extraction and ongoing chunking. |
|  `INDEXED`  | Available for authorised retrieval. |
|  `FAILED`  | Technical or political failure cannot be recovered. |

A document `QUARANTINED` never participate in the search.

## Security contract of the document

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

All the chunks inherit the policy. Reducing the classification or expanding ACL requires further approval and re-indexation.

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

### rules

- tenant and subject are derived from identity, not from payload;
- ACL shall be applied to the document and the chunk;
- clearance must be equal to or higher than the classification;
- the purpose of the consultation must be authorised;
- denied results are removed without revealing their existence;
- the quotation returns to the study of the study of the study of the study of the study of the study of the study of the study of the study of the study of the study of the study of the study of the study of the study of the study of the study of the study of the study of the study of the study of the study of the study of the study of the study of the study of the study of the study of the study of the study of the study of the study of the study of the study of the study of the study of the study of the study of the study of the study of the study of the study of the study of the study of the study of the study of the study of the study of the study of the study of the study of the study of the study of the study of the study of the study of the study of the study of the study of the study of the study of the study of the `policyDecisionId`, checksum and origin;
- only authorised chunks may be sent to the model;
- content retrieved is delimited and does not alter system/developer instructions.

## APIs

```http
POST /v1/knowledge-bases/{knowledgeBaseId}/documents
POST /v1/knowledge-bases/{knowledgeBaseId}:search
```

## published events

- `knowledge.ingested`
- `knowledge.quarantined`
- `document.indexed`
- `document.deleted`
- `embedding.generated`

Events do not carry full text, and should contain DIs, classification, checksum, status and quarantine motives.

## Exclusion and Re-indexation

Exclusion removes:

1. document original;
2. chunks;
3. embeddings;
4. caches;
5. references in derived datasets when applicable.

Re-indexation creates a new immutable version and invalidates the previous one. `documentId` and `tenantId`.

## Dependencies

| Dependence | Use |
|---|---|
| Object Storage | Origin in quarantine and approved |
| Malware/DLP Scanner | Content analysis |
| Policy Decision Point | ACL, purpose and classification |
| OpenSearch | Vector and hybrid search |
| PostgreSQL | Half-data, provenance and retention |
| Foundation Models | Embeddings approved |
| Kafka | Auditable events |

## Non-functional requirements

| Requirements | Guideline |
|---|---|
| Security | Deny by default, ACL by chunk and quarantine-first |
| privacy | Minimization, retention and verifiable exclusion |
| Rastreabilidade | Origin, checksum, version and policy decision |
| Quality | Evaluating retrieval separately from generation |
| Resilience | Idequate reprocessing and DLQ |
| scalability | Asynchronous separate consultation intake |

## Related Decisions

- [ADR-005 — Vector and hybrid search strategy](../adrs/005-vector-search-strategy.md)
- [ADR-007 — Hybrid and continuous AI assessment](../adrs/007-evaluation-strategy.md)
