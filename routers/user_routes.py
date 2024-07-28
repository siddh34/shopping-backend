from sqlalchemy.orm import Session
from models.user import User
from schemas.user import UserUpdate
from fastapi import APIRouter, Depends
from utils.database import get_db

router = APIRouter()


@router.post("/users/")
def create_user(user: User, db: Session = Depends(get_db)):
    db.add(user)
    db.commit()
    return {"message": "User created successfully"}


@router.get("/users/")
def read_users(db: Session = get_db()):
    return db.query(User).all()


@router.get("/users/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    return db.query(User).filter(User.id == user_id).first()


@router.put("/users/{user_id}")
@router.put("/users/{user_id}")
def update_user(
    user_id: int, userUpdaterScehma: UserUpdate, db: Session = Depends(get_db)
):
    db.query(User).filter(User.id == user_id).update(userUpdaterScehma.model_dump())
    db.commit()
    return {"message": "User updated successfully"}


@router.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db.query(User).filter(User.id == user_id).delete()
    db.commit()
    return {"message": "User deleted successfully"}
