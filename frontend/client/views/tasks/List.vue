<template>
  <div>
    <div class="tile is-ancestor" v-for="(item, index) in seriesData">
      <div class="tile is-parent is-8">
        <article class="tile is-child box">
          <div>
            <p class="title left">{{ item.title }}</p>
            <p class="right">{{ item.created_at }}</p>
          </div>
          <chart :type="'line'" :data="item" :options="options"></chart>
        </article>
      </div>
      <div class="tile is-parent is-4">
        <article class="tile is-child box">
          <p>{{ '基站方向图：' + item.lteDirection }}</p>
          <p>{{ '用户方向图：' + item.userDirection }}</p>
          <p>{{ '雷达方向图：' + item.radarDirection }}</p>
          <p>{{ item.description }}</p>
        </article>
      </div>
    </div>
    <tabs type="toggle" v-on:setTabsIndex="setPage" :selectedIndex="this.tasks.page - 1">
      <tab-pane :label="item + ''" v-for="item in pages"></tab-pane>
    </tabs>
  </div>
</template>

<script>
import { Collapse, Item as CollapseItem } from 'vue-bulma-collapse'
import { mapGetters, mapActions, mapMutations } from 'vuex'
import Chart from '../../components/Chartjs'
import Tooltip from 'vue-bulma-tooltip'
import Slider from 'vue-bulma-slider'
import * as types from '../../store/mutation-types'
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
      tasks: 'tasks'
    }),

    seriesData () {
      if (this.tasks.tasks.length === 0) {
        return []
      }
      let list = []
      for (let item of this.tasks.tasks) {
        let data = {
          labels: [],
          datasets: [{
            data: [],
            label: '干扰概率'
          }]
        }
        data.title = item.finished ? item.name : item.name + '（未完成）'
        data.created_at = item.created_at
        if (!item || !item.bundle || !item.result) {
          console.log('item 不完整')
          console.log(JSON.stringify(item))
          list.push(data)
          continue
        }
        data.userDirection = item.bundle['userDirection']
        data.lteDirection = item.bundle['lteDirection']
        data.radarDirection = item.bundle['radarDirection']
        data.description = item.description
        let acirMin = item['bundle']['pub']['acir_min']
        let acirMax = item['bundle']['pub']['acir_max']
        let acirSpace = item['bundle']['pub']['acir_space']
        if (!acirMin || !acirMax || !acirSpace) {
          console.log('acir 不完整')
          console.log(JSON.stringify(item))
          list.push(data)
          continue
        }
        acirMin = Number(acirMin)
        acirMax = Number(acirMax)
        acirSpace = Number(acirSpace)
        for (let acir = acirMin; acir <= acirMax; acir += acirSpace) {
          data.labels.push(acir.toFixed(2) + '')
        }
        if (item.result) {
          data.datasets[0].data = item.result
        }
        list.push(data)
      }
      return list
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
    console.log(this.tasks.page)
    if (!this.tasks.tasks || this.tasks.tasks.length === 0) {
      this.getTasksList({ page: this.tasks.page })
    }
    this.$http.get('http://computebackend.webdev.com/api/tasks/amount')
      .then(function (response) {
        if (response.body.code !== 0) {
          console.log('error ' + response.body.message)
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
      'getTasksList'
    ]),

    ...mapMutations({
      setStorePage: types.UPDATE_TASKS_PAGE
    }),

    setPage (page) {
      if (this.tasks.page === page) {
        return
      }
      this.setStorePage(page)
      this.getTasksList({ page: this.tasks.page })
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
