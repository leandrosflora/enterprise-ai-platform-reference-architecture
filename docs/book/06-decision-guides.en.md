# 7. Decision Guides

## How to use this chapter

The guides below do not replace ADRs, and they help to identify the most appropriate initial option and the factors that need to be recorded in the final decision.

## 1. Agent or deterministic workflow?

| Use the agent when | Use workflow when |
|---|---|
| entry and language are variables | sequence and rules are known |
| selection of tools depends on context | steps need to be reproducible |
| there is a need for interpretation | erro needs ser praticamente nulo |
| paths cannot be easily listed | audit requires explicit transitions |
| results can be assessed by heading | the result is validated by objective rule. |

### Recommendation

Use the lowest level of autonomy that solves the problem. An agent can interpret the intention and delegate the execution to a deterministic workflow.

### Warning signs

- agent used only to connect known PIAs;
- absence of a clear limit of autonomy;
- transactional tool without inequality;
- critical decision based only on generated text.

## 2. RAG ou fine-tuning?

| Criteria | RAG | Fine-tuning |
|---|---|---|
| knowledge often changes | strong | weak |
| need for citations | forte | weak |
| control by document | forte | difficult |
| style or format adaptation | moderado | forte |
| very specialized and stable knowledge | Possible | in some cases |
| Immediate removal of information | strong | difficult |
| preparation cost | Ingestion and retrieval | dataset and training |

### Recommendation

Start with RAG for changeable corporate knowledge. Use fine-tuning for behavior, format, classification or specialized language when there are dataset and measurable gain.

### Combination

An adjusted model may continue to use RAG. Fine-tuning does not eliminate the need for authorization, citations and lifecycle of knowledge.

## 3. Memory or transactional status?

| Memory of AI | Transaction status |
|---|---|
| preference, context or abstract | balance, status, contract, application or official decision |
| may expire or be recalculated | requires consistency and registration system |
| trust and origin need to be registered | integrity rules are mandatory |
| may be probabilistic | it must be deterministic |

### Recommendation

Never use the agent's memory as a registry system. The agent must consult the authoritative system for transactional events.

## 4. MCP ou API tradicional?

| MCP is useful when | Direct IPA is better when |
|---|---|
| multiple agents discover standardized tools | there is a single stable consumer, which has the right to use the technology of science. |
| description and schema need to be exposed to runtime. | integration has consolidated contract |
| the platform controls catalog and authorization | low latency and minimum path are priorities |
| tools need to be authorized by policy | dynamic discovery does not bring value |

### Recommendation

Use MCP as a layer of exposure governed for agents, without transforming the MCP Server into a new business system. The logic and rules remain in the responsible services.

## 5. Single-agent ou multi-agent?

| Single-agent | Multi-agent |
|---|---|
| less complexity | explicit specialization |
| simpler assessment | very distinct domains and tools |
| less hops and cost | Context separation required |
| tracing direto | collaboration brings proven gain |

### Recommendation

Start with a well-defined agent and tools. Insert multiple agents only when the decomposition improves quality, safety or ownership in a measurable manner.

### Occult multi-agent costs

- more tokens and latency;
- handoff failures;
- difficulty assigning responsibility;
- combinatorial assessment;
- excessive context propagation;
- more complex observability.

## 6. Synchrony or asynchrony?

| Synchronous | Asynchronous |
|---|---|
| immediate human interaction | long or batch tasks |
| Response within the SLO of the channel | dependencies with variable latency |
| simple and controlled effect | multiple steps and retries |
| Cancellation of session | connection independent processing |

### Recommendation

Use asynchronous for ingestion, extensive evaluations, batch generation and long workflows. `202 Accepted`, an identifier and an endpoint or event of status.

## 7. Single model or Model Gateway?

| Direct integration | Model Gateway |
|---|---|
| experimento isolado | multi-products or providers |
| low risk and short duration | region policies, cost and approved models |
| no need for fallback | Common routing and observability |
| local simplicity is the most important | portability and governance are needed |

### Recommendation

A corporate platform should converge to Model Gateway, but it does not need to block short-term prototypes.The transition should occur before the production or use of relevant data.

## 8. Vector database dedicada ou banco existente?

| Existing bank with vector search | Content database vector |
|---|---|
| volume and throughput moderate | scale or search standards |
| consistency with metadata is important to achieve the accuracy of the study. | distributed indexation and large-scale low latency |
| team already operates the technology | advanced resources justify new platform |
| menor complexidade operational | independent isolation and tuning are required |

### Recommendation

Avoid adding a technology only because it is popular.Do benchmark with corpus, filters, update, availability and actual cost.

Consultation [ADR-005 — Vector and hybrid search strategy](../adrs/005-vector-search-strategy.md).

## 9. Cachear or not?

Cache can reduce cost and latency, but it must incorporate:

- identity or authorised group;
- tenant;
- version of the agent;
- version of the sources;
- classification;
- purpose;
- model and configuration;
- expiry date.

Do not reuse a response between users when the authorization or context can alter the result.

## 10. Build ou buy?

| Pergunta | Favorece build | Favorece buy |
|---|---|---|
| capacity differentiates the business? | Yes | no |
| are integration requirements specific? | sim | no |
| is data control critical? | Yes | depends on the supplier |
| has the ability to operate? | sim | no |
| is time-to-market an absolute priority? | no | sim |
| does mature commodity exist in the market? | no | Yes |
| lock-in is acceptable? | no | sim |

### Components commonly purchased

- managed observability;
- model APIs;
- scanners and DLP;
- vector search managed;
- gateways or catalogs, when they meet the policies.

### Frequently strategic components

- operating model;
- corporate contracts;
- policies and risk gates;
- integration with identity and internal systems;
- datasets and domain evaluations;
- developer's experience;
- telemetry and cost assignment.

## 11. Single or multi-provider?

Multi-provider must meet a specific requirement:

- availability;
- residence of data;
- specific capacity;
- cost negotiation;
- concentration reduction;
- regulatory requirement.

Do not implement complete abstract portability without consumers, standardize contracts and telemetry, but accept capacity differences between models.

## 12. Guardrail no prompt ou policy enforcement externo?

Prompts are useful to guide behavior, but they should not be the only barrier to:

- authorization;
- access to data;
- tool selection;
- financial limits;
- Critical actions;
- retention and disposal;
- regions and models allowed.

These controls should be applied by deterministic components before or after generation.

## 13. Human in the loop ou human on the loop?

- **Human in the loop:** the execution pause and requires approval.
- **Human on the loop:** the execution occurs, but is supervised and can be interrupted.

Use HITL when the effect is irreversible, regulated, financial or high-impact; use supervision when the volume prevents individual approval and there are adequate limits, detection and rollback.

## ADR Template

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

O [maturity model and roadmap](07-adoption-roadmap.md) organizes these choices in a sequence of sustainable adoption.
