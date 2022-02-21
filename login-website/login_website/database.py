from sqlalchemy import engine
from sqlalchemy.ext.asyncio import create_async_engine
from login_website.settings import settings
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

DATABASE_URL = f"postgresql+asyncpg://{settings.database_user}:{settings.database_password}@{settings.database_host}/{settings.database_name}"
print(DATABASE_URL)
engine = create_async_engine(DATABASE_URL, echo=settings.debug)

SessionLocal = sessionmaker(
    engine, expire_on_commit=False, autocommit=False, class_=AsyncSession)

