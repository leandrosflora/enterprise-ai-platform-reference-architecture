# Governance Service

## Overview

The Governance Service centralizes the cycle of approval, publication, risk control and compliance of the platform's AI agents and solutions.

## responsibilities

- Management of approval flows for agents
- Implementing corporate AI policies
- Registering risk assessments
- Controlling publication, suspension and retirement of officials
- Integrating IA Evaluation results to the decision-making process
- Keep audible decision track

## Lifecycle of the Agent

```text
Draft
  ↓
Submitted for Review
  ↓
Risk Assessment
  ↓
Technical Review
  ↓
Compliance Review
  ↓
Approved / Rejected
  ↓
Published
  ↓
Retired
```

## APIs

### Submeter Agent for Approval

```http
POST /governance/agents/{agentId}/submit
```

### Approval Version

```http
POST /governance/agents/{agentId}/versions/{version}/approve
```

### Reject Version

```http
POST /governance/agents/{agentId}/versions/{version}/reject
```

## Approval Criteria

| Criteria | Description |
|---|---|
| Security | Authentication, authorization, secrecy and data exposure |
| LGPD | Processing of personal and sensitive data |
| Risk of AI | Hallucination, bias, explainability and operational impact |
| Observability | Logs, metrics, traces and audit |
| Costs | Model, expected volume and consumption limit |
| Quality | Minimum result in the defined assessments |

## Dependencies

| Dependence | Use |
|---|---|
| Agent Registry | Refer to metadata and versions |
| Evaluation Service | Refer to assessment results |
| Audit Service | Register decisions |
| PostgreSQL | Persist workflows and opinions |
| Kafka | Publicating governance events |

## published events

- `governance.approved`
- `governance.rejected`
- `agent.published`
- `agent.retired`

## Non-functional requirements

| Requirements | Guideline |
|---|---|
| Audit | All decisions must be traceable |
| Segregation | Different papers for creator, approver and operator |
| Conformity | Store evidence of approval |
| Security | Applying RBAC by domain, area and criticality |
| scalability | Support multiple areas and approval treadmills |

## Related Decisions

- [ADR-007 — Hybrid and continuous AI assessment](../adrs/007-evaluation-strategy.md)
