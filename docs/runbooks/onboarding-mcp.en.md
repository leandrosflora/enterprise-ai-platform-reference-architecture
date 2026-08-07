# Runbook — Onboarding of MCP Server and Tool

## Objet

Register and release a MCP tool with contract, authenticity, authorisation, idempotence, audit and rollback defined.

## Pre-requisites

- technical and business owner;
- the environment of testing;
- authentication by identity workload;
- OpenAPI or the contract of the destination system;
- data classification;
- definition of reading or writing;
- runbook of the corporative system.

## Procedimento

### 1. Classifying the tool

Documentar:

- finalidade;
- efeitos colaterais;
- systems and accessable data;
- risco `LOW`, `MEDIUM`, `HIGH` ou `CRITICAL`;
- the need for human approval;
- Timeout and competition limit.

### 2. define the contract

Thank you:

- name and version SemVer;
- JSON Schema entry and exit;
- compulsory fields and limits;
- state errors codes;
- idempotence policy;
- escopos;
- examples of examples of examples of examples of examples of examples of examples of examples of examples of examples of examples of examples of examples of examples of examples of examples of examples of examples of examples of examples of examples of examples of examples of examples of examples of examples of examples of examples of examples of examples of examples of examples of examples of examples of examples of examples of examples of examples of examples of examples of examples of examples of examples of examples of examples of examples of examples of examples of examples of examples of examples of examples of examples of examples of examples of examples of examples

### 3. Implement checks

- server-side validation of all arguments;
- a letting of operations;
- authorisation in the destination system, not just in Runtime;
- secret manager;
- timeout, circuit breaker e bulkhead;
- key idempotency for writing;
- logs network;
- reversible operation or compensation when possible.

### 4. Testar

Minimum:

- a liquid entry;
- a slick and infusing field;
- identity without a splinter;
- acesso cross-tenant;
- timeout of destination;
- repeating with same key idempotency;
- a quick/tool injection attempt;
- falha parcial;
- rollback or compensation.

### 5. Register at MCP Registry

Registrating contract, owner, risk, endpoint, workload identity, SLO and evidence.

**Sea-down certificate:** status `SUBMITTED`, never available for a product discovery.

### 6. Aprovar

- valid security, authenticity, egress and secrets;
- LGPD valid finality and minimisation when applicable;
- AI Architect valids the esthetic and uses by agents;
- owner of the valid destination system, capacity and rollback.

### 7. Publicar e vincular

The publication makes the available version only for explicitly authorized agents.

### 8. Smoke test

- descoberta autorizada funciona;
- discovery not authorized retornation of liquid or negation;
- implementation gen `tool.executed`;
- trace contains tool, version, status and operation ID;
- idempotent repeat not double effect;
- Methods and alerts are active.

## Rollback

1. removing the version of the discovery;
2. block implementation in enforcement policy;
3. keep the previous version when safe;
4. compensating short-term operations when applicable;
5. preservar auditoria;
6. notified owners of the consumer agents.

## Immediately rejection criteria

- secret on the contract or code;
- authorisation only in the prompt;
- written without idempotence;
- absence of timeout;
- open, unjustified schema;
- a generic tool that allows to execute arbitrarily commands;
- - No owner or rollback.
