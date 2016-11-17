import { lazyLoading } from './lazyLoading'

export default {
  name: '计算任务',
  path: '/events',
  meta: {
    icon: 'fa-bar-chart-o',
    expanded: false
  },
  component: lazyLoading('events', true),

  children: [
    {
      name: '新建任务',
      path: 'create',
      component: lazyLoading('events/Create')
    }
  ]
}
