"""Common API response schemas."""

from __future__ import annotations

from typing import Any, Dict, Generic, List, Optional, TypeVar

from pydantic import BaseModel

T = TypeVar("T")


class APIResponse(BaseModel):
    """Standard API response wrapper."""

    success: bool = True
    message: str = "OK"
    data: Optional[Any] = None


class PaginatedResponse(BaseModel, Generic[T]):
    """Paginated response wrapper."""

    success: bool = True
    data: List[T]
    total: int
    page: int
    page_size: int
    total_pages: int


class ErrorResponse(BaseModel):
    """Error response wrapper."""

    success: bool = False
    message: str = "An error occurred"
    details: Optional[Dict[str, Any]] = None
