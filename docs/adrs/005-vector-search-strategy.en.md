# ADR-005  Vector and hybrid search strategy

**Status:** Aceito

## Contexto

The platform needs to support semantic and hybrid search for corporate RAG scenarios, preserving metadata filters, tenant isolation, document authorisation and scale operation.

## Decision

Adopt **OpenSearch as the initial reference implementation** for vector and hybrid search, accessed exclusively through Knowledge Service.

The architecture shall maintain index abstraction and retrieval to allow for other mechanisms where domain, cost, scale or data residency requirements justify the exchange.

## Mandatory requirements

- vector, textual and hybrid search;
- server-side filters by tenant, rating, ACL, purpose and retention;
- versioning of the embedding model and index;
- aliases or equivalent mechanism for promotion and rollback;
- the verifiable exclusion by `documentId` and `tenantId`;
- the latency, recall, cost and filtered results telemetry;
- The Commission shall adopt delegated acts in accordance with Article 21 of Regulation (EU) No 182/2011 and in accordance with Article 21 thereof.

## Alternativas

| Alternativa | Vantagem | Limitation |
|---|---|---|
| OpenSearch | Hybrid search, filters and operational maturity | requires tuning and may have a relevant cost |
| pgvector | simplicity and proximity to relational data | less specialization for large-scale hybrid search |
| MongoDB Vector Search | integration with documents and memory | acopla retrieval ao datastore operacional |
| Vector database especializado | Advanced vector resources | Additional dependency, cost and own governance |

## Positive consequences

- reduce the initial quantity of specialised components;
- enables text and vector search on the same mechanism;
- use mature filters, aliases and operational practices;
- maintain the decision reversible through Knowledge Service.

## Negative consequences

- OpenSearch may not be the best option for all workloads;
- tuning of indexes, shards, refresh and embeddings requires specialized capability;
- excessive abstraction may hide useful resources from the mechanism;
- Migration requires re-indexation and quality validation.

## Minimum evidence

- a benchmark with a representative dataset;
- Recall, accuracy, MRR or nDCG metrics as appropriate;
- isolation test and denied access;
- the index versioning and rollback plan;
- estimated and observed cost per volume;
- the exclusion and re-indexation procedure.

## The Commission shall adopt delegated acts in accordance with Article 21 of this Regulation.

Review when quality, scale, cost, filtering requirements or data residency are no longer met, or when another mechanism demonstrates measurable gain without reducing governance and portability.
