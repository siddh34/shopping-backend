from typing import Union
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from .utils.env import Settings
from sqlalchemy.orm import Session
from .utils.database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

settings = Settings()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def read_root():
    return {"Server:": "Hi, I'm alive!"}