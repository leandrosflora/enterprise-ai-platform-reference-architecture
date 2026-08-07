# ADR-007 — Hybrid and continuous AI assessment

**Status:** accepted

## Context

Corporate agents need to be evaluated before and after publication to reduce hallucination, low relevance, retrieval failures, incorrect use of tools, unsafe responses and quality regressions.Manual evaluation only does not scale; evaluation only in production exposes users and processes to avoidable risk.

## Decision

Adopt a **Evaluation Service** with hybrid assessment:

- automatic for scale and regression;
- based on rules for deterministic requirements;
- model-based when there are controlled subjective criteria;
- human for critical cases, samples and calibration;
- offline before promotion and online during operation.

Results should be versioned, reproducible and traceable to the agent, prompt, model, dataset, policy, knowledge snapshot and code evaluated.

## Minimum dimensions

- quality of the task;
- retrieval and groundedness
- citation correctness;
- safety, toxicity and leakage;
- selection and arguments of tools;
- latency and reliability;
- cost per invocation and task completed;
- regression against baseline and previous version.

## Alternatives

| alternative | advantage | Limitation |
|---|---|---|
| Manual assessment only | Contextual judgment | low scale, cost and variability |
| Production assessment only | real use data | Risk of publication of undetected regressions |
| Only LLM-as-judge | fast coverage | bias, instability and judge dependence |
| Single aggregate note | simple communication | it hides critical flaws in specific dimensions of the study. |

## Positive consequences

- evidence-based publication gates;
- reproducible comparison between versions
- detection of degradation during operation;
- combined automatic scale with human judgment proportional to risk.

## Negative consequences

- increases the cost of implementing and maintaining dataset;
- metrics and judges may differ from business perception;
- outdated dates generate false confidence;
- critical scenarios remain requiring independent review.

## Minimum evidence

- dataset verified and approved;
- baseline and thresholds per dimension;
- evaluator and judge version;
- regression report;
- red-team results and negative tests;
- human review sample and agreement where applicable;
- decision to promote, except or block.

## Review criteria

To review when metrics no longer correlate with real results, when there is drift of the dataset or domain, when evaluation costs become disproportional, or when new methods offer greater validity and reproducibility.
