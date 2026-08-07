# Casos aplicados

The cases applied demonstrate how the logical capacities of Enterprise AI Platform can be materialized in domains, journeys and concrete topology.

They do not define a single implementation. Each case explains:

- the business problem;
- onde a IA participa da jornada;
- which capacities of the platform are used;
- which controls remain deterministic;
- what is implemented, demonstrated or only planned;
- the gaps for integration and production.

## Available cases

<div class="grid cards" markdown>

-   :material-message-processing-outline: **Multi-skill banking conversational platform**

    ---

    Bank journals via WhatsApp, multiple skills, Agent Runtimes, MCP tools, RAG, memory, eventing, audit and evaluation.

        [Abrir o caso conversacional](conversational-ai.md)

-   :material-clipboard-flow-outline: **Intelligent Backoffice — bank contest**

    ---

    Persistent workflow, document processing, assisted investigation, recommendation, human approval, policy enforcement, inadequate execution and reconciliation.

        [Abrir o caso de backoffice](intelligent-backoffice.md)

-   :material-source-branch: **Agentic SDLC governado**

    ---

    Specialized agents of the requirement for production feedback, durable workflow, Model Gateway, MCP, OPA, evidence, digest approval, observed release and rollback.

        [Abrir o caso de Agentic SDLC](agentic-sdlc.md)

</div>

## Fast comparison

| Caso | Main interaction unit | Autonomia inteligente | Efeito real governado |
|---|---|---|---|
| Plataforma conversacional | conversa e jornada do cliente | selecionar skill, responder e usar tools | banking operations mediated by domain services |
| Intelligent Backoffice | case, document and evidence | classificar, investigar e recomendar | Human approval and execution service |
| Agentic SDLC | software change and evidence bundle | refinar, desenhar, implementar e revisar | MCP tools, digest approval, release and rollback |

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
