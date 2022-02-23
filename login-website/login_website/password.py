from base64 import encode
from datetime import timedelta, datetime
from passlib.context import CryptContext
from typing import Optional
from jose import JWTError, jwt
from login_website.settings import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

secret_key = settings.secret
algorithm = "HS256"


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
    return encoded_jwt
