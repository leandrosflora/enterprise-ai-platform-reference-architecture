# Reference architecture - Internal Copilot

## Objective

To provide an internal corporate assistant to support collaborators in search of knowledge, operational guidance and assisted task execution.

## Cases of Use

- Searching for internal policies
- Apoio a atendimento interno
- Consulta a procedimentos
- Response generation with citation of sources
- Assisted call opening

## Componentes Envolvidos

- AI Portal
- Agent Gateway
- Agent Runtime
- Knowledge Service
- Memory Service
- MCP Registry
- Governance Service
- Evaluation Service
- Audit Service

## High Level Flow

1. The user accesses the UA Portal.
2. Agent Gateway authenticates and authorizes the request.
3. Agent Runtime performs the agent.
4. Knowledge Service recupera documentos relevantes.
5. Memory Service recovers allowed context.
6. Agent Runtime calls the foundational model.
7. Evaluation Service assesses the response.
8. Audit Service records the execution.

## Governance Requirements

- Approval of the Agent in the Catalog
- Risk classification
- Authorised knowledge base
- Minimum groundedness assessment
- Complete audit of interactions

## Metrics

- Resolution rate without scheduling
- Groundedness score
- Latency P95
- Cost per interaction
- User satisfaction
