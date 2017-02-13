import { lazyLoading } from './lazyLoading'

export default {
  name: '计算任务',
  path: '/tasks',
  meta: {
    icon: 'fa-bar-chart-o',
    expanded: false
  },
  component: lazyLoading('tasks', true),

  children: [
    {
      name: '新建任务',
      path: 'create',
      component: lazyLoading('tasks/Create')
    },
    {
      name: '任务列表',
      path: 'list',
      component: lazyLoading('tasks/List')
    }
  ]
}
