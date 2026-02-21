# Repository Guidelines

## Project Structure & Module Organization
Core app code lives in `app/`:
- `app/pages/` contains route-based Vue pages (`/yoga/*`, `/mountain/*`, `/blog`).
- `app/components/` contains reusable UI components (PascalCase filenames).
- `app/layouts/` defines layout shells (`default.vue`, `home.vue`).
- `app/assets/css/main.css` loads Tailwind CSS and Nuxt UI styles.

Content is managed with Nuxt Content in `content/blog/*.md` and typed by `content.config.ts`. Static assets are in `public/` (mostly `public/images/`). Treat `.nuxt/` and `node_modules/` as generated; do not edit them manually.

## Build, Test, and Development Commands
- `npm install`: install dependencies.
- `npm run dev`: start local dev server at `http://localhost:3000`.
- `npm run build`: create production build.
- `npm run preview`: preview the production build locally.
- `npm run generate`: generate a static version of the site.
- `npx nuxt typecheck`: run TypeScript checks before opening a PR.

## Coding Style & Naming Conventions
Use Vue 3 SFCs with `<script setup lang="ts">`. Follow existing style:
- 2-space indentation in `.vue`, `.ts`, and Markdown frontmatter blocks.
- Prefer single quotes in TypeScript.
- Components: PascalCase (example: `HeroSliderImg.vue`).
- Route/content filenames: lowercase kebab-case (example: `yoga-trail-running.md`).
- Keep copy and SEO metadata in French unless a page explicitly targets another language.

## Testing Guidelines
There is no automated test suite configured yet. For now, include manual verification in each PR:
- Check key routes: home, yoga pages, mountain pages, blog index, and one blog article.
- Validate responsive behavior (mobile menu and layout transitions).
- Run `npm run build` and `npx nuxt typecheck` before submission.

If adding automated tests, prefer Vitest for unit tests and Playwright for e2e, with `*.spec.ts` naming.

## Commit & Pull Request Guidelines
Recent history shows short, direct commit messages (often lowercase/French), e.g. `horaires`, `menu mobile`, `update ...`. Keep that style but make scope explicit when possible: `navigation: fix mobile switcher`.

PRs should include:
- A concise description of what changed and why.
- Affected routes/files.
- Before/after screenshots for UI changes (desktop + mobile).
- Manual test steps performed.
