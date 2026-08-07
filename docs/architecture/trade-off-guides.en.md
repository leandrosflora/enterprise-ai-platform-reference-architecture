# Trade-off Guides

Guides to support decisions are not universal rules; the choice should consider risk, volume, latency, cost, knowledge changeability and operational capacity.

## RAG × Fine-tuning × Long Context

| Criteria | RAG | Fine-tuning | Long Context |
|---|---|---|---|
| Knowledge often changes | Best option | weak | Adequado in baixo volume |
| Citations and traceability | Forte | weak | Average |
| Personalizar estilo/comportamento | Average | Forte | Average |
| Operational cost | index + retrieval | treino + hosting | tokens elevados |
| Supply governance | Strong | difficult to remove facts | depends on the context sent |

**Pattern:** start with prompt + RAG; use fine-tuning for proven repetitive behavior; use long context for small and controlled sets.

## MCP × REST × Event-Driven

| Criteria | MCP | REST | Events |
|---|---|---|---|
| Tool calling for agents | Strong | exige adapter | Inappropriate for immediate response |
| Dominant PIAs | Average | Strong | Average |
| Long-term procedures | Average | polling/callback | Forte |
| Discovery of contracts | native | OpenAPI | AsyncAPI/catalog |
| Desacoplamento temporal | weak | weak | Forte |

**Pattern:** PCM at the agent interface, NRS in the domain and events for asynchronous integration and business facts.

## Multi-Agent × Workflow × Single Agent

| Option | Use when | Avoid when |
|---|---|---|
| Single Agent | limited scope, few tools | complex coordination and high risk |
| Workflow | known sequence, gates and predictability | really open problem |
| Multi-Agent | autonomous specialization brings measurable gain in the study of the study. | only to simulate organograms |

**Pattern:** single agent first; workflow when there is process; multi-agent only after evidence of gain.

## Synchronous × asynchronous agents

- **Synchronous:** short interactions, predictable latency, necessary response to the channel.
- **Asynchronous:** long tasks, fan-out, retries, human approval or batch processing.
- For long operations, return `202 Accepted`, `operationId` e endpoint/event of status.

## Graph DB × Vector DB × SQL

| Bank | Better for | Do not use as standard for |
|---|---|---|
| Vector DB | semantic similarity and retrieval | transactions and exact relationships |
| Graph DB | deep relations and crossings | simple document lookup |
| SQL | transactional status, audit, metadata | semantic search without vector extension |

**Pattern:** SQL as a registry system, vector index for retrieval and graph only when crossings are a central requirement.