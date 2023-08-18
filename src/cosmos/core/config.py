"""Application settings and configuration."""


from pydantic import AnyHttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings container."""

    model_config = SettingsConfigDict(env_prefix="COSMOS_")

    api_prefix: str = "/api"
    cors_origins: list[AnyHttpUrl] = []


settings = Settings()
