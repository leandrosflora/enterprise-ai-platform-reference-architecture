# ADR-004: Estratégia de Observabilidade

## Status

Aceito

## Contexto

Soluções com agentes e LLMs exigem observabilidade além de logs tradicionais.

É necessário rastrear:

- Invocações de agentes
- Chamadas de modelo
- Tool calls
- Recuperação RAG
- Uso de memória
- Tokens
- Custos
- Latência
- Erros
- Resultado de avaliação

## Decisão

Adotar OpenTelemetry como padrão de tracing, métricas e logs correlacionados.

A plataforma deve gerar trace por execução de agente e spans específicos para modelo, ferramenta, memória, RAG e avaliação.

## Consequências Positivas

- Observabilidade padronizada
- Facilidade de integração com stacks existentes
- Correlação ponta a ponta por `correlationId`
- Melhor diagnóstico de falhas e custo
- Base para dashboards executivos e operacionais

## Consequências Negativas

- Aumenta volume de telemetria
- Exige política de mascaramento de dados sensíveis
- Requer governança sobre retenção de logs e traces

## Alternativas Consideradas

### Logs customizados por serviço

Rejeitado por baixa padronização e baixa correlação.

### Ferramenta proprietária única

Rejeitada para evitar lock-in e preservar portabilidade.

## Decisão Final

Usar OpenTelemetry como base de observabilidade, complementado por eventos Kafka para auditoria, FinOps e avaliação assíncrona.
