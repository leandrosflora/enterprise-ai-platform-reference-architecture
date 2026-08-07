# ADR-003 — Agent Gateway como ponto de entrada

**Status:** Aceito

## Context

Channels, agents and model providers evolve at different pace rhythms.Without a common frontier, authentication, quotas, routing, data protection and telemetry are doubled.

## Decision

Introduzir um **Agent Gateway** between channels/BFFs and runtimes, it does not contain business logic or specific prompts of the journey.

## Responsabilidades

- authentication, authorisation and resolution of tenant;
- rate limit, quotas e budget enforcement;
- Routing by agent, version and capacity;
- streaming normalization and asynchronous responses;
- correlation, tracing, metrics and audit;
- entry policies, classification and data masking;
- circuit breaker e fallback controlado.

## Non-responsibilities

- reasoning of the agent;
- direct implementation of domain tools;
- long-term memory storage;
- definition of business rules.

## Consequences

The gateway becomes a critical component and should be stateless, horizontally scalable and safely degraded.Agent configurations should be versed in Control Plane.

## Case evidence

In the conversational case, Channel BFF and Conversation Orchestrator materialize part of this frontier, and the recommended evolution is to consolidate common policies without focusing on the logic of the journey.