<template>
<div class="divbody">
  <div class="tile is-ancestor">
    <div class="tile is-parent is-3">
      <article class="tile is-child box">
        <h1 class="title" />
        <div class="block">
          <p class="control has-icon">
            <input class="input" v-model="email" type="username" placeholder="邮箱">
            <i class="fa fa-envelope"></i>
          </p>
          <p class="control has-icon">
            <input class="input" v-model="password" type="password" placeholder="密码">
            <i class="fa fa-lock"></i>
          </p>
          <p class="control">
            <button @click="login" class="button is-success">
                登录
            </button>
          </p>
          <p class="control">
            <button @click="goRegister" class="button">
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
import { mapGetters, mapActions } from 'vuex'

export default {
  components: {},

  beforeMount () {
    this.toggleSidebar(false)
  },

  beforeDestroy () {
    this.toggleSidebar(true)
  },

  activated () {
    console.log(`activated`)
  },

  mounted () {
    console.log(`mounted`)
    if (this.user.email) {
      console.log(`already logined, redirect.`)
      this.$router.push('/')
    }
  },

  computed: mapGetters({
    sidebar: 'sidebar',
    user: 'user'
  }),

  data () {
    return {
      email: '',
      password: ''
    }
  },

  methods: {
    ...mapActions([
      'toggleSidebar',
      'userLogin'
    ]),

    login () {
      console.log(`email: ${this.email}, password: ${this.password}`)
      this.userLogin({email: this.email, password: this.password, router: this.$router})
    },

    goRegister () {
      this.$router.push('/register')
      // this.userLogout()
    }
  }
}
</script>

<style lang="scss">
@import '~bulma/sass/utilities/variables';
@import '~bulma/sass/utilities/mixins';

.button {
  width: 100%;
}

.divbody {
  @include mobile() {
    margin-left: 0px;
    padding-left: 0px;
  }
}

div.tile {
  border: 0px solid black;
  margin: 0 auto;
  //width: 300px;
}
</style>
