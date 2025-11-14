from datetime import datetime
from typing import Optional
from fastapi import APIRouter
from sqlmodel import Field, Relationship, SQLModel
from fastapi import APIRouter
from models import Room

router = APIRouter()


class Room_Message(SQLModel, table=True):
    id: int | None = Field(primary_key=True)
    asociated_room: "Room" = Relationship()
    sender_message_name: str    
    content: str