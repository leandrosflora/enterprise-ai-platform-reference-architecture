# ADR-002: Seleção de Banco Vetorial

## Status

Aceito

## Contexto

A plataforma precisa suportar busca semântica e híbrida para cenários de RAG corporativo.

Os principais requisitos são:

- Busca vetorial
- Busca textual
- Filtros por metadados
- Escalabilidade
- Operação gerenciada
- Integração com observabilidade e segurança

## Decisão

Adotar OpenSearch como mecanismo de busca vetorial e híbrida inicial.

## Consequências Positivas

- Suporta busca vetorial e textual no mesmo mecanismo
- Facilita filtros por metadados
- Possui maturidade operacional
- Reduz quantidade de componentes especializados
- Boa aderência para workloads corporativos

## Consequências Negativas

- Pode não ser o melhor mecanismo para todos os cenários vetoriais avançados
- Requer tuning de índices, shards e estratégia de embeddings
- Pode ter custo relevante em alto volume

## Alternativas Consideradas

### Pinecone

Boa opção especializada, mas aumenta dependência externa e custo.

### pgvector

Boa opção para simplicidade, mas menos indicada para escala e busca híbrida avançada.

### MongoDB Vector Search

Boa opção quando memória e documentos já estão em MongoDB, mas não será o mecanismo principal inicial.

## Decisão Final

Utilizar OpenSearch como vector store principal da plataforma, mantendo possibilidade de adaptadores para outros mecanismos conforme domínio, custo e necessidade técnica.
