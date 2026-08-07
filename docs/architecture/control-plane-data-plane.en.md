# Control Plane e Data Plane

## Decision

The template is separate **gest and government**** of online implementation**.

- **control plane** administers metadata, policies, versions, approvals and evidence.
- **data plane** executes invokes, recovery, memory, models and tools under published policies.

This separation reduces the blast radius, allows each plan to be scaled independently and prevents administrative indisponibilities to interrupt workloads already published.

## Control plane

| Capacidade | Responsabilidade |
|---|---|
| Agent Registry | Metadates, imutable versions and state of life cycle. |
| Governance Service | Workflow, separation of functions and evidence. |
| Evaluation Service | Datasets, baselines, thresholds and reports. |
| MCP Registry | Catalog and approved versions of iron. |
| Policy Administration Point | Autorisation, review and publication of policies. |
| Model Catalog | Model allowance, regions, capacities and restrictions. |
| FinOps Administration | Budgets, quotas and cost allocation rules. |

## Data plane

| Capacidade | Responsabilidade |
|---|---|
| Agent Gateway | Autentification, initial authorisation, limit rate and roteament. |
| Agent Runtime | Order of the execution of the agent. |
| Policy Enforcement Points | Local application of decisions in Gateway, Runtime, Knowledge and MCP. |
| Policy Decision Point | Policy decision with low lattice and controlled cache. |
| Knowledge Service | Retrieval with document and chunk permission filters. |
| Memory Service | - The session memory and a link to TTL, consent and discharge. |
| Model Gateway | Rotation, guardrails, quotas, fallback and model telemetry. |
| MCP Execution | Execusion of allowing, idempotence and auditory machinery. |

## Publication flux

1. The developer creates a mutable version of the agent.
2. Contrats, datasets, budgets and policies are valid.
3. Governance Service records the decisions and evidence.
4. The policies adopted are published in the Policy Decision Point.
5. Agent Registry changes the version to `PUBLISHED`.
6. data plane is taking the invitations from that version.

## Voice flux

1. Agent Gateway valid identity, tenant, escopo and consumption limit.
2. Runtime only charges a version `PUBLISHED`.
3. Policy Decision Point assesses agent, user, tool, type and risk.
4. Knowledge, Memory, Model Gateway e MCP aplicam enforcement local.
5. Events and trace records, costs and results.

## Disponibilidade

The data plane does not depend on single names to the control plane during each invitation. Publication and policies are distributed and stored in cache with:

- version and checksum;
- Explanatory TTL;
- invalidation by event;
- fallback to the last viable policy;
- behaviour `deny by default` when there is no applicable policy.

## Isolamento

- namesspaces and service accounts separated by plan;
- metadating banks are not directly accessed by data plane;
- networks policies restrictlateral communication;
- workload identities use minimum privilege;
- Administrative operations require MF and systorage of functions.
