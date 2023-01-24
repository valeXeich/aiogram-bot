from sqlalchemy import Column, Integer, String

from db.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=True)
    tg_user_id = Column(Integer, unique=True, nullable=False)