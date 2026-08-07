# 7. Decision Guides

## How to Use This Chapter

The guides below do not replace ADRs. They help identify the most appropriate initial option and the factors that need to be recorded in the final decision.

## 1. Deterministic agent or workflow?

| Use agent when | Use workflow when |
|---|---|
| input and language are variables | sequence and rules are known |
| tool selection depends on context | steps need to be reproducible |
| There is a need for interpretation | erro precisa ser praticamente nulo |
| roads cannot be easily enumerated | Auditing requires explicit transitions |
| The result can be evaluated by heading | The result is validated by objective rule |

### Recommendation

Use the lowest level of autonomy that solves the problem. An agent can interpret the intent and delegate execution to a deterministic workflow.

### Warning signs

- agent used only to chain known APIs;
- the absence of a clear autonomy limit;
- a transactional tool without idempotence;
- critical decision based only on generated text.

## 2. RAG ou fine-tuning?

| Criterion of use | RAG | Fine-tuning |
|---|---|---|
| Knowledge changes frequently | forte | fraco |
| need for citations | forte | fraco |
| control by document | forte | difficult |
| adaptation of style or format | moderado | forte |
| very specialized and stable knowledge | possible | strong in some cases |
| immediate removal of information | forte | difficult |
| cost of preparation | ingestion and recovery | Data set and training |

### Recommendation

Start with RAG for changing corporate knowledge. Use fine-tuning for behavior, format, classification, or specialized language when there is a measurable dataset and earnings.

### Combination

An adjusted model can continue to use RAG. Fine-tuning does not eliminate the need for authorization, citation and lifecycle of knowledge.

## 3. Memory or transactional status?

| AI memory | The amount to be reported shall be reported in the following table: |
|---|---|
| preference, context or summary | Balance, status, contract, application or official decision |
| may expire or be recalculated | It requires consistency and a record system |
| Trust and origin must be recorded | Integrity rules are mandatory |
| It can be probabilistic. | must be deterministic |

### Recommendation

The agent should consult the authoritative system for transactional facts.

## 4. MCP ou API tradicional?

| MCP is useful when | API direct is better when |
|---|---|
| Multiple agents discover standardized tools | there is only one stable consumer |
| Description and schema need to be exposed to runtime | integration has a consolidated contract |
| the platform controls catalogue and authorisation | Low latency and minimum path are priorities |
| tools need to be enabled by policy | Dynamic discovery does not bring value |

### Recommendation

Use MCP as a controlled exposure layer for agents, without turning the MCP Server into a new business system.

## 5. Single-agent ou multi-agent?

| Single-agent | Multi-agent |
|---|---|
| menor complexidade | explicit specialization |
| simpler evaluation | Very different domains and tools |
| less hops and cost | necessary separation of context |
| tracing direto | Collaboration brings proven gains |

### Recommendation

Start with a well-defined agent and tools. Introduce multiple agents only when decomposition improves quality, safety, or ownership in a measurable way.

### Hidden costs of multi-agent

- more tokens and latency;
- handoff failure;
- difficulty in assigning responsibility;
- a combined assessment;
- excessive dissemination of context;
- more complex observability.

## 6. Synchronous or asynchronous?

| Synchronous | Asynchronous |
|---|---|
| immediate human interaction | Long-term or batch tasks |
| the response within the SLO channel | dependencies with variable latency |
| Simple and controlled effect | Multiple stages and retries |
| cancellation of the session | Processing independent of the connection |

### Recommendation

Use asynchronous for intake, extensive evaluations, batch generation and long workflows. Return `202 Accepted`, an identifier and an endpoint or status event.

## 7. Single model or Model Gateway?

| Direct integration | Model Gateway |
|---|---|
| experimento isolado | Multiple products or suppliers |
| low risk and short duration | Regional policies, cost and models approved |
| No need for fallback | Common routing and observability |
| Local simplicity is more important | portability and governance are necessary |

### Recommendation

A corporate platform should converge to Model Gateway but need not block short-lived prototypes.

## 8. Vector database dedicada ou banco existente?

| Existing bank with vector search | Vector database dedicada |
|---|---|
| Moderate volume and throughput | Specialized scale or search patterns |
| Consistency with metadata is important | Distributed indexation and low latency on a large scale |
| The team already operates the technology. | Advanced resources justify a new platform |
| menor complexidade operacional | Independent insulation and tuning are required |

### Recommendation

Avoid adding a technology just because it's popular, benchmark it with corpus, filters, update, availability, and real cost.

Consulte [ADR-005  Vector and hybrid search strategy](../adrs/005-vector-search-strategy.md).

## 9. To hide or not to hide?

Cache can reduce cost and latency, but it needs to incorporate:

- identidade ou grupo autorizado;
- tenant;
- the agent's version;
- version of the sources;
- the classification;
- finalidade;
- model and configuration;
- the period of validity.

Do not reuse a user response when authorisation or context may change the result.

## 10. Build ou buy?

| Pergunta | Favorece build | Favorece buy |
|---|---|---|
| capacity differentiates the business? | sim | No |
| are integration requirements specific? | sim | No |
| is data control critical? | sim | depends on the supplier |
| Do you have the ability to operate? | sim | No |
| Time-to-market is a top priority? | No | sim |
| Is there a mature commodity on the market? | No | sim |
| Lock-in is acceptable? | No | sim |

### Frequently purchased components

- managed observability;
- model APIs;
- scanners and DLP;
- vector search gerenciada;
- gateways or catalogs, when they meet policies.

### Often strategic components

- operating model;
- corporate contracts;
- policies and risk gates;
- integration with identity and internal systems;
- domain datasets and assessments;
- the experience of the developer;
- the use of telemetry and cost allocation.

## 11. Single provider or multi-provider?

The multi-provider shall fulfil a specific requirement:

- disponibilidade;
- the data residence;
- specific capacity;
- cost negotiation;
- concentration reduction;
- the need for regulation.

It doesn't implement complete abstract portability without consumers, it standardizes contracts and telemetry, but it accepts differences in capacity between models.

## 12. Guardrail on prompt or external policy enforcement?

Prompts are useful for guiding behavior, but they should not be the only barrier to:

- authorisation;
- access to data;
- selection of tools;
- limites financeiros;
- critical actions;
- retention and disposal;
- regions and permitted models.

These controls shall be applied by deterministic components before or after generation.

## 13. Human in the loop ou human on the loop?

- **Human in the loop:** the implementation pauses and requires approval.
- **Human on the loop:** execution occurs, but is monitored and may be interrupted.

Use HITL when the effect is irreversible, regulated, financial or high impact; use supervision when the volume prevents individual approval and there are appropriate limits, detection and rollback.

## The ADR template

For each relevant decision, register:

```text
Title
Status
Context
Decision drivers
Options considered
Decision
Consequences
Security and privacy impact
Operational impact
Cost impact
Validation plan
Revisit triggers
```

## Next chapter

The [maturity model and roadmap](07-adoption-roadmap.md) organizes these choices into a sustainable adoption sequence.
