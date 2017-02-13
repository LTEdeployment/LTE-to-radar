import { lazyLoading } from './lazyLoading'

export default {
  meta: {
    label: '视觉',
    icon: 'fa-laptop',
    expanded: false
  },

  children: [
    {
      name: 'Buttons',
      path: '/buttons',
      component: lazyLoading('ui/Buttons')
    },
    {
      name: 'Form',
      path: '/form',
      component: lazyLoading('ui/Form')
    },
    {
      name: 'Typography',
      path: '/typography',
      component: lazyLoading('ui/Typography')
    },
    {
      name: 'Icons',
      path: '/icons',
      component: lazyLoading('ui/Icons')
    }
  ]
}
