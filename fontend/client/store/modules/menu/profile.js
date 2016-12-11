import { lazyLoading } from './lazyLoading'

export default {
  name: '用户',
  path: '/profile',
  meta: {
    icon: 'fa-bar-chart-o',
    expanded: false
  },
  component: lazyLoading('profile', true),

  children: [
    {
      name: '个人设置',
      path: 'settings',
      component: lazyLoading('profile/Settings')
    }
  ]
}
