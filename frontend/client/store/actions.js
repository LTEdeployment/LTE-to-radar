import * as types from './mutation-types'
import Vue from 'vue'

const BASE_API_URL = 'http://computebackend.webdev.com/api/'
// const BASE_API_URL = 'http://computebackend.xhinliang.com/api/'

export const addDirection = function ({
  commit
}, payload) {
  // 拼装表单
  let formData = new window.FormData()
  formData.append('name', payload.paramName)
  formData.append('direction', payload.paramFile)
  formData.append('description', payload.paramDescription)

  Vue.http
    .post(`${BASE_API_URL}directions/create`, formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      },
      xhr: {
        withCredentials: true
      }
    })
    .then(function (response) {
      if (response.body.code !== 0) {
        // server error
        payload.onFail(response.body.message)
        return
      }
      payload.onSuccess('成功')
    }, function (error) {
      // network error
      payload.onFail('error ' + error)
    })
}

export const userLogin = ({
  commit
}, payload) => {
  console.log(`action login: ${payload.email} ${payload.password}`)
  Vue.http
    .post(`${BASE_API_URL}user/signin`, {
      email: payload.email,
      password: payload.password
    }, {
      xhr: {
        withCredentials: true
      }
    })
    .then(function (response) {
      if (response.body.code === 401) {
        payload.onSuccess(response.body.message)
        commit(types.LOGIN, payload.email)
        payload.router.push('/')
        return
      }
      if (response.body.code !== 0) {
        payload.onFail(response.body.message)
        return
      }
      let email = response.body.data.email
      console.log(`user logined: ${email}`)
      commit(types.LOGIN, email)
      payload.onSuccess('成功')
      payload.router.push('/')
    }, function (error) {
      payload.onFail('error ' + error)
      console.log('error ' + error)
    })
}

export const showModal = ({
  commit
}, payload) => {
  console.log('show modal: ' + payload.title)
  commit(types.SHOW_MODAL, payload.title, payload.message)
}

export const dismissModal = ({
  commit
}, payload) => {
  commit(types.DISMISS_MODAL)
}

export const userCheck = ({
  commit
}, payload) => {
  Vue.http
    .get(`${BASE_API_URL}user/check`)
    .then(function (response) {
      if (response.body.code !== 0) {
        payload.router.push('/login')
        return
      }
      let email = response.body.data.email
      console.log(`user checked: ${email}`)
      commit(types.LOGIN, email)
    }, function (error) {
      console.log('error ' + error)
    })
}

export const getDirectionsList = ({
  commit
}, payload) => {
  let page = payload.page
  Vue.http
    .get(`${BASE_API_URL}directions/list/${page}`)
    .then(function (response) {
      commit(types.UPDATE_DIRECTIONS, response.body, page)
    }, function (error) {
      console.log('error: ' + error)
    })
}

export const getTasksList = ({
  commit
}, payload) => {
  let page = payload.page
  Vue.http
    .get(`${BASE_API_URL}tasks/list/${page}`)
    .then(function (response) {
      commit(types.UPDATE_TASKS, response.body, page)
    }, function (error) {
      console.log('error: ' + error)
    })
}

export const userLogout = ({
  commit
}, payload) => {
  Vue.http
    .get(`${BASE_API_URL}user/signout`)
    .then(function (response) {
      if (response.body.code !== 0) {
        return
      }
      console.log(`user logout`)
      commit(types.LOGOUT)
      payload.router.push('/login')
    }, function (error) {
      console.log('error' + error)
    })
}

export const userRegister = ({
  commit
}, payload) => {
  Vue.http
    .post(`${BASE_API_URL}user/signup`, {
      email: payload.email,
      password: payload.password,
      bio: payload.bio
    })
    .then(function (response) {
      if (response.body.code !== 0) {
        console.log('register error' + JSON.stringify(response.body))
        payload.onFail('' + response.body.message)
        return
      }
      commit(types.LOGIN, payload.email)
      payload.onSuccess('ok')
      payload.router.push('/')
    }, function (error) {
      console.log('error' + error)
      payload.onFail('' + error)
    })
}

export const toggleSidebar = ({
  commit
}, opened) => {
  commit(types.TOGGLE_SIDEBAR, opened)
}

export const toggleDevice = ({
  commit
}, device) => commit(types.TOGGLE_DEVICE, device)

export const expandMenu = ({
  commit
}, menuItem) => {
  if (menuItem) {
    menuItem.expanded = menuItem.expanded || false
    commit(types.EXPAND_MENU, menuItem)
  }
}

export const switchEffect = ({
  commit
}, effectItem) => {
  if (effectItem) {
    commit(types.SWITCH_EFFECT, effectItem)
  }
}
