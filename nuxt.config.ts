// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: "2025-07-15",
  devtools: { enabled: true },
  modules: ["@nuxt/content", "@nuxt/image", "@nuxt/ui"],
  css: ['~/assets/css/main.css'],
  
  app: {
    head: {
      htmlAttrs: {
        lang: 'fr'
      },
      charset: 'utf-8',
      viewport: 'width=device-width, initial-scale=1',
      link: [
        { rel: 'canonical', href: 'https://antoninerochet.fr' }
      ]
    }
  },

  site: {
    url: 'https://antoninerochet.fr',
    name: 'Antonine Rochet - Yoga Iyengar & Accompagnatrice en Montagne',
    description: 'Cours de yoga Iyengar et randonnées guidées en montagne avec Antonine Rochet',
    defaultLocale: 'fr'
  }
});

