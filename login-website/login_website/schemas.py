from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(255), index=True, unique=True, nullable=False)
    username = Column(String(30))
    hashed_password = Column(String(255), nullable=False)
