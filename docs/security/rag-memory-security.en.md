# Security of RAG and Memory

## Objet

The mandatory controls for ingesting, recovery and knowledge use, as well as the persistance of communication and profile. The source executable of the rules is [`../../policies/rag-memory-security.yaml`](https://github.com/leandrosflora/enterprise-ai-platform-reference-architecture/blob/main/policies/rag-memory-security.yaml).

The standard decision is **deny by default**. The re-established content is always treated as untrustworthy, never as instruction.

## Principles

1. **Autorisation with the dado.** ACL, tenant, classification and finality are distributed from the document to each chunk.
2. **Information does not involve publication.** All documents enter into quarantine and can only be indexed after validation.
3. **Retrieval is not available.** Results not authorised are filtrated without indicating the document exists.
4. **Memorial is not log.** Only necessary ingredients, with finality, will be, trust, TTL and consent when applicable.
5. **Model does not create a true persistent.** Conteining inferred by the model can not turn memory long-term or perfil.
6. **Sensible data do not persist by default.** Classification `RESTRICTED` is blocked; exceptions require specific policy outside the baseline.

## RAG safe pipeline

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

### Printed documents and chunks

| Campo | Finalidade |
|---|---|
| `tenantId` | Putting mix between organisations. |
| `documentId` e `chunkId` | Retainability and syleptic excluding. |
| `classification` | Apply clearance and observation checks. |
| `allowedRoles` / `allowedSubjects` | Enforcement of ACL. |
| `allowedPurposes` | Reuse to be incompatible. |
| `sourceSystem` e `sourceUri` | Provenience. |
| `checksum` | Detect changes after approval. |
| `approvedSource` | Permitir apenas fontes registradas. |
| `retentionPolicy` e `expiresAt` | Expiration, exclusion and reindexation. |
| `securityScanVersion` | Re-return the quarantine decision. |

### Four-obligatory

The document remains `QUARANTINED` when one of these conditions is found:

- not approved source;
- checksum divergente;
- type or size not allowed;
- malware or active payload signature;
- indicator of indirect prompt injection;
- a lack of classification, ACL, finality or retention policy.

The release requires evidence of all checks and generates auditable events. Reindexation must invalidate chunks and previous embeddings.

### Retrieval

The consultation applies the filters before and after the veterinary search:

1. to defraud the tenant, user, passport and clearance of the authenticity;
2. restrict index/aliases by tenant;
3. implementing ACL and classification in the search mechanism;
4. executing post-filter in Knowledge Service;
5. remove non-autonomous results without revealing any content or title to the external caller;
6. re-torning `policyDecisionId`, checksum and proof of auditory origin;
7. to limit the contents recovered as not credible;
8. block instructions found in documents before the prompt assembly.

The model response can only cit pieces that have been used by the same authorisation decision in retrieval.

## Safe memory

### Tipos

| Tipo | Uso | TTL maximum | Consentimento | Fonte permitida |
|---|---|---:|---|---|
| `SESSION` | Context of the current conversation | 24 horas | No, I'm sorry for the specific staff | Model model use, system, iron and infertility |
| `SHORT_TERM` | Continuidade operacional curta | 7 dias | Conforme finalidade | User, system or device checked |
| `LONG_TERM` | re-used in the sessions | 365 dias | Thank you. | User confirmed or checked system |
| `PROFILE` | Explanatory preferences | 365 dias | Thank you. | User confirmed or checked system |

### Duty-free fields for item

- chave e valor minimizados;
- classification;
- finalidade;
- origem;
- trust;
- a property in stock;
- tenant;
- date of creation and expiration;
- version;
- reference to consent when required.

### Protection against memory poisoning

Before writing, Memory Service:

- rejects the commands and instructions dispelled from the files;
- blokes indicators such as “previous instructions”, attempt to reveal prompt or deactivating political systems;
- impedes the persistance of the `MODEL_INFERRED` contents outside `SESSION`;
- require the order of `USER_CONFIRMED` or `SYSTEM_VERIFIED` for `LONG_TERM` and `PROFILE`;
- rejeita `RESTRICTED`;
- only a few hidden gems in the events, never the full value.

Conflicting information must preserve historical version and require reconciliation when confident sources discord.

### Isolamento e descarte

The minimum logic key is:

```text
tenantId + subjectHash + sessionId + memoryType
```

Leiture and excluding use the sujeid of identity. A user does not choose freely another `subjectId`. Consentiment withdrawn block new laws and disseminates or anonimizes according to policy.

## Security observation

Registrar:

- decision of authorisation and blocking grounds;
- status of quarentine;
- documents/chunk IDs;
- checksum and scanner version;
- type of memory, number of itens, TTL and consent provision;
- excluding and reindexation.

Don't register:

- prompt completo;
- integral text of the document;
- full value of memory;
- 'their people are clear;'
- tokens ou segredos.

## Publications gates

| Gate | Evidence |
|---|---|
| Ingestive | Test of quarentene for malware, checksum and prompt injection. |
| Retrieval | ACL test by document/chunk, tenant and clearance. |
| Prompt | Evidence of delimitation and treatment of the context as untrustworthy. |
| Memory | Tests of consent, TTL, origin and poisoning. |
| Privacidade | Excusement for self-interest and retention policy. |
| Auditoria | Events without a sensible payload and with `policyDecisionId`. |

## Demonstrative implementation

The vertical slice implements:

- endpoint of ingesting with checksum, approved source and quarentine;
- - get with tenant, paedia, clearance, finality and post-filter;
- contained as `<untrusted_document>`;
- memory with consent, TTL, origin, confidence and isolation by itself;
- bloke of `RESTRICTED`, `MODEL_INFERRED` persistent and poisoning indicators;
- Automated tests that carry out these checks.

Demo uses memory storage and simulation headers. In production, identity, DLP, antoxirus, policy engine and persistence must be real services.
