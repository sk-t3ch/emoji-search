<template>
  <div class="blogPost my-1">
    <a :href="src" target="new">
      <v-chip>
        <v-avatar class="mr-3">
          <img alt="Branding Icon" :src="'https://www.google.com/s2/favicons?domain=' + src">
        </v-avatar>
        {{ title }}
      </v-chip>
    </a>
  </div>
</template>

<script>
export default {
  props: {
    src: {
      type: String,
      default: ''
    },
    title: {
      type: String,
      default: ''
    }
  }
}
</script>
<style scoped>

.blogPost > img {
    width: 16px;
    height: 16px;
}

a {
    font-weight: 500;
    letter-spacing: 1.1;
}
</style>
