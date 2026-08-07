# Control Plan and Date Plan

## Decision

The platform separates **Management and governance** of **online execution**.

- The **control plane** it administers metadata, policies, versions, approvals and evidence.
- The **Date planned** it performs invocations, recovery, memory, models and tools under published policies.

This separation reduces the blast radius, allows scaling each plan independently and prevents administrative unavailability from interrupting published workloads.

## Control plane

| Capacity | Responsabilidade |
|---|---|
| Agent Registry | Half-data, immutable versions and life cycle status. |
| Governance Service | Workflow, segregation of functions and evidence. |
| Evaluation Service | Datasets, baselines, thresholds and reports. |
| MCP Registry | Catalogue and approved versions of tools. |
| Policy Administration Point | Authorship, review and publication of policies. |
| Model Catalog | Allowlist of models, regions, capacities and constraints. |
| FinOps Administration | Budgets, quotas and cost allocation rules. |

## Data plane

| Capacity | Responsabilidade |
|---|---|
| Agent Gateway | Authentication, initial authorisation, rate limit and routing. |
| Agent Runtime | Orchestration of the execution of the agent. |
| Policy Enforcement Points | Local implementation of decisions in Gateway, Runtime, Knowledge and MCP. |
| Policy Decision Point | Policy decision with low latency and controlled cache. |
| Knowledge Service | Retrieval with authorization filters per document and chunk. |
| Memory Service | Session memory and profile with TTL, consent and discard. |
| Model Gateway | Roteling, guardrails, quotas, fallback and telemetry of models. |
| MCP Execution | Implementation of tools with allowance, improperty and audit. |

## Flow of publication

1. The deloper creates an immutable version of the agent.
2. Contracts, datesets, budgets and policies are validated.
3. Governance Service records decisions and evidence.
4. The approved policies are published in the Policy Decision Point.
5. Agent Registry changes the version to `PUBLISHED`.
6. The date plan shall accept the invocations of this version.

## Invoking flow

1. Agent Gateway validates identity, tenant, scope and consumption limit.
2. Runtime carries only one version `PUBLISHED`.
3. Policy Decision Point assesses agent, user, tool, data and risk.
4. Knowledge, Memory, Model Gateway and MCP apply local enforcement.
5. Events and traces record decisions, costs and results.

## Disponibilidade

The date plane does not depend on synchronous calls to the control plane during each invocation. Publication settings and policies are distributed and stored in cache with:

- version and checksum;
- Explicit TTL;
- invalidation by event;
- fallback to the latest valid policy;
- comportamento `deny by default` when there is no applicable policy.

## Isolamento

- namespaces and service accounts separated by plane;
- metadata banks are not accessed directly by the data plane;
- network policies restrict lateral communication;
- workload identities use minimum privilege;
- administrative operations require MFA and function segregation.
