from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    admin_email: str = "admin@firma.pl"
    admin_password: str
    secret_key: str
    database_url: str = "sqlite:///./ksiazka_tele.db"
    debug: bool = False
    cookie_secure: bool = True
    
    class Config:
        env_file = ".env"


settings = Settings()
