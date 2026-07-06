# ADR-005: Estratégia de Avaliação de IA

## Status

Aceito

## Contexto

Agentes corporativos precisam ser avaliados continuamente para reduzir riscos de alucinação, baixa relevância, respostas inseguras e regressões de qualidade.

A avaliação deve ser usada tanto no processo de governança quanto na operação contínua.

## Decisão

Criar um Evaluation Service responsável por avaliações automáticas, regressivas e operacionais.

Critérios iniciais:

- Groundedness
- Relevância
- Hallucination Detection
- Toxicidade
- Segurança da resposta
- Aderência a políticas
- Latência
- Custo

## Consequências Positivas

- Melhora qualidade de agentes publicados
- Cria evidência para governança
- Permite comparação entre versões
- Reduz risco operacional
- Suporta testes de regressão

## Consequências Negativas

- Aumenta custo por execução quando avaliação é síncrona
- Exige datasets de avaliação por domínio
- Pode demandar revisão humana em cenários críticos

## Alternativas Consideradas

### Avaliação apenas manual

Rejeitada por não escalar.

### Avaliação apenas em produção

Rejeitada por aumentar risco de publicação sem controle prévio.

## Decisão Final

Implementar avaliação híbrida: automática para escala, humana para casos críticos e regressiva para versionamento de agentes.
