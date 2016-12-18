<template>
<div class="divbody">
  <div class="tile is-ancestor">
    <div class="tile is-parent is-3">
      <article class="tile is-child box">
        <h1 class="title" />
        <div class="block">
          <p class="control has-icon">
            <input class="input" v-model="email" type="email" placeholder="邮箱">
            <i class="fa fa-envelope"></i>
          </p>
          <p class="control has-icon">
            <input class="input" v-model="password" type="password" placeholder="密码">
            <i class="fa fa-lock"></i>
          </p>
          <p class="control has-icon">
            <input class="input" v-model="repassword" type="password" placeholder="重复密码">
            <i class="fa fa-lock"></i>
          </p>
          <p class="control has-icon">
            <input class="input" v-model="bio" type="text" placeholder="一句话简介">
            <i class="fa fa-lock"></i>
          </p>
          <p class="control">
            <button @click="register" class="button is-success">
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

  beforeMount () {
    this.toggleSidebar(false)
  },

  beforeDestroy () {
    this.toggleSidebar(true)
  },

  data () {
    return {
      email: '',
      password: '',
      repassword: '',
      bio: ''
    }
  },

  computed: mapGetters({
    sidebar: 'sidebar',
    user: 'user'
  }),

  methods: {
    ...mapActions([
      'toggleSidebar',
      'userRegister'
    ]),

    register () {
      this.userRegister({email: this.email, password: this.password, bio: this.bio, router: this.$router})
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
    margin-left: 0;
  }
}

div.tile {
  border: 0px solid black;
  margin: 0 auto;
  //width: 300px;
}
</style>
