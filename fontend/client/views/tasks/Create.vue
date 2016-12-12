<template>
<div>
  <div class="tile is-ancestor">
    <div class="tile is-parent is-6">
      <article class="tile is-child box">
        <h1 class="title">LTE 参数</h1>
        <div class="block">
          <label class="label">最大发射功率</label>
          <p class="control">
            <input class="input" v-model="paramLte.input_max_emit_power" type="text" placeholder="Text input">
          </p>
          <label class="label">发射频率</label>
          <p class="control">
            <input class="input" v-model="paramLte.input_max_emit_frequency" type="text" placeholder="Text input" value="">
          </p>
          <label class="label">天线高度</label>
          <p class="control">
            <input class="input" v-model="paramLte.input_antenna_height" type="text" placeholder="Text input" value="">
          </p>
          <label class="label">天线增益</label>
          <p class="control">
            <input class="input" v-model="paramLte.input_antenna_gain" type="text" placeholder="Text input" value="">
          </p>
          <label class="label">天线效率</label>
          <p class="control">
            <input class="input" v-model="paramLte.input_antenna_ratio" type="text" placeholder="Text input" value="">
          </p>
          <label class="label">噪声系数</label>
          <p class="control">
            <input class="input" v-model="paramLte.input_noise_figure" type="text" placeholder="Text input" value="">
          </p>
          <label class="label">馈线损耗</label>
          <p class="control">
            <input class="input" v-model="paramLte.input_feeder_loss" type="text" placeholder="Text input" value="">
          </p>
          <label class="label">基站带宽</label>
          <p class="control">
            <input class="input" v-model="paramLte.input_station_wide" type="text" placeholder="Text input" value="">
          </p>
          <h3 class="title">用户参数</h3>
          <label class="label">最大发射功率</label>
          <p class="control">
            <input class="input" v-model="paramUser.user_max_emit_power" type="text" placeholder="Text input" value="">
          </p>
          <label class="label">发射频率</label>
          <p class="control">
            <input class="input" v-model="paramUser.user_max_emit_frequency" type="text" placeholder="Text input" value="">
          </p>
          <label class="label">天线高度</label>
          <p class="control">
            <input class="input" v-model="paramUser.user_antenna_height" type="text" placeholder="Text input" value="">
          </p>
          <label class="label">天线增益</label>
          <p class="control">
            <input class="input" v-model="paramUser.user_antenna_gain" type="text" placeholder="Text input" value="">
          </p>
          <label class="label">天线效率</label>
          <p class="control">
            <input class="input" v-model="paramUser.user_antenna_ratio" type="text" placeholder="Text input" value="">
          </p>
          <label class="label">噪声系数</label>
          <p class="control">
            <input class="input" v-model="paramUser.user_noise_figure" type="text" placeholder="Text input" value="">
          </p>
        </div>
      </article>
    </div>

    <div class="tile is-parent is-6">
      <article class="tile is-child box">
        <h1 class="title">Radar 参数</h1>
        <div class="block">
          <label class="label">天线高度</label>
          <p class="control">
            <input class="input" v-model="paramRadar.radar_antenna_height" type="text" placeholder="Text input">
          </p>
          <label class="label">天线增益</label>
          <p class="control">
            <input class="input" v-model="paramRadar.radar_antenna_gain" type="text" placeholder="Text input" value="">
          </p>
          <label class="label">天线效率</label>
          <p class="control">
            <input class="input" v-model="paramRadar.radar_antenna_ratio" type="text" placeholder="Text input" value="">
          </p>
          <label class="label">噪声系数</label>
          <p class="control">
            <input class="input" v-model="paramRadar.radar_noise_figure" type="text" placeholder="Text input" value="">
          </p>
          <label class="label">馈线损耗</label>
          <p class="control">
            <input class="input" v-model="paramRadar.radar_feeder_loss" type="text" placeholder="Text input" value="">
          </p>
          <label class="label">天线仰角</label>
          <p class="control">
            <input class="input" v-model="paramRadar.radar_antenna_tilt" type="text" placeholder="Text input" value="">
          </p>
          <label class="label">干扰阀值</label>
          <p class="control">
            <input class="input" v-model="paramRadar.radar_interference_threshold" type="text" placeholder="Text input" value="">
          </p>
          <label class="label">雷达带宽</label>
          <p class="control">
            <input class="input" v-model="paramRadar.radar_wide" type="text" placeholder="Text input" value="">
          </p>
        </div>
      </article>
    </div>
  </div>

  <div class="tile is-ancestor">
    <div class="tile is-parent">
      <article class="tile is-child box">
        <h1 class="title">任务属性</h1>
        <div class="block">
          <div class="control is-horizontal">
            <div class="control-label">
              <label class="label">邮箱</label>
            </div>
            <div class="control is-grouped">
              <p class="control is-expanded">
                <input class="input" type="text" placeholder="邮箱">
              </p>
            </div>
          </div>
          <div class="control is-horizontal">
            <div class="control-label">
              <label class="label">邮件通知</label>
            </div>
            <div class="control">
              <div class="select is-fullwidth">
                <select>
                  <option>通知</option>
                  <option>不通知</option>
                </select>
              </div>
            </div>
          </div>
          <div class="control is-horizontal">
            <div class="control-label">
              <label class="label">备注</label>
            </div>
            <div class="control">
              <textarea class="textarea"></textarea>
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
      'taskCreate'
    ]),

    create () {
      console.log(`task create!`)
      this.taskCreate({paramLte: this.paramLte, paramUser: this.paramUser, paramRadar: this.paramRadar})
    }
  },

  data () {
    return {
      paramLte: {
        input_max_emit_power: 0,
        input_max_emit_frequency: 0,
        input_antenna_height: 0,
        input_antenna_gain: 0,
        input_antenna_ratio: 0,
        input_noise_figure: 0,
        input_feeder_loss: 0,
        input_station_wide: 0,
        input_direction: 0
      },
      paramUser: {
        user_max_emit_power: 0,
        user_max_emit_frequency: 0,
        user_antenna_height: 0,
        user_antenna_gain: 0,
        user_antenna_ratio: 0,
        user_noise_figure: 0,
        user_direction: 0
      },
      paramRadar: {
        radar_antenna_height: 0,
        radar_antenna_gain: 0,
        radar_antenna_ratio: 0,
        radar_noise_figure: 0,
        radar_feeder_loss: 0,
        radar_antenna_tilt: 0,
        radar_interference_threshold: 0,
        radar_wide: 0,
        radar_direction: 0
      }
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
