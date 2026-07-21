"""User repository with auth-specific queries."""

from __future__ import annotations

from typing import Optional

from sqlalchemy import select

from app.models.user import User
from app.repositories.base import BaseRepository


class UserRepository(BaseRepository[User]):
    """Repository for User model with auth-specific methods."""

    def __init__(self, session):
        super().__init__(User, session)

    async def get_by_email(self, email: str) -> Optional[User]:
        """Get a user by email."""
        result = await self.session.execute(select(User).where(User.email == email))
        return result.scalar_one_or_none()

    async def get_by_username(self, username: str) -> Optional[User]:
        """Get a user by username."""
        result = await self.session.execute(select(User).where(User.username == username))
        return result.scalar_one_or_none()

    async def get_by_username_or_email(self, login: str) -> Optional[User]:
        """Get a user by username or email."""
        result = await self.session.execute(
            select(User).where((User.username == login) | (User.email == login))
        )
        return result.scalar_one_or_none()
