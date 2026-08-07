# This is the total amount of the project.

## Objective

Provide an internal corporate assistant to support employees in the pursuit of knowledge, operational guidance and assisted execution of tasks.

## Cases of use

- Search for internal policies
- Support for in-house care
- Consultation of the procedures
- Generating responses with citation of sources
- Assisted opening of calls

## Components involved

- AI Portal
- Agent Gateway
- Agent Runtime
- Knowledge Service
- Memory Service
- MCP Registry
- Governance Service
- Evaluation Service
- Audit Service

## High-level flow

1. The user accesses the AI Portal.
2. Agent Gateway authenticates and authorises the request.
3. Agent Runtime executes the agent.
4. Knowledge Service recupera documentos relevantes.
5. Memory Service recupera contexto permitido.
6. Agent Runtime calls it the foundation model.
7. Evaluation Service shall assess the response.
8. Audit Service shall record the execution.

## Governance requirements

- Approval of the agent in the AI Catalog
- Classification of risk
- Authorised knowledge base
- Minimum groundedness assessment
- Full audit of interactions

## The following information shall be provided:

- Resolution rate without staggering
- Groundedness score
- P95 latency
- Cost per interaction
- User satisfaction
