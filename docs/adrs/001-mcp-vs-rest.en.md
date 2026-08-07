# ADR-001 — MCP for tool calling

**Status:** Aceito

## Contexto

Agents need to find and execute corporative tools with contracts, authorisation, versioning and consistent audit. Direct REST integrations remain appropriate for APIs in the field, but do not resolve only through tools, schemas geared to agents and enforcement uniform during tool calling.

This ADR consolidates the original decision to use MCP with the logical strategy and governance of MCP Servers.

## Decision

Use **MCP** on the border between Agent Runtime and managed tools. APIs REST continues to be used as internal and external domain interfaces. MCP does not replace REST; it adds a trawl to the consumption by agents.

The plate must hold a **MCP Registry** for:

- catalogue and discovery of service providers, tools and schemas;
- ownership, risk classification and version;
- authorisation policies and authorisation policies by agent;
- compatibility between contract versions;
- operational state and withdrawal criteria;
- rastreability between tool call, identity, policy and registration system.

## Obligatory borders

- Agent Runtime does not directly access the domain systems;
- the MCP Server valids the identity of workload, tenant, scopes and finality;
- comands with the same effect require idempotence and auditory trility;
- long-running operations retracted `operationId` and remain assyncrone;
- schemas and efetish versions are recorded in trace and event;
- a lack of policy results in default;
- MCP Servers do not concentrate business rules that belong to the domain services.

## 'Cause it's because

- a detailed description of the methods and schemas;
- separation between the agent's race and the implementation of the field;
- central enforcement of identity, escopo, status of the newspaper and auditory;
- less arrangement between the framework of agents and corporate services;
- re-use of tools between agents and fields.

## Alternativas

| Alternativa | Vantagem | Limitation |
|---|---|---|
| REST direto | simples e universal | requiring specific adjustment in each agent and dispersing government |
| Eventos | desacoplamento e escala | unadequate for all request/reponse interaction |
| - a property SDK | produtividade inicial | lock-in and fragmented government |
| Plugin by agent | liberdade local | low re-use and inconsistent auditory |

## Consequences

The Tool Service/MCP Server becomes a security frontier and must have SLO, observation, version policy, rollback and onboarding. The adoption of MCP adds an operational box, but avoids that authorisation, audit and contracts are re-implemented by each agent.

## Minimum evidence

- contrato MCP versionado;
- owner and risk classification of the tool;
- the authorisations mater;
- tests of invariable arguments, negated access and idempotence;
- tracing a tracing agent, version, tool, policy and result;
- runbook, SLO and withdrawal strategy.

## Review criteria

Review the decision when the protocol leaves out security, compatibility, latability or interoperability requirements, or when another open framework offers equivalent government with less operational costs.
