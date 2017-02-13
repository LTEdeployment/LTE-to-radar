import Vue from 'vue'
import Resource from 'vue-resource'
import NProgress from 'vue-nprogress'
import { sync } from 'vuex-router-sync'
import App from './App.vue'
import router from './router'
import store from './store'
import * as filters from './filters'
import { TOGGLE_SIDEBAR } from 'vuex-store/mutation-types'

// vue-resource 是 Vue.js 的一款插件，它可以通过 XMLHttpRequest 或 JSONP 发起请求并处理响应。
Vue.use(Resource)
// 进度条插件
Vue.use(NProgress)

// If your web server can't handle requests encoded as application/json,
// you can enable the emulateJSON option.
// This will send the request as application/x-www-form-urlencoded MIME type, as if from an normal HTML form.
Vue.http.options.emulateJSON = true

// 添加跨域支持
Vue.http.options.credentials = true
Vue.http.options.xhr = { withCredentials: true }

// 没看懂，先不管
sync(store, router)
const nprogress = new NProgress({ parent: '.nprogress-container' })
const { state } = store

// 全局中间件
router.beforeEach((route, redirect, next) => {
  // 若是移动端，那么取消滚动条
  if (state.app.device.isMobile && state.app.sidebar.opened) {
    store.commit(TOGGLE_SIDEBAR, false)
  }
  next()
})

// filters 目录下定义的过滤器
Object.keys(filters).forEach(key => {
  Vue.filter(key, filters[key])
})

let paramsObj = {
  router,
  store,
  nprogress,
  // 对象展开运算符，将 App 对象展开然后作为 paramsObj 对象的属性
  ...App
}

const app = new Vue(paramsObj)
export { app, router, store }
