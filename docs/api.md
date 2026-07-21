# API Documentation

## Base URL

Development: `http://localhost:8000/api/v1`
Production: Configured via `VITE_API_URL`

## Authentication

Most endpoints require JWT authentication.

**Header:** `Authorization: Bearer <token>`

## Endpoints

### Health

```
GET /api/v1/health
```

Response:
```json
{
  "status": "healthy",
  "service": "Hackathon Starter Kit API",
  "version": "0.1.0"
}
```

### Authentication

#### Register

```
POST /api/v1/auth/register
```

Request:
```json
{
  "email": "user@example.com",
  "username": "johndoe",
  "password": "securepassword123",
  "full_name": "John Doe"
}
```

Response:
```json
{
  "success": true,
  "message": "User registered successfully",
  "data": {
    "id": 1,
    "email": "user@example.com",
    "username": "johndoe",
    "full_name": "John Doe",
    "is_active": true,
    "is_superuser": false,
    "created_at": "2024-01-01T00:00:00Z"
  }
}
```

#### Login

```
POST /api/v1/auth/login
```

Request:
```json
{
  "username": "johndoe",
  "password": "securepassword123"
}
```

Response:
```json
{
  "success": true,
  "message": "Login successful",
  "data": {
    "access_token": "eyJhbGciOiJIUzI1NiIs...",
    "token_type": "bearer"
  }
}
```

#### Get Current User

```
GET /api/v1/auth/me
```

Headers: `Authorization: Bearer <token>`

Response:
```json
{
  "success": true,
  "data": {
    "id": 1,
    "email": "user@example.com",
    "username": "johndoe",
    "full_name": "John Doe",
    "is_active": true,
    "is_superuser": false,
    "created_at": "2024-01-01T00:00:00Z"
  }
}
```

### File Upload

#### Upload Single File

```
POST /api/v1/upload
```

Headers: `Authorization: Bearer <token>`
Body: `multipart/form-data`

| Field | Type | Description |
|-------|------|-------------|
| file | File | The file to upload |
| subdir | string (optional) | Subdirectory within uploads |

Response:
```json
{
  "success": true,
  "message": "File uploaded successfully",
  "data": {
    "filename": "image.jpg",
    "path": "uploads/abc123.jpg"
  }
}
```

#### Upload Multiple Files

```
POST /api/v1/upload/multiple
```

Headers: `Authorization: Bearer <token>`
Body: `multipart/form-data` (multiple files)

Response:
```json
{
  "success": true,
  "message": "3 files uploaded successfully",
  "data": [
    {"filename": "img1.jpg", "path": "uploads/abc.jpg"},
    {"filename": "img2.jpg", "path": "uploads/def.jpg"}
  ]
}
```

## Error Responses

### Validation Error (422)
```json
{
  "detail": [
    {
      "loc": ["body", "email"],
      "msg": "value is not a valid email address",
      "type": "value_error"
    }
  ]
}
```

### Unauthorized (401)
```json
{
  "detail": "Invalid credentials"
}
```

### Not Found (404)
```json
{
  "detail": "User not found"
}
```

### Conflict (409)
```json
{
  "detail": "Email already registered"
}
```
