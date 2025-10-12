from datetime import datetime
from typing import Optional
from fastapi import APIRouter
from sqlmodel import Field, SQLModel
from fastapi import APIRouter

router = APIRouter()


class RoomMessage(SQLModel, table=True):
    id: int | None = Field(primary_key=True)
    asociated_room: str
    sender_message_name: str    
