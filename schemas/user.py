from pydantic import BaseModel

class UserResponse(BaseModel):
    id: int
    email: str
    is_active: bool

    class Config:
        from_attributes = True


class UserCreate(BaseModel):
    email: str
    hashed_password: str
    is_active: bool

    class Config:
        from_attributes = True

class UserUpdate(BaseModel):
    email: str
    hashed_password: str
    is_active: bool

    class Config:
        from_attributes = True

class UserDelete(BaseModel):
    id: int

    class Config:
        from_attributes = True
