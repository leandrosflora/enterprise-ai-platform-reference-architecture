# Exemplos End-to-End: Agent + RAG + MCP

This document shows complete flow of use of Enterprise AI Platform combinating agents, RAG, memory, MCP, evaluation, audit and FinOps.

---

## Example 1: Internal Policy Officer with RAG

### Objet

Allow a user to consult a body-based policy with cited and rastreactive responses.

### Componentes envolvidos

| Componente | Papel |
|---|---|
| AI Portal | User interface and autoatendiment. |
| Agent Gateway | Entry single, authentication, authorisation and limit rate. |
| Agent Runtime | Quick order, memory, RAG, model and evaluation. |
| Knowledge Service | Recupera documentos e chunks relevantes. |
| Foundation Model | - A logical answer on the basis of the context recovered. |
| Evaluation Service | Avalance of groundedness, relevance and risk of hallucination. |
| Audit Service | Check the execution line. |
| Billing Service | I've given the cost by agent/time. |

### Agent Card

```yaml
agentId: policy-assistant
name: Assistente de Políticas Internas
version: 1.0.0
owner: governance-team
businessUnit: corporate-governance
riskClassification: MEDIUM
modelPolicy:
  provider: bedrock
  modelId: anthropic.claude-3-5-sonnet
  maxInputTokens: 8000
  maxOutputTokens: 1200
  temperature: 0.2
knowledgeBaseIds:
  - corporate-policies-kb
allowedTools:
  - policy-document-search:1.0.0
requiredEvaluations:
  - GROUNDEDNESS
  - SAFETY
  - LATENCY
```

### Flux

```text
1. Business User envia pergunta no AI Portal.
2. Agent Gateway valida JWT, tenant, escopo agent.invoke e rate limit.
3. Agent Runtime carrega configuração do policy-assistant no Agent Registry.
4. Policy Enforcer valida se o agente pode acessar corporate-policies-kb.
5. Agent Runtime consulta memória da sessão.
6. Agent Runtime chama Knowledge Service para busca RAG.
7. Knowledge Service executa hybrid/vector search no OpenSearch.
8. Agent Runtime monta prompt com instruções, memória e chunks citáveis.
9. Agent Runtime chama foundation model.
10. Evaluation Service avalia groundedness e safety.
11. Audit Service registra input resumido, citações, decisões e output.
12. Billing Service registra tokens e custo.
13. AI Portal exibe resposta com citações.
```

### Request

```http
POST /agents/policy-assistant/invoke
Authorization: Bearer <token>
X-Correlation-Id: 7d8cf2aa-ef5f-4cc3-bafa-61ea26277511
Content-Type: application/json
```

```json
{
  "input": "Qual é a regra para retenção de dados pessoais em documentos internos?",
  "channel": "ai-portal",
  "sessionId": "session-20260706-001",
  "context": {
    "tenantId": "enterprise",
    "businessUnit": "corporate-governance",
    "locale": "pt-BR"
  }
}
```

### Knowledge Search

```json
{
  "query": "regra retenção dados pessoais documentos internos",
  "knowledgeBaseId": "corporate-policies-kb",
  "topK": 5,
  "filters": {
    "classification": "INTERNAL",
    "businessUnit": "corporate-governance"
  }
}
```

### Response

```json
{
  "conversationId": "conv-001",
  "messageId": "msg-001",
  "answer": "A retenção deve seguir a finalidade aprovada, o prazo definido na tabela de retenção e os requisitos de LGPD. Quando o prazo expirar, o documento deve ser eliminado ou anonimizado conforme a política corporativa.",
  "citations": [
    {
      "sourceId": "policy-lgpd-001",
      "title": "Política Corporativa de Privacidade e Retenção",
      "uri": "s3://corporate-policies/lgpd-retention.pdf",
      "chunkId": "chunk-014",
      "score": 0.91
    }
  ],
  "toolCalls": [
    {
      "toolName": "policy-document-search",
      "toolVersion": "1.0.0",
      "status": "SUCCESS",
      "latencyMs": 580
    }
  ],
  "tokenUsage": {
    "inputTokens": 1850,
    "outputTokens": 310,
    "totalCostUsd": 0.012
  },
  "evaluationStatus": "approved"
}
```

### Eventos esperados

| Evento | Produtor | Consumidores |
|---|---|---|
| `agent.invoked` | Agent Runtime | Audit Service, Billing Service, Evaluation Service |
| `tool.executed` | Agent Runtime | Audit Service, Billing Service |
| `evaluation.completed` | Evaluation Service | Governance Service, Audit Service |
| `audit.created` | Audit Service | Observability Stack |

---

## Example 2: Operations Officer with MCP of Controlled Writing

### Objet

Allow an agent to assist in a process of updating cases, but only with human authorization and approval when necessary.

### Componentes envolvidos

| Componente | Papel |
|---|---|
| Agent Runtime | Listen to the flow and apply policies. |
| MCP Registry | Descobre ferramentas aprovadas. |
| MCP Server | Expenditure `case-update`. |
| Corporate System | Operative system that carries cases. |
| Governance Service | - Definition of high-risk steel. |
| Audit Service | Check execution and decision. |

### Agent Card

