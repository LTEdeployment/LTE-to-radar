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
      name: '上传方向图',
      path: 'create',
      component: lazyLoading('directions/Create')
    },
    {
      name: '已上传方向图',
      path: 'list',
      component: lazyLoading('directions/List')
    }
  ]
}
