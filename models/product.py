from sqlalchemy import Float, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..utils.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Float, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="products")
    product = relationship("Cart", back_populates="product")
