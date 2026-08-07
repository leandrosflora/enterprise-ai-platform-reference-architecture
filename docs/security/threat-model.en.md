# Threat Model - Enterprise AI Platform

## Objective

Identify relevant threats using STRIDE and specific controls for agents, RAG, memory, models and tools.

## scope

- AI Portal, Agent Gateway and Agent Runtime;
- Model Gateway and providers;
- Knowledge Service, vector indexes and pipeline intake;
- Memory Service;
- MCP Registry and MCP Servers;
- Governance, Evaluation and Audit Services;
- supply chain of models, libraries, prompts and datasets.

## STRIDE

| Category | Threaten | Example | Mitigation |
|---|---|---|---|
| Spoofing | Falsified identity | Reused Token by accessing agent or memory | ICD, validation JWT, workload identity, mTLS |
| Tampering | Inappropriate modification | Document or event amended after approval | Checksum, signature, unchanged version, schema validation |
| Repudiation | Refusal of action | User denies tool call or writing memory | Audit trail, correlation ID, sujeito em hash, timestamp |
| Information Disclosure | Leakage | Chunk or memory of another tenant | ACL by chunk, clearance, subject isolation, redaction |
| Department of Service | Exhaustion | Retrieval explosion, embeddings or tool calls | Rate limit, quotas, timeout, circuit breaker |
| Elevation of Privilege | Scale | Agent accesses KB or unauthorised tool | Deny by default, PDP/PEP, scopes and allowlists |

## AI-specific threats

| Threaten | Scenario | Compulsory controls |
|---|---|---|
| Direct Prompt Injection | User tries to replace instructions | Separation of instructions, filters, policy enforcement |
| Indirect Prompt Injection | Document or tool response contains commands | Quarantine, scanner, boundaries and adverse evaluation |
| Jailbreak | Entry overcomes reformulation or coding restrictions | layered guardrails, standardisation and red-team |
| Date Exfiltration | Response includes unauthorised data | Tenant filter, ACL by chunk, output filtering and DLP |
| Sensitive Information Disclosure | Model reveals secrecy, PII or hidden context | minimisation, redaction, secret scanning and prohibition of prompt secrets |
| Poisoned Knowledge | Source or document changes responses | approved source, checksum, provenance and quarantine-first |
| Data Poisoning | Handled data degrades training or evaluation | lineage, signature, review, anomaly detection and unchanged dates |
| ACL Bypass | Vector search returns out of scope chunk | index filter, post-filter in the service and negative tests |
| Metadata Poisoning | Attacker reduces or expands ACL | signed/versioned metadata and approval for change |
| Memory Poisoning | Instruction or false fact becomes persistent memory | validation of origin, trust, consent and indicators |
| Cross-Subject Memory Access | User reads the profile of another | subject hash identity derived and composite key |
| Model Extraction | High volume of consultations replicates the model's behavior | rate limit, scraping detection, watermark when applicable and contract |
| Model Inversion | Outcomes allow inferring training data | output minimization, privacy testing and differential privacy when applicable |
| Supply Chain Compromise | Model, container, plugin or adulterated dates | SBOM, signature, allowlist, scanning and provenance |
| Tool Mixuse | Tool receives incorrect argument | JSON Schema, allowlist, idempotence and human approval |
| Agent Hijacking | Unreliable content changes plan or tool | policy enforcement external to the model and limits of autonomy |
| Resource Exhaustion | Excessive agent or context loops increase cost | limit of steps, tokens, time, budget and circuit breaker |
| Hallucination | response incorreta apresentada as fato | citations, groundedness, abstention and fallback |
| Excessive Agency | Agent shall act beyond what is permitted | limits of autonomy, risk tiering and human-in-the-loop |

## OWASP mapping for MLLs

| Risk | Platform treatment |
|---|---|
| Prompt Injection | prompt firewall, separation of instructions and adverse tests |
| Sensitive Information Disclosure | DLP, redaction, ACL and output filtering |
| Supply Chain | Signature, SBOM, scanning and approved suppliers |
| Date and Model Poisoning | provenance, quarantine, lineage and validation |
| Improper Output Handling | schema validation, encoding and sanitization before executing or rendering |
| Excessive Agency | minimum scopes, transaction boundary and human approval |
| System Prompt Leakage | Do not use prompt as a safe, remove secrets and block exposure |
| Vector and Embedding Weaknesses | isolation, server-side filters, chunk ACL and cross-tenant tests |
| Misinformation | grounding, citation, evaluation and abstention mechanism |
| Unbounded Consumption | quotas, budgets, context limits and steps |

## Confidence Borders

```text
Usuário → Gateway → Runtime
                    ├─ Model Gateway → Provider externo
                    ├─ Knowledge Service → documentos não confiáveis
                    ├─ Memory Service → contexto persistente
                    └─ MCP → sistemas com efeito colateral
```

Documents, tool responses, user content and model outputs are non-reliable inputs, and only policies, identities and configurations published by the control plane are treated as reliable instructions.

## Obligatory controls

- centralized identity and minimum scopes;
- tenant and subject derived from token;
- quarantine before indexing;
- ACL by document and chunk;
- provenance, signature and checksum;
- RAG content delimited as non-reliable;
- Consent, purpose, TTL and origin for memory;
- memory block `RESTRICTED`;
- detection of poisoning and anomalous behavior;
- output validation before rendering or execution;
- token limits, steps, time and cost;
- payload-free audit;
- continuous adverse evaluation;
- exclusion and verifiable reindexation.

Details: [RAG Security and Memory](rag-memory-security.md) and [AI Security Architecture](ai-security-architecture.md).

## Minimum Safety Tests

1. document with prompt injection remains in quarantine;
2. insufficient paper or clearance receives zero results;
3. tenant differently does not obtain any indication of the existence of the document;
4. chunk without compatible ACL does not reach the prompt;
5. profile memory without consent is denied;
6. `MODEL_INFERRED` does not persist in profile or long-term;
7. poisoning indicator is rejected;
8. another subject does not read or exclude memory;
9. withdrawal and TTL remove the data;
10. events do not contain text or sensitive value;
11. tool call outside the allowlist is blocked;
12. payload of invalid output is not executed;
13. agent closes when it reaches the limit of steps, time or budget;
14. attempt of volume extraction triggers rate limit and alerts;
15. artifact change without signature is rejected.

## Residual Risks

| Risk | Tratamento |
|---|---|
| New prompt injection indicator | update of scanner and continuous red-team |
| False negative classification | PLD, human review and minimisation |
| Inconsistency between index and metadata | reconciliation job and fail closed |
| Exclusion in backup | retention policy and crypto-shredding |
| Change in behavior of the model | regression testing and versioning |
| Common failure between generator and judge | human calibration and diversity of evaluators |
| Provider's vulnerability | Controlled fallback, contractual clauses and incident response |
