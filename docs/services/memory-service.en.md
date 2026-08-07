# Memory Service

## Overview

The Memory Service persists only in a necessary and authorized context; it is not a log of conversation and does not accept that the model transforms inferences into permanent facts.

Compulsory standard: [RAG Security and Memory](../security/rag-memory-security.md).

## responsibilities

- maintain session memory, short-term, long-term and profile;
- applying tenant and isolation by subject;
- validate purpose, consent, origin, trust and classification;
- impor TTL by type;
- detectar memory poisoning;
- changes;
- expiry or withdraw;
- events without sensitive values.

## Types of Memory

| type | Purpose | Maximum TTL | Consentimento |
|---|---|---:|---|
|  `SESSION`  | Context of the current conversation | 24 horas | according to dado |
|  `SHORT_TERM`  | Operational continuity | 7 days | For purpose |
|  `LONG_TERM`  | Reused facts | 365 days | Obligatory |
|  `PROFILE`  | Explicit preferences | 365 days | Obligatory |

## Item Model

```json
{
  "key": "preferred-language",
  "value": "pt-BR",
  "classification": "INTERNAL",
  "source": "USER_CONFIRMED",
  "confidence": 1.0,
  "purpose": "personalize-support",
  "consentReference": "consent-001",
  "expiresAt": "2027-01-01T00:00:00Z"
}
```

The value is encrypted at rest and does not appear in logs or events.

## Writing Policy

The standard decision is to deny. Writing only occurs when:

- the tenant and the subject come from the authenticated identity;
- the purpose is permitted;
- the TTL respects the type;
- the classification may be persisted;
- the origin is compatible with the type;
- there is no poisoning indicator;
- There is consent for `LONG_TERM` and `PROFILE`.

### Origin and trust

| Origem | Section | Curto prazo | Longo prazo / Perfil |
|---|---:|---:|---:|
|  `USER_CONFIRMED`  | Sim | Sim | Sim |
|  `SYSTEM_VERIFIED`  | Sim | Sim | Sim |
|  `TOOL_OUTPUT`  | Sim | According to policy | Not without verification |
|  `MODEL_INFERRED`  | Sim | No | No |

`RESTRICTED` is not persistent by pattern.

## Memory Poisoning Protection

The Office shall reject:

- instructions presented as facts;
- attempts to overwrite system/developer instructions;
- content asking for tool execution;
- data derived exclusively from the model for persistent memory;
- change of preference without confirmation;
- conflict with fact observed without reconciliation.

Indicators generate `policy_denials_total{resource_type="memory"}` and audit event without the rejected value.

## isolation

The logical key is:

```text
tenantId + subjectHash + sessionId + memoryType
```

- `subjectHash` is derived from identity;
- calls do not accept an arbitrary subject in payload;
- Technical workloads use workload identity with minimum scope;
- administrative consultations are separated and audited;
- caches preserve the same isolation key.

## APIs

```http
GET    /v1/sessions/{sessionId}/memory
PATCH  /v1/sessions/{sessionId}/memory
DELETE /v1/sessions/{sessionId}/memory
```

### Escrita

```json
{
  "memoryType": "PROFILE",
  "purpose": "Personalize approved support",
  "ttlSeconds": 3600,
  "consentReference": "consent-001",
  "items": [
    {
      "key": "preferred-language",
      "value": "pt-BR",
      "classification": "INTERNAL",
      "source": "USER_CONFIRMED",
      "confidence": 1.0
    }
  ]
}
```

## Life Cycle

1. validate policy;
2. record the unchanged version;
3. update the active version button;
4. record TTL;
5. emitir `memory.updated` No content;
6. expirar automaticamente;
7. excluir ou anonimizar;
8. emitir `memory.deleted`.

Consent repeal blocks reading and writing before asynchronous exclusion processing.

## Events

- `memory.updated`
- `memory.expired`
- `memory.deleted`
- `memory.consent_revoked`

Allowed fields: session, subject in hash, type, quantity, version, expiration and presence of consent.

## Armazenamento

MongoDB or equivalent bank with:

- resting cryptography;
- TTL index;
- composed of tenant and subject;
- versioning otimista;
- backup compatible with exclusion
- disposal trail.

## Non-functional requirements

| Requirements | Guideline |
|---|---|
| Security | Deny by default and anti-poisoning |
| privacy | Consent, minimisation and disposal |
| isolation | Tenant + subject hash |
| Traceability | Origin, trust, version and purpose |
| availability | Memory degradation when unavailable |
| Consistency | Competition control and reconciliation |
