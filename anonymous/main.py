from fastapi import FastAPI
import psycopg2
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from . import models
from . import schemas
from .database import SessionLocal
from . import utils
from .router import user,auth,senders

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router)
app.include_router(auth.router)
app.include_router(senders.router)

