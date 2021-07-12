<template>
  <v-card class="api-play">
    <v-row class="ma-0 pa-0">
      <v-spacer />
      <v-col cols="auto" class="ma-0 pa-0">
        <extra-tools :service-root-domain="serviceRootDomain" :t3chflicks-root-domain="t3chflicksRootDomain" :name="name" />
      </v-col>
    </v-row>
    <v-card-title class="mt-0 pt-0">
      <v-col cols="auto">
        <v-select
          v-if="(endpoints || []).length > 1"
          v-model="endpoint"
          :items="endpoints"
          dense
          rounded
          outlined
          :menu-props="{ auto: true, overflowY: true }"
          return-object
          item-text="path"
          @change="reset"
        >
          <template #selection="{ item }">
            {{ item.path }}
            <v-chip x-small color="accent" class="mx-2">
              {{ item.method }}
            </v-chip>
          </template>
        </v-select>
        <div v-else>
          <v-btn text>
            {{ endpoint.path }}
            <v-chip x-small color="accent" class="mx-2">
              {{ endpoint.method }}
            </v-chip>
          </v-btn>
        </div>
      </v-col>
      <v-spacer />
      <v-chip small color="accent" class="my-2">
        Cost: {{ endpoint.credits }}
      </v-chip>
    </v-card-title>
    <v-card-text v-if="inputSchema">
      <v-form ref="form" v-model="valid" lazy-validation>
        <div
          v-for="(parameter, parameterName) in inputSchema.properties"
          :key="parameterName"
          class="endpoint"
        >
          <div>
            <v-select
              v-if="parameter.enum"
              v-model.number="request[parameterName]"
              clearable
              :items="parameter.enum"
              class="parameter"
              :placeholder="parameter.example"
              :rules="[(v) => !!v || 'Item is required']"
              :label="
                parameterName +
                  '(' +
                  parameter.type +
                  ')' +
                  ' - ' +
                  parameter.description
              "
              outlined
              required
            />
            <v-text-field
              v-else-if="parameter.type == 'string'"
              v-model="request[parameterName]"
              clearable
              class="parameter"
              :placeholder="parameter.example"
              :label="
                parameterName +
                  '(' +
                  parameter.type +
                  ')' +
                  ' - ' +
                  parameter.description
              "
              :rules="[(v) => !!v || 'Item is required']"
              outlined
              required
            />
            <v-text-field
              v-else-if="parameter.type == 'number'"
              v-model.number="request[parameterName]"
              clearable
              class="parameter"
              :placeholder="parameter.example"
              :label="
                parameterName +
                  '(' +
                  parameter.type +
                  ')' +
                  ' - ' +
                  parameter.description
              "
              :rules="[(v) => !!v || 'Item is required']"
              outlined
              required
            />
          </div>
        </div>
        <v-btn
          small
          color="primary"
          dark
          outlined
          block
          :disabled="!valid"
          @click="submit"
          @keypress.enter="submit"
        >
          Submit ↵
        </v-btn>
      </v-form>
      <v-row class="mt-2 mr-1">
        <v-tabs
          v-model="resultsTab"
          color="accent"
          class="resultsTab caption mb-2"
          right
          small
          :show-arrows="$vuetify.breakpoint.smAndDown"
        >
          <v-tab href="#results" class="caption">
            Results
          </v-tab>
          <v-tab href="#inputSchema" class="caption">
            Input Schema
            <v-icon small color="yellow">
              mdi-lightning-bolt-outline
            </v-icon>
          </v-tab>
          <v-tab href="#outputSchema" class="caption">
            Output Schema
            <v-icon small color="yellow">
              mdi-lightning-bolt-outline
            </v-icon>
          </v-tab>
        </v-tabs>
      </v-row>
      <v-progress-linear v-if="loading" :loading="loading" />
      <v-scroll-y-transition>
        <div v-if="!loading" class="mt-6">
          <json-viewer
            :value="jsonData"
            :expand-depth="5"
            theme="my-awesome-json-theme"
            copyable
            boxed
            sort
          />
        </div>
      </v-scroll-y-transition>
    </v-card-text>
    <v-card-text v-else>
      <v-progress-circular :loading="isInitialising" indeterminate />
    </v-card-text>
  </v-card>
</template>

<script>
import ExtraTools from './ExtraTools'

