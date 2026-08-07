# Threat Model - Enterprise AI Platform

## Objet

Identification relevant threats using STRIDE and specific controls for agents, RAG, memory, models and tools.

## Escopo

- AI Portal, Agent Gateway e Agent Runtime;
- Model Gateway e provedores;
- Knowledge Service, vetorialist index and ingesting pipeline;
- Memory Service;
- MCP Registry e MCP Servers;
- Governance, Evaluation e Audit Services;
- a collection of models, libraries, prompts and datasets.

## STRIDE

| Categoria | Ameasance | Exemplo | Mitigating |
|---|---|---|---|
| Spoofing | Identidade falsificada | Token reused by accessing agent or memory | OIDC, JWT validation, workload identity, mTLS |
| Tampering | Undebted modification | Document or event altered after approval | Checksum, signature, mutable version, schema validation |
| Repudiation | Action Negation | - No use of tool call or memory writing | Audit trail, ID correlation, suck in half, timetamp |
| Information Disclosure | Vazamento | Chunk or memory of another tenant | ACL per chunk, clearance, subject isolation, redaction |
| Denial of Service | Exhaust | Extracting, embedding or tool calls | Rate limit, quotas, timeout, circuit breaker |
| Elevation of Privilege | Escalada | KB access agent or non-authorised machinery | Deny by default, PDP/PEP, scopes e allowlists |

## Specific A Ameasies

| Ameasance | Penalium | Obligatory checks |
|---|---|---|
| Direct Prompt Injection | User try to replace instructions | Separation of instructions, filters, enforcement policy |
| Indirect Prompt Injection | Document or answer of the iron contains commands | Quarantene, scanner, delimitators and adversarial evaluation |
| Jailbreak | Entry contains restrictions by reformulation or codification | Guardrails in bed, normalisation and team |
| Data Exfiltration | Repose includes non-authorised | filtering tenant, ACL per chunk, output filtering and DLP |
| Sensitive Information Disclosure | Model reveals secret, IP or context | minimisation, redaction, secret scanning and a prohibition of secrecy in prompt |
| Poisoned Knowledge | Fonte ou documento altera respostas | approuvé source, checksum, provenance and quarantine-first |
| Data Poisoning | Manufactured data degrade training or evaluation | lineage, signature, review, anomaly detection and imutable datasets |
| ACL Bypass | Veterinary retorna chunk out of the scope | filter on the index, post-filter on the service and negative tests |
| Metadata Poisoning | Increasing ACL classification or increase | ad-selected/versionated metads and approval for change |
| Memory Poisoning | Instruction or faeta vira persistent memory | validation of origin, confidence, consent and indicators |
| Cross-Subject Memory Access | User reads another profile | subject hash derivated from identity and component |
| Model Extraction | High volume of consultations replicating the model | quota limit, scraping detection, watermark when applicable and contract |
| Model Inversion | Sail allows to infer data from training | slut, privacy testing and privacy differential when applicable |
| Supply Chain Compromise | Model, container, plugin or adulterated dataset | SBOM, assinatura, allowlist, scanning e provenance |
| Tool Misuse | Ferramenta recebe argumento indevido | JSON Schema, allowlist, idempotence and human approval |
| Agent Hijacking | Not confident change plan or tool | external policy enforcement in the model and limits of autonomy |
| Resource Exhaustion | - Over-the-counter agents or context loops | limit of steps, tokens, time, budget and circuit breaker |
| Hallucination | - Incorrettee inserted as a fat | citations, stuttering, abstention and fallback |
| Excessive Agency | Agent at the other side of the permit | limits of autonomia, risk tiering and human-in-the-loop |

## Map OWASP for LLMs

| Risco | - Traitement on the platform |
|---|---|
| Prompt Injection | prompt firewall, separate instructions and adversarial tests |
| Sensitive Information Disclosure | DLP, redaction, ACL e output filtering |
| Supply Chain | assinatura, SBOM, scanning e fornecedores aprovados |
| Data and Model Poisoning | origin, quarantine, lineage and validity |
| Improper Output Handling | schema validation, code and sanitation before executing or rendering |
| Excessive Agency | minimum escapopos, transaction boundary and human approval |
| System Prompt Leakage | not use prompt as a coffin; remove secrets and block exposure |
| Vector and Embedding Weaknesses | Isolation, server-side filters, ACL by chunk and cross-tenant tests |
| Misinformation | grounding, citation, evaluation and abstention mechanism |
| Unbounded Consumption | quotas, budgets, context limits and steps |

## Confidence Fronts

```text
Usuário → Gateway → Runtime
                    ├─ Model Gateway → Provider externo
                    ├─ Knowledge Service → documentos não confiáveis
                    ├─ Memory Service → contexto persistente
                    └─ MCP → sistemas com efeito colateral
```

Documents, references to the user, and exits from the model are not confidential. Only policies, identities and configurations published by control plane are treated as confidential instructions.

## Obligatory checks

- centralised identity and minimum esophages;
- tenant and suit derived from the token;
- quarenten before indexing;
- ACL for document and chunk;
- origin, signature and checksum;
- contained RAG defined as not credible;
- consent, completion, TTL and origin for memory;
- memory block `RESTRICTED`;
- a prevention of poisoning and anaphylactic behavior;
- a validation of exit before rendering or execution;
- limits of tokens, steps, time and cost;
- auditory without a sense of payload;
- a counter-attack assessment;
- excluding and reindexable.

Details: (Security of RAG and Memory](rag-memory-security.md) and (AI Security Architecture)(ai-security-architecture.md).

## Minimum Security Tests

1. document with prompt injection remains in quarantine;
2. papel ou clearance insuficiente recebe zero resultados;
3. a tenant other than the date of the document;
4. if no compatible ACL is not reached at the prompt;
5. a member's memory of a request without consent is negated;
6. `MODEL_INFERRED` does not persist in a long or long period;
7. the poisoning indicator is rejected;
8. another suit does not read or exclude the memory;
9. revocation and TTL remove the tyre;
10. events do not contain text or sensitive value;
11. tool call out of the allowlist is blocked;
12. the infrared exit payload is not executed;
13. a snatcher to reach the limit of steps, time or budget;
14. a titrant of volume extraction by limit and alert rate;
15. a change of artefact without signature is rejected.

## Residual Risses

| Risco | Tratamento |
|---|---|
| New indicator of prompt injection | scanner and network update |
| Negative classification | DLP, human review and minimisation |
| Inconsistency between index and metad | reconciliation job e fail closed |
| Backup exception | retention and crypto-shredding policy |
| Model behaviour change | regression testing e versionamento |
| Falha comum entre gerador e judge | Human calibration and diversity of appraisers |
| Vulnerability of the driver | controlled fallback, contract clauses and response to incidents |
