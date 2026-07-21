# ADR-001 — MCP para tool calling governado

**Status:** Aceito  
**Contexto:** agentes precisam descobrir e executar ferramentas corporativas com contratos, autorização e auditoria consistentes.

## Decisão

Usar **MCP** na fronteira entre Agent Runtime e ferramentas governadas. APIs REST continuam sendo usadas como interfaces de domínio internas e externas. O MCP não substitui REST; ele adiciona uma camada orientada ao consumo por agentes.

## Por que

- descoberta padronizada de ferramentas e schemas;
- separação entre raciocínio do agente e implementação do domínio;
- enforcement central de identidade, escopo, estágio da jornada e auditoria;
- menor acoplamento entre framework de agentes e serviços corporativos.

## Alternativas

| Alternativa | Vantagem | Limitação |
|---|---|---|
| REST direto | simples e universal | exige adaptação específica em cada agente |
| Eventos | desacoplamento e escala | inadequado para toda interação request/response |
| SDK proprietário | produtividade inicial | lock-in e governança fragmentada |

## Consequências

O Tool Service/MCP Server deve validar identidade, tenant, autorização por ferramenta, idempotência, timeout e correlação. Operações longas devem retornar um identificador e prosseguir de forma assíncrona.

## Evidência no case

O `conversational-ai-demo-arch` aplica MCP no fluxo de renegociação para tool calling governado entre Agent Runtime, Tool Service e serviço de domínio.