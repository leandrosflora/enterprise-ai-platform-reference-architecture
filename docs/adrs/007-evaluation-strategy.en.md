# ADR-007 — Hybrid and iA summary

**Status:** Aceito

## Contexto

Corporate agents need to be assessed before and after publication to reduce alucination, low-resolution, retrieval failures, tool-incorrection, insecure responses and quality return. Assessment only manual does not escalate; assessment only in production using unused expenditures and processes at risk.

## Decision

Adopt a **Evaluation Service** with a full assessment:

- autometic for scala and return;
- based on rules for certain requirements;
- model-based when there are controlled sub-jet criteria;
- human for critical, amothos and calibration cases;
- offline before promotion and online during operation.

Results shall be compiled, reproduced and rastreaved to the agent, prompt, model, dataset, policy, knowledge snapshot and code evaluated.

## Minimum dimensions

- quality of the task;
- retrieval e groundedness;
- citation correctness;
- safety, toxicity and leakage;
- selection and arguments of tools;
- latability and confidentiality;
- cost for invocation and completion of the task;
- return against baseline and previous version.

## Alternativas

| Alternativa | Vantagem | Limitation |
|---|---|---|
| Assessment only manual | julgamento contextual | baixa escala, custo e variabilidade |
| Assessment only in production | real usage data | risk of publicising unidentified regressives |
| Just LLM-as-judge | quick coverage | you saw, instability and dependency of the judge |
| Single agregated note | simple communication | squeezing critical words in specific dimensions |

## Positive consequences

- publications gates based on evidence;
- reductive comparison of versions;
- degradation detection during operation;
- Combined automa-scaling with human judgment proportionate to risk.

## Negative consequences

- increase the cost of execution and maintenance of datasets;
- methods and judges may differ from the perception of the business;
- datasets unattended have been false trust;
- Critical scenarios remain required independent review.

## Minimum evidence

- dataset versionado e aprovado;
- baseline and thresholds per dimension;
- version of the assessor and judge;
- report on return;
- results of a team network and negative tests;
- human review sample and consistency when applicable;
- Decision of promotion, exemption or block.

## Review criteria

Review when methods are not able to match real results, when the dataset or field drifts, when assessment costs become unsuitable or when new methods offer greater validity and reproducibility.
