# chatbot_gateway/src/routes/chat_router.py
import os
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import httpx

router = APIRouter(tags=["chat"])

ADK_AGENT_URL = os.getenv("ADK_AGENT_URL", "http://adk-agent:8001")
LANGGRAPH_AGENT_URL = os.getenv("LANGGRAPH_AGENT_URL", "http://langgraph-agent:8080")
DEFAULT_USER = os.getenv("CHAT_USER_ID", "local-user")

class ChatIn(BaseModel):
    message: str
    target: str = "adk"  # "adk" o "langgraph"

@router.post("/chat")
async def chat(payload: ChatIn):
    try:
        async with httpx.AsyncClient(timeout=60) as client:

            # ---------- LangGraph ----------
            if payload.target == "langgraph":
                body = {"user": DEFAULT_USER, "question": payload.message}
                r = await client.post(f"{LANGGRAPH_AGENT_URL}/api/chatbot", json=body)
                if r.status_code == 200:
                    return {"ok": True, "agent": "langgraph", "data": r.json()}
                if r.status_code in (400, 422):
                    # devolvemos el detalle que envía FastAPI para ver el campo faltante
                    raise HTTPException(status_code=502, detail={"agent":"langgraph","tried": body, "error": r.json()})
                r.raise_for_status()

            # ---------- ADK ----------
            # Crear/asegurar sesión (409 = ya existe → OK)
            try:
                await client.post(
                    f"{ADK_AGENT_URL}/apps/sales_agent/users/{DEFAULT_USER}/sessions/{DEFAULT_USER}",
                    json={}
                )
            except Exception:
                pass

            # Forma confirmada por tus tests:
            body = {
                "appName": "sales_agent",
                "userId": DEFAULT_USER,
                "sessionId": DEFAULT_USER,
                "newMessage": {
                    "parts": [
                        {"text": payload.message}
                    ]
                }
            }

            r = await client.post(f"{ADK_AGENT_URL}/run", json=body)
            if r.status_code == 200:
                return {"ok": True, "agent": "adk", "data": r.json()}
            if r.status_code in (400, 422):
                raise HTTPException(status_code=502, detail={"agent":"adk","tried": body, "error": r.json()})
            r.raise_for_status()

    except httpx.HTTPError as e:
        raise HTTPException(status_code=502, detail=f"Agent error: {e}")
