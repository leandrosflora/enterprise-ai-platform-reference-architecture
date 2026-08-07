# ADR-002  Persistent memory under explicit criteria

**Status:** Aceito

## Contexto

Memory improves continuity and customization, but increases the risk of privacy, improper retention, contamination among tenants, and use of outdated facts.

## Decision

Adopt three levels:

1. ** shift memory:** context of the request;
2. **session memory:** short TTL in Redis;
3. **permanent memory:** durable storage only for purpose, consent or legal basis, classification, TTL and deletion mechanisms.

Persistent memory is not standard, so the agent should function without it whenever possible.

## Criteria for persistence

- measurable improvement in experience or efficiency;
- data permitted by the policy and LGPD;
- isolation by tenant and identity;
- the provenance, date of update and registered confidence;
- expiry and right of exclusion implemented.

## Consequences

Recovery must filter scope, recentity and purpose; recovered content is unreliable and must not overwrite system policies or instructions.

## Evidence in the case

The conversational case separates active session in Redis and long-term history/memory in MongoDB, allowing different policies of TTL, access and retention.