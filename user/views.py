from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from databases import get_db
from user.schemas import User, UserCreate
from user.services import get_user_by_email, create_users, get_users

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
