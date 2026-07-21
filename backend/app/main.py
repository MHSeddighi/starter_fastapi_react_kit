"""Hackathon Starter Kit - FastAPI Application."""

from __future__ import annotations

from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from loguru import logger

from app.api.v1.router import router as api_v1_router
from app.core.config import settings
from app.middleware.cors import setup_cors


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan: startup and shutdown events."""
    # Startup
    logger.info(f"Starting {settings.APP_NAME}")
    logger.info(f"Environment: {settings.APP_ENV}")

    # Ensure upload directory exists
    Path(settings.UPLOAD_DIR).mkdir(parents=True, exist_ok=True)

    yield

    # Shutdown
    logger.info(f"Shutting down {settings.APP_NAME}")
    from app.core.redis import close_redis
    await close_redis()


app = FastAPI(
    title=settings.APP_NAME,
    version="0.1.0",
    description="Hackathon Starter Kit - Build products fast",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan,
)

# Setup CORS
setup_cors(app)

# Include routers
app.include_router(api_v1_router)


# ─── Global Exception Handler ─────────────────────


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    """Global exception handler for unhandled exceptions."""
    logger.error(f"Unhandled exception: {exc}")
    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "message": "An unexpected error occurred",
        },
    )


# ─── Root endpoint ────────────────────────────────


@app.get("/")
async def root():
    """Root endpoint with API information."""
    return {
        "name": settings.APP_NAME,
        "version": "0.1.0",
        "docs": "/docs",
        "health": "/api/v1/health",
    }
