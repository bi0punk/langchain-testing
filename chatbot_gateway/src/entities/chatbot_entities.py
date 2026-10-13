from typing import Any

from pydantic import BaseModel, Field


class MessagePayload(BaseModel):
    id: str
    timestamp: int
    from_: str = Field(alias="from")
    fromMe: bool
    body: str
    hasMedia: bool
    ack: int
    _data: dict[str, Any]


class WahaRequest(BaseModel):
    event: str
    session: str
    payload: MessagePayload
