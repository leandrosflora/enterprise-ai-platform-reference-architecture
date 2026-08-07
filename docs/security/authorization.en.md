# Authorization

## Model

A plataforma usa RBAC + Policy Based Access Control.

- **RBAC** defines human and technical roles.
- **Policy Based Access Control** it applies rules by resource, scope, tenant, data classification, agent risk and tool criticality.
- The enforcement occurs at the **Agent Gateway**, **Agent Runtime**, **Governance Service**, **Knowledge Service** and **MCP Registry**.

## Papers

| role | Description |
|---|---|
| Platform Admin | It administers platform configuration, tenants, integrations and global policies. |
| AI Architect | It defines standards, reviews architecture, governance and risk of agents. |
| Developer | It creates agents, tools, knowledge bases and evaluation dates. |
| Business User | It uses agents that are published and approved for its business unit. |
| Auditor | It consults audit trails, decisions, executions and evidence. |
| Service Account | Technical identity used by internal and pipelines services. |

## Escopos

| scope | Uso |
|---|---|
|  `agent.read`  | Refer to catalog and metadata of agents. |
|  `agent.write`  | Create or change agent in state draft. |
|  `agent.invoke`  | Invite a published agent. |
|  `agent.publish`  | Publication of approved agent. |
|  `tool.read`  | Read the MCP catalog. |
|  `tool.register`  | record tool contract MCP. |
|  `tool.execute`  | Perform approved tool. |
|  `knowledge.read`  | Consultar knowledge bases autorizadas. |
|  `knowledge.write`  | Ingerir or atualizar documents. |
|  `memory.read`  | Read session memory/authorised context. |
|  `memory.write`  | Update session memory/authorised context. |
|  `governance.submit`  | Submit agent/tool for approval. |
|  `governance.review`  | To review risk, safety, LGPD and architecture. |
|  `governance.approve`  | Approve or refuse publication. |
|  `evaluation.read`  | Refer to assessment results. |
|  `evaluation.write`  | Create execution of evaluation. |
|  `audit.read`  | Consulting audit trails. |
|  `billing.read`  | Consulting costs and showback/chargeback. |
|  `platform.admin`  | Administering global policies. |

---

## Matriz role x scope

| role | Escopos permitidos |
|---|---|
| Platform Admin |  `platform.admin`, `agent.read`, `tool.read`, `governance.review`, `audit.read`, `billing.read`  |
| AI Architect |  `agent.read`, `tool.read`, `governance.review`, `governance.approve`, `evaluation.read`, `audit.read`, `billing.read`  |
| Developer |  `agent.read`, `agent.write`, `tool.read`, `tool.register`, `knowledge.read`, `knowledge.write`, `evaluation.read`, `evaluation.write`, `governance.submit`  |
| Business User |  `agent.read`, `agent.invoke`, `knowledge.read` limitado ao tenant/unidade |
| Auditor |  `agent.read`, `tool.read`, `evaluation.read`, `audit.read`, `billing.read`  |
| Service Account | Minimum scores per service, defined by workload identity |

---

## Resource x Action matrix

| Action | Action | Required score | Typical papers | Compulsory conditions |
|---|---|---|---|---|
| Agent | Listar |  `agent.read`  | Todos | Respect tenant and business unit. |
| Agent | Create/release draft |  `agent.write`  | Developer | Obligatory owner. |
| Agent | Submit approval |  `governance.submit`  | Developer | Test evidence and mandatory risk. |
| Agent | approve/rejeitar |  `governance.approve`  | AI Architect | It cannot be the same user that submitted. |
| Agent | Publicar |  `agent.publish`  | AI Architect, Service Account | Application for a decision `APPROVED`. |
| Agent | Invocar |  `agent.invoke`  | Business User | Agents should be able to work in any of these areas. `PUBLISHED`. |
| Tool MCP | record |  `tool.register`  | Developer | Contract with valid schemas. |
| Tool MCP | Perform |  `tool.execute`  | Service Account via Agent Runtime | Tool approved and linked to the agent. |
| Knowledge Base | Taking a document |  `knowledge.write`  | Developer | Compulsory classification of data. |
| Knowledge Base | Consultar |  `knowledge.read`  | Business User, Developer | Policy by classification and tenant. |
| Memory | Ler |  `memory.read`  | Service Account | Only session/authorised user. |
| Memory | Escrever |  `memory.write`  | Service Account | Sensitive data masked when required. |
| Evaluation | Create |  `evaluation.write`  | Developer, Service Account | Date of approval. |
| Evaluation | Consultar |  `evaluation.read`  | Developer, AI Architect, Auditor | Respeitar tenant. |
| Audit | Consultar |  `audit.read`  | Auditor, AI Architect | Consulta registrada in audit. |
| Billing | Consulting costs |  `billing.read`  | AI Architect, Auditor, Platform Admin | Limitated view per unit or tenant. |

---

## Data Classification Policies

| Classification | Acesso | Restrictions |
|---|---|---|
| PUBLIC | All authenticated users | No personal data. |
| INTERNAL | Users of tenant/unit | You cannot leave tenant. |
| CONFIDENTIAL | Users authorised by paper and scope | Compulsory masking in logs. |
| RESTRICTED | Only explicitly authorised paper | It requires approval of governance and reinforced audit. |

---

## Agent Risk Policies

| Risk | Minimum requirement |
|---|---|
| LOW | Automatic evaluation, defined owner and basic logs. |
| MEDIUM | AI Architect review, safety assessment and active observability. |
| HIGH | Human approval, matrix of allowed tools, regression tests and complete audit. |
| CRITICAL | Governance Committee, LGPD/Juridical/Security review and rollback plan. |

---

## Enforcement

| component | responsibility |
|---|---|
| Agent Gateway | Validate JWT, tenant, scopes and rate limit. |
| Agent Runtime | Apply policy by agent, tool, risk, cost and context. |
| MCP Registry | To allow the discovery of only approved and authorised tools. |
| Knowledge Service | Apply filters by tenant, unit, classification and document. |
| Governance Service | Checking separation of functions and approval status. |
| Audit Service | Register decisions on authorization, denials and critical executions. |

## Standard Decision

Standard decision is **deny by default**. Any resource, tool, base knowledge or agent without explicit policy shall be blocked.
