from pydantic import BaseModel

class User(BaseModel):
    id: int
    email: str
    hashed_password: str
    is_active: bool

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    email: str
    hashed_password: str
    is_active: bool

    class Config:
        orm_mode = True

class UserUpdate(BaseModel):
    email: str
    hashed_password: str
    is_active: bool

    class Config:
        orm_mode = True

class UserDelete(BaseModel):
    id: int

    class Config:
        orm_mode = True