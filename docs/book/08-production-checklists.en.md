# 9. Production checks

## How to use

Checks are verification instruments, not substitutes for analysis. Not applicable checks must be marked with proof. Not-assisted obligations require a formal block or exemption with owner and validity.

## 1. Business readiness

- [ ] problem and user are defined;
- [ ] outcome and success methods were agreed;
- [ ] there is a business owner;
- [ ] there is a technical owner;
- [ ] the alternative without IA was considered;
- [ ] impact of incorrect responses was analysed;
- [ ] feedback process was defined;
- [ ] communication strategy and adoption;
- [ ] acrimony criteria are defined.

## 2. Architecture readiness

- [ ] context and containers are documented;
- [ ] border between control plane and data plane are explcitative;
- [ ] registry systems remain ad hoc;
- [ ] API contracts, events and tools are updated;
- [ ] agent decision versus workflow is registered;
- [ ] synchronism and assynchronism are justified;
- [ ] timeouts, retries and circuit breakers are defined;
- [ ] idempotence exists for calamities;
- [ ] fallback and controlless degradation were discarded;
- [ ] DDRs cover relevant decisions;
- [ ] dependencies and failure modes were identified.

## 3. Identity and authorization

- [ ] users are authenticated by approved IdP;
- [ ] workloads use their own identity;
- [ ] tokens are valid by the issuer, audience, validity and signature;
- [ ] minimum scopes are defined;
- [ ] authorisation is `deny by default`;
- [ ] tenant and subject are not chosen freely by the client;
- [ ] access to agents, knowledge bases, memory and tools is independent;
- [ ] service-to-service utiliza mecanismo aprovado;
- [ ] a high-quality equestrian was tested;
- [ ] access revogasion was exercised.

## 4. Data, RAG and memory

- [ ] sources have ownership and classification;
- [ ] the use quality is registered;
- [ ] a pipe of ingesting using quarentine;
- [ ] checksum and provenance are preserved;
- [ ] malware, active and indirect content prompt injection are treated;
- [ ] ACL is applied by document and chunk;
- [ ] compulsory filters do not depend on the text of the query;
- [ ] the content recovered is treated as untrustworthy;
- [ ] references point to access sources to the user;
- [ ] expiration and excluding removal of the retrieval;
- [ ] embeddings and chunking are versioned;
- [ ] types of memory are expended;
- [ ] Maximum TTL is applied;
- [ ] consent exists when required;
- [ ] memory does not replace the register system;
- [ ] memory poisoning e acesso cross-subject foram testados.

Consult [Security of RAG and memory](../security/rag-memory-security.md).

## 5. Model and prompt readiness

- [ ] model is in the approved catalogue;
- [ ] region and process are concerned with policy;
- [ ] the main prompt is updated;
- [ ] sluts have limits;
- [ ] input and output token limits are defined;
- [ ] the maximum cost for execution is controlled;
- [ ] model fallback was tested when applicable;
- [ ] redaction and filters are configured;
- [ ] change of model model re-evaluation;
- [ ] dependencies of property capacity were recorded.

## 6. Tool and MCP readiness

- [ ] tool can be owner and version;
- [ ] entry and exit schema is restrictive;
- [ ] scopes are minimal;
- [ ] reading and writing operations are distinct;
- [ ] timeout e limites existem;
- [ ] idempotence was valid;
- [ ] retries do not double effect;
- [ ] compensation or rollback was defined;
- [ ] HITL exists for critical actions;
- [ ] arguments are valid outside the model;
- [ ] tool can be blocked without removing the runtime;
- [ ] auditors register operations without secret.

## 7. Security and privacy

- [ ] threat model is updated;
- [ ] risk classification was confirmed;
- [ ] secrets are not in the code or prompt;
- [ ] sensitive data are minimised;
- [ ] logs e traces possuem redaction;
- [ ] retention and discharge were defined;
- [ ] legal or justifiable basis of finality was analysed;
- [ ] vassing incidents may runbook;
- [ ] dependencies and images have been checked;
- [ ] the exit is controlled;
- [ ] trajectorium in transit and recurrent is applied;
- [ ] exceptions may compensate for controls and expiration.

