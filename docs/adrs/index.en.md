# Architecture Decision Records

The ADRs record structural decisions of the platform, its context, alternatives, consequences, evidence and review criteria. `docs/adrs/` it is the only canonical source for architectural decisions.

## Catalogue

| ADR | Decision | Status |
|---|---|---|
|  [ADR-001](001-mcp-vs-rest.md)  | MCP for governed tool calling; REST for domain APIs | Aceito |
|  [ADR-002](002-persistent-memory.md)  | Persistent memory only under explicit criteria | Aceito |
|  [ADR-003](003-agent-gateway.md)  | Agent Gateway como ponto de entrada e enforcement | Aceito |
|  [ADR-004](004-agent-runtime-strategy.md)  | Agent Runtime with stable core and adapters | Aceito |
|  [ADR-005](005-vector-search-strategy.md)  | OpenSearch as initial reference for vector and hybrid search | Aceito |
|  [ADR-006](006-observability-strategy.md)  | OpenTelemetry as observability pattern | Aceito |
|  [ADR-007](007-evaluation-strategy.md)  | Hybrid, regressive and continuous evaluation | Aceito |

## Status permitidos

| Status | Uso |
|---|---|
| Proposto | decision under discussion, not yet binding |
| Aceito | Existing decision |
| Depreciado | still existing, but not recommended for further implementations |
| Replaced | historical decision replaced by another ADR identified |
| Rejeitado | alternative analyzed and not adopted |

## Regras

- a number identifies a single decision;
- the file number shall match the ADR title;
- accepted decisions are not rewritten to hide material changes;
- Changes in direction create new ADRs and mark the former as replaced;
- Each ADR should record consequences, evidence and review criteria;
- internal links should point only to `docs/adrs/`.

## Migration of the legacy catalogue

| Legitimate decision | Canonical destination |
|---|---|
| Agent Runtime strategy | ADR-004 |
| Vector bank selection | ADR-005 |
| Integration strategy via PCM | consolidated content in ADR-001 |
| Observability strategy | ADR-006 |
| AI assessment strategy | ADR-007 |

Document validation blocks competing folders, duplicated DIs, divergence between name and title and ADRs absent from this index.
