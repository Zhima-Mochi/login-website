from datetime import datetime
from fastapi import Depends, HTTPException, Header, Response, status, Cookie
from jose import JWTError, jwt
from . import database, models, crud, password_tool
from .config.settings import settings


async def check_authentication(response: Response, redis_conn=Depends(database.get_redis_conn), session: str = Cookie(None)):
    if session is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, headers={
                            "Set-Cookie": "session=deleted; path=/; expires=Thu, 01 Jan 1970 00:00:00 GMT"})
    try:
        payload = jwt.decode(session, settings.secret_key, settings.algorithm)
        expire_time = payload.get("exp")
        if expire_time < datetime.now().timestamp():
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, headers={
                                "Set-Cookie": "session=deleted; path=/; expires=Thu, 01 Jan 1970 00:00:00 GMT"})
        user_email = payload.get("sub")
        redis_token = await redis_conn.get(user_email)
        if redis_token is None or redis_token != session:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, headers={
                                "Set-Cookie": "session=deleted; path=/; expires=Thu, 01 Jan 1970 00:00:00 GMT"})
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, headers={
                            "Set-Cookie": "session=deleted; path=/; expires=Thu, 01 Jan 1970 00:00:00 GMT"})
    return user_email


async def is_login(response: Response, user_email=Depends(check_authentication)):
    return True


async def get_user_info(user_email=Depends(check_authentication), connection=Depends(database.get_connection)):
    userDB = await crud.get_user_by_email(connection, user_email)
    return userDB


async def csrf_protection(x_csrftoken: str = Header(None), csrftoken: str = Cookie(None), session: str = Cookie(None), user_email=Depends(check_authentication)):
    if not password_tool.verify_csrf_token_and_session_token(csrftoken, session) or x_csrftoken != csrftoken:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, headers={
                            "Set-Cookie": "session=deleted; path=/; expires=Thu, 01 Jan 1970 00:00:00 GMT"})
