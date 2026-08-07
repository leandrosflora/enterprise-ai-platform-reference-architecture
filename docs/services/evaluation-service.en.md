# Evaluation Service

## General view

The Evaluation Service evaluates the quality of responses given by agents: based, relevance, alucine, toxicity and quality return. It is recommended by Agent Runtime to each injection and by Governance Service during the approval of agents.

## Responsabilidades

- Assess the basis and relevance of responses
- Detecting alucineation and toxicity
- Execute return assessments for new agents versions
- Publication of the results of evaluation for consumption by Governance and Audit
- Suporting syncrone (bloquer, for approval) and assyncrone (post-exercise, for continuous monitoring)

## Out of the scuff

- Officer's supervision
- End decision of approval (with Governance Service, which relates to the outcome of the evaluation)
- Cost calculator

## API Principal

```http
POST /evaluations
GET /evaluations/{id}
```

## Dependencies

| Dependence | Uso |
|---|---|
| Agent Runtime | Origin of the responses evaluated |
| Governance Service | Contained results for approval decision |
| Kafka | Publication and consorting evaluation events |

## Eventos Publicados

- `evaluation.started`
- `evaluation.completed`

## Non-functioning requirements

| Requisito | Diretriz |
|---|---|
| Latence | Singular evaluation must not block the answer to the user |
| Consistency | Detailed and reproducible evaluation criteria |
| Auditoria | All evaluation results are based on an invitation or agent version |
| Escalabilidade | Assessment in lot for return |

## Related Decisions

- (ADR-007 — Hybrid and IA summary assessment)(../adrs/007-evaluation-strategy.md)
