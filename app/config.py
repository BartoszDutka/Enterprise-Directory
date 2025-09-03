from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    admin_email: str = "admin@firma.pl"
    admin_password: str = "REDACTED_SECRET"
    secret_key: str = "REDACTED_SECRET"
    database_url: str = "sqlite:///./ksiazka_tele.db"
    debug: bool = True
    
    class Config:
        env_file = ".env"


settings = Settings()
