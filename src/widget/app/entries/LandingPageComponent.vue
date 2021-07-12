<template>
  <v-app>
    <v-main>
      <landing-page
        :service-name="serviceName"
        :service-endpoints="serviceEndpoints"
        :wide="wide"
        :second="second"
        :features="features"
        :examples="examples"
        :use-link="useLink"
        :description="description"
        :api-key="apiKey"
        :service-api-domain="serviceApiDomain"
        :service-root-domain="serviceRootDomain"
        :t3chflicks-root-domain="t3chflicksRootDomain"
      />
    </v-main>
  </v-app>
</template>

<script>
import Vue from 'vue'
import VueMeta from 'vue-meta'
import vuetify from '@/plugins/vuetify'
import serviceConfig from '@/config/service.js'

import 'vue-json-viewer/style.css'
import LandingPage from '../components/LandingPage.vue'
Vue.use(VueMeta)

export default {
  vuetify,
  components: { LandingPage },
  data () {
    return {
      serviceName: serviceConfig.name,
      useLink: `${serviceConfig.t3chflicksRootDomain}/Using/${serviceConfig.slug}`,
      serviceEndpoints: serviceConfig.endpoints,
      description: serviceConfig.description,
      wide: `${serviceConfig.serviceRootDomain}/branding/coin.png`,
      second: `${serviceConfig.serviceRootDomain}/branding/apiPlay.png`,
      examples: serviceConfig.examples,
      features: serviceConfig.features,
      serviceApiDomain: serviceConfig.serviceApiDomain,
      serviceRootDomain: serviceConfig.serviceRootDomain,
      t3chflicksRootDomain: serviceConfig.t3chflicksRootDomain
    }
  },
  created () {
    if (process.browser) { this.initDarkMode() }
    const { set } = this.$meta().addApp('custom')
    set({
      link: [
        { rel: 'stylesheet', href: 'https://fonts.googleapis.com/css?family=Roboto:100,300,400,500,700,900&display=swap' },
        { rel: 'stylesheet', href: 'https://cdn.jsdelivr.net/npm/@mdi/font@4.x/css/materialdesignicons.min.css' }
      ],
      title: 'Medium To MarkDown T3chFlicks',
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' }

      ]
    })
  },
  methods: {
    initDarkMode () {
      const darkMediaQuery = window.matchMedia('(prefers-color-scheme: dark)')

      darkMediaQuery.addEventListener('change', (e) => {
        this.$vuetify.theme.dark = !this.$vuetify.theme.dark
      })

      if (darkMediaQuery.matches) {
        console.log('change default light to dark theme')
        // need to set 0 sec timeout to set the dark more after mounted event, due to some bug in the framework
        setTimeout(() => (this.$vuetify.theme.dark = true), 0)
      }
    }
  }
}
</script>

<style scoped>
.widget-wrapper * {
  all: initial;
}
div {
  font-family: 'Roboto', sans-serif;
}
</style>
