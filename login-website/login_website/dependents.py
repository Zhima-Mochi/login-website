from datetime import datetime
from fastapi import Depends, HTTPException, Response, status, Cookie
from jose import JWTError, jwt
from . import database, models
from .config.settings import settings


async def get_login_status(response: Response, redis_conn=Depends(database.get_redis_conn), session: str = Cookie(None)):
    try:
        payload = jwt.decode(session, settings.secret_key, settings.algorithm)
        expire_time = payload.get("exp")
        if expire_time < datetime.now().timestamp():
            return models.LoginStatus.expire
        user_email = payload.get("sub")
        redis_token = await redis_conn.get(user_email)
        if redis_token is None or redis_token != session:
            return models.LoginStatus.unauth
    except JWTError:
        return models.LoginStatus.unauth
    return models.LoginStatus.auth