## 8. Evaluation readiness

- [ ] dataset representa casos reais e edge cases;
- [ ] dataset and version are identified;
- [ ] baseline is defined;
- [ ] the quality of the task is measured separately;
- [ ] retrieval and groundedness are assessed separately;
- [ ] prompt injection and leakage are part of the tests;
- [ ] tool selection and arguments are evaluated;
- [ ] performance e custo possuem thresholds;
- [ ] regresses bloated release conform to risk;
- [ ] results are reproduzable;
- [ ] food samples are reviewed controlled;
- [ ] human evaluation has consistent rules and criteria.

## 9. Observability and SRE

- [ ] ID correlation is propagated;
- [ ] agent, version, model, tenant and session are correlating;
- [ ] success, consistency, tokens and cost are required;
- [ ] policy of refusals is observed;
- [ ] retrieval, memory e tools possuem spans;
- [ ] logs do not hold complete prompts by default;
- [ ] SLO is defined by workload;
- [ ] alerts may be owned and acted;
- [ ] dashboards were reviewed with the support team;
- [ ] capacidade foi testada;
- [ ] critical dependencies may have circuit breaker or fallback;
- [ ] runbooks are accessible;
- [ ] on-call and escalonation are defined;
- [ ] rollback foi exercitado.

## 10. FinOps readiness

- [ ] costs may be tags or dimensions by agent and tenant;
- [ ] tokens and cost are medmed by model;
- [ ] monthly and daily budgets are set;
- [ ] quotas preventivas existem;
- [ ] anomalies alerts are configured;
- [ ] the cost for a well-known task is accompanied;
- [ ] reindexation and embeddings enter the cost model;
- [ ] observation and comparable infrastructure are considered;
- [ ] showback or chargeback was defined when necessary;
- [ ] strategy to reduce costs without degrade quality was analysed.

## 11. Governance and release

- [ ] the submetid version is frozen;
- [ ] evidence corresponds to the published article;
- [ ] decisions have the authority and independence necessary;
- [ ] approval conditions are verified;
- [ ] approval may be valid;
- [ ] pipeline checks decision before publication;
- [ ] a tonne or a progressive rollout is defined;
- [ ] feature flags and kill switch exist when applicable;
- [ ] release communication was prepared;
- [ ] post-release revision is scheduled;
- [ ] reavailing shit are defined.

## 12. Retirement readiness

- [ ] consumers and users were identified;
- [ ] migration plan or replacement exists;
- [ ] new voices may be blocked;
- [ ] certificates and scopes shall be reviewed;
- [ ] knowledge and memory will have appropriate destination;
- [ ] auditory evidence shall be withdrawn in accordance with policy;
- [ ] budgets, dashboards and alerts will be closed;
- [ ] documentation and catalog will be analyzed;
- [ ] owner approved the withdrawal.

## Release decision record

The final decision may be used as follows:

```yaml
agentId: policy-assistant
agentVersion: 1.2.0
riskClassification: MEDIUM
releaseDecision: APPROVED
approvedAt: 2026-07-19T18:00:00Z
validUntil: 2027-01-19T18:00:00Z
conditions:
  - internal-users-only
  - long-term-memory-disabled
  - daily-budget-usd-100
artifacts:
  evaluation: evaluation-report.json
  threatModel: threat-model.md
  runbook: runbook.md
rollback:
  method: feature-flag
  targetVersion: 1.1.0
owners:
  business: corporate-governance
  technical: ai-product-squad
```

## Definition of done for a published version

A version is ready when:

- deliver a measurable value;
- may be a known risk and controlled;
- may be observed and supported;
- tem custo controlado;
- may be reverted, suspended and withdrawn;
- I can have evidence to explain why it was published.

## Materials next

- [Glossary](glossary.md)
- [Runbooks](../runbooks/onboarding-agent.md)
- [AI Risk Framework](../governance/ai-risk-framework.md)
- (Not working requirements)(../architecture/non-functional-requirements.md)
