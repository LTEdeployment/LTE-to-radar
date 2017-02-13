<template>
<div class="divbody">
  <div class="tile is-ancestor">
    <div class="tile is-parent is-3">
      <article class="tile is-child box">
        <h1 class="title" />
        <div class="block">
          <p class="control has-icon">
            <input class="input" type="email" placeholder="邮箱">
            <i class="fa fa-envelope"></i>
          </p>
          <p class="control has-icon">
            <input class="input" type="password" placeholder="密码">
            <i class="fa fa-lock"></i>
          </p>
          <p class="control">
            <button class="button is-success">
                登录
            </button>
          </p>
          <p class="control">
            <button class="button">
                注册
            </button>
          </p>
        </div>
      </article>
    </div>
  </div>
</div>
</template>

<script>
import {
  mapGetters,
  mapActions
} from 'vuex'

export default {
  components: {},

  beforeMount () {
    this.toggleSidebar(false)
  },

  beforeDestroy () {
    this.toggleSidebar(true)
  },

  computed: mapGetters({
    sidebar: 'sidebar'
  }),

  methods: mapActions([
    'toggleSidebar'
  ])
}
</script>

<style lang="scss">
@import '~bulma';
.button {
  width: 100%;
}

.divbody {
  margin-left: -180px;

  @include mobile() {
    margin-left: 0;
  }
}

div.tile {
  border: 0px solid black;
  margin: 0 auto;
  width: 300px;
}
</style>
