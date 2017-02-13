import * as types from '../../mutation-types'

const state = {
  tasks: []
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
