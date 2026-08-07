# Documentation

This pasta contains the **Enterprise AI Platform Reference Book** and the articles supporting organisations in the development and implementation of their own corporative IA platforms.

The content is a documentary and architectural reference. It does not deliver a ready platform, does not define an obligation implementation and does not replace specific decisions of infrastructure, security, size or compliance.

## Comece pelo book

1. [Input of the book](book/index.md)
2. [Why a AI Platform?](book/01-why-ai-platform.md)
3. [Capability Map](book/02-capability-map.md)
4. [Operating Model](book/03-operating-model.md)
5. [Life cycle of agents](book/04-agent-lifecycle.md)
6. [Study of case of documentary agent](book/05-case-study-document-agent.md)
7. [Decision Guides](book/06-decision-guides.md)
8. [Adoption button](book/07-adoption-roadmap.md)
9. (production checklists)(book/08-production-checklists.md)
10. [Glossary](book/glossary.md)

## Estrutura

```text
book/                     Narrativa, operating model, casos, decisões e checklists
architecture/             Princípios, NFRs, C4 e separação de planos
adr/                      Architecture Decision Records
contracts/                OpenAPI, AsyncAPI, MCP, eventos e data stores
domains/                  Domínios funcionais da plataforma
services/                 Capacidades e responsabilidades lógicas por serviço
governance/               Workflow, risco, catálogo e ciclo de modelos
security/                 Autenticação, autorização, LGPD, RAG/memória e threat model
observability/            Tracing, métricas, dashboards, alertas e SLOs
finops/                   Custos, budgets, chargeback e showback
runbooks/                 Procedimentos operacionais de referência
examples/                 Exemplos ponta a ponta
reference-architectures/  Blueprints por caso de uso
roadmap/                  Sequenciamento recomendado para implementação
```

## Relationship between book and artefacts

- **book** explains the problem, decision, tradeoffs, operating model and success criteria.
- The ** Reference Framework** defines contracts, policies, capacities, events and procedures that can guide different implementations.
- The technical **asshole** shows parts of the controls in a way that is able to validate the documentation.

The technical sample does not represent a recommended physical arrangement or a ready-made plate for production.

The editorial content cannot be re-defined in any, envelopes, policies or metas different from the canonical sources.

## Canopies

| Assunto | Fonte |
|---|---|
| APIs HTTP | [`contracts/openapi.yaml`](contracts/openapi.yaml) |
| Eventos | [`contracts/async-api.yaml`](contracts/async-api.yaml) |
| Events Conventions | [`contracts/events.md`](contracts/events.md) |
| SLOs | [`architecture/non-functional-requirements.md`](architecture/non-functional-requirements.md) |
| Risk controls | [`governance/ai-risk-framework.md`](governance/ai-risk-framework.md) |
| Authorisation | [`security/authorization.md`](security/authorization.md) |
| Security of RAG and memory | [`security/rag-memory-security.md`](security/rag-memory-security.md) + [`../policies/rag-memory-security.yaml`](https://github.com/leandrosflora/enterprise-ai-platform-reference-architecture/blob/main/policies/rag-memory-security.yaml) |

## - Apocalypse

- [C4 Context](architecture/diagrams/c4-context.puml)
- [C4 Container](architecture/diagrams/c4-container.puml)
- [C4 Deployment](architecture/diagrams/c4-deployment.puml)
- [Control plane e data plane](architecture/control-plane-data-plane.md)
- [Event Storming](architecture/diagrams/event-storming.md)

## Reference Capacity and services

- [Agent Gateway](services/agent-gateway.md)
- [Agent Runtime](services/agent-runtime.md)
- [Agent Registry](services/agent-registry.md)
- [Model Gateway](services/model-gateway.md)
- [Knowledge Service](services/knowledge-service.md)
- [Memory Service](services/memory-service.md)
- [MCP Registry](services/mcp-registry.md)
- [Governance Service](services/governance-service.md)
- [Evaluation Service](services/evaluation-service.md)
- [Audit Service](services/audit-service.md)
- [Billing Service](services/billing-service.md)

These names represent architectural responsibility, and they do not require each capacity to be implemented as an independent microsystem.

## Reference operation

- [Agentboarding](runbooks/onboarding-agent.md)
- [Onboarding MCP](runbooks/onboarding-mcp.md)
- (Invocative troubles)(runbooks/troubleshooting-agent-invocation.md)

## Get the book

In the midst of the repository:

```bash
python scripts/build_book.py --check
python scripts/build_book.py
```

The PDF is automatically accessed by the `.github/workflows/book.yml` workflow using Pandoc and WeasyPrint.

## Validation

```bash
python scripts/validate_contracts.py
python scripts/validate_docs.py
python scripts/build_book.py --check
bash scripts/render_diagrams.sh
mkdocs build
```
