# ADR-005 — Veterinary and hybrid procurement strategy

**Status:** Aceito

## Contexto

The platform needs to support syringe and hybrid bust for RAG corporative cameras, preserving filters by metadating, isolating by tenant, authorisation by document and operation in a solitary place.

## Decision

Adopt **OpenSearch as initial reference implementation** for veterinary and hybrid search, only available by means of Knowledge Service.

The excavation must maintain an index and retrieval abbreviation to allow other mechanisms when data requirements, cost, scale or availability justify the exchange.

## Obligatory requirements

- veterinary, textual and hybrid search;
- server-side filter by tenant, classification, ACL, finality and retention;
- version of the embedding and index model;
- equivalentaliases or mechanism for promotion and rollback;
- excluding the verification by `documentId` and `tenantId`;
- a lattice, recall, cost and filtered results;
- idempotent reindexation and without avoidable indisponibility.

## Alternativas

| Alternativa | Vantagem | Limitation |
|---|---|---|
| OpenSearch | hybrid, filtres and operational maturity | you need tuning and you can have a relevant cost. |
| pgvector | simplicity and proximity with relational data |  less specialization for large-scale hybrid search |
| MongoDB Vector Search | integration with documents and memory | acopla retrieval ao datastore operacional |
| Vector database especializado | advanced railway resources | Additional dependencies, costs and own government |

## Positive consequences

- reduce the initial quantity of special components;
- allowing textual and veterinary use in the same mechanism;
- approves filter, aliases and operating practices;
- Keep the decision reversed by means of Knowledge Service.

## Negative consequences

- OpenSearch may not be the best option for all workloads;
- tuning of indexes, shards, refresh and embeddings requires special ability;
- excess absorption may hide useful resources from the mechanism;
- Migration requires reindexation and quality validation.

## Minimum evidence

- benchmark with representative dataset;
- recall, precision, MRR or nDCG methods in accordance with the case;
- isolation test and negated access;
- version and rollback plan of the index;
- estimated cost and observed by volume;
- Exclusion and reindexation procedure.

## Review criteria

Review when quality, scale, cost, filter requirements or data retention are not to be notified, or when another mechanism shows a significant gain without reducing governance and portability.
