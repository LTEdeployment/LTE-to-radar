import * as types from '../../mutation-types'

const state = {
  directions: [ 'fefe' ]
}

const mutations = {
  [types.UPDATE_DIRECTIONS] (state, directions) {
    state.directions = JSON.parse(directions)
    console.log(JSON.stringify(directions))
  }
}

export default {
  state,
  mutations
}
