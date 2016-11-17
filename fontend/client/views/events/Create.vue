<template>
  <div>
    <div class="tile is-ancestor">
      <div class="tile is-parent is-6">
        <article class="tile is-child box">
          <h1 class="title">LTE 参数</h1>
          <div class="block">
            <label class="label">最大发射功率</label>
            <p class="control">
              <input class="input" type="text" placeholder="Text input">
            </p>
            <label class="label">发射频率</label>
            <p class="control has-icon has-icon-right">
              <input class="input is-success" type="text" placeholder="Text input" value="">
            </p>
            <label class="label">天线高度</label>
            <p class="control has-icon has-icon-right">
              <input class="input is-danger" type="text" placeholder="Text input" value="">
            </p>
            <label class="label">天线增益</label>
            <p class="control has-icon has-icon-right">
              <input class="input is-danger" type="text" placeholder="Text input" value="">
            </p>
            <label class="label">天线效率</label>
            <p class="control has-icon has-icon-right">
              <input class="input is-danger" type="text" placeholder="Text input" value="">
            </p>
            <label class="label">噪声系数</label>
            <p class="control has-icon has-icon-right">
              <input class="input is-danger" type="text" placeholder="Text input" value="">
            </p>
            <label class="label">馈线损耗</label>
            <p class="control has-icon has-icon-right">
              <input class="input is-danger" type="text" placeholder="Text input" value="">
            </p>
            <label class="label">基站带宽</label>
            <p class="control has-icon has-icon-right">
              <input class="input is-danger" type="text" placeholder="Text input" value="">
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
              <input class="input" type="text" placeholder="Text input">
            </p>
            <label class="label">天线增益</label>
            <p class="control has-icon has-icon-right">
              <input class="input is-success" type="text" placeholder="Text input" value="">
            </p>
            <label class="label">天线效率</label>
            <p class="control has-icon has-icon-right">
              <input class="input is-danger" type="text" placeholder="Text input" value="">
            </p>
            <label class="label">噪声系数</label>
            <p class="control has-icon has-icon-right">
              <input class="input is-danger" type="text" placeholder="Text input" value="">
            </p>
            <label class="label">馈线损耗</label>
            <p class="control has-icon has-icon-right">
              <input class="input is-danger" type="text" placeholder="Text input" value="">
            </p>
            <label class="label">天线仰角</label>
            <p class="control has-icon has-icon-right">
              <input class="input is-danger" type="text" placeholder="Text input" value="">
            </p>
            <label class="label">干扰阀值</label>
            <p class="control has-icon has-icon-right">
              <input class="input is-danger" type="text" placeholder="Text input" value="">
            </p>
            <label class="label">雷达带宽</label>
            <p class="control has-icon has-icon-right">
              <input class="input is-danger" type="text" placeholder="Text input" value="">
            </p>
          </div>
        </article>
      </div>
  </div>

    <div class="tile is-ancestor">
      <div class="tile is-parent">
        <article class="tile is-child box">
          <h1 class="title">用户参数</h1>
          <div class="block">
            <div class="control is-horizontal">
              <div class="control-label">
                <label class="label">最大发射功率</label>
              </div>
              <div class="control">
                <input class="input is-danger" type="text" placeholder="Text input" value="">
              </div>
            </div>
            <div class="control is-horizontal">
              <div class="control-label">
                <label class="label">发射频率</label>
              </div>
              <div class="control">
                <input class="input is-danger" type="text" placeholder="Text input" value="">
              </div>
            </div>
            <div class="control is-horizontal">
              <div class="control-label">
                <label class="label">天线高度</label>
              </div>
              <div class="control">
                <input class="input is-danger" type="text" placeholder="Text input" value="">
              </div>
            </div>
            <div class="control is-horizontal">
              <div class="control-label">
                <label class="label">天线增益</label>
              </div>
              <div class="control">
                <input class="input is-danger" type="text" placeholder="Text input" value="">
              </div>
            </div>
            <div class="control is-horizontal">
              <div class="control-label">
                <label class="label">天线效率</label>
              </div>
              <div class="control">
                <input class="input is-danger" type="text" placeholder="Text input" value="">
              </div>
            </div>
            <div class="control is-horizontal">
              <div class="control-label">
                <label class="label">噪声系数</label>
              </div>
              <div class="control">
                <input class="input is-danger" type="text" placeholder="Text input" value="">
              </div>
            </div>
            <div class="control is-horizontal">
              <div class="control-label">
                <label class="label"></label>
              </div>
              <div class="control">
                <button class="button is-primary">Submit</button>
                <button class="button is-link">Cancel</button>
              </div>
            </div>
          </div>
        </article>
      </div>
    </div>
</template>

<script>
import Cleave from 'vue-cleave'
import 'cleave.js/dist/addons/cleave-phone.cn'

export default {
  components: {
    Cleave
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
