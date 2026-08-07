# ADR-004 — Agent Runtime with stable core and adapters

**Status:** accepted

## Context

The platform needs to execute corporate agents integrating models, memory, RAG, tools, evaluation, policies and observability.The framework ecosystem changes rapidly; coupling corporate contracts with a specific framework increases lock-in and makes it difficult to perform consistent governance.

## Decision

Adotar um **Stable-core corporate agent Runtime and adapters** for frameworks and orchestration providers.

The core shall control:

- identity of the agent and published version;
- loading of immutable configuration;
- application of policies and limits of autonomy;
- implementation of prompts, workflows and tools;
- Integration with Model Gateway, Knowledge Service and Memory Service;
- checkpoint, timeout, retry and cancellation;
- events, audit, evaluation and telemetry.

Adapters may integrate LangGraph, Semantic Kernel, managed services of agents or customized implementations, provided that they preserve the core contracts and controls.

## Limits

- business rules remain in domain services;
- provider credentials remain in Model Gateway;
- approval and catalog remain in Control Plane;
- tools are accessed by governed boundaries, preferably MCP;
- the framework does not define the canonical format of audit, events or policies.

## Alternatives

| alternative | advantage | Limitation |
|---|---|---|
| Single Framework | lower initial effort | lock-in and framework dependent controls |
| Runtime per squad | Local autonomy | Security fragmentation, telemetry and costs |
| Single managed service | simplified operation | portability and extensibility limited |

## Positive consequences

- corporate contracts remain stable during framework exchanges;
- policies, observability and FinOps are uniform;
- technological developments occur by adapters;
- agents can use different patterns without losing governance.

## Negative consequences

- increases the initial complexity of runtime;
- requires conformity testing for adapters;
- exclusive framework resources may need controlled extension;
- the core can become a bottleneck if it accumulates domain responsibilities.

## Minimum evidence

- the contract of invoicing;
- adapter conformity tests;
- traces de model call, retrieval, memory and tool call;
- timeout, cancellation, retry and rollback tests;
- policy decision recorded by execution;
- Documented compatibility between runtime version and adapters.

## Review criteria

To review when an open pattern or managed runtime provide equivalent portability, controls and observability, or when the adaptation layer generates more cost and risk than the lock-in that seeks to avoid.
