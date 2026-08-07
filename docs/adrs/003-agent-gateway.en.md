# ADR-003 — Agent Gateway como ponto de entrada

**Status:** Aceito

## Contexto

Canais, agentes e provedores de modelos evoluem em ritmos diferentes. Sem uma fronteira comum, autenticação, quotas, roteamento, proteção de dados e telemetria são duplicados.

## Decisão

Introduzir um **Agent Gateway** entre canais/BFFs e runtimes. Ele não contém lógica de negócio nem prompts específicos da jornada.

## Responsabilidades

- autenticação, autorização e resolução de tenant;
- rate limit, quotas e budget enforcement;
- roteamento por agente, versão e capacidade;
- normalização de streaming e respostas assíncronas;
- correlação, tracing, métricas e auditoria;
- políticas de entrada, classificação e mascaramento de dados;
- circuit breaker e fallback controlado.

## Não responsabilidades

- raciocínio do agente;
- execução direta de ferramentas de domínio;
- armazenamento de memória de longo prazo;
- definição de regras de negócio.

## Consequências

O gateway torna-se componente crítico e deve ser stateless, horizontalmente escalável e degradar com segurança. Configurações de agente devem ser versionadas no Control Plane.

## Evidência no case

No case conversacional, o Channel BFF e o Conversation Orchestrator materializam parte dessa fronteira. A evolução recomendada é consolidar políticas comuns sem concentrar a lógica da jornada.