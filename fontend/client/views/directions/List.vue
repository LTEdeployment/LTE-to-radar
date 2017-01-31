<template>
  <div>
    <div class="tile is-ancestor" v-for="(item, index) in directions.directions">
      <div class="tile is-parent is-8">
        <article class="tile is-child box">
          <h4 class="title"> {{ getTitle(item) }} </h4>
          <chart :type="'line'" :data="seriesData(item)" :options="options"></chart>
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

    getTitle (item) {
      if (!item.is_resolved) {
        return item.name + '（未解析）'
      }
      return item.name
    },

    update (index) {
      this.value = Number(index)
    },

    seriesData (item) {
      let data = {
        labels: [],
        datasets: [{
          data: [],
          label: '数据'
        }]
      }
      for (let i = 0; i <= 360; i++) {
        data.labels.push(i + '')
      }
      if (!item || !item.data) {
        return data
      }
      data.datasets[0].data = item.data[80]
      return data
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
