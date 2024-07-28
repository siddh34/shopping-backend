from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
database_path = os.path.join(base_dir, "../database/database.db")
absolute_database_url = f"sqlite:///{database_path}"

SQLALCHEMY_DATABASE_URL = absolute_database_url

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
