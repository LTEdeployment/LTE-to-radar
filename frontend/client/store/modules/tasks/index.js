import * as types from '../../mutation-types'

const state = {
  tasks: [],
  page: 1
}

const mutations = {
  [types.UPDATE_TASKS] (state, tasks) {
    state.tasks = tasks
  },
  [types.UPDATE_TASKS_PAGE] (state, page) {
    state.page = page
  }
}

export default {
  state,
  mutations
}
