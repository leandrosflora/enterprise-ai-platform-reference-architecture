# Data Stores

| Service | Banco | Finalidade |
|---|---|---|
| Agent Registry | PostgreSQL | Metadata and versions |
| Governance Service | PostgreSQL | Approvals and risks |
| Billing Service | PostgreSQL | Costs and chargeback |
| Memory Service | MongoDB | Conversational memory |
| Knowledge Service | OpenSearch | Vector search |
| Agent Gateway | Redis | Cache and rate limiting |
| Platform Events | Kafka | Asynchronous integration |

## Principles

- Ownership by service
- No direct access between banks
- Integration by APIs and events
- Auditable data
- Encryption at rest
