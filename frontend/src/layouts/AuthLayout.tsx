import { Outlet } from 'react-router-dom'
import { ThemeToggle } from '@/components/ThemeToggle'

export function AuthLayout() {
  return (
    <div className="min-h-screen flex items-center justify-center bg-muted/50 px-4">
      <div className="absolute top-4 right-4">
        <ThemeToggle />
      </div>
      <div className="w-full max-w-md">
        <div className="text-center mb-8">
          <h1 className="text-3xl font-bold tracking-tight">Hackathon Starter</h1>
          <p className="text-muted-foreground mt-2">Build your product, fast</p>
        </div>
        <Outlet />
      </div>
    </div>
  )
}
