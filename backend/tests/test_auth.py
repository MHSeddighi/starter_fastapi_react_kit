"""Authentication endpoint tests."""

from __future__ import annotations

import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_register_user(client: AsyncClient) -> None:
    """Test user registration."""
    response = await client.post(
        "/api/v1/auth/register",
        json={
            "email": "test@example.com",
            "username": "testuser",
            "password": "testpassword123",
            "full_name": "Test User",
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert data["data"]["email"] == "test@example.com"
    assert data["data"]["username"] == "testuser"


@pytest.mark.asyncio
async def test_register_duplicate_email(client: AsyncClient) -> None:
    """Test registration with duplicate email returns error."""
    # Register first user
    await client.post(
        "/api/v1/auth/register",
        json={
            "email": "duplicate@example.com",
            "username": "user1",
            "password": "testpassword123",
        },
    )

    # Try duplicate email
    response = await client.post(
        "/api/v1/auth/register",
        json={
            "email": "duplicate@example.com",
            "username": "user2",
            "password": "testpassword123",
        },
    )
    assert response.status_code == 409


@pytest.mark.asyncio
async def test_login_success(client: AsyncClient) -> None:
    """Test successful login returns token."""
    # Register user first
    await client.post(
        "/api/v1/auth/register",
        json={
            "email": "login@example.com",
            "username": "loginuser",
            "password": "testpassword123",
        },
    )

    # Login
    response = await client.post(
        "/api/v1/auth/login",
        json={
            "username": "loginuser",
            "password": "testpassword123",
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert "access_token" in data["data"]


@pytest.mark.asyncio
async def test_login_invalid_credentials(client: AsyncClient) -> None:
    """Test login with wrong password returns error."""
    response = await client.post(
        "/api/v1/auth/login",
        json={
            "username": "nonexistent",
            "password": "wrongpassword",
        },
    )
    assert response.status_code == 401


@pytest.mark.asyncio
async def test_get_me_authenticated(client: AsyncClient) -> None:
    """Test getting current user with valid token."""
    # Register and login
    await client.post(
        "/api/v1/auth/register",
        json={
            "email": "me@example.com",
            "username": "meuser",
            "password": "testpassword123",
        },
    )

    login_resp = await client.post(
        "/api/v1/auth/login",
        json={"username": "meuser", "password": "testpassword123"},
    )
    token = login_resp.json()["data"]["access_token"]

    # Get current user
    response = await client.get(
        "/api/v1/auth/me",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["data"]["username"] == "meuser"
    assert data["data"]["email"] == "me@example.com"


@pytest.mark.asyncio
async def test_get_me_unauthenticated(client: AsyncClient) -> None:
    """Test getting current user without token returns error."""
    response = await client.get("/api/v1/auth/me")
    assert response.status_code == 401
