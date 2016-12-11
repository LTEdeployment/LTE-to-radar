<template>
  <div class="content has-text-centered">
    <p>
      <img width="200" src="~assets/logo.svg" :alt="description">
    </p>

    <h1 class="is-title is-bold">{{ name.replace('-', ' ') }}</h1>

    <p>
      <strong>{{ description }}</strong>
    </p>
    <p>
      <a :href="author.url">作者主页</a>
    </p>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  data () {
    return this.$store.state.pkg
  },

  computed: mapGetters({
    sidebar: 'sidebar',
    user: 'user'
  }),

  mounted () {
    if (!this.user.email) {
      this.$router.push('/login')
    }
  }
}
</script>

<style lang="scss" scoped>
.is-title {
  text-transform: capitalize;
}
</style>
