# Observability Platform

## Objet

Providing rastreability, methods, logs and dashboards for operation of Enterprise AI Platform.

## Capacidades

- Agent Tracing
- Distributed Tracing
- Logs Correlacionados
- Metrics
- Token Tracking
- Cost Observability
- Alerting

## Relacionated services

- Agent Runtime
- Audit Service
- Billing Service
- Observability Stack

## Eventos

- agent.invoked
- tool.executed
- audit.created

## KPIs

| Indicador | Description |
|---|---|
| Latency P95 | Service and agent skills |
| Error Rate | error rate by component |
| Token Usage | Consumption of tokens |
| Trace Coverage | traces cover for execution |

## Non-functioning requirements

- OpenTelemetry as a symphony
- - a compulsory correction
- Sensitive data masking
- Retention defined by type of telemetry
- Dashboards by platform, agent and area
