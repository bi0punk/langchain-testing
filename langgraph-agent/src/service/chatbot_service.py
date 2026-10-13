import datetime
from typing import Any

from src.agent.agent import ChatbotGraph


class ChatbotService:
    _chatbot_graph: ChatbotGraph | None = None

    @classmethod
    def set_chatbot_graph(cls, graph: ChatbotGraph):
        cls._chatbot_graph = graph

    @classmethod
    def _require_graph(cls) -> ChatbotGraph:
        if cls._chatbot_graph is None:
            raise RuntimeError("ChatbotGraph no inicializado")
        return cls._chatbot_graph

    @classmethod
    async def process_question(cls, question: str, user: str) -> dict[str, Any]:
        result = cls._require_graph().process_message(question, user)

        # Agregar timestamp a la respuesta
        current_time = datetime.datetime.now().isoformat()
        result["processed_timestamp"] = current_time

        return result

    @classmethod
    async def get_chat_history(cls, user: str) -> dict[str, Any]:
        history = cls._require_graph().get_chat_history(user)

        return {"user": user, "messages": history}
