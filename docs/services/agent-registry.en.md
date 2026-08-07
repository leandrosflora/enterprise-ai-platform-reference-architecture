# Agent Registry

## Responsabilidades

- Catalogue of officials
- Versionamento
- Publication
- Metadados
- Ownership

## Storage Data

- Nome
- Version
- Owner
- Tags
- Status
- Dependencies

## APIs

POST /agents
GET /agents
GET /agents/{id}
POST /agents/{id}/publish

## Events

- agent.created
- agent.updated
- agent.published
- agent.retired
