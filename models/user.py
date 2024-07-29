from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from ..utils.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    products = relationship("Product", back_populates="owner")
    carts = relationship("Cart", back_populates="user")
