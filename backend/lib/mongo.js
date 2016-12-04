const config = require('config-lite');
const Mongolass = require('mongolass');
const mongolass = new Mongolass();
const moment = require('moment');
const objectIdToTimestamp = require('objectid-to-timestamp');

mongolass.connect(config.mongodb);

// 根据 id 生成创建时间 created_at
mongolass.plugin('addCreatedAt', {
  afterFind: function(results) {
    results.forEach(function(item) {
      item.created_at = moment(objectIdToTimestamp(item._id)).format('YYYY-MM-DD HH:mm');
    });
    return results;
  },
  afterFindOne: function(result) {
    if (result) {
      result.created_at = moment(objectIdToTimestamp(result._id)).format('YYYY-MM-DD HH:mm');
    }
    return result;
  }
});

exports.User = mongolass.model('User', {
  name: {
    type: 'string'
  },
  password: {
    type: 'string'
  },
  // 个人简介
  bio: {
    type: 'string'
  }
});
// 根据用户名找到用户，用户名全局唯一
exports.User.index({
  name: 1
}, {
  unique: true
}).exec();

exports.Task = mongolass.model('Task');