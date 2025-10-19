from fastapi import APIRouter, Depends, HTTPException, status, Header
from sqlmodel import Session
from models.user import User  
from db.init_db import SessionDep
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import timedelta
from typing import Annotated 
from services.auth import *
from fastapi_login.exceptions import InvalidCredentialsException
import os
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from services.helpers import save_and_refresh
app = APIRouter()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 100


oauth_scheme = OAuth2PasswordBearer(tokenUrl="/users/token")

@app.post("/register")
def create_user(user: User, session: Session = Depends(SessionDep)):
    hashed_password = get_password_hash(user.hashed_password)
    user.hashed_password = hashed_password
    save_and_refresh(session, user)
    return user


@app.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Annotated[Session, Depends(SessionDep)], ) -> Token:
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password", 
            headers={"WWW-Authenticate": "Bearer"},
            )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user.name}, expires_delta=access_token_expires)
    token = Token(access_token=access_token, token_type="bearer") 
    return token
             
@app.get("/home/me")
async def user_me(
    autenticated_user: Annotated[User, Depends(get_current_user)],):
    return autenticated_user
    




         