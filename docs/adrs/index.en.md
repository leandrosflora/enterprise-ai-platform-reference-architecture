# Architecture Decision Records

The ADRs shall record structural decisions of the platform, its context, alternatives, consequences, evidence and criteria. The `docs/adrs/` pasta is the only canoe source for architectural decisions.

## Catalog

| ADR | Decision | Status |
|---|---|---|
| [ADR-001](001-mcp-vs-rest.md) | MCP for tool calling governed; REST for APIs of field | Aceito |
| [ADR-002](002-persistent-memory.md) | Permanent memory only under explicit criteria | Aceito |
| [ADR-003](003-agent-gateway.md) | Agent Gateway as entry and enforcement point | Aceito |
| [ADR-004](004-agent-runtime-strategy.md) | Agent Runtime with stable and adaptable content | Aceito |
| [ADR-005](005-vector-search-strategy.md) | OpenSearch as initial reference for veterinary and hybrid search | Aceito |
| [ADR-006](006-observability-strategy.md) | OpenTelemetry as a warning pad | Aceito |
| [ADR-007](007-evaluation-strategy.md) | Hybrid, regressive and continuous evaluation | Aceito |

## Status permitidos

| Status | Uso |
|---|---|
| Proposto | Decision in discussion, not yet binding |
| Aceito | vigourous decision |
| Depreciado | still existing, but not recommended for new implementations |
| Substitute | Historical decision replaced by another ID |
| Rejeitado | alternative analysed and not adopted |

## Regras

- a number identifies a single decision;
- the number of the file must comply with the title of the ADR;
- accepted decisions are not written to oculate material changes;
- changes in direction create new ADR and mark the previous as replaced;
- each ADR shall record consequences, evidence and review criteria;
- Intern links must only be placed for `docs/adrs/`.

## Migration of the legal catalog

| - Legal decision | Canopic destination |
|---|---|
| Agent Runtime Strategy | ADR-004 |
| Veterinary bank selection | ADR-005 |
| Integration strategy via MCP | consolidated content in ADR-001 |
| Monitoring strategy | ADR-006 |
| IA Assessment Strategy | ADR-007 |

The documental validation of bloke pastas competing, double IDs, divergence between name and title and the unused ADRs of this Index.
