from pydantic import BaseSettings
import os


class Settings(BaseSettings):
    debug: bool = False
    database_host: str = os.environ['db_host']
    database_name: str = os.environ['db_name']
    database_user: str = os.environ['db_user']
    database_password: str = os.environ['db_password']


settings = Settings()
