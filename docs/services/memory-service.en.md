# Memory Service

## General view

Memory Service is only a necessary and authorized context, and it is not a conversation log and does not accept that the model transforms inferience into permanent fats.

The following shall be required: (Security of RAG and Memory)(../security/rag-memory-security.md).

## Responsabilidades

- keep a memory of sitting, short term, long term and profile;
- apply tenant and isolation by sujee;
- validating finality, consent, origin, confidence and classification;
- impose TTL by type;
- detectar memory poisoning;
- to amend amendments;
- to exclude or anonimise after expiry or repeal;
- emit events without sensibel values.

## Memory Tipos

| Tipo | Finalidade | TTL maximum | Consentimento |
|---|---|---:|---|
| `SESSION` | Context of the current conversation | 24 horas | Conforme dado |
| `SHORT_TERM` | Continuidade operacional | 7 dias | Conforme finalidade |
| `LONG_TERM` | Fatos reutilizados | 365 dias | Thank you. |
| `PROFILE` | Explanatory preferences | 365 dias | Thank you. |

## Model of item

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

The value is criptografted in reverse and does not appear in logs or events.

## Writing Policy

The standard decision is to be negated, the writing only occurs when:

- the tenant and the suspect see the authentic identity;
- the finality is allowed;
- the TTL respects the guy;
- the classification may be persisted;
- the origin is compatible with the type;
- there is no poisoning indicator;
- There is consent for `LONG_TERM` and `PROFILE`.

### Origin and confidence

| Origem | Session | Curto prazo | Longo prazo / Perfil |
|---|---:|---:|---:|
| `USER_CONFIRMED` | Sim | Sim | Sim |
| `SYSTEM_VERIFIED` | Sim | Sim | Sim |
| `TOOL_OUTPUT` | Sim | Politically | Not without verification |
| `MODEL_INFERRED` | Sim | No | No |

`RESTRICTED` is not persistent by default.

## Protection against Memory Poisoning

The service rejects:

- instructions presented as fats;
- attempts to create system/develop instructions;
- containing the application for the application of the iron;
- data derived exclusively from the model for persistent memory;
- amendment of preference without confirmation;
- Conflict with a vehement vehement reconciliation.

Indicators were `policy_denials_total{resource_type="memory"}` and auditory event without the value rejected.

## Isolamento

The logic key is:

```text
tenantId + subjectHash + sessionId + memoryType
```

- `subjectHash` is derived from identity;
- calls do not accept an arbitrarily sworn in on the payload;
- technical workloads use minimum workload identity;
- administrative consultations are separated and audited;
- caches preserve the same key of isolation.

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

## Vida Ciclo

1. validating policy;
2. a mutable version of the file;
3. update the active version;
4. registrar TTL;
5. emit `memory.updated` without a count;
6. expirar automaticamente;
7. excluir ou anonimizar;
8. emitir `memory.deleted`.

Revocation of bloke consent and written before the unauthorized processing.

## Eventos

- `memory.updated`
- `memory.expired`
- `memory.deleted`
- `memory.consent_revoked`

Camps permitted: sitting, sitting in the air, type, quantity, version, expiration and consenting presence.

## Armazenamento

MongoDB or equivalent bank with:

- criptography in reverse;
- TTL index;
- a key composed of tenant and supprop;
- versionamento otimista;
- compatible backup with excluding;
- - The fucking shit.

## Non-functioning requirements

| Requisito | Diretriz |
|---|---|
| Security | Deny by default e anti-poisoning |
| Privacidade | Consentiment, minimisation and discharge |
| Isolamento | Tenant + subject hash |
| Rastreabilidade | Origin, confidence, version and finish |
| Disponibilidade | Degradation without memory when indispotable |
| Consistency | Competition control and reconciliation |
