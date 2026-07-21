# 🚀 Hackathon Starter Kit - Developer Guide

> **The first document every developer should read.**

## 1. Project Overview

### Purpose

This is a **Hackathon Starter Kit** designed for 4-person teams competing in 24–48 hour buildathons. It provides a production-ready foundation so your team can focus on building the actual product instead of configuring infrastructure.

### Philosophy

- **Speed over abstraction** — Simple, flat structures. No unnecessary layers.
- **Easy onboarding** — Clone, install, run. That's it.
- **Reusable** — Same structure for every hackathon. Copy and build.
- **Production basics** — Not enterprise, but not a toy. Ready for demo day.

### Technologies

| Layer | Technology | Purpose |
|-------|-----------|---------|
| Frontend | React + Vite + TypeScript | Fast dev server, type safety |
| Styling | Tailwind CSS + shadcn/ui | Utility-first, pre-built components |
| Routing | React Router | Client-side navigation |
| State | TanStack Query | Server state management |
| Forms | React Hook Form + Zod | Type-safe form validation |
| HTTP | Axios | API communication |
| Backend | FastAPI | Python async web framework |
| Database | PostgreSQL + SQLAlchemy 2.0 | Relational data |
| Migrations | Alembic | Schema versioning |
| Cache | Redis | Caching, sessions |
| Auth | JWT | Simple token auth |
| Dev Tools | uv, Docker, Makefile | Fast setup |

### Architecture

```
┌─────────────┐     HTTP/JSON      ┌─────────────┐
│  Frontend   │ ──────────────────→ │   Backend   │
│  React/Vite │ ←────────────────── │   FastAPI   │
│  :5173      │     JWT tokens      │   :8000     │
└─────────────┘                     └──────┬──────┘
                                           │
                                    ┌──────┴──────┐
                                    │  PostgreSQL  │
                                    │  + Redis     │
                                    └─────────────┘
```

## 2. Repository Structure

```
hackathon-starter/
├── frontend/               # React + Vite application
│   ├── src/
│   │   ├── app/           # App entry point
│   │   ├── assets/        # Static assets (images, fonts)
│   │   ├── components/    # Shared UI components (shadcn/ui + custom)
│   │   │   └── ui/        # shadcn/ui generated components
│   │   ├── features/      # Business features (feature-based)
│   │   │   └── example/
│   │   │       ├── components/  # Feature-specific components
│   │   │       ├── hooks/      # Feature-specific hooks
│   │   │       ├── services/   # API service functions
│   │   │       ├── types.ts    # Feature TypeScript types
│   │   │       └── index.ts    # Public exports
│   │   ├── hooks/         # Shared custom hooks
│   │   ├── layouts/       # Page layouts (AppLayout, AuthLayout)
│   │   ├── lib/           # Utilities (axios client, helpers)
│   │   ├── pages/         # Page components (route targets)
│   │   ├── providers/     # React context providers
│   │   ├── routes/        # Route configuration
│   │   ├── styles/        # Global styles
│   │   ├── types/         # Shared TypeScript types
│   │   └── utils/         # Helper functions
│   ├── public/            # Static files
│   └── package.json
│
├── backend/                # FastAPI application
│   ├── app/
│   │   ├── api/           # API routes (endpoints)
│   │   │   └── v1/        # API version 1
│   │   ├── core/          # Config, database, security, redis
│   │   ├── db/            # Database setup
│   │   ├── middleware/    # CORS and other middleware
│   │   ├── models/        # SQLAlchemy models
│   │   ├── repositories/  # Data access layer
│   │   ├── schemas/       # Pydantic request/response schemas
│   │   ├── services/      # Business logic layer
│   │   ├── utils/         # Utility functions
│   │   ├── workers/       # Background task workers
│   │   ├── ai/            # AI/ML integration
│   │   └── main.py        # FastAPI application entry
│   ├── alembic/           # Database migrations
│   ├── scripts/           # Utility scripts (seed, etc.)
│   ├── tests/             # Test suite
│   └── pyproject.toml     # Python dependencies
│
├── docker/                 # Dockerfiles
│   ├── Dockerfile.frontend
│   └── Dockerfile.backend
│
├── database/               # Database init scripts
│   └── init.sql
│
├── docs/                   # Documentation
│   ├── DEVELOPER_GUIDE.md  # ← You are here
│   ├── architecture.md     # Architecture deep dive
│   ├── frontend.md         # Frontend specifics
│   ├── backend.md          # Backend specifics
│   ├── api.md              # API documentation
│   ├── deployment.md       # Deployment guide
│   └── competition-checklist.md  # Hackathon checklist
│
├── scripts/                # Shell scripts
├── .github/workflows/      # CI/CD pipelines
├── .env.example            # Environment variables template
├── .gitignore
├── Makefile                # Common commands
├── docker-compose.yml      # Docker services
└── README.md               # Project overview
```

