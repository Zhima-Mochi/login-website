from sqlalchemy import engine
from sqlalchemy.ext.asyncio import create_async_engine
from login_website.settings import settings
from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

DATABASE_URL = f"postgresql+asyncpg://{settings.database_user}:{settings.database_password}@{settings.database_url}/{settings.database_name}"

engine = create_async_engine(DATABASE_URL, echo=settings.debug)

SessionLocal = sessionmaker(
    engine, expire_on_commit=False, autocommit=False, class_=AsyncSession)

Base = declarative_base()
