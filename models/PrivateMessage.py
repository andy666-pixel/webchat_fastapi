from datetime import datetime
from typing import Optional
from fastapi import APIRouter
from sqlmodel import Field, SQLModel
from fastapi import APIRouter

router = APIRouter()


class Message(SQLModel, table=True):
    id: int | None = Field(primary_key=True)
    content: str
    sender_name: str
    receiver_name: Optional[str] = Field(default=None)
    timestamp: datetime = Field(default_factory=datetime.utcnow)