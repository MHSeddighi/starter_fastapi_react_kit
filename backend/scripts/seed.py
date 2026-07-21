"""Database seeder script.

Usage: uv run python -m scripts.seed
"""

from __future__ import annotations

import asyncio

from loguru import logger

from app.core.database import async_session_factory
from app.core.security import hash_password
from app.models.user import User


async def seed_database() -> None:
    """Seed the database with initial data."""
    logger.info("🌱 Seeding database...")

    async with async_session_factory() as session:
        # Create admin user
        admin = User(
            email="admin@example.com",
            username="admin",
            hashed_password=hash_password("admin123456"),
            full_name="Admin User",
            is_active=True,
            is_superuser=True,
        )
        session.add(admin)

        # Create demo user
        demo = User(
            email="demo@example.com",
            username="demo",
            hashed_password=hash_password("demo123456"),
            full_name="Demo User",
            is_active=True,
            is_superuser=False,
        )
        session.add(demo)

        await session.commit()
        logger.info("✅ Database seeded successfully!")
        logger.info("   Admin: admin / admin123456")
        logger.info("   Demo:  demo / demo123456")


if __name__ == "__main__":
    asyncio.run(seed_database())
