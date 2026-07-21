"""Base repository with common CRUD operations."""

from __future__ import annotations

from typing import Any, Dict, Generic, List, Optional, Type, TypeVar

from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import Base

ModelType = TypeVar("ModelType", bound=Base)


class BaseRepository(Generic[ModelType]):
    """Base repository with common database operations."""

    def __init__(self, model: Type[ModelType], session: AsyncSession):
        self.model = model
        self.session = session

    async def get(self, id: int) -> Optional[ModelType]:
        """Get a record by ID."""
        result = await self.session.execute(select(self.model).where(self.model.id == id))
        return result.scalar_one_or_none()

    async def get_all(
        self,
        skip: int = 0,
        limit: int = 100,
        filters: Optional[Dict[str, Any]] = None,
        order_by: Optional[str] = None,
    ) -> List[ModelType]:
        """Get all records with pagination and optional filtering."""
        query = select(self.model)

        if filters:
            for key, value in filters.items():
                if hasattr(self.model, key):
                    query = query.where(getattr(self.model, key) == value)

        if order_by and hasattr(self.model, order_by.lstrip("-")):
            col = getattr(self.model, order_by.lstrip("-"))
            query = query.order_by(col.desc() if order_by.startswith("-") else col)

        query = query.offset(skip).limit(limit)
        result = await self.session.execute(query)
        return list(result.scalars().all())

    async def create(self, **kwargs) -> ModelType:
        """Create a new record."""
        obj = self.model(**kwargs)
        self.session.add(obj)
        await self.session.flush()
        await self.session.refresh(obj)
        return obj

    async def update(self, id: int, **kwargs) -> Optional[ModelType]:
        """Update a record by ID."""
        obj = await self.get(id)
        if obj is None:
            return None
        for key, value in kwargs.items():
            if value is not None and hasattr(obj, key):
                setattr(obj, key, value)
        await self.session.flush()
        await self.session.refresh(obj)
        return obj

    async def delete(self, id: int) -> bool:
        """Delete a record by ID."""
        obj = await self.get(id)
        if obj is None:
            return False
        await self.session.delete(obj)
        await self.session.flush()
        return True

    async def count(self, filters: Optional[Dict[str, Any]] = None) -> int:
        """Count records."""
        query = select(func.count()).select_from(self.model)
        if filters:
            for key, value in filters.items():
                if hasattr(self.model, key):
                    query = query.where(getattr(self.model, key) == value)
        result = await self.session.execute(query)
        return result.scalar_one()

    async def exists(self, **kwargs) -> bool:
        """Check if a record exists with given filters."""
        query = select(self.model)
        for key, value in kwargs.items():
            if hasattr(self.model, key):
                query = query.where(getattr(self.model, key) == value)
        query = query.limit(1)
        result = await self.session.execute(query)
        return result.scalar_one_or_none() is not None
