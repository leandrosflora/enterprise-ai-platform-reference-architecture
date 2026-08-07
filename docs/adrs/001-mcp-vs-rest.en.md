# ADR-001 — MCP for governed tool calling

**Status:** accepted

## Context

Agents need to discover and implement corporate tools with consistent contracts, authorization, versioning and audit. Direct REST integrations remain adequate for domain IPAs, but do not solve themselves discovery of tools, agent-oriented schemes and uniform enforcement during tool calling.

This ADR consolidates the original decision to use MCP with the legislated catalogue and governance strategy of MCP Servers.

## Decision

Usar **MCP** at the boundary between Agent Runtime and governed tools, REST APIs continue to be used as internal and external domain interfaces. MCP does not replace REST; it adds a layer oriented to agent consumption.

The platform must keep a **MCP Registry** for:

- catalog and discovery of servers, tools and schemas;
- ownership, risk classification and version;
- authorisation policies and allowance allowance per agent;
- compatibility between versions of the contract;
- operational status and withdrawal criteria;
- traceability between tool call, identity, politics and registration system.

## Mandatory boundaries

- Agent Runtime does not directly access domain system credentials;
- the MCP Server validates identity of workload, tenant, scopes and purpose;
- commands with side effect require immunopower and audit trail;
- long operations return `operationId` and continue asynchronously;
- schemes and effective versions are recorded in traces and events;
- policy failure results in deny by default;
- MCP Servers do not concentrate business rules that belong to domain services.

## Rationale

- standardized discovery of tools and schemes;
- separation between reasoning of the agent and implementation of the domain;
- central enforcement of identity, scope, journey stage and audit;
- less coupling between agents and corporate services framework;
- governed reuse of tools between agents and domains.

## Alternatives

| alternative | advantage | Limitation |
|---|---|---|
| Direct REST | simple and universal | requires specific adaptation in each agent and dispersed governance |
| Events | Uncoupling and scale | inadequate for all interaction request/response |
| SDK owner | initial productivity | lock-in and fragmented governance |
| Plugin per agent | Local freedom | low re-use and inconsistent audit |

## Consequences

The Tool Service/MCP Server becomes a security frontier and must have SLO, observability, version policy, rollback and onboarding process. The adoption of MCP adds an operational layer, but prevents authorization, audit and contracts from being reimplemented by each agent.

## Minimum evidence

- the MCP contract, which has been executed;
- owner and tool risk classification;
- authorisation matrix;
- tests of disabled arguments, denied access and inequality;
- traces correlating agent, version, tool, policy and result;
- runbook, SLO and withdrawal strategy.

## Review criteria

Review the decision when the protocol no longer meets safety, compatibility, latency or interoperability requirements, or when another open standard offers equivalent governance with lower operational cost.
