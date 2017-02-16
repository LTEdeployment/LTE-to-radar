<template>
  <div>
    <div class="tile is-ancestor" v-for="(item, index) in directions.directions">
      <div class="tile is-parent is-8">
        <article class="tile is-child box">
          <div>
            <p class="title left">{{ getTitle(item) }}</p>
            <p class="right">{{ item.created_at }}</p>
          </div>
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
    <tabs type="toggle" v-on:setTabsIndex="setPage" :selectedIndex="directions.page - 1">
      <tab-pane :label="item + ''" v-for="item in pages"></tab-pane>
    </tabs>
  </div>
</template>

<script>
import { Collapse, Item as CollapseItem } from 'vue-bulma-collapse'
import { mapGetters, mapActions, mapMutations } from 'vuex'
import Chart from '../../components/Chartjs'
import Tooltip from 'vue-bulma-tooltip'
import * as types from '../../store/mutation-types'
import Slider from 'vue-bulma-slider'
// 使用 vue-bulma-tabs 作为分页
import { Tabs, TabPane } from '../../components/pagination'

export default {
  components: {
    Collapse,
    CollapseItem,
    Chart,
    Tooltip,
    Slider,
    Tabs,
    TabPane
  },

  computed: {
    ...mapGetters({
      directions: 'directions'
    }),

    per () {
      return this.value + ''
    },

    pages () {
      let pageAmount = this.amount / 10
      if (this.amount % 10) {
        pageAmount += 1
      }
      let pages = []
      for (let i = 1; i <= pageAmount; i++) {
        pages.push(i)
      }
      return pages
    }
  },

  mounted () {
    if (!this.directions.directions || this.directions.directions.length === 0 || this.directions.page === 0) {
      this.getDirectionsList({ page: this.directions.page })
    }
    this.$http.get('http://computebackend.webdev.com/api/directions/amount')
      .then(function (response) {
        if (response.body.code !== 0) {
          console.log('error' + response.body.message)
          return
        }
        this.amount = response.body.data
      }, function (error) {
        console.log('error' + error)
      })
  },

  data () {
    return {
      amount: 0,
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
      if (!item.finished) {
        return item.name + '（未解析）'
      }
      return item.name
    },

    update (index) {
      this.value = Number(index)
    },

    setPage (page) {
      if (this.directions.page === page) {
        return
      }
      this.setStorePage(page)
      console.log(this.directions.page)
      this.getDirectionsList({ page: this.directions.page })
    },

    ...mapMutations({
      setStorePage: types.UPDATE_DIRECTIONS_PAGE
    }),

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
.left {
  float: left;
  text-align: left;
}
.right {
  float: right;
  text-align: right;
}
</style>
