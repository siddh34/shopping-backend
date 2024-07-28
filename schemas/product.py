from pydantic import BaseModel

class ProductResponse(BaseModel):
    id: int
    name: str
    price: float
    description: str
    is_active: bool

    class Config:
        from_attributes = True

class ProductCreate(BaseModel):
    name: str
    price: float
    description: str
    is_active: bool

    class Config:
        from_attributes = True

class ProductUpdate(BaseModel):
    name: str
    price: float
    description: str
    is_active: bool

    class Config:
        from_attributes = True

class ProductDelete(BaseModel):
    id: int

    class Config:
        from_attributes = True
