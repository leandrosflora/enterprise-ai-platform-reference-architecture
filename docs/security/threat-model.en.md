# Threat Model - Enterprise AI Platform

## Objective

Identify relevant threats using STRIDE and controls specific to agents, RAG, memory, models and tools.

## Escopo

- AI Portal, Agent Gatewayand Agent Runtime;
- Model Gateway and suppliers;
- Knowledge Service, vector indices and intake pipeline;
- Memory Service;
- MCP Registryand MCP Servers;
- Governance, Evaluation and Audit Services;
- supply chain of models, libraries, prompts and datasets.

## STRIDE

| Categoria | Threat | Example | Mixing |
|---|---|---|---|
| Spoofing | Identidade falsificada | Reused token accessing agent or memory | OIDC, validation JWT, workload identity, mTLS |
| Tampering | Unnecessary change | Document or event amended after approval | This is the total amount of aid granted in accordance with Article 107 (1) of the Treaty. |
| Repudiation | Denial of action | User denies tool call or memory writing | This is the first time that the data has been collected in the database. |
| Information Disclosure | Vazamento | Chunk or memory of another tenant | ACL by chunk, clearance, subject isolation, redaction |
| Denial of Service | Exhaustion | Explosion of retrieval, embeddings or tool calls | Rate limit, quotas, timeout, circuit breaker |
| Elevation of Privilege | Escalada | Agent access KB or unauthorized tool | Deny by default, PDP/PEP, scopes and allowlists |

## Specific threats to AI

| Threat | Scenario | Compulsory checks |
|---|---|---|
| Direct Prompt Injection | User attempts to replace instructions | Separation of instructions, filters, policy enforcement |
| Indirect Prompt Injection | Document or tool response contains commands | Quarantine, scanner, delimiters and adverse assessment |
| Jailbreak | Entry circumvents restrictions by reformulation or coding | Layered guardrails, standardisation and red-team |
| Data Exfiltration | Answer includes unauthorised data | the tenant filter, ACL per chunk, output filtering and DLP |
| Sensitive Information Disclosure | Model reveals secret, PII or hidden context | Minimization, redaction, secret scanning and prohibition of secrets promptly |
| Poisoned Knowledge | Source or document changes answers | approved source, checksum, provenance and quarantine-first |
| Data Poisoning | Manipulated data degrades training or evaluation | The following information shall be provided in accordance with the provisions of this Regulation: |
| ACL Bypass | Vector search returns chunk out of scope | filter in the index, post-filter in the service and negative tests |
| Metadata Poisoning | Striker reduces classification or extends ACL | Signed/versioned metadata and approval for change |
| Memory Poisoning | False instruction or fact turns into persistent memory | validation of origin, confidence, consent and indicators |
| Cross-Subject Memory Access | User reads another person's profile | Subject hash derived from identity and composite key |
| Model Extraction | High volume of queries replicates model behavior | rate limit, scraping detection, watermark where applicable and contract |
| Model Inversion | Outputs allow to infer training data | Minimization of output, privacy testing and differential privacy where applicable |
| Supply Chain Compromise | Model, container, plugin or dataset tampered with | SBOM, signature, allowlist, scanning and provenance |
| Tool Misuse | Ferramenta recebe argumento indevido | JSON Scheme, allowlist, idempotence and human approval |
| Agent Hijacking | Unreliable content changes plan or tool | policy enforcement outside the model and autonomy limits |
| Resource Exhaustion | Agent loops or excessive context raise cost | Step limit, tokens, time, budget and circuit breaker |
| Hallucination | Misrepresented as fact | Submissions, groundedness, abstention and fallback |
| Excessive Agency | Agent acting beyond the permissible | The Commission will also examine the possible implications for the development of the new technologies.human-in-the-loop |

## Mapeamento OWASPto LLMs

| Risco | Treatment on the platform |
|---|---|
| Prompt Injection | prompt firewall, instruction separation and adverse testing |
| Sensitive Information Disclosure | DLP, redaction, ACL and output filtering |
| Supply Chain | Subscription, SBOM, scanning and approved suppliers |
| Data and Model Poisoning | origin, quarantine, lineage and validation |
| Improper Output Handling | schema validation, encoding and sanitization before running or rendering |
| Excessive Agency | Minimum scope, transaction boundary and human approval |
| System Prompt Leakage | Do not use prompt as a safe; remove secrets and block exposure |
| Vector and Embedding Weaknesses | Isolation, server-side filters, ACL by chunk and cross-tenant testing |
| Misinformation | grounding, submission, evaluation and abstention mechanism |
| Unbounded Consumption | The Commission shall adopt delegated acts in accordance with the opinion of the Standing Committee on Planning and Budgetary Control. |

## Confidence boundaries

```text
Usuário → Gateway → Runtime
                    ├─ Model Gateway → Provider externo
                    ├─ Knowledge Service → documentos não confiáveis
                    ├─ Memory Service → contexto persistente
                    └─ MCP → sistemas com efeito colateral
```

Documents, tool replies, user content and model outputs are unreliable inputs.Only policies, identities and settings published by control plane are treated as reliable instructions.

## Compulsory checks

- centralized identity and minimum scope;
- the token tenant and derivative subject;
- quarantine prior to indexation;
- ACL per document and chunk;
- origin, signature and checksum;
- content of RAG which is defined as unreliable;
- consent, purpose, TTL and origin for memory;
- the memory block `RESTRICTED`;
- detection of poisoning and abnormal behaviour;
- output validation before rendering or execution;
- Token limits, steps, time and cost;
- audit without a sensitive payload;
- continuous adverse assessment;
- verifiable deletion and re-indexation.

Detalhamento: [Security of RAGand Memory](rag-memory-security.md)and [AI Security Architecture](ai-security-architecture.md).

## Minimum safety tests

1. document with prompt injection remains in quarantine;
2. insufficient paper or clearance yields zero results;
3. a different tenant does not obtain an indication of the existence of the document;
4. chunk without a compatible ACL does not reach the prompt;
5. profile memory without consent is denied;
6. `MODEL_INFERRED` does not persist in profile or long term;
7. the poisoning indicator is rejected;
8. another subject does not read or delete memory;
9. revocation and TTL removes the data;
10. events do not contain text or any significant value;
11. tool call outside the allowlist is blocked;
12. the invalid output payload is not executed;
13. the agent closes upon reaching the step, time or budget limit;
14. the volume extraction attempt triggers the rate limit and alert;
15. change of artifact without signature is rejected.

## Residual risks

| Risco | Tratamento |
|---|---|
| New indicator of prompt injection | continuous update of scanner and network team |
| Negative misclassification | DLP, human review and minimisation |
| Inconsistency between index and metadata | reconciliation job and fail closed |
| Exclusion in backup | Retention and crypto-shredding policy |
| Change in model behaviour | regression testing and versioning |
| Common failure between generator and judge | Human calibration and diversity of evaluators |
| Vulnerability of the provider | Controlled fallback, contractual clauses and incident response |
