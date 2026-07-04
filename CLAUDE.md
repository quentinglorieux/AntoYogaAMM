# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Marketing/content website for Antonine Rochet, who teaches Yoga Iyengar (Fontainebleau & Larchant) and works as a mountain guide (accompagnatrice en montagne, Yoga & Trail). Built with Nuxt 4, Nuxt UI 4 (Tailwind-based), and Nuxt Content 3 for the blog. All UI copy and content is in French (`lang="fr"`).

## Commands

- `npm run dev` — start dev server on port 3111 (not the Nuxt default 3000; see `nuxt.config.ts` and `package.json`)
- `npm run build` — production build
- `npm run generate` — static site generation
- `npm run preview` — preview a production build locally
- `npx nuxt typecheck` — run TypeScript checks; do this before considering a change done
- There is no automated test suite. Verify changes manually: check home, the yoga pages, the mountain pages, blog index + one article, and mobile menu/responsive behavior.

## Architecture

**Dual-theme site.** The app is really two sub-sites sharing one shell, keyed off the URL prefix:
- `/yoga/*` — orange accent color, teaching-focused pages
- `/mountain/*` — blue accent color, guiding-focused pages
- `/blog/*` — shared, theme-neutral

[TheNavigation.vue](app/components/TheNavigation.vue) is the single source of truth for this split: it derives `isMountainSection`/`isYogaSection` from `route.path.startsWith('/mountain')` and conditionally renders nav links, colors, and the cross-theme "switcher" link. When adding a new route, decide which section it belongs to and update the nav there — routes aren't declared in a central config, they're just files under `app/pages/`.

**Nuxt 4 srcDir layout.** App code lives under `app/` (pages, components, layouts, assets), not the repo root — this is the Nuxt 4 default (`srcDir: app/`). `app.vue` is a thin shell (`NuxtLayout` + `NuxtPage`); `layouts/default.vue` adds `TheNavigation`, `layouts/home.vue` is bare (used for the landing page's full-bleed hero).

**Known stale duplicate:** there is a `components/content/` directory at the repo root (outside `app/`) that duplicates `app/components/content/BlogCarousel.vue` and `BlogGallery.vue` with slightly different content — it is not inside `srcDir` and is not what Nuxt actually resolves. Treat `app/components/` as authoritative; don't edit the root-level `components/` copies (consider them for cleanup if you touch these files).

**Content collection.** Blog posts are Markdown files in `content/blog/*.md`, typed via a Zod schema in [content.config.ts](content.config.ts) (`title`, `description`, `image`, `date`, optional `head.meta`). Rendered by `app/pages/blog/index.vue` (listing) and `app/pages/blog/[...slug].vue` (article).

**Styling.** Nuxt UI primary color is `orange` (set in both `nuxt.config.ts` under `ui.colors.primary` and `app.config.ts` under `ui.primary` — keep these in sync if changed), with per-section overrides to blue for `/mountain/*`. Tailwind utility classes are used directly in templates; there's no separate design-token layer beyond `app/assets/css/main.css`.

**Images.** Static images live in `public/images/`. `scripts/remove_bg.py` is a standalone Python utility for background removal on source images before they're added to `public/images/` — it's not part of the build pipeline.

## Conventions (from AGENTS.md)

- Vue 3 SFCs with `<script setup lang="ts">`, 2-space indentation, single quotes in TS.
- Components: PascalCase filenames. Route/content filenames: lowercase kebab-case.
- Keep copy and SEO metadata in French unless a page explicitly targets another language.
- Commit messages in this repo are short and often in French/lowercase (e.g. `horaires`, `menu mobile`); when scope helps, prefix it (e.g. `navigation: fix mobile switcher`).
