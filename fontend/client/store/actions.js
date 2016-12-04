import * as types from './mutation-types'
import Vue from 'vue'

export const userLogin = ({commit}, username, password) => {
  Vue.http.get(``).then(function (response) {
    console.log(response.body)
  }, function (error) {
    console.log(error)
  })
}

export const userRegister = ({commit}, username, password) => {
  Vue.http.get(``).then(function (response) {
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
