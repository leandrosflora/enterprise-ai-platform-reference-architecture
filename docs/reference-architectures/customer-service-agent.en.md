# This is the total amount of assigned revenue in accordance with Article 21 (3) of the Financial Regulation.

## Objective

Automate and support customer service journeys using agents with RAG, integration into corporate systems and equity governance.

## Cases of use

- Consultation of customer information
- Explanation of products and contracts
- Support for renegotiation
- Selection of requests
- Creation of protocols or calls

## Components involved

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
- Service platform
- Protocol system
- Knowledge base

## High-level flow

1. Customer starts service on the digital channel.
2. Channel Adapter is forwarding the message to Agent Gateway.
3. Agent Runtime recovers context, knowledge and policies.
4. MCP Server consulta sistemas corporativos autorizados.
5. Agent responds or performs a permitted action.
6. Audit Service records conversation, tool calls and decisions.

## Controls

- Scope and channel authorisation
- Masking of sensitive data
- Human-in-the-loopfor critical actions
- Risk autonomy limits
- Registration of consent where applicable

## The following information shall be provided:

- Containment rate
- Average attendance time
- Transfer rate to human
- Rate of error in tool calls
- Cost of care
