from fastapi import APIRouter, Depends, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from sqlmodel import Session
from db.init_db import SessionDep
from models.user import User
from services.auth import get_current_user
from typing import Annotated
from models.Message import Message
from fastapi.encoders import jsonable_encoder
app = APIRouter()

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Websocket Demo</title>
           <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">

    </head>
    <body>
    <div class="container mt-3">
        <h1>FastAPI WebSocket Chat</h1>
        <h2>Your ID: <span id="ws-id"></span></h2>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" class="form-control" id="messageText" autocomplete="off"/>
            <button class="btn btn-outline-primary mt-2">Send</button>
        </form>
        <ul id='messages' class="mt-5">
        </ul>
        
    </div>
    
        <script>
            var client_id = Date.now()
            document.querySelector("#ws-id").textContent = client_id;
            var ws = new WebSocket(`ws://localhost:8000/ws/${client_id}`);
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(JSON.stringify({ message: input.value }))
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""


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


@app.get("/")
async def get():
    return HTMLResponse(html)


@app.websocket("/ws/{username}")
async def global_messages(
 websocket: WebSocket, 
 session: Session = Depends(SessionDep),
 ):
    await manager.connect(websocket)
    try: 
        while True:
            data = await websocket.receive_json() 
            message_data = Message(**data)
            await manager.global_message(message_data, websocket)
            await manager.broadcast(message_data)
            session.add(message_data)
            session.commit()
            session.refresh(message_data)            
    except WebSocketDisconnect:
        manager.disconnect(websocket)




@app.websocket("/ws/{room}")
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
            session.add(message_data)
            session.commit()
            session.refresh(message_data)            
    except WebSocketDisconnect:
        manager.disconnect(websocket)
 