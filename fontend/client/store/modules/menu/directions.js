import { lazyLoading } from './lazyLoading'

export default {
  name: '方向图',
  path: '/directions',
  meta: {
    icon: 'fa-bar-chart-o',
    expanded: false
  },
  component: lazyLoading('directions', true),

  children: [
    {
      name: '新建方向图',
      path: 'create',
      component: lazyLoading('directions/Create')
    }
  ]
}
