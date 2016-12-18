import * as types from './mutation-types'
import Vue from 'vue'

// const BASE_API_URL = 'http://computebackend.webdev.com/api/'
const BASE_API_URL = 'http://computebackend.xhinliang.com/api/'

export const userLogin = ({commit}, payload) => {
  console.log(`action login: ${payload.email} ${payload.password}`)
  Vue.http
    .post(`${BASE_API_URL}user/signin`, {email: payload.email, password: payload.password}, {xhr: {withCredentials: true}})
    .then(function (response) {
      let email = response.body.data.email
      console.log(`user logined: ${email}`)
      commit(types.LOGIN, email)
      payload.router.push('/')
    }, function (error) {
      console.log('error' + error)
    })
}

export const userCheck = ({commit}) => {
  Vue.http
    .get(`${BASE_API_URL}user/check`)
    .then(function (response) {
      let email = response.body.data.email
      console.log(`user checked: ${email}`)
      commit(types.LOGIN, email)
    }, function (error) {
      console.log('error' + error)
    })
}

export const userLogout = ({commit}, payload) => {
  Vue.http
    .get(`${BASE_API_URL}user/signout`)
    .then(function (response) {
      console.log(`user logout`)
      commit(types.LOGOUT)
      payload.router.push('/login')
    }, function (error) {
      console.log('error' + error)
    })
}

export const userRegister = ({commit}, email, password, bio) => {
  Vue.http
    .post(`${BASE_API_URL}user/signup`, {email, password, bio})
    .then(function (response) {
      console.log(response.body)
    }, function (error) {
      console.log('error' + error)
    })
}

export const taskCreate = ({commit}, payload) => {
  Vue.http
    .post(`${BASE_API_URL}tasks/create`, {bundle: payload})
    .then(function (response) {
      console.log(response.body)
    }, function (error) {
      console.log('error' + error)
    })
}

export const toggleSidebar = ({ commit }, opened) => {
  commit(types.TOGGLE_SIDEBAR, opened)
}

export const toggleDevice = ({ commit }, device) => commit(types.TOGGLE_DEVICE, device)

export const expandMenu = ({ commit }, menuItem) => {
  if (menuItem) {
    menuItem.expanded = menuItem.expanded || false
    commit(types.EXPAND_MENU, menuItem)
  }
}

export const switchEffect = ({ commit }, effectItem) => {
  if (effectItem) {
    commit(types.SWITCH_EFFECT, effectItem)
  }
}
