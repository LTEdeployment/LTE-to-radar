'use strict';

const tool = require('../core/tool');
const User = require('../models/user');
const app = require('../core/app');
const cache = require('../core/cache');
let pub = {};

pub.register = async(req, res) => {
  let username = req.body.username;
  let password = req.body.password;
  let email = req.body.email;
  let user = new User(username, password, email);
  user.save(function(err, ops) {
    if (err) {
      tool.l(err);
      return res.status(500);
    }
    req.session.uid = ops._id;
    return res.send(ops);
  });
};

pub.login = async(req, res) => {
  let username = req.body.username;
  let password = req.body.password;
  User.login(username, function(err, ops)) {
    // 拿到 uid，保存在 SESSION 中
    req.session.uid = ops._id;
    return res.send(ops);
  }
}

module.exports = pub;
