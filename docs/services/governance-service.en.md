# Governance Service

## General view

Governance Service centralizes the approval, publication, risk control and compliance cycle of AI agents and solutions on the platform.

## Responsabilidades

- Manage the approval flow of agents
- Implementing corporate AI policies
- Registering risk assessments
- Monitoring the publication, suspension and retirement of agents
- Integrating AI Evaluation results into the decision-making process
- Maintaining an auditable decision track

## Life cycle of the agent

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

### Submitting Agent for Approval

```http
POST /governance/agents/{agentId}/submit
```

### Approve version

```http
POST /governance/agents/{agentId}/versions/{version}/approve
```

### Rejected Version

```http
POST /governance/agents/{agentId}/versions/{version}/reject
```

## Criteria for approval

| Criterion of use | Other information |
|---|---|
| Security | Authentication, authorisation, secrecy and data exposure |
| LGPD | Processing of personal data and sensitive data |
| Risk of AI | Allucination, bias, explainability and operational impact |
| Observability | Logs, metrics, traces and audit |
| Costs | Model, expected volume and consumption limit |
| Qualidade | Minimum result in defined assessments |

## Dependencies

| Dependence | Uso |
|---|---|
| Agent Registry | Reviewing metadata and versions |
| Evaluation Service | See the results of the evaluation |
| Audit Service | Registering decisions |
| PostgreSQL | Persistent workflows and opinions |
| Kafka | Publishing governance events |

## Events Published

- `governance.approved`
- `governance.rejected`
- `agent.published`
- `agent.retired`

## Non-functional requirements

| Requisito | Diretriz |
|---|---|
| Auditoria | All decisions must be traceable |
| Separation | Roles distinct for creator, authorising officer and operator |
| Conformidade | Keeping evidence of approval |
| Security | Apply RBAC by domain, area and critical |
| Escalabilidade | Support multiple areas and approval treadmills |

## Related Decisions

- [ADR-007  Hybrid and continuous assessment of AI](../adrs/007-evaluation-strategy.md)
