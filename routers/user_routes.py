from sqlalchemy.orm import Session
from ..models.user import User
from ..schemas.user import UserUpdate, UserResponse
from fastapi import APIRouter, Depends
from ..utils.database import get_db

router = APIRouter(
    prefix="/api",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.post("/users/", response_model=dict)
def create_user(user: UserResponse, db: Session = Depends(get_db)):
    db.add(user)
    db.commit()
    return {"message": "User created successfully"}


@router.get("/users/", response_model=list[UserResponse])
def read_users(db: Session = Depends(get_db)) -> any:
    users = db.query(User).all()
    return [UserResponse.model_validate(user) for user in users]


@router.get("/users/{user_id}", response_model=UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db)) -> UserResponse:
    return db.query(User).filter(User.id == user_id).first()


@router.put("/users/{user_id}", response_model=dict)
def update_user(
    user_id: int, userUpdaterScehma: UserUpdate, db: Session = Depends(get_db)
) -> dict:
    db.query(User).filter(User.id == user_id).update(userUpdaterScehma.model_dump())
    db.commit()
    return {"message": "User updated successfully"}

@router.delete("/users/{user_id}", response_model=dict)
def delete_user(user_id: int, db: Session = Depends(get_db)) -> dict:
    db.query(User).filter(User.id == user_id).delete()
    db.commit()
    return {"message": "User deleted successfully"}
