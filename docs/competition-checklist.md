# 🏆 Hackathon Competition Checklist

## Before the Hackathon

- [ ] Fork the starter kit repository
- [ ] Share the repo link with your team
- [ ] Ensure everyone has:
  - [ ] Git installed
  - [ ] Node.js 20+ installed
  - [ ] Python 3.11+ installed
  - [ ] Docker installed (optional)
  - [ ] Code editor with TypeScript/Python support
- [ ] Decide on your product idea
- [ ] Create a shared task board (GitHub Projects, Trello, etc.)
- [ ] Set up communication channel (Discord, Slack, etc.)

## Hour 0-1: Setup

- [ ] Clone the repository
- [ ] Run `make install` to install dependencies
- [ ] Copy `.env.example` to `.env`
- [ ] Start PostgreSQL and Redis (local or Docker)
- [ ] Run `make migrate` to create tables
- [ ] Run `make seed` for sample data
- [ ] Run `make dev` to verify everything works
- [ ] Everyone can see the app running locally

## Hour 1-2: Plan & Assign

- [ ] Define core data model (3-5 tables max)
- [ ] Assign roles:
  - [ ] Backend lead (APIs, database)
  - [ ] Frontend lead (UI, components)
  - [ ] Integrator (connecting frontend to backend)
  - [ ] Designer/PM (UI design, presentation)
- [ ] Create milestones for Day 1
- [ ] Document API contracts (what endpoints, what data)

## Hour 2-8: Build MVP

### Backend Team
- [ ] Create database models
- [ ] Create migrations: `make makemigrations`
- [ ] Create API endpoints (CRUD for core entities)
- [ ] Test endpoints with Swagger at `/docs`

### Frontend Team
- [ ] Create feature folders for core entities
- [ ] Build authentication pages (login/register)
- [ ] Build main dashboard layout
- [ ] Create API service files
- [ ] Build core feature pages

### Integration
- [ ] Connect frontend to backend APIs
- [ ] Test complete user flows
- [ ] Fix CORS/auth issues

## Hour 8-12: Core Features

- [ ] Build the main user-facing feature
- [ ] Implement file upload if needed
- [ ] Add form validation
- [ ] Handle error states
- [ ] Show loading states

## Hour 12-16: Polish

### Must Fix
- [ ] All critical bugs
- [ ] Broken navigation flows
- [ ] 404 pages
- [ ] Error messages
- [ ] Auth redirects

### Should Fix (If Time)
- [ ] Mobile responsiveness
- [ ] Loading skeletons
- [ ] Empty states
- [ ] Dark mode support (free with shadcn/ui!)
- [ ] Form validation feedback

## Hour 16-20: Deploy

- [ ] Prepare environment variables for production
- [ ] Deploy backend (Render, Railway, etc.)
- [ ] Deploy frontend (Vercel, Netlify, etc.)
- [ ] Configure CORS for production
- [ ] Set up custom domain (if available)
- [ ] Test production deployment
- [ ] Verify API endpoints work in production

## Hour 20-22: Presentation Prep

- [ ] Create a demo script
- [ ] Prepare slides (3-5 slides max):
  - [ ] Problem statement
  - [ ] Solution
  - [ ] Demo screenshots/video
  - [ ] Architecture (simple diagram)
  - [ ] Team roles
- [ ] Practice demo flow (3 times minimum)
- [ ] Prepare backup plans:
  - [ ] Local version ready if deployment fails
  - [ ] Screenshots of working features
  - [ ] Video recording as last resort

## Hour 22-24: Final Checks

- [ ] Final deployment check
- [ ] README.md updated with product info
- [ ] Clean up console.log and debug code
- [ ] Get some rest before presentation

## Presentation Tips

### Structure (3-5 minutes)

1. **Problem** (30s) — What are you solving?
2. **Solution** (30s) — How does your product help?
3. **Demo** (2-3 min) — Show the working product
4. **Architecture** (30s) — Tech stack, one slide
5. **Team** (15s) — Who did what

### Demo Flow

- Start with a clean browser (incognito)
- Show login/register flow
- Demonstrate the core feature
- Show error handling (it's okay if things break!)
- End with a summary slide

### What Judges Look For

- **Does it work?** — A working simple product > a broken complex one
- **Is it useful?** — Clear value proposition
- **Is it well-designed?** — Clean UI, not fancy
- **Team collaboration** — Git history shows teamwork
- **Technical competence** — Clean code, good architecture

## Post-Hackathon

- [ ] Push final code to GitHub
- [ ] Archive the repository
- [ ] Write a post-mortem:
  - [ ] What went well?
  - [ ] What would you change?
  - [ ] What did you learn?
- [ ] Take a break!
