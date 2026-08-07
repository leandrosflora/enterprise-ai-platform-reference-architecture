# Runbook — Troubleshooting of Agent Invitation

## Minimum entry

Collection without exposing sensitive data:

- UTC timetable;
- `correlationId`;
- agent and version;
- tenant;
- classe de workload;
- status HTTP ou `executionStatus`;
- policy ID/version quando houver bloqueio.

## Diagnostic sequence

1. localizar o trace pelo `correlationId`;
2. verifying authentication and authorisation in Gateway;
3. confirmed version `PUBLISHED` no cache do Runtime;
4. review the Policy Decision Point decision;
5. identify first span with error or abnormal latency;
6. verificar backlog e DLQ;
7. confirmar budget e quota;
8. apply or block affected component.

## Fast tree

| Sintoma | Verification | Initial action |
|---|---|---|
|  `401`  | token, issuer, audience e clock skew | Correcting identity |
|  `403`  | escopo, tenant e policy decision | do not release bypass |
|  `404`  | Resource visibility and published version | validate catalogue and tenant |
|  `409`  | uncontrolled or state | See original operation |
|  `422`  | policy violation and missing evidence | correct configuration |
|  `429`  | quota, rate limit ou budget | reduzir consumo ou aprovar novo limite |
|  `BLOCKED`  | policy/guardrail | confirmar bloqueio esperado |
|  `PARTIAL`  | degraded dependence | Inform limitation and call for fallback |
| timeout | span mais lento e deadline | isolate provider/tool and use asynchronous |

## Container

- disabling specific version or tool, not the whole platform;
- forcing fallback only for approved models and regions;
- preservar `deny by default`;
- stop transactional actions if audit is unavailable;
- comunicar impacto, escopo e workaround.

## Encerramento

- causa identificada;
- normalized metrics;
- mensagens na DLQ tratadas;
- smoke test completed;
- evidence attached;
- preventive action registered.
