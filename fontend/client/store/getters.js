const pkg = state => state.pkg
const app = state => state.app
const device = state => state.app.device
const sidebar = state => state.app.sidebar
const effect = state => state.app.effect
const menuitems = state => state.menu.items
const user = state => state.user
const modalData = state => state.modalData

const componententry = state => {
  return state.menu.items.filter(c => c.name === 'Components')[0]
}

export {
  pkg,
  app,
  device,
  sidebar,
  effect,
  menuitems,
  user,
  modalData,
  componententry
}
