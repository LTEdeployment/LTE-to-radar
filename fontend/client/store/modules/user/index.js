import * as types from '../../mutation-types'

const state = {
  email: null
}

const mutations = {
  [types.LOGIN] (state, email) {
    state.email = email
  }
}

export default {
  state,
  mutations
}
