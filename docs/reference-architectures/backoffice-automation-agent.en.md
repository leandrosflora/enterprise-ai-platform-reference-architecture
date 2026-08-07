# Reference architecture - Backoffice Automation Agent

## Objective

Automate repetitive operational backoffice tasks using agents integrated to internal systems, workflow and action governance.

## Cases of Use

- Screening of requests
- Consultation and updating of internal systems
- Supporting contest
- Preparation of documents
- Assisted implementation of operational tasks

## components involved

- Agent Gateway
- Agent Runtime
- MCP Registry
- MCP Servers
- Corporate Systems
- Workflow / BPM
- Audit Service
- Governance Service
- Billing Service

## High Level Flow

1. Event or request starts the process.
2. Agent Runtime interprets the objective and consults the context.
3. MCP Server performs actions in authorised systems.
4. Workflow receives status and next steps.
5. Critical cases are sent for human review.
6. Audit Service records decisions, commands and evidence.

## Controls

- idempotency for commands
- Human approval for irreversible actions
- Limit of autonomy for risk
- Segregation of functions
- Mandatory audit of tool calls

## Metrics

- Time saved by procedure
- Volume of automated tasks
- Operational error rate
- Human intervention rate
- Cost per procedure
