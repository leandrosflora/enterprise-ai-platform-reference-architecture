# MCP Contracts

Este documento define o contrato mínimo para ferramentas MCP corporativas expostas para agentes da Enterprise AI Platform.

## Princípios

- Todo tool contract deve ter `toolName`, `version`, `description`, `inputSchema`, `outputSchema`, `security`, `audit` e `runtimePolicy`.
- Schemas devem usar JSON Schema Draft 2020-12.
- Ferramentas são versionadas semanticamente.
- RBAC e escopos são obrigatórios por ferramenta.
- Toda execução deve carregar `correlationId`, `causationId`, `agentId`, `sessionId` e `tenantId`.
- Dados sensíveis devem ser classificados e mascarados em logs.
- Nenhuma ferramenta crítica pode ser executada sem política explícita de timeout, retry e idempotência.

---

## Envelope Padrão de Tool Contract

```json
{
  "toolName": "customer-search",
  "version": "1.0.0",
  "description": "Search customers by CPF, customerId or email.",
  "owner": "customer-platform-team",
  "riskClassification": "MEDIUM",
  "inputSchema": {},
  "outputSchema": {},
  "security": {
    "requiredScopes": ["tool.customer-search.execute"],
    "allowedRoles": ["Developer", "Business User"],
    "dataClassification": "CONFIDENTIAL"
  },
  "audit": {
    "required": true,
    "maskFields": ["cpf", "email", "phoneNumber"],
    "eventType": "tool.executed"
  },
  "runtimePolicy": {
    "timeoutMs": 3000,
    "retry": {
      "maxAttempts": 2,
      "backoffMs": 200
    },
    "idempotencyRequired": false
  }
}
```

---

## Tool: customer-search

### Finalidade

Localizar clientes em sistemas corporativos para apoiar agentes de atendimento, crédito ou backoffice.

### Contract

```json
{
  "toolName": "customer-search",
  "version": "1.0.0",
  "description": "Search customers by CPF, customerId or email.",
  "owner": "customer-platform-team",
  "riskClassification": "MEDIUM",
  "inputSchema": {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "additionalProperties": false,
    "required": ["searchType", "searchValue"],
    "properties": {
      "searchType": {
        "type": "string",
        "enum": ["CPF", "CUSTOMER_ID", "EMAIL"]
      },
      "searchValue": {
        "type": "string",
        "minLength": 3,
        "maxLength": 120
      },
      "includeInactive": {
        "type": "boolean",
        "default": false
      }
    }
  },
  "outputSchema": {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "additionalProperties": false,
    "required": ["customers"],
    "properties": {
      "customers": {
        "type": "array",
        "maxItems": 20,
        "items": {
          "type": "object",
          "required": ["customerId", "displayName", "status"],
          "properties": {
            "customerId": { "type": "string" },
            "displayName": { "type": "string" },
            "documentHash": { "type": "string" },
            "emailMasked": { "type": "string" },
            "status": { "type": "string", "enum": ["ACTIVE", "INACTIVE", "BLOCKED"] }
          }
        }
      }
    }
  },
  "security": {
    "requiredScopes": ["tool.customer-search.execute"],
    "allowedRoles": ["Developer", "Business User"],
    "dataClassification": "CONFIDENTIAL"
  },
  "audit": {
    "required": true,
    "maskFields": ["searchValue", "emailMasked"],
    "eventType": "tool.executed"
  },
  "runtimePolicy": {
    "timeoutMs": 3000,
    "retry": { "maxAttempts": 2, "backoffMs": 200 },
    "idempotencyRequired": false
  }
}
```

---

## Tool: policy-document-search

### Finalidade

Executar busca controlada em bases documentais corporativas via Knowledge Service.

### Contract

