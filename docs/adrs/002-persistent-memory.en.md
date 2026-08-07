# ADR-002 — Permanent memory under explanatory criteria

**Status:** Aceito

## Contexto

Memory improves continuity and personalisation, but increases risk of privacy, unfounded retention, contamination between tenants and use of unattended fats.

## Decision

Adopt three levels:

1. **change memory:** context of the requirement;
2. **session memory:** TTL short in Redis;
3. **Remaining memory:** Durable storage only with the following, consent or legal basis, classification, TTL and excluding mechanisms.

The persistent memory is not a pattern, and the agent must work without her when possible.

## Criteria for a persistent

- better measurable experience or effectiveness;
- given by the policy and LGPD;
- isolation by tenant and identity;
- provenance, date of update and registered trust;
- expiration and right to exclude implemented.

## Consequences

The recovery must filter out the esthetic, recognisance and consistency. The recovered content is given as untrustworthy and must not be subject to policy or system instructions.

## Evidence in the case

The conversacional case is active in Redis and historical/long term in MongoDB, allowing distinct TTL policies, access and retention.