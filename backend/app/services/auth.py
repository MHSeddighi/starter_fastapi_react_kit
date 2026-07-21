"""Authentication service."""

from __future__ import annotations

from typing import Optional

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.security import (
    create_access_token,
    decode_access_token,
    hash_password,
    verify_password,
)
from app.models.user import User
from app.repositories.user import UserRepository
from app.schemas.user import LoginRequest, RegisterRequest, UserResponse

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")


class AuthService:
    """Service handling authentication logic."""

    def __init__(self, session: AsyncSession):
        self.repo = UserRepository(session)

    async def register(self, request: RegisterRequest) -> User:
        """Register a new user."""
        # Check if email already exists
        existing = await self.repo.get_by_email(request.email)
        if existing:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email already registered",
            )

        # Check if username already exists
        existing = await self.repo.get_by_username(request.username)
        if existing:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Username already taken",
            )

        # Create user
        user = await self.repo.create(
            email=request.email,
            username=request.username,
            hashed_password=hash_password(request.password),
            full_name=request.full_name,
        )
        return user

    async def login(self, request: LoginRequest) -> str:
        """Authenticate user and return JWT token."""
        user = await self.repo.get_by_username_or_email(request.username)
        if not user or not verify_password(request.password, user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials",
            )
        if not user.is_active:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Account is inactive",
            )
        return create_access_token({"sub": str(user.id)})

    async def get_current_user(self, token: str) -> User:
        """Get the current user from a JWT token."""
        payload = decode_access_token(token)
        if payload is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid or expired token",
            )

        user_id = payload.get("sub")
        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token payload",
            )

        user = await self.repo.get(int(user_id))
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found",
            )
        if not user.is_active:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Account is inactive",
            )
        return user

    @staticmethod
    def user_to_response(user: User) -> UserResponse:
        """Convert User model to response schema."""
        return UserResponse(
            id=user.id,
            email=user.email,
            username=user.username,
            full_name=user.full_name,
            is_active=user.is_active,
            is_superuser=user.is_superuser,
            created_at=user.created_at,
        )


async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: AsyncSession = Depends(get_db),
) -> User:
    """Dependency to get the current authenticated user."""
    service = AuthService(db)
    return await service.get_current_user(token)
