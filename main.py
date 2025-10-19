from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers.user import app as users_router
from routers.websocket_routes import chat
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(users_router, prefix="/users", tags=["Users"])
app.include_router(chat, prefix="/chat", tags=["Chat"])
app.mount("/static", StaticFiles(directory="static", html=True), name="static")

