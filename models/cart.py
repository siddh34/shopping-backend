from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from utils.database import Base


class Cart(Base):
    __tablename__ = "cart"

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("product.id"))
    product = relationship("Product", back_populates="products")
