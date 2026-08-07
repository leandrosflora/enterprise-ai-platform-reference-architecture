# ADR-006  OpenTelemetry as an observability standard

**Status:** Aceito

## Contexto

Solutions with generative agents and models require traceability beyond traditional logs. An execution can go through gateway, runtime, policies, memory, retrieval, models, tools, evaluation and events, with simultaneous impact on quality, security, cost and latency.

## Decision

Adopt **OpenTelemetry** as a pattern of related traces, metrics and logs. Each invocation must have end-to-end traces and specific spans for policy decisions, retrieval, memory, model calls, tool calls, evaluation and audit.

Asynchronous events shall propagate the W3C context and maintain `correlationId` and `causationId` where applicable.

## Mandatory requirements

- the risk classification in the execution of `agent.id`, `agent.version`, `tenant.id`;
- the actual model version, prompt, policy, tool and knowledge snapshot;
- The amount of the exposure value of the underlying exposure shall be calculated as follows:
- an authorisation decision without recording secrets or gross sensitive payload;
- masking before export;
- the cardinality control of metrics;
- retention and access proportional to the classification of the data;
- correlation with audit and evaluation events.

## Alternativas

| Alternativa | Vantagem | Limitation |
|---|---|---|
| Customized logs by service | Simple local implementation | inconsistent correlation and semantics |
| Unique proprietary instrumentation | Rapid integration with a supplier | Lock-in and reduced portability |
| Audit events only | Good business trail | Technical diagnosis and insufficient performance |

## Positive consequences

- end-to-end correlation between capacities;
- integration with existing corporate stacks;
- the common basis for SRE, security, evaluation and FinOps;
- backend exchange without altering the main instrumentation.

## Negative consequences

- increase the volume and cost of telemetry;
- requires governance of attributes and cardinality;
- incorrect instrumentation may leak data or generate false confidence;
- sampling needs to preserve critical events.

## Minimum evidence

- a reference line covering a full invocation;
- the catalogue of spans, attributes and metrics;
- the HTTP and asynchronous spread test;
- proof-of-concept and absence of secrets;
- dashboards, alerts and SLOs associados;
- the retention, sampling and access policy.

## The Commission shall adopt delegated acts in accordance with Article 21 of this Regulation.

Review when the standard fails to meet interoperability, volume or safety requirements, or when the instrumentation causes an operational cost disproportionate to the diagnosis and governance achieved.
