from datetime import datetime
from typing import Optional
from fastapi import APIRouter
from sqlmodel import Field, SQLModel
from fastapi import APIRouter

router = APIRouter()


class Room(SQLModel, table=True):
    id: int | None = Field(primary_key=True)
    room_name: str
    users: str
    sender_message_name: str    
