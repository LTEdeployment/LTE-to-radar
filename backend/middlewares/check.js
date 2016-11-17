let pub = {};
pub.checkLogin = function(req, res, next) {
  if (!req.session || !req.session.user) {
    return res.redirect('/signin');
  }
  next();
};

pub.checkNotLogin = function(req, res, next) {
  if (req.session && req.session.user) {
    return res.redirect('back'); //返回之前的页面
  }
  next();
};
module.exports = pub;
