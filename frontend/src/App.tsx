import { RouterProvider } from 'react-router-dom'
import { ThemeProvider, QueryProvider } from '@/providers'
import { router } from '@/routes'
import { Toaster } from '@/components/ui/sonner'
function App() {
  return (
    <ThemeProvider defaultTheme="system" storageKey="ui-theme">
      <QueryProvider>
        <RouterProvider router={router} />
        <Toaster richColors closeButton />
      </QueryProvider>
    </ThemeProvider>
  )
}

export default App

