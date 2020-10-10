from sqlalchemy.orm import Session

from user.modles import User
from user.schemas import UserCreate


def get_user(db: Session, user_id: int):
    """
    根据用户ID获取用户
    :param db:
    :param user_id:
    :return:
    """
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    """
    根据email获取用户
    :param db:
    :param email:
    :return:
    """
    return db.query(User).filter(User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 10):
    """
    获取所有用户
    :param db:
    :param skip:
    :param limit:
    :return:
    """
    return db.query(User).offset(skip).limit(limit).all()


def create_users(db: Session, user: UserCreate):
    """
    创建用户
    :param db:
    :param user:
    :return:
    """
    fake_hashed_password = user.password + "notrealllyhashed"
    db_user = User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
