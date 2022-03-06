from pydantic import BaseSettings


class Settings(BaseSettings):
    debug: bool = False
    database_host: str
    database_name: str
    database_user: str
    database_password: str
    # openssl rand -hex 32
    secret_key: str
    redis_host: str
    redis_port: str

    class Config:
        env_file = ".env"


settings = Settings()
