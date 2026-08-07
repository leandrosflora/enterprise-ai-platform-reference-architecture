# Runbook — Onboarding de MCP Server e Tool

## Objective

Register and release a MCP tool with defined contract, authentication, authorisation, impartiality, audit and rollback.

## Prerequisites

- technical and business owner;
- test environment;
- authentication by workload identity;
- OpenAPI or contract for the destination system;
- Data classification;
- definition of reading or writing;
- runbook corporate system.

## Procedimento

### 1. Classificar a tool

Documentar:

- purpose;
- efeitos colaterais;
- systems and data accessed;
- risk `LOW`, `MEDIUM`, `HIGH` ou `CRITICAL`;
- necessidade de human approval;
- timeout and competition limit.

### 2. Definir o contrato

Obligatory:

- Name and version Without View;
- JSON Entry and Exit Schema;
- mandatory fields and limits;
- stable error codes;
- policy of inequality;
- escopos;
- valid and disabled examples.

### 3. Implementing controls

- server-side validation of all arguments;
- allowance for operations;
- authorisation in the destination system, not only in Runtime;
- secret manager;
- timeout, circuit breaker e bulkhead;
- idempotency key para escrita;
- redaction de logs;
- reversible operation or compensation when possible.

### 4. Testar

Minimum cases:

- valid entry;
- absent field and invalid shape;
- identity without scope;
- acesso cross-tenant;
- timeout do destino;
- repetition with the same idempotency key;
- tentativa de prompt/tool injection;
- falha parcial;
- rollback or compensation

### 5. Registrar no MCP Registry

Register contract, owner, risk, endpoint, workload identity, SLO and evidence.

**Exit criteria:** status `SUBMITTED`, never available for productive discovery.

### 6. Aprovar

- Security validates authentication, egress and secrets;
- LGPD validates purpose and minimization when applicable;
- AI Architect validates scope and use by agents;
- owner of the destination system validates capacity and rollback.

### 7. Publicar e vincular

The publication makes the version uncoverable only for explicitly authorised agents. Do not use wildcard of tool in production.

### 8. Smoke test

- descoberta autorizada funciona;
- unauthorised discovery returns empty or denied;
- implementation generates `tool.executed`;
- trace contains tool, version, status and operation ID;
- unavoidable repetition does not double effect;
- metrics and alerts are active.

## Rollback

1. withdraw the version from the discovery;
2. blocking execution in the policy enforcement;
3. keep the previous version when secure;
4. to compensate for outstanding transactions where applicable;
5. preservar auditoria;
6. notify owners of consumer agents.

## Immediate rejection criteria

- secret the contract or code;
- authorisation only in the prompt;
- writing without inequality;
- no timeout;
- schema aberto sem justificativa;
- generic tool that allows the execution of arbitrary commands;
- no owner or rollback.
