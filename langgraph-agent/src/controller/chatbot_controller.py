from typing import Any

from fastapi import HTTPException

from src.entities.chatbot_entities import ChatbotRequest
from src.service.chatbot_service import ChatbotService


class ChatbotController:
    @staticmethod
    async def process_chatbot_request(request: ChatbotRequest) -> dict[str, Any]:
        try:
            return await ChatbotService.process_question(
                question=request.question, user=request.user
            )
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Error processing request: {str(e)}"
            ) from e

    @staticmethod
    async def get_chat_history(user: str) -> dict[str, Any]:
        return await ChatbotService.get_chat_history(user)
