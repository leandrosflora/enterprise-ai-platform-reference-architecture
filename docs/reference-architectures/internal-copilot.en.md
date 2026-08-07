# Arquitetura de Referência - Copilot Interno

## Objetivo

Disponibilizar um assistente corporativo interno para apoiar colaboradores em busca de conhecimento, orientação operacional e execução assistida de tarefas.

## Casos de Uso

- Busca em políticas internas
- Apoio a atendimento interno
- Consulta a procedimentos
- Geração de respostas com citação de fontes
- Abertura assistida de chamados

## Componentes Envolvidos

- AI Portal
- Agent Gateway
- Agent Runtime
- Knowledge Service
- Memory Service
- MCP Registry
- Governance Service
- Evaluation Service
- Audit Service

## Fluxo de Alto Nível

1. Usuário acessa o AI Portal.
2. Agent Gateway autentica e autoriza a solicitação.
3. Agent Runtime executa o agente.
4. Knowledge Service recupera documentos relevantes.
5. Memory Service recupera contexto permitido.
6. Agent Runtime chama o modelo fundacional.
7. Evaluation Service avalia a resposta.
8. Audit Service registra a execução.

## Requisitos de Governança

- Aprovação do agente no AI Catalog
- Classificação de risco
- Base de conhecimento autorizada
- Avaliação mínima de groundedness
- Auditoria completa das interações

## Métricas

- Taxa de resolução sem escalonamento
- Groundedness score
- Latência P95
- Custo por interação
- Satisfação do usuário
