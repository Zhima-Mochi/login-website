from pydantic import BaseSettings
import os


class Settings(BaseSettings):
    debug: bool = False
    database_url: str = os.getenv('db_url')
    database_name: str = os.getenv('db_name')
    database_user: str = os.getenv('db_user')
    database_password: str = os.getenv('db_password')


settings = Settings()
