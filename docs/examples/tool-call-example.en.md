# Exemplo - Tool Call MCP

## Objective

Example of exposed tool call via MCP Server.

```json
{
  "correlationId": "corr-2026-001",
  "agentId": "internal-copilot",
  "toolName": "customer-search",
  "toolVersion": "1.0.0",
  "caller": {
    "userId": "user-123",
    "businessUnit": "Atendimento",
    "roles": ["BusinessUser"]
  },
  "arguments": {
    "document": "12345678900",
    "documentType": "CPF"
  }
}
```

## Resposta Esperada

```json
{
  "correlationId": "corr-2026-001",
  "status": "SUCCESS",
  "result": {
    "customerId": "cust-789",
    "status": "ACTIVE"
  }
}
```

## Controls

- Validation by JSON Schema
- Scope authorisation
- Tool call audit
- Sensitive data masking in logs
