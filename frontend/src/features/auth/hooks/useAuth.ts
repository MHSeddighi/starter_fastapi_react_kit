import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query'
import { useNavigate } from 'react-router-dom'
import { toast } from 'sonner'

import { authApi } from '../services/auth.api'
import type { LoginRequest, RegisterRequest, User } from '../types'

export function useLogin() {
  const queryClient = useQueryClient()
  const navigate = useNavigate()

  return useMutation({
    mutationFn: (data: LoginRequest) => authApi.login(data),
    onSuccess: (response) => {
      localStorage.setItem('auth_token', response.data.access_token)
      queryClient.invalidateQueries({ queryKey: ['currentUser'] })
      toast.success('Login successful!')
      navigate('/')
    },
    onError: (error: any) => {
      const message = error.response?.data?.detail || 'Login failed'
      toast.error(message)
    },
  })
}

export function useRegister() {
  const navigate = useNavigate()

  return useMutation({
    mutationFn: (data: RegisterRequest) => authApi.register(data),
    onSuccess: () => {
      toast.success('Registration successful! Please login.')
      navigate('/login')
    },
    onError: (error: any) => {
      const message = error.response?.data?.detail || 'Registration failed'
      toast.error(message)
    },
  })
}

export function useCurrentUser() {
  return useQuery({
    queryKey: ['currentUser'],
    queryFn: async () => {
      const token = localStorage.getItem('auth_token')
      if (!token) return null
      const response = await authApi.getMe()
      return response.data as User
    },
    retry: false,
    staleTime: 5 * 60 * 1000,
  })
}

export function useLogout() {
  const queryClient = useQueryClient()
  const navigate = useNavigate()

  return () => {
    localStorage.removeItem('auth_token')
    queryClient.invalidateQueries({ queryKey: ['currentUser'] })
    queryClient.setQueryData(['currentUser'], null)
    toast.success('Logged out')
    navigate('/login')
  }
}
