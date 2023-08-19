"""Application settings and configuration."""


from typing import Literal

from pydantic import AnyHttpUrl, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings container."""

    model_config = SettingsConfigDict(env_prefix="COSMOS_")

    api_prefix: str = "/api"
    cors_origins: list[AnyHttpUrl] = []
    env: Literal["dev", "prod"] = "dev"
    sqlalchemy_uri: PostgresDsn | Literal["sqlite:///cosmos.db"] = "sqlite:///cosmos.db"


settings = Settings()
