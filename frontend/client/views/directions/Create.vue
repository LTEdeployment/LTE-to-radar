<template>
<div>
  <div class="tile is-ancestor">
    <div class="tile is-parent">
      <article class="tile is-child box">
        <h1 class="title">新建方向图</h1>
        <div class="block">
          <div class="control is-horizontal">
            <div class="control-label">
              <label class="label">方向图名称</label>
            </div>
            <div class="control is-grouped">
              <p class="control is-expanded">
                <input v-model="name" class="input" type="text" placeholder="方向图名称">
              </p>
            </div>
          </div>
          <div class="control is-horizontal">
            <div class="control-label">
              <label class="label">方向图文件</label>
            </div>
            <div class="control is-grouped">
              <p class="control is-expanded">
                <input @change="onFileChange" type="file">
              </p>
            </div>
          </div>
          <div class="control is-horizontal">
            <div class="control-label">
              <label class="label">详细介绍</label>
            </div>
            <div class="control">
              <textarea v-model="description" class="textarea"></textarea>
            </div>
          </div>
          <div class="control is-horizontal">
            <div class="control-label">
              <label class="label"></label>
            </div>
            <div class="control">
              <button @click="create" class="button is-primary">提交</button>
              <button class="button is-link">检查</button>
            </div>
          </div>
        </div>
      </article>
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

  computed: mapGetters({
    user: 'user'
  }),

  mounted () {
    if (!this.user.email) {
      this.$router.push('/login')
    }
  },

  methods: {
    ...mapActions([
      'addDirection'
    ]),

    create () {
      this.addDirection({paramName: this.name, paramFile: this.file, paramDescription: this.description, onSuccess: this.successMessage, onFail: this.failMessage})
    },

    onFileChange (e) {
      let files = e.target.files || e.dataTransfer.files
      if (!files.length) {
        return
      }
      this.file = files[0]
    },

    successMessage (message) {
      openMessage({
        title: '提示',
        message,
        type: 'success',
        showCloseButton: true
      })
    },

    failMessage (message) {
      openMessage({
        title: '提示',
        message,
        type: 'warning',
        showCloseButton: true
      })
    }
  },

  data () {
    return {
      name: '',
      description: '',
      file: null
    }
  }
}
</script>

<style scoped>
.button {
  margin: 5px 0 0;
}

.control .button {
  margin: inherit;
}
</style>
