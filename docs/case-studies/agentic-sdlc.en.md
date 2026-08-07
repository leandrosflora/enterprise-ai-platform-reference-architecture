# Case aplicado — Agentic SDLC governado

[ Opening published documentation of Agentic SDLC Reference Architecture](https://leandrosflora.github.io/agentic-sdlc-reference-architecture/){ .md-button .md-button--primary target="_blank" }

This case demonstrates how the capabilities of the Enterprise AI Platform Reference Architecture can be applied to agent-oriented software engineering, covering the flow between demand, architecture, implementation, verification, approval, release, observation and recovery.

The objective is not to build only one agent who writes a code, but the proposal materializes a **sociotechnical system governed**, in which specialist agents produce proposals and evidence, while workflow, policies, quality gates, human approval and execution services keep the authority over real effects.

!!! info "State current"
    The solution has architecture, contracts, golden paths and a shared functional runtime. The environment demonstrates the point-to-point cycle with local adapters, controlled integration with GitHub and supports real Model Gateway and MCP. The P7 controls represent an implantable basis and substitutable adapters, but do not prove corporate productive operation.

## Problema

Code generation tools accelerate only part of the software Development Lifecycle. The main delays and risks remain distributed by:

- incomplete requirements;
- refinamentos e handoffs;
- architectural decisions without traceability;
- implementation outside the approved scope;
- cobertura e testes insuficientes;
- vulnerabilities and unsafe dependencies;
- review without consolidated context;
- uncoupled approvals of the final artifact;
- releases without evidence of observation;
- rollback manual e tardio;
- difficulty to relate requirement, code, test, approval and deploy.

Architecture transforms this flow into a durable, governed and audible journey.

## Jornada aplicada

```text
Epic, requisito ou GitHub Issue
        ↓
Product Agent
        ↓
Architecture Agent
        ↓
Developer Agent
        ↓
Test Agent
        ↓
Security Agent
        ↓
Reviewer Agent
        ↓
Aprovação humana vinculada ao digest
        ↓
Release Agent
        ↓
Deploy em ambiente controlado
        ↓
Observação por SLO e health checks
        ↓
Concluído ou rollback
        ↓
Incident Agent e feedback governado
```

Each step produces structured results, events, checkpoints and one **evidence bundle**. The orchestrator only advances when contracts, policies and gates of the stage are met.

## Specialised staff

| Agent | Responsabilidade principal | Efeito permitido | Limite de autoridade |
|---|---|---|---|
| Product | structuring objective, scope and acceptance criteria | Backlog and requirements | does not alter the code or approve release |
| Architecture | produzir abordagem, C4, ADRs, contratos e impacto | architectural artifacts | does not implement or publish |
| Developer | propose and implement delimited change | branch e draft PR | does not make merge or access production |
| Test | create and carry out verifications | tests and evidence | does not reduce stuttering |
| Security | executar scans e threat analysis | Findings and Evidence | does not silently alter the implementation |
| Reviewer | review quality, scope and evidence | parecer independente | does not implement or publish |
| Release | promover digest autorizado e operar rollback | controlled setting | does not ignore approval or policy |
| Incident | correlating change and telemetry | timeline and remediation proposal | does not perform destructive action without authorisation |

The agents represent logical roles executed by a shared runtime, and they do not need to be eight persistent services.

## Onde a IA participa

AI enters the activities that require interpretation, synthesis, generation and contextual assessment:

### Product Agent

- interprets requirements and Issues;
- identifica lacunas;
- proposes structured acceptance criteria;
- it registers risks and doubts for refinement.

### Architecture Agent

- analyzes context and restrictions;
- proposes decisions and alternatives;
- produces contracts and impact analysis;
- it relates the change with ADRs and existing patterns.

### Developer Agent

- generates a structured proposal for amendment;
- seleciona arquivos permitidos;
- produces code and tests within the scope;
- abre somente draft PR.

### Test e Security Agents

- proposing scenarios and verifications;
- analyze failures, coverage and regressions;
- synthesize security findings;
- they cannot reduce thresholds or remove controls.

### Reviewer e Incident Agents

- consolidate evidence of multiple steps;
- verify adherence to the requirement and architecture;
- correlacionam deploys, logs, traces e incidentes;
- recommend rework, recovery or further investigation.

The response of a model **has no direct authority**. All side effects go through the MCP Gateway, policy enforcement and workflow contracts.

## What remains deterministic

| Responsabilidade | Why should not depend on probabilistic decision |
|---|---|
| state machine | progression, timeout, retry and compensation need to be reproducible |
| policy enforcement | authorisation must be explicit and fail-closed |
| Segregation of functions | author, approver and executor need to be verifiable |
| Human approval | it must refer to identity, decision and exact digest |
| execution of tools | schemas, grants, paths e ambientes devem ser controlados |
| CI quality gates | tests, scans and thresholds need to produce objective results for the study of the study. |
| release | somente o digest aprovado pode ser promovido |
| Impotence | retries cannot double effects |
| observation and rollback | decisions should use health checks and versioned SLOs |
| evidence store | hashes, integrity chain and retention do not depend on the model. |

## Mapeamento para a Enterprise AI Platform

| Platform capacity | Materialisation in Agentic SDLC | Current status |
|---|---|---|
| Agent Gateway | GitHub Issues, PRs, Developer Portal, CI/CD e ChatOps como canais | defined architecture; demonstrated GitHub integrations |
| Agent Runtime | shared runtime with eight declarative definitions | implementado e testado |
| Agent Registry | definitions versioned with prompt, tools, limits and schemes | implementado no runtime e contratos |
| Model Gateway | provider fake deterministic and gateway HTTP OpenAI-compatible | implemented; corporate selection and central governance still evolving |
| MCP Gateway | MCP fake for tests and stdio transport JSON-RPC for real servers | implemented; HTTP/SSE remains evolving |
| Policy Enforcement | grants por papel e OPA no tool loop, remoto ou CLI | implemented; production requires OPA HA and signed bundles |
| Knowledge Service | Context Builder, documents, ADRs, contracts and project memory | baseline implementada; knowledge lifecycle corporativo pendente |
| Memory Service | checkpoints, approved context and historical change | baseline implementada |
| Evaluation Service | testes, scans, schemas, groundedness e quality gates | baseline implemented; continuous evaluation with real models still evolving |
| Governance Service | durable workflow, segregation, approval by digest and policy-as-code | demonstrado localmente |
| Evidence and Audit | evidence bundles write-once, SHA-256 e manifest com hash chain | implementado localmente; storage WORM corporativo pendente |
| Workload Identity | suporte a GitHub OIDC nos adapters P7 | implementado como adapter; trust policies reais pendentes |
| Observability | Correlated events and exporter OTLP HTTP | adapter implementado; backend corporativo e SLOs reais pendentes |
| FinOps | limits per agent and Budget Ledger | implementado como controle; backend compartilhado pendente |
| Supply Chain | Syft, Cosign, digest e manifesto Kubernetes | adapters implementados; registry e admission verification pendentes |
| Sandbox | Docker restrito, sem rede, read-only e limites | demonstrated; outstanding production isolation |
| Event Backbone | events du `change_id`, `project_id` e `agent_run_id`  | database based on archives; managed measurement is evolution |

## Implemented architecture

```mermaid
flowchart TB
    subgraph EXP[Experience and Integration]
      GH[GitHub Issues e PRs]
      PORTAL[Developer Portal]
      CICD[CI/CD]
      CHAT[ChatOps]
    end

    subgraph CP[Agent Control Plane]
      API[Workflow API]
      ORCH[Durable Orchestrator]
      REG[Agent and Tool Registry]
      PDP[OPA Policy Decision Point]
      EVAL[Evaluation Service]
      COST[Budget and Cost Controller]
    end

    subgraph AP[Agent Plane]
      PROD[Product]
      ARCH[Architecture]
      DEV[Developer]
      TEST[Test]
      SEC[Security]
      REV[Reviewer]
      REL[Release]
      INC[Incident]
    end

    subgraph KP[Knowledge and Evidence]
      CTX[Context Builder]
      MEM[(Project Memory)]
      EV[(Evidence Bundles)]
      AUD[(Audit and Traceability)]
      CHK[(Checkpoints)]
    end

    subgraph EP[Execution Plane]
      MODEL[Model Gateway]
      MCP[MCP Gateway]
      SBX[Ephemeral Sandbox]
      TOOLS[Git, CI, Cloud and Observability]
    end

    EXP --> API --> ORCH
    ORCH --> REG
    ORCH --> AP
    ORCH --> PDP
    ORCH --> EVAL
    ORCH --> COST
    AP --> CTX
    AP --> MODEL
    AP --> MCP
    MCP --> PDP
    MCP --> TOOLS
    DEV --> SBX
    TEST --> SBX
    CTX <--> MEM
    ORCH --> EV
    ORCH --> AUD
    ORCH --> CHK
    CICD --> EV
```

The architecture separates five planes:

1. **Experience and Integration:** entry points and registration systems;
2. **Agent Control Plane:** workflow, catalogue, policies, evaluations and budgets;
3. **Agent Plane:** specialized roles with own identities and permissions;
4. **Knowledge and Evidence:** context, memory, checkpoints and traceability;
5. **Execution Plane:** models, MCP, sandboxes and tools with real effect.

## Point to point flow

```mermaid
sequenceDiagram
    actor H as Humano
    participant G as GitHub
    participant O as Orchestrator
    participant A as Agents
    participant P as OPA and MCP
    participant C as CI/CD
    participant D as Demo Environment
    participant T as Telemetry

    H->>G: cria Issue ou requisito
    G->>O: evento autenticado
    O->>A: Product e Architecture
    A->>P: tool calls autorizadas
    P-->>A: decisão e resultado sanitizado
    O->>A: Developer, Test, Security e Reviewer
    A->>G: abre draft PR e publica evidências
    C->>O: testes, scans e artifact digest
    O->>H: solicita aprovação do digest
    H->>O: aprovação segregada
    O->>C: promove exatamente o digest aprovado
    C->>D: deploy controlado
    D->>T: health e SLO signals
    T-->>O: saudável ou violação
    alt saudável
      O->>G: conclui mudança
    else violação
      O->>D: rollback para digest anterior
      O->>G: registra rollback e evidências
    end
```

## Garantias demonstradas

| Aspecto | Garantia atual |
|---|---|
| Workflow | explicit order, persisted states and checkpoints per stage |
| Retomada | completed model response can be reused without further charge or effect |
| Tool use | grants per agent, schemas and policy before execution |
| Context | classification, provenance, redaction, limits and hashes |
| Evidence | arquivos write-once, SHA-256 e manifest append-only com hash chain |
| Approval | independente do autor e vinculada ao digest exato |
| Developer Agent | allowed paths, blocked sensitive files and only draft PR |
| Release | promotion only after human gate and with the approved digest |
| Remark | health check and explicit decision after deployment |
| Recovery | rollback restores the previous stable digest and maintains history of the digest. |
| Budgets | reserva e bloqueio antes de ultrapassar limite configurado |
| Security | OPA fail-closed, sandbox restrito e supply-chain adapters |

## Runtime compartilhado

O [agentic-sdlc-runtime](https://github.com/leandrosflora/agentic-sdlc-runtime) concentrates the execution of staff and provides:

- agent registry JSON;
- Context Builder with provenance and minimization;
- Model Gateway fake e OpenAI-compatible;
- MCP fake e MCP real via stdio;
- tool loop limitado;
- PAO authorisation;
- evidence bundles;
- checkpoints e retomada;
- CLI, demos e testes;
- Integration with Issues, comments, Checks and draft PRs;
- adapters P7 para OIDC, S3, OTLP, budgets, filas, sandbox e supply chain.

## Case repositories

| Repository | Responsabilidade |
|---|---|
|  [agentic-sdlc-reference-architecture](https://github.com/leandrosflora/agentic-sdlc-reference-architecture)  | architecture, contracts, policies, documentation, golden path and governance |
|  [agentic-sdlc-runtime](https://github.com/leandrosflora/agentic-sdlc-runtime)  | shared runtime, declarative agents, gateways, workflow and adapters |
|  [agentic-sdlc-demo-app](https://github.com/leandrosflora/agentic-sdlc-demo-app)  | target application used to validate branch, alteration, PR, release and rollback |
|  `sdlc-<role>-agent`  | adapters and scaffolds specific to the eight roles; canonical definitions are in the runtime. |

## Relationship with the life cycle of agents

The case applies the lifecycle of Enterprise AI Platform to the engineering agents themselves:

```text
Definir finalidade e owner
        ↓
Versionar prompt, modelo, tools e schemas
        ↓
Avaliar offline e testar policies
        ↓
Publicar no Agent Registry
        ↓
Executar com identidade, budget e contexto governado
        ↓
Coletar qualidade, custo, traces e evidências
        ↓
Promover, limitar, suspender ou retirar a versão
```

No agent can modify its own prompts, policies, thresholds or grants and promote them automatically.

## Security and threat boundaries

The main confidence limits are:

- Issue content, PR and repository is non-reliable entry;
- output of the model is not authorised;
- MCP Gateway is the only way out to corporate tools;
- code execution occurs in ephemeral sandbox;
- secrets are obtained just-in-time and do not enter the context;
- development and production runners should not share trust zone;
- unavailability of policy, identity or written audit blocks;
- insufficient telemetry prevents promotion, but should not prevent manual rollback.

## Current status

| Camada | Classification | Evidence |
|---|---|---|
| Architecture, contracts and policies |  `CONTRACT_DEFINED`  | Documentation, schemes, ADRs and Rego versioned |
| Golden path |  `DEMONSTRATED_LOCAL`  | deterministic flow and evidence bundle |
| Runtime compartilhado |  `DEMONSTRATED_LOCAL`  | testes, CLI, gateways, checkpoints e workflow E2E |
| Model Gateway real |  `IMPLEMENTATION_STARTED`  | OpenAI-compatible integration available and optional |
| MCP real |  `IMPLEMENTATION_STARTED`  | transport stdio available |
| GitHub integration |  `DEMONSTRATED_LOCAL`  | Issue, comment, Checks, branch and draft PR |
| Release e rollback demo |  `DEMONSTRATED_LOCAL`  | healthy path and rollback path |
| Adapters P7 |  `IMPLEMENTATION_STARTED`  | OIDC, S3, OTLP, SQS, Syft, Cosign e Kubernetes |
| Corporate operation | Pendente | providers, environments and real controls not yet approved |
| Production readiness |  `NOT_PRODUCTION_READY`  | lack of operational evidence and formal approval |

## Limites declarados

- Model Gateway fake is the standard of deterministic demos;
- provider real depende de endpoint e credenciais configurados externamente;
- Real MCP supports stdio; other transports are still evolving;
- evidence store local is tamper-evident, no storage corporate WORM;
- demo environment persists locally;
- adapters P7 precisam ser configurados contra providers reais;
- manifesto Kubernetes possui placeholders;
- integration, performance, safety and recovery still need to be validated in a representative environment;
- agents do not have authorization to merge or autonomous productive publication.

## Next slats

1. executar o workflow completo contra um Model Gateway corporativo;
2. connecting real MCP servers by tool and trust zone;
3. implantar OPA HA com bundles assinados;
4. usar workload identity e credenciais just-in-time;
5. Moving evidence to storage WORM with KMS and retention;
6. publish digest artifacts with SBOM and verified signature;
7. executar workers em filas gerenciadas com DLQ e autoscaling;
8. validar sandbox isolado, egress allowlist e limites de recursos;
9. to integrate metrics, traces, cost and SLOs to corporate operation;
10. perform game days rollback, unavailability of PDP and checkpoint recovery.

## Valor demonstrado para a Enterprise AI Platform

The Agentic SDLC shows that the Enterprise AI Platform can govern not only service agents or backoffice, but also agents that participate in the very software production.

The case shows that useful autonomy depends on:

- durable workflow;
- context with origin;
- tools governadas;
- segregation of functions;
- approval linked to the artifact;
- verifiable evidence;
- observation and rollback;
- identity, budget and policy by workload.

Productivity not only comes to generate faster code, but also comes to reduce handoffs and rework. **without removing the controls that make a secure, auditable and recoverable change**.

## References

- [Published documentation](https://leandrosflora.github.io/agentic-sdlc-reference-architecture/)
- [Architectural repository](https://github.com/leandrosflora/agentic-sdlc-reference-architecture)
- [Runtime funcional](https://github.com/leandrosflora/agentic-sdlc-runtime)
- [Implementation demo](https://github.com/leandrosflora/agentic-sdlc-demo-app)
- [Start-to-end integration](https://leandrosflora.github.io/agentic-sdlc-reference-architecture/end-to-end-workflow/)
- [P7 — Production and governance](https://leandrosflora.github.io/agentic-sdlc-reference-architecture/p7-production-governance/)
