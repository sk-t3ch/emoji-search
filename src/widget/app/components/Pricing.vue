<template>
  <v-card class="mx-auto elevation-12" color="rgb(0, 0, 0, 0.6)">
    <v-list-item class="py-3 px-6">
      <v-list-item-content>
        <v-list-item-title class="text-lg-h4 text-md-h5 text-h6 white--text">
          Pricing
        </v-list-item-title>
        <v-list-item-subtitle class="text-lg-h5 text-md-h6 text-subtitle-1 font-italic font-weight-light white--text">
          Get 100 FREE Credits at
          <a href="https://t3chflicks.org">T3chFlicks.org</a>
        </v-list-item-subtitle>
      </v-list-item-content>
    </v-list-item>
    <v-list-item v-for="endpoint in endpoints" :key="endpoint.path" class="mx-auto" link>
      <v-list-item-content color="secondary">
        <div>
          <v-btn text class="white--text">
            {{ endpoint.path }}
            <v-chip small color="accent" class="mx-2 white--text">
              {{ endpoint.method }}
            </v-chip>
          </v-btn>
          <v-chip small color="accent" class="my-2 white--text">
            {{ endpoint.credits }}
            {{ endpoint.credits > 1 ? "Credits" : "Credit" }}
          </v-chip>
        </div>
      </v-list-item-content>
    </v-list-item>
  </v-card>
</template>
<script>
export default {
  props: {
    endpoints: {
      type: Array,
      required: true
    }
  }
}
</script>