### What goes where

- **`frontend/src/features/`** — Business features. One folder per feature (auth, users, payments, etc.)
- **`frontend/src/components/`** — ONLY shared components used across features. shadcn/ui components go in `components/ui/`
- **`frontend/src/pages/`** — Page-level components that compose features into routes
- **`backend/app/api/v1/`** — API endpoints. One file per domain area (auth.py, users.py, etc.)
- **`backend/app/services/`** — Business logic. Services call repositories.
- **`backend/app/repositories/`** — Database queries. One repository per model.

## 3. Frontend Development

### Folder Structure

When adding something new:

- **New page?** → Add to `pages/`, create route in `routes/`
- **New feature?** → Create folder in `features/` with components, hooks, services, types
- **Shared component?** → Add to `components/`
- **New shadcn/ui component?** → Run `npx shadcn add <component-name>`

### Adding a New Page

1. Create the page component in `src/pages/`:
```tsx
// src/pages/MyNewPage.tsx
export function MyNewPage() {
  return <div>{/* Your page content */}</div>
}
```

2. Add the route in `src/routes/index.tsx`:
```tsx
import { MyNewPage } from '@/pages/MyNewPage'

// Inside the router config:
{ path: 'my-new-page', element: <MyNewPage /> }
```

3. Add navigation link in the sidebar layout.

### Adding a New Feature

1. Create feature folder: `src/features/my-feature/`
2. Create types: `types.ts`
3. Create API service: `services/my-feature.api.ts`
4. Create hooks: `hooks/useMyFeature.ts`
5. Create components: `components/MyFeatureCard.tsx`
6. Export from `index.ts`

### Using shadcn/ui

```bash
# Add a new component
npx shadcn add button

# Available components: button, input, form, card, dialog,
# table, dropdown-menu, tabs, sonner, skeleton, avatar, badge
```

### API Communication

All API calls go through the Axios client at `src/lib/axios.ts`.

```tsx
import apiClient from '@/lib/axios'

// GET
const { data } = await apiClient.get('/users')

// POST
const { data } = await apiClient.post('/auth/login', { username, password })

// With auth token (automatic via interceptor)
const { data } = await apiClient.get('/auth/me')
```

### Forms & Validation

```tsx
import { useForm } from 'react-hook-form'
import { zodResolver } from '@hookform/resolvers/zod'
import { z } from 'zod'

const schema = z.object({
  email: z.string().email(),
  name: z.string().min(2),
})

type FormData = z.infer<typeof schema>

function MyForm() {
  const form = useForm<FormData>({ resolver: zodResolver(schema) })
  // ...
}
```

### State Management

- **Server state** → TanStack Query (useQuery, useMutation)
- **URL state** → React Router (useParams, useSearchParams)
- **Local UI state** → useState, useReducer
- **No Redux, no global stores**

```tsx
import { useQuery, useMutation } from '@tanstack/react-query'

function useUsers() {
  return useQuery({
    queryKey: ['users'],
    queryFn: () => apiClient.get('/users').then(r => r.data),
  })
}
```

## 4. Backend Development

### API Creation Flow

```
1. Model → 2. Migration → 3. Schema → 4. Repository → 5. Service → 6. Endpoint
```

### Step-by-Step: Adding a New API

#### 1. Create Model

```python
# app/models/note.py
from sqlalchemy import String, Text
from app.core.database import Base

class Note(Base):
    __tablename__ = "notes"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200))
    content: Mapped[str] = mapped_column(Text)
```

Import in `app/models/__init__.py`

#### 2. Create Migration

```bash
make makemigrations message="add notes table"
```

#### 3. Create Schema

```python
# app/schemas/note.py
from pydantic import BaseModel

class NoteCreate(BaseModel):
    title: str
    content: str

class NoteResponse(BaseModel):
    id: int
    title: str
    content: str
    model_config = {"from_attributes": True}
```

