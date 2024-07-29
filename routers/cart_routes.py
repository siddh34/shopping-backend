from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from ..models.cart import Cart
from ..schemas.cart import CartResponse, CartCreate, CartUpdate
from ..utils.database import get_db

router = APIRouter(
    prefix="/api",
    tags=["cart"],
    responses={404: {"description": "Not found"}},
)

@router.get("/cart/", response_model=list[CartResponse])
def read_cart(db: Session = Depends(get_db)) -> any:
    carts = db.query(Cart).all()
    print(carts)
    return [CartResponse.model_validate(cart) for cart in carts]


@router.get("/cart/{cart_id}", response_model=CartResponse)
def read_cart(cart_id: int, db: Session = Depends(get_db)) -> CartResponse:
    cart = db.query(Cart).filter(Cart.id == cart_id).first()
    if cart is None:
        raise HTTPException(status_code=404, detail="Cart not found")
    return CartResponse.model_validate(cart)


@router.post("/cart/", response_model=dict)
def create_cart(cart: CartCreate, db: Session = Depends(get_db)):
    cart_data = Cart(
        user_id=cart.user_id, quantity=cart.quantity, product_id=cart.product_id
    )
    db.add(cart_data)
    db.commit()
    db.refresh(cart_data)
    return {"message": "Cart created successfully"}


@router.put("/cart/{cart_id}", response_model=dict)
def update_cart(
    cart_id: int, cartUpdaterScehma: CartUpdate, db: Session = Depends(get_db)
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
    if carts is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return [CartResponse.model_validate(cart) for cart in carts]

@router.get("/cart/product/{product_id}", response_model=list[CartResponse])
def read_cart_by_product(product_id: int, db: Session = Depends(get_db)) -> any:
    carts = db.query(Cart).filter(Cart.product_id == product_id).all()
    return [CartResponse.model_validate(cart) for cart in carts]

from fastapi import HTTPException


@router.get("/cart/user/{user_id}/product/{product_id}", response_model=CartResponse)
def read_cart_by_user_product(
    user_id: int, product_id: int, db: Session = Depends(get_db)
) -> CartResponse:
    cart = (
        db.query(Cart)
        .filter(Cart.user_id == user_id, Cart.product_id == product_id)
        .first()
    )
    if cart is None:
        raise HTTPException(status_code=404, detail="Cart not found")
    return CartResponse.model_validate(cart)
