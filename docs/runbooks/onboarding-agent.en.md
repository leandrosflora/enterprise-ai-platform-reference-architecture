# Runbook — Onboarding and Agent Publication

## Objective

Publish a version of an agent with validated contracts, risk, safety, assessment, observability, budget and rollback.

## Prerequisites

- technical and business owner defined;
- Agent Card versionado;
- dates of approved evaluation;
- knowledge bases and tools already registered;
- budget and cost center defined;
- acesso `agent.write`, `governance.submit` and test permits.

## Procedimento

### 1. Validar o Agent Card

Obligatory:

- `agentId`, name and version Without View;
- owner and business unit;
- objective, users and data used;
- risk;
- model policy for capacity, without credential provider;
- tools e knowledge bases permitidas;
- classe de workload e SLO;
- memory policy.

**Exit criteria:** schema valid and no blocking field absent.

### 2. Register the DRAFT version

```bash
curl -sS -X POST http://localhost:8080/v1/agents \
  -H 'Content-Type: application/json' \
  -H 'Idempotency-Key: policy-assistant-1.0.0-create' \
  -d @agent-card.json
```

**Esperado:** HTTP `201`, status `DRAFT` e `ETag`.

### 3. Validating dependencies

- All MCP contracts are approved;
- KBs aplicam ACL por documento/chunk;
- models requested are in Model Catalog;
- secrets and regions are approved;
- Policy `deny by default` foi exercitada.

### 4. Performing evaluations

Executar ao menos:

- regression;
- groundedness/retrieval quando houver RAG;
- safety/adversarial;
- latency of the workload class;
- cost per scenario.

**Exit criteria:** reproducible report and thresholds achieved.

### 5. Validating observability

Perform an invocation in the test environment and confirm:

- trace completo;
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

**Esperado:** Decision `APPROVED`, com `approvalId` e trilha de auditoria.

### 8. Publicar

```bash
curl -sS -X POST http://localhost:8080/v1/agents/policy-assistant:publish \
  -H 'Content-Type: application/json' \
  -H 'Idempotency-Key: policy-assistant-1.0.0-publish' \
  -d '{"approvalId":"apv-001","releaseNotes":"Primeira versão"}'
```

**Esperado:** HTTP `202`, status `PUBLISHED` e evento `agent.published`.

### 9. Smoke test

- authorised invocation returns `SUCCESS` ou `PARTIAL` esperado;
- scopeless invocation returns `403`;
- return `BLOCKED`;
- dashboard shows latency, tokens and cost;
- alertas de teste chegam ao canal correto.

## Rollback

1. blocking new invocations of the version;
2. restore the previous published version;
3. invalidate cache configuration and policies;
4. desabilitar tools afetadas;
5. preserve events, traces and evidence;
6. abrir incidente e registrar causa.

## Erros comuns

| Sintoma | Probable cause | Action |
|---|---|---|
|  `409 Conflict`  | version or idempotency key already used | check before repeating |
|  `422 Policy Violation`  | evidence, budget or absent dependence | corrigir o gate indicado |
| approved agent does not publish | approval ID does not match the version | re-make the publication with the correct decision |
|  `BLOCKED` in the invocation | policy bundle ausente ou desatualizado | validate distribution and version of the policy |
