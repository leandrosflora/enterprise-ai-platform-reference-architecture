# Documentação

Esta pasta concentra a documentação arquitetural da Enterprise AI Platform.

## Estrutura

```text
architecture/     Diagramas, princípios e decisões arquiteturais
adr/              Architecture Decision Records
domains/          Domínios funcionais da plataforma
services/         Documentação dos serviços da plataforma
integrations/     Integrações externas e corporativas
contracts/        Eventos, APIs e data stores
governance/       Governança de IA, riscos e ciclo de aprovação
observability/    Tracing, métricas, dashboards e alertas
security/         Autenticação, autorização, LGPD e segredos
finops/           Custos, chargeback, showback e token analytics
runbooks/         Guias operacionais
roadmap/          Evolução planejada da plataforma
```

## Diagramas iniciais

- [C4 Context](architecture/diagrams/c4-context.puml)
- [C4 Container](architecture/diagrams/c4-container.puml)

## Próximos artefatos recomendados

1. `contracts/events.md`
2. `services/agent-runtime.md`
3. `services/knowledge-service.md`
4. `services/governance-service.md`
5. `adr/ADR-001-agent-runtime-strategy.md`
6. `adr/ADR-002-vector-database.md`
