const path = require('path');
const sha1 = require('sha1');
const router = require('express').Router();
const UserModel = require('../models/users');
const checkNotLogin = require('../middlewares/check').checkNotLogin;

// POST /signup 用户注册
router.post('/', checkNotLogin, function(req, res, next) {
  let name = req.fields.name;
  let gender = req.fields.gender;
  let bio = req.fields.bio;
  let avatar = req.files.avatar.path.split(path.sep).pop();
  let password = req.fields.password;
  let repassword = req.fields.repassword;

  // 校验参数
  try {
    if (!(name.length >= 1 && name.length <= 10)) {
      throw new Error('名字请限制在 1-10 个字符');
    }
    if (!(bio.length >= 1 && bio.length <= 30)) {
      throw new Error('个人简介请限制在 1-30 个字符');
    }
    if (password.length < 6) {
      throw new Error('密码至少 6 个字符');
    }
  } catch (e) {
    return res.redirect('/signup');
  }

  // 明文密码加密
  password = sha1(password);

  // 待写入数据库的用户信息
  let user = {
    name: name,
    password: password,
    bio: bio
  };
  // 用户信息写入数据库
  UserModel
    .create(user)
    .then(function(result) {
      // 此 user 是插入 mongodb 后的值，包含 _id
      user = result.ops[0];
      // 将用户信息存入 session
      delete user.password;
      req.session.user = user;
      res.redirect('/posts');
    })
    .catch(function(e) {
      // 用户名被占用则跳回注册页，而不是错误页
      if (e.message.match('E11000 duplicate key')) {
        return res.redirect('/signup');
      }
      next(e);
    });
});

module.exports = router;
