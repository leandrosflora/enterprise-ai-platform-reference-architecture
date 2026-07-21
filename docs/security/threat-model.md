# Threat Model - Enterprise AI Platform

## Objetivo

Identificar ameaças relevantes usando STRIDE e controles específicos para agentes, RAG, memória, modelos e ferramentas.

## Escopo

- AI Portal, Agent Gateway e Agent Runtime;
- Model Gateway e provedores;
- Knowledge Service, índices vetoriais e pipeline de ingestão;
- Memory Service;
- MCP Registry e MCP Servers;
- Governance, Evaluation e Audit Services;
- cadeia de suprimentos de modelos, bibliotecas, prompts e datasets.

## STRIDE

| Categoria | Ameaça | Exemplo | Mitigação |
|---|---|---|---|
| Spoofing | Identidade falsificada | Token reutilizado acessando agente ou memória | OIDC, validação JWT, workload identity, mTLS |
| Tampering | Alteração indevida | Documento ou evento alterado após aprovação | Checksum, assinatura, versão imutável, schema validation |
| Repudiation | Negação de ação | Usuário nega tool call ou escrita de memória | Audit trail, correlation ID, sujeito em hash, timestamp |
| Information Disclosure | Vazamento | Chunk ou memória de outro tenant | ACL por chunk, clearance, subject isolation, redaction |
| Denial of Service | Exaustão | Explosão de retrieval, embeddings ou tool calls | Rate limit, quotas, timeout, circuit breaker |
| Elevation of Privilege | Escalada | Agente acessa KB ou ferramenta não autorizada | Deny by default, PDP/PEP, scopes e allowlists |

## Ameaças Específicas de IA

| Ameaça | Cenário | Controles obrigatórios |
|---|---|---|
| Direct Prompt Injection | Usuário tenta substituir instruções | Separação de instruções, filtros, policy enforcement |
| Indirect Prompt Injection | Documento ou resposta de ferramenta contém comandos | Quarentena, scanner, delimitadores e avaliação adversarial |
| Jailbreak | Entrada contorna restrições por reformulação ou codificação | guardrails em camadas, normalização e red-team |
| Data Exfiltration | Resposta inclui dado não autorizado | tenant filter, ACL por chunk, output filtering e DLP |
| Sensitive Information Disclosure | Modelo revela segredo, PII ou contexto oculto | minimização, redaction, secret scanning e proibição de segredos em prompt |
| Poisoned Knowledge | Fonte ou documento altera respostas | fonte aprovada, checksum, proveniência e quarantine-first |
| Data Poisoning | Dados manipulados degradam treino ou avaliação | lineage, assinatura, revisão, detecção de anomalia e datasets imutáveis |
| ACL Bypass | Busca vetorial retorna chunk fora do escopo | filtro no índice, post-filter no serviço e testes negativos |
| Metadata Poisoning | Atacante reduz classificação ou amplia ACL | metadados assinados/versionados e aprovação para mudança |
| Memory Poisoning | Instrução ou fato falso vira memória persistente | validação de origem, confiança, consentimento e indicadores |
| Cross-Subject Memory Access | Usuário lê perfil de outro | subject hash derivado da identidade e chave composta |
| Model Extraction | Alto volume de consultas replica comportamento do modelo | rate limit, detecção de scraping, watermark quando aplicável e contrato |
| Model Inversion | Saídas permitem inferir dados de treinamento | minimização de saída, privacy testing e differential privacy quando aplicável |
| Supply Chain Compromise | Modelo, container, plugin ou dataset adulterado | SBOM, assinatura, allowlist, scanning e provenance |
| Tool Misuse | Ferramenta recebe argumento indevido | JSON Schema, allowlist, idempotência e human approval |
| Agent Hijacking | Conteúdo não confiável muda plano ou ferramenta | policy enforcement externo ao modelo e limites de autonomia |
| Resource Exhaustion | Loops de agente ou contexto excessivo elevam custo | limite de passos, tokens, tempo, budget e circuit breaker |
| Hallucination | Resposta incorreta apresentada como fato | citações, groundedness, abstention e fallback |
| Excessive Agency | Agente atua além do permitido | limites de autonomia, risk tiering e human-in-the-loop |

