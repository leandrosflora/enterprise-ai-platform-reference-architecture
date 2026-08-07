# Authorization

## Modelo

A plataforma usa RBAC + Policy Based Access Control.

- **RBAC** define papéis humanos e técnicos.
- **Policy Based Access Control** aplica regras por recurso, escopo, tenant, classificação de dado, risco do agente e criticidade da ferramenta.
- O enforcement ocorre no **Agent Gateway**, **Agent Runtime**, **Governance Service**, **Knowledge Service** e **MCP Registry**.

## Papéis

| Papel | Descrição |
|---|---|
| Platform Admin | Administra configuração da plataforma, tenants, integrações e políticas globais. |
| AI Architect | Define padrões, revisa arquitetura, governança e risco de agentes. |
| Developer | Cria agentes, ferramentas, knowledge bases e datasets de avaliação. |
| Business User | Usa agentes publicados e aprovados para sua unidade de negócio. |
| Auditor | Consulta trilhas de auditoria, decisões, execuções e evidências. |
| Service Account | Identidade técnica usada por serviços internos e pipelines. |

## Escopos

| Escopo | Uso |
|---|---|
| `agent.read` | Consultar catálogo e metadados de agentes. |
| `agent.write` | Criar ou alterar agente em estado draft. |
| `agent.invoke` | Invocar agente publicado. |
| `agent.publish` | Publicar agente aprovado. |
| `tool.read` | Consultar catálogo MCP. |
| `tool.register` | Registrar tool contract MCP. |
| `tool.execute` | Executar ferramenta aprovada. |
| `knowledge.read` | Consultar knowledge bases autorizadas. |
| `knowledge.write` | Ingerir ou atualizar documentos. |
| `memory.read` | Ler memória de sessão/contexto permitido. |
| `memory.write` | Atualizar memória de sessão/contexto permitido. |
| `governance.submit` | Submeter agente/ferramenta para aprovação. |
| `governance.review` | Revisar risco, segurança, LGPD e arquitetura. |
| `governance.approve` | Aprovar ou rejeitar publicação. |
| `evaluation.read` | Consultar resultados de avaliação. |
| `evaluation.write` | Criar execução de avaliação. |
| `audit.read` | Consultar trilhas de auditoria. |
| `billing.read` | Consultar custos e showback/chargeback. |
| `platform.admin` | Administrar políticas globais. |

---

## Matriz Papel x Escopo

| Papel | Escopos permitidos |
|---|---|
| Platform Admin | `platform.admin`, `agent.read`, `tool.read`, `governance.review`, `audit.read`, `billing.read` |
| AI Architect | `agent.read`, `tool.read`, `governance.review`, `governance.approve`, `evaluation.read`, `audit.read`, `billing.read` |
| Developer | `agent.read`, `agent.write`, `tool.read`, `tool.register`, `knowledge.read`, `knowledge.write`, `evaluation.read`, `evaluation.write`, `governance.submit` |
| Business User | `agent.read`, `agent.invoke`, `knowledge.read` limitado ao tenant/unidade |
| Auditor | `agent.read`, `tool.read`, `evaluation.read`, `audit.read`, `billing.read` |
| Service Account | Escopos mínimos por serviço, definidos por workload identity |

---

## Matriz Recurso x Ação

| Recurso | Ação | Escopo requerido | Papéis típicos | Condições obrigatórias |
|---|---|---|---|---|
| Agent | Listar | `agent.read` | Todos | Respeitar tenant e unidade de negócio. |
| Agent | Criar/editar draft | `agent.write` | Developer | Owner obrigatório. |
| Agent | Submeter aprovação | `governance.submit` | Developer | Evidências de teste e risco obrigatório. |
| Agent | Aprovar/rejeitar | `governance.approve` | AI Architect | Não pode ser o mesmo usuário que submeteu. |
| Agent | Publicar | `agent.publish` | AI Architect, Service Account | Requer decisão `APPROVED`. |
| Agent | Invocar | `agent.invoke` | Business User | Agente precisa estar `PUBLISHED`. |
| Tool MCP | Registrar | `tool.register` | Developer | Contract com schemas válidos. |
| Tool MCP | Executar | `tool.execute` | Service Account via Agent Runtime | Ferramenta aprovada e vinculada ao agente. |
| Knowledge Base | Ingerir documento | `knowledge.write` | Developer | Classificação de dado obrigatória. |
| Knowledge Base | Consultar | `knowledge.read` | Business User, Developer | Política por classificação e tenant. |
| Memory | Ler | `memory.read` | Service Account | Apenas sessão/usuário autorizado. |
| Memory | Escrever | `memory.write` | Service Account | Dados sensíveis mascarados quando exigido. |
| Evaluation | Criar | `evaluation.write` | Developer, Service Account | Dataset aprovado. |
| Evaluation | Consultar | `evaluation.read` | Developer, AI Architect, Auditor | Respeitar tenant. |
| Audit | Consultar | `audit.read` | Auditor, AI Architect | Consulta registrada em auditoria. |
| Billing | Consultar custos | `billing.read` | AI Architect, Auditor, Platform Admin | Visão limitada por unidade ou tenant. |

---

## Políticas por Classificação de Dados

| Classificação | Acesso | Restrições |
|---|---|---|
| PUBLIC | Todos os usuários autenticados | Sem dados pessoais. |
| INTERNAL | Usuários do tenant/unidade | Não pode sair do tenant. |
| CONFIDENTIAL | Usuários autorizados por papel e escopo | Mascaramento obrigatório em logs. |
| RESTRICTED | Apenas papéis explicitamente autorizados | Exige aprovação de governança e auditoria reforçada. |

---

## Políticas por Risco do Agente

| Risco | Exigência mínima |
|---|---|
| LOW | Avaliação automática, owner definido e logs básicos. |
| MEDIUM | Revisão de AI Architect, avaliação de segurança e observabilidade ativa. |
| HIGH | Aprovação humana, matriz de ferramentas permitidas, testes de regressão e auditoria completa. |
| CRITICAL | Comitê de governança, revisão LGPD/Jurídico/Security e plano de rollback. |

---

## Enforcement

| Componente | Responsabilidade |
|---|---|
| Agent Gateway | Validar JWT, tenant, escopos e rate limit. |
| Agent Runtime | Aplicar policy por agente, ferramenta, risco, custo e contexto. |
| MCP Registry | Permitir descoberta apenas de ferramentas aprovadas e autorizadas. |
| Knowledge Service | Aplicar filtros por tenant, unidade, classificação e documento. |
| Governance Service | Controlar separação de funções e estado de aprovação. |
| Audit Service | Registrar decisões de autorização, negações e execuções críticas. |

## Decisão Padrão

A decisão padrão é **deny by default**. Qualquer recurso, ferramenta, knowledge base ou agente sem política explícita é bloqueado.
