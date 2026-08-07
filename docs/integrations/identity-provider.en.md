# Identity Provider Integration

## Objective

Integrate the platform with the corporate identity provider for authentication, authorisation and audit.

## Standards

- OIDC
- OAuth2
- JWT
- Service-to-service authentication

## Compatible providers

- Microsoft Entra ID
- Okta
- Keycloak
- Auth0

## Flows

| Flow | Uso |
|---|---|
| Authorization Code | Users on the AI Portal |
| Client Credentials | Communication between services |
| Token Exchange | Controlled delegation to tools |

## Claims Relevantes

- subject
- tenant
- businessUnit
- roles
- scopes
- groups

## Requirements

- Validation of the token in Agent Gateway
- Propagation of identity for audit
- Scope control by agent, tool and knowledge base