## Mapeamento OWASP para LLMs

| Risco | Tratamento na plataforma |
|---|---|
| Prompt Injection | prompt firewall, separação de instruções e testes adversariais |
| Sensitive Information Disclosure | DLP, redaction, ACL e output filtering |
| Supply Chain | assinatura, SBOM, scanning e fornecedores aprovados |
| Data and Model Poisoning | proveniência, quarentena, lineage e validação |
| Improper Output Handling | schema validation, encoding e sanitização antes de executar ou renderizar |
| Excessive Agency | escopos mínimos, transaction boundary e aprovação humana |
| System Prompt Leakage | não usar prompt como cofre; remover segredos e bloquear exposição |
| Vector and Embedding Weaknesses | isolamento, filtros server-side, ACL por chunk e testes cross-tenant |
| Misinformation | grounding, citação, avaliação e mecanismo de abstention |
| Unbounded Consumption | quotas, budgets, limites de contexto e passos |

## Fronteiras de Confiança

```text
Usuário → Gateway → Runtime
                    ├─ Model Gateway → Provider externo
                    ├─ Knowledge Service → documentos não confiáveis
                    ├─ Memory Service → contexto persistente
                    └─ MCP → sistemas com efeito colateral
```

Documentos, respostas de ferramentas, conteúdo do usuário e saídas do modelo são entradas não confiáveis. Somente políticas, identidades e configurações publicadas pelo control plane são tratadas como instruções confiáveis.

## Controles Obrigatórios

- identidade centralizada e escopos mínimos;
- tenant e sujeito derivados do token;
- quarentena antes de indexação;
- ACL por documento e chunk;
- proveniência, assinatura e checksum;
- conteúdo RAG delimitado como não confiável;
- consentimento, finalidade, TTL e origem para memória;
- bloqueio de memória `RESTRICTED`;
- detecção de poisoning e comportamento anômalo;
- validação de saída antes de renderização ou execução;
- limites de tokens, passos, tempo e custo;
- auditoria sem payload sensível;
- avaliação adversarial contínua;
- exclusão e reindexação verificáveis.

Detalhamento: [Segurança de RAG e Memória](rag-memory-security.md) e [AI Security Architecture](ai-security-architecture.md).

## Testes de Segurança Mínimos

1. documento com prompt injection permanece em quarentena;
2. papel ou clearance insuficiente recebe zero resultados;
3. tenant diferente não obtém indicação da existência do documento;
4. chunk sem ACL compatível não chega ao prompt;
5. memória de perfil sem consentimento é negada;
6. `MODEL_INFERRED` não persiste em perfil ou longo prazo;
7. indicador de poisoning é rejeitado;
8. outro sujeito não lê nem exclui a memória;
9. revogação e TTL removem o dado;
10. eventos não contêm texto ou valor sensível;
11. tool call fora da allowlist é bloqueada;
12. payload de saída inválido não é executado;
13. agente encerra ao atingir limite de passos, tempo ou budget;
14. tentativa de extração por volume dispara rate limit e alerta;
15. mudança de artefato sem assinatura é rejeitada.

## Riscos Residuais

| Risco | Tratamento |
|---|---|
| Indicador novo de prompt injection | atualização de scanner e red-team contínuo |
| Falso negativo de classificação | DLP, revisão humana e minimização |
| Inconsistência entre índice e metadados | reconciliation job e fail closed |
| Exclusão em backup | política de retenção e crypto-shredding |
| Mudança de comportamento do modelo | regression testing e versionamento |
| Falha comum entre gerador e judge | calibração humana e diversidade de avaliadores |
| Vulnerabilidade do provedor | fallback controlado, cláusulas contratuais e resposta a incidentes |