#### 4. Create Repository

```python
# app/repositories/note.py
from app.repositories.base import BaseRepository
from app.models.note import Note

class NoteRepository(BaseRepository[Note]):
    def __init__(self, session):
        super().__init__(Note, session)
```

#### 5. Create Service

```python
# app/services/note.py
from app.repositories.note import NoteRepository

class NoteService:
    def __init__(self, session):
        self.repo = NoteRepository(session)
    
    async def create(self, data, user_id):
        return await self.repo.create(**data.model_dump(), user_id=user_id)
```

#### 6. Create Endpoint

```python
# app/api/v1/notes.py
from fastapi import APIRouter, Depends
from app.services.note import NoteService

router = APIRouter(prefix="/notes", tags=["Notes"])

@router.post("")
async def create_note(data: NoteCreate, service = Depends(get_note_service)):
    result = await service.create(data, user_id)
    return APIResponse(data=result)
```

Register the router in `app/api/v1/router.py`:
```python
from app.api.v1.notes import router as notes_router
router.include_router(notes_router)
```

### Database Migrations

```bash
# Create new migration
make makemigrations message="description of changes"

# Apply migrations
make migrate

# Rollback (one step)
cd backend && uv run alembic downgrade -1
```

## 5. API Conventions

### Standard Response Format

**Success:**
```json
{
  "success": true,
  "message": "OK",
  "data": {}
}
```

**Error:**
```json
{
  "success": false,
  "message": "Human-readable error message",
  "details": {}  // Optional error details
}
```

**Paginated:**
```json
{
  "success": true,
  "data": [],
  "total": 100,
  "page": 1,
  "page_size": 20,
  "total_pages": 5
}
```

### HTTP Status Codes

| Code | When |
|------|------|
| 200 | Success |
| 201 | Created |
| 400 | Bad request (validation error) |
| 401 | Unauthorized (no/invalid token) |
| 403 | Forbidden (no permission) |
| 404 | Not found |
| 409 | Conflict (duplicate) |
| 422 | Validation error |
| 500 | Server error |

### Authentication

Add `Authorization: Bearer <token>` header to protected requests.

## 6. Development Workflow

### Branches

```
main        - Production-ready code
feat/*      - New features (feat/auth, feat/payments)
fix/*       - Bug fixes
docs/*      - Documentation
chore/*     - Maintenance
```

### Commits

Use conventional commits:
```
feat: add user registration
fix: correct email validation
docs: update API documentation
chore: update dependencies
```

### Testing

```bash
make test          # Run all tests
make test-backend  # Backend tests only
```

### Code Quality

```bash
make lint          # Lint all code
make format        # Auto-format all code
```

## 7. Hackathon Workflow

### Day 1: Foundation (Hours 1-12)

| Time | Task |
|------|------|
| Hour 1 | Clone repo, setup environment, verify everything runs |
| Hour 2 | Define data model, create migrations |
| Hour 3-4 | Build core backend APIs |
| Hour 5-6 | Build core frontend pages |
| Hour 7-8 | Connect frontend to backend |
| Hour 9-12 | Build MVP features |

### Day 2: Polish (Hours 13-24)

| Time | Task |
|------|------|
| Hour 13-15 | Complete remaining features |
| Hour 16-18 | Testing & bug fixes |
| Hour 19-20 | UI polish, loading states, error handling |
| Hour 21-22 | Deployment |
| Hour 23-24 | Presentation prep, demo script |

### MVP Mindset

- **Build the simplest thing that works**
- **One meaningful feature beats three half-baked ones**
- **Deploy early, deploy often**
- **Polish the demo flow, not edge cases**
- **Present what works, not what you planned**

## Quick Start

```bash
# 1. Clone
git clone <repo-url>
cd hackathon-starter

# 2. Install dependencies
make install

# 3. Set up environment
cp .env.example .env
# Edit .env with your settings

# 4. Start databases (PostgreSQL + Redis)
# Option A: Local
# Start PostgreSQL and Redis on your machine

# Option B: Docker
make docker-up

# 5. Run migrations
make migrate

# 6. Seed data (optional)
make seed

# 7. Start development
make dev
```

> **Frontend**: http://localhost:5173
> **Backend**: http://localhost:8000
> **API Docs**: http://localhost:8000/docs
