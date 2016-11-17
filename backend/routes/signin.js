const sha1 = require('sha1');
const router = require('express').Router();
const UserModel = require('../models/users');
const checkNotLogin = require('../middlewares/check').checkNotLogin;

// POST /signin 用户登录
router.post('/', checkNotLogin, function(req, res, next) {
  let name = req.body.name;
  let password = req.body.password;

  UserModel
    .getUserByName(name)
    .then(function(user) {
      if (!user) {
        return res.redirect('back');
      }
      // 检查密码是否匹配
      if (sha1(password) !== user.password) {
        return res.redirect('back');
      }
      // 用户信息写入 session
      delete user.password;
      req.session.user = user;
      // 跳转到主页
      res.redirect('/posts');
    })
    .catch(next);
});

module.exports = router;
