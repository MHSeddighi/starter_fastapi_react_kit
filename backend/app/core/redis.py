"""Redis client wrapper for caching and session support."""

from __future__ import annotations

import json
from typing import Any, Callable, Optional, TypeVar

from loguru import logger
from redis.asyncio import Redis

from app.core.config import settings

T = TypeVar("T")

redis_client: Optional[Redis] = None


async def get_redis() -> Redis:
    """Get or create the Redis connection."""
    global redis_client
    if redis_client is None:
        try:
            redis_client = Redis.from_url(
                settings.REDIS_URL,
                decode_responses=True,
                socket_connect_timeout=2,
            )
            await redis_client.ping()
            logger.info("Connected to Redis")
        except Exception as e:
            logger.warning(f"Redis connection failed: {e}. Caching disabled.")
            redis_client = None
    return redis_client


async def close_redis() -> None:
    """Close the Redis connection."""
    global redis_client
    if redis_client:
        await redis_client.close()
        redis_client = None
        logger.info("Redis connection closed")


async def cache_get(key: str) -> Optional[Any]:
    """Get a value from cache."""
    client = await get_redis()
    if client is None:
        return None
    try:
        value = await client.get(key)
        if value:
            return json.loads(value)
    except Exception as e:
        logger.warning(f"Cache get error: {e}")
    return None


async def cache_set(key: str, value: Any, ttl: int = 300) -> bool:
    """Set a value in cache with TTL (seconds)."""
    client = await get_redis()
    if client is None:
        return False
    try:
        await client.setex(key, ttl, json.dumps(value))
        return True
    except Exception as e:
        logger.warning(f"Cache set error: {e}")
    return False


async def cache_delete(key: str) -> bool:
    """Delete a key from cache."""
    client = await get_redis()
    if client is None:
        return False
    try:
        await client.delete(key)
        return True
    except Exception as e:
        logger.warning(f"Cache delete error: {e}")
    return False


async def cache_get_or_set(key: str, func: Callable[[], T], ttl: int = 300) -> T:
    """Get from cache or compute and cache."""
    cached = await cache_get(key)
    if cached is not None:
        return cached
    value = await func() if hasattr(func, "__call__") else func()
    await cache_set(key, value, ttl)
    return value
