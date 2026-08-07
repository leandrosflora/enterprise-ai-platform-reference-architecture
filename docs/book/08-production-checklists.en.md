# 9. Production checklists

## How to use

Checklists are verification instruments, not substitutes for analysis.Non-applicable items should be marked with justification.Compulsory items not met need formal block or exception with owner and validity.

## 1. Business readiness

- [ ] problem and user are defined;
- [ ] outcome and success metrics were agreed;
- [ ] there is business owner;
- [ ] there is a technical owner;
- [ ] a alternativa sem IA foi considerada;
- [ ] impacto de respostas incorretas foi analisado;
- [ ] feedback process was defined;
- [ ] Communication strategy and adoption exists;
- [ ] closure or deactivation criteria are defined.

## 2. Architecture readiness

- [ ] context and containers are documented;
- [ ] limits between control plane and date plane are explicit;
- [ ] registration systems remain authoritative;
- [ ] API contracts, events and tools are borrowed;
- [ ] agent versus workflow decision is registered;
- [ ] synchrony and asynchronous processing are justified;
- [ ] timeouts, retries and circuit breakers are defined;
- [ ] non-demographic effects exist for side effects;
- [ ] fallback and controlled degradation have been designed;
- [ ] ADRs cover relevant decisions;
- [ ] dependencies and failure modes were identified.

## 3. Identity and authorization

- [ ] users are authenticated by approved PPI;
- [ ] workloads use their own identity;
- [ ] tokens are validated by issuer, audience, validity and signature;
- [ ] minimum scopes are defined;
- [ ] authorisation is `deny by default`;
- [ ] tenant and subject are not freely chosen by the client;
- [ ] access to agents, knowledge bases, memory and tools is independent;
- [ ] service-to-service utiliza mecanismo aprovado;
- [ ] elevation of privilege was tested;
- [ ] withdrawal of access was exercised.

## 4. Data, RAG and memory

- [ ] sources have owner and classification;
- [ ] purpose of use is registered;
- [ ] pipeline for ingestion uses quarantine;
- [ ] checksum and provenance are preserved;
- [ ] malware, active content and indirect prompt injection are treated;
- [ ] ACL is applied by document and chunk;
- [ ] mandatory filters do not depend on the text of the query;
- [ ] content recovered is treated as unreliable;
- [ ] citations point to accessible sources to the user;
- [ ] expiration and exclusion remove retrieval content;
- [ ] embeddings and chunking are versioned;
- [ ] types of memory are explicit;
- [ ] Maximum TTL is applied;
- [ ] consent exists when required;
- [ ] memory does not replace the recording system;
- [ ] memory poisoning e acesso cross-subject foram testados.

Consulte [AGR security and memory](../security/rag-memory-security.md).

## 5. Model and prompt readiness

- [ ] model is in the approved catalogue;
- [ ] region and processing meet the policies;
- [ ] main prompt is versioned;
- [ ] parameters have limits;
- [ ] input and output token limits are defined;
- [ ] maximum cost per implementation is controlled;
- [ ] model fallback was tested when applicable;
- [ ] redaction and filters are configured;
- [ ] model change triggers reassessment;
- [ ] ownership capacity dependence was registered.

## 6. Tool and MCP readiness

- [ ] tool has owner and version;
- [ ] entry and exit scheme is restrictive;
- [ ] scopes are minimum;
- [ ] reading and writing operations are distinguishable;
- [ ] timeout e limites existem;
- [ ] inequality was validated;
- [ ] retries do not double effects;
- [ ] compensation or rollback has been defined;
- [ ] HITL exists for critical actions;
- [ ] arguments are validated outside the model;
- [ ] tool can be blocked without breaking the runtime;
- [ ] audit registers operation without exposing secrets.

## 7. Security and privacy

- [ ] threat model is updated;
- [ ] risk classification was confirmed;
- [ ] secrets are not in the code or prompt;
- [ ] sensitive data are minimized;
- [ ] logs e traces possuem redaction;
- [ ] retention and disposal were defined;
- [ ] legal basis or justification for purpose was analysed;
- [ ] incidentes de vazamento possuem runbook;
- [ ] facilities and images were checked;
- [ ] egress is controlled;
- [ ] transit and rest cryptography is applied;
- [ ] exceptions have compensating controls and expiration.

## 8. Evaluation readiness

- [ ] dataset represent real cases and edge cases;
- [ ] dateset and version are identified;
- [ ] baseline is defined;
- [ ] quality of the task is measured separately;
- [ ] retrieval and groundedness are evaluated separately;
- [ ] prompt injection e leakage fazem parte dos testes;
- [ ] tool selection and arguments are evaluated;
- [ ] performance and cost have thresholds;
- [ ] regressions block release according to risk;
- [ ] results are reproducible;
- [ ] production samples feed controlled review;
- [ ] human assessment has consistent heading and criteria.

## 9. Observability and SRE

- [ ] correlation ID is propagated;
- [ ] agent, version, model, tenant and session are correlated;
- [ ] success, latency, tokens and cost metrics exist;
- [ ] policy denials are observable;
- [ ] retrieval, memory e tools possuem spans;
- [ ] logs do not store complete prompts per pattern;
- [ ] SLO is defined by workload;
- [ ] alerts have owner and expected action;
- [ ] dashboards foram revisados com a equipe de suporte;
- [ ] capacity has been tested;
- [ ] critical dependencies have circuit breaker or fallback;
- [ ] runbooks are accessible;
- [ ] on-call and scheduling are defined;
- [ ] rollback foi exercitado.

## 10. FinOps readiness

- [ ] costs have tags or dimensions per agent and tenant;
- [ ] tokens and costs are measured by model;
- [ ] monthly and daily budget are defined;
- [ ] quotas preventivas existem;
- [ ] anomaly warnings are set;
- [ ] cost per successful task is followed;
- [ ] re-indexation and embeddings enter the cost model;
- [ ] observability and shared infrastructure are considered;
- [ ] showback or chargeback was defined when necessary;
- [ ] strategy to reduce cost without degrading quality was analyzed.

## 11. Governance and release

- [ ] submitted version is frozen;
- [ ] evidence corresponds to the published artifact;
- [ ] decision-makers have the necessary authority and independence;
- [ ] approval conditions are verifiable;
- [ ] approval is valid;
- [ ] pipeline checks the decision before publication;
- [ ] canary or progressive rollout is defined;
- [ ] feature flags and kill switch exist when applicable;
- [ ] release communication has been prepared;
- [ ] post-release review is scheduled;
- [ ] Re-evaluation triggers are defined.

## 12. Retirement readiness

- [ ] consumers and users were identified;
- [ ] the migration or replacement plan exists;
- [ ] new invocations may be blocked;
- [ ] credentials and scopes will be withdrawn;
- [ ] knowledge and memory will have adequate destination;
- [ ] audit evidence will be retained according to policy;
- [ ] budgets, dashboards and alerts will be closed;
- [ ] documentation and catalogue will be updated;
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

One version is ready when:

- delivery measurable value;
- has known risk and applied controls;
- pode ser observada e suportada;
- has a controlled cost;
- may be reversed, suspended and withdrawn;
- it has evidence that allows to explain why it has been published.

## Further materials

- [Glossary](glossary.md)
- [Runbooks](../runbooks/onboarding-agent.md)
- [AI Risk Framework](../governance/ai-risk-framework.md)
- [Non-functional requirements](../architecture/non-functional-requirements.md)
