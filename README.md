# Enterprise AI Platform - Arquitetura de Referência

> Arquitetura de referência para uma Plataforma Corporativa de IA, demonstrando governança, orquestração multiagentes, integração via MCP, RAG, observabilidade, avaliação de modelos, segurança e FinOps para adoção de IA em escala empresarial.

## Status do Projeto

Este repositório evoluiu de uma visão conceitual para uma arquitetura documentada contendo:

- C4 Context Diagram
- C4 Container Diagram
- C4 Component Diagram (Agent Runtime)
- Sequence Diagrams
- Contratos de Eventos
- Documentação de Serviços
- Architecture Decision Records (ADRs)

---

## Navegação Rápida

### Arquitetura

| Artefato | Link |
|-----------|------|
| C4 Context | docs/architecture/diagrams/c4-context.puml |
| C4 Container | docs/architecture/diagrams/c4-container.puml |
| C4 Component - Agent Runtime | docs/architecture/diagrams/c4-component-agent-runtime.puml |
|
| Agent Invocation Sequence | docs/architecture/diagrams/sequences/agent-invocation.puml |
| RAG Query Sequence | docs/architecture/diagrams/sequences/rag-query.puml |
| MCP Tool Execution Sequence | docs/architecture/diagrams/sequences/mcp-tool-execution.puml |
| Agent Publishing Sequence | docs/architecture/diagrams/sequences/agent-publishing.puml |

### Contratos

| Documento | Link |
|-----------|------|
| Eventos Kafka | docs/contracts/events.md |

### Serviços

| Serviço | Link |
|----------|------|
| Agent Runtime | docs/services/agent-runtime.md |
| Knowledge Service | docs/services/knowledge-service.md |
| Governance Service | docs/services/governance-service.md |

### Architecture Decision Records

| ADR | Link |
|-----|------|
| ADR-001 Agent Runtime Strategy | docs/adr/ADR-001-agent-runtime-strategy.md |
| ADR-002 Vector Database Selection | docs/adr/ADR-002-vector-database-selection.md |
| ADR-003 MCP Strategy | docs/adr/ADR-003-mcp-strategy.md |
| ADR-004 Observability Strategy | docs/adr/ADR-004-observability-strategy.md |
| ADR-005 Evaluation Framework | docs/adr/ADR-005-evaluation-framework.md |

---

## Estrutura de Documentação

Consulte também:

- docs/README.md

---

## Visão da Plataforma

A Enterprise AI Platform fornece capacidades corporativas para:

- Construção de agentes
- Governança de IA
- Integração via MCP
- RAG corporativo
- Memória conversacional
- Observabilidade
- Avaliação contínua
- FinOps para IA
- Segurança e conformidade

---

## Principais Capacidades

### Agent Platform

- Agent Runtime
- Agent Gateway
- Agent Registry
- Multi-Agent Orchestration
- Tool Calling

### Knowledge Platform

- Ingestão documental
- Embeddings
- Busca Vetorial
- RAG

### MCP Platform

- MCP Registry
- Tool Discovery
- Tool Governance

### AI Governance

- Catálogo de Agentes
- Aprovação
- Gestão de Riscos
- Auditoria

### AI Evaluation

- Groundedness
- Hallucination Detection
- Relevância
- Toxicidade

### AI Observability

- Tracing
- Logs
- Métricas
- Custos

### AI FinOps

- Chargeback
- Showback
- Token Analytics

---

## Tecnologias de Referência

- AWS
- Amazon Bedrock
- AgentCore
- OpenSearch
- PostgreSQL
- MongoDB
- Redis
- Kafka
- OpenTelemetry
- Kubernetes
- .NET
- React

---

## Roadmap

### Foundation

- Agent Gateway
- Agent Runtime
- MCP Registry

### Knowledge

- RAG
- Knowledge Service
- Memory Service

### Governance

- Evaluation Service
- Governance Service
- Observability

### Scale

- Multi-Agent Platform
- Self-Service Portal
- Agent Marketplace
- FinOps

---

## Licença

MIT