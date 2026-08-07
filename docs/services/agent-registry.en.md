# Agent Registry

## Responsabilidades

- Catalogue of agents
- Versionamento
- Publication
- Metadados
- Ownership

## Stored data

- Nome
- This is the version.
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
