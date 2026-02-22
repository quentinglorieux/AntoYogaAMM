// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: "2025-07-15",
  devtools: { enabled: true },
  modules: ["@nuxt/content", "@nuxt/image", "@nuxt/ui"],
  css: ['~/assets/css/main.css'],

  ui: {
    colors: {
      primary: 'red'
    }
  },


  app: {
    head: {
      htmlAttrs: {
        lang: 'fr'
      },
      charset: 'utf-8',
      viewport: 'width=device-width, initial-scale=1',
      link: [
        { rel: 'canonical', href: 'https://antoninerochet.fr' }
      ],
      meta: [
        { name: 'description', content: 'Cours de Yoga Iyengar à Fontainebleau et Larchant. Randonnées guidées, sorties montagne, Yoga & Trail sur le circuit des 25 bosses et séjours Yoga Rando avec Antonine Rochet.' }
      ]
    }
  },

});

