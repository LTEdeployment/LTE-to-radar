import * as types from '../../mutation-types'

const state = {
  directions: [],
  page: 1
}

const mutations = {
  [types.UPDATE_DIRECTIONS] (state, directions) {
    state.directions = JSON.parse(directions)
  },
  [types.UPDATE_DIRECTIONS_PAGE] (state, page) {
    state.page = page
  }
}

export default {
  state,
  mutations
}
