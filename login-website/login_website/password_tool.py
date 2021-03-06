import base64
from datetime import timedelta, datetime
from passlib.context import CryptContext
from typing import Optional
from jose import JWTError, jwt
from .config.settings import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

secret_key = settings.secret_key
algorithm = settings.algorithm


def get_hashed_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict, expire_delta: Optional[timedelta] = None):
    to_encode_data = data.copy()
    if expire_delta:
        expire_time = datetime.now()+expire_delta
    else:
        expire_time = datetime.now()+timedelta(hours=2)
    to_encode_data.update({"exp": expire_time})
    encoded_jwt = jwt.encode(to_encode_data, secret_key, algorithm)
    return (encoded_jwt, expire_time)


def create_csrf_token(jwt_token: str):
    token = jwt_token[::2]
    return token


def verify_csrf_token_and_session_token(csrf_token, session_token: str):
    return csrf_token == session_token[::2]
