from . import crud, password_tool, models
from fastapi import HTTPException
from starlette.status import HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND


async def authenticate_user(connection, email: str, password: str) -> models.UserDB:
    user_db = await crud.get_user_by_email(connection, email)
    return user_db
