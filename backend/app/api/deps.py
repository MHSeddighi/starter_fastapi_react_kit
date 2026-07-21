"""Shared API dependencies."""

from __future__ import annotations

from typing import AsyncGenerator

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.services.auth import AuthService, get_current_user


async def get_auth_service(db: AsyncSession = Depends(get_db)) -> AuthService:
    """Dependency to get an AuthService instance."""
    return AuthService(db)
