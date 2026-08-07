# Trade-off Guides

Guidelines for supporting decisions. These are not universal rules; the choice must take into account risk, volume, latency, cost, mutability of knowledge and operational capacity.

## RAG × Fine-tuning × Long Context

| Criterion of use | RAG | Fine-tuning | Long Context |
|---|---|---|---|
| Knowledge changes frequently | Best option | Fraco | Suitable for low volume |
| Citations and traceability | Forte | Fraco | Average |
| Personalizar estilo/comportamento | Average | Forte | Average |
| Custo operacional | index + retrieval | treino + hosting | tokens elevados |
| Governance of sources | Forte | difficult to remove | Depends on the context |

** Pattern:** start with prompt + RAG; use fine-tuning for proven repetitive behavior; use long context for small, controlled sets.

## MCP × REST × Event-Driven

| Criterion of use | MCP | REST | Events |
|---|---|---|---|
| Tool calling by agents | Forte | exige adapter | unsuitable for immediate response |
| APIsof domain | Average | Forte | Average |
| Long-term processes | Average | polling/callback | Forte |
| Discovery of contracts | nativa | OpenAPI | AsyncAPI/catalog |
| Desacoplamento temporal | Fraco | Fraco | Forte |

**Standard:** MCP in the agent interface, REST in the domain and events for asynchronous integration and business facts.

## Multi-Agent × Workflow × Single Agent

| Option | Use when | Avoid when |
|---|---|---|
| Single Agent | escopo limitado, poucas ferramentas | Complex and high risk coordination |
| Workflow | Known sequence, gates and predictability | problema realmente aberto |
| Multi-Agent | Autonomous specialisations bring measurable gains | only to simulate organograms |

**Standard:** single agent first; workflow when there is a process; multi-agent only after evidence of gain.

## Synchronous agents × asynchronous agents

- **Synchronous:** short interactions, predictable latency, required channel response.
- **Asynchronous:** long tasks, fan-out, retries, human approval or batch processing.
- For long operations, return `202 Accepted`, `operationId` and endpoint/event status.

## Graph DB × Vector DB × SQL

| Banco | Better to | Do not use as standard for |
|---|---|---|
| Vector DB | Semantic similarity and retrieval | Exact transactions and relationships |
| Graph DB | deep and transversal relationships | simples lookup documental |
| SQL | The following information is included in the report: | Semantic search without vector extension |

**Fact:** SQL as a recording system, vector index for retrieval and graph only when crossings are a central requirement.