# ADR-001 — MCPto tool calling governado

**Status:** Aceito

## Contexto

REST direct integrations remain suitable for APIs domain, but do not alone solve tool discovery, agent-oriented schemes and uniform enforcement during tool calling.

This ADR consolidates the original decision to use MCP with the legacy catalogue and governance strategy of MCP Servers.

## Decision

Use **MCP** at the border between Agent Runtime and controlled tools. APIs REST continue to be used as internal and external domain interfaces. MCP does not replace REST; it adds an agent-oriented layer.

The platform shall maintain a **MCP Registry** for:

- Catalogue and discovery of servers, tools and schemes;
- ownership, risk classification and version;
- authorisation and allowlist policies per agent;
- compatibility between contract versions;
- the operational status and withdrawal criteria;
- traceability between tool call, identity, policy and registration system.

## Mandatory boundaries

- the Agent Runtime does not directly access domain system credentials;
- the MCP Server validates the identity of the workload, tenant, scopes and purpose;
- side-effect commands require idempotence and audit trail;
- long operations return to `operationId` and continue asynchronously;
- actual schemes and versions are recorded in traces and events;
- policy failure results in deny by default;
- MCP Servers do not concentrate business rules that belong to domain services.

## Why ?

- standardised discovery of tools and schemes;
- separation between agent reasoning and domain implementation;
- central enforcement of identity, scope, duration of the journey and audit;
- less coupling between the agent framework and corporate services;
- the regulated reuse of tools between agents and domains.

## Alternativas

| Alternativa | Vantagem | Limitation |
|---|---|---|
| REST direto | Simple and universal | It requires specific adaptation in each agent and scatters governance |
| Events | decoupling and scale | not suitable for all request/response interactions |
| Owner of SDK | produtividade inicial | Lock-in and fragmented governance |
| Plugin by agent | liberdade local | Low reuse and inconsistent audit |

## Consequences

The Tool ServiceMCPServer becomes a security frontier and must possessSLOThe Commission's proposal for a regulation on the implementation of the Community's common agricultural policy (CFSP) and the common agricultural policy (CFSP).MCPadds an operational layer but prevents authorisation, audit and contracts from being reimplemented by each agent.

## Minimum evidence

- the MCP version of the contract;
- owner and risk classification of the tool;
- the authorisation matrix;
- In the case of a Member State, the competent authority shall inform the competent authority of the Member State concerned of the reasons for the failure to comply with this Regulation.
- traces correlating agent, version, tool, policy and outcome;
- the runbook, SLO and withdrawal strategy.

## The Commission shall adopt delegated acts in accordance with Article 21 of this Regulation.

Revising the decision when the protocol no longer meets security, compatibility, latency or interoperability requirements, or when another open standard offers equivalent governance at lower operational cost.
