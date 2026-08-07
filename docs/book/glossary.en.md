# Glossary

## ABAC

Attribute-Based Access Control. Authorization based on user attributes, workload, resource, context, tenant, purpose and classification.

## Agent Gateway

Entry boundary for agent invocations. It applies authentication, rate limit, routing, validation and context propagation.

## Agent Registry

Technical catalog of agents, versions, owners, status, risk, models, tools and allowed knowledge bases.

## Agent Runtime

Environment responsible for executing the agent, setting up context, applying policies, calling models, knowledge, memory and tools.

## AI Catalog

Corporate inventory of cases of use, agents, models, risks, owners, decisions and life cycle status.

## AI Platform

A set of capacities, standards, services and processes that allows creating and operating AI solutions with controlled autonomy.

## Baseline

Reference used to compare a version: previous version, human process, simpler model or approved threshold.

## Capability

Organizational or technical ability that describes what the platform needs to do, without depending on a specific technology.

## Chunk

A document for indexing and retrieval should be used to preserve provenance, classification and authorization.

## Control Plane

Plan responsible for registration, configuration, governance, policies, evaluation, catalogs and promotion of versions.

## Correlation ID

A spread identification between components to correlate execution point to point.

## Data Plane

Plan that performs invocations, retrieval, memory, models, tools and telemetry in execution time.

## Date of evaluation

Versioned set of inputs, context, expected responses, headings and negative scenarios used to measure behavior.

## Deny by default

Principle in which access is denied when no explicit rule allows the operation.

## Embedding

Vector representation of content used in similarity and retrieval. Model and version need to be identifiable.

## Error budget

SLO-derived failure tolerance, used to balance reliability and speed of change.

## Evaluation

Systematic measurement of quality, retrieval, groundedness, safety, tools, performance, reliability and cost.

## Evidence bundle

Reproducible package of artifacts that sustains a decision to publish.

## Fine-tuning

Parameter adjustment of a model using a dataset to change behavior, format or specific capacity.

## Foundation Model

General purpose model trained on a large scale and used as a basis for applications and agents.

## Golden path

Supported and automated path to build, evaluate, approve, publish and operate a solution.

## Groundedness

The degree to which a response is supported by the evidence provided to the model.

## Guardrail

Probabilistic guardrails do not replace deterministic authorization.

## HITL

Human in the loop. The break to a human decision.

## idempotency

Property that allows the repetition of an operation without producing additional improper effects.

## Indirect prompt injection

Malicious or conflicting instruction inserted into the retrieved content, pages, documents or tool results.

## Knowledge Base

Governed collection of documents and chunks available for retrieval under specific policies.

## Long-term Memory

Memory persists beyond the current session. It requires purpose, origin, trust, TTL and consent when applicable.

## MCP

Model Context Protocol. Protocol for exposure and standardized discovery of tools and resources for models and agents.

## Memory poisoning

Insertion of incorrect, malicious or unauthorized content into memory to influence future executions.

## Model Gateway

It abstracts providers and applies routing, policies, observability, limits, fallback and cost control.

## Model routing

Model selection based on capacity, quality, region, cost, latency and availability.

## Multi-agent

Architecture in which multiple specialized agents collaborate or delegate tasks to each other.

## NFR

Non-Functional Requirement. Security, reliability, performance, privacy, cost, support or operation requirements.

## OIDC

OpenID Connect. Identity protocol built on OAuth 2.0.

## Policy Decision Point

It is a component that evaluates policies and produces a decision of authorization or control.

## Policy Enforcement Point

Component that intercepts an operation and applies the policy decision.

## Prompt

The set of instructions, messages and context provided to the model should be versioned when it affects the product behavior.

## Provenance

Information about origin, version, transformations and processing chain of a given or artifact.

## RAG

Retrieval-Augmented Generation. Pattern that recovers external evidence and provides them to the model during generation.

## RBAC

Role-Based Access Control. Paper-based authorization.

## Reranking

Reordering of retrieval results using an additional model or algorithm.

## Retrieval

Process of finding relevant and authorized evidence for consultation.

## Risk tier

Risk class that determines controls, evidence, reviews and applicable gates.

## Session Memory

Ephemeral context limited to session and to the authorised subject.

## Shadow evaluation

Implementing a new version or model in parallel, without using its response to affect the user, for safe comparison.

## SLO

Service Level Objective. Measurable objective of availability, latency, success or other operational characteristic.

## System of record

Authoritative system for data and transactional states. Agent memory should not take this role.

## Tenant

Logical unit of isolation, such as company, area, client or environment.

## Tool

External capacity invoked by the agent by structured contract. The agent may consult data or take effect.

## Vertical slice

Minimum implementation point by point used to demonstrate contracts, flows and controls of architecture.

## Workload class

Operational category used to define SLOs and different limits, such as simple interaction, RAG, tool call or asynchronous processing.
