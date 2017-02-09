import * as types from '../../mutation-types'

const state = {
  tasks: [ 'fefe' ]
}

const mutations = {
  [types.UPDATE_TASKS] (state, tasks) {
    state.tasks = tasks
  }
}

export default {
  state,
  mutations
}
