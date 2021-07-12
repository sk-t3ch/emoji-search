import vuetifyOptions from './plugins/vuetify.options'

export default {
  target: 'static',
  env: {
    t3chflicksRootDomain: process.env.T3CHFLICKS_ROOT_DOMAIN,
    serviceRootDomain: process.env.SERVICE_ROOT_DOMAIN,
    serviceApiDomain: process.env.SERVICE_API_DOMAIN
  },
  head: {
    titleTemplate: '%s - app',
    title: 'app',
    htmlAttrs: {
      lang: 'en'
    },
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ]
  },

  css: [
  ],

  plugins: [
    { src: '~/plugins/json-viewer.js' }
  ],

  components: true,

  buildModules: [
    '@nuxtjs/eslint-module',
    ['@nuxtjs/vuetify', vuetifyOptions]
  ],

  customElements: {
    // analyzer: true,
    entries: [
      {
        async: true,
        name: 'ApiPlayComponent',
        tags: [
          {
            name: 'ApiPlayComponent',
            path: '@/entries/ApiPlayComponent',
            options () {
              return {
                props: ['apiKey']
              }
            }
          }
        ]
      },
      {
        name: 'LandingPageComponent',
        tags: [
          {
            name: 'LandingPageComponent',
            path: '@/entries/LandingPageComponent'
          }
        ]
      }
    ]
  },
  modules: [
    'nuxt-custom-elements'
  ],

  build: {
  }
}
