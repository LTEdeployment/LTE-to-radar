const Task = require('../lib/mongo').Task

let pub = {}

pub.create = function (task) {
  return Task.create(task).exec()
}

// TODO need bugfix
// 不能根据条件查找
pub.getTaskById = function (id) {
  return Task
    .findOne({
      _id: id
    })
    .populate({
      path: 'author',
      model: 'User'
    })
    .addCreatedAt()
    .exec()
}

pub.getTasks = function (author, limit, page) {
  let query = {}
  if (author) {
    query.author = author
  }
  return Task
    .find(query)
    .skip((page - 1) * limit)
    .limit(limit)
    .populate({
      path: 'author',
      model: 'User'
    })
    .sort({
      _id: -1
    })
    .addCreatedAt()
    .exec()
}

pub.getAmount = function (author) {
  var query = {}
  if (author) {
    query.author = author
  }
  return Task
    .count(query)
    .exec()
}

module.exports = pub
