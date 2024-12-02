import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL", "")
    DATABASE_NAME: str = os.getenv("DATABASE_NAME", "")
    TIME_PARSE_SCHEDULE: str = os.getenv("TIME_PARSE_SCHEDULE", 6)
    TIME_PARSE_GRADES: str = os.getenv("TIME_PARSE_GRADES", 6)

    class Config:
        env_file = ".env"


settings = Settings()