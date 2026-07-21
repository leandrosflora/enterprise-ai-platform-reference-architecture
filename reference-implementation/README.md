# AI Platform Reference Implementation

Implementação mínima para demonstrar que os principais limites da arquitetura são executáveis. Não é uma distribuição pronta para produção.

## Componentes

- FastAPI como Agent Gateway/API;
- LangGraph para orquestração do fluxo;
- adapter de modelos com modo local e pontos de extensão para OpenAI/Bedrock;
- PostgreSQL com extensão pgvector;
- Redis para sessão e cache;
- OpenTelemetry para traces;
- Docker Compose para execução local.

## Execução

```bash
cd reference-implementation
docker compose up --build
```

Teste:

```bash
curl -X POST http://localhost:8080/v1/agents/reference-agent/invoke \
  -H 'Content-Type: application/json' \
  -H 'X-Tenant-Id: demo' \
  -d '{"session_id":"session-1","message":"Como funciona a plataforma?"}'
```

## Fluxo

1. gateway valida tenant e entrada;
2. runtime carrega sessão no Redis;
3. grafo decide retrieval, modelo e resposta;
4. uso, latência e correlação são registrados;
5. sessão é atualizada com TTL.

## Evoluções esperadas

- implementar adapters reais de Bedrock e OpenAI;
- adicionar migrations e ingestão de documentos no pgvector;
- incorporar MCP server e ferramentas de domínio;
- aplicar autenticação OIDC/JWT e policy engine;
- exportar métricas de custo para o FinOps.