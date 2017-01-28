<template>
  <div>
    <div class="tile is-ancestor" v-for="(item, index) in directions.directions">
      <div class="tile is-parent is-8">
        <article class="tile is-child box">
          <h4 class="title">方向图细节</h4>
          <chart :type="'line'" :data="seriesData[index]" :options="options"></chart>
        </article>
      </div>
      <div class="tile is-parent is-4">
        <article class="tile is-child box">
          <p>平面旋转角度</p>
          <div class="block">
            <p>
              <tooltip type="success" :label="per" placement="top" always>
                <span class="tooltip-value"></span>
              </tooltip>
              <slider type="success" size="normal" :value="value" :max="360" :step="1" is-fullwidth @change="update"></slider>
            </p>
            <p>
              <input class="input" type="number" v-model="value" min="0" max="360" input/>
            </p>
          </div>
        </article>
      </div>
    </div>
  </div>
</template>

<script>
import { Collapse, Item as CollapseItem } from 'vue-bulma-collapse'
import { mapGetters, mapActions } from 'vuex'
import Chart from 'vue-bulma-chartjs'
import Tooltip from 'vue-bulma-tooltip'
import Slider from 'vue-bulma-slider'

export default {
  components: {
    Collapse,
    CollapseItem,
    Chart,
    Tooltip,
    Slider
  },

  computed: {
    ...mapGetters({
      directions: 'directions'
    }),

    per () {
      return this.value + ''
    },

    seriesData () {
      let list = []
      for (var j = 0; j < this.directions.directions.length; j++) {
        let data = {
          labels: [],
          datasets: [{
            data: [],
            label: 'hehe',
            borderColor: this.backgroundColor.replace(/1\)$/, '.5)'),
            pointBackgroundColor: this.backgroundColor,
            backgroundColor: this.backgroundColor.replace(/1\)$/, '.5)')
          }],
          per: this.random(1, 361)
        }
        for (var i = 0; i <= 181; i++) {
          data.labels.push(' ')
          data.datasets[0].data.push(this.random(30, 140))
        }
        list.push(data)
      }
      return list
    }
  },

  mounted () {
    this.getDirectionsList({ page: this.page })
  },

  data () {
    return {
      page: 1,
      value: 1,
      options: {
        segmentShowStroke: false,
        tooltips: {
          mode: 'label'
        }
      },
      backgroundColor: 'rgba(31, 200, 219, 1)'
    }
  },

  methods: {
    ...mapActions([
      'getDirectionsList'
    ]),

    update (index) {
      this.value = Number(index)
    },

    random (min, max) {
      return Math.round(Math.random() * (max - min) + min)
    }
  }
}
</script>

<style lang="scss" scoped>
.tile.is-child {
  width: 100%;
}
.button {
  margin: 5px 0 0;
}
p {
  margin-bottom: 20px;
}
.tooltip-value {
  width: 100%;
}
</style>
