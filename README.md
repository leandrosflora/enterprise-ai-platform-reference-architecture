# Enterprise AI Platform - Reference Architecture

> Enterprise-grade AI Platform reference architecture covering Agentic AI, MCP, RAG, Memory, Governance, Evaluation, Observability, Security and FinOps.

---

## Architecture Overview

This repository demonstrates how to design, govern and operate an Enterprise AI Platform at scale.

Capabilities covered:

- Agent Platform
- Knowledge Platform
- Memory Platform
- MCP Platform
- Governance Platform
- Evaluation Platform
- Observability Platform
- FinOps Platform

---

# Documentation Map

## Architecture

### C4 Model

- docs/architecture/diagrams/c4-context.puml
- docs/architecture/diagrams/c4-container.puml
- docs/architecture/diagrams/c4-component-agent-runtime.puml
- docs/architecture/diagrams/c4-component-knowledge-service.puml
- docs/architecture/diagrams/c4-component-governance-service.puml
- docs/architecture/diagrams/c4-deployment.puml

### Sequence Diagrams

- docs/architecture/diagrams/sequences/agent-invocation.puml
- docs/architecture/diagrams/sequences/rag-query.puml
- docs/architecture/diagrams/sequences/mcp-tool-execution.puml
- docs/architecture/diagrams/sequences/agent-publishing.puml

### Event Storming

- docs/architecture/diagrams/event-storming.md

---

## Domains

- docs/domains/agent-platform.md
- docs/domains/knowledge-platform.md
- docs/domains/memory-platform.md
- docs/domains/mcp-platform.md
- docs/domains/governance-platform.md
- docs/domains/evaluation-platform.md
- docs/domains/observability-platform.md
- docs/domains/finops-platform.md

---

## Services

- docs/services/agent-runtime.md
- docs/services/agent-registry.md
- docs/services/knowledge-service.md
- docs/services/memory-service.md
- docs/services/mcp-registry.md
- docs/services/governance-service.md

---

## Contracts

- docs/contracts/apis.md
- docs/contracts/events.md
- docs/contracts/async-api.yaml
- docs/contracts/data-stores.md
- docs/contracts/mcp-contracts.md

---

## Governance

- docs/governance/approval-workflow.md
- docs/governance/ai-catalog.md
- docs/governance/ai-risk-framework.md
- docs/governance/model-lifecycle.md

---

## Security

- docs/security/authentication.md
- docs/security/authorization.md
- docs/security/lgpd.md

---

## Observability

- docs/observability/tracing.md
- docs/observability/dashboards.md

---

## FinOps

- docs/finops/token-costs.md

---

## Integrations

- docs/integrations/foundation-models.md
- docs/integrations/identity-provider.md
- docs/integrations/corporate-systems.md
- docs/integrations/observability-stack.md
- docs/integrations/external-tools.md

---

## ADRs

- ADR-001 Agent Runtime Strategy
- ADR-002 Vector Database Selection
- ADR-003 MCP Strategy
- ADR-004 Observability Strategy
- ADR-005 Evaluation Framework

---

# Reference Technology Stack

## Platform

- AWS
- Kubernetes (EKS)
- Amazon MSK
- Amazon Bedrock
- OpenTelemetry

## Data

- PostgreSQL
- MongoDB
- OpenSearch
- Redis

## Development

- .NET
- React
- Kafka
- MCP

---

# Implementation Roadmap

## Phase 1

Foundation Platform

## Phase 2

Knowledge Platform and Enterprise RAG

## Phase 3

MCP and Corporate Integrations

## Phase 4

Governance and Evaluation

## Phase 5

Scale, Marketplace and FinOps

Roadmap details:

- docs/roadmap/implementation-roadmap.md

---

# Target Audience

- Enterprise Architects
- Solution Architects
- AI Architects
- Platform Engineers
- Technical Leads
- Governance Teams
- Security Teams

---

# License

MIT