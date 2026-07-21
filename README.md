# 🚀 Hackathon Starter Kit

> **Build real products in 24-48 hours. No boilerplate. No distractions.**

A production-ready starter kit for hackathons and buildathons. Optimized for **maximum development speed** with **minimum configuration**. Clone it, install it, and start building your product immediately.

## ✨ Features

- **🔐 Authentication** — JWT-based login/register out of the box
- **📁 File Upload** — Drag & drop, multiple files, progress display
- **🎨 Beautiful UI** — shadcn/ui components with light/dark/system themes
- **📝 Forms** — Type-safe forms with React Hook Form + Zod
- **📊 API Ready** — Axios client, TanStack Query, standard response format
- **🗄️ Database** — PostgreSQL with SQLAlchemy 2.0 + Alembic migrations
- **⚡ Redis** — Caching wrapper, ready for sessions and background jobs
- **🐳 Docker** — Full environment with one command
- **📚 Documentation** — Complete developer guide, API docs, competition checklist

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| **Frontend** | React 19, Vite 8, TypeScript 6, Tailwind CSS 4, shadcn/ui |
| **Backend** | FastAPI, SQLAlchemy 2.0, Alembic, Pydantic v2 |
| **Database** | PostgreSQL 16 |
| **Cache** | Redis 7 |
| **Auth** | JWT (python-jose, bcrypt) |
| **Dev Tools** | uv, Docker, Makefile |

## 🚦 Quick Start

### Prerequisites

- Node.js 20+
- Python 3.11+
- PostgreSQL 16+ (or Docker)
- Redis 7+ (or Docker)

### Installation

```bash
# 1. Clone the repository
git clone <repo-url>
cd hackathon-starter

# 2. Install all dependencies
make install

# 3. Set up environment variables
cp .env.example .env
# Edit .env with your settings

# 4. Start database services
# Option A: Using Docker
make docker-up

# Option B: Local PostgreSQL + Redis
# Start them manually on your machine

# 5. Run database migrations
make migrate

# 6. Seed sample data (optional)
make seed

# 7. Start development servers
make dev
```

The app is now running at:
- **Frontend**: http://localhost:5173
- **Backend**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs

## 📁 Folder Structure

```
hackathon-starter/
├── frontend/          # React + Vite SPA
│   ├── src/
│   │   ├── components/  # Shared UI components (shadcn/ui)
│   │   ├── features/    # Business features (auth, users, etc.)
│   │   ├── pages/       # Route pages
│   │   ├── layouts/     # App and auth layouts
│   │   ├── providers/   # React context providers
│   │   └── lib/         # Utilities (Axios client, helpers)
│   └── package.json
├── backend/           # FastAPI application
│   ├── app/
│   │   ├── api/v1/     # API endpoints
│   │   ├── core/       # Config, database, security
│   │   ├── models/     # SQLAlchemy models
│   │   ├── services/   # Business logic
│   │   ├── repositories/  # Data access
│   │   └── schemas/    # Pydantic schemas
│   ├── alembic/       # Database migrations
│   └── pyproject.toml
├── docker/            # Dockerfiles
├── docs/              # Documentation
├── .github/workflows/ # CI/CD
├── Makefile           # Common commands
└── docker-compose.yml
```

## 📋 Available Commands

| Command | Description |
|---------|-------------|
| `make install` | Install all dependencies |
| `make dev` | Start frontend + backend dev servers |
| `make dev-frontend` | Start frontend only |
| `make dev-backend` | Start backend only |
| `make build` | Build frontend for production |
| `make test` | Run all tests |
| `make lint` | Lint all code |
| `make format` | Format all code |
| `make migrate` | Apply database migrations |
| `make makemigrations` | Create a new migration |
| `make seed` | Seed database with sample data |
| `make clean` | Clean temporary files |
| `make docker-up` | Start all Docker services |
| `make docker-down` | Stop all Docker services |
| `make docker-logs` | View Docker logs |

## 📚 Documentation

| Document | Description |
|----------|-------------|
| [Developer Guide](docs/DEVELOPER_GUIDE.md) | First document to read |
| [Architecture](docs/architecture.md) | System architecture |
| [Frontend Guide](docs/frontend.md) | Frontend development |
| [Backend Guide](docs/backend.md) | Backend development |
| [API Reference](docs/api.md) | API endpoints |
| [Deployment Guide](docs/deployment.md) | Deployment instructions |
| [Competition Checklist](docs/competition-checklist.md) | Hackathon workflow |

## 🏗️ Adding a New Feature

**Frontend:**

1. Create `features/your-feature/` folder
2. Add `types.ts`, `services/`, `hooks/`, `components/`
3. Create page in `pages/`
4. Add route in `routes/`

**Backend:**

1. Create model in `models/`
2. Run `make makemigrations` + `make migrate`
3. Create schema in `schemas/`
4. Create repository in `repositories/`
5. Create service in `services/`
6. Create endpoint in `api/v1/`

## 🤝 Team Workflow

### Day 1: Foundation (12 hours)
- **Hour 1**: Setup, verify everything works
- **Hour 2-3**: Define data model, create migrations
- **Hour 4-8**: Build core APIs and pages
- **Hour 9-12**: Connect frontend to backend, build MVP

### Day 2: Polish (12 hours)
- **Hour 13-16**: Complete remaining features
- **Hour 17-19**: Testing, bug fixes, UI polish
- **Hour 20-22**: Deployment
- **Hour 23-24**: Presentation prep

> See [Competition Checklist](docs/competition-checklist.md) for detailed timeline.

## 🔒 Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `APP_SECRET_KEY` | `change-me` | FastAPI secret key |
| `JWT_SECRET_KEY` | `change-me` | JWT signing key |
| `DATABASE_URL` | `postgresql+asyncpg://...` | Async database URL |
| `REDIS_URL` | `redis://localhost:6379/0` | Redis connection |
| `VITE_API_URL` | `http://localhost:8000/api/v1` | Backend URL |

## 📄 License

MIT — use it for any hackathon, project, or product.
