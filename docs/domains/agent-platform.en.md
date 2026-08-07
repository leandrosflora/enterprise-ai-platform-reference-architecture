# Agent Platform

## Objective

Provide the core capabilities for the creation, execution, publication and operation of corporate agents.

## Capacities

- Agent Gateway
- Agent Runtime
- Agent Registry
- Multi-Agent Orchestration
- Tool Calling
- Agent Lifecycle Management

## Other services

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

| Indicador | Other information |
|---|---|
| Invocations | Volume of executions of agents |
| Success Rate | Percentage of executions successfully completed |
| Latency P95 | 95 percent latency per agent |
| Tool Call Rate | Use of tools by execution |
| Cost per Agent | Operating cost per agent |

## Non-functional requirements

- Authorisation by agent and scope
- End-to-end visibility
- Implementing audit
- Cost control by agent
- Resilience to model and tool failures
