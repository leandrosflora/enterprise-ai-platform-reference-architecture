# Runbook  Onboarding of MCP Server and Tool

## Objective

Register and release a MCP tool with defined contract, authentication, authorisation, idempotence, audit and rollback.

## Pre-requisites

- technical and business owner;
- the test environment;
- the workload identity authentication;
- OpenAPI or the destination system contract;
- the classification of data;
- the definition of reading or writing;
- runbook of the corporate system.

## Procedimento

### 1. Classification of the tool

Documentar:

- finalidade;
- efeitos colaterais;
- systems and data accessed;
- risco `LOW`, `MEDIUM`, `HIGH` ou `CRITICAL`;
- the need for human approval;
- timeout and limit of competition.

### 2. Defining the contract

This is mandatory:

- name and version of SemView;
- JSON Entry and exit scheme;
- compulsory fields and limits;
- stable error codes;
- the policy of impotence;
- escopos;
- valid and invalid examples.

### Implementing controls

- the server-side validation of all arguments;
- allowlist of operations;
- authorisation in the destination system, not only in Runtime;
- secret manager;
- timeout, circuit breaker and bulkhead;
- idempotency key for writing;
- the redaction of logs;
- reverse operation or compensation where possible.

### 4. Testar

Minimum cases:

- valid entry;
- missing field and invalid format;
- identity without scope;
- acesso cross-tenant;
- timeout from destination;
- repeat with the same idempotency key;
- the prompt/tool injection attempt;
- falha parcial;
- rollback or compensation.

### Registration at the MCP Registry

Register contract, owner, risk, endpoint, workload identity, SLO and evidence.

**Exit criterion:** status `SUBMITTED`, never available for productive discovery.

### 6. Aprovar

- Security validates authentication, exit and secrecy;
- LGPD validates purpose and minimization where applicable;
- AI Architect validates scope and use by agents;
- owner of the destination system validates capacity and rollback.

### 7. Publish and link

The publication makes the version uncoverable only to explicitly authorized agents.

### 8. Smoke test

- descoberta autorizada funciona;
- unauthorised discovery returns empty or denied;
- the execution generates `tool.executed`;
- trace contains tool, version, status and operation ID;
- idempotent repetition does not duplicate effect;
- Metrics and alerts are active.

## Rollback

1. remove the version of the discovery;
2. block execution in policy enforcement;
3. maintain the previous version when closed;
4. to offset outstanding transactions where applicable;
5. preservar auditoria;
6. notify the owners of the consumer agents.

## Criteria for immediate rejection

- secret in the contract or code;
- authorisation only on the prompt;
- written without idempotence;
- absence of timeout;
- Open scheme without justification;
- a generic tool that enables the execution of arbitrary commands;
- No owner or rollback.
