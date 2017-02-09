<template>
  <div>
    <div class="tile is-ancestor" v-for="(item, index) in tasks.tasks">
      <div class="tile is-parent is-8">
        <article class="tile is-child box">
          <h4 class="title"> {{ getTitle(item) }} </h4>
          <chart :type="'line'" :data="seriesData(item)" :options="options"></chart>
        </article>
      </div>
      <div class="tile is-parent is-4">
        <article class="tile is-child box">
          <p>详细信息</p>
        </article>
      </div>
    </div>
    <tabs type="toggle" v-on:setTabsIndex="setPage">
      <tab-pane :label="item + ''" v-for="item in pages"></tab-pane>
    </tabs>
  </div>
</template>

<script>
import { Collapse, Item as CollapseItem } from 'vue-bulma-collapse'
import { mapGetters, mapActions } from 'vuex'
import Chart from 'vue-bulma-chartjs'
import Tooltip from 'vue-bulma-tooltip'
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
      tasks: 'tasks'
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
    this.getTasksList({ page: this.page })
    this.$http.get('http://computebackend.webdev.com/api/tasks/amount')
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
      page: 1,
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
      'getTasksList'
    ]),

    getTitle (item) {
      if (!item.finished) {
        return item.name + '（未完成）'
      }
      return item.name
    },

    update (index) {
      this.value = Number(index)
    },

    setPage (page) {
      if (this.page === page) {
        return
      }
      this.page = page
      this.getTasksList({ page: this.page })
    },

    seriesData (item) {
      let data = {
        labels: [],
        datasets: [{
          data: [],
          label: '干扰概率'
        }]
      }
      if (!item || !item.bundle || !item.result) {
        return data
      }
      let acirMin = item['bundle']['pub']['acir_min']
      let acirMax = item['bundle']['pub']['acir_max']
      let acirSpace = item['bundle']['pub']['acir_space']
      if (!acirMin || !acirMax || !acirSpace) {
        return data
      }
      acirMin = Number(acirMin)
      acirMax = Number(acirMax)
      acirSpace = Number(acirSpace)
      for (let acir = acirMin; acir <= acirMax; acir += acirSpace) {
        data.labels.push(acir.toFixed(2) + '')
      }
      data.datasets[0].data = item.result
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
