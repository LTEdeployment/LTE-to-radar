import * as types from '../../mutation-types'

const state = {
  dismiss: true,
  title: '',
  message: ''
}

const mutations = {
  [types.SHOW_MODAL] (state, title, message) {
    state.title = title
    state.message = message
    state.dismiss = true
  },

  [types.DISMISS_MODAL] (state) {
    state.dismiss = false
  }
}

export default {
  state,
  mutations
}
