from fastapi import Depends
from sqlmodel import Session
from db.init_db import SessionDep
from services.auth import *
from services.helpers import save_and_refresh
from models.Room import Room
from fastapi import Depends, WebSocket, WebSocketDisconnect
from sqlmodel import Session
from db.init_db import SessionDep
from models.Message import Message
from fastapi.encoders import jsonable_encoder
from services.helpers import save_and_refresh
chat = APIRouter()


@chat.post("/create_room")
def create_room(room: Room, session: Session = Depends(SessionDep)):
    save_and_refresh(session, room)
    return room



class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []
    
    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)
    
    async def broadcast(self, message: Message):
        for connection in self.active_connections:
            await connection.send_json(jsonable_encoder(message))

    async def global_message(self, message: Message, websocket: WebSocket):
        await websocket.send_json(jsonable_encoder(message))
    
    async def room(self, message: Message, websocket: WebSocket):
        await websocket.send_json(jsonable_encoder(message))

    
manager = ConnectionManager()

@chat.websocket("/sendmessage/{username}")
async def global_messages(
 websocket: WebSocket,
 username: str,
 session: Session = Depends(SessionDep),
 ):
    await manager.connect(websocket)
    try: 
        while True:
            data = await websocket.receive_json() 
            message_data = Message(**data)
            await manager.global_message(message_data, websocket)
            await manager.broadcast(message_data)
            save_and_refresh(session, message_data)
    except WebSocketDisconnect:
        manager.disconnect(websocket)

@chat.websocket("/sendmessage/room/{room}")
async def join_room(
 websocket: WebSocket, 
 session: Session = Depends(SessionDep),
 ):
    await manager.connect(websocket)
    try: 
        while True:
            data = await websocket.receive_json() 
            message_data = Message(**data)
            await manager.room(message_data, websocket)
            await manager.broadcast(message_data)
            save_and_refresh(session, message_data)
    except WebSocketDisconnect:
        manager.disconnect(websocket)