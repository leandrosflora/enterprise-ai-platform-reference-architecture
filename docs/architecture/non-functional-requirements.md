# Requisitos Não Funcionais

## Objetivo

Definir os principais requisitos não funcionais da Enterprise AI Platform para orientar decisões de arquitetura, operação e governança.

---

## Disponibilidade e Continuidade

| Requisito | Meta de Referência |
|---|---|
| Disponibilidade da plataforma | 99,9% para workloads internos críticos |
| RTO | Até 2 horas para serviços críticos |
| RPO | Até 15 minutos para dados transacionais |
| Estratégia de contingência | Multi-AZ, backups e fallback de provedores |

---

## Performance

| Requisito | Meta de Referência |
|---|---|
| Latência P95 - Agent Gateway | Até 300 ms sem chamada de modelo |
| Latência P95 - Agent Invocation | Até 10 s para fluxos síncronos simples |
| Latência P95 - Retrieval | Até 1,5 s |
| Timeout de tool call | Configurável por ferramenta, padrão 30 s |

---

## Escalabilidade

| Requisito | Diretriz |
|---|---|
| Agent Runtime | Escala horizontal em Kubernetes |
| Kafka | Particionamento por domínio e volume |
| Knowledge Service | Escala separada para ingestão e consulta |
| Memory Service | Dimensionamento por volume de sessões e retenção |

---

## Segurança

| Requisito | Diretriz |
|---|---|
| Autenticação | OIDC/OAuth2 |
| Autorização | RBAC, ABAC e políticas por recurso |
| Segredos | Secret Manager ou equivalente |
| Criptografia | Em trânsito e em repouso |
| Auditoria | Obrigatória para agentes, tool calls e governança |

---

## Observabilidade

| Requisito | Diretriz |
|---|---|
| Tracing | OpenTelemetry |
| Logs | Estruturados e correlacionados |
| Métricas | Latência, erro, tokens, custo e qualidade |
| Correlação | correlationId obrigatório |
| Dashboards | Plataforma, agente, governança e FinOps |

---

## Dados e LGPD

| Requisito | Diretriz |
|---|---|
| Classificação | Dados classificados por sensibilidade |
| Retenção | Definida por tipo de dado e finalidade |
| Mascaramento | Aplicado em logs, traces e datasets |
| Consentimento | Registrado quando aplicável |
| Direito de exclusão | Suportado por processos de descarte |

---

## FinOps

| Requisito | Diretriz |
|---|---|
| Token tracking | Por agente, modelo, área e usuário técnico |
| Budget alerts | Alertas por limite de consumo |
| Chargeback / Showback | Por unidade de negócio |
| Otimização | Comparação entre modelos por custo e qualidade |

---

## Resiliência

| Requisito | Diretriz |
|---|---|
| Retry | Controlado por tipo de erro |
| Circuit breaker | Obrigatório para integrações externas |
| Fallback | Modelo, provedor ou fluxo alternativo |
| Idempotência | Obrigatória para comandos críticos |
| Graceful degradation | Resposta parcial quando possível |
