<template>
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
</template>

<script>
import serviceConfig from '@/config/service.js'
import LandingPage from '~/components/LandingPage.vue'

export default {
  components: {
    LandingPage
  },
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
      t3chflicksRootDomain: serviceConfig.t3chflicksRootDomain,
      apiKey: 'abc123'
    }
  }
}
</script>