export default {
  components: {
    ExtraTools
  },
  props: {
    name: {
      type: String,
      required: true
    },
    endpoints: {
      type: Array,
      required: true
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
  data () {
    return {
      endpoint: false,
      request: {},
      valid: true,
      loading: false,
      results: {},
      showSchema: true,
      resultsTab: 'outputSchema',
      inputSchema: null,
      outputSchema: null,
      isInitialising: true
    }
  },
  computed: {
    jsonData () {
      if (this.resultsTab === 'results') {
        return this.results
      } else if (this.resultsTab === 'inputSchema') {
        return this.inputSchema
      } else if (this.resultsTab === 'outputSchema') {
        return this.outputSchema
      } else {
        return {}
      }
    }
  },
  async created () {
    if (this.apiKey) {
      this.request.key = this.apiKey
    }
    if (this.endpoints.length > 0) {
      this.endpoint = this.endpoints[0]
    }
    await this.reset()
  },
  methods: {
    async reset () {
      try {
        const inputSchemaURL = `${this.serviceApiDomain}${this.endpoint.path}?${new URLSearchParams({ schema: 'input' })}`
        const requestInfo = {
          method: this.endpoint.method
        }
        this.inputSchema = await fetch(inputSchemaURL, requestInfo).then(resp => resp.json())
        const outputSchemaURL = `${this.serviceApiDomain}${this.endpoint.path}?${new URLSearchParams({ schema: 'output' })}`
        this.outputSchema = await fetch(outputSchemaURL, requestInfo).then(resp => resp.json())
        this.isInitialising = true
        this.request = Object.keys(this.inputSchema.properties || {}).reduce(
          (acc, curr) => {
            if (curr !== 'key') {
              acc[curr] = this.inputSchema.properties[curr].example
            } else {
              acc[curr] = this.apiKey
            }
            return acc
          },
          {}
        )
      } catch (err) {
        console.log(err)
      }
      this.isInitialising = false
    },
    async submit () {
      this.loading = true
      this.resultsTab = 'results'
      try {
        const response = await fetch(`${this.serviceApiDomain}${this.endpoint.path}`, {
          method: this.endpoint.method,
          body: JSON.stringify(this.request),
          headers: {
            'Content-Type': 'application/json'
          }
        }).then(resp => resp.json())
        console.log(response)
        this.results = response
      } catch (err) {
        console.log('ERROR: ', err)
        this.results = (err.response || { data: '' }).data
      }
      this.showSchema = false
      this.loading = false
    },
    getSchema () {
      return this.endpoint.outputs
    }
  }
}
</script>

<style lang="scss">
.v-select__selections input { display: none}

.parameter .v-label {
  color: var(--v-accent-base);
}

.my-awesome-json-theme {
  background: var(--v-secondary-base);
  white-space: nowrap;
  color: var(--v-invert-base);
  font-size: 14px;
  font-family: Consolas, Menlo, Courier, monospace;

  .jv-ellipsis {
    color: var(--v-invert-base);
    background-color: var(--v-secondary-base);
    display: inline-block;
    line-height: 0.9;
    font-size: 0.9em;
    padding: 0px 4px 2px 4px;
    border-radius: 3px;
    vertical-align: 2px;
    cursor: pointer;
    user-select: none;
  }
  .jv-button {
    color: #49b3ff;
  }
  .jv-key {
    color: var(--v-invert-base);
  }
  .jv-item {
    &.jv-array {
      color: var(--v-invert-base);
    }
    &.jv-boolean {
      color: #fc1e70;
    }
    &.jv-function {
      color: #067bca;
    }
    &.jv-number {
      color: #fc1e70;
    }
    &.jv-number-float {
      color: #fc1e70;
    }
    &.jv-number-integer {
      color: #fc1e70;
    }
    &.jv-object {
      color: var(--v-invert-base);
    }
    &.jv-undefined {
      color: #e08331;
    }
    &.jv-string {
      color: #42b983;
      word-break: break-word;
      white-space: normal;
    }
  }
  .jv-code {
    .jv-toggle {
      &:before {
        padding: 0px 2px;
        border-radius: 2px;
      }
      &:hover {
        &:before {
          background: var(--v-invert-base);
        }
      }
    }
  }
}
.jv-container .jv-code.boxed {
    max-height: 300px;
}
</style>
