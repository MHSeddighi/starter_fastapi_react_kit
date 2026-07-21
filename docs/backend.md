# Backend Guide

## Tech Stack

- **Python 3.11+** — Runtime
- **FastAPI** — Web framework
- **SQLAlchemy 2.0** — ORM
- **Alembic** — Migrations
- **PostgreSQL** — Database
- **Redis** — Caching/sessions
- **uv** — Package manager
- **Pydantic v2** — Validation
- **JWT (python-jose)** — Auth tokens
- **Pytest** — Testing
- **Loguru** — Logging
- **Ruff** — Linting/formatter

## Project Structure

```
backend/
├── app/
│   ├── api/
│   │   └── v1/           # API endpoints
│   │       ├── __init__.py
│   │       ├── auth.py    # Auth routes
│   │       ├── uploads.py # File upload routes
│   │       └── router.py  # Main router
│   ├── core/
│   │   ├── config.py      # Settings (Pydantic Settings)
│   │   ├── database.py    # SQLAlchemy engine/session
│   │   ├── redis.py       # Redis client wrapper
│   │   └── security.py    # JWT, password hashing
│   ├── middleware/
│   │   └── cors.py        # CORS setup
│   ├── models/            # SQLAlchemy models
│   │   ├── __init__.py
│   │   └── user.py
│   ├── repositories/      # Data access
│   │   ├── base.py        # Base CRUD repository
│   │   └── user.py
│   ├── schemas/           # Pydantic schemas
│   │   ├── common.py      # Response wrappers
│   │   └── user.py
│   ├── services/          # Business logic
│   │   ├── auth.py
│   │   └── file_upload.py
│   ├── utils/             # Helpers
│   ├── workers/           # Background tasks
│   ├── ai/                # AI integration
│   └── main.py            # App entry point
├── alembic/               # Migrations
├── scripts/               # Utility scripts
├── tests/                 # Tests
└── pyproject.toml         # Dependencies
```

## Commands

```bash
uv sync              # Install dependencies
uv run fastapi dev    # Start dev server (hot reload)
uv run pytest        # Run tests
uv run ruff check .  # Lint
uv run ruff format . # Format
```

## Adding a New API Endpoint

### 1. Model
Create in `app/models/`:
```python
from sqlalchemy import String
from app.core.database import Base

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
```

### 2. Migration
```bash
uv run alembic revision --autogenerate -m "add items table"
uv run alembic upgrade head
```

### 3. Schema
Create in `app/schemas/`:
```python
from pydantic import BaseModel
class ItemCreate(BaseModel):
    name: str
class ItemResponse(BaseModel):
    id: int
    name: str
    model_config = {"from_attributes": True}
```

### 4. Repository
Create in `app/repositories/`:
```python
from app.repositories.base import BaseRepository
class ItemRepository(BaseRepository[Item]):
    def __init__(self, session):
        super().__init__(Item, session)
```

### 5. Service
Create in `app/services/`:
```python
class ItemService:
    def __init__(self, session):
        self.repo = ItemRepository(session)
    async def create(self, data):
        return await self.repo.create(**data.model_dump())
```

### 6. Endpoint
Create in `app/api/v1/`:
```python
router = APIRouter(prefix="/items", tags=["Items"])
@router.post("")
async def create_item(data: ItemCreate, db=Depends(get_db)):
    service = ItemService(db)
    item = await service.create(data)
    return APIResponse(data=item)
```

## Database Configuration

Default connection strings in `.env`:
```
DATABASE_URL=postgresql+asyncpg://postgres:postgres@localhost:5432/hackathon
DATABASE_SYNC_URL=postgresql://postgres:postgres@localhost:5432/hackathon
```

## Redis Usage

```python
from app.core.redis import cache_get, cache_set, cache_delete, cache_get_or_set

# Get or compute with 5 min TTL
data = await cache_get_or_set("my_key", fetch_function, ttl=300)
```
