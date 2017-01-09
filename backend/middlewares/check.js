module.exports = {
  checkLogin: function (req, res, next) {
    if (!req.session.user) {
      req.flash('error', '未登录')
      return res.redirect('/user/signin')
    }
    next()
  },

  checkNotLogin: function (req, res, next) {
    if (req.session.user) {
      req.flash('error', '已登录')
      return res.redirect('back')
    }
    next()
  }
}
