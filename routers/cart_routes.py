from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from ..models.cart import Cart
from ..schemas.cart import CartResponse
from ..utils.database import get_db

router = APIRouter(
    prefix="/api",
    tags=["cart"],
    responses={404: {"description": "Not found"}},
)

@router.get("/cart/", response_model=list[CartResponse])
def read_cart(db: Session = Depends(get_db)) -> any:
    carts = db.query(Cart).all()
    return [CartResponse.model_validate(cart) for cart in carts]

@router.get("/cart/{cart_id}", response_model=CartResponse)
def read_cart(cart_id: int, db: Session = Depends(get_db)) -> CartResponse:
    return db.query(Cart).filter(Cart.id == cart_id).first()

@router.post("/cart/", response_model=dict)
def create_cart(cart: CartResponse, db: Session = Depends(get_db)):
    db.add(cart)
    db.commit()
    return {"message": "Cart created successfully"}

@router.put("/cart/{cart_id}", response_model=dict)
def update_cart(
    cart_id: int, cartUpdaterScehma: CartResponse, db: Session = Depends(get_db)
) -> dict:
    db.query(Cart).filter(Cart.id == cart_id).update(cartUpdaterScehma.model_dump())
    db.commit()
    return {"message": "Cart updated successfully"}

@router.delete("/cart/{cart_id}", response_model=dict)
def delete_cart(cart_id: int, db: Session = Depends(get_db)) -> dict:
    db.query(Cart).filter(Cart.id == cart_id).delete()
    db.commit()
    return {"message": "Cart deleted successfully"}

@router.get("/cart/user/{user_id}", response_model=list[CartResponse])
def read_cart_by_user(user_id: int, db: Session = Depends(get_db)) -> any:
    carts = db.query(Cart).filter(Cart.user_id == user_id).all()
    return [CartResponse.model_validate(cart) for cart in carts]

@router.get("/cart/product/{product_id}", response_model=list[CartResponse])
def read_cart_by_product(product_id: int, db: Session = Depends(get_db)) -> any:
    carts = db.query(Cart).filter(Cart.product_id == product_id).all()
    return [CartResponse.model_validate(cart) for cart in carts]

@router.get("/cart/user/{user_id}/product/{product_id}", response_model=CartResponse)
def read_cart_by_user_product(user_id: int, product_id: int, db: Session = Depends(get_db)) -> CartResponse:
    return db.query(Cart).filter(Cart.user_id == user_id, Cart.product_id == product_id).first()