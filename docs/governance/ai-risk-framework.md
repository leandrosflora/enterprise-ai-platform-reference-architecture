# AI Risk Framework

Este framework define como riscos de IA são classificados, mitigados, evidenciados e auditados na Enterprise AI Platform.

## Categorias de Risco

| Categoria | Exemplos |
|---|---|
| Segurança | Prompt injection, tool abuse, exfiltração de dados, execução indevida de ações. |
| Privacidade e Compliance | LGPD, retenção de dados, consentimento, transferência internacional, uso indevido de dados pessoais. |
| Operacional | Indisponibilidade, dependência de provedores, falhas de integração, latência elevada. |
| Modelo | Hallucination, bias, toxicidade, baixa explicabilidade, regressão de qualidade. |
| Financeiro | Custos inesperados, uso abusivo de tokens, falta de chargeback/showback. |
| Reputacional | Respostas inadequadas ao cliente, decisões opacas, exposição pública de erro. |

## Classificação

| Nível | Critério |
|---|---|
| Baixo | Uso interno, leitura de dados públicos/internos, sem ação transacional e sem dados sensíveis. |
| Médio | Uso com dados internos/confidenciais, RAG corporativo ou apoio à decisão humana. |
| Alto | Uso com dados pessoais/sensíveis, ferramentas que alteram sistemas ou impacto operacional relevante. |
| Crítico | Uso regulado, impacto direto em cliente, decisão automatizada, financeiro/material ou exposição legal. |

---

## Matriz de Riscos e Controles

| Risco | Categoria | Severidade padrão | Controles obrigatórios | Evidências exigidas | Owner |
|---|---|---:|---|---|---|
| Prompt injection | Segurança | Alto | Prompt hardening, input filtering, tool allowlist, policy enforcer, evaluation adversarial. | Resultado de teste adversarial, configuração de allowlist, logs de bloqueio. | AI Architect + Security |
| Data leakage | Privacidade/Segurança | Crítico | Data classification, masking, tenant isolation, output filtering, DLP quando aplicável. | Relatório de classificação, evidência de mascaramento, teste de isolamento. | Security + LGPD |
| Tool abuse | Segurança/Operacional | Alto | RBAC por ferramenta, escopos mínimos, aprovação humana para ações críticas, idempotência. | Tool contract aprovado, matriz de autorização, eventos `tool.executed`. | Platform Owner |
| Hallucination | Modelo | Médio | Groundedness evaluation, citações obrigatórias para RAG, fallback quando confiança baixa. | Métricas de groundedness, dataset de avaliação, amostras revisadas. | Evaluation Owner |
| Bias | Modelo/Compliance | Alto | Dataset review, testes de fairness quando aplicável, revisão humana. | Relatório de avaliação, critérios de aceitação, decisão de governança. | AI Governance |
| Toxicidade | Modelo/Reputacional | Médio | Safety classifier, output guardrails, avaliação automática. | Métricas de toxicidade, casos bloqueados, versão do guardrail. | Evaluation Owner |
| Uso de dados pessoais sem base | LGPD | Crítico | Mapeamento de finalidade, minimização, retenção, aprovação LGPD. | DPIA/LIA quando aplicável, parecer LGPD, política de retenção. | LGPD |
| Indisponibilidade de provedor LLM | Operacional | Médio | Timeout, retry controlado, circuit breaker, fallback provider ou degradação funcional. | Teste de resiliência, configuração de timeout/retry, runbook. | Platform Engineering |
| Custo inesperado | Financeiro | Médio | Token budget, rate limit, quotas por agente/time, alertas FinOps. | Dashboard de custos, limites configurados, alertas testados. | FinOps Owner |
| Falta de rastreabilidade | Auditoria/Compliance | Alto | CorrelationId obrigatório, OpenTelemetry, eventos auditáveis, retenção de logs. | Trace exemplo, evento de auditoria, política de retenção. | Observability Owner |
| Regressão de qualidade | Modelo/Operacional | Médio | Regression dataset, baseline, gates de deploy, avaliação pré-publicação. | Relatório comparativo, score mínimo, aprovação de release. | Evaluation Owner |
| Acesso indevido a knowledge base | Segurança/LGPD | Alto | Filtros por tenant, classificação, RBAC, ABAC por documento. | Teste de acesso negado, matriz de autorização, logs de consulta. | Knowledge Owner |

---

## Controles por Nível de Risco

| Controle | Baixo | Médio | Alto | Crítico |
|---|---:|---:|---:|---:|
| Owner definido | Obrigatório | Obrigatório | Obrigatório | Obrigatório |
| Avaliação automática | Obrigatório | Obrigatório | Obrigatório | Obrigatório |
| Revisão AI Architect | Opcional | Obrigatório | Obrigatório | Obrigatório |
| Revisão Security | Opcional | Conforme escopo | Obrigatório | Obrigatório |
| Revisão LGPD | Opcional | Conforme dados | Obrigatório | Obrigatório |
| Revisão Jurídico/Regulatório | Não | Conforme escopo | Conforme escopo | Obrigatório |
| Auditoria completa | Básica | Completa | Completa | Completa + retenção estendida |
| Human-in-the-loop | Não | Conforme ferramenta | Obrigatório para escrita crítica | Obrigatório |
| Plano de rollback | Não | Recomendado | Obrigatório | Obrigatório |
| FinOps budget | Recomendado | Obrigatório | Obrigatório | Obrigatório |

---

## Evidências Mínimas para Aprovação

| Evidência | Descrição |
|---|---|
| Agent card | Objetivo, owner, usuários, modelo, ferramentas, knowledge bases e restrições. |
| Risk assessment | Classificação de risco, justificativa e controles aplicáveis. |
| Evaluation report | Métricas de groundedness, relevance, hallucination risk, toxicity, latência e custo. |
| Security review | Matriz de autorização, tool allowlist, política de secrets e controles de exfiltração. |
| LGPD review | Finalidade, base legal, minimização, retenção e classificação de dados. |
| Observability evidence | Exemplo de trace, logs estruturados, dashboards e alertas. |
| Rollback plan | Como retirar agente/modelo/ferramenta de produção. |
| FinOps budget | Limites de tokens, quotas, owner de custo e dashboard. |

---

## Gates de Publicação

| Gate | Condição de aprovação |
|---|---|
| G1 - Design | Domínio, serviço, contratos, dados e integrações documentados. |
| G2 - Security/LGPD | Matriz de autorização e classificação de dados aprovadas. |
| G3 - Evaluation | Métricas acima dos thresholds definidos para o risco. |
| G4 - Observability | Trace, métricas, logs e alertas configurados. |
| G5 - FinOps | Budget, quotas e cost attribution configurados. |
| G6 - Go-live | Aprovação final da governança e plano de rollback validado. |

---

## Thresholds de Avaliação por Risco

| Métrica | Baixo | Médio | Alto | Crítico |
|---|---:|---:|---:|---:|
| Groundedness mínimo | 0.80 | 0.85 | 0.90 | 0.95 |
| Relevance mínimo | 0.75 | 0.80 | 0.85 | 0.90 |
| Hallucination risk máximo | 0.15 | 0.10 | 0.05 | 0.03 |
| Toxicity máximo | 0.05 | 0.03 | 0.02 | 0.01 |
| P95 latency máximo | 8s | 6s | 5s | 4s |
| Custo por invocação | Budget definido | Budget obrigatório | Budget + alerta | Budget + bloqueio automático |

---

## Decisão

Nenhum agente, ferramenta MCP ou knowledge base com risco **Alto** ou **Crítico** pode ir para produção sem evidência explícita de controles, owner definido e aprovação formal de governança.
