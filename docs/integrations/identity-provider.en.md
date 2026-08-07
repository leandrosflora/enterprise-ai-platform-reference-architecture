# Identity Provider Integration

## Objetivo

Integrar a plataforma ao provedor corporativo de identidade para autenticação, autorização e auditoria.

## Padrões

- OIDC
- OAuth2
- JWT
- Service-to-service authentication

## Provedores Compatíveis

- Microsoft Entra ID
- Okta
- Keycloak
- Auth0

## Fluxos

| Fluxo | Uso |
|---|---|
| Authorization Code | Usuários no AI Portal |
| Client Credentials | Comunicação entre serviços |
| Token Exchange | Delegação controlada para ferramentas |

## Claims Relevantes

- subject
- tenant
- businessUnit
- roles
- scopes
- groups

## Requisitos

- Validação de token no Agent Gateway
- Propagação de identidade para auditoria
- Controle de escopos por agente, tool e knowledge base
