"""Authentication endpoints."""

from __future__ import annotations

from fastapi import APIRouter, Depends

from app.models.user import User
from app.schemas.common import APIResponse
from app.schemas.user import LoginRequest, RegisterRequest, TokenResponse, UserResponse
from app.services.auth import AuthService, get_current_user

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register", response_model=APIResponse)
async def register(request: RegisterRequest, service: AuthService = Depends(AuthService)) -> APIResponse:
    """Register a new user."""
    user = await service.register(request)
    return APIResponse(
        success=True,
        message="User registered successfully",
        data=service.user_to_response(user),
    )


@router.post("/login", response_model=APIResponse)
async def login(request: LoginRequest, service: AuthService = Depends(AuthService)) -> APIResponse:
    """Login and get access token."""
    token = await service.login(request)
    return APIResponse(
        success=True,
        message="Login successful",
        data=TokenResponse(access_token=token),
    )


@router.get("/me", response_model=APIResponse)
async def get_me(current_user: User = Depends(get_current_user)) -> APIResponse:
    """Get current authenticated user."""
    return APIResponse(
        success=True,
        data=UserResponse(
            id=current_user.id,
            email=current_user.email,
            username=current_user.username,
            full_name=current_user.full_name,
            is_active=current_user.is_active,
            is_superuser=current_user.is_superuser,
            created_at=current_user.created_at,
        ),
    )
