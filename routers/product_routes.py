from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from ..models.product import Product
from ..schemas.product import ProductResponse, ProductCreate, ProductUpdate
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

from fastapi import HTTPException


@router.get("/products/{product_id}", response_model=ProductResponse)
def read_product(product_id: int, db: Session = Depends(get_db)) -> ProductResponse:
    product = db.query(Product).filter(Product.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return ProductResponse.model_validate(product)


@router.post("/products/", response_model=dict)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    product_data = Product(
        name=product.name,
        price=product.price,
        description=product.description,
        owner_id=product.owner_id
    )
    db.add(product_data)
    db.commit()
    db.refresh(product_data)
    return {"message": "Product created successfully"}


@router.put("/products/{product_id}", response_model=dict)
def update_product(
    product_id: int, productUpdaterScehma: ProductUpdate, db: Session = Depends(get_db)
) -> dict:
    db.query(Product).filter(Product.id == product_id).update(productUpdaterScehma.model_dump())
    db.commit()
    return {"message": "Product updated successfully"}


@router.delete("/products/{product_id}", response_model=dict)
def delete_product(product_id: int, db: Session = Depends(get_db)) -> dict:
    db.query(Product).filter(Product.id == product_id).delete()
    db.commit()
    return {"message": "Product deleted successfully"}