```yaml
agentId: operations-case-assistant
name: Assistente de Casos Operacionais
version: 1.0.0
owner: operations-team
businessUnit: customer-operations
riskClassification: HIGH
modelPolicy:
  provider: bedrock
  modelId: anthropic.claude-3-5-sonnet
  maxInputTokens: 6000
  maxOutputTokens: 1000
  temperature: 0.1
allowedTools:
  - customer-search:1.0.0
  - case-update:1.0.0
humanApproval:
  requiredForTools:
    - case-update
```

### Flux

```text
1. Usuário solicita atualização de caso via AI Portal.
2. Agent Gateway valida escopo agent.invoke.
3. Agent Runtime identifica necessidade de executar case-update.
4. Policy Enforcer verifica que case-update é HIGH e exige human approval.
5. Runtime gera proposta de ação e solicita confirmação humana.
6. Usuário confirma.
7. Runtime consulta MCP Registry e valida tool contract.
8. MCP Client invoca MCP Server com idempotencyKey.
9. MCP Server atualiza Corporate System.
10. Runtime publica tool.executed.
11. Audit Service registra ação, decisão e usuário confirmador.
12. Billing Service registra custo.
```

### Proposal before implementation

```json
{
  "proposedAction": {
    "toolName": "case-update",
    "toolVersion": "1.0.0",
    "riskClassification": "HIGH",
    "requiresHumanApproval": true,
    "input": {
      "caseId": "CASE-12345",
      "operation": "CHANGE_STATUS",
      "newStatus": "WAITING_CUSTOMER"
    }
  },
  "approvalRequired": true,
  "reason": "A ferramenta altera estado em sistema corporativo. Política exige confirmação humana."
}
```

### MCP Tool Invocation

```json
{
  "caseId": "CASE-12345",
  "operation": "CHANGE_STATUS",
  "newStatus": "WAITING_CUSTOMER",
  "idempotencyKey": "operations-case-assistant-CASE-12345-20260706-001"
}
```

### MCP Tool Response

```json
{
  "caseId": "CASE-12345",
  "status": "WAITING_CUSTOMER",
  "updatedAt": "2026-07-06T12:45:00Z",
  "operationId": "op-789"
}
```

### Evento `tool.executed`

```json
{
  "eventId": "evt-tool-001",
  "eventType": "tool.executed",
  "schemaVersion": "1.0.0",
  "occurredAt": "2026-07-06T12:45:01Z",
  "correlationId": "7d8cf2aa-ef5f-4cc3-bafa-61ea26277511",
  "causationId": "msg-001",
  "tenantId": "enterprise",
  "source": "agent-runtime",
  "payload": {
    "agentId": "operations-case-assistant",
    "agentVersion": "1.0.0",
    "toolName": "case-update",
    "toolVersion": "1.0.0",
    "status": "SUCCESS",
    "latencyMs": 920,
    "humanApproval": {
      "required": true,
      "approvedBy": "user-hash-123",
      "approvedAt": "2026-07-06T12:44:58Z"
    }
  }
}
```

---

## Example 3: Agent Publication Pipeline

### Objet

Publicate an agent only after the validity of contracts, risk, security, assessment, observation and FinOps.

### Flux

```text
1. Developer cria Agent Card e tool allowlist.
2. Developer registra ou referencia MCP contracts.
3. Developer vincula knowledge bases permitidas.
4. Evaluation Service executa dataset de regressão e safety.
5. Governance Service calcula risco e valida evidências.
6. AI Architect aprova ou rejeita.
7. Agent Registry muda status para APPROVED.
8. Pipeline publica agente em produção.
9. Agent Runtime passa a aceitar invocações da versão publicada.
```

### Publications evidence

| Evidence | Thank you. |
|---|---:|
| Agent Card | Sim |
| OpenAPI/Tool contracts | Sim |
| Risk assessment | Sim |
| Evaluation report | Sim |
| Authorization matrix | Sim |
| Observability dashboard | Sim |
| FinOps budget | Sim |
| Rollback plan | Sim |

### Governance Submission

```json
{
  "agentVersion": "1.0.0",
  "riskClassification": "HIGH",
  "evidence": [
    "agent-card.yaml",
    "evaluation-report-20260706.json",
    "authorization-matrix.md",
    "mcp-contracts.md",
    "observability-dashboard.json",
    "rollback-plan.md"
  ],
  "notes": "Agente operacional com ferramenta de escrita case-update. Human approval obrigatório."
}
```

### Governance Decision

```json
{
  "approvalId": "apv-001",
  "agentId": "operations-case-assistant",
  "decision": "APPROVED",
  "riskClassification": "HIGH",
  "decidedBy": "ai-architect-hash-456",
  "decidedAt": "2026-07-06T13:00:00Z"
}
```

---

## Checklist End-to-End

| Item | Acceptance criteria |
|---|---|
| Agent Card | Type owner, version, risk, model, tools and KBs. |
| OpenAPI | Endpoint documented with request, response, error and escope. |
| MCP Contract | Tool with input/output schema, security, audit and runtime policy. |
| Authorization | - Pitch, escap, resource and defined conditions. |
| Risk Controls | Printed with control, evidence and ownership. |
| Observability | Completely with spans and binding attributes. |
| Evaluation | Definitions and approved report. |
| FinOps | Budget e cost attribution configurados. |
| Audit | Eventos `agent.invoked`, `tool.executed` e `audit.created` registrados. |
| Rollback | Process defined to remove agent or iron. |
