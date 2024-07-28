from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from ..models.product import Product
from ..schemas.product import ProductResponse
from ..utils.database import get_db

router = APIRouter(
    prefix="/api",
    tags=["products"],
    responses={404: {"description": "Not found"}},
)

@router.get("/products/", response_model=list[ProductResponse])
def read_products(db: Session = Depends(get_db)) -> any:
    products = db.query(Product).all()
    return [ProductResponse.model_validate(product) for product in products]

@router.get("/products/{product_id}", response_model=ProductResponse)
def read_product(product_id: int, db: Session = Depends(get_db)) -> ProductResponse:
    return db.query(Product).filter(Product.id == product_id).first()

@router.post("/products/", response_model=dict)
def create_product(product: ProductResponse, db: Session = Depends(get_db)):
    db.add(product)
    db.commit()
    return {"message": "Product created successfully"}

@router.put("/products/{product_id}", response_model=dict)
def update_product(
    product_id: int, productUpdaterScehma: ProductResponse, db: Session = Depends(get_db)
) -> dict:
    db.query(Product).filter(Product.id == product_id).update(productUpdaterScehma.model_dump())
    db.commit()
    return {"message": "Product updated successfully"}

@router.delete("/products/{product_id}", response_model=dict)
def delete_product(product_id: int, db: Session = Depends(get_db)) -> dict:
    db.query(Product).filter(Product.id == product_id).delete()
    db.commit()
    return {"message": "Product deleted successfully"}