# Data Stores

| Serviço | Banco | Finalidade |
|---|---|---|
| Agent Registry | PostgreSQL | Metadados e versões |
| Governance Service | PostgreSQL | Aprovações e riscos |
| Billing Service | PostgreSQL | Custos e chargeback |
| Memory Service | MongoDB | Memória conversacional |
| Knowledge Service | OpenSearch | Busca vetorial |
| Agent Gateway | Redis | Cache e rate limiting |
| Platform Events | Kafka | Integração assíncrona |

## Princípios

- Ownership por serviço
- Sem acesso direto entre bancos
- Integração por APIs e eventos
- Dados auditáveis
- Criptografia em repouso
