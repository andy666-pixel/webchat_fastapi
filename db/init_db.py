from sqlmodel import Session, create_engine
from typing import Annotated
from fastapi import Depends, APIRouter
import os
from dotenv import load_dotenv
from sqlmodel import Session, create_engine
from typing import Generator



#Database creation and connection
#//---------------------------------------------------------------------------------------------------------//#
router = APIRouter()
load_dotenv()
DB_URL = os.getenv("DB_URL")
SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = os.getenv("DEBUG") == "True"



DATABASE_URL = DB_URL

# Crear el motor de base de datos
engine = create_engine(DATABASE_URL, echo=True)

# Función de dependencia para usar como instancia de sesión
def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session

# resultado para usar en las rutas
SessionDep = get_session
#//---------------------------------------------------------------------------------------------------------//#
#Database creation and connection
