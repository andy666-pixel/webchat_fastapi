from sqlmodel import select
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from models.user import User  
from db.init_db import SessionDep
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta, timezone
from typing import Annotated 
from passlib.context import CryptContext
from pydantic import BaseModel
from jose import JWTError, jwt
import os
app = APIRouter()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
<<<<<<< HEAD
ACCESS_TOKEN_EXPIRE_MINUTES = 90

oauth_scheme = OAuth2PasswordBearer(tokenUrl="/token")

=======
ACCESS_TOKEN_EXPIRE_MINUTES = 900
>>>>>>> 73c8e1f (resuelto el 401 unautorized)

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None  


class UserInDB(User):
    hashed_password: str

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

<<<<<<< HEAD
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
=======
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/token")
>>>>>>> 73c8e1f (resuelto el 401 unautorized)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return password_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return password_context.hash(password)


def get_user(db: Session, name: str):
    statement = select(User).where(User.name == name)
    user = db.exec(statement).first()
    if user:
        return UserInDB(**user.model_dump())
    return None


def authenticate_user(db: Session, name: str, password: str):
    user = get_user(db, name)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    db: Annotated[Session, Depends(SessionDep)]
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
<<<<<<< HEAD
        name = payload.get("sub")
        if name is None:
            raise credentials_exception
        token_data = TokenData(username=name) 
    except JWTError:
        raise credentials_exception
    user = get_user(db, name=token_data.username)
=======
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
    except (JWTError, ValueError, TypeError):
        raise credentials_exception

    user = get_user(db, username)  # ← Aquí el cambio correcto
>>>>>>> 73c8e1f (resuelto el 401 unautorized)
    if user is None:
        raise credentials_exception
    return user


<<<<<<< HEAD
async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)],
):
    if getattr(current_user, "disabled", False):
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
=======


async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)],
):
    return current_user
    # if getattr(current_user, "disabled", False):
    #     raise HTTPException(status_code=400, detail="Inactive user")
    
>>>>>>> 73c8e1f (resuelto el 401 unautorized)
