from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers.user import app as users_router
<<<<<<< HEAD
app = FastAPI()

app.include_router(users_router, prefix="/users", tags=["Users"])
=======
from services.chat import app as chat
app = FastAPI()

app.include_router(users_router, prefix="/users", tags=["Users"])
app.include_router(chat, tags=["Chat"])
>>>>>>> 73c8e1f (resuelto el 401 unautorized)
app.mount("/static", StaticFiles(directory="static", html=True), name="static")


