# This appropriation is intended to cover expenditure on technical assistance for the implementation of the programme.

## Objective

Automate the analysis of corporate documents, extracting information, classifying content, validating rules and supporting operational decisions.

## Cases of use

- Extraction of data from documents
- Classification of documents
- Validation of compulsory fields
- Comparison with internal policies
- Supported opinion generation

## Components involved

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
- Sistemas transacionais

## High-level flow

1. Document is received by upload, queue or corporate system.
2. Pipeline extracts text and metadata.
3. Knowledge Service index or refer to relevant references.
4. Agent Runtime analyses the document with rules and context.
5. Evaluation Service validates quality and consistency.
6. Results are recorded and forwarded for review or workflow.

## Controls

- Classification of data
- Masking of sensitive information
- Withholding according to corporate policy
- Evidence for audit
- Human review for critical decisions

## The following information shall be provided:

- Rate of correct extraction
- Average time of analysis
- Human review rate
- Failure by type of document
- Cost per document processed
