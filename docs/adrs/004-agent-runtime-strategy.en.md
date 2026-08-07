# ADR-004 — Agent Runtime with stable and adaptable content

**Status:** Aceito

## Contexto

The platform needs to execute corporative agents integrating models, memory, RAG, tools, evaluation, policies and observability. The framework ecosystem changes rapidly; bringing corporative contracts to a specific framework increases lock-in and complicates consistent governance.

## Decision

Adopt a **Agent Runtime corporative with stable and adaptable content** for frameworks and speakers of origin.

The code must control:

- the identity of the agent and published version;
- a switchable configuration load;
- application of policies and limits of autonomy;
- implementation of prompts, workflows and tools;
- integration with Model Gateway, Knowledge Service and Memory Service;
- checkpoint, timeout, retry e cancelamento;
- events, auditory, evaluation and telemetry.

Adapters may integrate LangGraph, Semantic Kernel, managed services of agents or custom-built implementations, provided they preserve the contracts and controls of the nitrate.

## Limites

- business rules remain in the field services;
- proving credentials remain in Model Gateway;
- approval and catalog remain in Control Plane;
- tools are available by government borders, preferably MCP;
- the framework does not define the canometric format of auditory, events or policies.

## Alternativas

| Alternativa | Vantagem | Limitation |
|---|---|---|
| Single Framework |                                                                                                                                                                                                 | lock-in and control dependent on the framework |
| Runtime by squad | autonomia local | security fragmentation, telemetry and costs |
| Single-generation service | simplified operation | portabilidade e extensibilidade limitadas |

## Positive consequences

- corporative contracts remain stable during framework exchanges;
- policies, observability and FinOps are uniform;
- technological developments occur by adapters;
- Agents can use different rules without losing power.

## Negative consequences

- increases the initial complexity of runtime;
- requires compliance tests for adapters;
- exclusive resources of frameworks may require control-controlled extension;
- the crystal may become a slut if it has accumulated domain responsibility.

## Minimum evidence

- a version-based voice contract;
- calibration tests of the adapter;
- traces of model call, retrieval, memory and tool call;
- timeout test, cancellation, retry and rollback;
- policy decision registered for implementation;
- compatibility documented between runtime and adapters.

## Review criteria

Reconsider when an open or runtime pattern provides portability, control and equivalent observability, or when the adapting chamber generates more cost and risk than the lock-in that attempts to avoid.
