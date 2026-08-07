# Glossary of terms

## ABAC

Attribute-Based Access Control. Authorisation based on user attributes, workload, resource, context, tenant, purpose, and rating.

## Agent Gateway

It applies authentication, rate limit, routing, validation and context propagation.

## Agent Registry

Technical catalogue of agents, versions, owners, status, risk, models, tools and knowledge bases allowed.

## Agent Runtime

Environment responsible for executing the agent, setting context, implementing policies, calling models, knowledge, memory and tools.

## AI Catalog

Corporate inventory of use cases, agents, models, risks, owners, decisions and life cycle status.

## AI Platform

A set of capabilities, standards, services and processes enabling AI solutions to be created and operated with controlled autonomy.

## Baseline

Reference used to compare a version: previous version, human process, simpler model or approved threshold.

## Capability

An organizational or technical skill that describes what the platform needs to be able to do without relying on a specific technology.

## Chunk

Excerpt derived from a document for indexation and retrieval. It must preserve provenance, classification and authorisation.

## Control Plane

Plan responsible for registration, configuration, governance, policies, evaluation, catalogues and promotion of versions.

## Correlation ID

Identifier propagated between components to correlate end-to-end execution.

## Data Plane

Plan that executes invocations, retrieval, memory, templates, tools and telemetry at runtime.

## Assessment data set

A versioned set of entries, context, expected responses, headings and negative scenarios used to measure behavior.

## Deny by default

Principle that access is denied when no explicit rule allows the operation.

## Embedding

Vector representation of content used in similarity and retrieval.

## Error budget

Failure tolerance derived from SLO, used to balance reliability and change speed.

## Evaluation

Systematic measurement of quality, retrieval, groundedness, safety, tools, performance, reliability and cost.

## Evidence bundle

Reproducible packaging of artifacts supporting a publication decision.

## Fine-tuning

Adjusting parameters of a model using a dataset to change specific behavior, format or capability.

## Foundation Model

A general purpose model trained on a large scale and used as a basis for applications and agents.

## Golden path

Supported and automated path to build, evaluate, approve, publish and operate a solution.

## Groundedness

The degree to which an answer is supported by the evidence available to the model.

## Guardrail

Probability guardrails do not replace deterministic permission.

## HITL

Human in the loop. The execution is suspended until a human decision is made.

## Impotence

Property that allows repeating an operation without producing additional undue effects.

## Indirect prompt injection

Malicious or conflicting instruction inserted into recovered content, pages, documents or tool results.

## Knowledge Base

Governed collection of documents and chunks available for retrieval under specific policies.

## Long-term Memory

Persistent memory beyond the current session. Requires purpose, origin, trust, TTL and consent where applicable.

## MCP

Model Context Protocol, a protocol for standardised exposure and discovery of tools and resources for models and agents.

## Memory poisoning

Inserting incorrect, malicious or unauthorized content into memory to influence future executions.

## Model Gateway

Layer that abstracts suppliers and applies routing, policies, observability, limits, fallback and cost control.

## Model routing

Model selection based on capacity, quality, region, cost, latency and availability.

## Multi-agent

Architecture in which multiple specialized agents collaborate or delegate tasks to each other.

## NFR

Non-functional Requirement: Requirement for security, reliability, performance, privacy, cost, support or operation.

## OIDC

OpenID Connect, an identity protocol built on OAuth 2.0.

## Policy Decision Point

A component that assesses policies and makes an authorisation or control decision.

## Policy Enforcement Point

A component that intercepts an operation and applies the policy decision.

## Prompt

Set of instructions, messages and context provided to the model. It must be versioned when it affects product behavior.

## Provenance

Information on the origin, version, transformation and chain of processing of a data or artifact.

## RAG

Retrieval-Augmented Generation. A pattern that retrieves external evidence and supplies it to the model during the generation.

## RBAC

Role-based access control, paper-based authorization.

## Reranking

Rearrangement of retrieval results using an additional model or algorithm.

## Retrieval

Process of locating relevant and authorised evidence for a consultation.

## Risk tier

Risk class determining applicable controls, evidence, reviews and gates.

## Session Memory

Temporary context limited to the session and authorized subject.

## Shadow evaluation

Running a new version or model in parallel without using its response to affect the user for safe comparison.

## SLO

Service level objective: measurable objective of availability, latency, success or other operational characteristic.

## System of record

An authoritative system for data and transactional statements.

## Tenant

Logical isolation unit, such as enterprise, area, customer or environment.

## Tool

External capacity invoked by the agent by structured contract.

## Vertical slice

Minimum end-to-end implementation used to demonstrate contracts, flows and controls of the architecture.

## Workload class

Operational category used to define SLOs and different limits such as simple interaction, RAG, tool call or asynchronous processing.
