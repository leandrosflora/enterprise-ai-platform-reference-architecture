# Cases applied

The cases applied demonstrate how the logical capacities of Enterprise AI Platform can be materialized in domains, journeys and concrete topology.

They do not define a single implementation. Each case explains:

- the business problem;
- where the AI participates in the journey;
- which capacities of the platform are used;
- which controls remain deterministic;
- what is implemented, demonstrated or only planned;
- the gaps for integration and production.

## Available cases

<div class="grid cards" markdown>

-   :material-message-processing-outline: **Multi-skill banking conversational platform**

    ---

    Bank journals via WhatsApp, multiple skills, Agent Runtimes, MCP tools, RAG, memory, eventing, audit and evaluation.

        [Opening the conversational case](conversational-ai.md)

-   : clipboard-flow-outline material: **Intelligent Backoffice — bank contest**

    ---

    Persistent workflow, document processing, assisted investigation, recommendation, human approval, policy enforcement, inadequate execution and reconciliation.

        [Opening the case of backoffice](intelligent-backoffice.md)

-   : source-branch: **Agentic SDLC governed**

    ---

    Specialized agents of the requirement for production feedback, durable workflow, Model Gateway, MCP, OPA, evidence, digest approval, observed release and rollback.

        [Opening the case of Agentic SDLC](agentic-sdlc.md)

</div>

## Fast comparison

| Case | Main interaction unit | Intelligent autonomy | Real governed effect |
|---|---|---|---|
| Conversational platform | Conversation and client's journey | select skill, answer and use tools | banking operations mediated by domain services |
| Intelligent Backoffice | case, document and evidence | studies | Human approval and execution service |
| Agentic SDLC | software change and evidence bundle | refine, design, implement and review | MCP tools, digest approval, release and rollback |

## How to interpret states

| State | Meaning |
|---|---|
|  `CONTRACT_DEFINED`  | Architecture, contract, policy or liability, without proven integration |
|  `IMPLEMENTATION_STARTED`  | Product code initiated, but without sufficient evidence of end-to-end integration |
|  `DEMONSTRATED_LOCAL`  | Capacity executed locally or in IC with data and synthetic integrations |
|  `VALIDATED_INTEGRATION`  | Validated integration against real services in a controlled environment |
|  `PASSED_PRODUCTION`  | Approved capacity for evidenced production, operation, safety and ownership |

!!! warning "Case applied does not mean production"
    Diagrams, code and local tests demonstrate decisions and mechanisms.Production requires real integration, authorised data, corporate security, operation, SLOs, support, risk and formal approval.
