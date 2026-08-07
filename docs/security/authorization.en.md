# Authorization

## Model

The platform uses RBAC + Policy Based Access Control.

- **RBAC** defines human and technical roles.
- **Policy Based Access Control** applies rules by resource, scope, tenant, data classification, agent risk and tool criticality.
- Enforcement takes place in **Agent Gateway**, **Agent Runtime**, **Governance Service**, **Knowledge Service** and **MCP Registry**.

## Paperwork

| Papel | Other information |
|---|---|
| Platform Admin | Manages platform configuration, tenants, integrations and global policies. |
| AI Architect | It sets standards, reviews architecture, governance and agent risk. |
| Developer | It creates agents, tools, knowledge bases and assessment datasets. |
| Business User | Use published and approved agents for your business unit. |
| Auditor | It consults audit trails, decisions, executions and evidence. |
| Service Account | Technical identity used by internal services and pipelines. |

## Escopos

| Escopo | Uso |
|---|---|
| `agent.read` | See the agent catalog and metadata. |
| `agent.write` | Creating or changing agent in draft status. |
| `agent.invoke` | Call in a posted agent. |
| `agent.publish` | Release an approved agent. |
| `tool.read` | See the catalogue MCP. |
| `tool.register` | Registrar tool contract MCP. |
| `tool.execute` | Executar ferramenta aprovada. |
| `knowledge.read` | Consultar knowledge bases autorizadas. |
| `knowledge.write` | Ingerir ou atualizar documentos. |
| `memory.read` | Read session memory/context allowed. |
| `memory.write` | Updating session/context memory allowed. |
| `governance.submit` | Submit the agent/tool for approval. |
| `governance.review` | Reviewing risk, security, LGPD and architecture. |
| `governance.approve` | Approve or reject publication. |
| `evaluation.read` | See the results of the evaluation. |
| `evaluation.write` | Create an evaluation execution. |
| `audit.read` | Look for audit trails. |
| `billing.read` | Consult costs and showback/chargeback. |
| `platform.admin` | Manage global policies. |

---

## Matriz Papel x Escopo

| Papel | Escopos permitidos |
|---|---|
| Platform Admin | `platform.admin`, `agent.read`, `tool.read`, `governance.review`, `audit.read`, `billing.read` |
| AI Architect | `agent.read`, `tool.read`, `governance.review`, `governance.approve`, `evaluation.read`, `audit.read`, `billing.read` |
| Developer | `agent.read`, `agent.write`, `tool.read`, `tool.register`, `knowledge.read`, `knowledge.write`, `evaluation.read`, `evaluation.write`, `governance.submit` |
| Business User | `agent.read`, `agent.invoke`, `knowledge.read` limitado ao tenant/unidade |
| Auditor | `agent.read`, `tool.read`, `evaluation.read`, `audit.read`, `billing.read` |
| Service Account | Minimum scope per service, defined by workload identity |

---

## Matrix Recourse x Action

| Recurso | Action | Escopo requerido | Typical papers | Compulsory conditions |
|---|---|---|---|---|
| Agent | Listar | `agent.read` | Todos | Respect tenant and business unit. |
| Agent | Criar/editar draft | `agent.write` | Developer | Obligatory owner. |
| Agent | Submission of approval | `governance.submit` | Developer | Test evidence and mandatory risk. |
| Agent | Aprovar/rejeitar | `governance.approve` | AI Architect | It can't be the same user you submitted. |
| Agent | Publicar | `agent.publish` | AI Architect, Service Account | It requires a decision `APPROVED`. |
| Agent | Invocar | `agent.invoke` | Business User | Agent needs to be `PUBLISHED`. |
| Tool MCP | Registrar | `tool.register` | Developer | Contract with valid schemes. |
| Tool MCP | Executar | `tool.execute` | Service Account via Agent Runtime | Approved tool and attached to the agent. |
| Knowledge Base | Ingerir documento | `knowledge.write` | Developer | This is a mandatory data classification. |
| Knowledge Base | Consultar | `knowledge.read` | Business User, Developer | Policy by rank and tenant. |
| Memory | Ler | `memory.read` | Service Account | Only session/authorized user. |
| Memory | Escrever | `memory.write` | Service Account | Sensitive data disguised when required. |
| Evaluation | Criar | `evaluation.write` | Developer, Service Account | Dataset aprovado. |
| Evaluation | Consultar | `evaluation.read` | Developer, AI Architect, Auditor | Respeitar tenant. |
| Audit | Consultar | `audit.read` | Auditor, AI Architect | Registered audit consultation. |
| Billing | Consulting costs | `billing.read` | AI Architect, Auditor, Platform Admin | Limited vision per unit or tenant. |

---

## Classification of data policies

| Classification | Acesso | Restrictions |
|---|---|---|
| PUBLIC | All authenticated users | No personal data. |
| INTERNAL | Users of the tenant/unit | You can't leave the tenant. |
| CONFIDENTIAL | Users authorised by paper and scope | Compulsory log masking. |
| RESTRICTED | Only explicitly authorised papers | It requires governance approval and enhanced auditing. |

---

## Risk policies of the agent

| Risco | Minimum requirement |
|---|---|
| LOW | Automatic evaluation, owner defined and basic logs. |
| MEDIUM | AI Architect review, safety assessment and active observability. |
| HIGH | Human approval, permissible toolkit, regression testing and full audit. |
| CRITICAL | Governance committee, review LGPDLegal/Security and rollback plan. |

---

## Enforcement

| Component | Responsabilidade |
|---|---|
| Agent Gateway | Validate JWT, tenant, scopes and rate limit. |
| Agent Runtime | Apply policy by agent, tool, risk, cost and context. |
| MCP Registry | Allow discovery only of approved and authorised tools. |
| Knowledge Service | Apply filters by tenant, unit, classification and document. |
| Governance Service | Control separation of functions and approval status. |
| Audit Service | Register authorisation decisions, denials and critical executions. |

## Standard decision

The default decision is **deny by default**. Any resource, tool, knowledge base or agent without explicit policy is blocked.
