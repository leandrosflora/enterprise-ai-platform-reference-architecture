# Runbook  Onboarding and Agent Publishing

## Objective

Publish an agent version with validated contracts, risk, security, valuation, observability, budget and rollback.

## Pre-requisites

- defined technical owner and business owner;
- Agent Card versionado;
- an approved evaluation dataset;
- knowledge bases and tools already registered;
- defined budget and cost centre;
- acesso `agent.write`, `governance.submit`and test permits.

## Procedimento

### Validate the Agent Card

This is mandatory:

- `agentId`, name and version of SemVer;
- owner and business unit;
- the target, users and data used;
- risco inicial;
- capacity model policy, without provider credential;
- tools and knowledge bases permitted;
- the workload class and SLO;
- the memory policy.

**Exit criterion:** Valid scheme and no blocking field missing.

### 2. Record the version in DRAFT

```bash
curl -sS -X POST http://localhost:8080/v1/agents \
  -H 'Content-Type: application/json' \
  -H 'Idempotency-Key: policy-assistant-1.0.0-create' \
  -d @agent-card.json
```

**Expected:** HTTP `201`, status `DRAFT` and `ETag`.

### 3. Validation of dependencies

- all MCP contracts are approved;
- KBs apply ACL per document/chunk;
- the models requested are in the Model Catalogue;
- Secrets and regions are approved;
- The policy of `deny by default` has been implemented.

### 4. carry out assessments

Executar ao menos:

- regression;
- groundedness/retrieval where there is RAG;
- safety/adversarial;
- the latency of the workload class;
- cost per scenario.

**Exit criterion:** Reproducible report and thresholds reached.

### 5. Validate the observability

Run an invocation in a test environment and confirm:

- trace completo;
- policy decision and version;
- tokens and cost;
- Events`agent.invoked`and dependencies;
- No sensitive payload in logs.

### 6. Submitting to governance

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

**Esperado:** HTTP `202`, decision `PENDING`.

### 7. Approval by functional segregation

The identity you submitted cannot be approved.

**Expected:** decision `APPROVED`, with `approvalId` and audit trail.

### 8. Publicar

```bash
curl -sS -X POST http://localhost:8080/v1/agents/policy-assistant:publish \
  -H 'Content-Type: application/json' \
  -H 'Idempotency-Key: policy-assistant-1.0.0-publish' \
  -d '{"approvalId":"apv-001","releaseNotes":"Primeira versão"}'
```

**Expected:** HTTP `202`, status `PUBLISHED` and event `agent.published`.

### 9. Smoke test

- the authorised invocation returns the expected `SUCCESS` or `PARTIAL`;
- the purposeless invocation returns `403`;
- the tool not allowed returns `BLOCKED`;
- dashboard shows latency, tokens and cost;
- Test alerts are coming to the correct channel.

## Rollback

1. block new invocations of the version;
2. restore the previously published version;
3. invalidate the configuration cache and policies;
4. desabilitar tools afetadas;
5. preserve events, traces and evidence;
6. Open an incident and file a lawsuit.

## Erros comuns

| Sintoma | Probable cause | Action |
|---|---|---|
| `409 Conflict` | version or idempotency key already used | Check the status before repeating |
| `422 Policy Violation` | Evidence, budget or dependency absent | correct the indicated gate |
| approved agent not publishing | approval ID does not match the version | Re-publishing with the correct decision |
| `BLOCKED` in the appeal | policy bundle ausente ou desatualizado | validate distribution and policy version |
