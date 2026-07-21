"""User schemas for request/response validation."""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, Field


# ─── Auth ──────────────────────────────────────────


class RegisterRequest(BaseModel):
    """Registration request schema."""

    email: EmailStr = Field(..., description="User email address")
    username: str = Field(..., min_length=3, max_length=50, description="Username")
    password: str = Field(..., min_length=8, max_length=128, description="Password")
    full_name: Optional[str] = Field(None, max_length=255, description="Full name")


class LoginRequest(BaseModel):
    """Login request schema."""

    username: str = Field(..., description="Username or email")
    password: str = Field(..., description="Password")


class TokenResponse(BaseModel):
    """Token response schema."""

    access_token: str
    token_type: str = "bearer"


# ─── User ──────────────────────────────────────────


class UserResponse(BaseModel):
    """User response schema."""

    id: int
    email: str
    username: str
    full_name: Optional[str] = None
    is_active: bool
    is_superuser: bool
    created_at: datetime

    model_config = {"from_attributes": True}


class UserUpdate(BaseModel):
    """User update schema."""

    full_name: Optional[str] = None
    email: Optional[EmailStr] = None
