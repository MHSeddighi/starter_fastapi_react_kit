export interface LoginRequest {
  username: string
  password: string
}

export interface RegisterRequest {
  email: string
  username: string
  password: string
  full_name?: string
}

export interface User {
  id: number
  email: string
  username: string
  full_name: string | null
  is_active: boolean
  is_superuser: boolean
  created_at: string
}

export interface AuthResponse {
  success: boolean
  message: string
  data: {
    access_token: string
    token_type: string
  }
}

export interface UserResponse {
  success: boolean
  data: User
}