```json
{
  "toolName": "policy-document-search",
  "version": "1.0.0",
  "description": "Search approved corporate policy documents using hybrid retrieval.",
  "owner": "knowledge-platform-team",
  "riskClassification": "LOW",
  "inputSchema": {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "additionalProperties": false,
    "required": ["query", "knowledgeBaseId"],
    "properties": {
      "query": { "type": "string", "minLength": 3, "maxLength": 1000 },
      "knowledgeBaseId": { "type": "string" },
      "topK": { "type": "integer", "minimum": 1, "maximum": 20, "default": 5 },
      "filters": {
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "classification": { "type": "string", "enum": ["PUBLIC", "INTERNAL", "CONFIDENTIAL"] },
          "businessUnit": { "type": "string" },
          "effectiveDateFrom": { "type": "string", "format": "date" }
        }
      }
    }
  },
  "outputSchema": {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "additionalProperties": false,
    "required": ["results"],
    "properties": {
      "results": {
        "type": "array",
        "items": {
          "type": "object",
          "required": ["documentId", "title", "chunkId", "score", "excerpt"],
          "properties": {
            "documentId": { "type": "string" },
            "title": { "type": "string" },
            "chunkId": { "type": "string" },
            "score": { "type": "number", "minimum": 0, "maximum": 1 },
            "excerpt": { "type": "string" },
            "sourceUri": { "type": "string" }
          }
        }
      }
    }
  },
  "security": {
    "requiredScopes": ["tool.policy-document-search.execute", "knowledge.read"],
    "allowedRoles": ["Developer", "Business User", "Auditor", "AI Architect"],
    "dataClassification": "INTERNAL"
  },
  "audit": {
    "required": true,
    "maskFields": [],
    "eventType": "tool.executed"
  },
  "runtimePolicy": {
    "timeoutMs": 5000,
    "retry": { "maxAttempts": 2, "backoffMs": 250 },
    "idempotencyRequired": false
  }
}
```

---

## Tool: case-update

### Finalidade

Atualizar um caso operacional em sistema corporativo. Esta ferramenta executa escrita e exige idempotência.

### Contract

```json
{
  "toolName": "case-update",
  "version": "1.0.0",
  "description": "Update an operational case with a new status, note or assignment.",
  "owner": "operations-platform-team",
  "riskClassification": "HIGH",
  "inputSchema": {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "additionalProperties": false,
    "required": ["caseId", "operation", "idempotencyKey"],
    "properties": {
      "caseId": { "type": "string" },
      "operation": { "type": "string", "enum": ["ADD_NOTE", "CHANGE_STATUS", "ASSIGN"] },
      "note": { "type": "string", "maxLength": 2000 },
      "newStatus": { "type": "string", "enum": ["OPEN", "IN_PROGRESS", "WAITING_CUSTOMER", "RESOLVED", "CLOSED"] },
      "assignee": { "type": "string" },
      "idempotencyKey": { "type": "string", "minLength": 20, "maxLength": 100 }
    },
    "allOf": [
      {
        "if": { "properties": { "operation": { "const": "ADD_NOTE" } } },
        "then": { "required": ["note"] }
      },
      {
        "if": { "properties": { "operation": { "const": "CHANGE_STATUS" } } },
        "then": { "required": ["newStatus"] }
      },
      {
        "if": { "properties": { "operation": { "const": "ASSIGN" } } },
        "then": { "required": ["assignee"] }
      }
    ]
  },
  "outputSchema": {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "additionalProperties": false,
    "required": ["caseId", "status", "updatedAt"],
    "properties": {
      "caseId": { "type": "string" },
      "status": { "type": "string" },
      "updatedAt": { "type": "string", "format": "date-time" },
      "operationId": { "type": "string" }
    }
  },
  "security": {
    "requiredScopes": ["tool.case-update.execute"],
    "allowedRoles": ["Developer"],
    "dataClassification": "CONFIDENTIAL",
    "requiresHumanApproval": true
  },
  "audit": {
    "required": true,
    "maskFields": ["note"],
    "eventType": "tool.executed"
  },
  "runtimePolicy": {
    "timeoutMs": 4000,
    "retry": { "maxAttempts": 1, "backoffMs": 0 },
    "idempotencyRequired": true
  }
}
```

---

## Erros Padronizados

```json
{
  "code": "TOOL_POLICY_DENIED",
  "message": "Agent is not allowed to execute the requested tool.",
  "correlationId": "7d8cf2aa-ef5f-4cc3-bafa-61ea26277511",
  "details": [
    "Missing scope: tool.case-update.execute",
    "Risk classification HIGH requires human approval"
  ]
}
```

## Eventos Obrigatórios

Toda execução deve publicar `tool.executed` com os campos mínimos:

| Campo | Obrigatório | Observação |
|---|---:|---|
| `eventId` | Sim | UUID |
| `eventType` | Sim | `tool.executed` |
| `schemaVersion` | Sim | SemVer |
| `correlationId` | Sim | Propagado da invocação do agente |
| `causationId` | Sim | Comando ou mensagem que causou a execução |
| `agentId` | Sim | Agente solicitante |
| `toolName` | Sim | Nome da ferramenta |
| `toolVersion` | Sim | Versão executada |
| `status` | Sim | `SUCCESS`, `FAILED` ou `BLOCKED` |
| `latencyMs` | Sim | Duração total |
| `errorCode` | Não | Obrigatório quando `status != SUCCESS` |
