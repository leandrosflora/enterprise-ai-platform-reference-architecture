# Trade-off Guides

Guias para apoiar decisões. Não são regras universais; a escolha deve considerar risco, volume, latência, custo, mutabilidade do conhecimento e capacidade operacional.

## RAG × Fine-tuning × Long Context

| Critério | RAG | Fine-tuning | Long Context |
|---|---|---|---|
| Conhecimento muda com frequência | Melhor opção | Fraco | Adequado em baixo volume |
| Citações e rastreabilidade | Forte | Fraco | Médio |
| Personalizar estilo/comportamento | Médio | Forte | Médio |
| Custo operacional | índice + retrieval | treino + hosting | tokens elevados |
| Governança de fontes | Forte | difícil remover fatos | depende do contexto enviado |

**Padrão:** começar com prompt + RAG; usar fine-tuning para comportamento comprovadamente repetitivo; usar long context para conjuntos pequenos e controlados.

## MCP × REST × Event-Driven

| Critério | MCP | REST | Eventos |
|---|---|---|---|
| Tool calling por agentes | Forte | exige adapter | inadequado para resposta imediata |
| APIs de domínio | Médio | Forte | Médio |
| Processos longos | Médio | polling/callback | Forte |
| Descoberta de contratos | nativa | OpenAPI | AsyncAPI/catalog |
| Desacoplamento temporal | Fraco | Fraco | Forte |

**Padrão:** MCP na interface do agente, REST no domínio e eventos para integração assíncrona e fatos de negócio.

## Multi-Agent × Workflow × Single Agent

| Opção | Use quando | Evite quando |
|---|---|---|
| Single Agent | escopo limitado, poucas ferramentas | coordenação complexa e alto risco |
| Workflow | sequência conhecida, gates e previsibilidade | problema realmente aberto |
| Multi-Agent | especializações autônomas trazem ganho mensurável | apenas para simular organogramas |

**Padrão:** single agent primeiro; workflow quando há processo; multi-agent somente após evidência de ganho.

## Agentes síncronos × assíncronos

- **Síncrono:** interações curtas, latência previsível, resposta necessária ao canal.
- **Assíncrono:** tarefas longas, fan-out, retries, aprovação humana ou processamento em lote.
- Para operações longas, retornar `202 Accepted`, `operationId` e endpoint/evento de status.

## Graph DB × Vector DB × SQL

| Banco | Melhor para | Não usar como padrão para |
|---|---|---|
| Vector DB | similaridade semântica e retrieval | transações e relacionamentos exatos |
| Graph DB | relações profundas e travessias | simples lookup documental |
| SQL | estado transacional, auditoria, metadados | busca semântica sem extensão vetorial |

**Padrão:** SQL como sistema de registro, vector index para retrieval e graph apenas quando travessias forem requisito central.