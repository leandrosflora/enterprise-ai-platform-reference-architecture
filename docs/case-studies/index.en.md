# Applied cases

The cases used demonstrate how the logical capabilities of Enterprise AI Platform can be materialized in specific domains, journeys and topologies.

They don't define a single implementation.

- the business problem;
- where the AI participates in the journey;
- which platform capabilities are used;
- which controls remain deterministic;
- what is being implemented, demonstrated or just planned;
- the gaps for integration and production.

## Available cases

<div class="grid cards" markdown>

-   This is the first of a series of reports on the implementation of the European Union's Strategy for Sustainable Development.

    ---

    Banking days via WhatsApp, multiple skills, Agent Runtimes, tools MCP, RAG, memory, eventing, audit and evals.

    [Open the conversation case](conversational-ai.md)

-   :material-clipboard-flow-outline: **Intelligent Backoffice  banking dispute**

    ---

    This appropriation is intended to cover expenditure relating to the implementation of the common agricultural policy and the management of the common agricultural policy.

    [Opening the backoffice case](intelligent-backoffice.md)

-   :material-source-branch: **Agentic SDLC governado**

    ---

    Specialized agents of the production feedback requirement, durable workflow, Model Gateway, MCP, OPA, evidence, digest approval, observed release and rollback.

    [Opening the Agentic SDLC case](agentic-sdlc.md)

</div>

## Rapid comparison

| Case in point | Main unit of interaction | Autonomia inteligente | Efeito real governado |
|---|---|---|---|
| A conversation platform | Customer conversation and journey | Select skill, respond and use tools | Banking operations mediated by domain services |
| Intelligent Backoffice | case, document and evidence | classify, investigate and recommend | Human approval and execution service |
| Agentic SDLC | Software change and evidence bundle | refining, designing, implementing and revising | tools via MCP, approval by digest, release and rollback |

## How to Interpret States

| State of origin | Significado |
|---|---|
| `CONTRACT_DEFINED` | Architecture, contract, policy or versioned liability, yet without proven integration |
| `IMPLEMENTATION_STARTED` | Product code initiated but without sufficient evidence of end-to-end integration |
| `DEMONSTRATED_LOCAL` | Capacity executed locally or in CI with synthetic data and integrations |
| `VALIDATED_INTEGRATION` | Valid integration against real services in controlled environment |
| `PASSED_PRODUCTION` | Approved production capacity with evidence, operation, safety and ownership |

!!! warning "If applied does not mean production"
    Local diagrams, code and testing demonstrate decisions and mechanisms.Production requires real integration, authorized data, corporate security, operation, SLOs, support, risk and formal approval.
