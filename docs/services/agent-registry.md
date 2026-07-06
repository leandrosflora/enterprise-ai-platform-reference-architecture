# Agent Registry

## Responsabilidades

- Catálogo de agentes
- Versionamento
- Publicação
- Metadados
- Ownership

## Dados Armazenados

- Nome
- Versão
- Owner
- Tags
- Status
- Dependências

## APIs

POST /agents
GET /agents
GET /agents/{id}
POST /agents/{id}/publish

## Eventos

- agent.created
- agent.updated
- agent.published
- agent.retired
