#!/bin/bash
# ─────────────────────────────────────────────────
# Hackathon Starter Kit - Setup Script
# ─────────────────────────────────────────────────
# This script handles the complete initial setup.

set -e

echo "🚀 Hackathon Starter Kit - Setup"
echo "================================"

# Check prerequisites
echo ""
echo "📋 Checking prerequisites..."

check_command() {
    if command -v "$1" &> /dev/null; then
        echo "  ✅ $1 found"
    else
        echo "  ❌ $1 not found"
        echo "  Please install $1 and try again."
        exit 1
    fi
}

check_command node
check_command python3
check_command uv || check_command pip

# Check for Docker (optional)
if command -v docker &> /dev/null; then
    echo "  ✅ Docker found (optional)"
else
    echo "  ⚠️  Docker not found (optional - needed for docker-compose)"
fi

echo ""
echo "📦 Installing dependencies..."

# Install backend dependencies
echo "  • Backend..."
cd backend
uv sync
cd ..

# Install frontend dependencies
echo "  • Frontend..."
cd frontend
npm install
cd ..

# Setup environment file
if [ ! -f .env ]; then
    echo ""
    echo "🔧 Creating .env file from .env.example..."
    cp .env.example .env
    echo "  ⚠️  Please edit .env with your settings!"
else
    echo ""
    echo "✅ .env file already exists"
fi

# Success message
echo ""
echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "  1. Edit .env with your database settings"
echo "  2. Start PostgreSQL and Redis"
echo "  3. Run: make migrate"
echo "  4. Run: make dev"
echo ""
echo "Happy hacking! 🎉"
