from . import crud, password_tool, models
from fastapi import HTTPException, status
from starlette.status import HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND


async def authenticate_user(connection, email: str, password: str) -> models.UserDB:
    http_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="email or password is wrong!")
    user_db = await crud.get_user_by_email(connection, email)
    if not user_db:
        raise http_exception
    if not password_tool.verify_password(password, user_db.user_hashed_password):
        raise http_exception
    return user_db
