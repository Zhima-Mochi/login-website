from unittest import result
from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from login_website import models, schemas, password
from starlette.status import HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND


async def get_user(session: AsyncSession, email: str) -> models.UserDB:
    select_query = select(schemas.User).where(
        schemas.User.email == email)
    result = await session.execute(select_query)
    user = result.scalars().first()
    if user is None:
        return user
    return models.User(**user.__dict__)


async def get_user_or_404(session: AsyncSession, email: str) -> models.UserDB:
    user = await get_user(session, email)
    if user is None:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND)
    return user


async def create_user(session: AsyncSession, user: models.User) -> models.UserDB:
    new_user = schemas.User(
        **user.dict(exclude={"password"}), hashed_password=password.get_hashed_password(user.password))
    session.add(new_user)
    await session.commit()
    return models.User(**new_user.__dict__)


async def authenticate_user_or_401(session: AsyncSession, email: str, password: str):
    user = await get_user(session, email)
    if user is None or not password.verify_password(password, user.hashed_password):
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED)
    return user
