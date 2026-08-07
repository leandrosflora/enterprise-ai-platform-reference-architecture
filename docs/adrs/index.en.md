# Architecture Decision Records

The ADRs record the platform's structural decisions, their context, alternatives, consequences, evidence and review criteria.`docs/adrs/`It's the only canonical source for architectural decisions.

## Catalogue

| ADR | Decision | Status |
|---|---|---|
| [ADR-001](001-mcp-vs-rest.md) | MCP for tool calling governed; REST for APIs domain | Aceito |
| [ADR-002](002-persistent-memory.md) | Persistent memory only under explicit criteria | Aceito |
| [ADR-003](003-agent-gateway.md) | Agent Gateway as entry and enforcement point | Aceito |
| [ADR-004](004-agent-runtime-strategy.md) | Agent Runtime with stable core and adapters | Aceito |
| [ADR-005](005-vector-search-strategy.md) | OpenSearch as an initial reference for vector and hybrid search | Aceito |
| [ADR-006](006-observability-strategy.md) | OpenTelemetry as an observability standard | Aceito |
| [ADR-007](007-evaluation-strategy.md) | Hybrid, regressive and continuous evaluation | Aceito |

## Status permitidos

| Status | Uso |
|---|---|
| Proposto | Decision under consideration, not yet binding |
| Aceito | Decision in force |
| Depreciado | still existing but not recommended for new implementations |
| Substituted | historical decision replaced by another identified ADR |
| Rejeitado | Alternative analysed and not adopted |

## Rules

- a number identifies a single decision;
- the file number shall coincide with the title of the ADR;
- accepted decisions are not rewritten to conceal material changes;
- direction changes create a new ADR and mark the previous one as a replacement;
- each ADR shall record consequences, evidence and review criteria;
- Internal links shall only point to `docs/adrs/`.

## Migration of the legacy catalogue

| Legacy decision | Canonical destiny |
|---|---|
| Strategy of Agent Runtime | ADR-004 |
| Selection of vector bench | ADR-005 |
| Integration strategy via MCP | Consolidated content in ADR-001 |
| Observability strategy | ADR-006 |
| The Commission shall adopt delegated acts in accordance with Article 21 of this Regulation. | ADR-007 |

Document validation blocks competing folders, duplicate IDs, name and title divergence and ADRs missing from this index.
