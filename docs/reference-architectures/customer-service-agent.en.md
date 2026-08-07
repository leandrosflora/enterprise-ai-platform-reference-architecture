# Reference architecture - Client Care Agent

## Objective

Automate and support client care journeys using AGR agents, integration to corporate systems and action governance.

## Casos de Uso

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
- Plataforma de atendimento
- Protocol system
- Knowledge base

## High Level Flow

1. Cliente inicia atendimento em canal digital.
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
- Taxa de erro em tool calls
- Cost of care
