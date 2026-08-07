# ADR-007  Hybrid and continuous assessment of AI

**Status:** Aceito

## Contexto

Corporate agents need to be evaluated before and after publication to reduce hallucinations, low relevance, retrieval failures, misuse of tools, uncertain responses, and quality regressions.

## Decision

Adopt a **Evaluation Service** with a hybrid rating:

- automatically for scale and regression;
- based on rules for deterministic requirements;
- model-based where subjective controlled criteria exist;
- human for critical cases, samples and calibration;
- offline before the promotion and online during the operation.

Results shall be versioned, reproducible and traceable to the agent, prompt, model, dataset, policy, knowledge snapshot and code evaluated.

## Minimum dimensions

- the quality of the task;
- retrieval and groundedness;
- citation correctness;
- safety, toxicity and leakage;
- selection and argumentation of tools;
- latency and reliability;
- cost per invocation and completed task;
- regression against baseline and previous version.

## Alternativas

| Alternativa | Vantagem | Limitation |
|---|---|---|
| Manual only assessment | julgamento contextual | Low scale, cost and variability |
| Assessment only in production | actual use data | risk of publishing undetected regressions |
| Only LLM-as-judge | Rapid coverage | prejudice, instability and dependence on the judge |
| Single aggregate note | simple communication | hides critical defects in specific dimensions |

## Positive consequences

- evidence-based publishing gates;
- reproducible comparison between versions;
- the detection of degradation during the operation;
- combination of automatic scale with risk-proportionate human judgment.

## Negative consequences

- increase the cost of running and maintaining datasets;
- metrics and judges may differ from business perceptions;
- outdated datasets generate false confidence;
- Critical scenarios continue to require independent review.

## Minimum evidence

- versioned and approved dataset;
- Baseline and thresholds by dimension;
- the version of the evaluator and the judge;
- the return report;
- Network team results and negative tests;
- human review and conformity sample, where applicable;
- the decision on promotion, exception or blocking.

## The Commission shall adopt delegated acts in accordance with Article 21 of this Regulation.

Review when metrics no longer correlate with actual results, when there is drift from the dataset or domain, when evaluation costs become disproportionate, or when new methods offer greater validity and reproducibility.
