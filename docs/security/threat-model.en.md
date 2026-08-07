# Threat Model - Enterprise AI Platform

## Objective

Identify relevant threats using STRIDE and specific controls for agents, RAG, memory, models and tools.

## Escopo

- AI Portal, Agent Gateway e Agent Runtime;
- Model Gateway e provedores;
- Knowledge Service, vector indexes and pipeline intake;
- Memory Service;
- MCP Registry e MCP Servers;
- Governance, Evaluation e Audit Services;
- supply chain of models, libraries, prompts and datesets.

## STRIDE

| Categoria | Threaten | Exemplo | Mitigation |
|---|---|---|---|
| Spoofing | Falsified identity | Reused Token by accessing agent or memory | ICD, validation JWT, workload identity, mTLS |
| Tampering | Inappropriate modification | Document or event amended after approval | Checksum, signature, unchanged version, schema validation |
| Repudiation | Refusal of action | User denies tool call or writing memory | Audit trail, correlation ID, sujeito em hash, timestamp |
| Information Disclosure | Vazamento | Chunk or memory of another tenant | ACL por chunk, clearance, subject isolation, redaction |
| Denial of Service | Exhaustion | Retrieval explosion, embeddings or tool calls | Rate limit, quotas, timeout, circuit breaker |
| Elevation of Privilege | Escalada | Agent accesses KB or unauthorised tool | Deny by default, PDP/PEP, scopes e allowlists |

## AI-specific threats

| Threaten | Scenario | Compulsory controls |
|---|---|---|
| Direct Prompt Injection | User tries to replace instructions | Separation of instructions, filters, policy enforcement |
| Indirect Prompt Injection | Document or tool response contains commands | Quarantine, scanner, boundaries and adverse evaluation |
| Jailbreak | Entry overcomes reformulation or coding restrictions | layered guardrails, standardisation and red-team |
| Data Exfiltration | Response includes unauthorised data | tenant filter, ACL por chunk, output filtering e DLP |
| Sensitive Information Disclosure | Model reveals secrecy, PII or hidden context | minimisation, redaction, secret scanning and prohibition of prompt secrets |
| Poisoned Knowledge | Source or document changes responses | approved source, checksum, provenance and quarantine-first |
| Data Poisoning | Handled data degrades training or evaluation | lineage, signature, review, anomaly detection and unchanged dates |
| ACL Bypass | Busca vetorial retorna chunk fora do escopo | index filter, post-filter in the service and negative tests |
| Metadata Poisoning | Attacker reduces or expands ACL | signed/versioned metadata and approval for change |
| Memory Poisoning | Instruction or false fact becomes persistent memory | validation of origin, trust, consent and indicators |
| Cross-Subject Memory Access | User reads the profile of another | subject hash identity derived and composite key |
| Model Extraction | High volume of consultations replicates the model's behavior | rate limit, scraping detection, watermark when applicable and contract |
| Model Inversion | Outcomes allow inferring training data | output minimization, privacy testing and differential privacy when applicable |
| Supply Chain Compromise | Model, container, plugin or adulterated dates | SBOM, assinatura, allowlist, scanning e provenance |
| Tool Misuse | Tool receives incorrect argument | JSON Schema, allowlist, idempotence and human approval |
| Agent Hijacking | Unreliable content changes plan or tool | policy enforcement external to the model and limits of autonomy |
| Resource Exhaustion | Excessive agent or context loops increase cost | limite de passos, tokens, tempo, budget e circuit breaker |
| Hallucination | Resposta incorreta apresentada como fato | citations, groundedness, abstention and fallback |
| Excessive Agency | Agent shall act beyond what is permitted | limites de autonomia, risk tiering e human-in-the-loop |

## Mapeamento OWASP para LLMs

| Risk | Tratamento na plataforma |
|---|---|
| Prompt Injection | prompt firewall, separation of instructions and adverse tests |
| Sensitive Information Disclosure | DLP, redaction, ACL e output filtering |
| Supply Chain | assinatura, SBOM, scanning e fornecedores aprovados |
| Data and Model Poisoning | provenance, quarantine, lineage and validation |
| Improper Output Handling | schema validation, encoding and sanitization before executing or rendering |
| Excessive Agency | minimum scopes, transaction boundary and human approval |
| System Prompt Leakage | Do not use prompt as a safe, remove secrets and block exposure |
| Vector and Embedding Weaknesses | isolamento, filtros server-side, ACL por chunk e testes cross-tenant |
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
- tenant e sujeito derivados do token;
- quarantine before indexing;
- ACL por documento e chunk;
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

Detalhamento: [RAG Security and Memory](rag-memory-security.md) e [AI Security Architecture](ai-security-architecture.md).

## Minimum Safety Tests

1. documento com prompt injection permanece em quarentena;
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
15. article change without signature is rejected.

## Residual Risks

| Risk | Tratamento |
|---|---|
| Indicador novo de prompt injection | update of scanner and continuous red-team |
| False negative classification | PLD, human review and minimisation |
| Inconsistency between index and metadata | reconciliation job e fail closed |
| Exclusion in backup | retention policy and crypto-shredding |
| Change in behavior of the model | regression testing e versionamento |
| Falha comum entre gerador e judge | human calibration and diversity of evaluators |
| Vulnerabilidade do provedor | Controlled fallback, contractual clauses and incident response |
