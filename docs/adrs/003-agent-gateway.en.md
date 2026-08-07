# ADR-003  Agent Gateway as an entry point

**Status:** Aceito

## Contexto

Channels, agents and model providers are evolving at different speeds. Without a common border, authentication, quotas, routing, data protection and telemetry are duplicated.

## Decision

Introduce a **Agent Gateway** between channels/BFFs and runtimes. It does not contain business logic or specific journey prompts.

## Responsabilidades

- authentication, authorisation and tenant resolution;
- rate limit, quotas and budget enforcement;
- routing by agent, version and capacity;
- standardisation of streaming and asynchronous responses;
- correlation, tracing, metrics and audit;
- policies for data entry, classification and masking;
- Circuit breaker and controlled fallback.

## No responsibilities

- the reasoning of the agent;
- direct implementation of domain tools;
- long-term memory storage;
- the definition of business rules.

## Consequences

The gateway becomes a critical component and must be stateless, horizontally scalable, and degrade safely.Control Plane.

## Evidence in the case

In the conversational case, Channel BFF and Conversation Orchestrator materialize part of this boundary.