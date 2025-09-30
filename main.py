from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers.user import app as users_router
from services.chat import app as chat
app = FastAPI()

app.include_router(users_router, prefix="/users", tags=["Users"])
app.include_router(chat, tags=["Chat"])
app.mount("/static", StaticFiles(directory="static", html=True), name="static")


