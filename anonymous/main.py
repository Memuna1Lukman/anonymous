from fastapi import FastAPI
import psycopg2
from sqlalchemy.orm import Session

from . import models
from . import schemas
from .database import SessionLocal
from . import utils
from .router import user,auth

app = FastAPI()


app.include_router(user.router)
app.include_router(auth.router)


