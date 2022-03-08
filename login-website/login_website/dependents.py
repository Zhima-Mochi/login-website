from datetime import datetime
from fastapi import Depends, HTTPException, Response, status, Cookie
from jose import JWTError, jwt
from . import database, models, crud
from .config.settings import settings


async def check_authentication(response: Response, redis_conn=Depends(database.get_redis_conn), session: str = Cookie(None)):
    if session is None:
        response.delete_cookie(key="session")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    try:
        payload = jwt.decode(session, settings.secret_key, settings.algorithm)
        expire_time = payload.get("exp")
        if expire_time < datetime.now().timestamp():
            response.delete_cookie(key="session")
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
        user_email = payload.get("sub")
        redis_token = await redis_conn.get(user_email)
        if redis_token is None or redis_token != session:
            response.delete_cookie(key="session")
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    except JWTError:
        response.delete_cookie(key="session")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return user_email


async def is_login(response: Response, user_email=Depends(check_authentication)):
    return True


async def get_user_info(user_email=Depends(check_authentication), connection=Depends(database.get_connection)):
    userDB = await crud.get_user_by_email(connection, user_email)
    return userDB
