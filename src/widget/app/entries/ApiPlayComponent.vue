<template>
  <v-app class="component">
    <v-main>
      <v-container fluid>
        <api-play
          :api-key="apiKey"
          :endpoints="serviceEndpoints"
          :service-api-domain="serviceApiDomain"
          :name="serviceName"
          :service-root-domain="serviceRootDomain"
          :t3chflicks-root-domain="t3chflicksRootDomain"
        />
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import Vue from 'vue'
import VueMeta from 'vue-meta'
import vuetify from '@/plugins/vuetify'
import JsonViewer from 'vue-json-viewer/ssr'
import serviceConfig from '@/config/service.js'

import 'vue-json-viewer/style.css'
import ApiPlay from '@/components/ApiPlay.vue'
Vue.use(JsonViewer)
Vue.use(VueMeta)

export default {
  vuetify,
  components: { ApiPlay },
  props: ['apiKey'],
  data () {
    return {
      serviceName: serviceConfig.name,
      serviceApiDomain: serviceConfig.serviceApiDomain,
      serviceRootDomain: serviceConfig.serviceRootDomain,
      t3chflicksRootDomain: serviceConfig.t3chflicksRootDomain,
      serviceEndpoints: serviceConfig.endpoints
    }
  },
  created () {
    if (process.browser) { this.initDarkMode() }
    const { set } = this.$meta().addApp('custom')
    set({
      link: [
        { rel: 'stylesheet', href: 'https://fonts.googleapis.com/css?family=Roboto:100,300,400,500,700,900&display=swap' },
        { rel: 'stylesheet', href: 'https://cdn.jsdelivr.net/npm/@mdi/font@4.x/css/materialdesignicons.min.css' }
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

.component >>> .v-application--wrap{
  min-height: auto;
}

.v-application--wrap {
  min-height: auto;
}
</style>
