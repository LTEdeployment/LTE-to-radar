module.exports = {
  checkLogin: function checkLogin(req, res, next) {
    if (!req.session.user) {
      return res.json({
        code: -1,
        message: "not signin yet"
      });
    }
    next();
  },

  checkNotLogin: function checkNotLogin(req, res, next) {
    if (req.session.user) {
      return res.json({
        code: -1,
        message: "already signin"
      });
    }
    next();
  }
};
