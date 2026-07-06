# Memory Service

## Responsabilidades

- Session Memory
- Short-Term Memory
- Long-Term Memory
- User Profile Memory

## Armazenamento

MongoDB

## APIs

GET /sessions/{sessionId}/memory
POST /sessions/{sessionId}/memory

## Eventos

- memory.updated

## Requisitos

- Persistência contextual
- Expiração configurável
- Isolamento por tenant
- Criptografia de dados
