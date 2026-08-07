# RAG security and memory

## Objective

Define the mandatory controls for ingestion, retrieval and use of knowledge, as well as the persistence of conversational and profile memory.[`../../policies/rag-memory-security.yaml`](https://github.com/leandrosflora/enterprise-ai-platform-reference-architecture/blob/main/policies/rag-memory-security.yaml).

The default decision is **deny by default**. Recovered content is always treated as unreliable data, never as instruction.

## Principles

1. **Authorisation accompanies the data.** ACL, tenant, classification and purpose are propagated from the document for each chunk.
2. **Ingestion does not imply publication.** All documents are quarantined and can only be indexed after validation.
3. **Retrieval does not exist.** Unauthorized results are filtered without informing the caller that the document exists.
4. **Memory is not log.** Only necessary facts, with purpose, origin, trust, TTL and consent where applicable.
5. **Model does not create persistent truth.** Content inferred by the model cannot turn into long-term memory or profile.
6. **Sensitive data do not persist by default.** `RESTRICTED` classification is blocked; exceptions require specific policy outside the baseline.

## Safe pipeline of RAG

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

### Mandatory metadata per document and chunk

| Campo | Finalidade |
|---|---|
| `tenantId` | Preventing mixing between organisations. |
| `documentId`and `chunkId` | Traceability and selective exclusion. |
| `classification` | Apply clearance and observability controls. |
| `allowedRoles` / `allowedSubjects` | ACL enforcement. |
| `allowedPurposes` | Avoid re-use for incompatible purposes. |
| `sourceSystem`and `sourceUri` | It's the origin. |
| `checksum` | Detect change after approval. |
| `approvedSource` | Allow only registered sources. |
| `retentionPolicy`and `expiresAt` | Expiration, deletion and re-indexation. |
| `securityScanVersion` | Repeat the quarantine decision. |

### Compulsory quarantine

The document shall remain `QUARANTINED` when any of the following conditions occur:

- unapproved source;
- checksum divergente;
- type or size not permitted;
- malware subscription or active payload;
- the indirect indicator prompt injection;
- absence of classification, ACL, purpose or retention policy.

Release requires proof of all controls and generates an auditable event.

### Retrieval

The query applies the filters before and after the vector search:

1. derive the tenant, user, documents and clearance of the authenticated identity;
2. restrict indices/aliases per tenant;
3. apply ACL and search engine ranking;
4. perform post-filtering on the Knowledge Service;
5. removing unauthorised results without revealing a count or title to the external caller;
6. return `policyDecisionId`, checksum and provenance to the audit;
7. identify recovered content as unreliable;
8. block instructions found in documents before installing the prompt.

The model response can only cite chunks that have passed the same authorisation decision used in retrieval.

## Secure memory

### Tipos

| Tipo | Uso | Maximum TTL | Consentimento | Permitted source |
|---|---|---:|---|---|
| `SESSION` | Context of the current conversation | 24 horas | No, except for specific personal data | User, system, tool and model inference |
| `SHORT_TERM` | Continuidade operacional curta | 7 dias | Conforme finalidade | Verified user, system or tool |
| `LONG_TERM` | Fact reused between sessions | 365 dias | Compulsory | Confirmed user or verified system |
| `PROFILE` | Explained preferences | 365 dias | Compulsory | Confirmed user or verified system |

### Mandatory fields by item

- key and value minimized;
- the classification;
- finalidade;
- origem;
- confidence;
- the hash owner;
- tenant;
- date of creation and expiry;
- the version;
- reference to consent where required.

### Protection against memory poisoning

Before writing, the Memory Service:

- Reject commands and instructions disguised as facts;
- blocks indicators such as ignore previous instructions, attempt to reveal system prompt or disable policy;
- prevent the persistence of content `MODEL_INFERRED` outside `SESSION`;
- requires the origin of `USER_CONFIRMED` or `SYSTEM_VERIFIED` for `LONG_TERM` and `PROFILE`;
- rejeita `RESTRICTED`;
- It only records secure metadata on events, never the full value.

Conflicting updates should preserve version history and require reconciliation when reliable sources disagree.

### Insulation and disposal

The minimum logical key is:

```text
tenantId + subjectHash + sessionId + memoryType
```

Read and delete use the identity-derived subject. One user does not freely choose another `subjectId`. Revocated consent blocks new readings and triggers exclusion or anonymisation according to the policy.

## Safe and reliable observation

Registrar:

- the authorisation decision and the reason for the block;
- the quarantine status;
- the document/chunk IDs;
- the checksum and version of the scanner;
- the type of memory, number of items, TTL and presence of consent;
- exclusion and re-indexation.

Not to be recorded:

- prompt completo;
- the full text of the document;
- the total value of the memory;
- personal data in clear;
- tokens ou segredos.

## Publication gates

| Gate | Evidence |
|---|---|
| Injection | Quarantine test for malware, checksum and prompt injection. |
| Retrieval | ACL test by document/chunk, tenant and clearance. |
| Prompt | Evidence of delimitation and treatment of context as unreliable. |
| The memory | Consent tests, TTL, origin and poisoning. |
| Privacidade | Exclusion by subject and retention policy. |
| Auditoria | Events without sensitive payload and with `policyDecisionId`. |

## Demonstrated implementation

The vertical slice implements:

- an intake endpoint with checksum, approved source and quarantine;
- search with tenant, papers, clearance, purpose and post-filter;
- Content marked as `<untrusted_document>`;
- the consent memory, TTL, origin, trust and isolation per subject;
- the presence of `RESTRICTED`, persistent `MODEL_INFERRED` blocking and poisoning indicators;
- automated tests that carry out these controls.

The demo uses memory storage and simulated headers. In production, identity, DLP, antivirus, policy engine and persistence must be real services.
