# ADR-005 — Vector and hybrid search strategy

**Status:** Aceito

## Context

The platform needs to support semantic and hybrid search for corporate RAG scenarios, preserving metadata filters, tenant isolation, document authorization and scale operation.

## Decision

Adotar **OpenSearch as initial reference implementation** for vector and hybrid search, accessed exclusively through the Knowledge Service.

The architecture must maintain an abstraction of index and retrieval to allow other mechanisms when domain, cost, scale or residence requirements of data justify the exchange.

## Compulsory requirements

- vector, textual and hybrid search;
- server-side filters by tenant, classification, ACL, purpose and retention;
- versioning of the embedding model and the index;
- aliases or equivalent mechanism for promotion and rollback;
- exclusion verifiable by `documentId` e `tenantId`;
- latency telemetry, recall, cost and filtered results;
- indexation is inappropriate and unavailable.

## Alternatives

| Alternativa | Vantagem | Limitation |
|---|---|---|
| OpenSearch | hybrid search, filters and operational maturity | it requires tuning and may have relevant cost |
| pgvector | simplicity and proximity to relational data | less specialization for large-scale hybrid search |
| MongoDB Vector Search | integration with documents and memory | acopla retrieval ao datastore operacional |
| Vector database especializado | Advanced vector resources | Additional dependence, cost and own governance |

## Positive consequences

- reduz a quantidade inicial de componentes especializados;
- permite busca textual e vetorial no mesmo mecanismo;
- takes advantage of filters, aliases and mature operational practices;
- maintains the decision reversible through the Knowledge Service.

## Negative consequences

- OpenSearch may not be the best option for all workloads;
- tuning indexes, shards, refresh and embeddings requires specialized capacity;
- excessive abstraction may hide useful resources of the mechanism;
- migration requires reindexing and quality validation.

## Minimum evidence

- benchmark com dataset representativo;
- recall, precision, MRR or nDCG metrics as appropriate;
- teste de isolamento e acesso negado;
- index versioning plan and rollback;
- estimated cost and observed by volume;
- exclusion and re-indexing procedure.

## Review criteria

To review when quality, scale, cost, filter requirements or data residence are no longer met, or when another mechanism demonstrates measurable gain without reducing governance and portability.
