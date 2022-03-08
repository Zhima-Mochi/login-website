from datetime import date
from enum import Enum
from fastapi import UploadFile, File
from pydantic import BaseModel, EmailStr
from typing import Optional


class UserBase(BaseModel):
    user_email: EmailStr


class UserInfoBase(UserBase):
    user_nickname: str = None
    user_birthday: date = None


class UserCreate(UserBase):
    user_password: str


class User(UserBase):
    user_id: int


class UserInfo(UserInfoBase):
    user_id: int


class UserDB(UserInfo):
    user_hashed_password: str


class UserInfoUpdate(UserInfoBase):
    pass


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    user_name: Optional[str] = None


class LoginStatus(str, Enum):
    expire = "expire"
    unauth = "unauthorized"
    invalid = "invalid token"
    auth = "authorized"
