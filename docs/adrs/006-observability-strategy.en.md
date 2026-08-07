# ADR-006 — OpenTelemetry as a warning pad

**Status:** Aceito

## Contexto

Solutions with generic agents and models require rastreability beyond traditional logs. An implementation can reach gateway, runtime, policies, memory, retrieval, models, tools, evaluation and events, with a simulating impact on quality, safety, cost and reliability.

## Decision

Adopt **OpenTelemetry** as trace pattern, methods and correlated logs. Each invoke must have trace point and specific lengths for policy, retrieval, memory, model calls, tool calls, evaluation and audit.

Assembly events shall propagate W3C context and maintain `correlationId` and `causationId` when applicable.

## Obligatory requirements

- `agent.id`, `agent.version`, `tenant.id` and risk classification in execution;
- model, prompt, policy, tool and knowledge snapshot;
- tokens, cost, latence, retries and fallback;
- decision to authorise without registering secrets or a brute-readable payload;
- mowing before export;
- a control of the cardinality of the methods;
- retention and appropriate access to the classification of the child;
- correction with auditory and evaluation events.

## Alternativas

| Alternativa | Vantagem | Limitation |
|---|---|---|
| Service logs | simple local implementation | inconsistent correlation and symbiosis |
| Single property instrument | rapid integration with a supplier | lock-in e portabilidade reduzida |
| Only auditory events | Good business trip | technical diagnostic and inadequate performance |

## Positive consequences

- a cross-section of the cross between capacities;
- integration with existing corporative stacks;
- common basis for SRE, security, assessment and FinOps;
- a backend without changing the main instrumentation.

## Negative consequences

- increase volume and cost of telemetry;
- requires a government of attributes and cardinality;
- a faulty instrumentation may be able to collect data or generate false confidence;
- sampling needs to preserve critical events.

## Minimum evidence

- a trace of reference bringing a complete voice;
- catalogue of spans, attributes and methods;
- HTTP propagation test and a synchrome test;
- test of redaction and absence of secrets;
- dashboards, alertas e SLOs associados;
- retention, sampling and access policy.

## Review criteria

Review when the framework does not allow interoperability, volume or security requirements, or when the instrument causes unfavourable operational costs to diagnostics and the government obtained.
