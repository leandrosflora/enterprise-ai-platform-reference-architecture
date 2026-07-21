from __future__ import annotations

import os
import time
from typing import TypedDict

from fastapi import FastAPI, Header, HTTPException
from langgraph.graph import END, StateGraph
from opentelemetry import trace
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.sdk.trace import TracerProvider
from pydantic import BaseModel, Field

trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer(__name__)

app = FastAPI(title="AI Platform Reference Implementation", version="0.1.0")
FastAPIInstrumentor.instrument_app(app)


class InvokeRequest(BaseModel):
    session_id: str = Field(min_length=1)
    message: str = Field(min_length=1, max_length=8000)


class AgentState(TypedDict):
    tenant_id: str
    session_id: str
    message: str
    response: str
    model: str


def invoke_model(state: AgentState) -> AgentState:
    provider = os.getenv("MODEL_PROVIDER", "mock")
    model = os.getenv("MODEL_NAME", "reference-model")
    # Adapter intencionalmente simples. Substitua por Bedrock/OpenAI mantendo o contrato.
    response = (
        f"Resposta de referência para o tenant {state['tenant_id']}: "
        f"recebi '{state['message']}'. Provider={provider}."
    )
    return {**state, "response": response, "model": model}


graph = StateGraph(AgentState)
graph.add_node("invoke_model", invoke_model)
graph.set_entry_point("invoke_model")
graph.add_edge("invoke_model", END)
agent = graph.compile()


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/v1/agents/{agent_id}/invoke")
def invoke_agent(
    agent_id: str,
    payload: InvokeRequest,
    x_tenant_id: str | None = Header(default=None),
) -> dict[str, object]:
    if not x_tenant_id:
        raise HTTPException(status_code=400, detail="X-Tenant-Id is required")

    started = time.perf_counter()
    with tracer.start_as_current_span("agent.invoke") as span:
        span.set_attribute("ai.agent.id", agent_id)
        span.set_attribute("ai.tenant.id", x_tenant_id)
        result = agent.invoke(
            {
                "tenant_id": x_tenant_id,
                "session_id": payload.session_id,
                "message": payload.message,
                "response": "",
                "model": "",
            }
        )

    return {
        "agent_id": agent_id,
        "session_id": payload.session_id,
        "response": result["response"],
        "model": result["model"],
        "latency_ms": round((time.perf_counter() - started) * 1000, 2),
    }
