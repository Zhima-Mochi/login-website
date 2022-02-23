from pydantic import BaseSettings
import os


class Settings(BaseSettings):
    debug: bool = False
    database_host: str 
    database_name: str 
    database_user: str 
    database_password: str 
    secret_key: str


settings = Settings()
