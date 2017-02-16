<template>
<div>
  <div class="tile is-ancestor">
    <div class="tile is-parent is-6">
      <article class="tile is-child box">
        <h1 class="title">LTE 参数</h1>
        <div class="block">
          <label class="label">系统带宽</label>
          <p class="control">
            <input class="input" v-model="paramLte.lte_bindwidth" type="text" placeholder="Text input" value="">
          </p>
          <label class="label">天线增益</label>
          <p class="control">
            <input class="input" v-model="paramLte.lte_antenna_gain" type="text" placeholder="Text input" value="">
          </p>
          <label class="label">天线损耗因子</label>
          <p class="control">
            <input class="input" v-model="paramLte.lte_antenna_loss_factor" type="text" placeholder="Text input" value="">
          </p>
          <label class="label">馈线损耗</label>
          <p class="control">
            <input class="input" v-model="paramLte.lte_feederline_factor" type="text" placeholder="Text input" value="">
          </p>
          <label class="label">噪声系数</label>
          <p class="control">
            <input class="input" v-model="paramLte.lte_noise_figure" type="text" placeholder="Text input" value="">
          </p>
          <label class="label">发射功率</label>
          <p class="control">
            <input class="input" v-model="paramLte.lte_power" type="text" placeholder="Text input">
          </p>
          <label class="label">天线高度</label>
          <p class="control">
            <input class="input" v-model="paramLte.lte_antenna_height" type="text" placeholder="Text input" value="">
          </p>
          <label class="label">发射频率</label>
          <p class="control">
            <input class="input" v-model="paramLte.lte_frequency" type="text" placeholder="Text input" value="">
          </p>
          <h3 class="title">用户参数</h3>
          <label class="label">天线增益</label>
          <p class="control">
            <input class="input" v-model="paramUser.user_antenna_gain" type="text" placeholder="Text input" value="">
          </p>
          <label class="label">天线损耗因子</label>
          <p class="control">
            <input class="input" v-model="paramUser.user_loss_factor" type="text" placeholder="Text input" value="">
          </p>
          <label class="label">噪声系数</label>
          <p class="control">
            <input class="input" v-model="paramUser.user_noise_figure" type="text" placeholder="Text input" value="">
          </p>
          <label class="label">天线高度</label>
          <p class="control">
            <input class="input" v-model="paramUser.user_antenna_height" type="text" placeholder="Text input" value="">
          </p>
          <label class="label">发射频率</label>
          <p class="control">
            <input class="input" v-model="paramUser.user_frequency" type="text" placeholder="Text input" value="">
          </p>
        </div>
      </article>
    </div>

    <div class="tile is-parent is-6">
      <article class="tile is-child box">
        <h1 class="title">Radar 参数</h1>
        <div class="block">
          <label class="label">天线增益</label>
          <p class="control">
            <input class="input" v-model="paramRadar.radar_antenna_gain" type="text" placeholder="Text input" value="">
          </p>
          <label class="label">天线损耗因子</label>
          <p class="control">
            <input class="input" v-model="paramRadar.radar_loss_factor" type="text" placeholder="Text input" value="">
          </p>
          <label class="label">雷达带宽</label>
          <p class="control">
            <input class="input" v-model="paramRadar.radar_bindwidth" type="text" placeholder="Text input" value="">
          </p>
          <label class="label">天线仰角</label>
          <p class="control">
            <input class="input" v-model="paramRadar.radar_antenna_tilt" type="text" placeholder="Text input" value="">
          </p>
          <label class="label">馈线损耗</label>
          <p class="control">
            <input class="input" v-model="paramRadar.radar_feeder_loss" type="text" placeholder="Text input" value="">
          </p>
          <label class="label">噪声系数</label>
          <p class="control">
            <input class="input" v-model="paramRadar.radar_noise_figure" type="text" placeholder="Text input" value="">
          </p>
          <label class="label">天线高度</label>
          <p class="control">
            <input class="input" v-model="paramRadar.radar_antenna_height" type="text" placeholder="Text input">
          </p>
        </div>
      </article>
    </div>
  </div>

  <div class="tile is-ancestor">
    <div class="tile is-parent">
      <article class="tile is-child box">
        <h1 class="title">公共参数</h1>
        <div class="block">
          <div class="control is-horizontal">
            <div class="control-label">
              <label class="label">ACIR最小值</label>
            </div>
            <div class="control is-grouped">
              <p class="control is-expanded">
                <input class="input" type="text" v-model="paramPublic.acir_min" placeholder="ACIR最小值">
              </p>
            </div>
          </div>
          <div class="control is-horizontal">
            <div class="control-label">
              <label class="label">ACIR最大值</label>
            </div>
            <div class="control is-grouped">
              <p class="control is-expanded">
                <input class="input" type="text" v-model="paramPublic.acir_max" placeholder="ACIR最大值">
              </p>
            </div>
          </div>
          <div class="control is-horizontal">
            <div class="control-label">
              <label class="label">ACIR步长</label>
            </div>
            <div class="control is-grouped">
              <p class="control is-expanded">
                <input class="input" type="text" v-model="paramPublic.acir_space" placeholder="ACIR步长">
              </p>
            </div>
          </div>
          <div class="control is-horizontal">
            <div class="control-label">
              <label class="label">基站间最近间距</label>
            </div>
            <div class="control is-grouped">
              <p class="control is-expanded">
                <input class="input" type="text" v-model="paramPublic.lte_min_d" placeholder="基站间最近间距">
              </p>
            </div>
          </div>
          <div class="control is-horizontal">
            <div class="control-label">
              <label class="label">隔离距离</label>
            </div>
            <div class="control is-grouped">
              <p class="control is-expanded">
                <input class="input" type="text" v-model="paramPublic.sR" placeholder="隔离距离">
              </p>
            </div>
          </div>
          <div class="control is-horizontal">
            <div class="control-label">
              <label class="label">仿真区域半径</label>
            </div>
            <div class="control is-grouped">
              <p class="control is-expanded">
                <input class="input" type="text" v-model="paramPublic.lR" placeholder="仿真区域半径">
              </p>
            </div>
          </div>
          <div class="control is-horizontal">
            <div class="control-label">
              <label class="label">每个下行用户占用的资源块数</label>
            </div>
            <div class="control is-grouped">
              <p class="control is-expanded">
                <input class="input" type="text" v-model="paramPublic.resource_block" placeholder="每个下行用户占用的资源块数">
              </p>
            </div>
          </div>
          <div class="control is-horizontal">
            <div class="control-label">
              <label class="label">路径损耗补偿因子</label>
            </div>
            <div class="control is-grouped">
              <p class="control is-expanded">
                <input class="input" type="text" v-model="paramPublic.compensation_factor" placeholder="路径损耗补偿因子">
              </p>
            </div>
          </div>
          <div class="control is-horizontal">
            <div class="control-label">
              <label class="label">USER 最大发射功率</label>
            </div>
            <div class="control is-grouped">
              <p class="control is-expanded">
                <input class="input" type="text" v-model="paramPublic.transpmax" placeholder="USER 最大发射功率">
              </p>
            </div>
          </div>
          <div class="control is-horizontal">
            <div class="control-label">
              <label class="label">是否采用三扇区</label>
            </div>
            <div class="control">
              <multiselect v-model="paramPublic.antenna_flag" :options="getOptionLabels('antenna_flag')" :allow-empty="false" ></multiselect>
            </div>
          </div>
          <div class="control is-horizontal">
            <div class="control-label">
              <label class="label">仿真场景规模</label>
            </div>
            <div class="control">
              <multiselect v-model="paramPublic.environment1" :options="getOptionLabels('environment1')" :allow-empty="false" ></multiselect>
            </div>
          </div>
          <div class="control is-horizontal">
            <div class="control-label">
              <label class="label">具体场景</label>
            </div>
            <div class="control">
              <multiselect v-model="paramPublic.environment2" :options="getOptionLabels('environment2')" :allow-empty="false" ></multiselect>
            </div>
          </div>
          <div class="control is-horizontal">
            <div class="control-label">
              <label class="label">链路方向</label>
            </div>
            <div class="control">
              <multiselect v-model="paramPublic.branch" :options="getOptionLabels('branch')" :allow-empty="false" ></multiselect>
            </div>
          </div>
          <div class="control is-horizontal">
            <div class="control-label">
              <label class="label">干扰源数</label>
            </div>
            <div class="control">
              <multiselect v-model="paramPublic.uti_or_multi" :options="getOptionLabels('uti_or_multi')" :allow-empty="false" ></multiselect>
            </div>
          </div>
        </div>
      </article>
    </div>

  <div class="tile is-ancestor">
    <div class="tile is-parent">
      <article class="tile is-child box">
        <h1 class="title">任务属性</h1>
        <div class="block">
          <div class="control is-horizontal">
            <div class="control-label">
              <label class="label">任务名</label>
            </div>
            <div class="control is-grouped">
              <p class="control is-expanded">
                <input class="input" type="text" v-model="name" placeholder="任务名">
              </p>
            </div>
          </div>
          <div class="control is-horizontal">
            <div class="control-label">
              <label class="label">基站方向图</label>
            </div>
            <div class="control">
              <multiselect v-model="lteDirection" :options="directionOptions" :custom-label="directionLabel" placeholder="Select one" label="name" track-by="name"></multiselect>
            </div>
          </div>
          <div class="control is-horizontal">
            <div class="control-label">
              <label class="label">用户方向图</label>
            </div>
            <div class="control">
              <multiselect v-model="userDirection" :options="directionOptions" :custom-label="directionLabel" placeholder="Select one" label="name" track-by="name"></multiselect>
            </div>
          </div>
          <div class="control is-horizontal">
            <div class="control-label">
              <label class="label">雷达方向图</label>
            </div>
            <div class="control">
              <multiselect v-model="radarDirection" :options="directionOptions" :custom-label="directionLabel" placeholder="Select one" label="name" track-by="name"></multiselect>
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
              <label class="label">描述</label>
            </div>
            <div class="control">
              <textarea class="textarea" v-model="description"></textarea>
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
import { mapGetters } from 'vuex'
import Multiselect from 'vue-multiselect'
import Message from 'vue-bulma-message'
import configJson from '../../../config/api.json'
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
  components: { Multiselect },

  computed: mapGetters({
    user: 'user'
  }),

  mounted () {
    this.$http.get(`${configJson['base_url']}api/directions/all`)
      .then(function (response) {
        if (response.body && response.body.code === 0) {
          this.directionOptions = response.body.data
          return
        }
        console.log('error: ' + response.body.message)
      }, function (err) {
        console.log('error: ' + JSON.stringify(err))
      })
  },

  methods: {
    create () {
      let pub = {}
      for (let key in this.paramPublic) {
        if (!this.paramPublic.hasOwnProperty(key)) {
          continue
        }
        if (Array.isArray(this.options[key])) {
          pub[key] = this.paramPublic[key] !== null ? this.getOptionIndex(key, this.paramPublic[key]) : 1
          continue
        }
        pub[key] = this.paramPublic[key]
      }
      let bundle = {
        lte: this.paramLte,
        user: this.paramUser,
        radar: this.paramRadar,
        pub,
        lteDirection: this.lteDirection.name,
        radarDirection: this.radarDirection.name,
        userDirection: this.userDirection.name
      }
      this.$http.post(`${configJson['base_url']}api/tasks/create`, {
        bundle,
        name: this.name,
        description: this.description
      })
      .then(function (response) {
        if (!response.body) {
          this.failMessage('服务器出错')
          return
        }
        if (response.body.code !== 0) {
          this.failMessage('创建任务失败: ' + response.body.message)
          return
        }
        this.successMessage('创建任务成功')
      }, function (err) {
        console.log('error: ' + JSON.stringify(err))
        this.failMessage('创建任务失败: ' + JSON.stringify(err))
      })
    },

    directionLabel ({ name, description }) {
      return `${name} — [${description}]`
    },

    getOptionIndex (label, key) {
      return this.options[label].indexOf(key) + 1
    },

    getOptionLabels (label) {
      return this.options[label]
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
      value: '',
      options: {
        antenna_flag: [ '三扇区', '全向天线' ],
        environment1: [ '大城市', '中小城市' ],
        environment2: [ '城市', '郊区', '农村', '丘陵', '开阔区' ],
        branch: [ '上行', '下行' ],
        uti_or_multi: [ '多源干扰', '单源干扰' ],
        lte_bindwidth: [ 5, 10, 15, 20 ]
      },
      lteDirection: { name: '未选择', description: '未选择' },
      radarDirection: { name: '未选择', description: '未选择' },
      userDirection: { name: '未选择', description: '未选择' },
      directionOptions: [
        { name: 'nothing', language: 'nothing' }
      ],
      name: '',
      description: '',
      paramPublic: {
        lte_min_d: 1000,
        sR: 120,
        lR: 121,
        antenna_flag: null,
        environment1: null,
        environment2: null,
        branch: '下行',
        uti_or_multi: null,
        acir_min: 6,
        acir_max: 8,
        acir_space: 0.4,
        resource_block: 1,
        compensation_factor: 0.8,
        transpmax: 23
      },
      paramLte: {
        lte_bindwidth: 20,
        lte_antenna_gain: 15,
        lte_antenna_loss_factor: 0.9,
        lte_feederline_factor: 0,
        lte_noise_figure: 5,
        lte_power: 43,
        lte_antenna_height: 30,
        lte_frequency: 3500
      },
      paramUser: {
        user_antenna_gain: 0,
        user_loss_factor: 0.9,
        user_noise_figure: 9,
        user_antenna_height: 1.5,
        user_frequency: 3500
      },
      paramRadar: {
        radar_antenna_gain: 34,
        radar_loss_factor: 0.9,
        radar_bindwidth: 20,
        radar_antenna_tilt: 0,
        radar_feeder_loss: 0,
        radar_noise_figure: 5,
        radar_antenna_height: 8
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
