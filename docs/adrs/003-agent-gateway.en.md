# ADR-003 — Agent Gateway as entry point

**Status:** Aceito

## Contexto

Canais, agents and models models evolve in different ways, without a common border, authenticity, quotas, roteament, data protection and telemetry are duplicated.

## Decision

Introduce **Agent Gateway** between channels and runs. It does not contain business logic or specific prompts of the newspaper.

## Responsabilidades

- authenticity, authorisation and tenant resolution;
- rate limit, quotas e budget enforcement;
- roteament by agent, version and capacity;
- normalisation of streaming and asynchronous responses;
- correction, trace, methods and auditory;
- entry, classification and re-filling policies;
- circuit breaker e fallback controlado.

## No responsibility

- the raciocinus of the agent;
- direct implementation of field machinery;
- long-term memory storage;
- definition of business rules.

## Consequences

The gateway becomes critical and must be stateless, horizontally stable and degrade with security. Agent configurations must be compiled in Control Plane.

## Evidence in the case

In the conversacional case, Channel BFF and the Conversation Orchestrator materialise part of that border. The recommended evolution is to consolidate common policies without focusing on the literature of the newspaper.