# Runbook — Onboarding and Agent Publication

## Objet

Publication of a contract-based agent version with risk, security, assessment, observation, budget and rollback valid.

## Pre-requisites

- technical owner and business owner defined;
- Agent Card versionado;
- sample of the approved assessment;
- knowledge bases and tools already registered;
- budget and cost centre defined;
- access `agent.write`, `governance.submit` and test permits.

## Procedimento

### 1. Validate Agent Card

Thank you:

- `agentId`, name and version SemVer;
- owner and business unit;
- purpose, users and data used;
- risco inicial;
- model policy by capacity, without proof of proof;
- tools e knowledge bases permitidas;
- workload class and SLO;
- Memory policy.

**Sea-down:** variable schema and no unlocked field.

### 2. Register the version in DRAFT

```bash
curl -sS -X POST http://localhost:8080/v1/agents \
  -H 'Content-Type: application/json' \
  -H 'Idempotency-Key: policy-assistant-1.0.0-create' \
  -d @agent-card.json
```

**Esperado:** HTTP `201`, status `DRAFT` e `ETag`.

### 3. Validating dependencies

- all MCP contracts are approved;
- KBs apply ACL for document/chunk;
- models requested are in the Model Catalog;
- secrets and regions are approved;
- - The `deny by default` policy was exercised.

### 4. Execute evaluations

Executar ao menos:

- regression;
- groundedness/retrieval when there is RAG;
- safety/adversarial;
- the latability of the workload class;
- Cost for a moment.

**Sea-down report:** reductive report and thresholds reached.

### 5. Validation of observation

Execute an invocation in the test environment and confirm:

- trace completo;
- policy decision and version;
- tokens e custo;
- events `agent.invoked` and dependents;
- - No sense of a sensible payload in logs.

### 6. Submit for government

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

### 7. Accept with a function separation

The identity that you submitted cannot be adopted.

**Early:** decision `APPROVED`, with `approvalId` and auditorium.

### 8. Publicar

```bash
curl -sS -X POST http://localhost:8080/v1/agents/policy-assistant:publish \
  -H 'Content-Type: application/json' \
  -H 'Idempotency-Key: policy-assistant-1.0.0-publish' \
  -d '{"approvalId":"apv-001","releaseNotes":"Primeira versão"}'
```

**Esperado:** HTTP `202`, status `PUBLISHED` e evento `agent.published`.

### 9. Smoke test

- authorized re-representation `SUCCESS` or `PARTIAL` inserted;
- a voice without a re-torning esophagus `403`;
- not allowed re-torning `BLOCKED`;
- dashboard shows lativity, tokens and cost;
- Test alerts come to the right channel.

## Rollback

1. blocking new voices in the version;
2. restoring the previously published version;
3. invalidate the configuration cache and policies;
4. desabilitar tools afetadas;
5. to preserve events, trace and evidence;
6. abrir incidente e registrar causa.

## Erros comuns

| Sintoma | Provisible cause | Action |
|---|---|---|
| `409 Conflict` | version or idempotency key already used | Consult state before repeat |
| `422 Policy Violation` | evidence, budget or absence of dependence | - Correct the gate indicated |
| approved agent not published | approval ID does not correspond to the version |  Refresh the publication with the correct decision |
| `BLOCKED` in the voice | policy bundle ausente ou desatualizado | validating distribution and version of the policy |
