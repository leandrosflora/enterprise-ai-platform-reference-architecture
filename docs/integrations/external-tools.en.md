# External Tools Integration

## Objetivo

Definir critérios para uso de ferramentas externas por agentes e serviços da plataforma.

## Tipos de Ferramentas

- SaaS APIs
- Search APIs
- Document Processing APIs
- OCR Services
- Communication Channels
- Ticketing Tools

## Critérios de Aprovação

| Critério | Descrição |
|---|---|
| Segurança | Autenticação, autorização e gestão de segredos |
| Dados | Classificação e localização dos dados |
| LGPD | Base legal, retenção e compartilhamento |
| Custo | Modelo de cobrança e previsibilidade |
| SLA | Disponibilidade e suporte |

## Padrões

- Preferir integração via MCP Server controlado
- Não expor segredos para agentes
- Registrar todos os tool calls
- Aplicar rate limiting
- Definir fallback para indisponibilidade

## Requisitos

- Aprovação de governança para ferramentas críticas
- Contrato versionado
- Observabilidade por chamada externa
- Plano de descontinuação
