from sqlalchemy import create_engine
from .config.settings import settings
from databases import Database
import aioredis

async_database_url = f"mysql+aiomysql://{settings.database_user}:{settings.database_password}@{settings.database_host}/{settings.database_name}"
sync_database_url = f"mysql://{settings.database_user}:{settings.database_password}@{settings.database_host}/{settings.database_name}"
redis_url = f"redis://{settings.redis_host}:{settings.redis_port}"


database = Database(async_database_url, min_size=5, max_size=20)
sync_engine = create_engine(sync_database_url, echo=settings.debug)
redis = aioredis.from_url(redis_url, encoding="utf-8", decode_responses=True)


async def get_connection():
    async with database.connection() as connection:
        yield connection


async def get_redis_conn():
    async with redis.client() as redis_conn:
        yield redis_conn
