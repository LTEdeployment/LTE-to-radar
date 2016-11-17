const User = require('../lib/mongo').User;

let pub = {};

// 注册一个用户
pub.create = function(user) {
  return User
    .create(user)
    .exec();
};

// 通过用户名获取用户信息
pub.getUserByName = function(name) {
  return User
    .findOne({
      name: name
    })
    .addCreatedAt()
    .exec();
}
module.exports = pub;
