'use strict';
const mongodb = require('../core/mongo');
const tool = require('../core/tool');
const bcrypt = require('bcrypt');

const MONGODB_COLLECTION = 'user';
const HASH_LENGTH = 12;

function User(username, password, email) {
  this.username = username;
  this.email = email;
  this.password = password;
  user.createTime = new Date();
}

User.prototype.hashPassword = function(callback) {
  // 先生成一个哈希盐
  bcrypt.genSalt(HASH_LENGTH, function(err, salt) {
    if (err) {
      return callback(err);
    }
    // 把生成的盐保存起来
    user.salt = salt;
    // 用生成的盐进行哈希
    bcrypt.hash(user.password, salt, function(err, hash) {
      if (err) {
        return callback(err);
      }
      user.password = hash;
      callback();
    });
  });
};

User.login = function(username, password, callback) {
  mongodb.open(function(err, db) {
    if (err) {
      return callback(err);
    }
    db.collection(MONGODB_COLLECTION, function(err, collection) {
      if (err) {
        mongodb.close();
        return callback(err, null);
      }
      collection.find({
        username
      }, function(err, result) {
        mongodb.close();
        User.validatePassword(password, result.salt, function(err, hash) {
          if (err) {
            return callback(err);
          }
          return callback(result);
        });
      });
    });
  });
};

User.validatePassword = function(password, salt, callbcak) {
  bcrypt.hash(password, salt, function(err, hash) {
    if (err) {
      return callbcak(err);
    }
    return callbcak(null, hash);
  });
};

User.prototype.save = function(callback) {
  let user = this;
  user.hashPassword(function() {
    mongodb.open(function(err, db) {
      if (err) {
        return callback(err);
      }
      db.collection(MONGODB_COLLECTION, function(err, collection) {
        if (err) {
          mongodb.close();
          return callback(err, null);
        }
        collection.insert(user, {
          safe: true
        }, function(err, result) {
          mongodb.close();
          if (err) {
            return callback(err);
          }
          callback(null, result.ops);
        });
      });
    });
  });
};

module.exports = User;
