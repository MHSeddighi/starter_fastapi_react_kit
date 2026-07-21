"""Main API v1 router combining all endpoint modules."""

from __future__ import annotations

from fastapi import APIRouter

from app.api.v1.auth import router as auth_router
from app.api.v1.uploads import router as uploads_router

router = APIRouter(prefix="/api/v1")

# Include sub-routers
router.include_router(auth_router)
router.include_router(uploads_router)


@router.get("/health", tags=["Health"])
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "service": "Hackathon Starter Kit API",
        "version": "0.1.0",
    }
