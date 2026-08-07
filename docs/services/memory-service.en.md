# Memory Service

## General view

The Memory Service persists only in necessary and authorized context. It is not a conversation log and does not accept the model to turn inferences into permanent facts.

Mandatory standard: [Security of RAGand Memory](../security/rag-memory-security.md).

## Responsabilidades

- maintain session memory, short-term, long-term and profile;
- apply tenant and insulation per subject;
- validate purpose, consent, origin, trust and classification;
- imposing TTL by type;
- detectar memory poisoning;
- to make changes;
- delete or anonymise after expiry or revocation;
- broadcast events without sensitive values.

## Types of memory

| Tipo | Finalidade | Maximum TTL | Consentimento |
|---|---|---:|---|
| `SESSION` | Context of the current conversation | 24 horas | Conforme dado |
| `SHORT_TERM` | Continuidade operacional | 7 dias | Conforme finalidade |
| `LONG_TERM` | Fatos reutilizados | 365 dias | Compulsory |
| `PROFILE` | Explained preferences | 365 dias | Compulsory |

## Model of Item

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

## Writing policy

The default decision is to deny.

- the tenant and subject come from the authenticated identity;
- the purpose is permitted;
- the TTL respects the type;
- the classification may be continued;
- the origin is compatible with the type;
- there is no indicator of poisoning;
- there is consent for `LONG_TERM` and `PROFILE`.

### Origin and Confidence

| Origem | Meeting | Curto prazo | Longo prazo / Perfil |
|---|---:|---:|---:|
| `USER_CONFIRMED` | Sim | Sim | Sim |
| `SYSTEM_VERIFIED` | Sim | Sim | Sim |
| `TOOL_OUTPUT` | Sim | Political | Not without verification |
| `MODEL_INFERRED` | Sim | No , it 's not . | No , it 's not . |

`RESTRICTED` is not persistent by default.

## Protection against memory poisoning

The service rejects:

- instructions presented as facts;
- attempts to overwrite system/developer instructions;
- Content requesting the execution of the tool;
- data derived exclusively from the model for persistent memory;
- change of preference without confirmation;
- conflict with verified fact without reconciliation.

Indicators generate `policy_denials_total{resource_type="memory"}` and an audit event without the rejected value.

## Isolamento

The logical key is:

```text
tenantId + subjectHash + sessionId + memoryType
```

- `subjectHash` is derived from the identity;
- calls do not accept an arbitrary subject on the payload;
- technical workloads use workload identity with minimal scope;
- administrative consultations are separate and audited;
- caches retain the same lock.

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

## Life cycle

1. validate policy;
2. recording an unchanged version;
3. update the active version pointer;
4. registrar TTL;
5. to issue `memory.updated` without content;
6. expirar automaticamente;
7. excluir ou anonimizar;
8. emitir `memory.deleted`.

Withdrawal of consent blocks reading and writing before the asynchronous processing of exclusion.

## Events

- `memory.updated`
- `memory.expired`
- `memory.deleted`
- `memory.consent_revoked`

Allowed fields: session, hash subject, type, quantity, version, expiration and presence of consent.

## Armazenamento

MongoDB or equivalent bank with:

- encryption at rest;
- TTL index;
- a key composed of tenant and subject;
- versionamento otimista;
- a back-up compatible with exclusion;
- the landfill track.

## Non-functional requirements

| Requisito | Diretriz |
|---|---|
| Security | Deny by default and anti-poisoning |
| Privacidade | Consent, minimization and discard |
| Isolamento | Tenant + subject hash |
| Rastreabilidade | Origin, confidence, version and purpose |
| Disponibilidade | Degradation without memory when unavailable |
| Consistency | Competition control and reconciliation |
