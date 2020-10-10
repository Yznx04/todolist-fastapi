from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from databases import Base


class User(Base):
    """用户的数据库模型"""
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_activate = Column(Boolean, default=True)
    items = relationship("Item", back_populates="owner")

