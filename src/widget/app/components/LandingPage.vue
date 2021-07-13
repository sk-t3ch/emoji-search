<template>
  <v-sheet id="scrolling-techniques-3" class="overflow-y-auto">
    <v-container fluid fill-height>
      <v-row justify="center">
        <v-col cols="12" class="mx-0 px-0">
          <v-card class="gradyOne pa-10">
            <v-row>
              <v-col xs="12" sm="12" md="6" class="py-12">
                <v-card-title
                  class="text-lg-h1 text-md-h2 text-sm-h2 text-h3 white--text"
                  style="overflow-wrap: break-word; word-break: break-word"
                >
                  {{ serviceName }}
                </v-card-title>
                <v-card-text class="text-body-1 white--text">
                  {{ description }}
                  <v-card class="mt-6 elevation-12" color="rgb(0, 0, 0, 0.6)">
                    <v-list-item class="px-auto">
                      <v-list-item-content>
                        <v-list-item-title class="subtitle-1 white--text">
                          Features
                        </v-list-item-title>
                      </v-list-item-content>
                    </v-list-item>
                    <v-list-item
                      v-for="(feature, feature_idx) in features"
                      :key="feature.name"
                      class="px-auto"
                    >
                      <v-list-item-content two-line>
                        <v-list-item-title class="text-body-1 font-weight-light white--text">
                          {{
                            feature.name
                          }}
                        </v-list-item-title>
                        <v-list-item-subtitle
                          v-for="(item, item_idx) in feature.items"
                          :key="'feature_' + feature_idx + '_item_' + item_idx"
                          class="py-1 white--text"
                        >
                          {{ item.text }}
                        </v-list-item-subtitle>
                      </v-list-item-content>
                    </v-list-item>
                  </v-card>
                </v-card-text>
              </v-col>
              <v-spacer />
              <v-col xs="12" sm="12" md="6" lg="6" class="pa-6">
                <v-btn
                  color="accent"
                  class="float-right elevation-4"
                  nuxt
                  fab
                  :href="useLink"
                >
                  USE
                </v-btn>
                <v-img :src="wide" contain />
              </v-col>
            </v-row>
          </v-card>
        </v-col>
      </v-row>
      <v-row
        v-if="companies"
        justify="space-around"
        class="my-1 grey lighten-2 px-8 py-6"
      >
        <v-img
          v-for="company in companies"
          :key="company.link"
          :src="company.link"
          max-height="180"
          max-width="300"
          contain
        />
      </v-row>
      <v-row justify="center">
        <v-col cols="12" class="mx-0 px-0">
          <v-card class="gradyTwo pa-10 pl-12">
            <v-row>
              <v-col sm="12" md="6" class="pa-12">
                <api-play
                  :api-key="apiKey"
                  :endpoints="serviceEndpoints"
                  :service-api-domain="serviceApiDomain"
                  :service-root-domain="serviceRootDomain"
                  :name="serviceName"
                  :t3chflicks-root-domain="t3chflicksRootDomain"
                />
              </v-col>
              <v-spacer />
              <v-col sm="12" md="6" class="pa-12">
                <v-spacer />
                <v-card class="ma-5 elevation-12" color="rgb(0, 0, 0, 0.6)">
                  <v-list-item class="px-auto">
                    <v-list-item-content>
                      <v-list-item-title class="subtitle-1 white--text">
                        Examples
                      </v-list-item-title>
                    </v-list-item-content>
                  </v-list-item>
                  <v-list-item
                    v-for="example in examples"
                    :key="example.link"
                    class="mx-auto"
                    link
                  >
                    <v-list-item-content color="secondary" class="text-body-1 font-weight-light white--text">
                      <favicon-link
                        :src="example.link"
                        :title="example.title"
                      />
                    </v-list-item-content>
                  </v-list-item>
                </v-card>
                <v-card-actions class="mt-6">
                  <v-spacer />
                  <v-btn
                    color="accent"
                    class="text-md-h3 text-h4 elevation-4"
                    nuxt
                    width="240"
                    height="240"
                    fab
                    :href="useLink"
                  >
                    USE
                  </v-btn>
                  <v-spacer />
                </v-card-actions>
                <v-spacer />
              </v-col>
            </v-row>
          </v-card>
        </v-col>
      </v-row>
      <v-row justify="center">
        <v-col cols="12" class="mx-0 px-0">
          <v-card class="gradyOne pa-10 pl-12">
            <pricing v-if="serviceEndpoints" :endpoints="serviceEndpoints" />
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-sheet>
</template>

<script>
import Pricing from './Pricing'
import FaviconLink from './FaviconLink'
import ApiPlay from './ApiPlay'

export default {
  components: {
    FaviconLink,
    Pricing,
    ApiPlay
  },
  props: {
    serviceName: {
      type: String,
      required: true
    },
    useLink: {
      type: String,
      required: true
    },
    description: {
      type: String,
      required: true
    },
    features: {
      type: Array,
      required: true
    },
    wide: {
      type: String,
      required: true
    },
    second: {
      type: String,
      required: true
    },
    serviceEndpoints: {
      type: Array,
      required: false
    },
    examples: {
      type: Array,
      required: false
    },
    companies: {
      type: Array,
      required: false
    },
    serviceApiDomain: {
      type: String,
      required: true
    },
    t3chflicksRootDomain: {
      type: String,
      required: true
    },
    serviceRootDomain: {
      type: String,
      required: true
    },
    apiKey: {
      type: String,
      required: false
    }
  },
  head () {
    return {
      title: this.serviceName,
      meta: [
        {
          hid: this.serviceName,
          name: this.serviceName,
          content: this.description
        }
      ]
    }
  }
}
</script>
<style scoped>
.gradyOne {
  background: linear-gradient(90deg, #dde0bd, #360639);
}
.gradyTwo {
  background: linear-gradient(90deg, #ff6c03 , #9a8c98);
}
</style>
