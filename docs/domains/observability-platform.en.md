# Observability Platform

## Objective

Provide traceability, metrics, logs and dashboards for the operation of Enterprise AI Platform.

## Capacities

- Agent Tracing
- Distributed Tracing
- Logs Correlacionados
- Metrics
- Token Tracking
- Cost Observability
- Alerting

## Related Services

- Agent Runtime
- Audit Service
- Billing Service
- Observability Stack

## Events

- agent.invoked
- tool.executed
- audit.created

## KPIs

| indicator | Description |
|---|---|
| Latency P95 | Latency by agent and service |
| Error Rate | Component error rate |
| Token Usage | Token consumption |
| Trace Coverage | Coverage of traces for execution |

## Non-functional requirements

- OpenTelemetry as standard
- Compulsory CorrelationId
- Sensitive data masking
- Retention defined by type of telemetry
- Dashboards per platform, agent and area
