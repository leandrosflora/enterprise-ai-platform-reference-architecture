# Casos aplicados

Os casos aplicados demonstram como as capacidades lógicas da Enterprise AI Platform podem ser materializadas em domínios, jornadas e topologias concretas.

Eles não definem uma implementação única. Cada caso explicita:

- o problema de negócio;
- onde a IA participa da jornada;
- quais capacidades da plataforma são utilizadas;
- quais controles permanecem determinísticos;
- o que está implementado, demonstrado ou apenas planejado;
- os gaps para integração e produção.

## Casos disponíveis

<div class="grid cards" markdown>

-   :material-message-processing-outline: **Plataforma conversacional bancária multi-skill**

    ---

    Jornadas bancárias via WhatsApp, múltiplas skills, Agent Runtimes, ferramentas MCP, RAG, memória, eventing, auditoria e evals.

    [Abrir o caso conversacional](conversational-ai.md)

-   :material-clipboard-flow-outline: **Intelligent Backoffice — contestação bancária**

    ---

    Workflow persistente, processamento documental, investigação assistida, recomendação, aprovação humana, policy enforcement, execução idempotente e reconciliação.

    [Abrir o caso de backoffice](intelligent-backoffice.md)

-   :material-source-branch: **Agentic SDLC governado**

    ---

    Agentes especializados do requisito ao feedback de produção, workflow durável, Model Gateway, MCP, OPA, evidências, aprovação por digest, release observado e rollback.

    [Abrir o caso de Agentic SDLC](agentic-sdlc.md)

</div>

## Comparação rápida

| Caso | Unidade principal de interação | Autonomia inteligente | Efeito real governado |
|---|---|---|---|
| Plataforma conversacional | conversa e jornada do cliente | selecionar skill, responder e usar tools | operações bancárias mediadas por serviços de domínio |
| Intelligent Backoffice | caso, documento e evidência | classificar, investigar e recomendar | aprovação humana e execution service |
| Agentic SDLC | mudança de software e evidence bundle | refinar, desenhar, implementar e revisar | tools via MCP, aprovação por digest, release e rollback |

## Como interpretar os estados

| Estado | Significado |
|---|---|
| `CONTRACT_DEFINED` | Arquitetura, contrato, policy ou responsabilidade versionada, ainda sem integração comprovada |
| `IMPLEMENTATION_STARTED` | Código de produto iniciado, mas sem evidência suficiente de integração ponta a ponta |
| `DEMONSTRATED_LOCAL` | Capacidade executada localmente ou no CI com dados e integrações sintéticos |
| `VALIDATED_INTEGRATION` | Integração validada contra serviços reais em ambiente controlado |
| `PASSED_PRODUCTION` | Capacidade aprovada para produção com evidência, operação, segurança e ownership |

!!! warning "Caso aplicado não significa produção"
    Diagramas, código e testes locais demonstram decisões e mecanismos. Produção exige integração real, dados autorizados, segurança corporativa, operação, SLOs, suporte, risco e aprovação formal.
