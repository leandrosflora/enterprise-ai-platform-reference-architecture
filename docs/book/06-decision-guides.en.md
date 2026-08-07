# 7. Decision Guides

## How to use this chapter

The upper lines do not replace DDRs, they help identify the most appropriate initial option and the factors that need to be recorded in the final decision.

## 1. deterministic agent or workflow?

| Use agent when | Use workflow when |
|---|---|
| entry and language are variable | sequence and rules are known |
| selection of tools depends on context | steps need to be reproduzable |
| There is a need for interpretation | erro precisa ser praticamente nulo |
| paths can't be easily outlined | auditory transactions require explicit transactions |
| result may be evaluated by type | result is valid by objective rule |

### Recommendation

Use the lowest autonomy level to solve the problem. An agent can interpret the intention and deleave the execution to a determined workflow.

### Alert Sinais

- agent used only to set up known APIs;
- absence of clear limit of autonomy;
- transatlantic rail without idempotence;
- a critical decision based only on a written text.

## 2. RAG ou fine-tuning?

| Criteria | RAG | Fine-tuning |
|---|---|---|
| Knowledge changes frequently | forte | fraco |
| need for quotations | forte | fraco |
| control by document | forte | hard |
| style or format adjustment | moderado | forte |
| very special and stable knowledge | possible | strong in some cases |
| immediate refund of information | forte | hard |
| preparation cost | ingesting and retrieval | dataset e treinamento |

### Recommendation

Start with RAG for mutable corporative knowledge. Use fine-tuning for behaviour, format, classification or language specialised when there is dataset and profit.

### Combination

A model adjusted may continue using RAG. Fine-tuning does not eliminate the need for authorisation, quotations and knowledge lifecycle.

## 3. Memory or transacional state?

| IA memory | Estado transacional |
|---|---|
| preference, context or summary | Saldo, status, contract, request or official decision |
| may expire or be recalculated | requires consistency and registration system |
| Trust and origin must be registered | integrity rules are compulsory |
| may be probabilistic | must be determined |

### Recommendation

The agent should never use the memory of the agent as a register system.

## 4. MCP ou API tradicional?

| MCP is useful when | API right is better when |
|---|---|
| miltiplos agents find padronizad tools | There is one single stable consumer |
| description and schema must be exposed to runtime | integration may already be consolidated |
| the catalog and authorisation plate | Low latitude and minimum path are priorities |
| tools need to be adapted by policy | -Damic discovery does not bring value |

### Recommendation

Use MCP as a controlled display box for agents, without turning the MCP Server into a new business system. The logic and rules remain in the responsible services.

## 5. Single-agent ou multi-agent?

| Single-agent | Multi-agent |
|---|---|
| menor complexidade | explcital specialisation |
| simple assessment | a very different field and tool |
| menos hops e custo | separation of the necessary context |
| tracing direto | collaboration forged |

### Recommendation

Start with a well defined agent and tools. Insert a few agents only when the decomposition improves quality, security or ownership in a timely manner.

### Multi-agent costs

- more tokens and latence;
- handoff failures;
- difficulty in attribution of responsibility;
- combination assessment;
- excessive context propagation;
- more complex observation.

## 6. Sing or sing?

| Sncron | Assyncron |
|---|---|
| human interaction immediately | long-term or in lot |
| response within the SLO of the channel | varies sensitivity dependents |
| efeito simples e controlado | marrows and retries |
| cancellation connected to the session | independent processing of the connection |

### Recommendation

Use assyncron for ingesting, extended evaluations, lot generation and long-term workflows. Retorne `202 Accepted`, a ID and an endpoint or status event.

## 7. Single model or Model Gateway?

| Direct integration | Model Gateway |
|---|---|
| experimento isolado | miltiples products or torso |
| low risk and short duration | regions, costs and approved models |
| no need for a fallback | common rotation and observation |
| Local simplicity is more important | portability and governance are necessary |

### Recommendation

A corporative plate must be referred to Model Gateway, but it does not need to block short-term prottotypes. The transition must occur before production or use of relevant data.

## 8. Vector database dedicada ou banco existente?

| Currently available with veterinary surgery | Vector database dedicada |
|---|---|
| volume e throughput moderados | sand or specialty sandbags |
| consistency with metads is important | indexed and low-level in large scale |
| the technology is already operating. | advances in resources justify new platform |
| menor complexidade operacional | isolation and independent tuning are necessary |

### Recommendation

It is essential to add a technology only because she's popular.

Consult [ADR-005 — Veterinary and Hybrid procurement strategy](../adrs/005-vector-search-strategy.md).

## 9. Shut up or not?

Cache can reduce cost and longevity, but it needs to include:

- identidade ou grupo autorizado;
- tenant;
- version of the agent;
- version of the sources;
- classification;
- finalidade;
- model and configuration;
- time of validity.

Do not reuse a response between users when authorisation or context may change the result.

## 10. Build ou buy?

| Pergunta | Favorece build | Favorece buy |
|---|---|---|
| - Does it differ from business? | sim | - Not a shit. |
| Are the integration requirements specific? | sim | - Not a shit. |
| Is data control critical? | sim | Depending on the supplier |
| Can I have the time to operate? | sim | - Not a shit. |
| Time-to-market is absolute priority? | - Not a shit. | sim |
| - Is madura on the market? | - Not a shit. | sim |
| Is lock-in acceptable? | - Not a shit. | sim |

### Commonly purchased components

- a general observation;
- model APIs;
- scanners e DLP;
- vector search gerenciada;
- gateways or catalogs, when they look at politics.

### Commonly strategic components

- operating model;
- contratos corporativos;
- policies and risk gates;
- integration with inter-identity and systems;
- datasets and evaluations of the field;
- experience of the developer;
- telemetry and cost allocation.

## 11. Single driver or multi-provider?

Multi-provider must meet a specific requirement:

- disponibilidade;
- data retention;
- specific capacity;
- cost negotiation;
- reduction in concentration;
- Regulatory need.

It does not implement complete portability without consumers. Padronize contracts and telemetry, but accepts differences in capacity between models.

## 12. Guardrail at the prompt or external enforcement?

Prompts are useful to guide behaviour, but they must not be the only barrier for:

- authorisation;
- access to data;
- selection of tools;
- limites financeiros;
- critical actions;
- retention and discharge;
- -Regions and models allowed.

These controls shall be applied by certain components before or after the generation.

## 13. Human in the loop ou human on the loop?

- **Human in the loop:** the implementation is paid and requires approval.
- **Human on the loop:** the execution occurs, but it is monitored and can be interrupted.

Use HITL when the effect is irreversible, regulatory, financial or high impact. Use supervision when the volume impeachs individual approval and exists appropriate limits, detection and rollback.

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

The [model of maturity and roadmap](07-adoption-roadmap.md) organizes these choices in a sequence of sustainable adoption.
