# GEMINI.md - Project Context for AntoYogaAMM

## Project Overview
**AntoYogaAMM** is a web application for Antonine Rochet, specializing in Yoga Iyengar (Fontainebleau and Larchant), guided mountain activities (accompagnatrice en montagne), and Yoga & Trail running.

The project is built using:
- **Framework:** Nuxt 4 (Version 4.2.1)
- **UI Framework:** Nuxt UI 4 (Version 4.2.1), which includes Tailwind CSS.
- **Content Management:** Nuxt Content 3 (Version 3.8.2) for blogging.
- **Image Optimization:** Nuxt Image.
- **Styling:** Tailwind CSS with Nuxt UI components.
- **Language:** Primary content is in French (`fr`).

## Project Structure
Following Nuxt 4 conventions:
- `app/`: Contains the main application code (pages, components, layouts, assets).
- `content/`: Markdown files for the blog.
- `public/`: Static assets like images and icons.
- `app/pages/`: Route-based views.
- `app/components/`: Reusable Vue components.
- `app/layouts/`: Page layouts (e.g., `default.vue`, `home.vue`).

## Building and Running
The following scripts are defined in `package.json`:

- **Install dependencies:** `npm install`
- **Start development server:** `npm run dev`
- **Build for production:** `npm run build`
- **Static site generation:** `npm run generate`
- **Preview production build:** `npm run preview`
- **Nuxt prepare:** `npm run postinstall`

## Development Conventions
- **Language:** Code comments and documentation should follow project context (French/English), while UI text is in French.
- **Component Styling:** Use Nuxt UI 4 components and Tailwind CSS for custom styling.
- **Content:** Blog posts are managed in `content/blog/` as Markdown files with specific metadata (title, description, image, date).
- **TypeScript:** The project uses TypeScript.
- **Nuxt 4:** Adhere to Nuxt 4 directory structures and composables.
- **Responsive Design:** Mobile-first approach using Tailwind's utility classes.
