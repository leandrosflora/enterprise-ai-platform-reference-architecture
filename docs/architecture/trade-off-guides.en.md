# Trade-off Guides

Guidelines for supporting decisions. They are not universal rules; choice should consider risk, volume, latitude, cost, knowledge mutability and operational capacity.

## RAG × Fine-tuning × Long Context

| Criteria | RAG | Fine-tuning | Long Context |
|---|---|---|---|
| Knowledge changes frequently | Better option | Fraco | Suitable at low volume |
| Citations and rastreability | Forte | Fraco | Method |
| Personalizar estilo/comportamento | Method | Forte | Method |
| Custo operacional | Index + retrieval | treino + hosting | tokens elevados |
| Source government | Forte | hard to remove fats | Depending on the context sent |

**Pathoro:** start with prompt + RAG; use fine-tuning to behave completely repeatable; use long context for small and controlled groups.

## MCP × REST × Event-Driven

| Criteria | MCP | REST | Eventos |
|---|---|---|---|
| Tool calling by agents | Forte | exige adapter | unadjusted for immediate response |
| APIs of field | Method | Forte | Method |
| Long-term processes | Method | polling/callback | Forte |
| Contract discovery | nativa | OpenAPI | AsyncAPI/catalog |
| Desacoplamento temporal | Fraco | Fraco | Forte |

**Pathron:** MCP on the agent interface, REST in the field and events for assembly integration and business activities.

## Multi-Agent × Workflow × Single Agent

| Opt | Use when | Hold on when |
|---|---|---|
| Single Agent | escopo limitado, poucas ferramentas | complex coordination and high risk |
| Workflow | knowledge, gates and forecast | problema realmente aberto |
| Multi-Agent | Autônomal specialisations are gaining a little shit | only for organograms |

**Pathoro:** single agent first; workflow when there is process; multi-agent only after evidence of gain.

## Syncroons  assyncroons

- **Syncron:** short-term interactions, forecast readiness, response needed to the canal.
- **Assembly:** long-term, fan-out, retries, human approval or lot processing.
- For long-term operations, re-torn `202 Accepted`, `operationId` and endpoint/eventh of status.

## Graph DB × Vector DB × SQL

| Banco | Better for | Don't use as a padrister for a shit. |
|---|---|---|
| Vector DB | symbiosis and retrieval similarity | Exact transactions and relations |
| Graph DB | deep and thorny relationships | simples lookup documental |
| SQL | estado transacional, auditoria, metadados | - a saline search without veterinary extension |

**Pathron:** SQL as a register, vector index for retrieval and graph only when traces are central.