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
import Message from 'vue-bulma-message'
import Vue from 'vue'

const MessageComponent = Vue.extend(Message)
const openMessage = (propsData = {
  title: '',
  message: '',
  type: '',
  direction: '',
  duration: 1500,
  container: '.messages'
}) => {
  return new MessageComponent({
    el: document.createElement('div'),
    propsData
  })
}

export default {
  components: {},

  beforeMount () {
    this.toggleSidebar(false)
  },

  mounted () {
    if (this.user.email) {
      console.log(`already logined, redirect.`)
      this.$router.push('/')
    }
  },

  activated () {
    console.log(`activated`)
  },

  beforeDestroy () {
    this.toggleSidebar(true)
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
      this.userLogin({email: this.email, password: this.password, router: this.$router, onSuccess: this.successMessage, onFail: this.failMessage})
    },

    goRegister () {
      this.$router.push('/register')
    },

    successMessage (message) {
      openMessage({
        title: '提示',
        type: 'success',
        message,
        showCloseButton: true
      })
    },

    failMessage (message) {
      openMessage({
        title: '提示',
        type: 'warning',
        message,
        showCloseButton: true
      })
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
