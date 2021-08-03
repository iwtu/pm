
from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    connectionstring: str = Field(..., env='DATABASE_CONNECTIONSTRING')

settings = Settings()