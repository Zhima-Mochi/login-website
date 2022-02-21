from unittest import result
from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from login_website import models, schemas, password
from starlette.status import HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND


async def get_user_or_404(session: AsyncSession, user_id: int) -> models.UserDB:
    select_query = select(schemas.User).where(
        schemas.User.id == user_id)
    result = await session.execute(select_query)
    user = result.scalars().first()
    if user is None:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND)
    return models.User(**user.__dict__)


async def create_user(session: AsyncSession, user: models.User) -> models.UserDB:
    new_user = schemas.User(
        **user.dict(exclude={"password"}), hashed_password=password.get_hashed_password(user.password))
    session.add(new_user)
    await session.commit()
    # return await get_user_or_404(session, new_user.id)
    return models.User(**new_user.__dict__)
