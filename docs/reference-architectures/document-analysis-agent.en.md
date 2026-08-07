# Reference architecture - Documentary Analysis Agent

## Objective

Automate the analysis of corporate documents, extracting information, classifying content, validating rules and supporting operational decisions.

## Casos de Uso

- Extraction of data from documents
- Documentary classification
- Validation of mandatory fields
- Comparison with internal policies
- Management of assisted opinions

## Componentes Envolvidos

- Agent Gateway
- Agent Runtime
- Knowledge Service
- Evaluation Service
- Governance Service
- Audit Service
- External OCR Service
- Document Management System

## Integrations

- OCR
- GED / ECM
- Data Lake
- Workflow / BPM
- Transaction systems

## High Level Flow

1. The document is received by upload, queue or corporate system.
2. Pipeline extrai texto e metadados.
3. Knowledge Service indexes or consults applicable references.
4. Agent Runtime analyzes the document with rules and context.
5. Evaluation Service validates quality and consistency.
6. Results are registered and sent for review or workflow.

## Controls

- Data classification
- Masking of sensitive information
- Retention according to corporate policy
- Evidence for audit
- Human review for critical decisions

## Metrics

- Correct extraction rate
- Mean time of analysis
- Human review rate
- Falhas por tipo documental
- Cost per document processed
