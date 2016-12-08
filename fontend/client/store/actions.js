import * as types from './mutation-types'
import Vue from 'vue'

const BASE_API_URL = 'http://computebackend.xhinliang.com/api/'

export const userLogin = ({commit}, username, password) => {
  Vue.http
    .post(`${BASE_API_URL}user/signin`, {username, password})
    .then(function (response) {
      console.log(response)
    }, function (error) {
      console.log(error)
    })
}

export const userRegister = ({commit}, username, password, description) => {
  Vue.http.post(`${BASE_API_URL}user/signup`, {username, password, description})
    .then(function (response) {
      console.log(response.body)
    }, function (error) {
      console.log(error)
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
