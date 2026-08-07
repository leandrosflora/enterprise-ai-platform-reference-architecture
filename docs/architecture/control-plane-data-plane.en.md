# Control Planeand Data Plane

## Decision

The platform separates management and governance from online execution.

- The control plane** manages metadata, policies, versions, approvals and evidence.
- The data plane** executes invocations, recovery, memory, templates and tools under published policies.

This separation reduces the blast radius, allows each plane to be scaled independently and prevents administrative unavailabilities from disrupting already published workloads.

## Control plane

| Capacity | Responsabilidade |
|---|---|
| Agent Registry | Metadata, unchanged versions and life cycle status. |
| Governance Service | Workflow, segregation of functions and evidence. |
| Evaluation Service | Data sets, baselines, thresholds and reports. |
| MCP Registry | Catalogue and approved versions of tools. |
| Policy Administration Point | Author, review and publication of policies. |
| Model Catalog | Allowlist of models, regions, capabilities and restrictions. |
| FinOps Administration | Budgets, quotas and cost allocation rules. |

## Data plane

| Capacity | Responsabilidade |
|---|---|
| Agent Gateway | Authentication, initial authorization, rate limit and routing. |
| Agent Runtime | Orchestration of the execution of the agent. |
| Policy Enforcement Points | Local decision-making in Gateway, Runtime, Knowledge and MCP. |
| Policy Decision Point | Policy decision with low latency and cached control. |
| Knowledge Service | Retrieval with authorization filters by document and chunk. |
| Memory Service | Session memory and TTL profile, consent and discard. |
| Model Gateway | Routing, guardrails, quotas, fallback and model telemetry. |
| MCP Execution | Implementing tools with allowlist, idempotence and audit. |

## Flow of publication

1. The developer creates an unchanging version of the agent.
2. Contracts, datasets, budgets and policies are validated.
3. Governance Service records the decisions and evidence.
4. Approved policies are published in the Policy Decision Point.
5. Agent Registry changes the version to `PUBLISHED`
6. data plane is now accepting claims for this version.

## Invocation flow

1. Agent Gateway validates identity, tenant, scope and limit of consumption.
2. Runtime only carries one version of `PUBLISHED`.
3. Policy Decision Point assesses agent, user, tool, data and risk.
4. Knowledge, Memory, Model Gateway and MCP apply local enforcement.
5. Events and traces record decisions, cost and outcome.

## Disponibilidade

data plane is not dependent on calls synchronized to control plane during each call. Published settings and policies are distributed and cached with:

- version and checksum;
- the TTL explicitly;
- invalidation by event;
- fallback to the last valid policy;
- `deny by default` behaviour where there is no applicable policy.

## Isolamento

- plan separate namespaces and service accounts;
- the metadata banks are not directly accessed by the data plane;
- network policies restrict lateral communication;
- workload identities use minimum privilege;
- administrative operations require MFA and segregation of functions.
