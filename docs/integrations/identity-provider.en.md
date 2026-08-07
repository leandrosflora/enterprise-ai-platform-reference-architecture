# Identity Provider Integration

## Objective

To integrate the platform to the corporate identity provider for authentication, authorization and audit.

## Standards

- OIDC
- OAuth2
- JWT
- Service-to-service authentication

## Compatible Ombudsmen

- Microsoft Entra ID
- Okta
- Keycloak
- Auth0

## Flows

| Flow | Uso |
|---|---|
| Authorization Code | Users of the UA Portal |
| Client Credentials | Communication between services |
| Token Exchange | Controlled delegation for tools |

## Claims Relevantes

- subject
- tenant
- businessUnit
- roles
- scopes
- groups

## Requirements

- Validation of token in the Agent Gateway
- Identity propagation for audit
- Scope control by agent, tool and base knowledge
