var sha1 = require('sha1')
var express = require('express')
var router = express.Router()

var UserModel = require('../models/users')
var checkNotLogin = require('../middlewares/check').checkNotLogin
var checkLogin = require('../middlewares/check').checkLogin

// GET /signin 登录页
router.get('/signin', checkNotLogin, function (req, res, next) {
  res.render('signin')
})

// POST /signin 用户登录
router.post('/signin', checkNotLogin, function (req, res, next) {
  var email = req.body.email
  var password = req.body.password

  UserModel
    .getUserByEmail(email)
    .then(function (user) {
      if (!user) {
        req.flash('error', '用户不存在')
        return res.redirect('back')
      }
      // 检查密码是否匹配
      if (sha1(password) !== user.password) {
        req.flash('error', '用户名或密码错误')
        return res.redirect('back')
      }
      req.flash('success', '登录成功')
      // 用户信息写入 session
      delete user.password
      req.session.user = user
      // 跳转到主页
      res.redirect('/user/profile')
    })
    .catch(next)
})

router.get('/profile', checkLogin, function (req, res, next) {
  return res.render('profile')
})

// GET /signout 登出
router.get('/signout', checkLogin, function (req, res, next) {
  // 清空 session 中用户信息
  req.session.user = null
  req.flash('success', '登出成功')
  // 登出成功后跳转到主页
  res.redirect('/user/profile')
})

// GET /signup 注册页
router.get('/signup', checkNotLogin, function (req, res, next) {
  res.render('signup')
})

// POST /signup 用户注册
router.post('/signup', checkNotLogin, function (req, res, next) {
  var email = req.body.email
  var bio = req.body.bio
  var password = req.body.password
  var repassword = req.body.repassword

  // 校验参数
  try {
    if (!(email.length >= 1 && email.length <= 100)) {
      throw new Error('名字请限制在 1-100 个字符')
    }
    if (!(bio.length >= 1 && bio.length <= 30)) {
      throw new Error('个人简介请限制在 1-30 个字符')
    }
    if (password.length < 6) {
      throw new Error('密码至少 6 个字符')
    }
    if (password !== repassword) {
      throw new Error('两次输入密码不一致')
    }
  } catch (e) {
    req.flash('error', e.message)
    return res.redirect('/user/signup')
  }

  // 明文密码加密
  password = sha1(password)

  // 待写入数据库的用户信息
  var user = {
    email: email,
    password: password,
    bio: bio
  }
  // 用户信息写入数据库
  UserModel.create(user)
    .then(function (result) {
      // 此 user 是插入 mongodb 后的值，包含 _id
      user = result.ops[0]
      // 将用户信息存入 session
      delete user.password
      req.session.user = user
      // 写入 flash
      req.flash('success', '注册成功')
      // 跳转到首页
      res.redirect('/user/profile')
    })
    .catch(function (e) {
      // 用户名被占用则跳回注册页，而不是错误页
      if (e.message.match('E11000 duplicate key')) {
        req.flash('error', '用户名已被占用')
        return res.redirect('/user/signup')
      }
      next(e)
    })
})

module.exports = router
