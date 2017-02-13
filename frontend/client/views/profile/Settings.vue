<template>
  <div>
    <div class="tile is-ancestor">
      <div class="tile is-parent">
        <article class="tile is-child box">
          <h4 class="title">Table</h4>
          <table class="table">
            <thead>
              <tr>
                <th>Name</th>
                <th>Instrument</th>
                <th></th>
                <th></th>
              </tr>
            </thead>
            <tfoot>
              <tr>
                <th>Name</th>
                <th>Instrument</th>
                <th></th>
                <th></th>
              </tr>
            </tfoot>
            <tbody>
              <tr>
                <td>Misty Abbott</td>
                <td>Bass Guitar</td>
                <td class="is-icon">
                  <a href="#">
                    <i class="fa fa-twitter"></i>
                  </a>
                </td>
                <td class="is-icon">
                  <a href="#">
                    <i class="fa fa-instagram"></i>
                  </a>
                </td>
              </tr>
              <tr>
                <td>John Smith</td>
                <td>Rhythm Guitar</td>
                <td class="is-icon">
                  <a href="#">
                    <i class="fa fa-twitter"></i>
                  </a>
                </td>
                <td class="is-icon">
                  <a href="#">
                    <i class="fa fa-instagram"></i>
                  </a>
                </td>
              </tr>
              <tr>
                <td>Robert Mikels</td>
                <td>Lead Guitar</td>
                <td class="is-icon">
                  <a href="#">
                    <i class="fa fa-twitter"></i>
                  </a>
                </td>
                <td class="is-icon">
                  <a href="#">
                    <i class="fa fa-instagram"></i>
                  </a>
                </td>
              </tr>
            </tbody>
          </table>
          <a @click="logout" class="button is-danger is-outlined">
            <span class="icon">
            <i class="fa fa-times"></i>
            </span>
            <span>注销登录</span>
          </a>
        </article>
      </div>
    </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
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
      'userLogout'
    ]),

    logout () {
      this.userLogout({router: this.$router})
    }
  }
}
</script>

<style lang="scss">
.table-responsive {
  display: block;
  width: 100%;
  min-height: .01%;
  overflow-x: auto;
}
</style>
