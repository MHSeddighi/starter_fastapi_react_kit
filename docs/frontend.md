# Frontend Guide

## Tech Stack

- **React 19** — UI library
- **Vite 8** — Build tool and dev server
- **TypeScript 6** — Type safety
- **Tailwind CSS 4** — Utility-first CSS
- **shadcn/ui** — Pre-built accessible components
- **React Router 7** — Client-side routing
- **TanStack Query 5** — Server state management
- **React Hook Form 7** — Form handling
- **Zod 4** — Schema validation
- **Axios** — HTTP client
- **Lucide React** — Icons
- **Sonner** — Toast notifications
- **react-dropzone** — File upload
- **Recharts** — Charts

## Project Structure

```
src/
├── app/           # App entry point
├── assets/        # Static assets
├── components/    # Shared components
│   └── ui/        # shadcn/ui components
├── features/      # Feature modules
│   └── auth/
│       ├── components/
│       ├── hooks/
│       ├── services/
│       ├── types.ts
│       └── index.ts
├── hooks/         # Shared hooks
├── layouts/       # Page layouts
├── lib/           # Utilities
├── pages/         # Route pages
├── providers/     # Context providers
├── routes/        # Route config
├── styles/        # Global styles
├── types/         # Shared types
└── utils/         # Helper functions
```

## Commands

```bash
npm run dev        # Start dev server
npm run build      # Build for production
npm run lint       # Lint code
npm run format     # Format code
```

## Adding shadcn Components

```bash
npx shadcn add button
npx shadcn add card
npx shadcn add dialog
# etc.
```

## Theme System

Three themes available: light, dark, system.

The theme is persisted in localStorage under `ui-theme`.

Usage:
```tsx
import { useTheme } from '@/providers'

function Component() {
  const { theme, setTheme } = useTheme()
  return <button onClick={() => setTheme('dark')}>Dark mode</button>
}
```

## Creating a New Feature

See the `auth` feature as a reference. Each feature should have:

```
features/your-feature/
├── components/    # Feature-specific components
├── hooks/         # Custom hooks for data fetching
├── services/      # API service functions
├── types.ts       # TypeScript interfaces/types
└── index.ts       # Public exports
```
