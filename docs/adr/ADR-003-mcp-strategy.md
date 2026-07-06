# ADR-003: Estratégia de Integração via MCP

## Status

Aceito

## Contexto

Agentes precisam executar ações em sistemas corporativos sem criar integrações ponto a ponto frágeis e sem governança.

A plataforma precisa padronizar descoberta, autorização, versionamento e auditoria de ferramentas.

## Decisão

Adotar MCP como padrão de exposição e consumo de ferramentas corporativas para agentes.

A plataforma terá um MCP Registry para catálogo, descoberta, versionamento e políticas de uso.

## Consequências Positivas

- Padroniza integração entre agentes e ferramentas
- Reduz acoplamento entre Agent Runtime e sistemas corporativos
- Permite governança por ferramenta
- Facilita auditoria de tool calls
- Ajuda na reutilização entre agentes

## Consequências Negativas

- Exige maturidade operacional dos MCP Servers
- Requer políticas fortes de autenticação e autorização
- Pode adicionar latência nas chamadas

## Alternativas Consideradas

### Integração direta por API

Rejeitada como padrão principal por aumentar acoplamento e dispersar governança.

### Plugins específicos por agente

Rejeitados por baixa reutilização e difícil auditoria.

## Decisão Final

Utilizar MCP como camada padrão de tools para agentes, com catálogo central, políticas, versionamento, auditoria e integração com o Agent Runtime.
