from sqlalchemy import Column, ForeignKey, String, Integer, Date, BLOB
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    user_email = Column(String(255), index=True, unique=True, nullable=False)
    user_nickname = Column(String(30), nullable=True)
    user_birthday = Column(Date, nullable=True)
    user_hashed_password = Column(String(255), nullable=False)


class UserProfile(Base):
    __tablename__ = 'users_profile'
    user_id = Column(Integer, ForeignKey('users.user_id'), primary_key=True)
    user_profile = Column(BLOB, nullable=True)
