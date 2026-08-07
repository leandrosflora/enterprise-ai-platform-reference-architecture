# Example - Implementation Trace

## Objective

Example of tip-to-end traceability for agent invocation.

```text
traceId: trace-001
correlationId: corr-2026-001

spans:
  - name: agent-gateway.receive-request
    durationMs: 80
    attributes:
      agentId: internal-copilot
      userId: user-123

  - name: agent-runtime.execute
    durationMs: 2400
    attributes:
      agentVersion: 1.0.0
      runtime: langgraph

  - name: knowledge-service.retrieve
    durationMs: 650
    attributes:
      knowledgeBaseId: kb-policies
      documentsReturned: 5

  - name: foundation-model.invoke
    durationMs: 1450
    attributes:
      provider: bedrock
      modelId: anthropic.claude
      inputTokens: 1200
      outputTokens: 350

  - name: evaluation-service.evaluate
    durationMs: 220
    attributes:
      groundednessScore: 0.92
      relevanceScore: 0.88
```

## Implementation

O trace permite diagnosticar:

- Latency per component
- Consumo de tokens
- Quality of response
- Integration failures
- Gargalos de retrieval
