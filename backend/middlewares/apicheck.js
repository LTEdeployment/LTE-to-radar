module.exports = {
  checkLogin: function (req, res, next) {
    if (!req.session.user) {
      return res.json({
        code: -1,
        message: 'not signin yet'
      })
    }
    next()
  },

  checkNotLogin: function (req, res, next) {
    if (req.session.user) {
      return res.json({
        code: -1,
        message: 'already signin'
      })
    }
    next()
  }
}
