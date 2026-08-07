# Runbook — Troubleshooting of Agent Invocation

## Minimum entry

- No sensitive data:

- a UTC office;
- `correlationId`;
- agent and version;
- tenant;
- workload class;
- status HTTP ou `executionStatus`;
- policy ID/version when there is blockage.

## Diagnostic sequence

1. locate trace by `correlationId`;
2. verify authentication and authorization at the Gateway;
3. confirm `PUBLISHED` version in Runtime cache;
4. re-examine the Decision Point Policy;
5. identify first time with an abnormal error or atypical lativity;
6. verificar backlog e DLQ;
7. confirmar budget e quota;
8. aplicar fallback ou bloquear componente afetado.

## Quick tree

| Sintoma | Check | Initial action |
|---|---|---|
| `401` | token, issuer, audience e clock skew | corrigir identidade |
| `403` | escopo, tenant e policy decision | reauthorisation, not release bypass |
| `404` | visibility of the resource and published version | validating catalog and tenant |
| `409` | idempotence or state | consult original operation |
| `422` | infringement of policy and failure to prove | adjusting configuration |
| `429` | quota, rate limit ou budget | reduzir consumo ou aprovar novo limite |
| `BLOCKED` | policy/guardrail | confirmar bloqueio esperado |
| `PARTIAL` | Degraded dependency | inform limitation and follow fallback |
| timeout | span mais lento e deadline | isolator/tool and use assyncron |

## Contenuation

- deactivate the version or specific tool, not the entire platform;
- forcing fallback only for approved models and regions;
- preservar `deny by default`;
- imposing transnational actions if it is indisputable;
- comunicar impacto, escopo e workaround.

## Encerramento

- causa identificada;
- normalised methods;
- messages in the DLQ handled;
- a completed smoke test;
- timeline and evidence annexed;
- a preventive action registered.
