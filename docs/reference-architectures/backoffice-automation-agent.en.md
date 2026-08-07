# This is the total amount of assigned revenue in accordance with Article 21 (3) of the Financial Regulation.

## Objective

Automate repetitive backoffice operational tasks using agents with integration into internal systems, workflow and action governance.

## Cases of use

- Selection of requests
- Consultation and updating of internal systems
- I support the challenge
- Preparation of documents
- Assisted execution of operational tasks

## Components involved

- Agent Gateway
- Agent Runtime
- MCP Registry
- MCP Servers
- Corporate Systems
- Workflow / BPM
- Audit Service
- Governance Service
- Billing Service

## High-level flow

1. Event or request starts the process.
2. Agent Runtime interprets the objective and consults the context.
3. MCP Server performs actions on authorised systems.
4. Workflow receives status and next steps.
5. Critical cases are sent for human review.
6. Audit Service records decisions, commands and evidence.

## Controls

- Idempotence for commands
- Human approval for irreversible actions
- Limit of autonomy by risk
- Separation of functions
- Compulsory auditing of tool calls

## The following information shall be provided:

- Time saved by process
- Automated tasks volume
- Operational error rate
- Human intervention rate
- Cost per process
