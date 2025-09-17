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

app = APIRouter()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 10


oauth_scheme = OAuth2PasswordBearer(tokenUrl="/users/token")


@app.post("/cookie/")
def create_cookie(access_token: Annotated[str, Depends(oauth_scheme)]):
    content = {"Content-Language": "en-US", "Authorization": f"Bearer {access_token}"}
    response = JSONResponse(content=content)
    response.set_cookie(key="session", value=content)
    return response


@app.get("/headers/")
def get_headers(access_token: Annotated[str, Depends(oauth_scheme)]):
    headers = {"Content-Language": "en-US", "Authorization": f"Bearer {access_token}"}
    session_header = JSONResponse(headers=headers)
    return session_header


@app.post("/register")
def create_user(user: User, session: Session = Depends(SessionDep)):
    hashed_password = get_password_hash(user.hashed_password)
    user.hashed_password = hashed_password
<<<<<<< HEAD
    if hasattr(user, "hashed_password"):
     delattr(user, "hashed_password")
=======
    # if hasattr(user, "hashed_password"):
    #    delattr(user, "hashed_password")
>>>>>>> 73c8e1f (resuelto el 401 unautorized)
    session.add(user)
    session.commit()
    session.refresh(user)
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


@app.post("/login")
def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()], 
<<<<<<< HEAD
    db: Annotated[Session, Depends(SessionDep)]):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise InvalidCredentialsException
    return {"message": "Login exitoso", "info1": user.id ,"info": user.name}
=======
    autenticated_user: Annotated[User, Depends(get_current_active_user)],
    db: Annotated[Session, Depends(SessionDep)]):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
     raise InvalidCredentialsException
    return autenticated_user
    # return {"message": "Login exitoso", "info1": user.id ,"info": user.name}
>>>>>>> 73c8e1f (resuelto el 401 unautorized)
    # return RedirectResponse(url="/users/home/me")
    
             
@app.get("/home/me")
async def user_me(
    autenticated_user: Annotated[User, Depends(get_current_active_user)],):
    return autenticated_user
    




         