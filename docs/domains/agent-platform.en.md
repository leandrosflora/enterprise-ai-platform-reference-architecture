# Agent Platform

## Objective

Providing central capacities for the creation, execution, publication and operation of corporate agents.

## Capacities

- Agent Gateway
- Agent Runtime
- Agent Registry
- Multi-Agent Orchestration
- Tool Calling
- Agent Lifecycle Management

## Related Services

- Agent Gateway
- Agent Runtime
- Agent Registry
- Governance Service
- Evaluation Service

## Events

- agent.created
- agent.updated
- agent.published
- agent.retired
- agent.invoked
- tool.executed

## KPIs

| indicator | Description |
|---|---|
| Invocations | Volume of executions of officials |
| Success Rate | Percentage of successful executions |
| Latency P95 | 95th percentile latency per agent |
| Tool Call Rate | Use of tools for implementation |
| Cost per Agent | Operating cost per agent |

## Non-functional requirements

- Authorisation by agent and scope
- Overall observability
- Audit for implementation
- Cost control per agent
- Resilience against model and tool failure
