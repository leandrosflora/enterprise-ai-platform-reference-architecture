# ADR-001: Estratégia de Agent Runtime

## Status

Aceito

## Contexto

A plataforma precisa executar agentes corporativos com integração a modelos, memória, RAG, ferramentas via MCP, avaliação e observabilidade.

A decisão não deve prender a arquitetura a um único framework, pois o ecossistema de agentes muda rapidamente.

## Decisão

Adotar um Agent Runtime com núcleo próprio e adaptadores para frameworks de orquestração.

O runtime deve expor contratos internos estáveis e permitir integração com:

- LangGraph
- Semantic Kernel
- Bedrock Agents
- Implementações customizadas em .NET

## Consequências Positivas

- Reduz acoplamento com frameworks específicos
- Permite troca gradual de tecnologia
- Facilita padronização de auditoria, segurança e FinOps
- Centraliza observabilidade e política de execução

## Consequências Negativas

- Aumenta complexidade inicial
- Exige camada de abstração bem definida
- Pode limitar uso de recursos muito específicos de cada framework

## Alternativas Consideradas

### Framework único

Rejeitado por risco de lock-in e baixa flexibilidade.

### Cada time escolhe seu runtime

Rejeitado por dispersar governança, observabilidade e custos.

## Decisão Final

Criar um Agent Runtime corporativo com adaptadores para frameworks e provedores, mantendo o controle centralizado de execução, políticas, auditoria e eventos.
