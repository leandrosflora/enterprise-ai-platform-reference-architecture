# ADR-002 — Persistent memory under explicit criteria

**Status:** Aceito

## Context

Memory improves continuity and personalization, but increases the risk of privacy, improper retention, contamination between tenants and use of outdated facts.

## Decision

Adopt three levels:

1. **shift memory:** context of the requisition;
2. **Session memory:** Short TTL in Redis;
3. **Persistent memory:** durable storage only for purpose, consent or legal basis, classification, TTL and exclusion mechanisms.

Persistent memory is not standard, and the agent should work without it when possible.

## Criteria to persist

- measurable improvement of experience or efficiency;
- data allowed by the policy and LGPD;
- isolation by tenant and identity;
- provenance, update date and confidence recorded;
- expiry and exclusion rights implemented.

## Consequences

Retrieval should filter scope, requirement and purpose. Retrieved content is not reliable and should not overwrite system policies or instructions.

## Case evidence

The conversational case separates active session in Redis and long-term history/memory in MongoDB, allowing different TTL, access and retention policies.