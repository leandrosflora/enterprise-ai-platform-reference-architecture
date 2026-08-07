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

## Other services

- Agent Runtime
- Audit Service
- Billing Service
- Observability Stack

## Events

- agent.invoked
- tool.executed
- audit.created

## KPIs

| Indicador | Other information |
|---|---|
| Latency P95 | Latency by agent and service |
| Error Rate | Error rate per component |
| Token Usage | Use of tokens |
| Trace Coverage | Trace coverage by execution |

## Non-functional requirements

- OpenTelemetry as standard
- Compulsory correlation
- Masking of sensitive data
- Retention defined by type of telemetry
- Dashboards by platform, agent and area
