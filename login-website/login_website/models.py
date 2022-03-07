from enum import Enum
from pydantic import BaseModel, EmailStr
from typing import Optional


class UserBase(BaseModel):
    user_email: EmailStr
    user_name: str


class UserCreate(UserBase):
    user_password: str


class User(UserBase):
    user_id: int


class UserDB(User):
    user_hashed_password: str


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
