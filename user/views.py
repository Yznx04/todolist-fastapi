from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from databases import get_db
from items.schemas import ItemCreate
from items.services import create_user_item
from user.schemas import User, UserCreate
from user.services import get_user_by_email, create_users, get_users, get_user

router = APIRouter()


@router.post("/users/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_users(db=db, user=user)


@router.get("/users/", response_model=List[User])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = get_users(db, skip, limit)
    return users


@router.get("/users/<user_id>", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id)
    if db_user is None:
        raise HTTPException(
            status_code=400,
            detail="User not found"
        )
    return db_user


@router.post("/users/{user_id}/items/")
def create_item_for_user(user_id: int, item: ItemCreate, db: Session = Depends(get_db)):
    return create_user_item(db, item, user_id)
