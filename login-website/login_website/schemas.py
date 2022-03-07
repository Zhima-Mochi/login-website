from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    user_email = Column(String(255), index=True, unique=True, nullable=False)
    user_name = Column(String(30))
    user_hashed_password = Column(String(255), nullable=False)
