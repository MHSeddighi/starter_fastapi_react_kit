# ─────────────────────────────────────────────────
# Hackathon Starter Kit - Makefile
# Usage: make <command>
# ─────────────────────────────────────────────────

.PHONY: help install dev build test lint format migrate makemigrations seed clean docker-up docker-down logs

# ─── Help ──────────────────────────────────────────
help: ## Show this help message
	@echo "Hackathon Starter Kit - Makefile"
	@echo ""
	@echo "Usage: make <command>"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

# ─── Installation ──────────────────────────────────
install: ## Install all dependencies (frontend + backend)
	@echo "📦 Installing backend dependencies..."
	cd backend && uv sync
	@echo "📦 Installing frontend dependencies..."
	cd frontend && npm install
	@echo "✅ All dependencies installed"

install-frontend: ## Install frontend dependencies only
	@echo "📦 Installing frontend dependencies..."
	cd frontend && npm install
	@echo "✅ Frontend dependencies installed"

install-backend: ## Install backend dependencies only
	@echo "📦 Installing backend dependencies..."
	cd backend && uv sync
	@echo "✅ Backend dependencies installed"

# ─── Development ───────────────────────────────────
dev: ## Start development servers (frontend + backend)
	@echo "🚀 Starting backend..."
	cd backend && uv run fastapi dev app/main.py --port 8000 &
	@sleep 2
	@echo "🚀 Starting frontend..."
	cd frontend && npm run dev

dev-backend: ## Start backend development server only
	@echo "🚀 Starting backend..."
	cd backend && uv run fastapi dev app/main.py --port 8000

dev-frontend: ## Start frontend development server only
	@echo "🚀 Starting frontend..."
	cd frontend && npm run dev

# ─── Build ─────────────────────────────────────────
build: ## Build frontend for production
	@echo "🔨 Building frontend..."
	cd frontend && npm run build
	@echo "✅ Frontend built"

# ─── Testing ───────────────────────────────────────
test: ## Run all tests
	@echo "🧪 Running backend tests..."
	cd backend && uv run pytest
	@echo "🧪 Running frontend tests..."
	cd frontend && npm run test 2>/dev/null || echo "No frontend tests configured"
	@echo "✅ Tests completed"

test-backend: ## Run backend tests only
	@echo "🧪 Running backend tests..."
	cd backend && uv run pytest

test-frontend: ## Run frontend tests only
	@echo "🧪 Running frontend tests..."
	cd frontend && npm run test 2>/dev/null || echo "No frontend tests configured"

# ─── Linting & Formatting ─────────────────────────
lint: ## Lint all code
	@echo "🔍 Linting backend..."
	cd backend && uv run ruff check .
	@echo "🔍 Linting frontend..."
	cd frontend && npm run lint
	@echo "✅ Linting completed"

format: ## Format all code
	@echo "✨ Formatting backend..."
	cd backend && uv run ruff format .
	@echo "✨ Formatting frontend..."
	cd frontend && npm run format 2>/dev/null || npx prettier --write "src/**/*.{ts,tsx,css}"
	@echo "✅ Formatting completed"

# ─── Database ─────────────────────────────────────
migrate: ## Run database migrations
	@echo "🗄️  Running migrations..."
	cd backend && uv run alembic upgrade head
	@echo "✅ Migrations completed"

makemigrations: ## Create new database migration
	@echo "🗄️  Creating new migration..."
	cd backend && uv run alembic revision --autogenerate -m "$(message)"
	@echo "✅ Migration created"

seed: ## Seed database with sample data
	@echo "🌱 Seeding database..."
	cd backend && uv run python -m scripts.seed
	@echo "✅ Database seeded"

# ─── Cleanup ──────────────────────────────────────
clean: ## Clean temporary files and build artifacts
	@echo "🧹 Cleaning..."
	rm -rf frontend/dist
	rm -rf backend/.ruff_cache
	rm -rf backend/**/__pycache__
	rm -rf .pytest_cache
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@echo "✅ Cleaned"

# ─── Docker ────────────────────────────────────────
docker-up: ## Start all Docker containers
	@echo "🐳 Starting Docker containers..."
	docker compose up -d
	@echo "✅ Docker containers started"
	@echo "📝 Backend: http://localhost:8000"
	@echo "📝 Frontend: http://localhost:5173"
	@echo "📝 API Docs: http://localhost:8000/docs"

docker-down: ## Stop all Docker containers
	@echo "🐳 Stopping Docker containers..."
	docker compose down
	@echo "✅ Docker containers stopped"

docker-build: ## Build Docker images
	@echo "🐳 Building Docker images..."
	docker compose build
	@echo "✅ Docker images built"

docker-logs: ## View Docker container logs
	docker compose logs -f

docker-reset: ## Reset Docker containers (down + up)
	@echo "🔄 Resetting Docker containers..."
	docker compose down -v
	docker compose up -d
	@echo "✅ Docker containers reset"

# ─── Utilities ────────────────────────────────────
logs: ## View backend logs
	tail -f backend/logs/app.log 2>/dev/null || echo "No logs found"

shell-backend: ## Open a shell in the backend container
	docker compose exec backend bash

shell-db: ## Open a PostgreSQL shell
	docker compose exec postgres psql -U postgres -d hackathon

shell-redis: ## Open a Redis CLI
	docker compose exec redis redis-cli
