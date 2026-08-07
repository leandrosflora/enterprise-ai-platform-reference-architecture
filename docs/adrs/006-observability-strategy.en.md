# ADR-006 — OpenTelemetry as observability standard

**Status:** Aceito

## Context

Solutions with generative agents and models require traceability in addition to traditional logs. An execution can cross gateway, runtime, policies, memory, retrieval, models, tools, evaluation and events, with simultaneous impact on quality, safety, cost and latency.

## Decision

Adotar **OpenTelemetry** as a standard of traces, metrics and correlated logs, each invocation must have tip-to-end trace and spans specific for policy decisions, retrieval, memory, model calls, tool calls, evaluation and audit.

Asynchronous events should spread W3C context and maintain `correlationId` e `causationId` if applicable.

## Compulsory requirements

- `agent.id`, `agent.version`, `tenant.id` and risk classification in the execution;
- effective version of model, prompt, policy, tool and knowledge snapshot;
- tokens, cost, latency, retries and fallback;
- authorisation decision without registering secrets or gross payload;
- masking before export;
- metric cardinality control;
- retention and proportional access to the classification of the data;
- correlation with audit and evaluation events.

## Alternatives

| Alternativa | Vantagem | Limitation |
|---|---|---|
| Customized logs per service | Simple local implementation | correlation and inconsistent semantics |
| Single ownership instrumentation | rapid integration with a supplier | lock-in e portabilidade reduzida |
| Only audit events | good business trail | technical diagnosis and insufficient performance |

## Positive consequences

- tip to tip correlation between capacities;
- integration with existing corporate stacks;
- Common basis for SRE, safety, evaluation and FinOps;
- backend exchange without changing the main instrumentation.

## Negative consequences

- increases the volume and cost of telemetry;
- requires attribute governance and cardinality;
- incorrect instrumentation may leak data or generate false confidence;
- sampling needs to preserve critical events.

## Minimum evidence

- reference trace covering a full invocation;
- catalog of spans, attributes and metrics;
- HTTP and asynchronous propagation test;
- redaction test and absence of secrets;
- dashboards, alertas e SLOs associados;
- retention policy, sampling and access.

## Review criteria

To review when the standard fails to meet interoperability, volume or safety requirements, or when instrumentation causes disproportional operational costs to the diagnosis and governance obtained.
