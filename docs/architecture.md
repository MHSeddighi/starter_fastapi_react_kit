# Architecture

## Overview

The Hackathon Starter Kit follows a simple, modern web application architecture optimized for rapid development.

## High-Level Architecture

```
┌─────────────────────────────────────────────────────┐
│                   Frontend (React)                    │
│  ┌─────────┐ ┌──────────┐ ┌────────┐ ┌──────────┐  │
│  │  Pages   │ │ Features │ │  Hooks  │ │  Services │  │
│  └────┬────┘ └────┬─────┘ └───┬────┘ └────┬─────┘  │
│       │           │            │           │         │
│  ┌────┴───────────┴────────────┴───────────┴─────┐  │
│  │              Axios Client (lib/axios.ts)       │  │
│  └───────────────────┬───────────────────────────┘  │
└──────────────────────┼──────────────────────────────┘
                       │ HTTP/JSON + JWT
┌──────────────────────┼──────────────────────────────┐
│                 Backend (FastAPI)                     │
│  ┌───────────────────┴───────────────────────────┐  │
│  │           API Endpoints (api/v1/)              │  │
│  └───────────────────┬───────────────────────────┘  │
│  ┌───────────────────┴───────────────────────────┐  │
│  │              Services (business logic)         │  │
│  └───────────────────┬───────────────────────────┘  │
│  ┌───────────────────┴───────────────────────────┐  │
│  │           Repositories (data access)           │  │
│  └───────────────────┬───────────────────────────┘  │
│  ┌───────────────────┴───────────────────────────┐  │
│  │     SQLAlchemy Models + PostgreSQL             │  │
│  └───────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────┘
```

## Request Lifecycle

1. User interacts with React UI
2. Component calls a custom hook (e.g., `useUsers()`)
3. Hook uses TanStack Query to manage server state
4. Query calls an API service function (e.g., `usersApi.getAll()`)
5. Service function uses Axios client to make HTTP request
6. Axios client adds JWT token via interceptor
7. FastAPI endpoint receives request
8. Endpoint validates input via Pydantic schema
9. Endpoint calls Service layer for business logic
10. Service calls Repository layer for database operations
11. Repository executes SQLAlchemy query
12. Response flows back through the same chain

## Key Decisions

### Why not Next.js?
Next.js adds server-side rendering complexity. For hackathons, a simple SPA is faster to build and deploy.

### Why not Redux?
TanStack Query handles server state. Local state with useState/useReducer handles the rest. Redux adds boilerplate without proportional value.

### Why feature-based frontend?
Keeps related code together. Easy to add, modify, or remove features without touching unrelated code.

### Why repository pattern?
Thin data access layer that keeps SQLAlchemy queries out of services. Easy to test and swap databases.

### Why not microservices?
A single FastAPI app is simpler, faster to develop, and sufficient for any hackathon project.

## Data Flow

### Frontend → Backend

```
Component → Hook → Query/Mutation → API Service → Axios → FastAPI → Service → Repository → DB
```

### Backend → Frontend

```
DB → Repository → Service → Schema → FastAPI → JSON → Axios → Hook → Component
```
