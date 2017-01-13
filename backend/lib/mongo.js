var config = require('config-lite')
var Mongolass = require('mongolass')
var mongolass = new Mongolass()
var objectIdToTimestamp = require('objectid-to-timestamp')
var moment = require('moment')

mongolass.connect(config.mongodb)

// 根据 id 生成创建时间 created_at
mongolass.plugin('addCreatedAt', {
  afterFind: function (results) {
    results.forEach(function (item) {
      item.created_at = moment(objectIdToTimestamp(item._id)).format('YYYY-MM-DD HH:mm')
    })
    return results
  },
  afterFindOne: function (result) {
    if (result) {
      result.created_at = moment(objectIdToTimestamp(result._id)).format('YYYY-MM-DD HH:mm')
    }
    return result
  }
})

exports.User = mongolass.model('User', {
  email: {
    type: 'string'
  },
  password: {
    type: 'string'
  },
  bio: {
    type: 'string'
  }
})

// 根据用户名找到用户，用户名全局唯一
exports.User.index({
  email: 1
}, {
  unique: true
}).exec()

exports.Task = mongolass.model('Task')
// 任务名字全局唯一
exports.Task.index({
  name: 1
}, {
  unique: true
}).exec()

exports.Direction = mongolass.model('Direction')
// 方向图名字全局唯一
exports.Direction.index({
  name: 1
}, {
  unique: true
}).exec()
