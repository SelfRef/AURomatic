// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-04-03',
  devtools: { enabled: true },
  app: {
    rootId: 'app'
  },
  css: [
    '~/assets/global.scss',
    '~/assets/themes/simple.scss'
  ],
  routeRules: {
    '/api/**': {
      proxy: {
        to: 'http://localhost:8000/api/**'
      }
    },
  }
})
