# ADR-004  Agent Runtime with stable core and adapters

**Status:** Aceito

## Contexto

The platform needs to execute corporate agents by integrating models, memory, RAG, tools, evaluation, policies, and observability. The framework ecosystem changes rapidly; linking corporate contracts to a specific framework increases lock-in and makes consistent governance difficult.

## Decision

Adopting a **Agent Runtimea stable core and adapters** for frameworks and orchestration providers.

The core shall control:

- the identity of the agent and the published version;
- the unchanging configuration load;
- the implementation of policies and limits of autonomy;
- execution of prompts, workflows and tools;
- integration with Model Gateway, Knowledge Serviceand Memory Service;
- the checkpoint, timeout, retry and cancellation;
- The Commission shall adopt delegated acts in accordance with Article 21 of Regulation (EU) No 182/2011 and in accordance with Article 21 thereof.

Adapters can integrate LangGraph, Semantic Kernel, agent-managed services or custom implementations, provided they preserve the core contracts and controls.

## Limites

- business rules remain in the domain services;
- supplier credentials remain in the Model Gateway;
- approval and catalogue remain in the Control Plane;
- tools are accessed by governed borders, preferably MCP;
- the framework does not define the canonical format of audits, events or policies.

## Alternativas

| Alternativa | Vantagem | Limitation |
|---|---|---|
| Single framework | lower initial effort | Lock-in and framework-dependent controls |
| Runtime by squad | autonomia local | The Commission shall adopt delegated acts in accordance with the opinion of the Standing Committee on Planning and Budgetary Control. |
| Single managed service | Simplified operation | Limited portability and extensibility |

## Positive consequences

- corporate contracts remain stable during framework exchanges;
- the policies, observability and FinOps are uniform;
- technological development is carried out by adaptors;
- agents can use distinct standards without losing governance.

## Negative consequences

- increases the initial complexity of the runtime;
- require conformity tests for adapters;
- the unique features of frameworks may require controlled extension;
- The core can become a bottleneck if it accumulates domain responsibilities.

## Minimum evidence

- the versioned invocation contract;
- conformity tests of the adapter;
- the model call, retrieval, memory and tool call traces;
- timeout, cancellation, retry and rollback testing;
- policy decision recorded by execution;
- documented compatibility between runtime version and adapters.

## The Commission shall adopt delegated acts in accordance with Article 21 of this Regulation.

Review when an open or managed runtime standard provides equivalent portability, controls and observability, or when the adaptation layer generates more cost and risk than the lock-in it seeks to avoid.
