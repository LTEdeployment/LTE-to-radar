import * as types from '../../mutation-types'

const state = {
  email: null
}

const mutations = {
  [types.LOGIN] (state, email) {
    state.email = email
  },

  [types.LOGOUT] (state) {
    state.email = null
  }
}

export default {
  state,
  mutations
}
