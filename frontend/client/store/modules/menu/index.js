import * as types from '../../mutation-types'
import { lazyLoading } from './lazyLoading'
// import charts from './charts'
import tasks from './tasks'
import directions from './directions'
import profile from './profile'
// import uifeatures from './uifeatures'
// import components from './components'
// import tables from './tables'

/*
 * show: meta.label -> name
 * meta.label: display label
 * name: component name
 */
const state = {
  items: [
    {
      name: '登录',
      path: '/login',
      meta: {
        icon: 'fa-tachometer'
      },
      component: lazyLoading('login', true)
    },
    {
      name: '注册',
      path: '/register',
      meta: {
        icon: 'fa-tachometer'
      },
      component: lazyLoading('register', true)
    },
    // charts,
    directions,
    tasks,
    // uifeatures,
    // components,
    // tables,
    profile
  ]
}

const mutations = {
  [types.EXPAND_MENU] (state, menuItem) {
    if (menuItem.index > -1) {
      if (state.items[menuItem.index] && state.items[menuItem.index].meta) {
        state.items[menuItem.index].meta.expanded = menuItem.expanded
      }
    } else if (menuItem.item && 'expanded' in menuItem.item.meta) {
      menuItem.item.meta.expanded = menuItem.expanded
    }
  }
}

export default {
  state,
  mutations
}
