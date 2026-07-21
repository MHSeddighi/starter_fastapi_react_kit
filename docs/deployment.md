# Deployment Guide

## Deployment Options

### Option 1: Docker (Recommended)

```bash
# Build and start all services
make docker-up

# The app will be available at:
# Frontend: http://localhost:5173
# Backend: http://localhost:8000
# API Docs: http://localhost:8000/docs
```

### Option 2: Manual Deployment

#### Prerequisites

- Node.js 20+
- Python 3.11+
- PostgreSQL 16+
- Redis 7+

#### Backend

```bash
cd backend
uv sync
uv run alembic upgrade head
uv run fastapi run app/main.py --port 8000 --host 0.0.0.0
```

#### Frontend

```bash
cd frontend
npm install
npm run build
# Serve dist/ with any static file server
npx serve dist -l 5173
```

### Option 3: Platform Deployment

#### Render

1. Create a PostgreSQL database
2. Create a Redis instance
3. Web Service (Backend):
   - Build Command: `cd backend && pip install uv && uv sync`
   - Start Command: `cd backend && uv run alembic upgrade head && uv run fastapi run app/main.py --port 8000`
4. Static Site (Frontend):
   - Build Command: `cd frontend && npm install && npm run build`
   - Publish Directory: `frontend/dist`

#### Railway

1. Connect GitHub repository
2. Add PostgreSQL plugin
3. Add Redis plugin
4. Configure environment variables
5. Deploy

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| APP_SECRET_KEY | FastAPI secret key | Required |
| JWT_SECRET_KEY | JWT signing key | Required |
| DATABASE_URL | Async PostgreSQL URL | postgresql+asyncpg://... |
| REDIS_URL | Redis connection URL | redis://localhost:6379/0 |
| APP_CORS_ORIGINS | Allowed CORS origins | ["http://localhost:5173"] |
| VITE_API_URL | Backend URL for frontend | http://localhost:8000/api/v1 |

## Production Checklist

- [ ] Set strong `APP_SECRET_KEY` and `JWT_SECRET_KEY`
- [ ] Set `APP_DEBUG=false`
- [ ] Configure `APP_CORS_ORIGINS` to your frontend domain
- [ ] Use managed PostgreSQL (Render, Railway, Neon, etc.)
- [ ] Use managed Redis (Upstash, Redis Cloud, etc.)
- [ ] Set up custom domain
- [ ] Enable HTTPS
- [ ] Configure database connection pooling
