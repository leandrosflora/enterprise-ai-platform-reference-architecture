# Runbook — Onboarding and Agent Publication

## Objective

Publish a version of an agent with validated contracts, risk, safety, assessment, observability, budget and rollback.

## Prerequisites

- technical and business owner defined;
- Agent Card versioned;
- dates of approved evaluation;
- knowledge bases and tools already registered;
- budget and cost center defined;
- acesso `agent.write`, `governance.submit` and test permits.

## Procedimento

### 1. validate the Agent Card

Obligatory:

- `agentId`, name and version Without View;
- owner and business unit;
- objective, users and data used;
- risk;
- model policy for capacity, without credential provider;
- tools and knowledge allowed bases;
- workload class and SLO;
- memory policy.

**Exit criteria:** schema valid and no blocking field absent.

### 2. Register the DRAFT version

```bash
curl -sS -X POST http://localhost:8080/v1/agents \
  -H 'Content-Type: application/json' \
  -H 'Idempotency-Key: policy-assistant-1.0.0-create' \
  -d @agent-card.json
```

**Expected:** HTTP `201`, status `DRAFT` and `ETag`.

### 3. Validating dependencies

- All MCP contracts are approved;
- KBs aplicam ACL by document/chunk;
- models requested are in Model Catalog;
- secrets and regions are approved;
- Policy `deny by default` foi exercitada.

### 4. Performing evaluations

execute to the less:

- regression;
- groundedness/retrieval when there is RAG;
- safety/adversarial;
- latency of the workload class;
- cost per scenario.

**Exit criteria:** reproducible report and thresholds achieved.

### 5. Validating observability

Perform an invocation in the test environment and confirm:

- trace complete;
- policy decision and version;
- tokens and costs;
- events `agent.invoked` and requirements;
- no payload sensitive in logs.

### 6. Submitting for governance

```bash
curl -sS -X POST http://localhost:8080/v1/agents/policy-assistant:submit \
  -H 'Content-Type: application/json' \
  -H 'Idempotency-Key: policy-assistant-1.0.0-submit' \
  -d '{
    "agentVersion":"1.0.0",
    "riskClassification":"MEDIUM",
    "evidence":["evaluation-report.json","authorization-matrix.md","rollback-plan.md"]
  }'
```

**Esperado:** HTTP `202`, Decision `PENDING`.

### 7. Approval with segregation of function

The approver cannot approve the identity that he/she submitted. The approver validates the gates G1–G7.

**Expected:** Decision `APPROVED`, `approvalId` and audit trail.

### 8. Publicar

```bash
curl -sS -X POST http://localhost:8080/v1/agents/policy-assistant:publish \
  -H 'Content-Type: application/json' \
  -H 'Idempotency-Key: policy-assistant-1.0.0-publish' \
  -d '{"approvalId":"apv-001","releaseNotes":"Primeira versão"}'
```

**Expected:** HTTP `202`, status `PUBLISHED` and event `agent.published`.

### 9. Smoke test

- authorised invocation returns `SUCCESS` or `PARTIAL` expected;
- scopeless invocation returns `403`;
- return `BLOCKED`;
- dashboard shows latency, tokens and cost;
- test alerts arrive at the correct channel.

## Rollback

1. blocking new invocations of the version;
2. restore the previous published version;
3. invalidate cache configuration and policies;
4. desabilitar tools afetadas;
5. preserve events, traces and evidence;
6. open incident and register cause.

## Erros comuns

| Sintoma | Probable cause | Action |
|---|---|---|
|  `409 Conflict`  | version or idempotency key already used | check before repeating |
|  `422 Policy Violation`  | evidence, budget or absent dependence | correct the indicated gate |
| approved agent does not publish | approval ID does not match the version | re-make the publication with the correct decision |
|  `BLOCKED` in the invocation | policy bundle ausente ou desatualizado | validate distribution and version of the policy |
