import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8001
    GOOGLE_API_KEY: str
    API_KEY: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()