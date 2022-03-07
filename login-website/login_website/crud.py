from fastapi import HTTPException
from sqlalchemy import select, insert, update, delete
from login_website import models, schemas, password_tool
from starlette.status import HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND


async def get_user_by_id(connection, user_id: int) -> models.UserDB:
    stmt = select(schemas.User).where(
        schemas.User.user_id == user_id)
    result = await connection.fetch_one(stmt)
    if result is None:
        return result
    return models.UserDB(**result)


async def get_user_by_email(connection, user_email: str) -> models.UserDB:
    stmt = select(schemas.User).where(
        schemas.User.user_email == user_email)
    result = await connection.fetch_one(stmt)
    if result is None:
        return result
    return models.UserDB(**result)



async def create_user(connection, user: models.User) -> models.UserDB:
    stmt = insert(schemas.User).values(
        **user.dict(exclude={"user_password"}), user_hashed_password=password_tool.get_hashed_password(user.user_password))
    user_id = await connection.execute(stmt)
    return await get_user_by_id(connection, user_id)

async def get_user_or_404(connection, user_email: str) -> models.UserDB:
    user = await get_user_by_email(connection, user_email)
    if user is None:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND)
    return user
