# 9. Checklists of production

## How to use

Checklists are verification tools, not substitutes for analysis.Non-applicable items must be marked with a justification.Compulsory items that are not met require a formal blocking or exception with owner and validity.

## 1. Business readiness

- [ ] problem and user are defined;
- [ ] outcome and success metrics have been agreed;
- [ ] there is a business owner;
- [ ] there is a technical owner;
- [ ] the AI-free alternative has been considered;
- [ ] the impact of incorrect responses has been analysed;
- [ ] feedback process has been defined;
- [ ] communication and adoption strategy exists;
- [ ] closure or deactivation criteria are defined.

## 2. Architecture readiness

- [ ] context and containers are documented;
- [ ] boundaries between control plane and data plane are explicit;
- [ ] registration systems remain authoritative;
- [ ] API contracts, events and tools are versioned;
- [ ] agent versus workflow decision is recorded;
- [ ] synchronicity and asynchronous processing are warranted;
- [ ] timeouts, retries and circuit breakers are defined;
- [ ] impotence exists for side effects;
- [ ] fallback and controlled degradation have been designed;
- [ ] ADRs cover relevant decisions;
- [ ] dependencies and failure modes have been identified.

## 3. Identity and authorization

- [ ] users are authenticated by an approved IDP;
- [ ] workloads use their own identity;
- [ ] tokens are validated by issuer, audience, validity and signature;
- [ ] minimum scopes are defined;
- [ ] authorisation is `deny by default`;
- [ ] tenant and subject are not freely chosen by the client;
- [ ] access to agents, knowledge bases, memory and tools is independent;
- [ ] service-to-service utiliza mecanismo aprovado;
- [ ] privilege elevation has been tested;
- [ ] revocation of access has been exercised.

## 4. Data, RAG and memory

- [ ] sources have owner and classification;
- [ ] purpose of use is recorded;
- [ ] intake pipeline uses quarantine;
- [ ] checksum and provenance are preserved;
- [ ] malware, active content and indirect prompt injection are treated;
- [ ] ACL is applied by document and chunk;
- [ ] mandatory filters are not dependent on query text;
- [ ] recovered content is treated as unreliable;
- [ ] citations point to sources accessible to the user;
- [ ] expiration and deletion remove content from retrieval;
- [ ] embeddings and chunking are versioned;
- [ ] memory types are explicit;
- [ ] maximum TTL is applied;
- [ ] consent exists when required;
- [ ] memory does not replace a recording system;
- [ ] memory poisoning and cross-subject access were tested.

Consulte [Security of RAGand memory](../security/rag-memory-security.md).

## 5. Model and prompt readiness

- [ ] the model is in the approved catalogue;
- [ ] region and processing are policy-friendly;
- [ ] the main prompt is versioned;
- [ ] parameters have limits;
- [ ] input and output token limits are defined;
- [ ] maximum cost per execution is controlled;
- [ ] model fallback has been tested where applicable;
- [ ] redaction and filters are configured;
- [ ] change of model triggers reassessment;
- [ ] dependency on ownership capacity was recorded.

## 6. Tool and MCP readiness

- [ ] tool has owner and version;
- [ ] Entry and exit scheme is restrictive;
- [ ] scopes are minimal;
- [ ] read and write operations are distinguishable;
- [ ] timeout and limits exist;
- [ ] idempotence has been validated;
- [ ] retries do not duplicate effects;
- [ ] clearing or rollback has been defined;
- [ ] HITL exists for critical actions;
- [ ] arguments are validated outside the template;
- [ ] tool can be locked without knocking down the runtime;
- [ ] audit records operation without exposing secrets.

## 7. Security and privacy

- [ ] threat model is updated;
- [ ] risk classification has been confirmed;
- [ ] secrets are not in the code or prompt;
- [ ] sensitive data shall be minimised;
- [ ] logs and traces have redaction;
- [ ] retention and discard have been defined;
- [ ] legal basis or justification for purpose has been examined;
- [ ] leakage incidents have runbook;
- [ ] dependencies and images have been verified;
- [ ] egress is controlled;
- [ ] transit and rest encryption is applied;
- [ ] Exceptions have compensating controls and expiration.

## 8. Evaluation readiness

- [ ] dataset represents real cases and edge cases;
- [ ] dataset and version are identified;
- [ ] baseline is defined;
- [ ] the quality of the task is measured separately;
- [ ] retrieval and groundedness are assessed separately;
- [ ] prompt injection and leakage are part of the tests;
- [ ] tool selection and arguments are evaluated;
- [ ] performance and cost have thresholds;
- [ ] regressions block risk-based release;
- [ ] results are reproducible;
- [ ] production samples feed controlled review;
- [ ] Human evaluation has consistent scope and criteria.

## 9. Observability and SRE

- [ ] correlation ID is propagated;
- [ ] agent, version, model, tenant and session are correlated;
- [ ] success, latency, tokens and cost metrics exist;
- [ ] policy denials are observable;
- [ ] retrieval, memory and tools have spans;
- [ ] logs do not store full prompts by default;
- [ ] SLO is defined by workload;
- [ ] alerts have owner and expected action;
- [ ] dashboards have been reviewed with the support team;
- [ ] capacity has been tested;
- [ ] critical dependencies have a circuit breaker or fallback;
- [ ] runbooks are accessible;
- [ ] on-call and staging are defined;
- [ ] rollback foi exercitado.

## 10. FinOps readiness

- [ ] costs have tags or dimensions per agent and tenant;
- [ ] tokens and cost are measured by model;
- [ ] monthly and daily budgets are defined;
- [ ] quotas preventivas existem;
- [ ] anomaly alerts are set;
- [ ] cost per successful task is accompanied;
- [ ] re-indexation and embeddings enter the cost model;
- [ ] observability and shared infrastructure are considered;
- [ ] showback or chargeback has been defined where necessary;
- [ ] strategy to reduce cost without degrading quality was analysed.

## 11. Governance and release

- [ ] the submitted version is frozen;
- [ ] evidence corresponds to the published artifact;
- [ ] decision-makers shall have the necessary authority and independence;
- [ ] approval conditions are verifiable;
- [ ] approval is valid;
- [ ] pipeline verifies decision before publication;
- [ ] canary or progressive rollout is defined;
- [ ] feature flags and kill switch exist where applicable;
- [ ] release notice has been prepared;
- [ ] post-release review is scheduled;
- [ ] reassessment triggers are set.

## 12. Retirement readiness

- [ ] consumers and users have been identified;
- [ ] a migration or replacement plan exists;
- [ ] new invocations may be blocked;
- [ ] credentials and scopes shall be revoked;
- [ ] knowledge and memory shall have an appropriate purpose;
- [ ] audit evidence shall be retained in accordance with policy;
- [ ] budgets, dashboards and alerts will be closed;
- [ ] documentation and catalogue shall be updated;
- [ ] owner approved the withdrawal.

## Release decision record

The final decision may use the following summary:

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

- deliver measurable value;
- has a known risk and controls applied;
- can be observed and sustained;
- tem custo controlado;
- may be reversed, suspended and withdrawn;
- has evidence to explain why it was published.

## Next to materials

- [Glossary of terms](glossary.md)
- [Runbooks](../runbooks/onboarding-agent.md)
- [AI Risk Framework](../governance/ai-risk-framework.md)
- [Non-functional requirements](../architecture/non-functional-requirements.md)
