# Authorization

## Model

The platform uses RBAC + Policy Based Access Control.

- **RBAC** defines human and technical paediatric paediatrics.
- **Policy Based Access Control** applies rules for resource, escopo, tenant, dad classification, agent risk and iron criticity.
- The enforcement occurs in **Agent Gateway**, **Agent Runtime**, **Governance Service**, **Knowledge Service** and **MCP Registry**.

## Papers

| Papel | Description |
|---|---|
| Platform Admin | Configuration of the platform, tenants, integrations and global policies. |
| AI Architect | Set rules, review architecture, governance and risk of agents. |
| Developer | Criasants, tools, knowledge bases and evaluation datasets. |
| Business User | Use public and approved agents for your business unit. |
| Auditor | Consult auditory trilles, decisions, executions and evidence. |
| Service Account | Technical identity used by inter- and pipeline services. |

## Escopos

| Escopo | Uso |
|---|---|
| `agent.read` | Consult catalog and a number of agents. |
| `agent.write` | Write or change agent in draft state. |
| `agent.invoke` | - Invocating published agent. |
| `agent.publish` | Publicate approved agent. |
| `tool.read` | Consult MCP. |
| `tool.register` | Registrar tool contract MCP. |
| `tool.execute` | Executar ferramenta aprovada. |
| `knowledge.read` | Consultar knowledge bases autorizadas. |
| `knowledge.write` | Ingerir ou atualizar documentos. |
| `memory.read` | A memory of sitting/context allowed. |
| `memory.write` | Maintain a memory of sitting/context allowed. |
| `governance.submit` | Submit agent/fra-fra-fra-fra-fra-fra-fra-fra-fra-fra-fra-fra-fra-fra-fra-fra-fra-fra-fra-fra-fra-fra-fra-fra-fra-fra-fra-flying approval. |
| `governance.review` | Reconsider risk, security, LGPD and architecture. |
| `governance.approve` | - Accept or reject publication. |
| `evaluation.read` | Check out the evaluation results. |
| `evaluation.write` | Creating evaluation. |
| `audit.read` | Check out auditory boxes. |
| `billing.read` | See costs and showback/chargeback. |
| `platform.admin` | Administrating global policies. |

---

## Matriz Papel x Escopo

| Papel | Escopos permitidos |
|---|---|
| Platform Admin | `platform.admin`, `agent.read`, `tool.read`, `governance.review`, `audit.read`, `billing.read` |
| AI Architect | `agent.read`, `tool.read`, `governance.review`, `governance.approve`, `evaluation.read`, `audit.read`, `billing.read` |
| Developer | `agent.read`, `agent.write`, `tool.read`, `tool.register`, `knowledge.read`, `knowledge.write`, `evaluation.read`, `evaluation.write`, `governance.submit` |
| Business User | `agent.read`, `agent.invoke`, `knowledge.read` limitado ao tenant/unidade |
| Auditor | `agent.read`, `tool.read`, `evaluation.read`, `audit.read`, `billing.read` |
| Service Account | Minimums for service, defined by a corresponding workload |

---

## x Action

| Recurso | Action | Escopo requerido | Typical figures | Conditions for compulsory conditions |
|---|---|---|---|---|
| Agent | Listar | `agent.read` | Todos | Remain tenant and business unit. |
| Agent | Criar/editar draft | `agent.write` | Developer | - The owner's obliged. |
| Agent | Approval | `governance.submit` | Developer | Test evidence and obligation risk. |
| Agent | Aprovar/rejeitar | `governance.approve` | AI Architect | It can't be the same user you've submitted. |
| Agent | Publicar | `agent.publish` | AI Architect, Service Account | Request `APPROVED`. |
| Agent | Invocar | `agent.invoke` | Business User | Agent needs to be `PUBLISHED`. |
| Tool MCP | Registrar | `tool.register` | Developer | Contract with multiple schemas. |
| Tool MCP | Executar | `tool.execute` | Service Account via Agent Runtime | Approved and notified to the agent. |
| Knowledge Base | Ingerir documento | `knowledge.write` | Developer | Classification of duty. |
| Knowledge Base | Consultar | `knowledge.read` | Business User, Developer | Policy for classification and tenant. |
| Memory | Ler | `memory.read` | Service Account | Only a session/use authorized. |
| Memory | Escrever | `memory.write` | Service Account | Sensible data messed up when required. |
| Evaluation | Criar | `evaluation.write` | Developer, Service Account | Dataset aprovado. |
| Evaluation | Consultar | `evaluation.read` | Developer, AI Architect, Auditor | Respeitar tenant. |
| Audit | Consultar | `audit.read` | Auditor, AI Architect | Checked out in the auditorium. |
| Billing | Consult costs | `billing.read` | AI Architect, Auditor, Platform Admin | Limited visibility by unit or tenant. |

---

## Data Classification Policies

| Classification | Acesso | Excusements |
|---|---|---|
| PUBLIC | All authentic users | No personal data. |
| INTERNAL | Owner/unit users | You can't leave the tenant. |
| CONFIDENTIAL | Auto-employed workers by job and escope | - a mandatory mashment in logs. |
| RESTRICTED | Only explicitly authorised copies | Exhausted government approval and enhanced audit. |

---

## Policies by the Agent Risco

| Risco | Minimum exigence |
|---|---|
| LOW | Auto-adjustment, defined owner and basic logs. |
| MEDIUM | Architect AI review, security assessment and active observation. |
| HIGH | Human amplification, a killing of permitted tools, regress tests and full auditory. |
| CRITICAL | Government committee, review LGPD/Jury/Security and rollback plan. |

---

## Enforcement

| Componente | Responsabilidade |
|---|---|
| Agent Gateway | Validar JWT, tenant, escopos e rate limit. |
| Agent Runtime | Implement policy by agent, tool, risk, cost and context. |
| MCP Registry | Allow discovery only of approved and authorized tools. |
| Knowledge Service | Using filters by tenant, unit, classification and document. |
| Governance Service | Control separation of functions and approval status. |
| Audit Service | Registrating decisions for authorisation, negotiations and critical implementations. |

## Decision Father

The standard decision is **deny by default**. Any resource, tool, knowledge base or agent without explicit policy is blocked.
