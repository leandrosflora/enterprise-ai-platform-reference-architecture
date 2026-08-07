# Runbook — Troubleshooting of Agent Invitation

## Minimum entry

Collection without exposing sensitive data:

- UTC timetable;
- `correlationId`;
- agent and version;
- tenant;
- workload class;
- status HTTP ou `executionStatus`;
- policy ID/version when there is blockade.

## Diagnostic sequence

1. locating the trace by `correlationId`;
2. verifying authentication and authorisation in Gateway;
3. confirmed version `PUBLISHED` in the Runtime cache;
4. review the Policy Decision Point decision;
5. identify first span with error or abnormal latency;
6. check backlog and DLQ;
7. confirm budget and quota;
8. apply or block affected component.

## Fast tree

| Symptoms | Verification | Initial action |
|---|---|---|
|  `401`  | token, issuer, audience and clock skew | Correcting identity |
|  `403`  | scope, tenant and policy decision | do not release bypass |
|  `404`  | Resource visibility and published version | validate catalogue and tenant |
|  `409`  | uncontrolled or state | See original operation |
|  `422`  | policy violation and missing evidence | correct configuration |
|  `429`  | quota, rate limit or budget | reduce consumption or approve novo limit |
|  `BLOCKED`  | policy/guardrail | confirmar bloqueio esperado |
|  `PARTIAL`  | degraded dependence | Inform limitation and call for fallback |
| timeout | span slower and deadline | isolate provider/tool and use asynchronous |

## Container

- disabling specific version or tool, not the whole platform;
- forcing fallback only for approved models and regions;
- preservar `deny by default`;
- stop transactional actions if audit is unavailable;
- communicate impact, scope and workaround.

## Encerramento

- causa identificada;
- normalized metrics;
- DLQ messages treated;
- smoke test completed;
- evidence attached;
- preventive action registered.
