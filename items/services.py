from sqlalchemy.orm import Session

from .models import Item
from .schemas import ItemCreate


def get_items(db: Session, skip: int = 0, limit: int = 10):
    """
    获取所有的待办事项
    :param db:
    :param skip:
    :param limit:
    :return:
    """
    return db.query(Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: ItemCreate, user_id: int):
    db_item = Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
