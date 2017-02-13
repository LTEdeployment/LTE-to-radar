import { lazyLoading } from './lazyLoading'

export default {
  name: '表格',
  meta: {
    icon: 'fa-table',
    expanded: false
  },

  children: [
    {
      name: 'BasicTables',
      path: '/tables/basic',
      meta: {
        label: 'Basic Tables'
      },
      component: lazyLoading('tables/Basic')
    },
    {
      name: 'Handsontable',
      path: '/tables/handsontable',
      component: lazyLoading('tables/Handsontable')
    }
  ]
}
