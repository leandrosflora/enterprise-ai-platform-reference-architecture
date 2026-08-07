# Reference architecture - Client Care Agent

## Objective

Automate and support client care journeys using RAG agents, integration to corporate systems and action governance.

## Cases of Use

- Consultation of customer information
- Explanation of products and contracts
- Support for renegotiation
- Screening of requests
- Creation of protocols or calls

## Componentes Envolvidos

- Channel Adapter
- Agent Gateway
- Agent Runtime
- Knowledge Service
- Memory Service
- MCP Registry
- Corporate Systems
- Governance Service
- Audit Service

## Integrations

- CRM
- Core Banking
- Care platform
- Protocol system
- Knowledge base

## High Level Flow

1. The patient starts receiving care in a digital channel.
2. Channel Adapter encaminha a mensagem ao Agent Gateway.
3. Agent Runtime recovers context, knowledge and policies.
4. MCP Server consultates authorised corporate systems.
5. The agent responds or performs a permitted action.
6. Audit Service records conversation, tool calls and decisions.

## Controls

- Authorisation by scope and channel
- Sensitive data masking
- Human-in-the-loop for critical actions
- Limits of autonomy for risk
- Registry of consent where applicable

## Metrics

- Containment rate
- Mean time of care
- Transfer to human
- Tool call error rate
- Cost of care
