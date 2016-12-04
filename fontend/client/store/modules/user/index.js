import * as types from './mutation-types'

const state = {
  user: {
    username: null
  }
}

const mutations = {
  [types.LOGIN] (state, user) {
    state.user = user
  }
}

export default {
  state,
  mutations
}
