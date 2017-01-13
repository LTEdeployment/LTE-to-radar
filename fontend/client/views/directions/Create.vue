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
      this.addDirection({paramName: this.name, paramFile: this.file})
    },

    onFileChange (e) {
      console.log('onFileChange')
      let files = e.target.files || e.dataTransfer.files
      if (!files.length) {
        return
      }
      console.log('new file')
      this.file = files[0]
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
