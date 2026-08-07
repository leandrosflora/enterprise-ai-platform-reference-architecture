# Runbook  Troubleshooting of Agent Invocation

## Minimum entry

Collect without exposing sensitive data:

- UTC time;
- `correlationId`;
- agent and version;
- tenant;
- the workload class;
- status HTTP ou `executionStatus`;
- policy ID/version when there is a block.

## Diagnostic sequence

1. locate the trace by `correlationId`;
2. verify authentication and authorisation on the Gateway;
3. confirm the `PUBLISHED` version in the Runtime cache;
4. review a decision of the Policy Decision Point;
5. identify first span with error or abnormal latency;
6. verify backlog and DLQ;
7. confirm the budget and quota;
8. apply fallback or block the affected component.

## Fast tree

| Sintoma | Verification | Initial action |
|---|---|---|
| `401` | token, issuer, audience and clock skew | corrigir identidade |
| `403` | scope, tenant and policy decision | review authorisation, not release bypass |
| `404` | visibility of the resource and published version | validate catalogue and tenant |
| `409` | Impotence or state | to consult original operation |
| `422` | policy violation and lack of evidence | correct the configuration |
| `429` | quota, rate limit ou budget | reduzir consumo ou aprovar novo limite |
| `BLOCKED` | policy/guardrail | confirmar bloqueio esperado |
| `PARTIAL` | degraded dependence | report limitation and trigger fallback |
| timeout | slower span and deadline | isolate provider/tool and use asynchronous |

## Containment

- disable a specific version or tool, not the entire platform;
- Forcing fallback only for approved models and regions;
- preservar `deny by default`;
- to pause transactional actions if the audit is unavailable;
- communicate impact, scope and workaround.

## Encerramento

- causa identificada;
- standardised metrics;
- messages in the treated DLQ;
- smoke test completed;
- timeline and attached evidence;
- registered preventive action.
