import * as types from '../../mutation-types'

const state = {
  directions: []
}

const mutations = {
  [types.UPDATE_DIRECTIONS] (state, directions) {
    state.directions = JSON.parse(directions)
  }
}

export default {
  state,
  mutations
}
