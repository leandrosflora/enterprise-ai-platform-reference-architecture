# Data Stores

| Office | Banco | Purpose |
|---|---|---|
| Agent Registry | PostgreSQL | Half-data and versions |
| Governance Service | PostgreSQL | Approvals and risks |
| Billing Service | PostgreSQL | Costs and chargeback |
| Memory Service | MongoDB | Conversational memory |
| Knowledge Service | OpenSearch | Vector search |
| Agent Gateway | Redis | Cache and rate limiting |
| Platform Events | Kafka | Asynchronous integration |

## Principles

- Service ownership
- No direct access between banks
- Integration through PIAs and events
- Auditable data
- Rest chronography
