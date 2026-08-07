# Responsible AI

## Objective

Defining principles, decisions, controls and evidence so that AI solutions are fair, transparent, safe, reliable and supervised throughout the life cycle.

## Principles

| Principle | Architectural question | Expected evidence |
|---|---|---|
| Fairness | Does the system produce disproportional impact between groups? | metrics per segment, test dates and mitigation plan |
| Transparency | Do the user knows that he/she interacts with AI and what are his/her limits? | Notification of use, Agent Card and published limitations |
| Explicabilidade | Is it possible to justify answers or decisions? | citations, relevant factors, rationale allowed and decision trail |
| Accountability | Is there a person responsible for risk, operation and outcome? | owner, approvers, ICA and decision record |
| Privacy | Does data use respect purpose, minimization and retention? | classification, legal basis, IAD/ALI when applicable and TTL |
| Security | Are inputs, context, memory, tools and outputs treated as unreliable? | threat model, adverse tests and technical controls |
| Robustez | Does the system degrade safely in the face of failures or changes? | fallback, circuit breaker, resilience tests and rollback |
| Human supervision | Is autonomy proportional to the impact? | human-in-the-loop, transactional limits and segregation of function |

## Life cycle

```mermaid
flowchart LR
    A[Ideia] --> B[Risk assessment]
    B --> C[Dados e modelo]
    C --> D[Design e controles]
    D --> E[Evaluation]
    E --> F[Aprovação]
    F --> G[Produção]
    G --> H[Monitoramento]
    H --> I[Reavaliação ou retirada]
```

## Requirements per stage

### Discovery and design

- define purpose, users, impact and use limits;
- rating risk and data;
- identify potentially affected groups;
- determine the maximum degree of autonomy;
- register alternatives not based on AI.

### Construction

- use approved and traceable sources;
- version prompts, models, policies and datasets;
- separate reliable instructions from unreliable content;
- applying minimisation, masking and access controls;
- implement proportional explanations to the use case.

### Evaluation

- measure quality, groundedness, safety, bias and robustness;
- perform adverse tests and relevant segments;
- compare against baseline and previous version;
- require human review for HIGH and CRITICAL risks.

### Operation

- monitoring drift, regression, toxicity, incidents and cost;
- register decisions and tool calls without exposing sensitive content;
- maintaining a channel of contestation and human scheduling;
- re-evaluate after model change, prompt, source or purpose.

## Fairness and bias

Fairness should be assessed only with legitimate attributes and segments for the context.The removal of a sensitive attribute does not necessarily eliminate the bias, as proxies may remain.

Minimum controls:

1. define groups and metrics before the test;
2. analyze disparity of precision, false positives and false negatives;
3. to review the representativeness and quality of data;
4. document trade-offs between performance and equity;
5. blocking publication when the residual impact is not accepted.

## Transparency for the user

All experience shall inform:

- that there is AI involved;
- which data are used;
- which actions the system can perform;
- known limitations;
- how to request human review;
- how to contest or correct a decision.

## Human-in-the-loop

| Impacto | Supervision pattern |
|---|---|
| Package leaflet | sampling review |
| Recommendation | humano decide |
| Reversible writing | Explicit confirmation |
| Critical writing | Double approval or segregation of function |
| Adjusted decision | final human decision or specific legal control |

## Compulsory evidence

- Agent Card ou Model Card;
- risk assessment;
- dataset and assessment report;
- authorization matrix;
- justification for the level of autonomy;
- recording of residual limitations and risks;
- monitoring plan, rollback and withdrawal.
