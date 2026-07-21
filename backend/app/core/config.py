"""Application configuration management using Pydantic Settings."""

from __future__ import annotations

import json
from pathlib import Path
from typing import List, Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # ─── App ────────────────────────────────────────
    APP_NAME: str = "Hackathon Starter Kit"
    APP_ENV: str = "development"
    APP_DEBUG: bool = True
    APP_SECRET_KEY: str = "change-me-to-a-random-secret-key"
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000
    APP_CORS_ORIGINS: str = '["http://localhost:5173","http://localhost:3000"]'

    # ─── Database ───────────────────────────────────
    DATABASE_URL: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/hackathon"
    DATABASE_SYNC_URL: str = "postgresql://postgres:postgres@localhost:5432/hackathon"

    # ─── Redis ──────────────────────────────────────
    REDIS_URL: str = "redis://localhost:6379/0"

    # ─── JWT ────────────────────────────────────────
    JWT_SECRET_KEY: str = "change-me-to-a-jwt-secret"
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRATION_MINUTES: int = 1440  # 24 hours

    # ─── File Upload ────────────────────────────────
    UPLOAD_DIR: str = "uploads"
    UPLOAD_MAX_SIZE: int = 5 * 1024 * 1024  # 5MB
    UPLOAD_ALLOWED_EXTENSIONS: str = '["jpg","jpeg","png","gif","webp","pdf","doc","docx","csv","json"]'

    @property
    def cors_origins(self) -> List[str]:
        """Parse CORS origins from JSON string."""
        return json.loads(self.APP_CORS_ORIGINS)

    @property
    def upload_allowed_extensions(self) -> List[str]:
        """Parse allowed extensions from JSON string."""
        return json.loads(self.UPLOAD_ALLOWED_EXTENSIONS)

    @property
    def upload_path(self) -> Path:
        """Get the upload directory path."""
        path = Path(self.UPLOAD_DIR)
        path.mkdir(parents=True, exist_ok=True)
        return path


settings = Settings()

# Backwards compatibility aliases
get_settings = lambda: settings
