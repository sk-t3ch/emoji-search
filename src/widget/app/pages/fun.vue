<template>
  <api-play
    :api-key="apiKey"
    :endpoints="serviceEndpoints"
    :service-api-domain="serviceApiDomain"
    :service-root-domain="serviceRootDomain"
    :name="serviceName"
    :t3chflicks-root-domain="t3chflicksRootDomain"
    :home="serviceApiDomain"
  />
</template>

<script>
import serviceConfig from '@/config/service.js'
import ApiPlay from '@/components/ApiPlay.vue'

export default {
  components: {
    ApiPlay
  },
  data () {
    return {
      apiKey: 'abc123',
      serviceName: serviceConfig.name,
      serviceApiDomain: serviceConfig.serviceApiDomain,
      t3chflicksRootDomain: serviceConfig.t3chflicksRootDomain,
      serviceRootDomain: serviceConfig.serviceRootDomain,
      serviceEndpoints: serviceConfig.endpoints
    }
  }
}
</script>
