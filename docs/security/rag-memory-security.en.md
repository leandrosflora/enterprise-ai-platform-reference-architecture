# RAG Security and Memory

## Objective

Defining mandatory controls for intake, recovery and use of knowledge, in addition to persistence of conversational memory and profile is the main source of rules. [`../../policies/rag-memory-security.yaml`](https://github.com/leandrosflora/enterprise-ai-platform-reference-architecture/blob/main/policies/rag-memory-security.yaml).

Standard decision is **deny by default**. Retrieved content is always treated as unreliable data, never as instruction.

## Principles

1. **Authorisation accompanies the data.** ACL, tenant, classification and purpose are disseminated from the document to each chunk.
2. **Administration does not imply publication.** Each document enters quarantine and can only be indexed after validation.
3. **Retrieval does not leak out.** Unauthorised results are filtered without informing the call for the document.
4. **Memory is not log.** Only necessary facts, purpose, origin, trust, TTL and consent when applicable.
5. **A model does not create persistent truth.** Content inferred by the model cannot become long-term memory or profile.
6. **Sensitive data do not persist by pattern.** Classification `RESTRICTED` it is blocked; exceptions require specific policy outside the baseline.

## Safe Pipeline for RAG

```text
Fonte
  ↓
Validação de tipo e tamanho
  ↓
Antivírus / detecção de payload
  ↓
Checksum e proveniência
  ↓
Classificação e ACL
  ↓
Detecção de indirect prompt injection
  ↓
Quarentena
  ↓ aprovação
Extração e chunking com ACL herdada
  ↓
Embedding e indexação
  ↓
Retrieval com tenant + ACL + clearance + finalidade
  ↓
Post-filter e sanitização
  ↓
Contexto delimitado como <untrusted_document>
```

### Compulsory half-data per document and chunk

| Campo | Purpose |
|---|---|
|  `tenantId`  | To prevent mixing between organizations. |
|  `documentId` and `chunkId`  | Traceability and selective exclusion. |
|  `classification`  | Applying clearance and observability controls. |
|  `allowedRoles` / `allowedSubjects`  | ACL effort. |
|  `allowedPurposes`  | Avoid re-use for incompatible use. |
|  `sourceSystem` and `sourceUri`  | Origin. |
|  `checksum`  | Detect alteration after approval. |
|  `approvedSource`  | Allow only registered sources. |
|  `retentionPolicy` and `expiresAt`  | Expiration, exclusion and re-indexation. |
|  `securityScanVersion`  | Reproduce the quarantine decision. |

### Compulsory quarantine

the document permanece `QUARANTINED` Where any of these conditions occur:

- source not approved;
- checksum divergente;
- type or size not allowed;
- signature of malware or active payload;
- indirect prompt injection indicator;
- No classification, ACL, purpose or retention policy.

Release requires evidence from all controls and generates auditable events.Re-indexation should invalidate previous chunks and embeddings.

### Retrieval

The query applies the filters before and after the vector search:

1. derive tenant, user, roles and clearance of authenticated identity;
2. restrict tenant indexes/aliasis;
3. apply ACL and classification in the search mechanism;
4. perform post-filter in the Knowledge Service;
5. removing unauthorised results without revealing counting or title to the external call forward;
6. return `policyDecisionId`, checksum and audit provenance;
7. delimiting the content recovered as non-reliable;
8. blocking instructions found in documents before assembling the prompt.

The model's response can only mention chunks that have undergone the same authorization decision used in the retrieval.

## Secure memory

### types

| type | Uso | Maximum TTL | Consentimento | Permitted source |
|---|---|---:|---|---|
|  `SESSION`  | Context of the current conversation | 24 hour | No, except for specific personal data | User, system, tool and model inference |
|  `SHORT_TERM`  | Short operational continuity | 7 days | For purpose | User, system or tool checked |
|  `LONG_TERM`  | Reused work between sessions | 365 days | Obligatory | Confirmed user or verified system |
|  `PROFILE`  | Explicit preferences | 365 days | Obligatory | Confirmed user or verified system |

### Compulsory fields per item

- key and minimized value;
- classification;
- purpose;
- origem;
- trust;
- subject owner in hash;
- tenant;
- date of breeding and expiry;
- version;
- if required.

### Memory poisoning protection

Before writing, the Memory Service:

- rejects commands and instructions disguised of facts;
- blocks indicators such as “ignore previous instructions”, an attempt to reveal system prompt or deactivate policy;
- prevents content persistence `MODEL_INFERRED` or `SESSION`;
- requires origin `USER_CONFIRMED` or `SYSTEM_VERIFIED` for `LONG_TERM` and `PROFILE`;
- rejeita `RESTRICTED`;
- registers only safe metadata in events, never the full value.

Conflicting updates should preserve the version history and require reconciliation when reliable sources disagree.

### Isolation and disposal

The minimum logical key is:

```text
tenantId + subjectHash + sessionId + memoryType
```

Reading and exclusion use the subject derived from identity. One user does not freely choose another `subjectId`. Repealed consent blocks new readings and triggers exclusion or anonymisation according to policy.

## Secure observability

record:

- authorisation decision and reason for blocking;
- Quarantine status;
- Document/chunk IDs;
- checksum and version of the scanner;
- type of memory, number of items, TTL and presence of consent;
- exclusion and re-indexation.

Do not register:

- prompt complete;
- full text of the document;
- integral value of memory;
- dado pessoal em claro;
- tokens ou segredos.

## Publication banks

| Gate | Evidence |
|---|---|
| Ingestion | Quarantine test for malware, checksum and prompt injection. |
| Retrieval | ACL test by document/chunk, tenant and clearance. |
| Prompt | Evidence of delimiting and treating the context as non-reliable. |
| Memory | Consent tests, TTL, origin and poisoning. |
| privacy | Subject exclusion and retention policy. |
| Audit | Events without sensitive payload and without `policyDecisionId`. |

## Demonstrative implementation

A vertical slice implementa:

- endpoint of ingestion with checksum, approved source and quarantine;
- search with tenant, roles, clearance, purpose and post-filter;
- content defined as `<untrusted_document>`;
- consent memory, TTL, origin, trust and isolation by subject;
- blockade of `RESTRICTED`, `MODEL_INFERRED` persistent and poisoning indicators;
- automated tests that exercise these controls.

The demo uses memory storage and simulated headers.In production, identity, DLP, antivirus, policy engine and persistence, they should be real services.
