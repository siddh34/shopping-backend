from typing import Union
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from .utils.env import Settings
from .utils.database import SessionLocal, engine, Base
from .routers import user_routes, product_routes, cart_routes

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

@app.get("/", response_model=dict)
async def read_root() -> dict:
    return {"Server:": "Hi, I'm alive!"}

app.include_router(user_routes.router)
app.include_router(product_routes.router)
app.include_router(cart_routes.router)