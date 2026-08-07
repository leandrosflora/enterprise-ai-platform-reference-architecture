# Governance Service

## General view

Governance Service centralizes the approval cycle, publication, risk control and compliance with the agents and solutions of the plate.

## Responsabilidades

- Increasing flow of approval of agents
- Implementing corporative IA policies
- Registrating risk assessments
- Control publication, suspension and apprehension of agents
- Integrate AI Evaluation results into the decision-making process
- Maintain a reliable review of decisions

## Agent's Vida Ciclo

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

### Submeter Agent for Appropriation

```http
POST /governance/agents/{agentId}/submit
```

### Appropriate version

```http
POST /governance/agents/{agentId}/versions/{version}/approve
```

### Rejet

```http
POST /governance/agents/{agentId}/versions/{version}/reject
```

## Appropriations criteria

| Criteria | Description |
|---|---|
| Security | Authorisation, secrets and data exposure |
| LGPD | Personal data and sensitive data |
| IA Riss | Alucination, viés, explanation and operational impact |
| Observability | Logs, methods, trace and auditory |
| Costs | Model, volume and consumption limit |
| Qualidade | Maximum results in the evaluations defined |

## Dependencies

| Dependence | Uso |
|---|---|
| Agent Registry | Consult metads and versions |
| Evaluation Service | Consult evaluation results |
| Audit Service | Registrating decisions |
| PostgreSQL | Persistir workflows e pareceres |
| Kafka | Publicate government events |

## Eventos Publicados

- `governance.approved`
- `governance.rejected`
- `agent.published`
- `agent.retired`

## Non-functioning requirements

| Requisito | Diretriz |
|---|---|
| Auditoria | All decisions must be re-run |
| Segregation | Different types for creating, appendix and operator |
| Conformidade | Keep evidence of approval |
| Security | Application of BAC for the field, area and criticism |
| Escalabilidade | Suporting marrows and approval areas |

## Related Decisions

- (ADR-007 — Hybrid and IA summary assessment)(../adrs/007-evaluation-strategy.md)
