<template>
  <v-menu
    transition="slide-y-transition"
    bottom
    :close-on-content-click="false"
    nudge-bottom="20"
    open-on-hover
    left
    style="z-index: 999999;"
  >
    <template #activator="{ on, attrs }">
      <v-btn
        small
        icon
        v-bind="attrs"
        v-on="on"
      >
        <v-icon>
          mdi-menu-down
        </v-icon>
      </v-btn>
    </template>
    <v-list>
      <v-list-item
        class="ma-0 pa-0"
      >
        <v-list-item-title class="pr-6 py-0">
          <v-switch v-model="$vuetify.theme.dark" class="ma-0 mt-2 float-right" small inset>
            <template #label>
              <v-icon>mdi-brightness-6</v-icon>
            </template>
          </v-switch>
        </v-list-item-title>
      </v-list-item>
      <v-list-item>
        <v-list-item-title>
          <v-btn small class="retro-button-accent float-right my-2 mr-1" :href="serviceRootDomain">
            {{ name }}
          </v-btn>
        </v-list-item-title>
      </v-list-item>
      <v-list-item>
        <v-list-item-title class="right">
          <v-btn small class="retro-button-main float-right my-2 mr-1" :href="t3chflicksRootDomain">
            T3chFlicks
          </v-btn>
        </v-list-item-title>
      </v-list-item>
    </v-list>
  </v-menu>
</template>
<script>
export default {
  props: {
    name: {
      type: String,
      required: true
    },
    serviceRootDomain: {
      type: String,
      required: true
    },
    t3chflicksRootDomain: {
      type: String,
      required: true
    }
  }
}
</script>
<style scoped>
.retro-button-accent{
  vertical-align: middle;
  user-select: none;
  font-size: 1rem;
  background: var(--v-accent-base) !important;
  color: var(--v-secondary-darken1) !important;
  border: 3px solid var(--v-secondary-base)!important;
  border-radius: 0;
  box-shadow: 1px 1px var(--v-secondary-base), 3px 3px var(--v-accent-base);
}

.retro-button-main{
  vertical-align: middle;
  user-select: none;
  font-size: 1rem;
  background: var(--v-primary-base) !important;
  color: var(--v-secondary-darken1) !important;
  border: 3px solid var(--v-secondary-base)!important;
  border-radius: 0;
  box-shadow: 1px 1px var(--v-secondary-base), 3px 3px var(--v-primary-base);
}
</style>
